---
{
  "module": "src/Lib/CM/FormalGroup/FormalParameter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/FormalGroup/FormalParameter.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/FormalGroup/FormalParameter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The formal parameter

Let `d ≡ 7` mod `8` be a prime and `C` a lattice with complex multiplication by the integers of
`K = ℚ(√-d)`. Let `p` be a prime, `ιₚ : ℂ →+* ℂ_[p]` a fixed embedding and `𝒪` the valuation ring of
`ℂ_[p]`. Power series are in the variable `z`, which is `X` in the code; so the formal parameter is
written `T`.

* `New.CMLattice.isSeriesGenerator_formalParam`: the part `T` of `y` in degrees `≡ 1` mod `q - 1`
  generates `𝒪[[y]]`.
* `New.CMLattice.exists_scaled_formalParam`: for some `ϖ` of valuation `ρ_p` the series
  `Y = T(ϖ z) / ϖ` is integral, and `Y - Y ^ q ≡ z`, `Y ≡ ∑ z ^ q ^ j` mod `π_p`. The proof writes
  `T(π_p z) = π_p T + b₁ T ^ q + ⋯` with a unit `b₁` and takes `ϖ ^ (q - 1) = -π_p / b₁`.
* `New.CMLattice.rescale_mem_range_seriesToCp`, `New.CMLattice.norm_coeff_le_one_of_lt`: for
  `g ∈ 𝒪[[y]]` the series `g(ϖ z)` is integral, and `g` is integral in the degrees below `q`.

## Notation

* `q = primeNorm d p` is the norm of a prime of `K` above `p`.
* `π_p = piPrime d p` is `√-d` if `p = d` and `p` otherwise; `piPrimeInt d` is its image in `𝒪`.
* `y = taylorVia ιₚ C.translatedY` is the Taylor series at `0` of the coordinate function
  `C.translatedY`, moved to `ℂ_[p]` by the embedding `ιₚ`.
* `𝒪[[y]] = C.integralSeriesRing` is the ring of the series `g(y)` with `g` a series over `𝒪`.
* `ρ_p = varpiValuation d p` is the valuation of `π_p` divided by `q - 1`.

## Relation to the literature

Known result: multiplication by `π_p` on the formal group of a curve with complex multiplication is
an endomorphism in the sense of Lubin and Tate. That `b₁` is a unit follows from the bound for the
height of the formal group (`New.CMLattice.insepDegree_piPrime_le`), and the scaling is an
elementary consequence. Lubin–Tate, Formal complex multiplication in local fields.


### `mem_normPairClosure_of_pow_eq_one`

 If `ζ ^ (q - 1) = 1`, where `q = primeNorm d p`, then the pair `(ζ, ζ ^ (p + 1))` is a limit in
`ℂ_[p] × ℂ_[p]` of pairs `(α, α ᾱ)` with `α` an integer of `ℚ(√-d)`. 

### `not_isUnit_piPrimeInt`

 The number `π_p` (`√-d` if `p = d`, and `p` otherwise) is not a unit of the valuation ring of
`ℂ_[p]`. 

### `norm_eq_rpow_neg_varpiValuation_of_pow_eq`

 If `ϖ ^ (q - 1) = π_p u` with `q = primeNorm d p`, `π_p = piPrimeInt d` and `u` a unit of the
valuation ring of `ℂ_[p]`, then `ϖ` has valuation `ρ_p = varpiValuation d p`. 

### `rescale_translatedY_mem_of_pow_eq_one`

 For a prime `d ≡ 7 (mod 8)` and `q = primeNorm d p` (`p²` if `(p/d) = −1`, else `p`), if
`ζ ^ (q - 1) = 1` then `y(ζ z)` lies in the ring `𝒪[[y]] = C.integralSeriesRing` of integral series
in `y`. Here `y = taylorVia ιₚ C.translatedY` is the `p`-adic Taylor series at `0` of
`C.translatedY`, i.e. of `½(℘′(z + t) − a₁(℘(z + t) − ℘(t)))`. 

### `expSubst_rescale_sub_mem_of_pow_eq_one`

 Let `q = primeNorm d p`, which is `p²` if `(p/d) = -1` and `p` otherwise, and let
`g = C.negLogTheta` be the series `-log θ` with `g(0) = 0`, that is, minus the logarithm of the
Taylor series at `0` of the theta function `C.θ` of the lattice `C`, read in `ℂ_[p]`. If
`ζ ^ (q - 1) = 1`, then `exp (ζ⁻¹ ^ (p + 1) g(ζ X) - g(X))` lies in `C.integralSeriesRing`. That
ring is `𝒪[[y]]`, the integral power series in the `p`-adic Taylor series `y` of `C.translatedY`. 

### `formalParam`

 The formal parameter `T`: the part in degrees `≡ 1` mod `q - 1` of `y`, the `p`-adic Taylor
series of `C.translatedY`, where `q = primeNorm d p`. 

### `isSeriesGenerator_formalParam`

 Let `d` be a prime `≡ 7` mod 8 and `p` a prime with a `p`-adic place `ιₚ`, and set
`q = primeNorm d p` (`p²` if `(p/d) = -1`, otherwise `p`). The formal parameter `T = C.formalParam`
is the part in degrees `≡ 1` mod `q - 1` of `y`, the `p`-adic Taylor series of `C.translatedY`. `T`
generates `C.integralSeriesRing = 𝒪[[y]]`: it has the form `X + ⋯`, and the ring consists exactly of
the series `g(T)` with `g` a power series over the valuation ring `𝒪` of `ℂ_[p]`. 

### `mem_integralSeriesRing_iff_exists_subst_formalParam`

 Let `y` be the `p`-adic Taylor series of `C.translatedY`, let `q = primeNorm d p`, and let
`T = C.formalParam` be the part of `y` in degrees `≡ 1` mod `q - 1`. A series `f` over `ℂ_[p]` lies
in `𝒪[[y]] = C.integralSeriesRing` if and only if `f = g(T)` for some power series `g` with
coefficients in the valuation ring `valRingCp p`. 

### `congruencePart_subst_formalParam`

 Taking the part of a series in degrees `≡ r` mod `q - 1`, where `q = primeNorm d p`, commutes
with the substitution of the formal parameter. 

### `isUnit_coeff_primeNorm_of_rescale_formalParam_eq`

 Let `d` be a prime `≡ 7 mod 8`, `p` a prime with fixed `p`-adic place `ιₚ`, `q = primeNorm d p`
(`p²` if `(p/d) = -1`, else `p`), `π = piPrime d p` (`√-d` if `p = d`, else `p`; `piPrimeInt d` is
`ιₚ π` in the valuation ring of `ℂ_[p]`), and `T = C.formalParam` the part in degrees `≡ 1` mod
`q - 1` of the `p`-adic Taylor series of `C.translatedY`. If `T(π z) = g(T)` with `g = π z + ⋯` an
integral series (`seriesToCp g` as a series over `ℂ_[p]`) supported in degrees `1 + i (q - 1)`, then
the coefficient of `z ^ q` in `g` is a unit. 

### `exists_rescale_piPrime_formalParam_eq`

 Let `d` be a prime `≡ 7 mod 8`, `p` a prime with fixed `p`-adic place `ιₚ`, `q = primeNorm d p`
(`p²` if `(p/d) = -1`, else `p`), `π = piPrime d p` (`√-d` if `p = d`, else `p`; `piPrimeInt d` is
`ιₚ π` in the valuation ring of `ℂ_[p]`), and `T = C.formalParam` the part in degrees `≡ 1` mod
`q - 1` of the `p`-adic Taylor series of `C.translatedY`. Then `T(π z) = g(T)` for an integral
series `g = π z + b₁ z ^ q + ∑_{i ≥ 2} bᵢ z ^ (1 + i (q - 1))` (`seriesToCp g` as a series over
`ℂ_[p]`) with `b₁` a unit. 

### `exists_scaled_formalParam`

 Let `d` be a prime `≡ 7 mod 8`, `p` a prime, and `ιₚ : ℂ → ℂ_p` the fixed `p`-adic place. Let
`q = primeNorm d p` (`p²` if `(p/d) = -1`, else `p`), and let `T = C.formalParam` be the part in
degrees `≡ 1` mod `q - 1` of the `p`-adic Taylor series of `C.translatedY`. There is `ϖ ∈ ℂ_[p]`
with `‖ϖ‖ = p ^ (-ρ_p)`, where `ρ_p = varpiValuation d p` is `1/(p-1)`, `1/(p²-1)`, `1/(2p-2)` for
`p` split, inert, ramified in `ℚ(√-d)`, such that `Y = T(ϖ z) / ϖ` is integral (`seriesToCp Y` is
`Y` as a series over `ℂ_[p]`), and `Y - Y ^ q ≡ z` and `Y ≡ ∑_{j ≥ 0} z ^ q ^ j` modulo
`piPrimeInt d = ιₚ π_p`, where `π_p` is `√-d` if `p = d` and `p` otherwise. 

### `rescale_mem_range_seriesToCp`

 Let `d` be a prime `≡ 7 mod 8` and `p` a prime with fixed `p`-adic place `ιₚ : ℂ → ℂ_p`. Suppose
`g` is an integral power series in `y`, the `p`-adic Taylor series of `C.translatedY` (that is,
`g ∈ C.integralSeriesRing`). Suppose also `‖ϖ‖ ≤ p ^ (-ρ_p)`, with `ρ_p = varpiValuation d p` equal
to `1/(p-1)`, `1/(p²-1)`, `1/(2p-2)` for `p` split, inert, ramified in `ℚ(√-d)`. Then `g(ϖ z)` has
integral coefficients (it lies in the range of `seriesToCp`). 

### `norm_coeff_le_one_of_lt`

 If `g` is an integral series in `y`, the `p`-adic Taylor series of `C.translatedY` (that is,
`g ∈ C.integralSeriesRing`), then its coefficients in degrees below `q = primeNorm d p` are
integral. 
