---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/Multiplicative/FixedPoint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Multiplicative/FixedPoint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Multiplicative/FixedPoint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A compact convex fixed-point theorem for normalized multiplication

This proves the particular fixed-point theorem needed in Appendix A.2 directly.
Finite geometric averages supply approximate eigenstates; compactness of the
whole state set supplies an exact eigenstate. No general Schauder theorem or
fixed-point premise is assumed.


### `projective_fixedPoint_of_compact_convex`

 A nonempty compact convex set of normalized positive functions, preserved by
normalized multiplication, contains a fixed point of that map. 
