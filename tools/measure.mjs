// Local measurement instrument. The deploy contains static files only.
import http from "node:http";
import { performance } from "node:perf_hooks";
import { readFile, writeFile } from "node:fs/promises";
import { chromium, firefox, webkit } from "playwright";

const [target, fixtureFile, output, engine = "chromium"] = process.argv.slice(2);
if (!output) throw new Error("Usage: node tools/measure.mjs PREVIEW_URL FIXTURES_JSON REPORT_JSON [chromium|firefox|webkit]");
const fixtures = JSON.parse(await readFile(fixtureFile));
const requests = [];
const received = new WeakMap();
const proxy = http.createServer((req,res) => {
  const socket = req.socket;
  const requestBytes = socket.bytesRead - (received.get(socket) || 0);
  received.set(socket,socket.bytesRead);
  const before = socket.bytesWritten;
  const url = new URL(req.url,target);
  const headers = {...req.headers, host:url.host};
  if (headers.range) throw new Error("Unexpected browser byte-range request");
  const upstream = http.get(url,{headers}, response => {
    // Preserve the encoded body. Count bytes on the browser-facing HTTP/1.1
    // socket, including its response headers and chunk framing.
    res.writeHead(response.statusCode,response.headers);
    let bodyBytes = 0;
    response.on("data", b => { bodyBytes += b.length; });
    res.on("finish", () => requests.push({path:url.pathname, status:res.statusCode,
      requestBytes, responseBytes:socket.bytesWritten-before, bodyBytes,
      encoding:response.headers["content-encoding"] || "identity",
      type:response.headers["content-type"] || "", cache:response.headers["cache-control"] || ""}));
    response.pipe(res);
  });
  upstream.on("error",e => res.destroy(e));
});
await new Promise(resolve => proxy.listen(0,"127.0.0.1",resolve));
const origin = `http://127.0.0.1:${proxy.address().port}`;
const probe = new URL(target);
const entry = new URL(probe.pathname + probe.search, origin);
const browser = await ({chromium, firefox, webkit})[engine].launch({executablePath:process.env[engine.toUpperCase()+"_EXECUTABLE"]});
const report = {engine, browser:browser.version(), protocol:"HTTP/1.1 loopback", samples:[]};
function stats(rows) {
  return {files:rows.length, encodedBody:rows.reduce((n,r)=>n+r.bodyBytes,0),
    responseWire:rows.reduce((n,r)=>n+r.responseBytes,0), requestWire:rows.reduce((n,r)=>n+r.requestBytes,0)};
}
async function run(page, query, state) {
  const {kind,value,expected} = query;
  await page.selectOption("#kind",kind);
  const mark = requests.length;
  const elapsedMs = await page.evaluate(async (value) => {
    const input = document.querySelector("#value");
    input.value = value;
    input.dispatchEvent(new Event("input", {bubbles:true}));
    const label=document.querySelector("#state"), start=performance.now();
    return new Promise(resolve => {
      const observer=new MutationObserver(() => {
        if (["Complete","Failed"].includes(label.textContent)) {
          observer.disconnect(); resolve(performance.now()-start);
        }
      });
      observer.observe(label,{childList:true});
      document.querySelector("form").requestSubmit();
    });
  },value);
  if (await page.textContent("#state") !== "Complete") throw Error(await page.textContent("#result"));
  const got = JSON.parse(await page.textContent("#result"));
  if (JSON.stringify(got)!==JSON.stringify(expected)) throw Error(`SQLite WASM result differs from native SQLite for ${kind}`);
  const all = requests.slice(mark);
  const data = all.filter(r=>r.path.startsWith("/db/"));
  if (data.some(r=>r.status!==200 || !r.cache.includes("immutable"))) throw Error("Unexpected page response or cache policy");
  if (state==="cold" && data.filter(r=>r.path.endsWith("/interior")).length!==1) throw Error("Expected one cold interior bundle");
  if (new Set(data.map(r=>r.path)).size!==data.length) throw Error("Duplicate page fetch");
  const fileLimit = {typeahead:5, search:20, module:state==="warm" ? 12 : 25}[kind];
  if (fileLimit !== undefined && data.length > fileLimit) {
    throw Error(`${kind} ${state} ${value}: fetched ${data.length} database files (limit ${fileLimit})`);
  }
  return {kind,state,value,elapsedMs:+elapsedMs.toFixed(2),database:stats(data),allQueryAssets:stats(all),
    requests:data.map(r=>({...r,path:r.path.split("/").slice(3).join("/")}))};
}
try {
  for (const fixture of fixtures.queries) {
    for (const primed of [false,true]) {
      const context = await browser.newContext();
      const page = await context.newPage();
      const navigationAt=requests.length;
      await page.goto(entry.href, {waitUntil:"networkidle"});
      if (await page.evaluate(() => self.crossOriginIsolated)) throw Error("Unexpected cross-origin isolation");
      const navigation=stats(requests.slice(navigationAt));
      if (primed) await run(page,fixtures.prime,"primer");
      const s=await run(page,fixture,primed?"warm":"cold");
      s.navigation=navigation;
      report.samples.push(s);
      if (!primed) {
        const repeat=await run(page,fixture,"repeat");
        if(repeat.database.files!==0) throw Error("Repeated query missed the VFS cache");
        report.samples.push(repeat);
      }
      await context.close();
    }
  }
  await writeFile(output,JSON.stringify(report,null,2)+"\n");
} finally {
  await browser.close();
  proxy.closeAllConnections();
  await new Promise(resolve=>proxy.close(resolve));
}
