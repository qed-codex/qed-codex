import sqlite3InitModule from "./vendor/index.mjs";
import {openProof} from "./pages-vfs.mjs";

let database;
const rowLimit = 200;
const resultBytes = 512 * 1024;
const encoder = new TextEncoder();
async function open() {
  const [sqlite, manifest] = await Promise.all([
    sqlite3InitModule(), fetch("./proof.json").then(response => {
      if (!response.ok) throw Error("Could not read the proof manifest.");
      return response.json();
    }),
  ]);
  const {db} = await openProof(sqlite, manifest);
  const {capi} = sqlite;
  const tables = new Set(["sqlite_schema", "sqlite_master", ...db.selectValues("SELECT name FROM sqlite_schema WHERE type IN ('table','view')")]);
  const functions = new Set(db.selectValues("SELECT name FROM pragma_function_list WHERE builtin AND (flags & ?) != 0", [capi.SQLITE_INNOCUOUS]));
  functions.add("match"); // FTS5 implements MATCH on the names virtual table.
  // Connect FTS5 before restricting user statements. Its constructor reads schema metadata.
  db.selectValues("SELECT rowid FROM names WHERE names MATCH 'geometry' LIMIT 0");
  const inspection = new Set(["table_info", "table_xinfo", "index_list", "index_info", "index_xinfo", "table_list"]);
  const authorize = (_context, action, object, fn, schema) => {
    if (action === capi.SQLITE_SELECT || action === capi.SQLITE_RECURSIVE) return capi.SQLITE_OK;
    if (action === capi.SQLITE_READ && (schema === "main" || (!schema && !fn)) && tables.has(object)) return capi.SQLITE_OK;
    if (action === capi.SQLITE_FUNCTION && functions.has(fn)) return capi.SQLITE_OK;
    if (action === capi.SQLITE_PRAGMA && (inspection.has(object) || (object === "data_version" && !fn))) return capi.SQLITE_OK;
    return capi.SQLITE_DENY;
  };
  db.checkRc(capi.sqlite3_set_authorizer(db.pointer, authorize, 0));
  capi.sqlite3_limit(db.pointer, capi.SQLITE_LIMIT_LENGTH, 1024 * 1024);
  capi.sqlite3_limit(db.pointer, capi.SQLITE_LIMIT_COLUMN, 100);
  capi.sqlite3_limit(db.pointer, capi.SQLITE_LIMIT_SQL_LENGTH, 48000);
  return {db, capi, tables};
}
function readQuery({db, capi, tables}, sql) {
  if (typeof sql !== "string" || sql.includes("\0") || sql.length > 12000) throw Error("Use one query of up to 12,000 characters.");
  const stmt = db.prepare(sql);
  try {
    const prepared = capi.sqlite3_sql(stmt.pointer);
    const tail = sql.slice(prepared.length);
    if (!sql.startsWith(prepared) || !/^(?:\s|;|--[^\n]*(?:\n|$)|\/\*[\s\S]*?\*\/)*$/u.test(tail))
      throw Error("Run one SQL statement at a time.");
    if (!stmt.isReadOnly() || !stmt.columnCount) throw Error("Enter a read-only query that returns columns.");
    // Give the timeout handler a reason before stepping a network-backed scan.
    if (/^\s*(?:SELECT|WITH)\b/i.test(prepared)) {
      const plan = db.selectObjects("EXPLAIN QUERY PLAN " + prepared);
      if (plan.some(({detail}) => {
        const scan = /^SCAN (\S+)(?: USING (?:COVERING )?INDEX .+)?$/.exec(detail);
        return scan && tables.has(scan[1]);
      })) self.postMessage({wholeTableScan:true});
    }
    const columns = stmt.getColumnNames();
    const rows = [];
    let bytes = 0;
    while (stmt.step()) {
      if (rows.length === rowLimit) return {columns, rows, limited:true};
      const values = stmt.get([]).map(value => value instanceof Uint8Array ? `[BLOB · ${value.length} bytes]` : value);
      for (const v of values) bytes += encoder.encode(String(v)).length;
      if (bytes > resultBytes) return {columns, rows, limited:true};
      rows.push(values);
    }
    return {columns, rows, limited:false};
  } finally { stmt.finalize(); }
}
self.onmessage = async ({data}) => {
  try {
    database ??= open();
    self.postMessage(readQuery(await database, data));
  } catch (error) { self.postMessage({error: error.message || String(error)}); }
};
