---
{
  "module": "src/Lib/CM/FormalGroup/InseparableDegree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/FormalGroup/InseparableDegree.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/FormalGroup/InseparableDegree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The inseparable degree

For `α ∈ 𝒪_K` let `o(α)` be the order in `y` of `y(α z) ∈ 𝒪[[y]]` modulo the maximal ideal of `𝒪`.

* `New.CMLattice.insepDegree_le`: `o(α) ≤ α ᾱ` for `α ≠ 0`, since `x(α z)` is, up to a unit, an
  integral polynomial in `x` with a unit coefficient in a degree at most `α ᾱ`.
* `New.CMLattice.insepDegree_piPrime_le`: `o(π_p) ≤ q_p` for every prime `p`.

## Notation

* `C : CMLattice d` is a lattice `Λ` stable under `𝒪_K = quadInt d`, the ring of integers of
  `K = ℚ(√-d)` in `ℂ`, with a point `t = C.t` of order two modulo `Λ`.
* `ιₚ : ℂ →+* ℂ_[p]` is the chosen place, `𝒪 = valRingCp p` is the valuation ring of `ℂ_[p]`, and
  `seriesToCp` is the inclusion `𝒪[[X]] → ℂ_[p][[X]]`.
* `taylorVia ιₚ f` is the Taylor series of `f` at `0` with `ιₚ` applied to its coefficients.
* `x` and `y` are the series of `C.translatedX` and `C.translatedY`, the coordinates of the curve
  `y ^ 2 + a₁ x y = x ^ 3 + x` at `z + t`, and `C.integralSeriesRing` is the ring `𝒪[[y]]`; `σ` is
  the sigma function of `Λ` and `θ = C.θ` its normalised twisted translate by `t`, with `θ(0) = 1`
  and `σ ^ 2 = x θ ^ 2`.

## Relation to the literature

Known result: the inseparable degree of the reduction of an isogeny is at most its degree. This
gives the bound on the height of the formal group in Deuring's criterion. Sources: Deuring, Die
Typen der Multiplikatorenringe elliptischer Funktionenkörper; Blake, A Deuring criterion for abelian
varieties, arXiv 1311.5454, Theorem 1.1; Bluher, Formal groups, elliptic curves, and some theorems
of Couveignes, ANTS-III, LNCS 1423 (1998), 3.2 and 6.1 (numbering of arXiv math/9708215).


### `order_subst`

 Over a field, the order of `f(g)` is the product of the orders of `f` and `g`, for a power
series `g` without constant term. 

### `reducedOrder`

 The order in `y` of a series `f ∈ 𝒪[[y]]` modulo the maximal ideal of `𝒪`: write `f = g(y)` with
`g ∈ 𝒪[[X]]` and take the order of the reduction of `g`. Here `y` is the Taylor series of
`C.translatedY`. The value for `f` outside `𝒪[[y]]` has no meaning. 

### `exists_eq_subst_of_mem_integralSeriesRing`

 Every element of `C.integralSeriesRing = 𝒪[[y]]` is `g(y)` for an integral series `g`. 

### `reducedOrder_subst_translatedY`

 For an integral series `g ∈ 𝒪[[X]]`, viewed in `ℂ_[p][[X]]` by `seriesToCp`, the reduced order
of `g(y)` is the order of the reduction of `g` modulo the maximal ideal of `𝒪`, where `y` is the
Taylor series of `C.translatedY`. 

### `reducedOrder_mul`

 The reduced order (the order in `y` modulo the maximal ideal) is additive on products in
`C.integralSeriesRing = 𝒪[[y]]`. 

### `reducedOrder_subst`

 Let `T ∈ C.integralSeriesRing = 𝒪[[y]]` have no constant term and let `g` be an integral series.
The reduced order of `g(T)` (its order in `y` modulo the maximal ideal) is the order of the
reduction of `g` times the reduced order of `T`. 

### `reducedOrder_eq_zero`

 A series in `C.integralSeriesRing = 𝒪[[y]]` whose constant coefficient has norm one has the
reduced order (the order in `y` modulo the maximal ideal) zero. 

### `reducedOrder_eq_one`

 A series in `C.integralSeriesRing = 𝒪[[y]]` without constant term whose linear coefficient has
norm one has the reduced order (the order in `y` modulo the maximal ideal) one. 

### `reducedOrder_translatedX`

 The Taylor series `x = y ^ 2 + ⋯` of `C.translatedX` has the reduced order (the order in `y`
modulo the maximal ideal) two. 

### `insepDegree`

 The number `o(α)`: the order in `y` of `y(α z)` modulo the maximal ideal of `𝒪`, where `y` is
the Taylor series of `C.translatedY`. 

### `rescale_translatedY_mem_of_mem_quadInt`

 For `α` in the ring of integers `quadInt d` of `ℚ(√-d)`, the series `y(α z)` lies in
`C.integralSeriesRing = 𝒪[[y]]`, where `y` is the Taylor series of `C.translatedY`. 

### `reducedOrder_rescale`

 For `α` in the ring of integers `quadInt d` and `f ∈ C.integralSeriesRing = 𝒪[[y]]`, the reduced
order of `f(α z)` is the reduced order of `f` times `o(α) = C.insepDegree α`. 

### `insepDegree_mul`

 The inseparable degree is multiplicative on the ring of integers `quadInt d`. 

### `insepDegree_eq_one`

 An element `α` of the ring of integers `quadInt d` that is a unit at the place `ιₚ` has the
inseparable degree one. 

### `norm_torsionValue_sigma_sq_t`

 The torsion value (the value at `0` of the twisted translate) of the square of the sigma
function `σ`, in degree two (the degree of `σ ^ 2` as a section: `σ ^ 2 ∈ C.sections 2`), at the
point `t` of order two is a unit at the place `ιₚ`. Indeed the torsion value at `t` of `θ`, the
normalised twisted translate of `σ` by `t`, vanishes. 

### `isTorsion_t_div`

 If `α ≠ 0` lies in the ring of integers `quadInt d` and has the norm `ν`, then `t / α` is a
torsion point: `2 ν · (t / α) = ᾱ · 2 t` lies in the lattice. 

### `exists_rescale_sigma_sq_eq`

 Let `α ≠ 0` lie in the ring of integers `quadInt d` and have the norm `ν`. As Taylor series over
`ℂ_[p]`, `σ(α z) ^ 2 = θ ^ (2 ν) R(x)` with `x` the series of `C.translatedX`, for a polynomial `R`
whose coefficients are integral at the place `ιₚ` and which has a unit coefficient in a degree at
most `ν`. Here `σ` is the sigma function of the lattice and `θ` is its normalised twisted translate
by the point `t` of order two. 

### `taylorVia_sigma_sq`

 The Taylor series of `σ ^ 2` is `x θ ^ 2`. Here `σ` is the sigma function of the lattice, `θ`
is its normalised twisted translate by `t`, and `x` is the series of `C.translatedX`. 

### `exists_rescale_theta_eq_pow_mul_of_mem_quadInt`

 Let `α` in the ring of integers `quadInt d` have the norm `ν`. As Taylor series over `ℂ_[p]`,
`θ(α z) = θ ^ ν v` for a series `v ∈ C.integralSeriesRing = 𝒪[[y]]` with the constant coefficient
`1`. Here `θ` is the normalised twisted translate of `σ` by `t`. 

### `reducedOrder_aeval_translatedX_le`

 Let `R` be a complex polynomial whose coefficients are integral at the place `ιₚ` and whose
coefficient of degree `i` is a unit there. Then `R(x)` has the reduced order (the order in `y`
modulo the maximal ideal) at most `2 i`, where `x` is the series of `C.translatedX`. 

### `insepDegree_le`

 **Inseparable degree.** Let `d` be a prime ≡ 7 mod 8 and fix a `p`-adic place of ℂ. Let
`C : CMLattice d` be a CM lattice: a lattice stable under the integers of ℚ(√-d), with a point `t`
of order two scaled so that `℘''(t) = 2` and a square root of `12 ℘(t)`, and with neither `ω t` nor
`ω̄ t` in the lattice, where `ω = (1 + √-d) / 2`. If `α ≠ 0` lies in the ring of integers
`quadInt d` of `ℚ(√-d)` and `α ᾱ = ν`, then `C.insepDegree α` is at most `ν`; this is the order in
`y` of `y(α z)` modulo the maximal ideal of `𝒪` at the chosen place, where `y` is the Taylor series
of `C.translatedY`. 

### `insepDegree_piPrime_le`

 **Inseparable degree of `π_p`.** For every prime `p` the inseparable degree of `π_p` (the order
in `y` of `y(π_p z)` modulo the maximal ideal) is at most `q_p`. Here `π_p = piPrime d p` is `√-d`
for `p = d` and `p` otherwise, and `q_p = primeNorm d p` is the norm of a prime of `ℚ(√-d)` above
`p`. A case of Deuring's criterion: the formal group of the reduction has height at most one at
split primes and at most two at the others. 
