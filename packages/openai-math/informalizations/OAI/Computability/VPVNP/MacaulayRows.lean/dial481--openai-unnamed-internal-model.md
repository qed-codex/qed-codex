---
{
  "module": "OAI/Computability/VPVNP/MacaulayRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The bounded coefficient matrix of the finite slice

Appendix D.1 uses rows given by monomial multiples of the slicing equations.
The bounded Rabinowitsch certificate puts the coefficient vector of the required
power of a vanishing polynomial in this matrix's row space. Conversely, row-space
membership implies vanishing at every geometric zero.


### `BoundedMonomial`

 Multi-indices of total degree at most `D` in the original `t` variables. 

### `BoundedMonomial.encode`

 The exponent of each variable is at most the total degree bound. 

### `card_boundedMonomial_le`

 Each of the `t` exponents admits at most `D + 1` choices. 

### `coefficientRow`

 Coefficient row in the ordered matrix columns through degree `D`. 

### `macaulayMatrix`

 The row indexed by `(i, a)` is the coefficient vector of `X^a Fᵢ`. 

### `macaulayMatrix_apply`

 The coefficient of a monomial multiple is the original coefficient with its
exponent shifted, or zero if one of the exponents is too small. 

### `macaulayMatrix_natAbs_le`

 For integer equations, the same absolute coefficient bound applies to every row. 

### `coefficientRow_one_natAbs_le`

 The row augmenting the certificate matrix has a single nonzero coefficient, one. 

### `coefficientRow_sum_mul_mem`

 Bounded multipliers express the coefficient row of a polynomial combination
in the span of the Macaulay rows, over any commutative semiring. 

### `coefficientRow_pow_mem`

 The row space test resulting from the bounded inconsistency certificate, with the
paper's multiplier bound `H + P * R₀` and column bound `H + P * R₀ + d`. 

### `aeval_eq_zero_of_row_mem`

 A coefficient row in the Macaulay row space vanishes at all common zeros of the
equations, including zeros in arbitrary extension fields. 
