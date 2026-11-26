---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutReplaceConstraints.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutReplaceConstraints.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutReplaceConstraints.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Runtime row order and basis choices need not match `Fintype.equivFin`.
Any explicitly supplied integer row family spanning the old one over the
rationals retains exact locality with the same polynomial rows and heads. 

### `signature_reindex_eq_iff`

 Reordering or redundantly enumerating all rows preserves the exact
integer signature partition. This is independent of a chosen row basis. 
