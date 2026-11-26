---
{
  "module": "OAI/Computability/VPVNP/ExactOneWeights.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExactOneWeights.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExactOneWeights.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Weighted exact-one reduction

The original variables retain their weights. Every selector and filler has
weight one, so the unique extension of an assignment preserves its contribution
over any commutative semiring.


### `weightedExactOne`

 Weighted generating function of assignments meeting each clause exactly once. 

### `extendLabels`

 A selector or filler receives the supplied neutral label. 

### `augmentWeight`

 Extend the weights to all Boolean variables of the exact-one instance. 

### `augmentProjection`

 The extension also preserves variable-or-constant projection labels. 

### `weightedExactOne_augment`

 The exact-one reduction preserves the entire generating polynomial. 
