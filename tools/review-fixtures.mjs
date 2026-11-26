import assert from "node:assert/strict";
import {readFile, writeFile} from "node:fs/promises";
import {chromium, firefox, webkit} from "playwright";
import {reviewOrigin} from "./review-origin.mjs";
const [address, engine, dir] = process.argv.slice(2);
const base = reviewOrigin(address);
const fixture = JSON.parse(await readFile(dir + "/fixtures.json"));
const browser = await ({chromium,firefox,webkit})[engine].launch({executablePath:process.env[engine.toUpperCase()+"_EXECUTABLE"]});
const receipt = {engine, version:browser.version(), origin:base, samples:[]};
async function run(page, traffic, q, state) {
  const {kind,value,expected} = q;
  await page.selectOption("#kind",kind);
  const mark=traffic.length;
  await page.evaluate(value=>{
    const input=document.querySelector("#value");
    input.value=value;
    input.dispatchEvent(new Event("input",{bubbles:true}));
    document.querySelector("form").requestSubmit();
  },value);
  await page.waitForFunction(()=>["Complete","Failed"].includes(document.querySelector("#state").textContent),null,{timeout:90000});
  assert.equal(await page.textContent("#state"),"Complete",await page.textContent("#result"));
  assert.deepEqual(JSON.parse(await page.textContent("#result")),expected);
  const requests=traffic.slice(mark);
  const paths=requests.map(r=>new URL(r.url()).pathname);
  assert.equal(new Set(paths).size,paths.length);
  for(const r of requests) {
    assert.equal(r.headers().range,undefined);
    const response=await r.response();
    assert.equal(response?.status(),200,r.url());
    assert.match(await response.headerValue("cache-control"),/immutable/);
  }
  if(state==="cold") assert.equal(paths.filter(p=>p.endsWith("/interior")).length,1);
  if(state==="repeat") assert.equal(paths.length,0);
  const limit={module:state==="warm"?12:25,typeahead:5,search:20}[kind];
  if(limit!==undefined) assert.ok(paths.length<=limit,kind+" "+state+" "+value+" fetched "+paths.length+" files; budget "+limit);
  return {kind,value,state,files:paths.length};
}
try {
  for(const q of fixture.queries) {
    for(const primed of [false,true]) {
      const context=await browser.newContext();
      const traffic=[];
      context.on("request",r=>{const u=new URL(r.url()); if(u.origin===base && u.pathname.startsWith("/db/")) traffic.push(r);});
      try {
        const page=await context.newPage();
        const r=await page.goto(base+"/probe.html",{waitUntil:"networkidle"});
        assert.equal(r.status(),200);
        assert.equal(await page.evaluate(()=>self.crossOriginIsolated),false);
        if(primed) await run(page,traffic,fixture.prime,"primer");
        receipt.samples.push(await run(page,traffic,q,primed?"warm":"cold"));
        if(!primed) receipt.samples.push(await run(page,traffic,q,"repeat"));
      } finally {await context.close();}
    }
    await writeFile(dir+"/fixtures-"+engine+".json",JSON.stringify(receipt,null,2)+"\n");
    console.log(engine, q.kind,q.value,receipt.samples.slice(-3).map(r=>r.files).join("/"));
  }
  assert.equal(receipt.samples.length,42);
} finally {await browser.close();}
