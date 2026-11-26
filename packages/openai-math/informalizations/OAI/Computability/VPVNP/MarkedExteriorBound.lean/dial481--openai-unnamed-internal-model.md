---
{
  "module": "OAI/Computability/VPVNP/MarkedExteriorBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MarkedExteriorBound.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MarkedExteriorBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Finite exterior bound for a marked tensor

In Appendix A.2 the degree-`h` exterior identity gives two orders of the
creation and contraction operators. Placing the old marked index at opposite
endpoints bounds the two orders by wire costs through degrees `h+1` and `h-1`.
The matrices are the same integral matrices over every field.


### `value_marked_exterior_bound`

 The finite, unpowered inequality underlying the relocation estimate in
Lemma A.1. The parties `x`, `a`, and `b` may coincide. 
