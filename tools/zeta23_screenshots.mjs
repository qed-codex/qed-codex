import assert from "node:assert/strict";
import {createHash} from "node:crypto";
import {mkdir, readFile, writeFile} from "node:fs/promises";
import {chromium} from "playwright";

const [base, output] = process.argv.slice(2);
assert.equal(new URL(base).hostname, "127.0.0.1");
const pages = [
  ["assembly", "Zeta23/Assembly.lean"],
  ["auxiliary", "Zeta23/FromPNTPlus/Auxiliary.lean"],
  ["challenge", "Challenge.lean"],
  ["bounds", "Zeta23/FromPNTPlus/ZetaBounds.lean"],
  ["no-notes", "scripts/PrintAxioms.lean"],
];
const {staticModules} = await (await fetch(new URL("/directory.json",base))).json();
const inventory = ["file\twidth\theight\tsha256"];
await mkdir(output,{recursive:true});
const browser = await chromium.launch();
try {
  for (const [slug, path] of pages) {
    const key = "zeta23/" + createHash("sha256").update(path).digest("hex").slice(0,16);
    const entry = staticModules.includes(key);
    assert.equal(Boolean(entry),slug !== "no-notes");
    const route = entry ? "/m/records/" + key + "/" : "/m/?pkg=zeta23&p=" + encodeURIComponent(path);
    for (const width of [390,1280]) {
      const page = await browser.newPage({viewport:{width,height:820},deviceScaleFactor:1});
      await page.goto(new URL(route,base).href);
      await page.getByText("This package has no declaration index yet.",{exact:true}).waitFor();
      const main = page.locator("main");
      assert.match(await main.innerText(),/Theorem-use data unavailable/);
      assert.match(await main.innerText(),/independent description under CC BY 4.0/);
      assert.ok(await main.locator('a[href*="/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/"]').count());
      assert.equal(await main.locator(".status").textContent(),"no informalization");
      if (entry) assert.equal(await main.getByRole("heading",{name:"From the source",exact:true}).count(),1);
      if (entry) assert.equal(await main.locator("article.informalization").count(),1);
      if (slug === "auxiliary") assert.match(await main.locator("article .meta").innerText(),/Michael Stoll/);
      if (slug === "no-notes") assert.equal(await main.locator("article.informalization").count(),0);
      await page.evaluate(()=>document.fonts.ready);
      const file = slug + "-" + width + ".png";
      await page.screenshot({path:output + "/" + file,fullPage:true});
      const bytes = await readFile(output + "/" + file);
      inventory.push([file,bytes.readUInt32BE(16),bytes.readUInt32BE(20),createHash("sha256").update(bytes).digest("hex")].join("\t"));
      console.log(file,bytes.readUInt32BE(16),bytes.readUInt32BE(20));
      await page.close();
    }
  }
} finally { await browser.close(); }
await writeFile(output + "/inventory.tsv",inventory.join("\n") + "\n");
