---
{
  "module": "OAI/Computability/VPVNP/ShiftedCrossing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShiftedCrossing.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShiftedCrossing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integral factorizations for the two-wire crossing tensor

The wire labels are numbered from zero, and each of the two summands has its
own number of factor coordinates. The four integer arrays can be reduced into
any field without changing either cut.


### `IntegralCrossing`

 Two integral matrix factorizations, one on each of the two cuts of the
product of the two identity wires. 

### `IntegralCrossing.leftPlus`

 The integer factor indexed by the first operator index `i` and output state `α` on the
  forward cut. 

### `IntegralCrossing.rightPlus`

 The integer factor indexed by the second operator index `j` and input state `β` on the
  forward cut. 

### `IntegralCrossing.leftMinus`

 The integer factor indexed by the first operator index `i` and input state `β` on the
  reversed cut. 

### `IntegralCrossing.rightMinus`

 The integer factor indexed by the second operator index `j` and output state `α` on the
  reversed cut. 

### `integralCrossing_of_factors`

 Convert the state and factor indices of an integral crossing to numbered
wires, padding each cut independently to its prescribed bound. 

### `IntegralCrossing.flatteningRanks`

 The same four integer factors give a decomposition of the two identity
wires over every field with the indicated flattening rank bounds. The first
tensor is flattened on `(i,α)|(j,β)` and the second on `(i,β)|(j,α)`. 

### `integral_shifted_crossing`

 Finite, integer form of the shifted crossing in doubled energy units.
The first wire omits the empty state, and the intermediate cutoffs differ by
twice the Laurent coefficient shift. 

### `shiftedCrossing`

 Theorem 3.1 of *VP and VNP differ over every field*. For two prescribed
wire rates and one signed shift, the same integer tensors work over every field.
The limits of the two factor bounds are distinct when the shift is nonzero.
The ordinary flattening ranks follow from `IntegralCrossing.flatteningRanks`. 
