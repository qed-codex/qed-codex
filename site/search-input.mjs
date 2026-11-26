// The table uses SQLite BINARY collation and Unicode lowercase short names.
export function parameters(kind, value, ftsOffset) {
  if (kind === "wantedSource") return [value.pkg, value.start];
  if (kind === "wanted") return [Number(value) || 1];
  if (kind === "typeahead") return [value.trim().toLowerCase()];
  if (kind === "search" || kind === "searchCount") {
    const raw = (typeof value === "string" ? value : value.term).trim();
    const words = raw.match(/[\p{L}\p{N}]+/gu) || [];
    const expression = words.map(word => '"' + word + '"').join(" AND ");
    const moduleName = raw.replace(/^src\//, "").replace(/\.lean$/, "").replaceAll("/", ".");
    const tail = name => name.split(".").at(-1).toLowerCase();
    return [expression, ftsOffset, typeof value === "string" ? 0 : value.offset,
      raw, tail(moduleName), moduleName, tail(raw), raw.toLowerCase()];
  }
  const {name, pkg, sourceRoot} = typeof value === "string"
    ? {name:value, pkg:"riemann-hypothesis", sourceRoot:"src/"} : value;
  let full = name.trim();
  if (kind === "module" && full.endsWith(".lean")) {
    if (sourceRoot && full.startsWith(sourceRoot)) full = full.slice(sourceRoot.length);
    full = full.slice(0, -5).replaceAll("/", ".");
  }
  return [full.split(".").at(-1).toLowerCase(), full, pkg];
}
