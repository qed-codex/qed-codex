---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/Additive/Finite.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Additive/Finite.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Additive/Finite.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The compactness obstruction can be restricted to finitely many coordinates,
including the unit. Outside those coordinates, zero is a valid box coordinate.
This is the concrete finite-dimensional input to rational linear elimination. 

### `finite_coordinate_obstruction`

 A finite obstruction includes only these coordinate bounds; no infinite
system is passed silently to the finite rational cone theorem. 
