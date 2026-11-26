import {bytes} from "./startup-assets.mjs";
import { readAsset, inflateAsset } from "./page-reader.mjs";

export function createPageReader(manifest, interior, base) {
  const size = manifest.pageBytes;
  const cache = new Map();
  const singlePageFiles = (manifest.pagesPerPiece ?? 1) === 1;
  const length = manifest.interior.length * size;
  const bundle = interior ? inflateAsset(interior, length, "interior") : readAsset(new URL("interior", base), length);
  manifest.interior.forEach((page, i) => cache.set(page, bundle.subarray(i * size, (i + 1) * size)));

  return function readPage(page) {
    if (cache.has(page)) return cache.get(page);
    const bytes = readAsset(new URL(`p/${page}`, base), size);
    // A slice of a grouped piece retains its whole buffer. Its reader owns that cache.
    if (singlePageFiles) cache.set(page, bytes);
    return bytes;
  };
}

// Runs in a browser thread dedicated to SQLite. Each miss fetches an entire static asset.
export async function openProof(sqlite, manifest, interior) {
  const { capi, wasm } = sqlite;
  const size = manifest.pageBytes;
  const base = new URL(`./db/${manifest.buildId}/`, self.location.href);
  const readPage = createPageReader(manifest, interior ?? await bytes(new URL("interior", base)), base);

  const io = new capi.sqlite3_io_methods();
  const vfs = new capi.sqlite3_vfs();
  io.$iVersion = vfs.$iVersion = 1;
  vfs.$szOsFile = capi.sqlite3_file.structInfo.sizeof;
  vfs.$mxPathname = 256;
  vfs.$zName = wasm.allocCString("qed-pages");
  const defaultVfs = new capi.sqlite3_vfs(capi.sqlite3_vfs_find(null));
  for (const method of ["$xSleep", "$xRandomness", "$xCurrentTime"]) vfs[method] = defaultVfs[method];
  const fileBytes = size * manifest.pageCount;
  let readError;
  sqlite.vfs.installVfs({
    vfs: { struct: vfs, methods: {
      xOpen(_vfs, name, file, flags, outFlags) {
        if (wasm.cstrToJs(name) !== "/proof.sqlite3" || !(flags & capi.SQLITE_OPEN_READONLY)) {
          return capi.SQLITE_CANTOPEN;
        }
        const handle = new capi.sqlite3_file(file);
        handle.$pMethods = io.pointer;
        if (outFlags) wasm.poke32(outFlags, capi.SQLITE_OPEN_READONLY);
        return 0;
      },
      xAccess(_vfs, name, _flags, out) {
        wasm.poke32(out, Number(wasm.cstrToJs(name) === "/proof.sqlite3"));
        return 0;
      },
      xFullPathname(_vfs, name, n, out) {
        return wasm.cstrncpy(out, name, n) < n ? 0 : capi.SQLITE_CANTOPEN;
      },
      xDelete: () => capi.SQLITE_READONLY
    }},
    io: { struct: io, methods: {
      xClose: () => 0,
      xRead(_file, ptr, n, offset) {
        let pos = Number(offset);
        const heap = wasm.heap8u();
        try {
          while (n > 0 && pos < fileBytes) {
            const page = Math.floor(pos / size) + 1;
            const within = pos % size;
            const count = Math.min(n, size - within);
            heap.set(readPage(page).subarray(within, within + count), Number(ptr));
            pos += count;
            ptr += count;
            n -= count;
          }
          if (!n) return 0;
          heap.fill(0, Number(ptr), Number(ptr) + n);
          return capi.SQLITE_IOERR_SHORT_READ;
        } catch (error) {
          readError = error.message;
          return capi.SQLITE_IOERR_READ;
        }
      },
      xFileSize(_file, out) { wasm.poke(out, BigInt(fileBytes), "i64"); return 0; },
      xWrite: () => capi.SQLITE_READONLY, xTruncate: () => capi.SQLITE_READONLY,
      xSync: () => 0, xLock: () => 0, xUnlock: () => 0,
      xCheckReservedLock(_file,out) { wasm.poke32(out,0); return 0; },
      xFileControl: () => capi.SQLITE_NOTFOUND, xSectorSize: () => size,
      xDeviceCharacteristics: () => capi.SQLITE_IOCAP_IMMUTABLE
    }}
  });
  const db = new sqlite.oo1.DB({ filename: "/proof.sqlite3", flags: "r", vfs: "qed-pages" });
  db.exec("PRAGMA query_only=ON; PRAGMA temp_store=MEMORY");
  return { db, lastReadError: () => readError };
}
