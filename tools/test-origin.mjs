import assert from "node:assert/strict";
import {chromium,firefox,webkit} from "playwright";

const base = new URL(process.argv[2]);
assert(["localhost","127.0.0.1"].includes(base.hostname));
for (const [engine,driver] of Object.entries({chromium,firefox,webkit})) {
  const browser = await driver.launch({executablePath:process.env[engine.toUpperCase()+"_EXECUTABLE"]});
  try {
    for (const origin of ["wrote","generated","other-author"]) {
      const page = await browser.newPage();
      await page.route("https://github.com/*/*/new/main?*", r => r.fulfill({body:"Editor fixture"}));
      await page.goto(new URL("/sample/riemann-hypothesis/rowsrc/",base).href);
      const permanent = page.getByRole("link",{name:"Permalink",exact:true});
      const entry = new URL(await permanent.first().getAttribute("href"),base);
      assert.equal(entry.hash,"#informalization-dial481--codex-gpt-6-2-astra");
      await page.goto(entry.href);
      const record = page.locator(entry.hash);
      await record.waitFor();
      await page.waitForFunction(id => Math.abs(document.getElementById(id).getBoundingClientRect().top)<2,entry.hash.slice(1));
      assert.equal(await record.locator(".meta strong").innerText(),"Codex (GPT-6.2 Astra)");
      const form = page.locator(".contribute"), submit = form.getByRole("button");
      assert(await submit.isDisabled());
      assert.equal(await form.locator("select:visible").count(),1);
      await form.getByLabel("GitHub handle").fill("fixture-reader");
      await form.getByLabel("Writer (person or model)").fill("Écrivain 一");
      await form.getByLabel("Origin",{exact:true}).selectOption(origin);
      assert.equal(await form.getByLabel("Original source URL").isVisible(),origin==="other-author");
      await form.getByRole("checkbox", {name: origin==="other-author" ? "This text is published under the licence I selected, and I have copied its notices exactly." : "I have the right to submit this under CC BY 4.0."}).check();
      if (origin==="other-author") {
        assert(await submit.isDisabled());
        await form.getByLabel("Licence the source states").selectOption("MIT");
        await form.getByLabel("Where the source states the licence").fill("https://example.org/LICENSE");
        await form.getByLabel("Copyright line exactly").fill("none in the source");
        await form.getByLabel("Changes made").fill("none");
        await form.getByLabel("Original source URL").fill("https://example.org/work");
      }
      const request = page.waitForRequest(r=>r.url().includes("/new/main?"));
      await submit.click();
      const q = new URL((await request).url()).searchParams;
      assert(q.get("filename").endsWith("/fixture-reader--écrivain-一.md"));
      const text=q.get("value");
      assert(text.includes("origin: "+origin) && text.includes("license: "+(origin==="other-author" ? "MIT" : "CC-BY-4.0")));
      assert.equal(text.includes("https://example.org/work"), origin==="other-author");
      assert.equal(text.match(/^kind: (.+)$/m)?.[1], {wrote:"human",generated:"ai"}[origin]);
      assert(!/^(?:certificate|tool|model):/m.test(text));
      await page.close();
    }
    console.log(engine,browser.version(),"passed three form origins");
  } finally {await browser.close();}
}
