import {readDirectoryProof} from "./read-directory-proof.mjs";
import assert from "node:assert/strict";
import {readFileSync} from "node:fs";
import {escape, modulePage} from "../site/record.mjs";

const proof = readDirectoryProof();
proof.repository = "https://github.com/qed-codex/qed-codex";
const data = {facts:[{path:"src/Main.lean",package:"riemann-hypothesis"}],links:[],members:[],disputes:[]};
for (const license of ["CC-BY-4.0","with-permission","Apache-2.0","MIT","CC0-1.0"]) {
  const copyright = ["MIT","Apache-2.0"].includes(license) ? "Copyright Example & collaborators" : null;
  data.informalizations = [{writer:"Example",author:"dial481",kind:null,license,copyright,source_url:"https://example.org/original",
    declarations_json:"[]",agrees_with_json:"{}",informalization_html:"<p>Body.</p>"}];
  const html = modulePage(proof,data);
  const byline = html.match(/<article class="informalization"[^>]*><p class="meta">([\s\S]*?)<\/p>/)[1];
  if (license === "with-permission") assert.match(byline,/href="https:\/\/example.org\/original">Used with permission of Example/);
  else assert.ok(byline.includes('href="/LICENSES/'+license+'.txt"'));
  if (copyright) assert.ok(byline.includes("Copyright Example &amp; collaborators"));
}
console.log("Five entry license bylines passed.");

const entry = data.informalizations[0];
const source = {...entry, writer:"Source writer", entry_type:"source-documentation"};
const alone = modulePage(proof,{...data, informalizations:[source]});
assert.match(alone,/class="status">no informalization</);
assert.ok(alone.indexOf("From the source") < alone.indexOf("Source writer"));
assert.ok(alone.indexOf("Source writer") < alone.indexOf(">Informalizations<"));
const mixed = modulePage(proof,{...data, informalizations:[source, entry]});
assert.match(mixed,/class="status">one informalization</);
assert.ok(mixed.indexOf(">Informalizations<") < mixed.indexOf("<strong>Example</strong>"));

const block = "  Alpha.Beta_a/b\n\n\t<code> & </pre>\n";
const fenced = "<pre><code>" + escape(block) + "</code></pre>";
const inline = "<p><code>Alpha.Beta_a/b</code></p>";
for (const item of [source, entry]) {
  const body = fenced + inline + fenced;
  const html = modulePage(proof, {...data, informalizations:[{...item, informalization_html:body}]});
  // Exact serialized contents check both the text (including whitespace) and the absence of child tags.
  assert.deepEqual(html.match(/<pre>[\s\S]*?<\/pre>/g), [fenced, fenced]);
  assert.match(html, /<p><code class="identifier"><span>Alpha\.<\/span><wbr>/);
}
console.log("Fenced text, escaping and inline identifiers passed for contributed and source entries.");

const published = {...entry, origin:"other-author",license:"MIT",license_source:"https://example.org/terms",
  copyright:"none in the source", notice:"<original>\nSecond line", changes:"Excerpted."};
const publishedPage = modulePage(proof,{...data,informalizations:[published]});
assert.match(publishedPage,/href="\/LICENSES\/MIT.txt">MIT</);
assert.match(publishedPage,/no copyright line in the source/);
assert.match(publishedPage,/href="https:\/\/example.org\/terms">licence stated at</);
assert.match(publishedPage,/Changes: Excerpted\./);
assert.ok(publishedPage.includes("<details><summary>NOTICE</summary><pre>&lt;original&gt;\nSecond line</pre></details>"));
