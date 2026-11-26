---
{
  "module": "OAI/Computability/VPVNP/PermanentGraphRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentGraphRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentGraphRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Row factors of the exact-one cycle-cover graph

Regard the exterior columns as variables of the coefficient ring. Each occurrence
then supplies its three internal row factors, with the two exits contributing
exterior column variables. Each variable-ring row chooses one of two directions,
and each clause row chooses an occurrence in that clause.


### `rowProduct_split`

 Decomposition into one equality factor per occurrence and one choice factor per
exterior row. The coefficients of the internal polynomials are exterior polynomials. 
