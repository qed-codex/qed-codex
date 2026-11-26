---
{
  "module": "src/New/Congruences/Selmer/StickelbergerLine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/StickelbergerLine.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/StickelbergerLine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Stickelberger systems on a line

Let `P = ψ_X(Θ_J)` be the value of the polynomial character `ψ_X = ∏_j (1 + X_j) ^ h_j` at the
element `Θ_J` of a Stickelberger system, where `J` is a set of tied auxiliary primes, the first
prime `P₀` included. On the line on which all variables but the one of `P₀` vanish, `P` is a
polynomial `P(X, 0)` in one variable. Up to a power of `1 + X` it is congruent to `R₀ R₁` modulo
`(1 + X) ^ ℓ ^ N - 1`. Here `R₀` comes from the element for `{P₀}` and has `v(R₀(0)) ≤ β` if
`ϑ(φ_{P₀})` is close enough to `ϑ(g₀)` and `N` is large, and `R₁` comes from the Euler factors at
the other primes and has small Gauss valuation. If `ρ ≤ 1` and `v_ρ(R₀ R₁) < N ρ`, the congruence
bounds the valuation of `P` at a point where `R₀ R₁` attains its Gauss valuation.

* `New.Selmer.StickelbergerSystem.exists_congruence_lineChar_element`: the congruence.
* `New.Selmer.StickelbergerSystem.exists_point_ellVal_universalChar_le`: an upper bound for the
  valuation of `P` at some point whose coordinates have valuation at least `ρ`.

Notions from other files:
* `New.Selmer.StickelbergerSystem`: elements `Θ_Q` of the group rings of class groups `Cl_Q` with a
  norm relation, a character `ϑ`, a list of integers `e`, and the number `β`.
* `New.Selmer.IsTiedPrimes`: an auxiliary set `J` of primes with places, Frobenius elements `φ`,
  tame generators `γ`, characters `h` to `ℤ / ℓ ^ N` and slopes, and a first prime `P₀ ∈ J`; for
  primes `v, w ≠ P₀` of `J` one has `h_{P₀}(φ_v) = 1` and `h_w(φ_v) = 0`.
* `New.Selmer.groupRingEval`: the value of a function on `Gal(Ω/E)`, read on `Cl_Q` and extended
  linearly, at an element of the group ring of `Cl_Q`.
* `New.ellVal`: the valuation `v` of `ℚ̄_ℓ` with `v(ℓ) = 1`, cut off at `0` from below;
  `New.intQpBar` is its valuation ring.
* `New.Selmer.gaussVal`: the Gauss valuation `v_ρ(g) = min_i (v(y_i) + ρ i)` of `g = ∑ y_i Y ^ i`.


### `isFromU1_pointChar`

 Let `E` be a CM number field embedded in the algebraic closure `Ω` of `ℚ`, let `ζ_j` be `q`-th
roots of unity in `R`, and `h_j` characters of `Gal(Ω/E)` to `ℤ / q`. If each `h_j` with `ζ_j ≠ 1`
comes from the norm-one torus with modulus `I` and is trivial at `S`, then so does the character
`g ↦ ∏ ζ_j ^ h_j(g)` (`pointChar`). 

### `coe_eval_groupRingEval_universalChar`

 Let `E` be a CM number field embedded in the algebraic closure `Ω` of `ℚ`, let `h_j` be
characters of `Gal(Ω/E)` to `ℤ / q`, and `ζ_j` `q`-th roots of unity in the valuation ring of
`ℚ̄_ℓ`. Let `a` be in the group ring over that valuation ring of `Cl_Q = U1ClassGroup Q`, the finite
ideles `u` with `u ū = 1` modulo those in `Eˣ` and the units that are `≡ 1` at the primes in `Q`.
Then the value of `ψ_X = ∏ (1 + X_j) ^ h_j` (`universalChar`) on `a`, at the point `(ζ_j - 1)_j`, is
the value of the character `∏ ζ_j ^ h_j` (`pointChar`) on `a`. 

### `le_ellVal_add`

 The ultrametric inequality for the valuation `v = ellVal` of `ℚ̄_ℓ`. 

### `ellVal_inv_sub_inv`

 For units `a` and `b`, the differences `a⁻¹ - b⁻¹` and `a - b` have the same valuation. 

### `ellVal_sub_one_le_ellVal_zpow_sub_one`

 For a unit `a`, the valuation of `a ^ k - 1` is at least that of `a - 1`, for every integer
`k`. 

### `ellVal_one_sub_mul_eq`

 If `‖a‖ = 1`, and `a ≡ b` and `c ≡ 1` up to valuation `M > v(b - 1)`, where `v = ellVal`, then
`v(1 - a * c) = v(b - 1)`. 

### `ellVal_one_sub_mul_one_sub_inv_le`

 Let `a`, `b` and `q` be `ℓ`-adic units with `a ≡ b` and `q ≡ 1` up to valuation
`M > v(b - 1)`. Then `(1 - a q ^ k) (1 - a⁻¹ q ^ k)` has valuation at most `2 v(b - 1)`, since each
factor has the valuation of `b - 1`. 

### `ellVal_eulerFactor_le`

 Let `a`, `b` and `q` be `ℓ`-adic units with `a ≡ b` and `q ≡ 1` up to valuation `M`, and let
`M > 2 r v(b - 1)`, where `r` is the length of the list `exps`. Then the product
`eulerFactor exps a q` of the factors `1 - a ^ (±1) q ^ (-e)`, `e ∈ exps`, has valuation at most
`2 r v(b - 1)`. 

### `exists_polynomial_one_sub_mul_one_sub_inv`

 Let `α` and `c` be `ℓ`-adic units. There is an integral polynomial `R` whose Gauss valuation of
radius `ρ` is at most `2 ρ`, with `R(ζ - 1) = ζ (1 - α ζ c) (1 - (α ζ)⁻¹ c)` for all integral
`ζ ≠ 0`. It is the product of `1 - α c (1 + X)` and `1 + X - α⁻¹ c`. 

### `exists_polynomial_eulerFactor`

 Let `α` and `q` be `ℓ`-adic units and `r` the length of the list `exps`. There is an integral
polynomial `R` whose Gauss valuation of radius `ρ` is at most `2 r ρ`, with `R(ζ - 1) = ζ ^ r ∏_e
∏_± (1 - (α ζ) ^ (±1) q ^ (-e))` for all integral `ζ ≠ 0`. The double product, over `e ∈ exps`, is
`eulerFactor exps (α ζ) q`. 

### `one_add_X_pow_sub_one_dvd`

 A polynomial that vanishes at all `ζ - 1` with `ζ ^ q = 1` is divisible by `(1 + X) ^ q - 1`,
since these are the `q` distinct roots of this monic polynomial. 

### `le_ellVal_one_add_pow_sub_one`

 If `v(y) ≥ ρ` for the valuation `v = ellVal`, with `ρ ≤ 1`, then `(1 + y) ^ ℓ ^ N - 1` has
valuation at least `N * ρ`. 

### `exists_ellVal_eval_le_gaussVal`

 Let `(1 + X) ^ j P ≡ R` modulo `(1 + X) ^ ℓ ^ N - 1`, where the Gauss valuation `v_ρ(R)` is less
than `N ρ` and `ρ ≤ 1`. Then `v(P(y)) ≤ v_ρ(R)` at some point `y` with `v(y) ≥ ρ`. 

### `lineChar`

 The polynomial `(1 + X) ^ (h g)`, with the exponent `h g ∈ ℤ / q` read as a natural number. It
is the restriction of `ψ_X(g) = ∏ (1 + X_j) ^ (h_j g)` to the line on which all variables but the
one belonging to `h` vanish. 

### `eval_single_groupRingEval_universalChar`

 Let the `h_i` be characters `Gal(Ω/E) → ℤ / q`, let `Q` be a finite set of primes of `E`, and
let `a` be an element of the group ring of `Cl_Q = U1ClassGroup Q`, the finite ideles `u` with
`u ū = 1` modulo those in `Eˣ` and the units that are `≡ 1` at the primes of `Q`. The value of
`ψ_X = ∏ (1 + X_i) ^ h_i` (`universalChar`) on `a`, at the point with `j`-th coordinate `y` and all
others `0`, is the value of `(1 + X) ^ h_j` (`lineChar`) on `a` at `X = y`. 

### `coe_eval_groupRingEval`

 For a function `f` on `Gal(Ω/E)` with polynomial values, extended linearly to the group ring of
`Cl_Q = U1ClassGroup Q` (`groupRingEval`), evaluation of the polynomials at a point `y` commutes
with this extension. 

### `coe_eval_groupRingEval_lineChar`

 At `X = ζ - 1` with `ζ ^ q = 1`, the value of `(1 + X) ^ h` (`lineChar`) on an element `a` of
the group ring of `Cl_Q` is the value of the character `ζ ^ h` on `a`. 

### `coe_eval_zero_groupRingEval_lineChar`

 At `X = 0`, the value of `(1 + X) ^ h` (`lineChar`) on an element `a` of the group ring of
`Cl_Q` is the value of the trivial character on `a`. 

### `norm_natCast_eq_one_of_modEq`

 A natural number `q ≡ 1` modulo a positive power of `ℓ` is an `ℓ`-adic unit. 

### `le_ellVal_natCast_sub_one`

 If `q ≡ 1` modulo `ℓ ^ N`, then `q - 1` has valuation (`ellVal`) at least `N`. 

### `eventually_le_ellVal_sub`

 Near `g₀` the values of the continuous character `ϑ = Y.twistChar` of the Stickelberger system
`Y` are congruent to `ϑ(g₀)` modulo `ℓ ^ M`. 

### `groupRingEval_element_eq_mul_prod_eulerFactor`

 The norm relation of a Stickelberger system along tied primes. If `ζ ^ ℓ ^ N = 1`, the value of
the character `ζ ^ h_{P₀}` at `Θ_J` is its value at `Θ_{P₀}` times the product, over `v ≠ P₀` in `J`
and all `e`, of `(1 - a q ^ (-e)) (1 - a⁻¹ q ^ (-e))` (`eulerFactor`), where `a = ϑ(φ_v) ζ` and `q`
is the norm of `v`. 

### `exists_congruence_lineChar_element`

 The congruence `(1 + X) ^ j₀ P(X, 0) ≡ R₀(X) R(X)` modulo `(1 + X) ^ ℓ ^ N - 1`, for `N ≠ 0`.
The polynomials `P(X, 0)` and `R₀(X)` are the values of `(1 + X) ^ h₀` (`lineChar`) at `Θ_J` and
`Θ_{P₀}`, where `h₀ = (x P₀).1.character`, and `j₀ = #(J \ {P₀}) * r` with `r` the length of
`Y.exponents`. The polynomial `R` collects the Euler factors at the primes other than `P₀`, and its
Gauss valuation of radius `ρ` is at most `2 j₀ ρ`. 

### `ellVal_one_element_singleton_le`

 A Stickelberger system `Y` for a set `S₀` of places and an element `g₀ ∈ Gal(Ω/E)` gives
elements `Θ_Q = Y.element Q` of the group rings of class groups `Cl_Q` with a norm relation, a
character `ϑ = Y.twistChar` with `ϑ(g₀) ≠ 1` and a list of `r` integers `e` (`Y.exponents`). Let
`β = v(1(Θ_∅)) + 2 r v(ϑ(g₀) - 1)`, where `1` is the trivial character and `v = ellVal`. Let `J` be
tied auxiliary primes with first prime `P₀`, so the norm `q` of `P₀` is `≡ 1` modulo `ℓ ^ N`, and
let `φ = (x P₀).1.frob` be its Frobenius element. If `β < M ≤ N` and `ϑ(φ) ≡ ϑ(g₀)` modulo `ℓ ^ M`,
then `v(1(Θ_{P₀})) ≤ β`, since each factor `1 - ϑ(φ) ^ (±1) q ^ (-e)` is congruent to
`1 - ϑ(g₀) ^ (±1)` modulo `ℓ ^ M`. 

### `exists_point_ellVal_universalChar_le`

 The system `Y`, for a set `S₀` of places and `g₀ ∈ Gal(Ω/E)`, gives elements `Θ_Q = Y.element Q`
of the group rings of class groups `Cl_Q` with a norm relation, a character `ϑ = Y.twistChar` and
`r` integers (`Y.exponents`); `β = v(1(Θ_∅)) + 2 r v(ϑ(g₀) - 1)`, with `v = ellVal`. Suppose
`ϑ(φ_{P₀}) ≡ ϑ(g₀)` modulo `ℓ ^ M`, `β + 1 < M ≤ N ρ`, and a natural number `s₀ ≥ 1` satisfies
`2 r #J ≤ s₀` and `s₀ ρ < 1`. Then `v(P(y)) ≤ β + s₀ ρ` at some point `y` whose coordinates have
valuation at least `ρ`. 
