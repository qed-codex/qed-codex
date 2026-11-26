// node tools/test-piece-cache.mjs PACKAGE DATABASE
import assert from "node:assert/strict";
import {openSync, readFileSync, readSync, closeSync} from "node:fs";
import {resolve} from "node:path";
import {pathToFileURL} from "node:url";

const root = resolve(process.argv[2]);
const manifest = JSON.parse(readFileSync(resolve(root, "proof.json")));
const perPiece = manifest.pagesPerPiece;
assert.ok(perPiece > 1);
const base = pathToFileURL(resolve(root, "db", manifest.buildId) + "/");
const fetched = [];
globalThis.XMLHttpRequest = class {
  open(method, url) { this.url = url; }
  send() {
    const compressed = readFileSync(this.url);
    this.status = 200;
    this.response = compressed.buffer.slice(compressed.byteOffset, compressed.byteOffset + compressed.byteLength);
    fetched.push(this.url.pathname);
  }
};
const {createPageReader} = await import(pathToFileURL(resolve(root, "pages-vfs.mjs")));
const page = createPageReader(manifest, null, base);
const interior = new Set(manifest.interior);
const leaves = [];
for (let n = 1; n <= manifest.pageCount && leaves.length < 33; n += perPiece) {
  if (!interior.has(n) && !interior.has(n + 1)) leaves.push(n);
}
assert.equal(leaves.length, 33);
const db = openSync(process.argv[3], "r");
function read(n) {
  const reference = Buffer.alloc(manifest.pageBytes);
  assert.equal(readSync(db, reference, 0, reference.length, (n-1)*reference.length), reference.length);
  assert.deepEqual(Buffer.from(page(n)), reference);
}
try {
  assert.equal(fetched.length, 1); // Interior bundle.
  leaves.slice(0,32).forEach(read);
  assert.equal(fetched.length, 33);
  read(leaves[0]+1); // Refresh the first piece through a different page.
  assert.equal(fetched.length, 33);
  read(leaves[32]); // The second piece is now the oldest.
  read(leaves[0]);
  read(manifest.interior[0]);
  assert.equal(fetched.length, 34);
  read(leaves[1]); // Must reach the piece reader again, even for the exact same page.
  assert.equal(fetched.length, 35);
  assert.equal(fetched.at(-1), fetched[2]);
  read(manifest.pageCount);
} finally {closeSync(db);}
console.log("32-piece LRU, adjacent hits, eviction through the VFS, pinned interior and final page passed.");
