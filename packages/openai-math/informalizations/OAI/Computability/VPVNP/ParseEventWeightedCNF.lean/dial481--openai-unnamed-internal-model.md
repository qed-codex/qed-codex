---
{
  "module": "OAI/Computability/VPVNP/ParseEventWeightedCNF.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseEventWeightedCNF.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseEventWeightedCNF.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Weighted CNF for a grammar state

The incidence clauses select one Boolean assignment per ordered parse. The
product of its selected coordinates counts every production scalar and every
terminal variable with the multiplicity of that occurrence in the tree.


### `eval_eq_weightedCNF`

 Reindex the grammar polynomial's parse expansion by satisfying Boolean
assignments to the incidence clauses. 
