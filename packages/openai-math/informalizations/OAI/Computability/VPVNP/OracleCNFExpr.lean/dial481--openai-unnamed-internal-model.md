---
{
  "module": "OAI/Computability/VPVNP/OracleCNFExpr.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/OracleCNFExpr.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/OracleCNFExpr.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Boolean expressions for the coefficient oracle's CNF

Each clause becomes a disjunction of its signed input flags. Negating the
disjunction of failed clauses enforces their conjunction, including the empty
formula and formulas containing empty clauses.


### `formula`

 Expression testing the CNF on the indicated wires of a larger Boolean frame. 

### `formula_size_le`

 The expression has linear size in the number of literals and clauses. 
