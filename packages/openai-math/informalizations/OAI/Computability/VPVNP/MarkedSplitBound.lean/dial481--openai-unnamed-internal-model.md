---
{
  "module": "OAI/Computability/VPVNP/MarkedSplitBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MarkedSplitBound.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MarkedSplitBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cost of the two orders of a marked-index operator

Appendix A.2 places the exterior column and row at fixed endpoints, with an
old index and a newly exposed index. The two matrix orders pair these four
roles in opposite ways. Local restriction first realizes the factorization
and then contracts the old index against the background tensor.


### `value_splitMarkedTerm_le_plus`

 The old index pairs with the row, and the new index pairs with the column. 

### `value_splitMarkedTerm_le_minus`

 The old index pairs with the column, and the new index pairs with the row. 
