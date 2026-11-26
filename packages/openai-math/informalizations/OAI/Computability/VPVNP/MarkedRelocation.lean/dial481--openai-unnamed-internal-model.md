---
{
  "module": "OAI/Computability/VPVNP/MarkedRelocation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MarkedRelocation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MarkedRelocation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Relocation of one marked tensor index

In Lemma A.1 of *VP and VNP differ over every field*, exterior multiplication
and contraction on the marked index split its product with a wire. Dividing
by the wire value leaves two ratios of adjacent exterior dimensions. Their
bounds over tensor powers yield geometric interpolation of the endpoint
values.


### `value_marked_atFraction_le`

 Lemma A.1. Placing a marked tensor index at a fractional point gives a
spectral value bounded by the weighted geometric mean of the endpoint
placements. The bound also holds for zero coefficient arrays. 
