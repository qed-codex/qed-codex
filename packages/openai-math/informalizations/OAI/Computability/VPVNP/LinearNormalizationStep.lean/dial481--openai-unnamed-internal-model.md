---
{
  "module": "OAI/Computability/VPVNP/LinearNormalizationStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LinearNormalizationStep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LinearNormalizationStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A linear shear eliminating one generator

Given a relation on generators `g₀,…,gₙ`, choose a direction where the
highest homogeneous component of the relation is nonzero. Its restriction to
a line through the sheared generators gives an integral equation. Each original
generator is then integral over the algebra of the `n` sheared generators.


### `exists_integral_shear`

 A nontrivial polynomial relation permits removing one generator by a linear
change of coordinates, with an integral extension of the resulting algebra. 
