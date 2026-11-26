---
{
  "module": "OAI/Algorithms/SubexponentialSAT/PolynomialAlgorithm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/PolynomialAlgorithm.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/PolynomialAlgorithm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable dense univariate polynomial arithmetic

Lists store coefficients from constant term upwards. Trailing zeroes are allowed.
The instrumented algorithms return their value and the number of coefficient-ring
additions and multiplications they actually perform. List manipulation and primitive
bit costs are separate. Recursive results are bound once and reused.


### `addWithCost`

 Dense addition; unmatched tails are returned without scalar arithmetic. 

### `scaleWithCost`

 One scalar multiplication for every stored coefficient. 

### `mulWithCost`

 Schoolbook multiplication, with each partial product computed only once. 

### `sumWithCost`

 Sum a list of dense polynomials, computing each tail sum once. 

### `productWithCost`

 Multiply a list of dense polynomials, computing each tail product once. 

### `evalWithCost`

 Horner evaluation uses one multiplication and one addition per coefficient. 

### `shiftWithCost`

 Polynomial Horner substitution at X+a. Each previous accumulator is
computed once, then multiplied by the stored linear polynomial [a, 1]. 

### `truncate`

 Truncation is just a prefix of the coefficient list. 

### `truncateWithCost`

 Taking a prefix performs no coefficient-ring operations. 

### `coeff`

 Coefficient lookup, with zero beyond the stored list. 

### `denote`

 Mathematical meaning of a coefficient list; only this interpretation is
noncomputable. The list algorithms above use no classical choice. 

### `neg`

 Negation through the already instrumented scalar multiplication loop. 
