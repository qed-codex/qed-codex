import {readDirectoryProof} from "./read-directory-proof.mjs";
import {reviewOrigin} from "./review-origin.mjs";
// Capture the rendered directory and replay the native SQLite fixtures over local HTTP.
import assert from "node:assert/strict";
import { execFile } from "node:child_process";
import { createHash } from "node:crypto";
import { mkdir, mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { promisify } from "node:util";
import { chromium, firefox, webkit } from "playwright";

const [target, fixtures, output, mode = "all"] = process.argv.slice(2);
if (!output || !["all", "pages", "fixtures"].includes(mode)) {
  throw Error("Usage: node tools/gate3-evidence.mjs LOCAL_URL FIXTURES_JSON REPORT_DIR [all|pages|fixtures]");
}
const origin = new URL(target).origin;
reviewOrigin(origin);
const proof = readDirectoryProof();
const ledger = "https://github.com/qed-codex/qed-codex";
const kernelCredit = "https://github.com/james-shore/rh-proof-dependencies/releases/tag/v0.2.1";
const engines = { chromium, firefox, webkit };
const rowPath = "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/RowSrc.lean";
const samples = [
  { id: "home", route: "/" },
  ...[
    ["rowsrc", rowPath],
    ["slope", "src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean"],
    ["d1", "src/BuildAid/D1.lean"],
  ].map(([id, file]) => ({ id, type: "module", file, route: "/m/?" + new URLSearchParams({pkg:"riemann-hypothesis",p:file}) })),
  ...[
    ["galois", "UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter", rowPath, 6],
    ["anygeometry", "GlobalTheory.Mem.Top.Bl.anyGeometry", "src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean", 19],
    ["rh", "riemannHypothesis", "src/Main.lean", 4],
  ].map(([id, name, file, line]) => ({ id, type: "declaration", name, file, line, route: "/d/?" + new URLSearchParams({pkg:"riemann-hypothesis",n:name}) })),
];

await mkdir(output, { recursive: true });

async function recordFixtures() {
  const run = promisify(execFile);
  const temp = await mkdtemp(path.join(os.tmpdir(), "qed-fixtures-"));
  try {
    const native = JSON.parse(await readFile(fixtures, "utf8"));
    assert.equal(native.queries.length, 14);
    const summary = {};
    for (const engine of Object.keys(engines)) {
      const file = path.join(temp, engine + ".json");
      await run(process.execPath, ["tools/measure.mjs", origin + "/probe.html", fixtures, file, engine]);
      const result = JSON.parse(await readFile(file, "utf8"));
      assert.equal(result.samples.length, 42);
      const counts = native.queries.map(({kind, value}) => {
        const rows = result.samples.filter(row => row.kind === kind && row.value === value);
        assert.deepEqual(rows.map(row => row.state), ["cold", "repeat", "warm"]);
        return {kind, value, cold: rows[0].database.files, repeat: rows[1].database.files, warm: rows[2].database.files};
      });
      summary[engine] = { version: result.browser, queries: counts };
      console.log(engine, "matched fourteen native fixtures in each cache state");
    }
    await writeFile(path.join(output, "fixture-files.json"), JSON.stringify(summary, null, 2) + "\n");
  } finally {
    await rm(temp, { recursive: true, force: true });
  }
}

async function render(page, sample) {
  const response = await page.goto(origin + sample.route, { waitUntil: "domcontentloaded" });
  assert.equal(response.status(), 200);
  const policy = response.headers()["content-security-policy"];
  assert(policy?.includes("https://giscus.app") && policy.includes("https://raw.githubusercontent.com"));
  const marker = sample.name?.split(".").at(-1) ?? (sample.file ? sample.file.split("/").at(-1).replace(/\.lean$/, "") : "QED Codex");
  await page.waitForFunction(marker => document.body.innerText.includes(marker), marker);
  const text = await page.locator("body").innerText();
  assert(text.includes("Independent project. Not affiliated with any AI vendor."));
  if (!sample.type) {
    const introduction = await page.locator(".home-intro h1 + p").textContent();
    for (const term of ["machine-written proofs", "people", "autoinformalizations by AI", "side by side"]) assert(introduction.includes(term));
    return;
  }
  assert(text.includes("James Shore") && text.includes("Andrew Sutherland") && text.includes("Levent Alpöge"));
  const links = await page.locator("a:visible").evaluateAll(anchors => anchors.map(a => a.href));
  const source = proof.source_url + "/blob/" + proof.source_commit + "/" + sample.file;
  assert(links.some(href => href === source || href.startsWith(source + "#")));
  assert(links.includes(kernelCredit), "Missing versioned kernel dataset credit");
  if (sample.type === "module") {
    assert(text.includes("Discussion opens at launch"));
    const record = page.locator("article.record:visible");
    assert.deepEqual(await record.locator(":scope > section > h2").allTextContents(),
      ["Informalizations", "Declarations", "Elsewhere", "Open disputes", "Discussion"]);
    assert.equal(await record.locator(".kernel").first().locator(".chip").count(), 5);
    assert.equal(await record.locator("span.status").innerText(), sample.id === "rowsrc" ? "one informalization" : "no informalization");
    const issue = links.map(href => new URL(href)).find(url => url.href.startsWith(ledger + "/issues/new?"));
    assert(issue?.searchParams.get("template"), "Issue form template");
    assert([...issue.searchParams.values()].includes("riemann-hypothesis:" + sample.file), "Prefilled module");
    if (sample.id === "rowsrc") {
      assert(text.includes("@dial481"));
      assert((await record.locator(".informalization .meta").innerText()).includes("Codex (GPT-6.2 Astra)"));
      assert(await record.locator(".informalization math").count() > 0, "Compiled math");
    }
    if (sample.id === "slope") assert(text.includes("Andrew O’Desky"));
  } else {
    assert(links.some(href => href.startsWith(source + "#L" + sample.line)));
    const record = page.locator("article.record:visible");
    const heading = record.locator("h1").first();
    const components = sample.name.split(".");
    assert.equal(await heading.textContent(), components.pop());
    if (components.length) {
      const namespace = components.join(".");
      assert.equal(await heading.evaluate(el => el.previousElementSibling?.textContent.trim().replace(/\.$/, "")), namespace);
    }
    assert.deepEqual(await record.locator(":scope > section > h2").allTextContents(),
      ["Lean source", "Trail to riemannHypothesis", ...(sample.id === "anygeometry" ? [] : ["Elsewhere"]), "Other declarations in this module"]);
    const trail = record.locator("ol.trail > li");
    assert.equal(await trail.count(), {galois: 5, anygeometry: 9, rh: 1}[sample.id]);
    assert((await trail.last().innerText()).includes("riemannHypothesis"));
    const detachedCitations = await trail.evaluateAll(items => items.flatMap(item => {
      const name = item.querySelector(".identifier > span:last-child");
      const nameLine = name.getBoundingClientRect();
      return [...item.querySelectorAll(".trail-lines a")].filter(a => {
        const lines = [...a.getClientRects()];
        return lines.length !== 1 || lines[0].bottom <= nameLine.top || lines[0].top >= nameLine.bottom;
      }).map(a => a.textContent);
    }));
    assert.deepEqual(detachedCitations, [], "Trail citations should share the final name line");
    const peers = record.locator("section").last().locator("li");
    for (const peer of await peers.all()) {
      const a = peer.getByRole("link");
      const name = await a.textContent();
      assert.equal(await a.getAttribute("href"), "/d/?pkg=riemann-hypothesis&n=" + encodeURIComponent(name));
      const summary = await peer.locator(".kernel-summary").textContent();
      const expected = sample.id === "rh" ? name : name.endsWith(".geoOf") ? "none" : "all five";
      assert.equal(summary, "Used by: " + expected);
    }
    if (sample.id === "anygeometry") {
      assert.match(await record.locator("p.path").innerText(), /def.*OverIx\.lean.*Line 19/s);
      assert.equal(await record.locator(":scope > .kernel > .used").count(), 5);
    }
    assert(links.some(href => {
      const url = new URL(href);
      return url.origin === origin && url.pathname === "/m/" && url.searchParams.get("p") === sample.file;
    }));
  }
}

async function exercise(browser) {
  const context = await browser.newContext({viewport:{width:380,height:844}});
  try {
    const page = await context.newPage();
    const exceptions = [];
    page.on("pageerror", error => exceptions.push(error.message));
    await page.goto(origin + "/d/?pkg=riemann-hypothesis&n=allChi");
    const peerRow = page.locator(".record-list li").filter({
      has: page.getByRole("link", {name: "rhOfAll", exact: true}),
    });
    await peerRow.locator(".kernel-summary").waitFor();
    assert.equal(await peerRow.locator(".kernel-summary").textContent(), "Used by: riemannHypothesis, riemannZeta_eq_zero_re");
    await peerRow.getByRole("link", {name: "rhOfAll", exact: true}).click();
    await page.getByRole("heading", {name: "rhOfAll", exact: true}).waitFor();
    await page.goto(origin + "/");
    await page.getByRole("searchbox").fill("RowSrc");
    const moduleMatch = page.locator("#matches").getByRole("link", {name: /\.RowSrc$/});
    await moduleMatch.waitFor();
    const moduleTarget = new URL(await moduleMatch.getAttribute("href"), origin);
    assert.equal(moduleTarget.pathname, "/m/");
    assert.deepEqual([...moduleTarget.searchParams], [["pkg","riemann-hypothesis"],["p", rowPath]]);
    await page.getByRole("searchbox").fill("anyGeometry");
    const match = page.locator("#matches").getByRole("link", {name:"GlobalTheory.Mem.Top.Bl.anyGeometry", exact:true});
    await match.waitFor();
    const refreshed = page.evaluate(() => new Promise(resolve => {
      const observer = new MutationObserver(() => { observer.disconnect(); resolve(); });
      observer.observe(document.querySelector("#matches"), {childList:true});
    }));
    await page.getByRole("button", {name:"Search everywhere"}).click();
    await refreshed;
    await match.click();
    const sample = samples.find(s => s.id === "anygeometry");
    await page.locator(".lean-source pre code").waitFor();
    assert.equal(await page.locator(".lean-source pre code").textContent(), "def anyGeometry : GeoP := fun _ _ _ => True");
    // Traverse a declaration and module outside the six generated samples.
    await page.getByRole("link",{name:"GlobalTheory.Mem.Top.Bl.geoOf",exact:true}).click();
    await page.getByRole("heading",{name:"geoOf",exact:true}).waitFor();
    assert.equal(await page.locator("article.record > .kernel > .unused").count(),5);
    await page.getByRole("link", {name:sample.file,exact:true}).click();
    await page.getByRole("heading", {name:"OverIx.lean",exact:true}).waitFor();

    // Intercept GitHub navigation locally. The test neither creates a file nor opens an issue.
    const editor = page.waitForRequest(r => r.url().startsWith(ledger + "/new/main?"));
    await context.route(ledger + "/new/main?*", route => route.fulfill({contentType:"text/html", body:"<title>Local editor destination check</title>"}));
    assert(await page.getByRole("button",{name:"Add an informalization"}).isDisabled());
    await page.getByLabel("GitHub handle").fill("fixture-handle");
    await page.getByLabel("Writer (person or model)").fill("Fixture Writer");
    await page.getByLabel("Origin",{exact:true}).selectOption("wrote");
    assert(await page.getByRole("button",{name:"Add an informalization"}).isDisabled());
    await page.getByRole("checkbox",{name:"I have the right to submit this under CC BY 4.0."}).check();
    await page.getByRole("button",{name:"Add an informalization"}).click();
    const params = new URL((await editor).url()).searchParams;
    assert.equal(params.get("filename"), "packages/riemann-hypothesis/informalizations/" + sample.file + "/fixture-handle--fixture-writer.md");
    const front = params.get("value");
    for (const expected of [sample.file, "fixture-handle", "writer: \"Fixture Writer\"", "origin: wrote", "declarations: []", "CC-BY-4.0", proof.source_commit]) {
      assert(front.includes(expected));
    }

    const sourceSlices = [];
    for (const declaration of samples.filter(s => s.type === "declaration")) {
      await page.goto(origin + declaration.route);
      const box = page.locator(".lean-source");
      const code = box.locator("pre code");
      await code.waitFor();
      const rawUrl = proof.source_url.replace("github.com", "raw.githubusercontent.com") + "/" + proof.source_commit + "/" + declaration.file;
      const raw = await context.request.get(rawUrl);
      assert.equal(raw.status(), 200);
      const lines = (await raw.text()).split(/\r?\n/);
      const start = Number(await box.getAttribute("data-start")), end = Number(await box.getAttribute("data-end"));
      assert.equal(start, declaration.line);
      assert.equal(await code.textContent(), lines.slice(start - 1, end).join("\n"));
      sourceSlices.push({declaration:declaration.name,start,end});
    }

    await context.route("https://raw.githubusercontent.com/**", route => route.abort());
    await page.goto(origin + sample.route);
    await page.getByText("Use the pinned source link to read this declaration.").waitFor();
    assert((await page.getByRole("link",{name:"Open pinned source"}).getAttribute("href")).endsWith("/"+sample.file+"#L19"));
    assert.deepEqual(exceptions, []);
    return {typeahead:true, fullText:true, sourceSlices, sourceFallback:true,
      linkedDeclaration:true, linkedModule:true, typeaheadModulePath:moduleTarget.searchParams.get("p"), newFilePrefill:true};
  } finally {
    await context.close();
  }
}

async function collectPages() {
  const folder = path.join(output, "screenshots");
  await mkdir(folder, { recursive: true });
  const images = [];
  const routeEvidence = {};
  for (const [name, launcher] of Object.entries(engines)) {
    const browser = await launcher.launch({executablePath: process.env[name.toUpperCase() + "_EXECUTABLE"]});
    try {
      routeEvidence[name] = {version: browser.version(), routes: [], interactions: await exercise(browser)};
      const widths = name === "chromium" ? [1280, 380] : [380];
      for (const width of widths) for (const scheme of name === "chromium" ? ["light", "dark"] : ["light"]) {
        const height = width === 1280 ? 900 : 844;
        const context = await browser.newContext({viewport: {width, height}, colorScheme: scheme, deviceScaleFactor: 1});
        await context.addInitScript(() => {
          window.blockedResources = [];
          document.addEventListener("securitypolicyviolation", e => {
            window.blockedResources.push({directive:e.effectiveDirective, blocked:e.blockedURI});
          });
        });
        try {
          for (const sample of samples) {
            const page = await context.newPage();
            try {
              const errors = [];
              const pagesRead = [];
              const primedAssets = new Set();
              page.on("pageerror", error => errors.push(error.message));
              context.on("request", onRequest);
              function onRequest(request) {
                const url = new URL(request.url());
                if (url.origin !== origin) return;
                if (url.pathname === "/proof.json") primedAssets.add("manifest");
                if (url.pathname.endsWith("/sqlite3.wasm")) primedAssets.add("wasm");
                if (url.pathname.endsWith("/interior")) primedAssets.add("interior");
                if (/\/db\/[^/]+\/p\/\d+$/.test(url.pathname)) pagesRead.push(url.pathname);
              }
              try {
                await render(page, sample);
                await page.waitForLoadState("networkidle");
                if (sample.id === "home") {
                  const deadline = Date.now() + 5000;
                  while (primedAssets.size < 3 && Date.now() < deadline)
                    await new Promise(resolve => setTimeout(resolve, 25));
                  assert.deepEqual([...primedAssets].sort(), ["interior", "manifest", "wasm"]);
                } else {
                  assert.equal(primedAssets.size, 0, "Record fetched database startup assets");
                }
                const metric = await page.evaluate(() => ({
                  viewport: window.innerWidth,
                  screen: document.documentElement.clientWidth,
                  scroll: document.documentElement.scrollWidth,
                  height: document.documentElement.scrollHeight,
                  footerBottom: Math.round(document.querySelector("footer").getBoundingClientRect().bottom + scrollY),
                  dark: matchMedia("(prefers-color-scheme: dark)").matches,
                  violations: window.blockedResources,
                }));
                assert.equal(metric.viewport, width);
                assert(metric.scroll <= metric.screen, sample.id + " overflows at " + width + " CSS pixels");
                assert(metric.footerBottom > 0 && metric.footerBottom <= metric.height + 1, "Footer must fit within the captured document");
                assert.equal(metric.dark, scheme === "dark");
                // A word can have several inline text nodes. A DOM Range over each
                // component must stay on one visual line, even if the name wraps.
                const splitWords = await page.evaluate(() => {
                  const selector = ".record > h1, .record .path a, .trail-row > a:first-child, .record-list a[href^='/d/'], .record-list a[href^='/m/'], .sample-links a";
                  for (const el of document.querySelectorAll(selector)) {
                    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
                    const text = el.textContent;
                    let offset = 0;
                    const nodes = [];
                    for (let node = walker.nextNode(); node; node = walker.nextNode()) {
                      nodes.push({ node, start: offset, end: offset + node.length });
                      offset += node.length;
                    }
                    for (const word of text.matchAll(/[^._/\s]+/gu)) {
                      const end = word.index + word[0].length;
                      const first = nodes.find(n => n.end > word.index);
                      const last = nodes.find(n => n.end >= end);
                      const range = document.createRange();
                      range.setStart(first.node, word.index - first.start);
                      range.setEnd(last.node, end - last.start);
                      const tops = [...range.getClientRects()].filter(r => r.width > 0 && r.height > 0).map(r => r.top);
                      if (tops.length && Math.max(...tops) - Math.min(...tops) > 2) return word[0];
                    }
                  }
                  return null;
                });
                assert.equal(splitWords, null, "Word split inside a name or path on " + sample.id);
                assert.deepEqual(metric.violations, [], sample.id + " CSP");
                assert.deepEqual(errors, [], sample.id + " page errors");
                assert.deepEqual(pagesRead, [], sample.id + " needed database pages before interaction");
                if (name === "chromium") {
                  const filename = sample.id + "-" + width + "-" + scheme + ".png";
                  const png = await page.screenshot({path: path.join(folder, filename), animations:"disabled", fullPage:true});
                  assert.equal(png.readUInt32BE(16), width);
                  assert.equal(png.readUInt32BE(20), metric.height, "Full document height including footer");
                  const digest = createHash("sha256").update(png).digest("hex");
                  images.push([filename, width, metric.height, scheme, digest]);
                }
                routeEvidence[name].routes.push({route: sample.id, width, scheme, fullHeight: metric.height, footerBottom: metric.footerBottom, numberedDatabasePages: pagesRead.length, idleAssets: [...primedAssets].sort()});
              } finally {
                context.off("request", onRequest);
              }
            } finally {
              await page.close();
            }
          }
        } finally {
          await context.close();
        }
      }
    } finally {
      await browser.close();
    }
  }
  assert.equal(images.length, 28);
  await writeFile(path.join(output, "screenshots.tsv"), ["file\twidth\theight\tscheme\tsha256", ...images.map(row => row.join("\t"))].join("\n") + "\n");
  await writeFile(path.join(output, "page-checks.json"), JSON.stringify(routeEvidence, null, 2) + "\n");
}

if (mode !== "pages") await recordFixtures();
if (mode !== "fixtures") await collectPages();
