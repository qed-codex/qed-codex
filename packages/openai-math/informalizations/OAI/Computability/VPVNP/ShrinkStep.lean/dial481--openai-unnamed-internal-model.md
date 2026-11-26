---
{
  "module": "OAI/Computability/VPVNP/ShrinkStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkStep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact contraction of the shrinking step

For any list of admissible six-party terms, one common layout minimizes
surviving energy. This determines the placement of every old factor and the
regular lift carrying the surviving payloads. Equation (7.1) sums the placed
kernels on these lifts, with one shared value on each new wire.


### `shrinkTermLayout`

 Select one layout for all motifs using their aggregate supply energies. 

### `shrinkStep`

 The complete shrinking kernel, with the actual six-party identities,
padded output arcs, and local contractions of absorbed wire values. 

### `shrinkStep_output`

 The lift and widths passed to the next substep. 

### `shrinkStep_place`

 A selected term moves each complete old position once. 
