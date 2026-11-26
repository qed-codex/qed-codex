---
{
  "module": "src/Lib/Analytic/ZeroSymmetry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/ZeroSymmetry.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/ZeroSymmetry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Zeros of L(s, χ) and of L(1 − s, χ⁻¹)

`New.gammaFactor_eq_zero_or_LFunction_one_sub_eq_zero` shows that a zero `s` of L(·, χ) with
`s.re ≠ 0` and `s ≠ 1` is either a pole of `χ.gammaFactor` or gives the zero `1 - s` of L(·, χ⁻¹),
extending the symmetry given by the functional equation from primitive to all Dirichlet characters.

## Relation to the literature

Known result: the symmetry of the zeros, a consequence of the functional equation for Dirichlet
L-functions. Source: Montgomery and Vaughan, Multiplicative Number Theory I, 2007, Corollaries 10.3
and 10.8.


### `New.prod_euler_factor_ne_zero`

 For a Dirichlet character `χ` and `re s ≠ 0`, the product of the inverse Euler factors
`1 - χ(p) p ^ (-s)` over the primes `p` dividing `M` does not vanish. 

### `New.exists_isPrimitive_changeLevel_eq`

 Every complex Dirichlet character χ mod N, with N ≥ 1, is induced by a primitive character ψ
mod M for some divisor M ≥ 1 of N. 

### `New.gammaFactor_changeLevel`

 A character induced by `ψ` has the parity of `ψ`, hence the same gamma factor. 

### `New.gammaFactor_eq_zero_or_LFunction_one_sub_eq_zero`

 Symmetry of the zeros: if L(s, χ) = 0, re s ≠ 0 and s ≠ 1, then either s is a pole of the gamma
factor of χ (where Mathlib gives it the value 0), or L(1 − s, χ⁻¹) = 0. The character need not be
primitive, and multiplicities are not compared.

This is a consequence of the functional equation for the primitive character inducing χ; it keeps
only the reflection s ↦ 1 − s of zeros from χ to χ⁻¹, not the identity itself or the root number. 
