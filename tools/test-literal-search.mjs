import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { DatabaseSync } from "node:sqlite";
import { parameters } from "../site/search-input.mjs";

const queries=JSON.parse(readFileSync("site/queries.json","utf8"));
const db=new DatabaseSync(process.argv[2] || "build/rh.sqlite3",{readOnly:true});
const offset=db.prepare("SELECT value FROM summary WHERE metric='fts_declaration_offset'").get().value;
const rows=(term,skip=0)=>db.prepare(queries.search.matches).all(...parameters("search",{term,offset:skip},offset));
const count=term=>db.prepare(queries.searchCount.totals).get(...parameters("searchCount",term,offset)).total;
try {
  for(const input of ["'",'"',"(",")","*","-",":","^","+","{","}",".","/","_"," "]) {
    assert.equal(parameters("search",input,offset)[0],"");
    assert.equal(count(input),0);
    assert.deepEqual(rows(input),[]);
  }
  for(const word of ["AND","OR","NOT","NEAR"]) {
    assert.equal(parameters("search",word,offset)[0],'"'+word+'"');
    assert.ok(count(word)>=rows(word).length);
  }
  assert.equal(parameters("search","Γ.β/λ_23' AND",offset)[0],'"Γ" AND "β" AND "λ" AND "23" AND "AND"');
  assert.equal(parameters("search",`x' y"`,offset)[0],'"x" AND "y"');
  assert.equal(count("Formalism AND siegel*"),0);
  assert.ok(count("Formalism siegel")>0);
  assert.equal(rows("src/Main")[0].name,"src/Main.lean");
  assert.equal(rows("src/Main.lean")[0].kind,"module");
  assert.equal(rows("GlobalTheory.Mem.Top.Bl.anyGeometry")[0].name,"GlobalTheory.Mem.Top.Bl.anyGeometry");
  assert.equal(rows("Formalism.DivisorInequality.BaseLevelBoundsWithCovolume")[0].kind,"declaration");
  const hits=[...rows("heckeone"),...rows("heckeone",20),...rows("heckeone",40)];
  assert.equal(hits[0].name.split(".").at(-1).toLowerCase(),"heckeone");
  assert.equal(hits.length,44);
  assert.equal(count("heckeone"),hits.length);
  assert.equal(new Set(hits.map(r=>JSON.stringify(r))).size,hits.length);
  for (const name of ["OAI.Computability.VPVNP.Standalone.vp_ne_vnp","vp_ne_vnp","exact_count_and_sat","riemannHypothesis"]) {
    assert.equal(rows(name)[0].kind, "proof", name);
  }
  for (const short of ["square_exponent", "dual_exponent", "rectangular_exponent"]) {
    const full = "OAI.LinearAlgebra.SpectralBooks." + short;
    for (const query of [short, full]) {
      const first = rows(query)[0];
      assert.equal(first.proof, "openai-math/MatrixExponent");
      assert.equal(first.name, full);
    }
  }
  for (const name of ["riemannHypothesis","riemannZeta_eq_zero_re","LFunction_ne_zero_of_half_lt_re",
                       "LFunction_eq_zero_re","LFunction_eq_zero_re_of_isPrimitive"]) {
    const result = rows(name);
    assert.ok(result.some(hit => hit.proof === "grh-readable"), name);
    assert.ok(result.some(hit => hit.kind === "declaration" && hit.package === "riemann-hypothesis" && hit.name === name), name);
    if (name === "riemannHypothesis")
      assert.deepEqual(result.slice(0,2).map(hit => hit.proof), ["riemann-hypothesis","grh-readable"]);
  }
  const note = db.prepare("SELECT h.name,h.anchor,m.path,m.package FROM note_headings h JOIN modules m ON m.id=h.module WHERE h.lookup IN (SELECT lookup FROM note_headings GROUP BY lookup HAVING count(*)=1) LIMIT 1").get();
  assert.ok(rows(note.name).some(hit => hit.kind === "source note" && hit.anchor === note.anchor &&
    hit.path === note.path && hit.package === note.package));
  console.log("Literal tokens, indexed exact results, total and pagination passed");
} finally {db.close();}
