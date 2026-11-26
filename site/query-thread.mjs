import sqlite3InitModule from "./vendor/index.mjs";
import { parameters } from "./search-input.mjs";
import { openProof } from "./pages-vfs.mjs";

let ready, connection;
async function open(assets) {
  const [sql, manifest, queries] = await Promise.all([
    sqlite3InitModule(assets ? { wasmBinary: assets.wasm } : undefined),
    assets?.manifest ?? fetch("./proof.json").then((r) => r.json()),
    fetch("./queries.json").then((r) => r.json()),
  ]);
  connection = await openProof(sql, manifest, assets?.interior);
  return { queries, offset: manifest.ftsDeclarationOffset };
}
self.onmessage = async ({ data: { id, kind, value, assets } }) => {
  try {
    ready ??= open(assets);
    const { queries, offset } = await ready;
    if (!Object.hasOwn(queries, kind)) throw Error("Unknown query");
    const result = {};
    for (const [key, sql] of Object.entries(queries[kind])) {
      result[key] = connection.db.exec({
        sql,
        bind: parameters(kind, value, offset),
        returnValue: "resultRows",
        rowMode: "object",
      });
    }
    self.postMessage({ id, result });
  } catch (error) {
    self.postMessage({
      id,
      error: connection?.lastReadError() || error.message || String(error),
    });
  }
};
