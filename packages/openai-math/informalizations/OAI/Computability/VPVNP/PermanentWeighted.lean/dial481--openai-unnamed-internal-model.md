---
{
  "module": "OAI/Computability/VPVNP/PermanentWeighted.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentWeighted.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentWeighted.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Weighted exact-one assignments as a projection of the permanent

The squarefree interior coefficient enforces the equality gadget for each literal.
The exterior coefficient enforces consistent orientations of the variable rings. Finally,
there is exactly one compatible choice in each clause of a satisfying assignment.


### `permanent_graph_eq_weighted`

 The weighted graph computes exactly the generating polynomial of exact-one assignments. 

### `weighted_projection`

 A p-projection with literal variable-or-constant entries, valid whenever the field's
characteristic is different from two. 
