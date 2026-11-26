// Compare real SQLite module routes with the static template using each engine's DOM serialization.
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { parseArgs } from "node:util";
import { DatabaseSync } from "node:sqlite";
import { chromium, firefox, webkit } from "playwright";
import { localPackage } from "./package-measurements.mjs";

const { positionals, values } = parseArgs({
  allowPositionals: true,
  options: { package: { type: "string" }, paths: { type: "string" } },
});
const [database, site, reference, engine, previous] = positionals;
if (
  positionals.length < 4 ||
  positionals.length > 5 ||
  !["chromium", "firefox", "webkit"].includes(engine) ||
  Boolean(values.package) !== Boolean(values.paths)
) {
  throw Error(
    "Usage: check-source-note-pages.mjs DATABASE SITE STATIC_REFERENCE ENGINE [PREVIOUS] [--package KEY --paths FILE]",
  );
}
const db = new DatabaseSync(database, { readOnly: true });
const config = JSON.parse(await readFile(join(site, "directory.json")));
const kept = new Set(config.staticModules);
// An import inventory can include files without notes and modules kept as static records.
let selected;
if (values.paths) {
  const inventory = await readFile(values.paths, "utf8");
  selected = new Set(inventory.split(/\r?\n/).filter(Boolean));
  if (!selected.size) throw Error("Empty module path list: " + values.paths);
  const known = new Set(
    db
      .prepare("SELECT path FROM modules WHERE package=?")
      .all(values.package)
      .map((row) => row.path),
  );
  for (const path of selected) {
    if (!known.has(path))
      throw Error("Unknown module in " + values.package + ": " + path);
  }
}
const modules = db
  .prepare(
    `SELECT m.id,m.package,m.path,i.source_url,i.copyright FROM modules m
   JOIN informalizations i ON m.id=i.module WHERE i.entry_type='source-documentation'
   AND NOT EXISTS (SELECT 1 FROM informalizations other WHERE other.module=m.id AND other.entry_type!='source-documentation')
   ORDER BY m.package,m.path`,
  )
  .all()
  .filter(
    (row) =>
      !selected || (row.package === values.package && selected.has(row.path)),
  );
const headings = db.prepare(
  "SELECT anchor FROM note_headings WHERE module=? ORDER BY anchor",
);
const proofs = db.prepare(`SELECT p.id,p.title FROM proofs p WHERE p.id IN (
  SELECT proof FROM proof_modules WHERE module=?1 UNION SELECT proof FROM proof_roles WHERE module=?1)`);
const server = await localPackage(site, { cache: true });
const browser = await { chromium, firefox, webkit }[engine].launch({
  executablePath: process.env[engine.toUpperCase() + "_EXECUTABLE"],
});
let next = 0,
  failures = 0,
  noteTargets = 0;
async function lane() {
  while (next < modules.length) {
    const context = await browser.newContext({
      viewport: { width: 390, height: 820 },
    });
    try {
      const page = await context.newPage();
      for (let i = 0; i < 40 && next < modules.length; i++) {
        const row = modules[next++];
        try {
          const key =
            row.package +
            "/" +
            createHash("sha256").update(row.path).digest("hex").slice(0, 16);
          assert.ok(!kept.has(key), key);
          const path = "m/records/" + key + "/index.html";
          const input = {
            row,
            html: await readFile(join(reference, path), "utf8"),
            original: previous
              ? await readFile(join(previous, path), "utf8")
              : null,
            headings: headings.all(row.id).map((h) => h.anchor),
            proofs: proofs.all({ 1: row.id }),
            terms: config.proof.packages[row.package].sourceTerms,
          };
          const url = new URL("/m/", server.url);
          url.search = new URLSearchParams({ pkg: row.package, p: row.path });
          if (input.headings.length) url.hash = input.headings[0];
          const res = await page.goto(url.href, {
            waitUntil: "domcontentloaded",
          });
          assert.equal(res.status(), 200);
          await page.waitForFunction(
            (p) =>
              document.querySelector("form.contribute")?.dataset.path === p,
            row.path,
          );
          assert.ok(page.workers().length, "SQLite worker missing");
          const outcome = await page
            .locator("main")
            .evaluate(
              (main, { row, html, original, headings, proofs, terms }) => {
                const parse = (s) =>
                  new DOMParser()
                    .parseFromString(s, "text/html")
                    .querySelector("main");
                if (main.innerHTML !== parse(html).innerHTML)
                  throw Error("main.innerHTML differs");
                let previousChange = "";
                if (original && main.innerHTML !== parse(original).innerHTML) {
                  const copy = parse(html);
                  const labels = [...copy.querySelectorAll("p")].find(
                    (e) =>
                      e.tagName === "P" && e.textContent.startsWith("Proofs: "),
                  );
                  labels?.remove();
                  if (copy.innerHTML !== parse(original).innerHTML)
                    throw Error(
                      "Additional change from the approved static main",
                    );
                  previousChange = "added proof label";
                }
                const ids = [...main.querySelectorAll("article h3[id]")]
                  .map((h) => h.id)
                  .sort();
                if (
                  JSON.stringify(ids) !== JSON.stringify(headings) ||
                  ids.some((id) => !document.getElementById(id))
                )
                  throw Error("Note targets differ");
                if (
                  headings.length &&
                  decodeURIComponent(location.hash.slice(1)) !== headings[0]
                )
                  throw Error("Fragment target missing");
                const meta = main.querySelector(
                  "article.informalization p.meta",
                );
                const links = [...meta.querySelectorAll("a")].map((a) =>
                  a.getAttribute("href"),
                );
                for (const href of [...Object.values(terms), row.source_url])
                  if (!links.includes(href))
                    throw Error("Missing credit link " + href);
                if (
                  !meta.textContent.includes(
                    row.copyright || "no copyright line in this file",
                  )
                )
                  throw Error("Missing copyright");
                const labels = [...main.querySelectorAll("a")];
                for (const p of proofs)
                  if (
                    !labels.some(
                      (a) =>
                        a.pathname === "/proofs/" + p.id + "/" &&
                        a.textContent === p.title,
                    )
                  )
                    throw Error("Missing proof " + p.id);
                if (document.documentElement.scrollWidth > innerWidth)
                  throw Error("Page overflows at 390px");
                return {
                  headings: ids.length,
                  proofs: proofs.length,
                  previousChange,
                };
              },
              input,
            );
          noteTargets += outcome.headings;
          console.log(
            JSON.stringify({
              engine,
              package: row.package,
              path: row.path,
              ...outcome,
            }),
          );
        } catch (e) {
          failures++;
          console.log(
            JSON.stringify({
              engine,
              package: row.package,
              path: row.path,
              error: e.message,
            }),
          );
        }
      }
    } finally {
      await context.close();
    }
  }
}
try {
  await Promise.all(Array.from({ length: 4 }, lane));
} finally {
  await browser.close();
  await server.close();
  db.close();
}
console.error(
  JSON.stringify({
    engine,
    package: values.package,
    requested: selected?.size,
    pages: modules.length,
    skipped: selected ? selected.size - modules.length : undefined,
    noteTargets,
    failures,
  }),
);
if (failures) process.exitCode = 1;
