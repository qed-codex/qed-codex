import assert from "node:assert/strict";
import {test} from "node:test";
import {bytes} from "../site/startup-assets.mjs";

test("read immutable assets through asynchronous binary XHR", async t => {
  const url = "/db/gzip-v1-a-p4/interior";
  const payload = new Uint8Array([1, 2]).buffer;
  class Request {
    open(method, target, async = true) {
      assert.deepEqual([method, target, async], ["GET", url, true]);
    }
    send() {
      assert.equal(this.responseType, "arraybuffer");
      this.status = 200;
      this.response = payload;
      queueMicrotask(() => this.onload());
    }
  }
  const previous = Object.getOwnPropertyDescriptor(globalThis, "XMLHttpRequest");
  globalThis.XMLHttpRequest = Request;
  t.after(() => previous ? Object.defineProperty(globalThis, "XMLHttpRequest", previous) : delete globalThis.XMLHttpRequest);
  assert.equal(await bytes(url), payload);
});
