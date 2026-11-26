---
{
  "module": "src/Lib/General/NumberTheory/PadicLimitsValuation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/PadicLimitsValuation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/PadicLimitsValuation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Algebraicity from ℓ-adic bounds, roots of unity as limits, and the ℓ-adic valuation

This file proves three groups of facts. `New.isAlgebraic_of_norm_complexToCp_le` shows that a
complex number that stays ℓ-adically bounded under all isomorphisms ℂ ≅ ℚ̄_ℓ, for one prime ℓ, is
algebraic. The second section approximates the roots of unity ζ in ℂ_p with ζ^{q_p} = ζ by images of
integers of K = ℚ(√−d); the third collects properties of the ℓ-adic valuation and of coefficient
rings.

* `quadInt d` is the ring of integers of K inside ℂ, and a `PadicPlace p` fixes a map ιₚ : ℂ → ℂ_p.
* `primeNorm d p` is the number q_p, equal to p² if the Legendre symbol `chiK d p` = (p/d) is −1 and
  to p otherwise.
* v = `New.ellVal` is the normalised valuation on ℚ̄_ℓ = `PadicAlgCl ℓ`, truncated to 0 on elements
  of norm at least 1, so that its values lie in [0, ∞].
* O denotes a ring in `New.CoeffRing ℓ`: the ring of integers of a finite Galois extension of ℚ_ℓ
  inside ℚ̄_ℓ. `ThePrime ℓ` says that ℓ is prime.

## Main definitions and results

* `New.mem_normPairClosure_of_pow_eq`: an element `ζ` of `ℂ_p` of norm 1 with `ζ ^ q_p = ζ` is a
  limit of images of integers `α` of `K`, in such a way that the image of `α ᾱ` tends to
  `ζ ^ (p + 1)`.
* `New.CoeffRing.normLength`, `New.CoeffRing.normLength_addVal`: the rescaling of lengths of
  O-modules that sends the additive valuation of x to v(x), so that they become comparable for
  different O.
* `New.CoeffRing.eventually_exists_isPrimitiveRoot`: all large O hold a primitive k-th root of
  unity.

## Relation to the literature

Known result: Teichmüller representatives as limits of powers. Source: Serre, Local Fields, Chapter
II.



## An ℓ-adic criterion for algebraicity of complex numbers

A transcendental number can be sent to any transcendental element of `PadicAlgCl ℓ` by
`New.exists_ringEquiv_extend`, and these elements have unbounded norm.


### `New.isAlgebraic_of_norm_complexToCp_le`

 Let `ℓ` be a prime. If the `ℓ`-adic norms of the images of `x : ℂ` under all field isomorphisms
`ι` from `ℂ` onto the algebraic closure of `ℚ_ℓ` have a common bound `c`, then `x` is algebraic over
`ℚ`. The norm is taken in `ℂ_[ℓ]`: `complexToCp ι` is `ι` followed by the isometric embedding into
`ℂ_[ℓ]`. 


## Roots of unity as limits of integers of `K`

Proof idea: lift the residue of `ζ` to an integer `a` of `K` and take the powers `a ^ q_p ^ n`.


### `instance : CharP (ResidueField (valRingCp p)) p`

 The residue field of the valuation ring of `ℂ_[p]` has characteristic `p`, since `‖p‖ < 1`. 

### `tendsto_pow_pow_of_norm_sub_one_lt`

 If `‖u - 1‖ < 1` in `ℂ_p` and `p ∣ q`, then `u ^ q ^ n` tends to `1` as `n → ∞`. 

### `tendsto_pow_pow_of_residue_eq`

 If `x` and `y` in the valuation ring of `ℂ_p` have the same residue, `‖y‖ = 1`, `p ∣ q` and
`y ^ q ^ n = y` for all `n`, then `x ^ q ^ n` tends to `y`. 

### `QuadField.exists_map_eq_and_map_star_eq_pow`

 Let `p` be a prime, `d` a prime congruent to 7 modulo 8, and let `φ` map the integers of
`K = ℚ(√-d)` to a field of characteristic `p`. An element `z` with `z ^ q_p = z`, where
`q_p = primeNorm d p` is `p ^ 2` if the Legendre symbol `chiK d p = (p/d)` is `-1` and `p`
otherwise, is the image of an integer whose conjugate has the image `z ^ p`. 

### `normPairClosure`

 The closure in `ℂ_p²` of the set of images under `ιₚ` of the pairs `(α, α ᾱ)`, with `α` an
integer of `K = ℚ(√-d)`. 

### `mem_normPairClosure_of_pow_eq`

 If `ζ` is an element of `ℂ_p` of norm `1` with `ζ ^ q_p = ζ`, where `q_p = primeNorm d p`
(`p ^ 2` if `chiK d p = -1`, else `p`), then `(ζ, ζ ^ (p + 1))` lies in `normPairClosure d`: it is a
limit of images under `ιₚ` of pairs `(α, α ᾱ)` with `α` an integer of `K = ℚ(√-d)`. 


## The normalised ℓ-adic valuation and normalised lengths

We have v(x) = −log_ℓ |x| for |x| ≤ 1, with v(ℓ) = 1 and v(0) = ∞, and v(x) = 0 for |x| ≥ 1.
By this truncation, v is in general only subadditive on products (`New.ellVal_mul_le`). Each O is an
instance of `New.PadicIntegerRing`; in particular O/x is finite for x ≠ 0.


 ### The valuation on ℚ̄_ℓ 

### `ellVal_le_add_iff`

 For `x`, `y` in ℚ̄_ℓ with `‖y‖ ≤ 1` and a real `c ≥ 0`, the inequality v(x) ≤ c + v(y) means
`ℓ ^ (-c) * ‖y‖ ≤ ‖x‖`, where v = `ellVal` is the normalised valuation. 

### `ellVal_le_iff`

 For `c ≥ 0`, the inequality v(x) ≤ c means `ℓ ^ (-c) ≤ ‖x‖`, where v = `ellVal`. 

### `Selmer.dvd_iff_ellVal_le`

 For `x`, `y` in `intQpBar ℓ`, the valuation ring of ℚ̄_ℓ, `x` divides `y` exactly if
v(x) ≤ v(y), where v = `ellVal` is the normalised valuation. 

### `ellVal_le_ellVal`

 The valuation v = `ellVal` is antitone in the norm: if `‖y‖ ≤ ‖x‖`, then v(x) ≤ v(y). 

### `ellVal_mul_le`

 The normalised valuation v = `ellVal` on ℚ̄_ℓ (v(x) is the positive part of −log_ℓ ‖x‖, and v(0)
= ∞) is subadditive on products: v(xy) ≤ v(x) + v(y). 

### `ellVal_natCast`

 The normalised valuation of a nonzero natural number `n` in ℚ̄_ℓ is its ℓ-adic valuation. 

 ### Coefficient rings: units, lengths, roots of unity and finite quotients 

### `uniformizer`

 A chosen uniformiser of the discrete valuation ring `O`. 

### `normLength`

 Normalised length: the additive map sending n to n·v(ϖ) and ∞ to ∞, where ϖ is the chosen
uniformiser `O.uniformizer` and v(ℓ) = 1. The value does not depend on the choice of ϖ
(`normLength_natCast_of_irreducible`). 

### `normLength_natCast`

 The normalised length of `n` is `-n log_ℓ ‖ϖ‖`, with `ϖ` the chosen uniformiser of `O`. 

### `normLength_addVal`

 Let `O` be a coefficient ring, the ring of integers of a finite Galois extension of ℚ_ℓ inside
ℚ̄_ℓ, with chosen uniformiser ϖ. For x ∈ O, let `addVal O x` be the number of factors of ϖ in x, and
let the normalised length `normLength` send n to n·v(ϖ) (and ∞ to ∞). Then the normalised length of
`addVal O x` equals v(x), where v = `ellVal` equals −log_ℓ|·| on elements of ℚ̄_ℓ of norm ≤ 1,
normalised by v(ℓ) = 1. 

### `normLength_natCast_of_irreducible`

 The normalised length of `n` is `n v(ϖ)` for every uniformiser `ϖ` of `O`, where v = `ellVal`
is the normalised valuation on ℚ̄_ℓ. 

### `eventually_exists_isPrimitiveRoot`

 For `k ≠ 0`, all coefficient rings `O` (rings of integers of finite Galois extensions of ℚ_ℓ
inside ℚ̄_ℓ) that are sufficiently large with respect to inclusion contain a primitive `k`-th root
of unity. 

### `noncomputable instance : PadicIntegerRing O ℓ`

 A coefficient ring is an ℓ-adic integer ring; its quotients by nonzero ideals are finite, as
these ideals are open and the ring is compact. 
