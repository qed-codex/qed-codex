---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/TotalOrderBasic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/TotalOrderBasic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/TotalOrderBasic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Shared total-order truncation of nilpotent expansions

The outer variable is a formal marker U. `output` evaluates the canonical
representative after truncation at U = 1. This is an additive operation on
polynomials, not a homomorphism out of the quotient by U^t.


### `row`

 A finite expansion whose s-th coefficient carries s powers of h. 

### `fullProduct`

 The full product is a semantic object; the executable version uses arrays. 

### `retainedProduct`

 The unique chosen representative has U-degree strictly below t. 

### `output`

 Evaluation applies to the chosen polynomial representative only. 

### `sumRetainedAddHom`

 A linear coefficient sum; no multiplicativity is asserted. 

### `powerDivisible_row`

 Each row has the divisibility invariant needed to kill discarded terms. 

### `trunc_eq_self_of_powerDivisible`

 An arbitrary power-divisible polynomial loses no terms after the generator
becomes nilpotent. This is an equality of canonical representatives. 

### `retainedProduct_eq_fullProduct`

 After substitution into a nilpotent setting, EVERY discarded coefficient
vanishes; therefore truncating the shared total order is exact. 

### `output_eq_prod`

 The exact shared truncation equals the product of local exact values. 

### `map_output_eq_prod`

 Apply after evaluating symbolic coefficients at an actual input. 
