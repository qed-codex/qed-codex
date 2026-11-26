import {reviewOrigin} from "./review-origin.mjs";
// Verify the compiled module route and both edges of the ranked board on loopback.
import assert from "node:assert/strict";
import {readFileSync} from "node:fs";
import {DatabaseSync} from "node:sqlite";
import {parameters} from "../site/search-input.mjs";
import {chromium, firefox, webkit} from "playwright";

const origin = new URL(process.argv[2]).origin;
reviewOrigin(origin);
const database = new DatabaseSync(process.argv[3] || "build/rh.sqlite3", {readOnly:true});
const firstWanted = database.prepare("SELECT path, spine_rank FROM most_wanted JOIN modules ON modules.id = most_wanted.module WHERE rank=1").get();
const offset = database.prepare("SELECT value FROM summary WHERE metric='fts_declaration_offset'").get().value;
const queries = JSON.parse(readFileSync("site/queries.json", "utf8"));
const matches = database.prepare(queries.searchCount.totals).get(...parameters("searchCount", "galois", offset)).total;
const searchTotal = matches.toLocaleString("en-US") + " results";
const expectedNames = [0, 20].map(skip => database.prepare(queries.search.matches)
  .all(...parameters("search", {term:"galois", offset:skip}, offset)).map(row => row.name));
database.close();
for (const [engine, launcher] of Object.entries({chromium, firefox, webkit})) {
  const browser = await launcher.launch({executablePath:process.env[engine.toUpperCase()+"_EXECUTABLE"]});
  try {
    const page = await browser.newPage({viewport:{width:380,height:844}});
    const url = (p) => new URL(p, origin).href;
    const numbered = [];
    page.context().on("request", r => {
      if (/\/db\/[^/]+\/p\/\d+$/.test(new URL(r.url()).pathname)) numbered.push(r.url());
    });
    const config = await (await page.request.get(url("/directory.json"))).json();
    await page.goto(url("/"));
    await page.getByRole("link",{name:"Unmatched statements",exact:true}).click();
    await page.getByRole("heading",{name:"Unmatched statements",exact:true}).waitFor();
    const unmatched = await page.locator("main section li a").count();
    assert.match(await page.locator("main > p").first().innerText(),new RegExp("^"+unmatched+" entries"));
    assert.deepEqual(numbered,[]);
    const direct = "/m/records/" + config.staticModules[0] + "/";
    await page.goto(url(direct));
    const file = await page.locator("main").getAttribute("data-original-path");
    assert.ok(file?.endsWith(".lean"));
    const original = await page.locator("main article.record").innerText();
    const pkg = await page.locator("main").getAttribute("data-package");
    await page.goto(url("/m/?" + new URLSearchParams({pkg,p:file})));
    await page.locator("main article.record").waitFor();
    assert.equal(await page.locator("main article.record").innerText(),original);
    assert.equal(await page.evaluate(() => performance.getEntriesByType("resource").some(r => new URL(r.name).pathname.endsWith("/select-static.js"))), false, "Non-sample module must not download the sample markup");
    await page.goto(url("/wanted/"));
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), "Board fits the narrow viewport");
    const entries = page.locator(".record-list li");
    assert.equal(await entries.count(),50);
    assert.equal(await entries.first().locator("a").textContent(), firstWanted.path);
    assert.equal(await entries.first().locator(".chip").first().textContent(), "Spine · " + firstWanted.spine_rank);
    assert.deepEqual(numbered,[]);
    await page.getByRole("link",{name:"Next",exact:true}).click();
    await page.getByText(/^Showing 51–100 /).waitFor();
    assert.equal(await entries.count(),50);
    assert.ok(numbered.length>0);
    const last = 1 + Math.floor((config.wantedCount - 1) / 50) * 50;
    await page.goto(url("/wanted/?start="+last));
    await page.getByText(new RegExp("^Showing "+last+"–")).waitFor();
    assert.equal(await entries.count(),config.wantedCount-last+1);
    assert.equal(await page.getByRole("link",{name:"Next",exact:true}).count(),0);
    const unknown = {};
    for (const [path, heading] of [["/qed-unlisted-test-path/", "Page not found"],
         ["/m/?pkg=riemann-hypothesis&p=src%2FQEDUnknownModule.lean", "Module not found"], ["/d/?pkg=riemann-hypothesis&n=QED.UnknownDeclaration", "Declaration not found"]]) {
      const response = await page.goto(url(path));
      await page.getByRole("heading", {name:heading, exact:true}).waitFor();
      assert.equal(response.status(),path.startsWith("/qed-unlisted") ? 404 : 200);
      unknown[path] = {status:response.status(), heading};
    }
    await page.goto(url("/?q=galois"));
    await page.getByText(searchTotal,{exact:true}).waitFor();
    const hits = page.locator("#matches li a");
    const pageOne = await hits.allTextContents();
    assert.equal(pageOne.length,20);
    assert.deepEqual(pageOne, expectedNames[0]);
    await page.getByRole("link",{name:"More results"}).click();
    await page.getByText(searchTotal,{exact:true}).waitFor();
    assert.equal(new URL(page.url()).searchParams.get("page"),"2");
    assert.deepEqual(await hits.allTextContents(), expectedNames[1]);
    await hits.first().click();
    await page.locator("article.record").waitFor();
    await page.goBack();
    await page.getByText(searchTotal,{exact:true}).waitFor();
    assert.equal(await page.getByRole("searchbox").inputValue(),"galois");
    await page.goBack();
    await page.getByText(searchTotal,{exact:true}).waitFor();
    assert.deepEqual(await hits.allTextContents(),pageOne);
    await page.goto(url("/about/"));
    await page.getByRole("link",{name:"contact@qedcodex.org"}).first().waitFor();
    assert.equal(await page.locator("#glossary").count(),1);
    await page.goto(url("/d/?pkg=riemann-hypothesis&n=CompanionTheory.Bmu.QBd"));
    await page.getByText(/The kernel data records use/).waitFor();
    console.log(JSON.stringify({engine,unknown,version:browser.version(),staticModule:file,staticAndBoardNumberedReads:0,
      unmatched,boardRanks:[1,51,last,config.wantedCount]}));
  } finally {await browser.close();}
}
