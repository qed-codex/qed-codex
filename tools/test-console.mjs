import {reviewOrigin} from "./review-origin.mjs";
// Replay the console checks against a packaged QED Codex site served on loopback.
import assert from "node:assert/strict";
import {chromium, firefox, webkit} from "playwright";

const [origin, ...selected] = process.argv.slice(2);
reviewOrigin(origin);
const engines = {chromium, firefox, webkit};
const sample = "SELECT path, cut FROM modules WHERE path = 'src/Main.lean'";
for (const name of selected.length ? selected : Object.keys(engines)) {
  const browser = await engines[name].launch(name === "webkit" && process.env.WEBKIT_EXECUTABLE ?
    {executablePath:process.env.WEBKIT_EXECUTABLE} : {});
  try {
    const page = await browser.newPage({viewport:{width:380,height:844}});
    // The VFS fetches a whole SQLite page per miss. Model a WAN round trip.
    await page.context().route("**/db/*/p/*", async route => {
      await new Promise(resolve => setTimeout(resolve, 50));
      await route.continue().catch(error => {
        if (!route.request().failure() && !page.isClosed()) throw error;
      });
    });
    const errors = [];
    const databaseRequests = [];
    page.on("pageerror", error => errors.push(error.message));
    page.context().on("request", request => {
      if (new URL(request.url()).pathname.startsWith("/db/")) databaseRequests.push(request.url());
    });
    const query = page.getByLabel("SQL query", {exact:true});
    const status = page.getByRole("status");
    const run = page.getByRole("button",{name:"Run query"});
    async function execute(sql) {
      await query.fill(sql);
      await run.click();
      await page.waitForFunction(()=>!document.querySelector("#run").disabled, null, {timeout:45000});
      return status.textContent();
    }
    await page.goto(origin + "/sql/#" + new URLSearchParams({q:sample}));
    assert.equal(await query.inputValue(),sample);
    assert.equal(await status.textContent(),"");
    assert.equal(databaseRequests.length,0);
    assert.equal(await execute(sample),"1 row.");
    assert.deepEqual(await page.locator("tbody td").allTextContents(),["src/Main.lean","175186"]);
    const examples = await page.locator("#examples [data-sql]").evaluateAll(buttons => buttons.map(b => b.dataset.sql));
    examples.push(await query.evaluate(element => element.defaultValue));
    for (const example of examples) {
      await execute("EXPLAIN QUERY PLAN " + example);
      const plan = await page.locator("tbody").innerText();
      assert.match(plan, /SEARCH .* USING/);
      assert.doesNotMatch(plan, /SCAN /);
    }
    assert.equal(await execute("SELECT value FROM summary WHERE metric = 'modules'"),"1 row.");
    assert.equal(await page.locator("tbody td").innerText(),"184039");
    const scanned = await execute("SELECT count(*) FROM modules");
    if (scanned === "1 row.") assert.equal(await page.locator("tbody td").innerText(), "184039");
    else assert.equal(scanned, "Query stopped after 30 seconds. A whole-table scan was reading pages over the network. Row counts are in summary. Filter on an indexed column for other lookups.");
    console.log(name, "full scan with 50 ms per page:", scanned);
    assert.equal(await execute("SELECT rowid FROM names WHERE names MATCH 'geometry' LIMIT 3"),"3 rows.");
    assert.equal(await execute("SELECT row_number() OVER (ORDER BY id) FROM modules LIMIT 3"),"3 rows.");
    assert.equal(await execute("SELECT 1; -- a trailing comment"),"1 row.");
    await query.fill("SELECT '<i>hello</i>' AS markup");
    const share = await page.getByRole("link",{name:"Link to this query"}).getAttribute("href");
    await page.goto(share);
    assert.equal(await query.inputValue(),"SELECT '<i>hello</i>' AS markup");
    await execute(await query.inputValue());
    assert.equal(await page.locator("tbody td").innerText(),"<i>hello</i>");
    assert.equal(await page.locator("tbody i").count(),0);
    for (const sql of [
      "DELETE FROM modules", "CREATE TEMP TABLE handle (n)",
      "ATTACH ':memory:' AS more", "PRAGMA query_only=OFF",
      "SELECT 1; SELECT 2", "SELECT load_extension('unavailable')"
    ]) {
      assert.match(await execute(sql),/authoriz|prohibited|one SQL statement|no such function/i);
      assert.equal(await page.locator("tbody").count(),0);
    }
    assert.equal(await execute("SELECT path FROM modules ORDER BY id LIMIT 201"),"Showing 200 rows (result limit reached).");
    assert.equal(await page.locator("tbody tr").count(),200);
    await query.fill("WITH RECURSIVE tally(n) AS (VALUES (1) UNION ALL SELECT n+1 FROM tally) SELECT max(n) FROM tally");
    await run.click();
    await page.getByRole("button",{name:"Cancel",exact:true}).click();
    assert.equal(await status.textContent(),"Query cancelled.");
    assert.equal(await execute(sample),"1 row.");
    assert.deepEqual(errors,[]);
    console.log(name, browser.version(), "passed indexed examples, share links, reads, limits, authorization, cancellation and recovery");
  } finally { await browser.close(); }
}
