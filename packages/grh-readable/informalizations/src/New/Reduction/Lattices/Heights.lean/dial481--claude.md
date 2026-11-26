---
{
  "module": "src/New/Reduction/Lattices/Heights.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Heights.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Heights.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The height of a family over all places: products, monotonicity and the product formula

A height for families of complex numbers indexed by the pairs `ι` of a prime `l` and an isomorphism
`ℂ ≃+* ℚ̄_l` (`New.PrimePadicIso`).

* `New.HeightLe c y`: for some multiplier `H ≠ 0` and some `h l ≥ 0`, the conjugates of `H` are
  bounded by `exp α`, the numbers `H * y ι` are bounded `l`-adically by `l ^ h l`, and
  `α + ∑ h l * log l ≤ c` over every finite set of primes.
* `New.HeightLe.of_mul_le`, `New.HeightLe.of_le`, `New.HeightLe.mono`, `New.HeightLe.mul`,
  `New.HeightLe.prod`, `New.HeightLe.pow`: the calculus of heights.
* `New.HeightLe.nonneg_of_one`: the constant family `1` has height at least `0`, by the product
  formula (`New.log_product_formula`) for the norm of `H`. `New.HeightLe.neg_le_of_norm_map_le` is
  the form for a number `z ≠ 0`.

## Relation to the literature

The multiplier H, and so the bound at infinity, does not depend on ι, while y ι may; so each prime
may use its own twist. Related work: Gaudron, Pentes des fibrés vectoriels adéliques sur un corps
global, 2006; Bombieri–Gubler, Heights in Diophantine Geometry, ch. 1, 2006.


### `PrimePadicIso`

 A prime `l` together with an isomorphism of `ℂ` with the algebraic closure `ℚ̄_l` of `ℚ_l`. 

### `PrimePadicIso.prime`

 The prime `l`. 

### `PrimePadicIso.iso`

 The isomorphism `ℂ ≃+* ℚ̄_l`. 

### `HeightLe`

 The family `y`, with one complex number for each pair `ι` of a prime `l` and an isomorphism
`ℂ ≃+* ℚ̄_l`, has height at most `c`: there are a multiplier `H ≠ 0` and real numbers `h_∞ = α` and
`h_l = h l ≥ 0` with the three properties below. 

### `log_product_formula`

 The product formula for `ℚ`, in logarithms: `log |q| + ∑ log |q|_p = 0` (`log q` is `log |q|`
and `log 0 = 0`), the sum taken over the primes below any bound `M` that exceeds the absolute value
of the numerator of `q` and the denominator of `q`. 

 ### The calculus of heights 

### `mono`

 Let `y`, `y'` be families of complex numbers indexed by the pairs `ι` of a prime `l` and an
isomorphism `ι.iso : ℂ ≃+* ℚ̄_l`. If `y` has height at most `c ≤ c'`, and `y' ι` is `l`-adically no
larger than `y ι` under each `ι.iso`, then `y'` has height at most `c'`. 

### `rpow_mul`

 Let `y` be a family of complex numbers indexed by the pairs `ι` of a prime `l` and an
isomorphism `ι.iso : ℂ ≃+* ℚ̄_l`, of height at most `c ≤ c'`. Multiplying `y ι` by a rational power
`N ι ^ e ι` of a natural number `N ι` prime to `l` gives a family of height at most `c'`. 

### `of_mul_le`

 Let `y` be a family of complex numbers indexed by the pairs `ι` of a prime `l` and an
isomorphism `ι.iso : ℂ ≃+* ℚ̄_l`. Suppose `H ≠ 0` has `|σ H| ≤ exp α` for all automorphisms `σ` of
`ℂ`, `H * y ι` has `l`-adic norm at most `exp (e l)` under each `ι.iso`, and `α + ∑ e l ≤ c` for the
sum over every finite set of primes. Then `y` has height at most `c`. The `e l` may have any
sign. 

### `of_le`

 If reals `e l` have sum at most `c` over every finite set of primes, and `y ι` has `l`-adic norm
at most `exp (e l)` under `ι.iso` for every pair `ι` of a prime `l = ι.prime` and an isomorphism
`ι.iso : ℂ ≃+* ℚ̄_l`, then the family `y` has height at most `c`: some `H ≠ 0`, `α` and `h l ≥ 0`
satisfy `|σ H| ≤ exp α` for all automorphisms `σ` of `ℂ`, `‖ι.iso (H * y ι)‖ ≤ l ^ h l` for all `ι`,
and `α + ∑ h l * log l ≤ c` over finite sets of primes. 

### `inv_const`

 If `H ≠ 0` and `|σ H| ≤ exp c` for all automorphisms `σ` of `ℂ`, then the constant family `H⁻¹`,
indexed by the pairs `ι` of a prime `l` and an isomorphism `ι.iso : ℂ ≃+* ℚ̄_l`, has height at most
`c`: some `H' ≠ 0`, `α` and `h l ≥ 0` satisfy `|σ H'| ≤ exp α` for all `σ`,
`‖ι.iso (H' * H⁻¹)‖ ≤ l ^ h l` for all `ι`, and `α + ∑ h l * log l ≤ c` over finite sets of
primes. 

### `mul`

 Let `y`, `y'` be families of complex numbers indexed by the pairs `ι` of a prime `l` and an
isomorphism `ι.iso : ℂ ≃+* ℚ̄_l`, of height at most `c` and `c'`; then the pointwise product
`y * y'` has height at most `c + c'`. 

### `prod`

 Heights add in finite products: if each `y i`, a family indexed by the pairs `ι` of a prime `l`
and an isomorphism `ι.iso : ℂ ≃+* ℚ̄_l`, has height at most `c i`, then the pointwise product of the
`y i` has height at most the sum of the `c i`. 

### `pow`

 Let `y` be a family of complex numbers indexed by the pairs `ι` of a prime `l` and an
isomorphism `ι.iso : ℂ ≃+* ℚ̄_l`, of height at most `c`; then its pointwise power `y ^ n` has height
at most `n * c`. 

### `norm_algebraMap_norm_gen_le`

 Let `H` be an algebraic number of degree `n` and `F` an algebraically closed normed field of
characteristic zero with the cardinality of `ℂ`. If `‖ι H‖ ≤ exp b` for all isomorphisms
`ι : ℂ ≃+* F`, then the norm of `H` from `ℚ(H)` to `ℚ` has size at most `exp (n * b)` in `F`. 

### `nonneg_of_one`

 If the constant family `1` has height at most `c`, then `0 ≤ c`. This is a form of the product
formula. 

### `neg_le_of_norm_map_le`

 A consequence of the product formula: if `z ≠ 0`, the constant family `z` has height at most
`c`, and `|σ z| ≤ exp c'` for all automorphisms `σ` of `ℂ`, then `-c ≤ c'`. 
