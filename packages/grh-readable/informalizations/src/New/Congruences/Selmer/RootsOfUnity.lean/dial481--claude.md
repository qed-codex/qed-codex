---
{
  "module": "src/New/Congruences/Selmer/RootsOfUnity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/RootsOfUnity.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/RootsOfUnity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Roots of unity `ζ` with polynomials hardly more divisible at `ζ - 1` than at given points

For `ρ > 0`, `ε > 0`, finitely many integral polynomials `P_i` in at most `s₀` variables and points
`x_i` whose coordinates have valuation at least `ρ`, with a bound on `∑ v(P_i(x_i))`, we find roots
of unity `ζ_j` of `ℓ`-power order with `v(ζ_j - 1) ≤ ρ` such that `v(P_i((ζ_j - 1)_j))` exceeds
`v(P_i(x_i))` by at most `ε`. The orders of the `ζ_j` are bounded before the polynomials are given.

* `New.Selmer.exists_rootOfUnity_eval_le_gaussVal_add`: the step in one variable, by counting roots.
* `New.Selmer.exists_rootsOfUnity_ellVal_eval_le_add`: several variables, by moving one coordinate
  of all points at a time.

Notions from other files:
* `New.ThePrime ℓ`: the class saying that `ℓ` is prime and is the prime in scope.
* `New.ellVal`: the valuation `v(x) = max (-log_ℓ |x|) 0` on `ℚ̄_ℓ`, with `v ℓ = 1` and `v 0 = ∞`;
  `New.intQpBar ℓ` is the ring `ℤ̄_ℓ` of integral elements.
* `New.Selmer.gaussVal`: the Gauss valuation `v_ρ(g) = min_i (v(y_i) + ρ i)` of `g = ∑ y_i Y ^ i`.

## Relation to the literature

Finitely many integral polynomials of any degree that are little divisible at given points of
positive valuation remain so at a single tuple of `ζ - 1`, with `ζ` roots of unity of `ℓ`-power
order. A degree-free bound at some `ℓ`-power root of unity for one element is known in the
literature. Related work: Kriz–Nordentoft, Horizontal p-adic L-functions, 2023; Serban, An
infinitesimal p-adic multiplicative Manin–Mumford conjecture, 2018; Kurihara, The structure of
Selmer groups of elliptic curves and modular symbols, 2014.


 ### The radii `ρ_h` and the harmonic sum 

### `rootRadius`

 The number `ρ_h = 1 / φ(ℓ ^ h)`, where `φ` is Euler's totient. For `h ≥ 1` it is the valuation
`v(ζ - 1)`, normalised by `v ℓ = 1`, for `ζ` of order `ℓ ^ h`. 

### `ellVal_sub_one_eq_rootRadius`

 For `h ≥ 1` and a primitive `ℓ ^ h`-th root of unity `ζ` in `ℤ̄_ℓ = intQpBar ℓ`, the valuation
`v(ζ - 1)`, where `v = ellVal` is normalised by `v ℓ = 1`, is the radius `ρ_h = 1 / φ(ℓ ^ h)`. 

### `rootRadius_injOn`

 The radii `rootRadius ℓ h` with `h ≥ 1` are distinct. 

### `eventually_rootRadius_le`

 For `ρ > 0`, all large `h` have `rootRadius ℓ h = 1 / φ(ℓ ^ h) ≤ ρ`. 

### `radiusExponents`

 The exponents `h` with `1 ≤ h ≤ h₀` and `ρ_h ≤ ρ`, where `ρ_h = rootRadius ℓ h`. 

### `exists_lt_mul_sum_radiusExponents`

 Let `ρ > 0` and `δ > 0`. As the harmonic series diverges, there is an `h₀` such that `δ` times
the sum of `1 / (h + 1)` over `radiusExponents ℓ ρ h₀` (the `h` with `1 ≤ h ≤ h₀` and
`rootRadius ℓ h = 1 / φ(ℓ ^ h) ≤ ρ`) exceeds `B`. 

 ### One variable 

### `rootsOfValuation`

 The multiset of roots of `g` in `ℤ̄_ℓ = intQpBar ℓ` of valuation `r`, counted with multiplicity,
where the valuation `ellVal` is normalised by `v ℓ = 1`. For `r = ρ_h` it is written `R_h` in the
docstrings. 

### `ellVal_of_mem_rootsOfValuation`

 A member of `rootsOfValuation g r`, the roots of `g` in `ℤ̄_ℓ` of valuation `r`, has valuation
`r`. 

### `card_rootsOfValuation_mul`

 For the valuation `v = ellVal` on `ℚ̄_ℓ`, normalised by `v ℓ = 1`, the number of roots of `g` in
`ℤ̄_ℓ = intQpBar ℓ` with `v(α) = r`, counted with multiplicity, times `c` is the sum, over all roots
`α` in `ℤ̄_ℓ` with multiplicity, of `c` if `v(α) = r` and `0` otherwise. 

### `ellVal_eval_add_card_mul`

 Let `v = ellVal` be the valuation on `ℚ̄_ℓ` with `v ℓ = 1`, let `g = ∑ y_i Y ^ i` be a
polynomial over the valuation ring `ℤ̄_ℓ = intQpBar ℓ`, and let `v_r(g) = gaussVal r g` be its Gauss
valuation `min_i (v(y_i) + r i)`. At a point `y` of valuation `r` only the roots `α` of `g` in
`ℤ̄_ℓ` of valuation `r` matter: `v(g(y)) - v_r(g) = ∑ (v(y - α) - r)` over the multiset
`rootsOfValuation g r` of these roots, counted with multiplicity, stated here without
subtraction. 

### `sum_rootRadius_filter_le_min`

 Let `α` be in the valuation ring `ℤ̄_ℓ = intQpBar ℓ` of `ℚ̄_ℓ` and `v = ellVal` the valuation
with `v ℓ = 1`. At most one radius `ρ_h = rootRadius ℓ h = 1 / φ(ℓ ^ h)` with `h` in
`radiusExponents ℓ ρ h₀` equals `v(α)`, so the sum of these radii is at most `min (v(α)) ρ`. 

### `sum_card_rootsOfValuation_mul_le`

 Let `v = ellVal` be the valuation on `ℚ̄_ℓ` with `v ℓ = 1`, and let `g = ∑ y_i Y ^ i` be a
polynomial over `ℤ̄_ℓ = intQpBar ℓ`. Let `ρ_h = rootRadius ℓ h = 1 / φ(ℓ ^ h)`, and let
`R_h = rootsOfValuation g ρ_h` be the multiset of roots of `g` in `ℤ̄_ℓ` of valuation `ρ_h`, counted
with multiplicity. The sum of `#R_h ρ_h` over `radiusExponents ℓ ρ h₀` is at most the Gauss
valuation `gaussVal ρ g = min_i (v(y_i) + ρ i)`. 

### `exists_card_rootsOfValuation_mul_le`

 Let `v = ellVal` be the valuation on `ℚ̄_ℓ` with `v ℓ = 1`, and let `g = ∑ y_i Y ^ i` be a
polynomial over `ℤ̄_ℓ = intQpBar ℓ`. Let `ρ_h = rootRadius ℓ h = 1 / φ(ℓ ^ h)`, and let
`R_h = rootsOfValuation g ρ_h` be the multiset of roots of `g` in `ℤ̄_ℓ` of valuation `ρ_h`, counted
with multiplicity. Suppose that the Gauss valuation `gaussVal ρ g = min_i (v(y_i) + ρ i)` is at most
`B`. Suppose also that `B` is less than `δ` times the sum of `1 / (h + 1)` over
`radiusExponents ℓ ρ h₀`. Then one of these `h` has `#R_h ρ_h ≤ δ / (h + 1)`. 

### `sum_min_ellVal_sub_le`

 An integral `α` is close to few `ζ - 1`: if `1 + α` is a unit of `ℤ̄_ℓ`, then the sum of
`min (v(ζ - 1 - α)) 1` over the primitive `ℓ ^ h`-th roots of unity `ζ` is at most `h + 1`, where
`v = ellVal` is the valuation with `v ℓ = 1`. 

### `exists_isPrimitiveRoot_pow`

 The valuation ring `ℤ̄_ℓ = intQpBar ℓ` of `ℚ̄_ℓ` contains a primitive `ℓ ^ h`-th root of
unity. 

### `exists_sum_min_ellVal_sub_le`

 Averaging over the roots of unity of order `ℓ ^ h`. Let `v = ellVal` be the valuation on `ℚ̄_ℓ`
with `v ℓ = 1` and `ρ_h = rootRadius ℓ h = 1 / φ(ℓ ^ h)`, so that there are `1 / ρ_h` such roots in
`ℤ̄_ℓ = intQpBar ℓ`. Let `R` be a multiset in `ℤ̄_ℓ` with `1 + α` a unit for all `α ∈ R`. Then for
one such root of unity `ζ` the numbers `min (v(ζ - 1 - α)) 1`, `α ∈ R`, add up to at most
`#R ρ_h (h + 1)`. 

### `isUnit_one_add_of_ellVal_pos`

 An element `1 + α` of `ℤ̄_ℓ = intQpBar ℓ` is a unit if the valuation `ellVal` of `α` is
positive. 

### `exists_rootOfUnity_eval_le_gaussVal_add`

 Write `v = ellVal` for the valuation on `ℚ̄_ℓ` with `v ℓ = 1`, and
`v_r(g) = gaussVal r g = min_i (v(y_i) + r i)` for the Gauss valuation of a polynomial
`g = ∑ y_i Y ^ i` over the ring `ℤ̄_ℓ = intQpBar ℓ` of integral elements. Let `δ < 1`, and let `δ`
times the sum of `1 / (h + 1)` over the exponents `1 ≤ h ≤ h₀` with `ρ_h ≤ ρ` exceed `B`, where
`ρ_h = rootRadius ℓ h = 1 / φ(ℓ ^ h)`. If `v_ρ(g) ≤ B`, then for one of these exponents `h` and some
`ζ` of order `ℓ ^ h` we have `v(g(ζ - 1)) ≤ v_{ρ_h}(g) + δ`. 

 ### Several variables 

### `le_add_of_sum_le_sum_add`

 If `b i ≤ a i` for all `i`, the sum `∑ b i` is finite and `∑ a i ≤ ∑ b i + c`, then
`a i ≤ b i + c` for each `i`. 

### `freeCoordinate`

 For a point `x` with coordinates in `ℤ̄_ℓ = intQpBar ℓ` and a coordinate index `j`, the
polynomial `P` at `x` with one variable `Y` in place of `x j`. 

### `eval_freeCoordinate`

 The value of `freeCoordinate x j P` at `y` is the value of `P` at the point `x` with its
coordinate `x j` replaced by `y`. 

### `exists_ellVal_eval_update_le_add`

 Moving one coordinate `j`. Let `δ < 1`, and let `δ` times the sum of `1 / (h + 1)` over the
exponents `1 ≤ h ≤ h₀` with `1 / φ(ℓ ^ h) ≤ ρ` exceed `B`. Let `P i` be polynomials and `x i` points
over the valuation ring `ℤ̄_ℓ = intQpBar ℓ` of `ℚ̄_ℓ` with `v(x i j) ≥ ρ` and
`∑ i, v(P i (x i)) ≤ B`. Then all `x i j` can be replaced by one number `ζ - 1`, with
`ζ ^ ℓ ^ h₀ = 1` and `v(ζ - 1) ≤ ρ`, so that each `v(P i (x i))`, and also their sum, grows by at
most `δ`. 

### `exists_ellVal_eval_piecewise_le_add`

 Moving the coordinates in a finite set `t` in turn. Let `δ < 1` and `#σ δ ≤ 1`, and let `δ`
times the sum of `1 / (h + 1)` over the exponents `1 ≤ h ≤ h₀` with `1 / φ(ℓ ^ h) ≤ ρ` exceed
`β + 1`. Let `P i` be polynomials and `x i` points over the valuation ring `ℤ̄_ℓ = intQpBar ℓ` of
`ℚ̄_ℓ` with `v(x i j) ≥ ρ` for all `j` and `∑ i, v(P i (x i)) ≤ β`. Then the coordinates `x i j`
with `j ∈ t` can be replaced by numbers `ζ j - 1`, the same for all `i`, with `ζ j ^ ℓ ^ h₀ = 1` and
`v(ζ j - 1) ≤ ρ`, so that each `v(P i (x i))` grows by at most `#t δ` and their sum stays at most
`β + #t δ`. 

### `exists_rootsOfUnity_ellVal_eval_le_add`

 Let a natural number `s₀`, a rational `ρ > 0`, `β ≥ 0` and `ε > 0` be given. There is an `h₀`
with the following property. Let `P i` be finitely many polynomials over `ℤ̄_ℓ = intQpBar ℓ` in one
set of at most `s₀` variables, and `x i` points whose coordinates have valuation at least `ρ`, with
`∑ i, v(P i (x i)) ≤ β`. Then there are roots of unity `ζ j` of orders dividing `ℓ ^ h₀` with
`v(ζ j - 1) ≤ ρ` for all `j` and `v(P i ((ζ j - 1)_j)) ≤ v(P i (x i)) + ε` for all `i`. 
