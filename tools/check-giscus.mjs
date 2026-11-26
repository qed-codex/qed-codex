// Read an existing discussion signed out. The check never submits a comment.
import assert from "node:assert/strict";
import http from "node:http";
import { chromium, firefox, webkit } from "playwright";

const engines = {chromium, firefox, webkit};
const selected = process.argv.slice(2);
const script = `<script src="https://giscus.app/client.js" data-repo="giscus/react-giscus"
data-repo-id="MDEwOlJlcG9zaXRvcnkzODMxNjMyOTY=" data-category="General"
data-category-id="DIC_kwDOFtaboM4B-N2d" data-mapping="number" data-term="1"
data-reactions-enabled="0" data-input-position="top" data-theme="light"
data-lang="en" crossorigin="anonymous" async></script>`;

const server = http.createServer((req, res) => {
  const headers = {"Content-Type": "text/html; charset=utf-8"};
  if (req.url === "/isolated") {
    headers["Cross-Origin-Opener-Policy"] = "same-origin";
    headers["Cross-Origin-Embedder-Policy"] = "require-corp";
  }
  res.writeHead(200, headers);
  res.end(`<!doctype html><meta charset="utf-8"><title>Widget check</title>
    <main><div class="giscus"></div>${script}</main>`);
});
await new Promise(resolve => server.listen(0, "127.0.0.1", resolve));
try {
  for (const name of selected.length ? selected : Object.keys(engines)) {
    const browser = await engines[name].launch({executablePath: process.env[name.toUpperCase() + "_EXECUTABLE"]});
    try {
      for (const mode of ["control", "isolated"]) {
        const page = await browser.newPage();
        const failedRequests = [];
        page.on("requestfailed", request => failedRequests.push(new URL(request.url()).pathname));
        await page.goto(`http://127.0.0.1:${server.address().port}/${mode}`, {waitUntil: "domcontentloaded"});
        const frame = page.frameLocator("iframe.giscus-frame");
        const signIn = frame.getByText(/sign in with github/i).first();
        const widgetReady = await signIn.waitFor({state: "visible", timeout: 15000}).then(() => true, () => false);
        const isolated = await page.evaluate(() => self.crossOriginIsolated);
        console.log(JSON.stringify({engine: name, version: browser.version(), mode, isolated, widgetReady, failedRequests}));
        assert.equal(isolated, mode === "isolated", "The test page should apply the requested headers");
        assert.equal(widgetReady, mode === "control", "Widget behavior changed");
        await page.close();
      }
    } finally {
      await browser.close();
    }
  }
} finally {
  server.closeAllConnections();
  await new Promise(resolve => server.close(resolve));
}
