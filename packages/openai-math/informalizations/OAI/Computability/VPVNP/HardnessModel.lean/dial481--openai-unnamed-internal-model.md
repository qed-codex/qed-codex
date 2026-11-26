---
{
  "module": "OAI/Computability/VPVNP/HardnessModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessModel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Boolean formulas with scalar and variable labels

Each selected bit contributes a scalar and, optionally, a single formal
variable. The accepted assignments of the formula index a sum of monomials.
Selector bits implement finite scalar linear combinations of these sums.


### `MarkedCNF`

 A Boolean formula whose true variables contribute a scalar and, optionally, a polynomial
variable to the weight of an assignment. 

### `MarkedCNF.width`

 Number of Boolean variables in the marked formula. 

### `MarkedCNF.clauses`

 The clauses selecting the assignments whose weights enter the polynomial. 

### `MarkedCNF.scalar`

 Coefficient factor contributed when a given Boolean variable is true. 

### `MarkedCNF.label`

 Optional polynomial variable contributed when a given Boolean variable is true. 

### `value`

 The formal polynomial specified by the selected scalar and variable labels. 

### `unit`

 The empty CNF with no Boolean variables has a single assignment of weight one. 

### `linearCombination`

 The selector for a summand carries that summand's scalar. All data bits
retain the scalar and optional variable of the corresponding private block. 
