import { createHash } from "node:crypto";
import { mkdir, readFile, unlink, writeFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import {
  identifier, declarationPage, escape, formalization, kernelCredit,
  modulePage, recordMetadata, wantedPage, route, title,
} from "../site/record.mjs";

process.stdin.setEncoding("utf8");
let input = "";
for await (const chunk of process.stdin) input += chunk;
const { proof, imports, catalogue, proofRows, samples, records, extra, board, wantedCount, unmatched, settings, baseURL, previewProbe } = JSON.parse(input);
const out = process.argv[2];
const sitemap = [];

// Fingerprint frequently reused assets so queries can revalidate their HTML shell cheaply.
async function publishAsset(name, transform = value => value) {
  const original = join(out, name);
  const bytes = transform(await readFile(original));
  const digest = createHash("sha256").update(bytes).digest("hex");
  const folder = join(out, "assets", digest);
  await mkdir(folder, {recursive:true});
  await writeFile(join(folder, name), bytes);
  await unlink(original);
  return "/assets/" + digest + "/" + name;
}
const icon = await publishAsset("icon.png");
const stylesheet = await publishAsset("directory.css", css => css.toString().replace("/icon.png", icon));
const directoryIndex = await readFile(join(out, "directory.json"), "utf8");
const recordScript = await publishAsset("record.mjs", js =>
  js.toString().replace("/* @directory-config@ */ null", () => directoryIndex.trimEnd()));
const clientFile = join(out, "directory.mjs");
await writeFile(clientFile, (await readFile(clientFile, "utf8")).replace('"./record.mjs"', JSON.stringify(recordScript)));

const ledger = escape(settings.repository);
const footer = `<footer><p>Independent project. Not affiliated with any AI vendor.</p>
<nav aria-label="Project resources"><a href="${ledger}">Repository</a> · <a href="${ledger}/blob/main/CONTRIBUTING.md">Contributing</a> · <a href="${ledger}/blob/main/LICENSE">Code license</a> · <a href="https://creativecommons.org/licenses/by/4.0/">Original text license</a> · <a href="/about/">About</a></nav></footer>`;

async function page(path, name, description, body, { attrs = "", script = "/directory.mjs", style = "", indexable = true, noindex = false } = {}) {
  const label = escape(name + " · QED Codex");
  const desc = escape(description);
  const address = baseURL && new URL(path, baseURL).href;
  if (indexable && address) sitemap.push(address);
  const production = address ? `<link rel="canonical" href="${escape(address)}"><meta property="og:image" content="${escape(new URL("/qed-codex-logo.png", baseURL).href)}">` : "";
  const html = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>${label}</title><meta name="description" content="${desc}"><meta property="og:title" content="${label}"><meta property="og:description" content="${desc}">${production}${noindex ? '<meta name="robots" content="noindex">' : ""}
<link rel="icon" type="image/png" href="${icon}"><link rel="stylesheet" href="${stylesheet}">${style ? `<link rel="stylesheet" href="${style}">` : ""}</head>
<body><header class="masthead"><a class="brand" href="/">QED Codex</a><span class="proof-label">Proof directory</span></header>
<main id="content" ${attrs}>${body}</main>${footer}<script type="module" src="${script}"></script></body></html>\n`;
  const file = join(out, path.endsWith("/") ? path + "index.html" : path);
  await mkdir(dirname(file), { recursive: true });
  await writeFile(file, html);
}
function sampleLinks(group, staticPath = false) {
  return '<ul class="sample-links">' + group.map(s =>
    `<li><a href="${escape(staticPath ? "/sample/" + s.package + "/" + s.id + "/" : route(s.type, s.value, s.package))}"><code>${identifier(title(s.type, s.value))}</code></a></li>`).join("") + "</ul>";
}
const projectLinks = catalogue.map(p =>
  `<li><a href="/proofs/${escape(p.package)}/">${p.titleHTML}</a><span>Formalization: <a href="${escape(p.creditSource)}">${escape(p.listCredit ?? p.credit)}</a> · ${p.moduleCount.toLocaleString("en-US")} modules</span></li>`
).join("");
const home = `<div class="home-intro"><h1>Search the proofs</h1><p>QED Codex presents informalizations of machine-written proofs by people and autoinformalizations by AI, side by side.</p></div>
<form class="search-box" role="search"><label for="term">Lean name or module path</label><input id="term" type="search" autocomplete="off" placeholder="e.g. anyGeometry">
<button type="submit">Search everywhere</button></form><div id="matches" aria-live="polite"></div>
<nav aria-labelledby="proofs-heading"><h2 id="proofs-heading">Proofs</h2><ul class="proof-list">${projectLinks}</ul><a href="/proofs/">All proofs</a></nav>
<section><h2>Example modules from the Riemann Hypothesis proof</h2>${sampleLinks(samples.filter(s => s.type === "module"))}</section>
<section><h2>Example declarations from the Riemann Hypothesis proof</h2>${sampleLinks(samples.filter(s => s.type === "declaration"))}</section>
<nav class="directory-tools"><a href="/wanted/">Most-wanted informalizations</a> · <a href="/sql/">SQL console</a> · <a href="/unmatched/">Unmatched statements</a></nav>`;
await page("/", "Search the proofs", "Browse registered Lean proofs or search for a module or declaration.", home);
const proofsById = new Map(catalogue.map(p => [p.package, p]));
const indexRows = proofRows.map(({id, source, modules, documented, contributed}) => {
  const p = proofsById.get(id);
  const pinURL = proof.packages[source].url + "/tree/" + p.commit;
  const numbers = [modules, documented, contributed].map(n => `<td>${n.toLocaleString("en-US")}</td>`).join("");
  return `<tr><th scope="row"><a href="/proofs/${escape(id)}/">${p.titleHTML}</a></th>
    <td><a href="${escape(p.creditSource)}">${escape(p.listCredit ?? p.credit)}</a></td>
    <td>${escape(source)}<br><a href="${escape(pinURL)}"><code>${escape(p.commit.slice(0, 8))}</code></a></td>
    <td>${escape(p.license || "Not stated")}</td>${numbers}<td>${p.verificationRecords?.length ? "Yes" : "No"}</td></tr>`;
}).join("");
await page("/proofs/", "All proofs", "Registered proofs, pinned sources and contributions.",
  `<h1 id="index-title">All proofs</h1><div class="proof-index" role="region" aria-labelledby="index-title" tabindex="0">
  <table aria-labelledby="index-title"><thead><tr><th scope="col">Proof</th><th scope="col">Formalization</th>
  <th scope="col">Source and pin</th><th scope="col">Licence</th><th scope="col">Modules</th>
  <th scope="col">Modules with source notes</th><th scope="col">Contributed informalizations</th>
  <th scope="col">Verification record</th></tr></thead><tbody>${indexRows}</tbody></table></div>`,
  {attrs:'data-static-page="true"'});

// Render source metadata as data. URLs are links and all other values are escaped text.
function metadataValue(value) {
  if (Array.isArray(value)) return "<ul>" + value.map(v => "<li>" + metadataValue(v) + "</li>").join("") + "</ul>";
  if (value && typeof value === "object")
    return "<dl>" + Object.entries(value).map(([key,v]) => "<dt>" + escape(key.replaceAll("_"," ")) + "</dt><dd>" + metadataValue(v) + "</dd>").join("") + "</dl>";
  const text = escape(String(value));
  return /^https?:\/\//.test(value) ? '<a href="' + text + '">' + text + '</a>' : text;
}
function sourceTerms(pkg) {
  const links = Object.entries(proof.packages[pkg].sourceTerms).map(([name, url]) =>
    '<a href="' + escape(url) + '">' + escape(name) + '</a>');
  return links.length ? '<p>Source files: ' + links.join(' · ') + '</p>' : '';
}
function otherVersions(versions = []) {
  if (!versions.length) return "";
  return '<section><h2>Other versions of this proof</h2><ul>' + versions.map(({label,url}) =>
    '<li><a href="' + escape(url) + '">' + escape(label) + '</a></li>').join('') + '</ul></section>';
}
function proofMaterials(details) {
  if (!details.sections) return "";
  const record = path => '<a href="' + escape(route('module',path,details.package)) + '">' + identifier(path) + '</a>';
  return '<p>Root and solution: ' + record(details.rootModule) + '</p>' + details.sections.map(s =>
    '<section class="proof-source"><h2>' + escape(s.heading) + '</h2><p><a href="' + escape(s.address) + '">Pinned source</a>' +
    (s.path.endsWith('.lean') ? ' · ' + record(s.path) : '') + '</p><div class="informalization">' + s.html + '</div></section>'
  ).join('') + '<p>' + details.sourceDocuments.map(path =>
    '<a href="' + escape(details.root + path) + '">' + escape(path) + '</a>').join(' · ') + '</p>';
}
function verificationRecords(records = []) {
  if (!records.length) return "";
  const items = records.map(({title, who, address}) => {
    if (!title || !who || !/^https?:\/\//.test(address)) throw Error("Invalid verification record");
    return '<li><a href="' + escape(address) + '">' + escape(title) + '</a> · ' + escape(who) + '</li>';
  });
  return '<section><h2>Verification records</h2><ul>' + items.join("") + '</ul></section>';
}
function proofReferences({verificationRecords: records, papers, papersHeading = "Papers"}) {
  const verification = verificationRecords(records);
  if (!papers?.length) return verification;
  const date = new Intl.DateTimeFormat("en-GB", {
    day: "numeric", month: "short", year: "numeric", timeZone: "UTC"
  });
  const items = papers.map(({title, authors, arxiv, submitted}) =>
    '<li><cite>' + escape(title) + '</cite> · ' + authors.map(escape).join(', ') +
    ' · <a href="https://arxiv.org/abs/' + escape(arxiv) + '">arXiv:' + escape(arxiv) +
    '</a> · <time datetime="' + escape(submitted) + '">' + date.format(new Date(submitted)) + '</time></li>'
  );
  return verification + '<section><h2>' + escape(papersHeading) + '</h2><ul>' + items.join('') + '</ul></section>';
}
function moduleGroups(modules, pkg) {
  const folders = new Map();
  for (const m of modules) {
    const folder = dirname(m.path);
    if (!folders.has(folder)) folders.set(folder, []);
    folders.get(folder).push(m);
  }
  return [...folders].map(([folder, items]) => '<details><summary>' + identifier(folder === "." ? "Root" : folder) +
    ' (' + items.length + ')</summary><ul>' + items.map(m => '<li><a href="' +
    escape(route("module",m.path,pkg)) + '">' + identifier(m.path) + '</a>' +
    (m.documented ? ' · source documentation' : '') + (m.contributed === 0 ? ' · awaiting an informalization' : '') +
    '</li>').join('') + '</ul></details>').join('');
}
const wantedLink = pkg => '<p><a href="/wanted/?pkg=' + encodeURIComponent(pkg) + '">Most-wanted modules in ' + escape(pkg) + '</a></p>';
const compareLink = pkg => '<p><a href="/comparisons/' + escape(pkg) + '/">Compare the formal statements</a></p>';

const zetaProof = catalogue.find(p => p.package === "zeta23");
const zeta = zetaProof.metadata;
const info = zeta.project;
function citations(sources) {
  return '<section><h2>Sources</h2><ul>' + sources.map(source => {
    const title = '<cite>' + escape(source.title) + '</cite>';
    const linkedTitle = /^https?:\/\//.test(source.location) ? '<a href="' + escape(source.location) + '">' + title + '</a>' : title;
    return '<li>' + [source.authors?.map(escape).join(", "), linkedTitle, source.id && escape(source.id)]
      .filter(Boolean).join(". ") + '.' +
      (source.relationship ? ' This proof ' + escape(source.relationship) + ' this work.' : '') +
      (source.note ? '<p>' + escape(source.note) + '</p>' : '') +
      (source.author_endorsement === 'participated' ? '<p>The source records author participation.</p>' :
        source.author_endorsement ? '<p>Author endorsement: ' + escape(source.author_endorsement) + '</p>' : '') + '</li>';
  }).join('') + '</ul></section>';
}
const sections = [["Related formalizations",zeta.related_formalizations], ["Automation",zeta.automation]];
const zetaSpec = proof.packages.zeta23;
const metaUrl = zetaSpec.url + "/blob/" + zetaSpec.commit + "/" + zetaSpec.repositoryFolder + "formalization.yaml";
const sourceDescription = '<p>From the authors’ <a href="' + escape(metaUrl) + '">pinned project description</a>.</p>';
await page("/proofs/zeta23/",info.name,info.description,
  '<h1>' + escape(info.name) + '</h1>' + sourceDescription + '<p>' + escape(info.description) + '</p>' +
  '<p>Authors: ' + escape(info.authors.join(", ")) + ' · <a href="/LICENSES/' + escape(info.license) + '.txt">' + escape(info.license) + '</a></p>' +
  citations(zeta.sources) + sections.map(([label,data]) => "<section><h2>" + label + "</h2>" + metadataValue(data) + "</section>").join("") +
  sourceTerms("zeta23") + proofReferences(zetaProof) + "<section><h2>Modules</h2><p>This proof has no declaration index or theorem-use data yet. Each module welcomes an independent description under CC BY 4.0.</p>" + wantedLink("zeta23") + moduleGroups(zetaProof.modules,"zeta23") + "</section>", {attrs:'data-static-page="true"'});
await page("/proofs/riemann-hypothesis/","Riemann Hypothesis","Source, modules and final declarations of the pinned RH proof.",
  "<h1>Riemann Hypothesis</h1><p>" + formalization(proof) + "</p>" + wantedLink("riemann-hypothesis") + proofReferences(proof) + otherVersions(proof.otherVersions) + "<h2>Modules</h2>" + sampleLinks(samples.filter(s => s.type === "module"),true)
  + "<h2>Declarations</h2>" + sampleLinks(samples.filter(s => s.type === "declaration"),true), {attrs:'data-static-page="true"'});
for (const details of catalogue.filter(p => p.openingHTML)) {
  const {package:pkg, root, title, openingHTML, credit, creditSource, modules} = details;
  await page("/proofs/" + pkg + "/", title, "Pinned source documentation and modules for " + pkg + ".",
    '<p>Opening of the <a href="' + escape(root + "README.md") + '">pinned project README</a>, reproduced verbatim.</p>' +
    openingHTML + '<p>Source documentation credited to <a href="' + escape(creditSource) + '">' + escape(credit) +
    '</a> · <a href="/LICENSES/Apache-2.0.txt">Apache-2.0</a></p>' +
    (details.noticeText ? '<p>' + escape(details.noticeText) + ' <a href="' + escape(root + "NOTICE") + '">Source NOTICE</a></p>' : '') +
    sourceTerms(pkg) + proofMaterials(details) + proofReferences(details) + otherVersions(details.otherVersions) + '<section><h2>Modules</h2><p>This proof has no declaration index or theorem-use data yet. Each module welcomes an independent description under CC BY 4.0.</p>' + wantedLink(pkg) + (catalogue.some(p => p.comparisonSource === pkg) ? compareLink(pkg) : '') + moduleGroups(modules,pkg) + '</section>', {attrs:'data-static-page="true"'});
}
for (const sourceKey of new Set(catalogue.filter(p => p.material).map(p => p.sourceKey))) {
  const results = catalogue.filter(p => p.sourceKey === sourceKey);
  const source = proof.packages[sourceKey];
  const entry = results[0];
  await page('/proofs/' + sourceKey + '/', sourceKey, 'Catalogued proofs in this source.',
    '<h1>' + escape(sourceKey) + '</h1><p>Repository: <a href="' + escape(source.url) + '">' + escape(source.url) +
    '</a> · Pin: <a href="' + escape(source.url + '/tree/' + source.commit) + '">' + escape(source.commit) +
    '</a> · <a href="' + escape(source.sourceTerms.LICENSE) + '">' + escape(source.license) +
    '</a></p><p>Writer: <a href="' + escape(entry.creditSource) + '">' + escape(entry.credit) + '</a></p><ul>' + results.map(p => '<li><a href="/proofs/' + escape(p.package) +
    '/">' + p.titleHTML + '</a></li>').join('') + '</ul>', {attrs:'data-static-page="true"'});
}
for (const p of catalogue.filter(p => p.material)) {
  const other = catalogue.find(q => q.package === p.comparisonSource);
  const root = p.rootURL + proof.packages[p.sourceKey].repositoryFolder;
  const material = (label, file, url) => '<section class="proof-source"><h2>' + escape(label) +
    '</h2><p><a href="' + escape(url) + '">Pinned source</a></p>' +
    (file === 'scope.md' ? '<div class="informalization">' + p.scopeHTML + '</div>' : '<pre>' + escape(p.material[file]) + '</pre>') + '</section>';
  const statement = material('Comparator statement and definitions', 'statement.lean', root + p.statement);
  const moduleLink = (pkg, path) => '<p><a href="' + escape(route("module",path,pkg)) +
    '">Read or contribute an informalization of ' + identifier(path) + '</a></p>';
  const paper = p.rootURL + 'preprints/VP-and-VNP-are-different-November-23-2026/build/';
  const sourceModule = path => '<a href="' + escape(route("module",path,p.sourceKey)) + '">' + identifier(path.split("/").at(-1)) + '</a>';
  const adaptation = p.package === "openai-math/VPVNP" ? '<p>The source notes in ' +
    sourceModule("OAI/Computability/VPVNP/ShiftedResidue.lean") + ' and ' +
    sourceModule("OAI/Computability/VPVNP/StateCount.lean") +
    ' credit results of Kirill Khoruzhii. The Lean notes of this proof cite a paper under the title “VP and VNP differ over every field”.</p><p>The manuscript says it adapts the square scheme of “Claude (Anthropic). A 2^o(n) Time Algorithm for 3-SAT”. <a href="' +
    escape(paper + 'Paper.tex#L1099-L1103') + '">Manuscript</a> · <a href="' +
    escape(paper + 'references.tex#L87-L88') + '">Reference</a> · <a href="/proofs/eth/">ETH proof</a></p>' : '';
  const roleLink = (label, path) => '<p>' + label + ': <a href="' + escape(route('module',path,p.sourceKey)) + '">' + identifier(path) + '</a></p>';
  await page('/proofs/' + p.package + '/', p.title, p.title,
    '<h1>' + p.titleHTML + '</h1><p>Formalization: <a href="' + escape(p.creditSource) + '">' + escape(p.credit) +
    '</a> · <a href="/proofs/' + p.sourceKey + '/">' + p.sourceKey + '</a></p>' + sourceTerms(p.sourceKey) + adaptation +
    roleLink('Root',p.root) + roleLink('Statement module',p.statement) + roleLink('Solution module',p.solution) + statement +
    material('Comparator configuration', 'config.json',root + p.statement.replace(/\.lean$/, '.json')) +
    material(p.family ? 'Family scope note · Euclidean tensor geometry and its applications to complexity and combinatorics' : 'Scope note','scope.md',root + p.scope) +
    proofReferences(p) + (other ? compareLink(other.package) : "") + wantedLink(p.sourceKey) +
    '<section><h2>Modules (' + p.moduleCount + ')</h2>' + moduleGroups(p.modules,p.sourceKey) + '</section>', {attrs:'data-static-page="true"'});
  if (!other) continue;
  const otherLink = other.root + p.comparisonFile;
  const topic = other.package === 'eth' ? 'Exponential Time Hypothesis' : 'VP and VNP';
  const comparisonHeading = item => {
    const source = proof.packages[item.sourceKey || item.package];
    return '<h2><a href="/proofs/' + escape(item.package) + '/">' + item.titleHTML + '</a></h2>' +
      '<p>Formalization: <a href="' + escape(item.creditSource) + '">' + escape(item.credit) + '</a> · Pin: <a href="' +
      escape(source.url + '/tree/' + item.commit) + '">' + escape(item.commit.slice(0, 12)) + '</a></p>';
  };
  await page('/comparisons/' + other.package + '/', topic, 'Formal statements and definitions at their pinned revisions.',
    '<h1>' + topic + '</h1><div class="proof-comparison"><section>' + comparisonHeading(other) +
    moduleLink(other.package,'Challenge.lean') + material('Comparator statement','other-challenge.lean',other.root+'Challenge.lean') +
    moduleLink(other.package,p.comparisonFile) + material('Definitions','comparison.lean',otherLink) +
    '</section><section>' + comparisonHeading(p) + moduleLink(p.sourceKey,p.statement) + statement +
    '</section></div>', {attrs:'data-static-page="true"'});
}

const shells = [];
const selectable = [];
for (const [type, dir, render] of [["module", "m", modulePage], ["declaration", "d", declarationPage]]) {
  const group = samples.filter(s => s.type === type);
  for (const s of group) {
    const html = render(proof, records[s.id]);
    const { name, description } = recordMetadata(type, s.value, s.package);
    const samplePath = "/sample/" + s.package + "/" + s.id + "/";
    await page(samplePath, name, description, html, {attrs:'data-ready="true"'});
    selectable.push({type, key:s.value, package:s.package, name, description, samplePath, html});
  }
  shells.push({type, dir, group});
}
const selector = await publishAsset("select-static.js", js =>
  js.toString().replace("/* @samples@ */ []", () => JSON.stringify(selectable)));
for (const {type, dir, group} of shells) {
  await page("/" + dir + "/", type === "module" ? "Module" : "Declaration",
    type === "module" ? "Look up a Lean module by its original source path." : "Look up a Lean declaration by its qualified name.",
    "Opening " + type + "…<noscript><p>Available static pages</p>" + sampleLinks(group, true) + "</noscript>",
    {attrs:`data-type="${type}" data-sample-selector="${selector}"`, indexable:false});
}
for (const [key, data] of Object.entries(extra)) {
  const path = data.facts[0].path;
  const { name, description } = recordMetadata("module", path, data.facts[0].package);
  await page("/m/records/" + key + "/", name, description, modulePage(proof, data),
    {attrs:'data-ready="true" data-package="' + escape(data.facts[0].package) + '" data-original-path="' + escape(path) + '"'});
}
await page("/wanted/", "Most-wanted informalizations", "Modules awaiting a contributed informalization.", wantedPage(proof, board, 1, wantedCount), {attrs:'data-board="true"'});

const lists = [];
for (const kind of ["theorem", "definition"]) {
  const cards = unmatched.filter(c => c.kind === kind);
  if (!cards.length) continue;
  const rows = cards.map(c => `<li><a href="${escape(c.url)}">${escape(c.title)}</a></li>`);
  lists.push(`<section><h2>${kind === "theorem" ? "Theorems" : "Definitions"} (${cards.length})</h2><ul>${rows.join("")}</ul></section>`);
}
const definitions = unmatched.filter(c => c.kind === "definition").length;
const groupDescription = definitions && definitions === unmatched.length ? `All ${definitions} are definition pages.` : "";
await page("/unmatched/", "Unmatched statements", "Statements and definitions awaiting a link to an original Lean module.",
  `<h1>Unmatched statements</h1><p>${unmatched.length} entries from Andrew O’Desky’s <a href="https://andrewodesky.com/rh/">Statements of the Lean RH project</a> have no module link. ${groupDescription}</p>` +
  '<p><a href="' + ledger + '/blob/main/CONTRIBUTING.md#propose-an-outside-link">Propose a module link</a></p>' + lists.join(""), {attrs:'data-static-page="true"'});
await page("/sql/", "SQL console", "Run read-only SQLite queries against the proof directory in your browser.",
  await readFile("tools/templates/console.html", "utf8") + kernelCredit(proof), {script:"/console.mjs", style:"/sql/console.css"});
if (previewProbe) await page("/probe.html", "Database test page", "Preview test page for the directory’s browser database fixtures.",
  await readFile("tools/templates/probe.html", "utf8") + kernelCredit(proof), {script:"/app.mjs", noindex:true, indexable:false});
const importRows = imports.map(row => `<tr><th scope="row">${escape(row.import)}</th><td><a href="${escape(row.source)}">Source</a></td><td>${escape(row.pin)}</td><td>${escape(row.license)}</td><td><code>${escape(row.replay)}</code></td><td>${escape(row.entries)}</td></tr>`).join("");
await page("/sources/", "Sources and licences", "Pinned imports, their licences and replay commands.",
  `<h1>Sources and licences</h1><p>New text written or generated for QED Codex is CC BY 4.0. Previously published text shows its source licence. Imported text keeps its own licence, shown beside it. Code is MIT.</p><div class="import-register"><table><caption>Register of imported entries</caption><thead><tr><th>Import</th><th>Source</th><th>Pin</th><th>Licence</th><th>Replay from the captured input</th><th>Entries</th></tr></thead><tbody>${importRows}</tbody></table></div>`, {attrs:'data-static-page="true"'});
await page("/about/", "About QED Codex", "Sources, licenses, contribution guidelines and definitions for the proof directory.",
  (await readFile("tools/templates/about.html","utf8")).replaceAll("{{repository}}",ledger)
    .replaceAll("{{email}}",escape(settings.contact_email)).replace("{{formalization}}",formalization(proof))
    .replace("{{kernel}}",kernelCredit(proof)), {attrs:'data-static-page="true"'});
await page("/404.html","Page not found","This address has no directory page.",
  '<h1>Page not found</h1><p><a href="/">Search the directory</a></p>', {attrs:'data-static-page="true"', noindex:true,indexable:false});
if (baseURL) {
  await writeFile(join(out,"robots.txt"),"User-agent: *\nAllow: /\nSitemap: " + new URL("/sitemap.xml",baseURL).href + "\n");
  const entries = sitemap.sort().map(address => `  <url><loc>${escape(address)}</loc></url>`);
  await writeFile(join(out, "sitemap.xml"), '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + entries.join("\n") + "\n</urlset>\n");
}
