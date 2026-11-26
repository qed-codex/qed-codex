---
{
  "module": "OAI/Computability/VPVNP/BalancedPowerObstruction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BalancedPowerObstruction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BalancedPowerObstruction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tensor powers and the balanced-cut obstruction

The tensor value of an `h`-fold power is the `h`th power of its initial value.
For a polynomial-size circuit, each balanced layout contributes at most a fixed
constant times its own exponential. If every layout has smaller growth than the
initial tensor, no circuit within the given size bound can compute the coefficients
at any sufficiently large power. This is the comparison at the end of Theorem 4.2.


### `placed_array_power_value`

 A placed tensor power has the spectral value of the original coefficient array
raised to the power `h`, with the local digit order explicit. 

### `spectral_power_bound`

 Finite spectral upper bound on one concrete power. The multiplicative budget
factor `K` remains explicit, so it can also be chosen polynomially in `h`. 

### `eventually_no_balanced_power_circuit`

 If every balanced two-center layout costs less than the tensor's spectral value,
all sufficiently large powers violate the indicated gate budget. Only the selected
formal coefficients of the circuit are prescribed. 
