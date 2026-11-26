---
{
  "module": "OAI/Computability/VPVNP/ShiftedReadout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShiftedReadout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShiftedReadout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Coefficient extraction for opposite-order products of energy-graded matrices.
The grades can be doubled fermionic energies, which are integers for all states. 

### `energyMode`

 Retain the entries of an operator that change the energy by exactly `q`. 

### `energyField`

 Record the energy change of an operator entry as a Laurent monomial. 

### `forward_coeff_any_energy`

 Read an arbitrary coefficient of the forward product, including its binomial multiplier. 

### `forward_coeff`

 Coefficient between states of the same energy. 

### `reverse_coeff_any_energy`

 Read the same Laurent coefficient with the two operators in reverse order. 

### `reverse_coeff`

 Coefficient between states of the same energy. 

### `modes_off_energy`

 The product of two modes vanishes outside its total energy shift. 

### `opposite_modes_off_energy`

 Opposite energy changes give zero on matrix entries of different energies. 

### `bivariate_supercommutator_readout`

 Bivariate coefficient readout between states whose energy difference agrees
with the total degree of the selected monomial. The two exponents of the fields
are `p-d+a` and `q-a` before multiplication by the binomial. 

### `shifted_supercommutator_readout`

 With doubled energies and the paper's coefficient index `s`, the first order
raises the intermediate energy by `2 * s+hB-2*a` and the second order lowers it
by the same amount. Here `ε` is the sign in the supercommutator. 
