---
{
  "module": "OAI/Computability/VPVNP/SpectralStates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralStates.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralStates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Extreme positive states in spectral comparison

In Appendix A.1 the localization has an order unit. Its rational-linear
positive functionals normalized at the unit form a compact subset of the
space of real-valued functions, with the topology of pointwise convergence.
An extreme such functional is multiplicative on the tensor generators.


### `states`

 Real-valued rational-linear functionals normalized to one at the unit and nonnegative on
the specified cone. 

### `stateLinearMap`

 The rational-linear map underlying a normalized positive state on the cone. 

### `exists_extreme_state_le`

 A minimizing face contains a state extreme in the original set. 

### `extreme_state_mul_of_split`

 Splitting the unit into two positive multipliers makes both reweighted
states coincide with an extreme state. This is the multiplicativity step of A.1. 

### `extreme_state_mul_generator`

 If `v*s=u`, the split proves multiplicativity on the original element `s`. 
