---
{
  "module": "OAI/Algorithms/SubexponentialSAT/QuarticSearch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/QuarticSearch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/QuarticSearch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable search for an irreducible quartic

The execution data are four field coefficients. Polynomial expressions occur
only in the correctness proof. Linear and quadratic trial division is performed
by fixed-size synthetic-division formulas.


### `vectors`

 Exhaustive explicit list of coefficient vectors. 

### `poly`

 Mathematical interpretation; the search does not execute polynomial operations. 

### `map_poly`

 Polynomial interpretation commutes with a coefficient homomorphism. 

### `coeff_poly`

 The input vector is exactly the low-degree coefficient vector. 

### `linearQuotient`

 Quotient coefficients on division by `X+a`. 

### `quadraticQuotient`

 Quotient coefficients on division by `X^2+a₁X+a₀`. 

### `irreducible_iff_remainders`

 A monic quartic is irreducible exactly when these finite-size trial divisions fail. 

### `elements`

 The explicit residue representatives, in increasing order. 

### `linearPass`

 Single linear-divisor test, implemented by field operations and equality. 

### `quadraticPass`

 Single quadratic-divisor test. 

### `passes`

 Test all monic linear and quadratic divisors using only field arithmetic. 

### `checkAll`

 Boolean list conjunction, counting the tests actually performed. 

### `evaluate`

 Evaluate both divisor lists and count the tests actually performed. 

### `scan`

 Ordered exhaustive search, counting both candidates and inner tests. 

### `search`

 Search result: coefficient vector, candidate count, divisor-test count. 

### `coefficients`

 Total executable coefficient selection. Prime moduli are proved below to succeed. 

### `liftedCoefficients`

 Executable coefficientwise lift into the prime-power base ring. 
