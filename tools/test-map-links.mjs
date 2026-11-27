// A single outside page explains both declarations in this module in the recorded TSV.
import assert from "node:assert/strict";
import {chromium,firefox,webkit} from "playwright";
import {route} from "../site/record.mjs";
const origin = new URL(process.argv[2]);
assert(["localhost","127.0.0.1"].includes(origin.hostname));
const pkg = "riemann-hypothesis";
const path = "src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ContinuousConjFin.lean";
const outside = "https://andrewodesky.com/rh/lean/GlobalTheory.CuspRep.CuspSub/";
for (const [engine,launcher] of Object.entries({chromium,firefox,webkit})) {
  const browser = await launcher.launch({executablePath:process.env[engine.toUpperCase()+"_EXECUTABLE"]});
  try {
    const page = await browser.newPage();
    for (const [kind,name] of [["module",path],["declaration","GlobalTheory.CuspRep.Eop"],
                               ["declaration","GlobalTheory.CuspRep.Zalg"]]) {
      await page.goto(new URL(route(kind,name,pkg),origin).href);
      const link = page.locator("main section").filter({has:page.getByRole("heading",{name:"Elsewhere",exact:true})}).locator('a[href="'+outside+'"]');
      await link.first().waitFor();
      assert.equal(await link.count(),1);
      assert.ok((await link.innerText()).trim());
    }
    console.log(engine,"one module link and both named declaration links passed");
  } finally { await browser.close(); }
}
