---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpWeightCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpWeightCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpWeightCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable coordinate-label monomial weights

The supplied coordinate list, labels, and exponent array are ordinary input
data. The recursive programs below perform actual scalar multiplications and
return their count. No mathematical finite-set choice is used by the programs.
For a duplicate-free support and a retained exponent, at most 3D+1 scalar
multiplications are performed. This is a scalar-operation bound, not a
Turing-machine bound for evaluating an arbitrary supplied coefficient ring.


### `powerWithCost`

 A linear power loop, counting its one scalar multiplication per step. 

### `weightWithCost`

 Compute one monomial weight by traversing the supplied support list.
Each coordinate incurs its power-loop multiplications and one multiplication
into the product of the remaining coordinates. 

### `inputReads`

 Reading the label and exponent arrays requires two entries per coordinate.
This separate index count does not classify array lookup as scalar arithmetic. 

### `fullWeightWithCost`

 Executable full-coordinate version, used for the unsplit moment weight. 

### `weightWithCost_cost_le_length`

 A direct coordinatewise bound on the recorded scalar operation count. 

### `weightWithCost_cost_le_retained`

 The retained total-degree bound gives a stronger linear operation bound. 

### `momentWeight_eq_computed_partition`

 The computed local weights split the full moment across any supplied
duplicate-free color lists and a duplicate-free complementary list. 

### `rawScalar`

 An ordinary singleton coefficient list at the zero X,U,Z index. 

### `rawWeightWithCost`

 Compute the scalar coefficient and emit its literal for the symbolic backend.
Literal construction adds no scalar multiplications to the power/product loop. 
