import {bytes} from "./startup-assets.mjs";
import {
  directoryConfig as config,
  identifier,
  declarationPage, trailSection, siblingSection, outsideSection,
  escape,
  modulePage,
  wantedPage,
  newInformalization, writerSlug,
  route,
  recordMetadata,
} from "./record.mjs";

const main = document.querySelector("main");
let warmup,
  worker,
  startup,
  sequence = 0;
const pending = new Map();

function json(response) {
  if (!response.ok) throw Error("Could not load the directory.");
  return response.json();
}
function prime() {
  if (!warmup)
    warmup = (async () => {
      const manifest = await fetch("/proof.json").then(json);
      const [wasm, interior] = await Promise.all([
        bytes("/vendor/sqlite3.wasm"),
        bytes("/db/" + manifest.buildId + "/interior"),
      ]);
      return { manifest, wasm, interior };
    })().catch((error) => {
      warmup = null;
      throw error;
    });
  return warmup;
}
async function query(kind, value) {
  if (!worker) {
    worker = new Worker("/query-thread.mjs", { type: "module" });
    worker.onmessage = ({ data }) => {
      const handler = pending.get(data.id);
      if (!handler) return;
      pending.delete(data.id);
      if (data.error) handler.reject(Error(data.error));
      else handler.resolve(data.result);
    };
    worker.onerror = () => {
      for (const handler of pending.values())
        handler.reject(Error("The database worker could not run."));
      pending.clear();
    };
    startup = prime();
  }
  const assets = await startup;
  const initial = assets.wasm.byteLength > 0;
  return new Promise((resolve, reject) => {
    const id = ++sequence;
    pending.set(id, { resolve, reject });
    worker.postMessage(
      { id, kind, value, assets: initial ? assets : undefined },
      initial ? [assets.wasm, assets.interior] : [],
    );
  });
}

async function showSource() {
  const box = main.querySelector(".lean-source");
  if (!box) return;
  const { proof } = await config;
  const raw =
    proof.packages[box.dataset.package].url.replace(
      "https://github.com/",
      "https://raw.githubusercontent.com/",
    ) +
    "/" +
    proof.packages[box.dataset.package].commit +
    "/" +
    ((proof.packages[box.dataset.package].repositoryFolder || "") + box.dataset.path).split("/").map(encodeURIComponent).join("/");
  try {
    const response = await fetch(raw, { credentials: "omit" });
    if (!response.ok) throw Error("Source unavailable");
    const text = (await response.text()).split(/\r?\n/);
    const start = Number(box.dataset.start),
      end = Number(box.dataset.end);
    if (!(start >= 1 && end >= start && end <= text.length))
      throw Error("Line range unavailable");
    const pre = document.createElement("pre"),
      code = document.createElement("code");
    code.textContent = text.slice(start - 1, end).join("\n");
    pre.className = "source";
    pre.append(code);
    box.replaceChildren(pre);
  } catch {
    box.textContent = "Use the pinned source link to read this declaration.";
  }
}
function recordHead(type, value, pkg, path) {
  const {name, description} = recordMetadata(type, value, pkg);
  document.title = name + " · QED Codex";
  document.querySelector('[property="og:title"]').content = document.title;
  document.querySelector('[name="description"]').content = description;
  document.querySelector('[property="og:description"]').content = description;
  const canonical = document.querySelector('link[rel="canonical"]');
  if (canonical && path) canonical.href = new URL(path, canonical.href).href;
  else canonical?.remove();
}
async function readTrail(input) {
  const {manifest} = await prime();
  if (!manifest.traceNodesPerPiece) return query("trail", input);
  const {positions} = await query("tracePosition", input);
  if (!positions.length) return {sites:[]};
  try {
    let id = positions[0].id;
    const piece = Math.floor(id / manifest.traceNodesPerPiece);
    const response = await fetch("/db/" + manifest.buildId + "/trails-v1/" + piece);
    if (!response.ok) throw Error("Trail unavailable");
    const rows = await new Response(response.body.pipeThrough(new DecompressionStream("gzip"))).json();
    const sites = [];
    const visited = new Set();
    while (id !== null) {
      if (visited.has(id)) throw Error("Circular trail");
      visited.add(id);
      const [parent, packageKey, path, line, use_line, indexed, name] = rows[id];
      sites.push({step:sites.length, package:packageKey, path, line, use_line, indexed, name});
      id = parent;
    }
    return {sites};
  } catch {
    return query("trail", input);
  }
}

async function fillDeclaration(part, request, render) {
  const box = main.querySelector('[data-decl-part="' + part + '"]');
  try {
    box.innerHTML = render(await request);
  } catch {
    box.textContent = "Could not load " + part + ". Reload to try again.";
  }
}

async function openRecord() {
  const type = main.dataset.type;
  if (type && main.dataset.ready !== "true") {
    const value = new URLSearchParams(location.search).get(
      type === "module" ? "p" : "n",
    );
    const pkg = new URLSearchParams(location.search).get("pkg");
    if (!pkg || !value) {
      main.textContent = !pkg ? "A package is required. Choose a " + type + " from the search page." : "Choose a " + type + " from the search page.";
      document.querySelector('link[rel="canonical"]')?.remove();
      return;
    }
    const { proof, samples, staticModules } = await config;
    if (main.dataset.sampleSelector && samples.some(s => s.type === type && s.package === pkg && s.value === value)) {
      // Only sample permalinks need the pre-rendered sample bodies.
      await import(main.dataset.sampleSelector).catch(() => {});
      if (main.dataset.ready === "true") return showSource();
    }
    if (!Object.hasOwn(proof.packages, pkg)) {
      main.textContent = "Unknown package.";
      document.querySelector('link[rel="canonical"]')?.remove();
      return;
    }
    const input = {name:value, pkg, sourceRoot:proof.packages[pkg].sourceRoot};
    if (type === "module" && value.endsWith(".lean")) {
      const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(value));
      const key = pkg + "/" + [...new Uint8Array(digest, 0, 8)].map(n => n.toString(16).padStart(2, "0")).join("");
      if (staticModules.includes(key)) {
        const response = await fetch("/m/records/" + key + "/");
        if (response.ok) {
          const doc = new DOMParser().parseFromString(await response.text(), "text/html");
          const compiled = doc.querySelector("main[data-original-path]");
          if (compiled?.dataset.originalPath === value && compiled.dataset.package === pkg) {
            main.replaceChildren(...compiled.childNodes);
            recordHead(type, value, pkg, "/m/records/" + key + "/");
            return;
          }
        }
      }
    }
    const data = await query(type === "declaration" ? "declarationHead" : type, input);
    if (type === "module" && data.facts[0]?.path !== value) data.facts = [];
    if (type === "module") {
      main.innerHTML = modulePage(proof, data);
      if (data.facts.length)
        history.replaceState(null, "", route(type, data.facts[0].path, pkg) + location.hash);
    } else {
      main.innerHTML = declarationPage(proof, data);
      const d = data.declarations[0];
      if (d) {
        recordHead(type, d.name, pkg, null);
        void showSource();
        await Promise.all([
          fillDeclaration("trail", readTrail(input), detail => trailSection(proof, d, detail)),
          fillDeclaration("siblings", query("siblings", input), detail => siblingSection(d, detail)),
          fillDeclaration("outside", query("declarationOutside", input), detail => outsideSection(detail.outside)),
        ]);
        main.dataset.declarationComplete = "true";
        return;
      }
    }
    const resolved = data.facts?.[0]?.path || data.declarations?.[0]?.name;
    if (resolved) recordHead(type, resolved, pkg, null);
    else {
      document.title = (type === "module" ? "Module" : "Declaration") + " not found · QED Codex";
      document.querySelector('[property="og:title"]').content = document.title;
      document.querySelector('link[rel="canonical"]')?.remove();
    }
  }
  await showSource();
}
function checkContribution(form) {
  const fields = form.elements;
  const third = fields.origin.value === "other-author";
  form.querySelector(".third-party").hidden = !third;
  for (const field of form.querySelectorAll(".third-party input, .third-party select, .third-party textarea")) field.disabled = !third;
  if (form.dataset.certification !== fields.origin.value) {
    fields.rights.checked = false;
    form.dataset.certification = fields.origin.value;
    form.querySelector(".certify span").textContent = third
      ? "This text is published under the licence I selected, and I have copied its notices exactly."
      : "I have the right to submit this under CC BY 4.0.";
  }
  fields.source.required = third;
  const writer = fields.writer.value;
  const slug = writerSlug(writer);
  fields.writer.setCustomValidity(writer && (!slug || writer !== writer.trim() ||
    /[\p{C}\p{Zl}\p{Zp}]/u.test(writer) || new TextEncoder().encode(slug).length > 210)
    ? "Enter a writer name that can be used in a file name." : "");
  for (const field of [fields.source, fields.license_source]) {
    let valid = true;
    if (third && field.value) {
      try {
        const url = new URL(field.value);
        valid = ["https:","http:"].includes(url.protocol) && !url.username && !url.password && !/\s/.test(field.value);
      } catch { valid = false; }
    }
    field.setCustomValidity(valid ? "" : "Enter an absolute HTTP or HTTPS address.");
  }
  form.querySelector("button").disabled = !form.checkValidity();
}
for (const type of ["input","change"]) main.addEventListener(type,event => {
  const form = event.target.closest("form.contribute");
  if (form) checkContribution(form);
});
main.addEventListener("submit", event => {
  const form = event.target.closest("form.contribute");
  if (!form) return;
  event.preventDefault();
  checkContribution(form);
  if (!form.reportValidity()) return;
  location.assign(newInformalization(form.dataset.path,Object.fromEntries(new FormData(form)),form.dataset.commit,form.dataset.repo,form.dataset.package,form.dataset.indexed === "true"));
});

const search = document.querySelector(".search-box");
if (search) {
  const warmSearch = () => prime().catch(() => {});
  if ("requestIdleCallback" in window)
    requestIdleCallback(warmSearch, {timeout:1500});
  else
    window.addEventListener("load", () => setTimeout(warmSearch, 32), {once:true});
  const input = search.querySelector("input"),
    output = document.querySelector("#matches");
  let version = 0,
    timer;
  function searchAddress(term, page) {
    const url = new URL("/", location.href);
    url.searchParams.set("q",term);
    if (page > 1) url.searchParams.set("page",String(page));
    return url.pathname + url.search;
  }
  async function searchFor(kind, id, page = 1) {
    const term = input.value.trim();
    const prefix = term.replace(/\.lean$/, "").split(/[./]/).filter(Boolean).at(-1) || "";
    if (!term || (kind === "typeahead" && !prefix)) {
      output.innerHTML = kind === "search" ? '<p class="search-total" role="status">0 results</p><p>No matches on this page.</p>' : "";
      return;
    }
    const full = kind === "search";
    try {
      const results = await query(kind, full ? {term, offset:20*(page-1)} : prefix);
      if (id !== version) return;
      const exactNote = n => n.name.toLowerCase() === prefix.toLowerCase();
      const matches = full ? results.matches : [...results.proofs, ...results.notes.filter(exactNote),
        ...results.matches, ...results.notes.filter(n => !exactNote(n))].slice(0, 20);
      const rows = matches.map(m => {
        const path = m.kind === "module" && !full
          ? m.path : m.name;
        const href = m.kind === "proof" ? "/proofs/" + m.proof + "/" : m.kind === "source note"
          ? route("module", m.path, m.package) + "#" + m.anchor : route(m.kind, path, m.package);
        const label = m.kind === "source note" ? "Source documentation · " + m.path : m.kind;
        return '<li><a href="' + escape(href) + '"><code>' + identifier(m.name) +
          '</code></a> <span class="meta">' + escape(label) + ' · ' + escape(m.package) + '</span></li>';
      }).join("");
      output.innerHTML = (full ? '<p class="search-total" role="status">Counting results…</p>' : "") +
        (rows ? '<ul class="record-list">' + rows + '</ul>' : '<p>No matches on this page.</p>');
      if (!full) return;
      const {totals} = await query("searchCount",term);
      if (id !== version) return;
      const total = totals[0].total;
      output.querySelector(".search-total").textContent = total.toLocaleString("en-US") + (total === 1 ? " result" : " results");
      const pages = [];
      if (page > 1) pages.push([page-1, "Previous results"]);
      if (page*20 < total) pages.push([page+1, "More results"]);
      if (pages.length) output.insertAdjacentHTML("beforeend",'<nav aria-label="Search pages">' +
        pages.map(([n,label]) => '<a href="' + escape(searchAddress(term,n)) + '">' + label + '</a>').join(" · ") + '</nav>');
    } catch {
      if (version === id) output.textContent = "Search could not complete. Try a Lean name or a shorter term.";
    }
  }
  input.addEventListener("input", () => {
    const id = ++version;
    clearTimeout(timer);
    if (!input.value.trim()) { output.replaceChildren(); return; }
    timer = setTimeout(() => searchFor("typeahead",id),120);
  });
  function restore() {
    clearTimeout(timer);
    const url = new URL(location.href);
    input.value = url.searchParams.get("q") || "";
    const page = Number(url.searchParams.get("page") || 1);
    searchFor("search",++version, Number.isSafeInteger(page) && page > 0 && page <= 1000000 ? page : 1);
  }
  if (new URL(location.href).searchParams.has("q")) restore();
  else if (input.value.trim()) searchFor("typeahead",++version);
  window.addEventListener("popstate",restore);
  search.addEventListener("submit", event => {
    event.preventDefault();
    const term = input.value.trim();
    history.pushState(null,"",searchAddress(term,1));
    restore();
  });
} else if (main.dataset.board) {
  const start = Number(new URLSearchParams(location.search).get("start") ?? 1);
  if (!Number.isSafeInteger(start) || start < 1) {
    main.textContent = "Invalid starting rank.";
  } else if (new URLSearchParams(location.search).has("pkg")) {
    const pkg = new URLSearchParams(location.search).get("pkg");
    Promise.all([config, query("wantedSource", {pkg,start})]).then(([data,result]) => {
      main.innerHTML = wantedPage(data.proof,result.modules,start,result.total[0]?.n || 0,pkg);
    }).catch(() => { main.textContent = "Could not open this source board."; });
  } else if (start !== 1) {
    Promise.all([config, query("wanted", String(start))]).then(([data,result]) => {
      main.innerHTML = wantedPage(data.proof,result.modules,start,data.wantedCount);
    }).catch(() => {main.textContent = "Could not open this board page.";});
  }
} else if (!main.dataset.staticPage) {
  function scrollToEntry() {
    if (!/^#(?:informalization-|note-)/.test(location.hash)) return;
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const entry = document.getElementById(id);
    if (entry?.matches("article.informalization, article.informalization h3")) entry.scrollIntoView();
  }
  window.addEventListener("hashchange", scrollToEntry);
  openRecord().then(scrollToEntry).catch(() => {
    main.textContent =
      "This record could not be opened. Reload the page to try again.";
  });
}
