---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/Additive/Catalyst.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Additive/Catalyst.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Additive/Catalyst.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Catalysts in the additive-state obstruction

All comparisons retain the catalyst. In particular the multiplicative induction
below keeps a single copy of `s`; it neither cancels `s` nor substitutes `s^j`.
The hypotheses are elementary ordered-semiring laws, to be instantiated by the
concrete tensor restriction semiring.


### `StableEquality`

 The stable equality supplied by a cleared finite additive certificate. 

### `catalyst_nonzero`

 Additive flattening rank, not ordinary tensor rank, rules out `s = 0`. 

### `catalyst_additive_iteration`

 Additive iteration retains one fixed `D`, while both gains scale with `n`. 

### `catalyst_absorbed_comparison`

 Absorb the fixed catalyst using its rank bound and `1 ≤ s`. 

### `catalytic_power_iteration`

 Iteration of a catalytic multiplicative comparison does not cancel the tensor. 
