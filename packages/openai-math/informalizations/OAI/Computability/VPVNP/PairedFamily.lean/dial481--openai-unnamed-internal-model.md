---
{
  "module": "OAI/Computability/VPVNP/PairedFamily.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairedFamily.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairedFamily.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Paired variables for the universal counting polynomial

In equation (1.1) of *VP and VNP differ over every field*, the monomial for a word
`x` takes precisely one variable from each pair, with the second index recording its bit.
The coefficient and degree calculations hold for every coefficient function over a
commutative semiring.


### `pairedExponent`

 The exponent vector for the word `x` in the paired variables. 

### `pairedPolynomial`

 The polynomial in (1.1), with `u` providing its coefficients. 

### `coeff_pairedPolynomial`

 The coefficient of the monomial indexed by `x` recovers the value at `x`. 

### `pairedPolynomial_multilinear`

 Each individual variable has degree at most one, including in positive characteristic. 

### `P`

 Equation (1.1) over the integers, using the clocked table encoding from §1.1. 

### `map_P`

 Interpretation of the integer polynomial in a commutative ring. 

### `map_P_eq_sum_witnesses`

 Expansion over input words and their canonical machine-choice strings. The verifier
in this identity is the deterministic Boolean function `verifiesInput`. 

### `totalDegree_map_P`

 The formal total degree remains exactly `n` after base change, including in positive
characteristic. For positive lengths, the all-zero input has exactly one accepting path. 
