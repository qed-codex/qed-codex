// The packager embeds the public directory index in this versioned browser module.
export const directoryConfig = /* @directory-config@ */ null;

// Shared by static compilation and the browser. Contributed HTML is sanitized by the compiler.
const targets = [
  "riemannHypothesis",
  "riemannZeta_eq_zero_re",
  "LFunction_ne_zero_of_half_lt_re",
  "LFunction_eq_zero_re",
  "LFunction_eq_zero_re_of_isPrimitive",
];
const abbreviations = [
  "RH",
  "Zeta zero",
  "L nonvanishing",
  "L zero",
  "Primitive L zero",
];
export const escape = (value) =>
  String(value ?? "").replace(
    /[&<>"']/g,
    (c) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[
        c
      ],
  );
// Keep the displayed and accessible name intact. Each segment is unbreakable.
function segments(text) {
  return text.split(/(?<=[._/])/u).map(part => "<span>" + part + "</span>").join("<wbr>");
}
export const identifier = value => '<span class="identifier">' + segments(escape(value)) + '</span>';
const code = value => "<code>" + identifier(value) + "</code>";
function heading(name, namespace) {
  const parent = namespace ? '<p class="namespace">' + identifier(namespace) + '</p>' : '';
  return '<article class="record">' + parent + '<h1>' + code(name) + '</h1>';
}
const pathPart = (p) => p.split("/").map(encodeURIComponent).join("/");
export function route(type, value, pkg) {
  const module = type === "module";
  return (module ? "/m/?" : "/d/?") + new URLSearchParams({pkg, [module ? "p" : "n"]:value});
}
function link(url, text, format = escape) {
  if (!/^(?:https?:\/\/|\/(?!\/))/.test(url)) return escape(text);
  return '<a href="' + escape(url) + '">' + format(text) + "</a>";
}
export function title(type, value) {
  return type === "module" ? value.split("/").at(-1) : value.split(".").at(-1);
}
export function recordMetadata(type, value, pkg) {
  const name = type === "module"
    ? [value.split("/").at(-1), value.split("/").slice(0, -1).join("/")].filter(Boolean).join(" · ")
    : value;
  const description = type === "module"
    ? `Informalizations, outside explanations and theorem-use data for the Lean module ${value}.`
    : `Pinned Lean source, theorem use and the recorded dependency trail for ${value}.`;
  return {name: name + " · " + pkg, description};
}
export function formalization(proof, pkg = "riemann-hypothesis") {
  const {url, commit, credit, repositoryFolder = ""} = proof.packages[pkg];
  return link(url + "/tree/" + commit + (repositoryFolder ? "/" + repositoryFolder.replace(/\/$/, "") : ""), credit);
}
function list(items, empty) {
  return items.length
    ? '<ul class="record-list">' +
        items.map((x) => "<li>" + x + "</li>").join("") +
        "</ul>"
    : "<p>" + empty + "</p>";
}
export function source(proof, pkg, path, start, end) {
  const {url:repo, commit, repositoryFolder = ""} = proof.packages[pkg];
  return (
    repo +
    "/blob/" +
    commit +
    "/" +
    pathPart(repositoryFolder + path) +
    (start
      ? "#L" + Number(start) + (end && end !== start ? "-L" + Number(end) : "")
      : "")
  );
}
function chips(mask) {
  if (mask == null) return "<span>Theorem-use data unavailable for this proof.</span>";
  return targets
    .map((name, i) => {
      const active = Boolean(mask & (1 << i));
      return (
        '<span class="chip ' +
        (active ? "used" : "unused") +
        '" title="' +
        escape(name) +
        '" aria-label="' +
        escape(name) +
        (active ? " used" : " unused") +
        '">' +
        abbreviations[i] +
        (active ? " · yes" : " · no") +
        "</span>"
      );
    })
    .join("");
}
function kernelSummary(mask) {
  if (mask === 0) return "none";
  if (mask === 31) return "all five";
  return targets.filter((_, i) => mask & (1 << i)).map(identifier).join(", ");
}
export const kernelCredit = proof => '<p class="credit">Kernel masks from ' +
  link(proof.kernel_url, proof.kernel_author + "’s " + proof.kernel_version + " dataset") +
  ", built from " + link(proof.kernel_export_url, proof.kernel_export_author + "’s kernel export") + ".</p>";
const section = (heading, content) =>
  "<section><h2>" + heading + "</h2>" + content + "</section>";
function status(informalizations, disputes) {
  if (disputes.length) return "disputed";
  if (informalizations.some((r) => r.kind === "ai-reviewed-by-human"))
    return "human reviewed";
  if (!informalizations.length) return "no informalization";
  if (informalizations.length === 1) return "one informalization";
  if (
    informalizations.some((r) =>
      informalizations.every(
        (peer) =>
          peer === r ||
          Object.hasOwn(JSON.parse(r.agrees_with_json), peer.author + "--" + writerSlug(peer.writer)),
      ),
    )
  )
    return "informalizations agree";
  return null;
}
function problemLink(path, pkg, repo) {
  const params = new URLSearchParams({template:"module-problem.yml", module:pkg + ":" + path, title:"Module problem · " + title("module",path)});
  return '<p>' + link(repo + "/issues/new?" + params,"Flag a problem") + '</p>';
}
export const writerSlug = name => name.normalize("NFKC").toLowerCase().replace(/[^\p{L}\p{N}]+/gu,"-").replace(/^-|-$/g,"");
const entryId = row => "informalization-" + row.author + "--" + writerSlug(row.writer);
function contribution(path, pkg, proof) {
  return '<p>Open a prefilled file on GitHub. New descriptions use CC BY 4.0.</p>' +
    '<form class="contribute" data-path="' + escape(path) + '" data-commit="' + escape(proof.packages[pkg].commit) +
    '" data-package="' + escape(pkg) + '" data-indexed="' + Boolean(proof.packages[pkg].hasDeclarationIndex) + '" data-repo="' + escape(proof.repository) + '">' +
    '<label>GitHub handle <input name="handle" required maxlength="39" pattern="[A-Za-z0-9]+(&#45;[A-Za-z0-9]+)*"></label>' +
    '<label>Writer (person or model) <input name="writer" required></label>' +
    '<label>Origin <select name="origin" aria-label="Origin" required><option value="">Choose an origin</option><option value="wrote">I wrote it</option><option value="generated">I generated it with this model</option><option value="other-author">It is another author’s work</option></select></label>' +
    '<div class="third-party" hidden><label>Original source URL <input type="url" name="source" disabled></label>' +
    '<label>Licence the source states <select name="license" required disabled><option value="">Choose a licence</option>' +
    '<option value="CC-BY-4.0">CC BY 4.0</option><option value="CC0-1.0">CC0 1.0</option><option>Apache-2.0</option><option>MIT</option></select></label>' +
    '<label>Where the source states the licence <input type="url" name="license_source" required disabled></label>' +
    '<label>Copyright line exactly as published, or “none in the source” <input name="copyright" required disabled></label>' +
    '<label>Source NOTICE text, if present <textarea name="notice" disabled></textarea></label>' +
    '<label>Changes made to the text, or “none” <textarea name="changes" required disabled></textarea></label>' +
    '<p class="import-suggestion">For a whole proof or many files, use ' +
    link(proof.repository + "/issues/new?template=suggest-import.yml", "Suggest an import") + '.</p></div>' +
    '<label class="certify"><input type="checkbox" name="rights" required><span>I have the right to submit this under CC BY 4.0.</span></label>' +
    '<button type="submit" disabled>Add an informalization</button></form>';
}
export function newInformalization(path, fields, commit, ledger, pkg, indexed) {
  const {handle, writer, origin} = fields;
  const metadata = [
    "module: " + JSON.stringify(path), indexed ? "declarations: []" : "declarations: [] # This source has no declaration index. Leave this list empty.", "author: " + JSON.stringify(handle),
    "writer: " + JSON.stringify(writer), "origin: " + origin,
    ...(origin === "other-author" ? [] : ["kind: " + (origin === "wrote" ? "human" : "ai")]),
    "source_commit: " + JSON.stringify(commit), "license: " + (origin === "other-author" ? fields.license : "CC-BY-4.0"),
  ];
  if (origin === "other-author") {
    for (const key of ["source", "license_source", "copyright", "notice", "changes"]) {
      metadata.push(key + ": " + JSON.stringify(fields[key]));
    }
  }
  return ledger + "/new/main?" + new URLSearchParams({
    filename: "packages/" + pkg + "/informalizations/" + path + "/" + handle + "--" + writerSlug(writer) + ".md",
    value: "---\n" + metadata.join("\n") + "\n---\n\n",
  });
}
export function outsideLabel(row) {
  if (row.label?.trim()) return row.label;
  const url = new URL(row.url);
  return url.host + url.pathname + url.search + url.hash;
}

function moduleDeclarations(rows, pkg, indexed) {
  const items = rows.map(r => link(route("declaration",r.name,pkg),r.name,identifier));
  const cap = 12;
  const empty = indexed ? "No indexed declarations." : "This package has no declaration index yet.";
  return list(items.slice(0,cap),empty) + (items.length > cap
    ? '<details><summary>Show all ' + items.length + ' declarations</summary>' + list(items.slice(cap),"") + '</details>' : "");
}
function outsideLinks(rows) {
  return list(rows.map(l => link(l.url,outsideLabel(l)) + " · " + escape(l.author)), "No linked explanations.");
}
function proofMemberships(rows, pkg, hasSourceNotes) {
  const roles = new Map();
  for (const {id, role, title} of rows) {
    if (!roles.has(id)) roles.set(id, {title, labels:[]});
    if (role !== "uses") roles.get(id).labels.push(role + " module");
  }
  if (!roles.size || (!hasSourceNotes && roles.size === 1 && roles.get(pkg)?.labels.length === 0)) return "";
  return "<p>Proofs: " + [...roles].map(([id, {title, labels}]) =>
    link("/proofs/" + id + "/", title) + (labels.length ? " (" + labels.join(", ") + ")" : "")
  ).join(" · ") + "</p>";
}

export function modulePage(proof, data) {
  const f = data.facts[0];
  if (!f) return missing("Module");
  const docs = proof.packages[f.package].moduleDocs;
  const links = docs?.roots.includes(f.path.split("/", 1)[0]) ? [...data.links, {
    url: docs.base + pathPart(f.path.replace(/\.lean$/, ".html")),
    label: docs.label, author: docs.author,
  }] : data.links;
  const sourceNotes = data.informalizations.filter(r => r.entry_type === "source-documentation");
  const contributions = data.informalizations.filter(r => r.entry_type !== "source-documentation");
  const badge = status(contributions, data.disputes);
  const measured = proof.packages[f.package].hasTheoremUse !== false;
  const facts = !measured ? [] : [
    ["Import rank", f.import_rank],
    ["Cut", f.cut],
    [
      "Upstream",
      f.removed_upstream == null
        ? "outside project"
        : f.removed_upstream
          ? "removed"
          : "retained",
    ],
    ["Spine rank", f.spine_rank],
  ];
  const sourceTerms = proof.packages[f.package].sourceTerms || {};
  const articles = (entries) => entries
    .map(
      (r) =>
        '<article class="informalization" id="' + escape(entryId(r)) + '"><p class="meta">' +
        '<strong>' + escape(r.writer) + '</strong>' + (r.kind ? ' · ' + escape(r.kind) : '') + ' · submitted by ' +
        link("https://github.com/" + encodeURIComponent(r.author),"@" + r.author) +
        (r.kind === "ai-reviewed-by-human" ? " (human reviewer)" : "") + " · " +
        (r.license === "with-permission"
          ? link(r.source_url,"Used with permission of " + r.writer)
          : link((r.entry_type === "source-documentation" && sourceTerms.LICENSE) || "/LICENSES/" + encodeURIComponent(r.license) + ".txt", r.license === "CC-BY-4.0" ? "CC BY 4.0" : r.license) +
            (r.entry_type === "source-documentation" && sourceTerms.NOTICE ? " · " + link(sourceTerms.NOTICE, "NOTICE") : "") +
            (r.entry_type === "source-documentation" && sourceTerms["ATTRIBUTION.md"] ? " · " + link(sourceTerms["ATTRIBUTION.md"], "ATTRIBUTION.md") : "") +
            ((r.copyright === "" || (r.license_source && r.copyright === "none in the source")) ? (r.entry_type === "source-documentation" ? " · no copyright line in this file" : " · no copyright line in the source") : r.copyright ? " · " + escape(r.copyright) : "") +
            (r.source_url ? " · " + link(r.source_url,"Source") : "") +
            (r.license_source ? " · " + link(r.license_source,"licence stated at") + " · Changes: " + escape(r.changes) : "")) +
        " · " + link(route("module", f.path, f.package) + "#" + encodeURIComponent(entryId(r)), "Permalink") +
        "</p>" + (r.notice ? '<details><summary>NOTICE</summary><pre>' + escape(r.notice) + '</pre></details>' : "") +
        JSON.parse(r.declarations_json)
          .map((n) => link(route("declaration", n, f.package), n, identifier))
          .join(" · ") +
        r.informalization_html.replace(/<pre>[\s\S]*?<\/pre>|<code>([^<>]*)<\/code>/g, (markup, inline) =>
          inline === undefined ? markup : '<code class="identifier">' + segments(inline) + '</code>')
          .replace(/<math display="(inline|block)">[\s\S]*?<\/math>/g, (math, display) =>
            '<span class="formula-' + display + '">' + math + '</span>') +
        "</article>",
    )
    .join("");
  return (
    heading(title("module", f.path), f.path.replace(/^src\//, "").split("/").slice(0, -1).join(".")) +
    '<p class="path">' +
    link(source(proof, f.package, f.path), f.path, identifier) + " · " + link(route("module", f.path, f.package), "Module permalink") + " · " + formalization(proof, f.package) +
    "</p>" +
    proofMemberships(data.memberships || [], f.package, sourceNotes.length > 0) +
    '<div class="facts">' +
    facts
      .map(
        ([k, v]) =>
          '<span class="chip">' + k + " · " + escape(v ?? "—") + "</span>",
      )
      .join("") +
    "</div>" +
    '<div class="facts kernel">' +
    chips(f.mask) + (measured ? link("/about/#glossary","Badge guide") : "") +
    "</div>" +
    (measured ? kernelCredit(proof) : "") +
    (badge
      ? '<span class="status">' + badge + "</span>"
      : "<p>" + contributions.length + " informalizations · comparison pending</p>") +
    (sourceNotes.length ? section("From the source", articles(sourceNotes)) : "") +
    section(
      "Informalizations",
      (articles(contributions) || "<p>No contributed informalization for this module.</p>") +
      (!measured ? "<p>Add an independent description under CC BY 4.0.</p>" : "") + contribution(f.path, f.package, proof),
    ) +
    section("Declarations", moduleDeclarations(data.members, f.package, proof.packages[f.package].hasDeclarationIndex)) +
    section("Elsewhere",outsideLinks(links)) +
    section(
      "Open disputes",
      list(
        data.disputes.map((d) => link(d.url, "View dispute")),
        "No open disputes.",
      ) + problemLink(f.path, f.package, proof.repository),
    ) +
    section("Discussion", "<p>Discussion opens at launch</p>") +
    "</article>"
  );
}
export function missing(kind) {
  return (
    "<h1>" +
    kind +
    " not found</h1><p>" +
    link("/", "Search the directory") +
    "</p>"
  );
}
export function trailSection(proof, d, data) {
  const trail = data.sites.length
    ? '<ol class="trail">' +
      data.sites
        .map(
          (s, i) =>
            '<li><div class="trail-row">' +
            link(
              s.indexed
                ? route("declaration", s.name, s.package)
                : source(proof, s.package, s.path, s.line),
              s.name, identifier,
            ) +
            '&nbsp;<span class="trail-lines">· ' +
            link(source(proof, s.package, s.path, s.line), "line " + s.line) +
            (data.sites[i + 1]
              ? " · " +
                link(
                  source(proof, data.sites[i + 1].package, data.sites[i + 1].path, s.use_line),
                  "use at line " + s.use_line,
                )
              : "") +
            "</span></div></li>",
        )
        .join("") +
      "</ol>"
    : "<p>No route in the frozen source trace.</p>" + (d.kernel_mask & 1 ? "<p>The kernel data records use by the Riemann Hypothesis, and the source trace did not find the route.</p>" : "");
  return section(
      "Trail to riemannHypothesis",
      '<p class="meta">Calling sites in the frozen source trace.</p>' + trail,
    );
}

export function siblingSection(d, data) {
  return section(
      "Other declarations in this module",
      list(
        data.peers.map(
          (p) =>
            link(route("declaration", p.name, d.package), p.name, identifier) +
            ' <span class="kernel-summary">Used by: ' +
            kernelSummary(p.kernel_mask) +
            "</span>",
        ),
        "No other indexed declarations.",
      ),
    );
}

export function outsideSection(rows) {
  return rows.length ? section("Elsewhere", outsideLinks(rows)) : "";
}

export function declarationPage(proof, data) {
  const d = data.declarations[0];
  if (!d) return missing("Declaration");
  const lines = d.start
    ? "Line" +
      (d.end && d.end !== d.start
        ? "s " + d.start + "–" + d.end
        : " " + d.start)
    : "Source file";
  const src = source(proof, d.package, d.path, d.start, d.end);
  return (
    heading(title("declaration", d.name), d.name.split(".").slice(0, -1).join(".")) +
    '<p class="path">' +
    escape(d.kind) +
    " · " +
    link(route("module", d.path, d.package), d.path, identifier) +
    " · " +
    link(src, lines) + " · " + link(route("declaration", d.name, d.package), "Declaration permalink") + " · " + formalization(proof, d.package) +
    "</p>" +
    '<div class="facts kernel">' +
    chips(d.kernel_mask) + link("/about/#glossary","Badge guide") +
    "</div>" +
    kernelCredit(proof) +
    section(
      "Lean source",
      "<p>" +
        link(src, "Open pinned source") +
        "</p>" +
        (d.start
          ? '<div class="lean-source" data-package="' + escape(d.package) + '" data-path="' +
            escape(d.path) +
            '" data-start="' +
            d.start +
            '" data-end="' +
            (d.end || d.start) +
            '"></div>'
          : ""),
    ) +
    '<div data-decl-part="trail">' + (data.sites ? trailSection(proof, d, data) : '<p>Loading trail…</p>') + '</div>' +
    '<div data-decl-part="outside">' + (data.outside ? outsideSection(data.outside) : '') + '</div>' +
    '<div data-decl-part="siblings">' + (data.peers ? siblingSection(d, data) : '<p>Loading declarations…</p>') + '</div>' +
    "</article>"
  );
}

export function wantedPage(proof, rows, start, total, pkg = "") {
  const page = rows.slice(0, 50);
  const board = pkg ? "/wanted/?pkg=" + encodeURIComponent(pkg) + "&start=" : "/wanted/?start=";
  const previous = start > 1 ? link(board + Math.max(1, start - 50), "Previous") : "";
  const next = rows.length > 50 ? link(board + (start + 50), "Next") : "";
  const rh = !pkg || pkg === "riemann-hypothesis";
  return '<h1>Most-wanted informalizations' + (pkg ? ' · ' + escape(pkg) : '') + '</h1><p>Modules awaiting an informalization. Modules with source documentation still welcome an independent informalization.</p>' +
    (rh ? '<p>The RH list covers modules used by the Riemann Hypothesis. Modules with a spine rank appear in rank order, followed by the remaining modules in descending order of cut.</p>' + kernelCredit(proof) : '') +
    (page.length ? '<p>Showing ' + start + '–' + page.at(-1).rank + ' of ' + total.toLocaleString("en-US") + '</p>' +
      '<ol class="record-list" start="' + start + '">' + page.map(row =>
        '<li><div>' + link(route("module",row.path,row.package),row.path,identifier) + '<div class="board-badges">' +
        (row.spine_rank == null ? "" : ' <span class="chip">Spine · ' + row.spine_rank + '</span>') +
        ' <span class="chip">Cut · ' + (row.cut ?? "unmeasured") + '</span></div></div></li>').join("") + '</ol>' : '<p>No modules on this page.</p>') +
    '<nav aria-label="Board pages">' + [previous, next].filter(Boolean).join(" · ") + '</nav>';
}
