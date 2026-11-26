import assert from "node:assert/strict";
import {createHash} from "node:crypto";
import {mkdir,readFile,writeFile} from "node:fs/promises";
import {chromium} from "playwright";

const [before,after,out] = process.argv.slice(2);
for (const host of [before,after]) assert.equal(new URL(host).hostname,"127.0.0.1");
const records = [
  ["frame","src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean","codex-gpt-6-2-astra"],
  ["inert-thin","src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/RealDescent/LyingOverPrimes/InertThin.lean","andrew-o-desky"],
];
await mkdir(out,{recursive:true});
const browser=await chromium.launch();
const layouts=["page\tstage\tviewport_px\tdocument_width_px\tentry_width_px\tentry_scroll_width_px"];
const inventory=["file\twidth\theight\tsha256"];
try {
  for (const [stage,base] of [["before",before],["after",after]]) {
    const empty=await browser.newPage();
    const requested=[];
    empty.on("request",r=>{if(r.url().includes("/fonts/")) requested.push(r.url());});
    await empty.goto(new URL("/about/",base).href);
    await empty.evaluate(()=>document.fonts.ready);
    assert.equal(await empty.locator("math").count(),0);
    assert.deepEqual(requested,[]);
    console.log(stage,"About font requests",requested.length);
    await empty.close();
    for(const [key,path,writer] of records) {
      const index=await (await fetch(new URL("/informalizations.json",base))).json();
      const entry=index.find(row=>row.module===path && new URL(row.page).hash==="#informalization-dial481--"+writer);
      assert.ok(entry,"Missing indexed entry");
      for (const width of [380,1280]) {
        const page=await browser.newPage({viewport:{width,height:850},deviceScaleFactor:1});
        const fonts=[];
        page.on("response",res=>{if(res.url().includes("/fonts/")) fonts.push([res.url(),res.status()]);});
        await page.goto(new URL(new URL(entry.page).pathname,base).href);
        const article=page.locator("#informalization-dial481--"+writer);
        await article.waitFor();
        await article.scrollIntoViewIfNeeded();
        await page.evaluate(()=>document.fonts.ready);
        const formula=article.locator("math");
        assert.ok(await formula.count()>0);
        if (stage==="after") {
          assert.deepEqual(fonts,[[new URL("/fonts/stix-two-math.woff2",base).href,200]]);
          assert.equal(await page.evaluate(()=>[...document.fonts].some(f=>f.family==="STIX Two Math"&&f.status==="loaded")),true);
        } else assert.deepEqual(fonts,[]);
        const name=key+"-"+width+"-"+stage+".png";
        const dimensions=await article.evaluate(a=>({
          width:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight,
          articleWidth:a.clientWidth,articleScroll:a.scrollWidth
        }));
        layouts.push([key,stage,width,dimensions.width,dimensions.articleWidth,dimensions.articleScroll].join("\t"));
        // Capture the viewport-width strip through the entire document, including pages with pre-existing overflow.
        await page.screenshot({path:out+"/"+name,fullPage:true,clip:{x:0,y:0,width,height:dimensions.height}});
        const png=await readFile(out+"/"+name);
        assert.equal(png.readUInt32BE(16),width);
        assert.equal(png.readUInt32BE(20),dimensions.height);
        inventory.push([name,png.readUInt32BE(16),png.readUInt32BE(20),createHash("sha256").update(png).digest("hex")].join("\t"));
        const selector=key==="frame"?'math[display=block]':'math';
        const glyphs=article.locator(selector).filter({hasText:key==="frame"?/η/:/[𝔞-𝔷ℭℌℑℜℨ]/u}).first();
        if(width===380 && key==="frame") {
          const name=key+"-equation-"+stage+".png";
          const png=await glyphs.screenshot({path:out+"/"+name});
          inventory.push([name,png.readUInt32BE(16),png.readUInt32BE(20),createHash("sha256").update(png).digest("hex")].join("\t"));
        }
        console.log(stage,key,width,"formulas",await formula.count(),"font responses",fonts.length);
        await page.close();
      }
    }
  }
} finally {await browser.close();}
await writeFile(out+"/inventory.tsv",inventory.join("\n")+"\n");
await writeFile(out+"/layout.tsv",layouts.join("\n")+"\n");
