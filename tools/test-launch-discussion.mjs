// Fixture mode exercises our integration offline. Live mode uses the real widget.
import assert from "node:assert/strict";
import {fileURLToPath} from "node:url";
import {chromium, firefox, webkit} from "playwright";

const [address, mode] = process.argv.slice(2);
const origin = new URL(address);
assert(["--fixture","--live"].includes(mode));
if (mode === "--fixture") assert(["127.0.0.1","localhost"].includes(origin.hostname));
else assert(origin.protocol === "https:" || ["127.0.0.1","localhost"].includes(origin.hostname));
for (const [engine, launcher] of Object.entries({chromium,firefox,webkit})) {
  const browser = await launcher.launch({executablePath:process.env[engine.toUpperCase()+"_EXECUTABLE"]});
  try {
    for (const path of ["/sample/riemann-hypothesis/rowsrc/","/m/?pkg=riemann-hypothesis&p=src%2FMain.lean"]) {
      const page = await browser.newPage();
      const mapped = [];
      await page.addInitScript(() => {
        window.parentViolations = [];
        document.addEventListener("securitypolicyviolation", e => window.parentViolations.push(e.effectiveDirective));
      });
      if (mode === "--fixture") {
        await page.route("**/*", route => new URL(route.request().url()).origin === origin.origin
          ? route.continue() : route.abort());
        await page.route("https://giscus.app/client.js", route => route.fulfill({
          path:fileURLToPath(new URL("./fixtures/giscus-client.js",import.meta.url)),
          contentType:"text/javascript", headers:{"Access-Control-Allow-Origin":"*"},
        }));
      }
      await page.route("https://giscus.app/**/widget?**", async route => {
        const url = new URL(route.request().url());
        mapped.push({term:url.searchParams.get("term"), repo:url.searchParams.get("repo"), strict:url.searchParams.get("strict")});
        if (mode === "--live") return route.continue();
        await route.fulfill({path:fileURLToPath(new URL("./fixtures/giscus-widget.html",import.meta.url)),
          contentType:"text/html"});
      });
      const response = await page.goto(new URL(path,origin).href,{waitUntil:"domcontentloaded"});
      assert.match(response.headers()["content-security-policy"], /script-src[^;]* https:\/\/giscus\.app;/);
      await page.frameLocator("iframe.giscus-frame").getByText(/sign in with github/i).first().waitFor({timeout:45000});
      assert.equal(await page.locator(".giscus-frame").count(),1);
      assert.deepEqual(mapped,[{term:"module:riemann-hypothesis:" + await page.locator("form.contribute").getAttribute("data-path"),
        repo:"qed-codex/qed-codex",strict:"1"}]);
      assert.deepEqual(await page.evaluate(()=>window.parentViolations),[]);
      console.log(JSON.stringify({engine,version:browser.version(),path,term:mapped[0].term,mode,widgetReady:true}));
      await page.close();
    }
    if (mode === "--fixture") {
      const page = await browser.newPage();
      await page.route("**/*", route => new URL(route.request().url()).origin === origin.origin
        ? route.continue() : route.abort());
      const errors = [];
      page.on("pageerror", error => errors.push(error.message));
      const pending = Promise.withResolvers();
      await page.route("**/discussion.json", async route => {
        await pending.promise;
        await route.fulfill({status:404, contentType:"text/plain", body:"Missing configuration"});
      });
      const missing = page.waitForResponse(r => r.url().endsWith("/discussion.json") && r.status() === 404);
      try {
        await page.goto(new URL("/m/?pkg=riemann-hypothesis&p=src%2FMain.lean",origin).href,{waitUntil:"commit"});
        await page.getByRole("heading",{name:"Main.lean",exact:true}).waitFor();
      } finally { pending.resolve(); }
      await missing;
      await page.getByText("Discussion opens at launch",{exact:true}).waitFor();
      assert.equal(await page.locator("iframe.giscus-frame").count(),0);
      const homeScript = Promise.withResolvers();
      await page.route("**/directory.mjs", async route => {
        await homeScript.promise;
        await route.continue();
      });
      // Exercise a keystroke before the home page has finished attaching its handlers.
      await page.getByRole("link",{name:"QED Codex",exact:true}).click({noWaitAfter:true});
      try {
        await page.getByRole("searchbox").fill("anyGeometry");
      } finally { homeScript.resolve(); }
      const hit = page.getByRole("link",{name:"GlobalTheory.Mem.Top.Bl.anyGeometry",exact:true});
      await hit.click();
      await page.getByRole("heading",{name:"anyGeometry",exact:true}).waitFor();
      assert.deepEqual(errors,[]);
      console.log(JSON.stringify({engine,version:browser.version(),configStatus:404,
        moduleRenderedBeforeConfig:true,searchOpenedDeclaration:true,pageErrors:errors.length}));
      await page.close();
    }
  } finally {await browser.close();}
}
