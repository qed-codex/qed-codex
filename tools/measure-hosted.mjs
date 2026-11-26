import assert from "node:assert/strict";
import http from "node:http";
import net from "node:net";
import { readFile, writeFile } from "node:fs/promises";
import { chromium } from "playwright";
const [hostFile, fixtureFile, output] = process.argv.slice(2);
const host = (await readFile(hostFile, "utf8")).trim();
assert(/^[a-f0-9]+\.qed-codex\.pages\.dev$/.test(host));
const fixtures = JSON.parse(await readFile(fixtureFile));
const wire = { sent: 0, received: 0 },
  sockets = new Set();
// Count encrypted records without terminating browser TLS or retaining the origin.
const proxy = http.createServer();
proxy.on("connect", (req, client, head) => {
  if (req.url !== host + ":443") {
    client.end("HTTP/1.1 403 Forbidden\r\n\r\n");
    return;
  }
  const remote = net.connect(443, host, () => {
    client.write("HTTP/1.1 200 Connection Established\r\n\r\n");
    if (head.length) {
      wire.sent += head.length;
      remote.write(head);
    }
    client.on("data", (b) => (wire.sent += b.length));
    remote.on("data", (b) => (wire.received += b.length));
    client.pipe(remote);
    remote.pipe(client);
  });
  for (const s of [client, remote]) {
    sockets.add(s);
    s.on("close", () => sockets.delete(s));
  }
  remote.on("error", () => client.destroy());
  client.on("error", () => remote.destroy());
  client.on("close", () => remote.destroy());
  remote.on("close", () => client.destroy());
});
await new Promise((resolve) => proxy.listen(0, "127.0.0.1", resolve));
const browser = await chromium.launch({
  proxy: { server: "http://127.0.0.1:" + proxy.address().port },
  args: ["--disable-quic"],
});
const report = {
  browser: browser.version(),
  transport: "Direct browser TLS through a byte-counting CONNECT tunnel",
  samples: [],
};
async function instrument(page) {
  const session = await page.context().newCDPSession(page),
    requests = new Map(),
    finished = [];
  await session.send("Network.enable");
  session.on("Network.requestWillBeSent", ({ requestId, request }) => {
    const u = new URL(request.url);
    if (u.host === host && u.pathname.startsWith("/db/")) {
      assert(
        !Object.keys(request.headers).some((h) => h.toLowerCase() === "range"),
      );
      requests.set(requestId, {
        asset: u.pathname.split("/").slice(3).join("/"),
      });
    }
  });
  session.on("Network.responseReceived", ({ requestId, response }) => {
    const row = requests.get(requestId);
    if (!row) return;
    const headers = Object.fromEntries(
      Object.entries(response.headers).map(([k, v]) => [k.toLowerCase(), v]),
    );
    Object.assign(row, {
      status: response.status,
      protocol: response.protocol,
      contentEncoding: headers["content-encoding"] || "identity",
      cache: headers["cache-control"] || "",
      type: headers["content-type"] || "",
      fromCache: !!response.fromDiskCache,
    });
  });
  session.on("Network.dataReceived", ({ requestId, dataLength }) => {
    const r = requests.get(requestId);
    if (r) r.bodyBytes = (r.bodyBytes || 0) + dataLength;
  });
  session.on("Network.loadingFinished", ({ requestId, encodedDataLength }) => {
    const row = requests.get(requestId);
    if (row) {
      row.encodedResponseBytes = encodedDataLength;
      finished.push(row);
      requests.delete(requestId);
    }
  });
  return finished;
}
function delta(before) {
  return {
    sent: wire.sent - before.sent,
    received: wire.received - before.received,
    total: wire.sent + wire.received - before.sent - before.received,
  };
}
async function run(page, rows, q, state) {
  await page.selectOption("#kind", q.kind);
  const mark = rows.length,
    before = { ...wire };
  const elapsedMs = await page.evaluate((value) => {
    const input = document.querySelector("#value"),
      label = document.querySelector("#state");
    const t = performance.now();
    input.value = value;
    input.dispatchEvent(new Event("input", { bubbles: true }));
    return new Promise((resolve, reject) => {
      const timeout = setTimeout(() => {
        obs.disconnect();
        reject(Error("Hosted query timed out"));
      }, 45000);
      const obs = new MutationObserver(() => {
        if (!["Complete", "Failed"].includes(label.textContent)) return;
        clearTimeout(timeout);
        obs.disconnect();
        if (label.textContent === "Failed")
          reject(Error("Hosted query failed"));
        else resolve(performance.now() - t);
      });
      obs.observe(label, { childList: true });
      document.querySelector("form").requestSubmit();
    });
  }, q.value);
  // Capture the interval before asking the browser for the completed result.
  const tls = delta(before);
  assert.deepEqual(JSON.parse(await page.textContent("#result")), q.expected);
  const files = rows.slice(mark);
  assert.equal(new Set(files.map((x) => x.asset)).size, files.length);
  for (const r of files) {
    assert.equal(r.status, 200);
    assert(!r.fromCache);
    assert(r.cache.includes("immutable"));
    assert(r.bodyBytes > 0);
    assert(r.encodedResponseBytes > 0);
  }
  if (state === "cold")
    assert.equal(files.filter((x) => x.asset === "interior").length, 1);
  if (state === "repeat") assert.equal(files.length, 0);
  if (state === "warm") assert(!files.some((x) => x.asset === "interior"));
  const budget = {
    module: state === "warm" ? 12 : 25,
    typeahead: 5,
    search: 20,
  }[q.kind];
  if (budget) assert(files.length <= budget);
  return {
    kind: q.kind,
    value: q.value,
    state,
    elapsedMs: Math.round(elapsedMs * 10) / 10,
    tls,
    files: files.length,
    databasePayload: files.reduce((n, x) => n + x.bodyBytes, 0),
    databaseEncodedResponses: files.reduce(
      (n, x) => n + x.encodedResponseBytes,
      0,
    ),
    requests: files,
  };
}
try {
  for (const fixture of fixtures.queries) {
    for (const state of ["cold", "warm"]) {
      const ctx = await browser.newContext();
      try {
        const page = await ctx.newPage();
        const rows = await instrument(page);
        const before = { ...wire };
        const nav = await page.goto("https://" + host + "/", {
          waitUntil: "networkidle",
          timeout: 45000,
        });
        assert.equal(nav.status(), 200);
        assert.equal(new URL(page.url()).host, host);
        const navigationTls = delta(before);
        if (state === "warm") await run(page, rows, fixtures.prime, "primer");
        report.samples.push({
          ...(await run(page, rows, fixture, state)),
          navigationTls,
        });
        if (state === "cold")
          report.samples.push(await run(page, rows, fixture, "repeat"));
      } finally {
        await ctx.close();
      }
    }
    await writeFile(output, JSON.stringify(report, null, 2) + "\n");
    console.log("Measured", fixture.kind, report.samples.length);
  }
} finally {
  await browser.close();
  for (const s of sockets) s.destroy();
  await new Promise((r) => proxy.close(r));
}
