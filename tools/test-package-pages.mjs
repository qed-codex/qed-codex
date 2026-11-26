import {readDirectoryProof} from "./read-directory-proof.mjs";
import assert from "node:assert/strict";
import {readFile} from "node:fs/promises";
import {chromium,firefox,webkit} from "playwright";
import {modulePage, newInformalization, route} from "../site/record.mjs";

const origin = new URL(process.argv[2]);
assert(["localhost","127.0.0.1"].includes(origin.hostname));
const proof = readDirectoryProof();
proof.repository = "https://github.com/qed-codex/qed-codex";
const path = "src/A & B.lean";
const fields = {handle:"example",writer:"Example writer",origin:"wrote"};
for (const pkg of Object.keys(proof.packages)) {
  const item = {facts:[{path,package:pkg,mask:null}], members:[],informalizations:[],links:[],disputes:[]};
  const html = modulePage(proof,item);
  if (pkg === "mathlib") {
    assert(!html.includes("Alpöge"));
    assert(!html.includes("mathlib4_docs"));
    assert(html.includes("This package has no declaration index yet."));
  }
  assert(html.includes("Theorem-use data unavailable"));
  assert(html.includes('data-package="'+pkg+'"'));
  assert(html.includes(encodeURIComponent(pkg+":"+path).replaceAll("%20","+")));
  const permalink = new URL(route("module",path,pkg),origin);
  assert.equal(permalink.searchParams.get("p"),path);
  const editor = new URL(newInformalization(path,fields,proof.packages[pkg].commit,proof.repository,pkg,proof.packages[pkg].hasDeclarationIndex));
  assert.equal(editor.searchParams.get("value").includes("Leave this list empty"), !proof.packages[pkg].hasDeclarationIndex);
  assert.equal(editor.searchParams.get("filename"),"packages/"+pkg+"/informalizations/"+path+"/example--example-writer.md");
  assert(editor.searchParams.get("value").includes(proof.packages[pkg].commit));
  // Proof membership and the displayed proof label do not enter the record identity.
  assert.equal(modulePage({...proof,title:"Another proof"},item),html);
}
for (const [engine,launcher] of Object.entries({chromium,firefox,webkit})) {
  const browser=await launcher.launch({executablePath:process.env[engine.toUpperCase()+"_EXECUTABLE"]});
  try {
    const page=await browser.newPage();
    const zeta = "Mathlib/NumberTheory/LSeries/RiemannZeta.lean";
    await page.goto(new URL(route("module",zeta,"mathlib"),origin).href);
    const docs=page.getByRole("link",{name:"Mathlib documentation (current version)",exact:true});
    await docs.waitFor();
    assert.equal(await docs.count(),1);
    assert.equal(await docs.getAttribute("href"),"https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html");
    await page.goto(new URL(route("module","MathlibTest/DefEqAbuse.lean","mathlib"),origin).href);
    await page.getByRole("link",{name:"Module permalink"}).waitFor();
    assert.equal(await docs.count(),0);
    for (const address of ["/m/?p=src%2FMain.lean","/d/?n=riemannHypothesis"]) {
      await page.goto(new URL(address,origin).href);
      await page.getByText(/Choose a (module|declaration) from the search page/).waitFor();
      assert.equal(await page.locator("article.record").count(),0);
    }
    await page.goto(new URL("/d/?pkg=mathlib&n=riemannHypothesis",origin).href);
    await page.getByRole("heading",{name:"Declaration not found"}).waitFor();
    assert.equal((await page.request.get(new URL("/sample/rowsrc/",origin).href)).status(),404);
    await page.goto(new URL("/d/?pkg=riemann-hypothesis&n=riemannHypothesis",origin).href);
    const copy=page.getByRole("link",{name:"Declaration permalink"});
    await copy.waitFor();
    assert.equal(new URL(await copy.getAttribute("href"),origin).searchParams.get("pkg"),"riemann-hypothesis");
    const canonical=page.locator("link[rel=canonical]");
    if (await canonical.count()) assert.equal(new URL(await canonical.getAttribute("href")).pathname,"/sample/riemann-hypothesis/rh/");
    await page.goto(new URL("/?q=galois",origin).href);
    const hit=page.locator("#matches a[href*='/d/?']").first();await hit.click();
    await page.getByRole("link",{name:"Declaration permalink"}).waitFor();
    await page.locator("p.path a[href^='/m/']").click();await page.getByRole("link",{name:"Module permalink"}).waitFor();
    await page.goBack();await page.getByRole("link",{name:"Declaration permalink"}).waitFor();
    await page.goBack();assert.equal(new URL(page.url()).searchParams.get("q"),"galois");
    console.log(engine,"package identity, missing/wrong package, permalink and Back passed");
  } finally {await browser.close();}
}
