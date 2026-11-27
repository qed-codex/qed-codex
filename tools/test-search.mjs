import assert from "node:assert/strict";
import {readFile} from "node:fs/promises";
import {chromium} from "playwright";
import {reviewOrigin} from "./review-origin.mjs";

const origin = reviewOrigin(process.argv[2]);
const tests = JSON.parse(await readFile(process.argv[3], "utf8")).queries.filter(q => q.kind === "search");
const browser = await chromium.launch();
try {
  for (const {value,expected} of tests) {
    const page = await browser.newPage();
    const files = new Set();
    page.on("request", req => { const u = new URL(req.url()); if (u.pathname.startsWith("/db/")) files.add(u.pathname); });
    await page.goto(origin+"/?"+new URLSearchParams({q:value}));
    await page.locator(".search-total").filter({hasText:/[0-9] results?$/}).waitFor();
    const names = await page.locator("#matches li a").allTextContents();
    assert.deepEqual(names,expected.matches.map(row => row.name));
    console.log(JSON.stringify({query:value,total:await page.locator(".search-total").innerText(),files:files.size}));
    // Cold search fetches physical SQLite pieces. Ledger growth and FTS layout
    // can shift the same rows across piece boundaries (20–21 files measured).
    // Allow four more files above 20 while still catching large regressions.
    assert(files.size <= 24, value + " fetched " + files.size + " files for names and count");
    await page.close();
  }
} finally { await browser.close(); }
