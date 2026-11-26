// node tools/search-pairs.mjs BASE_URL SEED DATABASE
import assert from "node:assert/strict";
import {createHash} from "node:crypto";
import {DatabaseSync} from "node:sqlite";
import {chromium,firefox,webkit} from "playwright";

const [base,seed,database,mode="repeat"]=process.argv.slice(2);
assert.ok(["repeat","different"].includes(mode));
const db=new DatabaseSync(database,{readOnly:true});
db.function("sample_key",{deterministic:true},text =>
  createHash("sha256").update(seed).update("\0").update(text).digest("hex"));
const names=db.prepare("SELECT DISTINCT short FROM shortnames WHERE short<>'' ORDER BY sample_key(short),short LIMIT 20").all();
db.close();
function databaseBytes() {
  return performance.getEntriesByType("resource").filter(e=>new URL(e.name).pathname.startsWith("/db/"))
    .reduce((n,e)=>n+e.transferSize,0);
}
async function total(page) {
  const parts=await Promise.all([page.evaluate(databaseBytes),...page.workers().map(w=>w.evaluate(databaseBytes))]);
  return parts.reduce((a,b)=>a+b,0);
}
console.log("engine\tversion\tcold_query\twarm_query\tcold_ms\tcold_db_bytes\twarm_ms\twarm_db_bytes");
for (const [engine,launcher] of Object.entries({chromium,firefox,webkit})) {
  const browser=await launcher.launch({executablePath:process.env[engine.toUpperCase()+"_EXECUTABLE"]});
  try {
    for (const [index,{short}] of names.entries()) {
      const context=await browser.newContext();
      try {
        const page=await context.newPage();
        await page.addInitScript(()=>performance.setResourceTimingBufferSize(8192));
        page.on("worker",w=>w.evaluate(()=>performance.setResourceTimingBufferSize(8192)).catch(()=>{}));
        const warm = mode === "different" ? names[(index+1)%names.length].short : short;
        const fields=[engine,browser.version(),short,warm];
        let previous=0;
        for(const phase of ["cold","warm"]) {
          const start=performance.now();
          if(phase==="cold"){
            const url=new URL("/",base);url.searchParams.set("q",short);
            await page.goto(url.href,{waitUntil:"domcontentloaded"});
          }else{
            // Remove the previous result nodes so completion requires a second response.
            await page.evaluate(term=>{document.querySelector("#matches").replaceChildren();const form=document.querySelector(".search-box");form.querySelector("input").value=term;form.requestSubmit()},warm);
          }
          await page.waitForFunction(()=>/^[\d,]+ results?$/.test(document.querySelector("#matches .search-total")?.textContent??""));
          const ms=Math.round(performance.now()-start);
          const name=new URL(await page.locator("#matches li a").first().getAttribute("href"),base).searchParams;
          const last=name.has("n")?name.get("n").split(".").at(-1):name.get("p").split("/").at(-1).replace(/\.lean$/,"");
          assert.equal(last.toLowerCase(),phase==="cold" ? short : warm);
          const current=await total(page);
          assert.ok(current>=previous);
          fields.push(ms,current-previous);previous=current;
        }
        console.log(fields.join("\t"));
      }finally{await context.close();}
    }
  }finally{await browser.close();}
}
