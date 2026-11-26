---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/Elementary.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/Elementary.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/Elementary.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable truncated elementary-symmetric recurrence

The executable routines below traverse finite coefficient lists. They do not
enumerate subsets. The coefficient semiring may be noncommutative, in
particular a matrix semiring or a semiring of linear endomorphisms.

The measured routines execute the same recurrence while recording one
addition and one multiplication per retained coefficient. This is an
arithmetic-operation count, not a claim about a bit-machine implementation.


### `update`

 One coefficient-list pass. The second argument is the preceding old
coefficient; at the beginning of a pass it is zero. 

### `initial`

 The retained coefficients of the constant polynomial one. 

### `coefficients`

 Compute the first R elementary coefficients by successive list passes.
The tail is processed first, fixing an order even without commutativity. 

### `getD_coefficients_cons`

 Exact coefficient recurrence, including the zero-degree boundary. 

### `generatingPolynomial`

 The generating polynomial specifying the ordered elementary coefficients.
Only the specification uses polynomials; the executable routine uses lists. 

### `coefficients_eq_polynomial`

 The executable list agrees with the first R coefficients of the generating
polynomial, for an arbitrary possibly noncommutative coefficient semiring. 

### `measuredUpdate`

 An instrumented execution of a coefficient pass, counting additions and
multiplications in S. 

### `measuredCoefficients`

 An instrumented execution of the entire retained-coefficient algorithm. 

### `measuredCoefficients_operations`

 Exactly two semiring operations are executed for every input operator
and every retained coefficient. 

### `commutingProduct`

 The order-independent product of a commuting family. This is used only
in the specification, never by the executable recurrence. 

### `subsetCoefficient`

 The mathematical elementary-symmetric sum over subsets of size j. 

### `subsetCoefficient_insert_succ`

 Partitioning subsets according to whether they contain the newly
inserted index gives exactly the list-update recurrence. 

### `coefficients_eq_subsetCoefficient`

 For a duplicate-free list of indices, the executable recurrence equals
the genuine elementary-symmetric subset sum. Duplicate operator values are
allowed: only the indices must be distinct. 

### `coefficients_eq_powersetCard`

 The executable recurrence computes the exact ordered-list product
formula used for elementary operator polynomials in the layout. 

### `coefficients_indicator`

 On a zero-one family, the computed elementary coefficient is the
integer binomial coefficient in the number of ones, cast only afterwards. 

### `parity_weighted_indicator`

 The computed coefficients, with the existing exact binomial
interpolation weights, yield corrected eigenvalue one on the entire
integer interval. No restriction on characteristic or R is imposed. 
