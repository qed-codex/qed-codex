// Record the captured live page and the matching compiled section at both widths.
import {chromium} from "playwright";
import {createHash} from "node:crypto";
import {mkdir,readFile,writeFile} from "node:fs/promises";
import {join} from "node:path";
import assert from "node:assert/strict";

const [site, capture] = process.argv.slice(2);
const report = "reports/permission-statements";
const out = join(report,"screenshots");
await mkdir(out,{recursive:true});
const {sample} = JSON.parse(await readFile(join(report,"live-sample.json")));
const index = await (await fetch(new URL("/informalizations.json",site))).json();
const rows = new Map(index.filter(x=>x.writer==="Andrew O'Desky").map(x=>[x.module,x]));
const browser = await chromium.launch();
const inventory = ["file\twidth\theight\tsha256"];
const comparisons = [];
// Independent of the Python renderer. For each font command occurring in this
// sample, derive its code point from the Unicode alphabet (and its historic holes).
// Refuse unfamiliar argument syntax so a new sample cannot silently skip a letter.
const alphabets = {
  mathbb: [0x1d538, 0x1d552, 0x1d7d8, {C:"ℂ", H:"ℍ", N:"ℕ", P:"ℙ", Q:"ℚ", R:"ℝ", Z:"ℤ"}],
  mathcal: [0x1d49c, 0x1d4b6, null, {B:"ℬ", E:"ℰ", F:"ℱ", H:"ℋ", I:"ℐ", L:"ℒ",
    M:"ℳ", R:"ℛ", e:"ℯ", g:"ℊ", o:"ℴ"}],
  mathfrak: [0x1d504, 0x1d51e, null, {C:"ℭ", H:"ℌ", I:"ℑ", R:"ℜ", Z:"ℨ"}],
  mathsf: [0x1d5a0, 0x1d5ba, 0x1d7e2, {}],
  mathbf: [0x1d400, 0x1d41a, 0x1d7ce, {}],
};
alphabets.mathscr = alphabets.mathcal;

function sourceLetters(tex) {
  const letters = [];
  for (const match of tex.matchAll(/\\([A-Za-z]+)/gu)) {
    const command = match[1];
    if (!(command in alphabets)) {
      if (/^(mathit|mathtt|mathbfit|mathsfit|mathnormal|boldsymbol|bm|Bbb|bf|frak|scr|cal|sf|tt)$/u.test(command))
        throw Error("Reference alphabet required for " + match[0]);
      continue;
    }
    const arg = /^\s*(?:\{([A-Za-z0-9 ]+)\}|([A-Za-z0-9]))/u.exec(tex.slice(match.index + match[0].length));
    assert.ok(arg, "Unsupported font argument in " + tex);
    const [upper, lower, digit, holes] = alphabets[command];
    for (const ch of (arg[1] ?? arg[2]).replaceAll(" ", "")) {
      const base = /[A-Z]/u.test(ch) ? upper : /[a-z]/u.test(ch) ? lower : digit;
      assert.notEqual(base, null);
      const start = /[A-Z]/u.test(ch) ? 65 : /[a-z]/u.test(ch) ? 97 : 48;
      const glyph = holes[ch] ?? String.fromCodePoint(base + ch.codePointAt(0) - start);
      letters.push({command, letter:ch, expected:glyph});
    }
  }
  return letters;
}

async function compareGlyphs(original, rendered) {
  const source = await original.locator('.katex annotation[encoding="application/x-tex"]').allTextContents();
  const output = await rendered.locator("math").evaluateAll(nodes => nodes.map(n => n.textContent));
  assert.equal(source.length, output.length);
  const records = [];
  for (const [i, tex] of source.entries()) {
    let pos = 0;
    for (const letter of sourceLetters(tex)) {
      const index = output[i].indexOf(letter.expected, pos);
      assert.ok(index >= 0, `Formula ${i+1} in ${tex} needs ${letter.expected}, got ${output[i]}`);
      const actual = String.fromCodePoint(output[i].codePointAt(index));
      records.push({formula:i+1, ...letter, actual});
      pos = index + actual.length;
    }
  }
  return records;
}
const glyphReport = [];
function fingerprint(root,selector) {
  const clone=root.cloneNode(true);
  const formulas=[...clone.querySelectorAll(selector)];
  for (const element of formulas) element.replaceWith(document.createTextNode("@MATH@"));
  return {math:formulas.length, text:clone.textContent.replace(/\s+/gu,""),
    links:[...clone.querySelectorAll("a")].map(a=>a.href), viewport:innerWidth,
    documentOverflow:document.documentElement.scrollWidth>innerWidth};
}
async function photo(page,section,name) {
  await page.evaluate(async()=> {await document.fonts.ready; scrollTo(0,0);});
  const clip=await section.evaluate(el=>{
    const rect=el.getBoundingClientRect();
    return {x:0,y:Math.max(0,Math.floor(rect.top+scrollY)),width:innerWidth,height:Math.ceil(rect.height)+1};
  });
  const image=await page.screenshot({clip,fullPage:true,animations:"disabled",timeout:45000});
  await writeFile(join(out,name),image);
  inventory.push([name,image.readUInt32BE(16),image.readUInt32BE(20),createHash("sha256").update(image).digest("hex")].join("\t"));
}
try {
  const context=await browser.newContext({viewport:{width:1280,height:900},colorScheme:"light"});
  const live=await context.newPage(), local=await context.newPage();
  // Use the captured response at its actual address, retaining the site's CSS,
  // fonts, math scripts, relative URL resolution and layout on resize.
  await live.route("**/*",async route=>{
    const req=route.request();
    if (req.isNavigationRequest() && req.frame()===live.mainFrame()) {
      const card=sample.find(c=>req.url()===c.url);
      if (!card) return route.abort();
      const bytes=await readFile(join(capture,"single-pages",card.id+".html"));
      assert.equal(createHash("sha256").update(bytes).digest("hex"),card.sha256);
      return route.fulfill({body:bytes,contentType:"text/html; charset=utf-8"});
    }
    if (/\/comments\/|\/js\/plausible/.test(req.url())) return route.abort();
    return route.continue();
  });
  for (const card of sample) {
    const result=rows.get(card.module);
    const addr=new URL(result.page);
    await live.goto(card.url,{waitUntil:"load"});
    await local.goto(new URL(addr.pathname,site).href);
    const original=live.locator(".stmt").first();
    const entry=local.locator('[id="'+decodeURIComponent(addr.hash.slice(1))+'"]');
    // Isolate these siblings within the actual informalization without changing its layout.
    await entry.evaluate((entry,url)=>{
      const meta=[...entry.querySelectorAll("h2 + p")].find(p=>p.querySelector("a")?.href===url);
      if(!meta) throw Error("Statement heading missing");
      const wrapper=document.createElement("div"); wrapper.className="comparison-statement";
      let sibling=meta.nextElementSibling;
      meta.after(wrapper);
      while(sibling && sibling.tagName!=="H2"){const next=sibling.nextElementSibling;wrapper.append(sibling);sibling=next;}
    },card.source);
    const rendered=entry.locator(".comparison-statement");
    const expected=await rendered.locator("math").count();
    if(expected) await live.waitForFunction(()=>document.querySelector(".stmt .katex, .stmt .katex-error"),null,{timeout:20000});
    for(const width of [380,1280]){
      await Promise.all([local,live].map(p=>p.setViewportSize({width,height:900})));
      const compare=async(locator,selector)=>locator.evaluate(fingerprint,selector);
      const a=await compare(original,".katex"), b=await compare(rendered,"math");
      const record={id:card.id,width,liveMath:a.math,localMath:b.math,liveKatexErrors:await original.locator(".katex-error").count(),
        sameProse:a.text===b.text,sameLinks:JSON.stringify(a.links)===JSON.stringify(b.links),
        sourcePageOverflow:a.documentOverflow,modulePageOverflow:b.documentOverflow};
      assert.ok(record.sameProse && record.sameLinks && !record.modulePageOverflow && !record.liveKatexErrors, card.id);
      assert.equal(a.math, b.math, card.id);
      const letters = await compareGlyphs(original, rendered);
      if (width === 380) glyphReport.push({id:card.id, formulas:a.math, letters});
      else assert.deepEqual(letters, glyphReport.at(-1).letters);
      record.styledGlyphsMatched = letters.length;
      comparisons.push(record);
      await photo(live,original,card.id+"-"+width+"-source.png");
      await photo(local,rendered,card.id+"-"+width+"-directory.png");
    }
    console.log(card.id,comparisons.at(-1).sameProse,comparisons.at(-1).sameLinks);
  }
} finally {
  await browser.close();
  await writeFile(join(out,"inventory.tsv"),inventory.join("\n")+"\n");
  await writeFile(join(report,"sample-glyphs.json"),JSON.stringify(glyphReport,null,2)+"\n");
  await writeFile(join(report,"visual-checks.json"),JSON.stringify(comparisons,null,2)+"\n");
}
