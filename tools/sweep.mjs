import {readDirectoryProof} from "./read-directory-proof.mjs";
// node tools/sweep.mjs BASE_URL SEED [SQLITE_FILE] [--reflow-only] [chromium firefox webkit] > results.tsv
import assert from "node:assert/strict";
import {createHash} from "node:crypto";
import {readFileSync,readdirSync,statSync} from "node:fs";
import {dirname,join} from "node:path";
import {DatabaseSync} from "node:sqlite";
import {chromium, firefox, webkit} from "playwright";
import {parameters} from "../site/search-input.mjs";
import {recordMetadata, source} from "../site/record.mjs";

const queries = JSON.parse(readFileSync("site/queries.json"));
const args = JSON.parse(readFileSync("tools/sweep-inputs.json"));
for (const kind of Object.keys(queries)) {
  assert.ok(Object.hasOwn(args, kind), "Provide a test input for " + kind);
}
if (process.argv[2] === "--check-inputs") {
  console.log("Sweep inputs cover all " + Object.keys(queries).length + " query groups.");
  process.exit(0);
}

// Optional package measurements use the same installed browser engines.
if (["--compare-staging", "--module-pairs"].includes(process.argv[2])) {
  const {measure} = await import("./package-measurements.mjs");
  await measure(...process.argv.slice(2));
  process.exit(0);
}

const [base, seed, database = "build/rh.sqlite3", ...options] = process.argv.slice(2);
const reflowOnly = options.includes("--reflow-only");
const engines = options.filter(arg => arg !== "--reflow-only");
if (!base || !seed) throw Error("Usage: sweep.mjs BASE_URL SEED [SQLITE_FILE]");
const origin = new URL(base).origin;
const db = new DatabaseSync(database, {readOnly:true});
db.function("sample_key", {deterministic:true}, text =>
  createHash("sha256").update(seed).update("\0").update(text).digest("hex"));
const proof = readDirectoryProof();
const offset = db.prepare("SELECT value FROM summary WHERE metric='fts_declaration_offset'").get().value;
const select = (sql,...values) => db.prepare(sql).all(...values);

function distinct(rows, field, size) {
  const seen = new Set();
  const sample = rows.filter(row => !seen.has(row[field]) && seen.add(row[field])).slice(0,size);
  assert.equal(sample.length,size);
  return sample;
}
const cases = [];
function group(rows, category, make) {
  rows.forEach((row,i) => cases.push({...make(row), category, small:i % 10 === 0}));
}
for (const [pkg, size] of [["riemann-hypothesis",300],["mathlib",50]]) {
  const sql = "SELECT path FROM modules WHERE package=? ORDER BY ";
  const rows = distinct([...select(sql+"length(path) DESC,path LIMIT 20",pkg),
    ...select(sql+"sample_key(path),path LIMIT ?",pkg,size)], "path",size);
  group(rows,pkg,({path})=>({name:path,path,pkg,kind:"module"}));
}
// All mapped statements have a static module page, including the sample routes.
const siteDir = join(dirname(database),"preview");
const proofBytes = readFileSync(join(siteDir,"proof.json"),"utf8");
const hosted = await fetch(new URL("/proof.json",origin));
assert.ok(hosted.ok, "Cannot identify hosted build");
assert.equal((await hosted.json()).buildId, JSON.parse(proofBytes).buildId, "Hosted and local database builds differ");
const hostedQueries = await fetch(new URL("/queries.json",origin));
assert.ok(hostedQueries.ok && await hostedQueries.text() === readFileSync("site/queries.json","utf8"),
  "Hosted queries differ from the checkout");
const index = JSON.parse(readFileSync(join(siteDir,"informalizations.json")));
const capture = JSON.parse(readFileSync("reports/permission-statements/card-capture.json", "utf8"));
const publicationDate = new Intl.DateTimeFormat("en-GB", {dateStyle:"long", timeZone:"UTC"})
  .format(new Date(capture["index.html"].utc));
const permission = new Map(index.filter(r => r.writer === "Andrew O'Desky" && r.license === "with-permission")
  .map(r=>[r.module,statSync(join(siteDir,new URL(r.page).pathname,"index.html")).size]));
const linked = select(`SELECT m.path,m.package AS pkg FROM modules m JOIN informalizations i ON i.module=m.id
  WHERE i.writer=? AND i.license='with-permission' ORDER BY sample_key(m.path),m.path`, "Andrew O'Desky");
assert.equal(linked.length, permission.size);
const largest = [...linked].sort((a,b) => permission.get(b.path)-permission.get(a.path) ||
  Buffer.compare(Buffer.from(a.path),Buffer.from(b.path))).slice(0,5);
const pathsAlreadyVisited = new Set(cases.map(c => c.path));
const additional = distinct([...largest,...linked.filter(row=>!pathsAlreadyVisited.has(row.path))], "path",100);
group(additional, "statement-module", ({path,pkg})=>({
  name:path,path,pkg,kind:"module",pageBytes:permission.get(path),
  largestRank:largest.findIndex(row=>row.path===path)+1 || "",
}));
const framePath="src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean";
cases.push({category:"frame-width",kind:"module",name:framePath,path:framePath,pkg:"riemann-hypothesis",small:true});
const columns = "SELECT d.name,m.path,m.package AS pkg,d.start,d.end FROM declarations d JOIN modules m ON m.id=d.module";
const longestFiles = select("SELECT path FROM modules WHERE EXISTS (SELECT 1 FROM declarations WHERE module=modules.id) ORDER BY length(path) DESC,path LIMIT 20");
const fileRepresentatives = longestFiles.map(({path}) => db.prepare(columns+" WHERE m.path=? ORDER BY d.start,d.id LIMIT 1").get(path));
const declarations = distinct([
  ...select(columns+" ORDER BY length(d.name) DESC,d.name LIMIT 20"), ...fileRepresentatives,
  ...select(columns+" WHERE d.name GLOB '_private.*' ORDER BY sample_key(d.name),d.name LIMIT 20"),
  ...select(columns+" WHERE length(CAST(d.name AS blob))>length(d.name) ORDER BY sample_key(d.name),d.name LIMIT 20"),
  ...select(columns+" ORDER BY sample_key(d.name),d.name LIMIT 300"),
], "name",300);
group(declarations,"declaration", row=>({...row,kind:"declaration"}));
const searches = select("SELECT short FROM (SELECT DISTINCT short FROM shortnames WHERE short<>'') ORDER BY sample_key(short),short LIMIT 100");
group(searches,"search",({short})=>({name:short,kind:"search",match:"short"}));
for (const {short} of searches) {
  const hit = db.prepare("SELECT full,kind,ref,package FROM shortnames WHERE short=? ORDER BY (instr(full,'.')>0) DESC,(kind='declaration') DESC,full,package LIMIT 1").get(short);
  const path = hit.kind === "module" ? db.prepare("SELECT path FROM modules WHERE id=?").get(hit.ref).path : hit.full;
  cases.push({category:"qualified-search",kind:"search",name:hit.full,expectedName:path,match:"full"});
}
const pathSearches=select("SELECT path FROM modules ORDER BY sample_key(path),path LIMIT 20");
pathSearches.forEach(({path},index) => cases.push({category:"path-search",kind:"search",match:"full",
  name:index%2 ? path.slice(0,-5) : path,expectedName:path}));
for (const name of ["'", '"', "(", ")", "*", "-", ":", "^", "+", "{", "}", ".", "/", "_", "AND", "OR", "NOT", "NEAR", " ", "x' y\""]) {
  cases.push({category:"literal-input",kind:"search",name,match:"any"});
}
// Pick an unseeded module with links to exercise the module queries.
args.module = select("SELECT m.path FROM modules m JOIN links l ON l.module=m.id WHERE m.package='riemann-hypothesis' AND NOT EXISTS(SELECT 1 FROM informalizations i WHERE i.module=m.id) ORDER BY m.path LIMIT 1")[0].path;
for (const [kind, group] of Object.entries(queries)) {
  const value = args[kind];
  const expected = Object.fromEntries(Object.entries(group).map(([key,sql]) =>
    [key, select(sql,...parameters(kind,value,offset))]));
  cases.push({category:"queries.json",kind:"worker",name:kind,small:true,value,expected});
}
db.close();

const auxiliary = "Zeta23/FromPNTPlus/Auxiliary.lean";
const staticPages = readdirSync(siteDir, {recursive:true})
  .filter(path => path.endsWith(".html"))
  .sort()
  .map(path => "/" + path.replace(/(^|\/)index\.html$/, "$1"));
assert.ok(staticPages.includes("/"), "The package has no home page");
const auxiliaryKey = createHash("sha256").update(auxiliary).digest("hex").slice(0,16);
cases.push({kind:"layout", category:"page-width", name:"/proofs/zeta23/", width:360, small:true});
const auxiliaryEntry = readFileSync("packages/zeta23/informalizations/" + auxiliary + "/dial481--michael-stoll.md","utf8");
const headerText = auxiliaryEntry.match(/^```text\n([\s\S]*?\n)```$/m)[1];
const fencePages = ["/m/?pkg=zeta23&p=" + auxiliary];
const auxiliaryStatic = "/m/records/zeta23/" + auxiliaryKey + "/";
if (staticPages.includes(auxiliaryStatic)) fencePages.push(auxiliaryStatic);
for (const width of [1280,390]) {
  for (const path of fencePages) {
    cases.push({kind:"layout",category:"fenced-header",name:path,width,small:true});
  }
}

for (const width of [440, 1280]) {
  for (const scheme of ["light", "dark"]) {
    cases.push({kind:"layout", category:"contribution-form", name:"/sample/riemann-hypothesis/rowsrc/", width, scheme, small:true});
  }
}

function measureForm(form) {
  const checkbox = form.elements.rights.getBoundingClientRect();
  const label = form.elements.rights.parentElement.querySelector("span");
  const range = document.createRange();
  range.selectNodeContents(label);
  const firstLine = range.getClientRects()[0];
  const origin = form.elements.origin;
  range.selectNodeContents(origin.parentElement.firstChild);
  const originLabel = range.getBoundingClientRect();
  const select = origin.getBoundingClientRect();
  return {
    checkboxHeight: checkbox.height,
    centerDelta: Math.abs(checkbox.top + checkbox.height / 2 - firstLine.top - firstLine.height / 2),
    originBelowLabel: select.top >= originLabel.bottom,
    fieldWidths: [select.width, form.elements.handle.offsetWidth, form.elements.writer.offsetWidth],
    theme: matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light",
  };
}

// Read glyph positions even on an old build where spans split the original text nodes.
function measureHeader(code, expected) {
  const pre = code.parentElement;
  const walker = document.createTreeWalker(code, NodeFilter.SHOW_TEXT);
  const range = document.createRange();
  let node = walker.nextNode(), offset = 0;
  function topAt(index) {
    while (node && index >= offset + node.length) {
      offset += node.length;
      node = walker.nextNode();
    }
    range.setStart(node, index - offset);
    range.setEnd(node, index - offset + 1);
    return range.getBoundingClientRect().top;
  }
  const textMatches = code.textContent === expected;
  const lines = expected.replace(/\n$/, "").split("\n");
  const lineHeight = Number.parseFloat(getComputedStyle(pre).lineHeight);
  let index = 0, lineStarts = 0, blanks = 0, previousEnd;
  if (textMatches) {
    for (const line of lines) {
      if (line.length) {
        // WebKit can return an empty rectangle for a newline. Measure blank lines
        // by the row spacing between the visible characters on either side.
        const start = topAt(index);
        const rows = previousEnd === undefined ? 1 : Math.round((start - previousEnd) / lineHeight);
        lineStarts += Math.max(0, Math.min(1 + blanks, rows));
        previousEnd = topAt(index + line.length - 1);
        blanks = 0;
      } else {
        blanks++;
      }
      index += line.length + 1;
    }
  }
  return {sourceLines:lines.length, lineStarts, preScroll:pre.scrollWidth, preClient:pre.clientWidth,
    codeElements:code.childElementCount, textMatches};
}

async function visit(page, test, measured) {
  const {name,kind,pkg,path} = test;
  const url = new URL(kind === "layout" ? name : kind === "worker" || kind === "search" ? "/" : kind === "module" ? "/m/" : "/d/",origin);
  if (pkg) {
    url.searchParams.set("pkg",pkg);
    url.searchParams.set(kind==="module"?"p":"n",name);
  } else if (kind==="search") url.searchParams.set("q",name);
  if (test.scheme) await page.emulateMedia({colorScheme: test.scheme});
  if (test.width) await page.setViewportSize({width:test.width,height:820});
  const res = await page.goto(url.href,{waitUntil:test.width ? "load" : "domcontentloaded"});
  assert.ok([200,304].includes(res?.status()), "HTTP "+res?.status()+" for "+url.pathname);
  if (kind==="layout") {
    await page.locator("main h1").first().waitFor({state:"attached"});
    if (name.startsWith("/m/")) await page.locator("article.informalization pre > code").first().waitFor();
    if (name.startsWith("/sample/")) await page.locator("article.record").waitFor();
  } else if (kind==="worker") {
    const data = await page.evaluate(({name,value}) => new Promise((resolve,reject) => {
      const worker = new Worker("/query-thread.mjs",{type:"module"});
      worker.onerror = event => {worker.terminate(); reject(Error(event.message));};
      worker.onmessage = ({data}) => {worker.terminate(); data.error ? reject(Error(data.error)) : resolve(data.result);};
      worker.postMessage({id:1,kind:name,value});
    }),{name,value:test.value});
    for (const [key,rows] of Object.entries(test.expected)) {
      assert.equal(JSON.stringify(data[key]),JSON.stringify(rows),"Native SQLite mismatch for "+name+"."+key);
    }
  } else if (kind==="search") {
    await page.waitForFunction(()=> {
      const matches=document.querySelector("#matches");
      return /^[\d,]+ results?$/.test(matches?.querySelector(".search-total")?.textContent ?? "") ||
        /could not complete/i.test(matches?.textContent ?? "");
    });
    const count = page.locator(".search-total");
    if (!await count.count()) throw Error(await page.locator("#matches").innerText());
    const countText = await count.textContent();
    assert.match(countText,/^[\d,]+ results?$/);
    const first = page.locator("#matches li a").first();
    if (test.match==="any") {
      if (countText!=="0 results") assert.ok(await first.count(),"Missing result");
    } else {
      assert.ok(await first.count(),"Missing exact result");
      const address=new URL(await first.getAttribute("href"),origin);
      const module=address.searchParams.get("p");
      const result=module ?? address.searchParams.get("n") ??
        (address.pathname.startsWith("/proofs/") ? await first.textContent() : null);
      assert.ok(result, "Result has no module, declaration or proof address");
      const short=module ? module.split("/").at(-1).replace(/\.lean$/,"") : result.split(".").at(-1);
      assert.equal(test.match==="short" ? short.toLowerCase() : result, test.expectedName ?? name);
    }
  } else {
    await page.waitForFunction(()=>document.querySelector("article.record") ||
      /not found|could not be opened|unknown package/i.test(document.querySelector("main")?.innerText));
    const heading = await page.locator("main h1").allTextContents();
    assert.ok(heading.length && !/not found/i.test(heading[0]),"Record missing: "+heading.join(" "));
    assert.equal(await page.title(),recordMetadata(kind,name,pkg).name+" · QED Codex","Wrong document title");
    const pin = source(proof,pkg,path,test.start,test.end);
    assert.ok(await page.locator("main a").evaluateAll((links,url)=>links.some(a=>a.href===url),pin),"Missing pinned source link");
    if (test.category === "statement-module") {
      const entry = page.locator('[id="informalization-dial481--andrew-o-desky"]');
      assert.ok(await entry.count(), "Missing permission entry");
      assert.ok((await entry.innerText()).includes(`As published on ${publicationDate}.`), "Missing snapshot date");
      assert.ok(await entry.locator("h2").count(), "Statement body missing");
    }
    if (kind==="declaration") await page.waitForFunction(()=>{
      const box=document.querySelector(".lean-source");
      return !box || box.querySelector("pre") || box.textContent.includes("Use the pinned source link");
    });
  }
  await page.evaluate(()=>document.fonts.ready);
  const width = await page.evaluate(()=>({document:document.documentElement.scrollWidth,screen:innerWidth}));
  Object.assign(measured, width);
  if (test.width) assert.equal(width.screen, test.width, "Viewport width differs from requested size");
  if (test.category === "contribution-form") {
    const form = await page.locator("form.contribute").evaluate(measureForm);
    Object.assign(measured, form);
    assert.equal(form.theme, test.scheme);
    assert.ok(form.checkboxHeight > 0 && form.checkboxHeight <= 20, `Checkbox height ${form.checkboxHeight}px`);
    assert.ok(form.centerDelta <= 2, `Checkbox centre differs from the label by ${form.centerDelta}px`);
    assert.ok(form.originBelowLabel, "Origin label overlaps its select");
    assert.ok(Math.max(...form.fieldWidths) - Math.min(...form.fieldWidths) < 1, "Contribution field widths differ");
  }
  if (test.category === "fenced-header") {
    Object.assign(measured, await page.locator("article.informalization pre > code").first().evaluate(measureHeader,headerText));
    assert.ok(measured.textMatches, "Fence text differs from the ledger");
    assert.equal(measured.codeElements, 0, "Fence contains child elements");
    assert.equal(measured.lineStarts, measured.sourceLines, "Source lines run together");
    assert.ok(measured.preScroll <= measured.preClient, "Fence overflows its box");
  }
  assert.ok(width.document <= width.screen, `Document width ${width.document}px exceeds ${width.screen}px`);
  assert.ok((await page.title()).trim(),"Missing document title");
}
const clean = text=>String(text).replace(/[\r\n\t]+/g," ");
console.log("browser\tversion\tcategory\tkind\tinput\tstatus\tms\ttransfer_bytes\tdb_transfer_bytes\tpage_bytes\tlargest_rank\terrors\tviewport_px\tdocument_px\tsource_lines\tline_starts\tpre_scroll_px\tpre_client_px\tcode_children\tcolor_scheme\tcheckbox_height_px\tfirst_line_center_delta_px");
let failures=0;
function printRow(fields) {
  console.log(fields.map(value => {
    const field=clean(value);
    return field.includes('"') ? '"' + field.replaceAll('"','""') + '"' : field;
  }).join("\t"));
}

// Navigate once per HTML file and measure three viewports in the same tab.
async function sweepStaticPages(context, name, version) {
  const widths = [440,390,320];
  const result = new Array(staticPages.length);
  let next = 0;
  async function lane() {
    const page = await context.newPage();
    page.setDefaultTimeout(30000);
    try {
      while (next < staticPages.length) {
        const i = next++, path = staticPages[i], rows = [];
        let loadError;
        const start = performance.now();
        try {
          const response = await page.goto(new URL(path,origin).href, {waitUntil:"load"});
          assert.ok(response?.ok() || (path === "/404.html" && response?.status() === 404),
            "HTTP " + response?.status() + " for " + path);
          if (await page.locator(".lean-source").count()) {
            await page.waitForFunction(() => {
              const box=document.querySelector(".lean-source");
              return box.querySelector("pre") || box.textContent.includes("Use the pinned source link");
            });
          }
          assert.ok((await page.title()).trim(), "Missing document title");
        } catch (error) { loadError = clean(error.message); }
        for (const viewport of widths) {
          const errors = [];
          let documentWidth = "";
          if (loadError) errors.push(loadError);
          else try {
            await page.setViewportSize({width:viewport, height:820});
            const measured = await page.evaluate(async () => {
              // Force layout for this viewport before waiting on any font it selects.
              void document.documentElement.offsetWidth;
              await document.fonts.ready;
              return {document:document.documentElement.scrollWidth, screen:innerWidth};
            });
            documentWidth = measured.document;
            assert.equal(measured.screen, viewport, "Unexpected viewport");
            assert.ok(documentWidth <= measured.screen, "Document width " + documentWidth + "px exceeds " + viewport + "px");
          } catch (error) { errors.push(clean(error.message)); }
          if (errors.length) failures++;
          rows.push([name,version,"page-width","layout",path,errors.length?"FAIL":"PASS",
            Math.round(performance.now()-start),"","","","",JSON.stringify(errors),viewport,documentWidth,"","","","","","","",""]);
        }
        result[i] = rows;
        if ((i+1)%500===0) console.error(name, i+1, "of", staticPages.length, "static pages");
      }
    } finally { await page.close(); }
  }
  await Promise.all(Array.from({length:name==="chromium" ? 6 : 4},lane));
  for (const rows of result) for (const fields of rows) printRow(fields);
}
async function runBrowser(name,launcher) {
  const browser=await launcher.launch({executablePath:process.env[name.toUpperCase()+"_EXECUTABLE"]});
  try {
    const context=await browser.newContext({viewport:{width:380,height:820}});
    const sample=cases.filter(x=>reflowOnly ? x.kind==="layout" : name==="chromium" || x.small || x.kind==="search");
    const rows=[];
    let next=0;
    async function lane() {
      while (next<sample.length) {
        const i=next++, test=sample[i], errors=new Set();
        const measured = {};
        const page=await context.newPage();
        const transport = new Set();
        const remember = (request, detail) => {
          if (transport.size < 8) transport.add(detail + " " + new URL(request.url()).pathname);
        };
        page.on("response", r=>{if (r.status() >= 400) remember(r.request(), "HTTP " + r.status());});
        page.on("requestfailed", r=>remember(r, r.failure()?.errorText || "Request failed"));
        page.on("console",msg=>{if(msg.type()==="error") errors.add("console: "+msg.text()+" "+msg.location().url);});
        page.on("pageerror",error=>errors.add("page: "+error.message));
        let timer;
        if (test.kind==="search") {
          await page.addInitScript(() => performance.setResourceTimingBufferSize(8192));
          page.on("worker",w=>w.evaluate(()=>performance.setResourceTimingBufferSize(8192)).catch(()=>{}));
        }
        const start=performance.now();
        try {
          await Promise.race([visit(page,test,measured),new Promise((_,reject)=>{
            timer=setTimeout(()=>reject(Error("No result within 30 seconds")),30000);
          })]);
        } catch(error) {errors.add(clean(error.message));}
        const ms=Math.round(performance.now()-start);
        clearTimeout(timer);
        let bytes="", dbBytes="";
        if (test.kind==="search") {
          const timings = () => ["navigation","resource"].flatMap(type=>performance.getEntriesByType(type))
            .map(e=>({url:e.name,bytes:e.transferSize}));
          try {
            const entries = (await Promise.all([page.evaluate(timings),...page.workers().map(w=>w.evaluate(timings))])).flat();
            bytes=entries.reduce((sum,e)=>sum+e.bytes,0);
            dbBytes=entries.filter(e=>new URL(e.url).pathname.startsWith("/db/")).reduce((sum,e)=>sum+e.bytes,0);
            assert.ok(Number.isFinite(bytes),"Missing browser transfer sizes");
          } catch(error) {errors.add("Measurement: "+clean(error.message));}
        }
        if (errors.size) for (const message of transport) errors.add(message);
        await page.close();
        const variants=test.kind==="worker"?Object.keys(queries[test.name]):[test.kind];
        for (const key of variants) rows.push({i,key,fields:[name,browser.version(),test.category,key,test.name,errors.size?"FAIL":"PASS",ms,bytes,dbBytes,test.pageBytes ?? "",test.largestRank ?? "",JSON.stringify([...errors]),
          measured.screen ?? test.width ?? "", measured.document ?? "", measured.sourceLines ?? "", measured.lineStarts ?? "",
          measured.preScroll ?? "", measured.preClient ?? "", measured.codeElements ?? "",test.scheme ?? "",measured.checkboxHeight ?? "",measured.centerDelta ?? ""]});
        if(errors.size) failures+=variants.length;
        if(i%100===0) console.error(name,i+1,"of",sample.length);
      }
    }
    await Promise.all(Array.from({length:name==="chromium"?6:2},lane));
    rows.sort((a,b)=>a.i-b.i || a.key.localeCompare(b.key,"en"));
    for (const row of rows) printRow(row.fields);
    await sweepStaticPages(context,name,browser.version());
  } finally {await browser.close();}
}
const launchers = {chromium,firefox,webkit};
for (const name of engines.length ? engines : Object.keys(launchers)) {
  assert.ok(Object.hasOwn(launchers,name), "Unknown browser: "+name);
  await runBrowser(name,launchers[name]);
}
process.exitCode=failures?1:0;
