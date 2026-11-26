// The loopback origin counts gzip payloads, including synchronous requests from SQLite workers.
import assert from "node:assert/strict";
import {createHash} from "node:crypto";
import {createServer} from "node:http";
import {readFile} from "node:fs/promises";
import {extname,resolve,sep} from "node:path";
import {chromium,firefox,webkit} from "playwright";

const engines = {chromium,firefox,webkit};
const mime = {".html":"text/html; charset=utf-8",".js":"text/javascript",".mjs":"text/javascript",
  ".css":"text/css",".json":"application/json",".wasm":"application/wasm",".woff2":"font/woff2",".png":"image/png"};
export async function localPackage(directory, {cache=false, delay=0}={}) {
  const root = resolve(directory);
  const state = {force:false, pieces:0, dbBytes:0};
  const server = createServer(async (req,res) => {
    const path = decodeURIComponent(new URL(req.url,"http://localhost").pathname);
    const file = resolve(root, "."+path+(path.endsWith("/") ? "index.html" : ""));
    try {
      if (!file.startsWith(root+sep)) throw Error("Invalid path");
      if (state.force && path.startsWith("/m/records/")) {
        res.writeHead(404,{"Cache-Control":"no-store"}).end(); return;
      }
      const bytes = await readFile(file);
      if (delay && path.startsWith("/db/")) await new Promise(r=>setTimeout(r,delay));
      if (path.startsWith("/db/")) {
        state.dbBytes+=bytes.length;
        if (path.includes("/p/")) state.pieces++;
      }
      res.writeHead(200,{"Content-Type":mime[extname(file)]||"application/octet-stream",
        "Content-Length":bytes.length,"Cache-Control":cache ? "public, max-age=3600" : "no-store"});
      res.end(bytes);
    } catch { res.writeHead(404).end(); }
  });
  await new Promise(r=>server.listen(0,"127.0.0.1",r));
  return {url:"http://127.0.0.1:"+server.address().port,state,
    reset() {Object.assign(state,{pieces:0,dbBytes:0});},
    async close() {server.closeAllConnections(); await new Promise(r=>server.close(r));}};
}

async function modules(root) {
  const data=JSON.parse(await readFile(resolve(root,"directory.json")));
  const samples=data.samples.filter(s=>s.type==="module").map(s=>({pkg:s.package,path:s.value,staticPath:"/sample/"+s.package+"/"+s.id+"/"}));
  const rows=await Promise.all(data.staticModules.map(async key=>{
    const staticPath="/m/records/"+key+"/";
    const html=await readFile(resolve(root,"."+staticPath,"index.html"),"utf8");
    const match=html.match(/<main\b[^>]*data-original-path="([^"]+)"/);
    assert.ok(match,staticPath);
    const path=match[1].replace(/&quot;/g,'"').replace(/&#39;|&#x27;/g,"'").replace(/&lt;/g,"<").replace(/&gt;/g,">").replace(/&amp;/g,"&");
    const [pkg,hash]=key.split("/");
    assert.equal(createHash("sha256").update(path).digest("hex").slice(0,16),hash);
    return {pkg,path,staticPath};
  }));
  return [...samples,...rows];
}
async function visit(page,url,input) {
  const started=performance.now();
  const response=await page.goto(url,{waitUntil:"domcontentloaded",timeout:30000});
  assert.equal(response.status(),200);
  await page.waitForFunction(path=>document.querySelector("main form.contribute")?.dataset.path===path,input,{polling:"raf",timeout:30000});
  const ms=Math.round(performance.now()-started);
  const hash=await page.locator("main").evaluate(async el=>{
    const bytes=await crypto.subtle.digest("SHA-256",new TextEncoder().encode(el.innerHTML));
    return Array.from(new Uint8Array(bytes), n=>n.toString(16).padStart(2,"0")).join("");
  });
  return {ms,hash};
}
// The preview bytes are public to this signed-out browser. Only the two forced-fallback
// requests are answered locally. Independent browser contexts make both visits cold.
async function measureStaging(browser, engine, root, base, limit) {
  const origin=new URL(base);
  assert.ok(origin.protocol==="https:" && origin.hostname.endsWith(".qed-codex.pages.dev"));
  const local=JSON.parse(await readFile(resolve(root,"proof.json")));
  const probe=await browser.newContext();
  try {
    const response=await probe.request.get(new URL("/proof.json",origin).href);
    assert.ok(response.ok());assert.deepEqual(await response.json(),local);
  } finally {await probe.close();}
  let records = await modules(root);
  if (limit && /^\d+$/.test(limit)) records = records.slice(0, Number(limit));
  else if (limit) {
    const selected = new Set((await readFile(limit, "utf8")).trimEnd().split("\n"));
    records = records.filter(r => selected.has(r.staticPath));
    assert.equal(records.length, selected.size, "Unknown static path in selection");
  }
  let next=0,done=0,failed=0;
  async function lane(){
    while(next<records.length){
      const {pkg,path,staticPath}=records[next++];
      const query=new URL("/m/",origin);query.search=new URLSearchParams({pkg,p:path});
      let fixed,actual,net,error="";
      try {
        for (const forced of [false,true]){
          const context=await browser.newContext();
          try{
            if(forced) {
              await context.route("**/m/records/**",r=>r.fulfill({status:404,body:""}));
              if(staticPath.startsWith("/sample/")) await context.route("**/select-static.js",r=>r.fulfill({
                contentType:"text/javascript",body:'document.querySelector("main").replaceChildren()'}));
            }
            const page=await context.newPage();
            if (!forced) fixed=await visit(page,new URL(staticPath,origin).href,path);
            else {
              actual=await visit(page,query.href,path);
              assert.ok(page.workers().length,"No SQLite worker");
              const resources=()=>performance.getEntriesByType("resource")
                .filter(e=>new URL(e.name).pathname.startsWith("/db/"))
                .map(e=>[new URL(e.name).pathname,e.transferSize]);
              const entries=(await Promise.all([page.evaluate(resources),...page.workers().map(w=>w.evaluate(resources))])).flat();
              net={pieces:entries.filter(([url])=>url.includes("/p/")).length,wire:entries.reduce((n,e)=>n+e[1],0)};
              assert.ok(net.pieces>0,"No observed database pieces");
              assert.equal(actual.hash,fixed.hash,"main subtree differs");
            }
          } finally {await context.close();}
        }
      } catch(e){error=e.message.replace(/\s+/g," ").slice(0,220);failed++;}
      console.log([engine,pkg,path,staticPath,fixed?.ms,actual?.ms,net?.pieces,net?.wire,fixed?.hash,actual?.hash,error].join("\t"));
      if(++done%500===0)console.error(engine,done,"of",records.length);
    }
  }
  await Promise.all(Array.from({length:4},lane));
  if(failed)throw Error(failed+" staging comparisons failed");
}

async function modulePairs(browser, engine, root) {
  const path = "Zeta23/FromPNTPlus/Auxiliary.lean";
  const server = await localPackage(root, {cache:true, delay:50});
  try {
    server.state.force = true;
    const query = new URL("/m/",server.url);
    query.search = new URLSearchParams({pkg:"zeta23",p:path});
    for (let trial=1;trial<=12;trial++) {
      const context = await browser.newContext();
      try {
        const page = await context.newPage();
        server.reset();
        const cold = await visit(page, query.href, path);
        const coldNet = {...server.state};
        assert.ok(coldNet.pieces>0, "Module must reach SQLite");
        server.reset();
        const warm = await visit(page, query.href, path);
        assert.equal(cold.hash, warm.hash);
        console.log([engine,trial,cold.ms,coldNet.pieces,coldNet.dbBytes,
          warm.ms,server.state.pieces,server.state.dbBytes].join("\t"));
      } finally {await context.close();}
    }
  } finally {await server.close();}
}

export async function measure(mode, root, engine, ...args) {
  assert.ok(Object.hasOwn(engines, engine), "Unknown browser engine");
  const browser = await engines[engine].launch({executablePath:process.env[engine.toUpperCase()+"_EXECUTABLE"]});
  try {
    if (mode === "--compare-staging") await measureStaging(browser, engine, root, ...args);
    else {
      assert.equal(mode, "--module-pairs");
      await modulePairs(browser, engine, root);
    }
  } finally {await browser.close();}
}
