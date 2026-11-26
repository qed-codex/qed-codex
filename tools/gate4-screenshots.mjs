// Capture the full board and a completed, reproducible console query on loopback.
import assert from "node:assert/strict";
import {createHash} from "node:crypto";
import {mkdir, writeFile} from "node:fs/promises";
import {join} from "node:path";
import {chromium} from "playwright";

const [address, output] = process.argv.slice(2);
const origin = new URL(address);
assert(["localhost","127.0.0.1"].includes(origin.hostname));
await mkdir(output, {recursive:true});
const inventory = ["file\twidth\theight\tscheme\tsha256"];
const browser = await chromium.launch();
try {
  for (const route of ["wanted","sql"]) {
    for (const width of [1280,380]) {
      for (const scheme of ["light","dark"]) {
        const page = await browser.newPage({viewport:{width,height:844},colorScheme:scheme});
        await page.goto(new URL("/"+route+"/",origin).href);
        if (route === "sql") {
          await page.getByLabel("SQL query").fill("SELECT path, cut FROM modules WHERE path = 'src/Main.lean'");
          await page.getByRole("button",{name:"Run query"}).click();
          await page.getByText("1 row.",{exact:true}).waitFor();
        } else {
          assert.equal(await page.locator(".record-list li").count(),50);
        }
        await page.evaluate(() => document.fonts.ready);
        const size = await page.evaluate(() => ({
          height:document.documentElement.scrollHeight,width:document.documentElement.scrollWidth,
          footer:document.querySelector("footer").getBoundingClientRect().bottom + scrollY,
        }));
        assert.equal(size.width,width);
        assert(size.footer <= size.height + 1);
        const file = route+"-"+width+"-"+scheme+".png";
        const png = await page.screenshot({path:join(output,file),fullPage:true,animations:"disabled"});
        assert.equal(png.readUInt32BE(16),width);
        assert.equal(png.readUInt32BE(20),size.height);
        inventory.push([file,width,size.height,scheme,createHash("sha256").update(png).digest("hex")].join("\t"));
        await page.close();
      }
    }
  }
} finally {await browser.close();}
await writeFile(join(output,"inventory.tsv"),inventory.join("\n")+"\n");
