---
{
  "module": "OAI/Computability/VPVNP/SpectralStateHom.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralStateHom.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralStateHom.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Multiplicativity of extreme states on tensor fractions

In Appendix A.1 the reciprocal of `1 + s` splits the normalized unit into
two positive summands. Extremality makes each summand act multiplicatively.
Restricting the resulting state to the original semiring gives a spectral point.


### `state_pos_of_unit_multiplier`

 A unit whose multiplication preserves an order-unit cone has strictly
positive value at every normalized positive state. 

### `extreme_state_mul_of_unit_denominator`

 A tensor unit acts multiplicatively on every extreme state when it and
the reciprocal of its sum with the unit preserve the cone. 

### `extreme_state_mul_tensor`

 Extreme states multiply by every tensor in the localization. 

### `extremeStateHom`

 Restriction of an extreme state to the original tensor semiring. 

### `fractionPositive_of_spectrum_lt`

 Strict comparison at every spectral point places the corresponding
difference inside the order cone of the localization. 
