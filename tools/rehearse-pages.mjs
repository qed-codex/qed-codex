// Run the installed Wrangler against a loopback receiver that checks every asset.
import assert from "node:assert/strict";
import http from "node:http";
import {spawn} from "node:child_process";
import {createHash} from "node:crypto";
import {mkdtemp, readFile, readdir, rm} from "node:fs/promises";
import {tmpdir} from "node:os";
import {join, relative, resolve} from "node:path";
import {once} from "node:events";

const [directory, commit] = process.argv.slice(2);
assert.match(commit,/^[a-f\d]{40}$/);
const root = resolve(directory), expected = new Map(), uploads = new Map();
const sha = b => createHash("sha256").update(b).digest("hex");
for (const entry of await readdir(root,{recursive:true,withFileTypes:true})) {
  if (!entry.isFile()) continue;
  const path = join(entry.parentPath,entry.name);
  expected.set("/"+relative(root,path),sha(await readFile(path)));
}
const project = "/accounts/"+ "0".repeat(32) +"/pages/projects/qed-codex";
let verified = false, total = 0;
const server = http.createServer(async (req,res) => {
  try {
    const chunks=[]; for await (const chunk of req) chunks.push(chunk);
    const body=Buffer.concat(chunks), path=new URL(req.url,"http://localhost").pathname;
    let result;
    if (path===project && req.method==="GET") result={name:"qed-codex",production_branch:"main",deployment_configs:{production:{}}};
    else if (path===project+"/upload-token") result={jwt:["fixture", Buffer.from(JSON.stringify({exp:4102444800})).toString("base64url"), "fixture"].join(".")};
    else if (path==="/pages/assets/check-missing") result=JSON.parse(body).hashes;
    else if (path==="/pages/assets/upload") {
      for (const asset of JSON.parse(body)) {
        const bytes=Buffer.from(asset.value,"base64");
        total+=bytes.length;
        uploads.set(asset.key,sha(bytes));
      }
      result={};
    } else if (path==="/pages/assets/upsert-hashes") result={};
    else if (path===project+"/deployments" && req.method==="POST") {
      const form=await new Response(body,{headers:{"content-type":req.headers["content-type"]}}).formData();
      assert.equal(form.get("branch"),"main"); assert.equal(form.get("commit_hash"),commit);
      assert.equal(sha(Buffer.from(await form.get("_headers").arrayBuffer())),expected.get("/_headers"));
      const manifest=JSON.parse(form.get("manifest"));
      assert.equal(Object.keys(manifest).length,expected.size-1);
      for (const [name,hash] of Object.entries(manifest)) {
        assert(expected.has(name)); assert.equal(uploads.get(hash),expected.get(name),name);
      }
      verified=true; result={id:"local",url:"http://localhost/"};
    } else if (path===project+"/deployments/local") result={latest_stage:{name:"deploy",status:"success"},aliases:[]};
    else throw Error("Unexpected mock route "+path);
    res.writeHead(200,{"content-type":"application/json"});res.end(JSON.stringify({success:true,result,errors:[],messages:[]}));
  } catch (err) {
    console.error(err.message);
    res.writeHead(400,{"content-type":"application/json"});res.end(JSON.stringify({success:false,errors:[{code:1,message:"Local validation failed"}]}));
  }
});
await new Promise(ok=>server.listen(0,"127.0.0.1",ok));
const temp=await mkdtemp(join(tmpdir(),"qed-pages-"));
try {
  const child=spawn(resolve("node_modules/.bin/wrangler"),["pages","deploy",root,"--project-name","qed-codex","--branch","main","--commit-hash",commit,"--commit-dirty=false"],{
    cwd:temp,stdio:["ignore","pipe","pipe"],env:{PATH:process.env.PATH, XDG_CONFIG_HOME:temp, CI:"1",
      WRANGLER_SEND_METRICS:"false",CLOUDFLARE_ACCOUNT_ID:"0".repeat(32), CLOUDFLARE_API_TOKEN:"local-fixture",
      CLOUDFLARE_API_BASE_URL:"http://127.0.0.1:"+server.address().port}});
  const log=[];child.stdout.on("data",x=>log.push(x));child.stderr.on("data",x=>log.push(x));
  const [code]=await once(child,"close");if(code!==0) throw Error(Buffer.concat(log).toString());
  assert(verified);
  console.log(JSON.stringify({ledgerCommit:commit,files:expected.size,manifestAssets:expected.size-1,
    distinctAssetHashes:uploads.size,assetPayloadBytes:total,headersSha256:expected.get("/_headers")},null,2));
} finally {server.closeAllConnections();server.close();await rm(temp,{recursive:true,force:true});}
