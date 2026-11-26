---
{
  "module": "src/Lib/General/NumberTheory/GaussValuation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/GaussValuation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/GaussValuation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Gauss valuation of a polynomial over the ring of integers of ℚ̄_ℓ

The function `New.ellVal` agrees with the valuation `v` only on integral elements of `ℚ̄_ℓ`, so
almost everything is stated over their ring `ℤ̄_ℓ`. The first sections collect the rules of `v`
there and show that monic polynomials split, that every nonnegative rational number is the valuation
of some element, and that the residue field is algebraically closed. For a rational number `ρ ≥ 0`,
called the radius, and `g = ∑ y_i Y ^ i` put `v_ρ(g) = min_i (v(y_i) + ρ i)`.

* `New.Selmer.gaussVal`, `New.Selmer.gaussVal_le_eval`: `v(g(y)) ≥ v_ρ(g)` if `v(y) ≥ ρ`.
* `New.Selmer.exists_forall_ellVal_eval_eq_gaussVal`: for finitely many polynomials equality holds
  at one such point.
* `New.Selmer.gaussVal_mul`, `New.Selmer.gaussVal_eq_add_sum_roots`: `v_ρ` is additive on products,
  and it is given by `v₀(g)` and the valuations of the integral roots.
* `New.Selmer.exists_one_add_pow_eq`: a solution of `(1 + x') ^ j = 1 + x` of large valuation.
* `New.Selmer.le_ellVal_geom_sum`, `New.Selmer.ellVal_pow_sub_one_le`: bounds for the valuations of
  geometric sums of elements near `1` and of `ζ ^ j - 1` for roots of unity `ζ` of `ℓ`-power order.

Notions from other files:
* `New.ellVal`: the valuation `v` on `ℚ̄_ℓ` with `v ℓ = 1`, cut off below at `0`; `New.intQpBar ℓ`
  is the ring `ℤ̄_ℓ` of integral elements, and `x.1` is `x` as an element of `ℚ̄_ℓ`.
* `New.ThePrime ℓ`: `ℓ` is prime.

## Relation to the literature

Known result: Gauss norms and Gauss's lemma for polynomials over the integral elements of ℚ̄_ℓ.
Source: Bosch, Güntzer, Remmert, Non-Archimedean Analysis.


 ### The valuation on integral elements 

### `ellVal_val_mul`

 The valuation `v = ellVal` is additive on products of elements of `ℤ̄_ℓ = intQpBar ℓ`. (Outside
this ring it is cut off at `0` and is not additive.) 

### `min_ellVal_le_ellVal_add`

 The ultrametric inequality for `v = ellVal` on the integral elements `ℤ̄_ℓ = intQpBar ℓ`:
`min(v(x), v(y)) ≤ v(x + y)`. 

### `ellAddVal`

 The valuation `v = ellVal`, with `v(ℓ) = 1`, as an additive valuation on `ℤ̄_ℓ = intQpBar ℓ`,
the ring of integral elements of `ℚ̄_ℓ`. 

### `ellVal_add_eq_min_of_ne`

 If two integral elements `x`, `y` of `ℚ̄_ℓ` have different valuations, then `v(x + y)` is the
smaller of these. 

### `ellVal_sub_eq_min_of_ne`

 If two integral elements `x`, `y` of `ℚ̄_ℓ` have different valuations, then `v(x - y)` is the
smaller of these. 

### `le_ellVal_sum`

 A sum of integral elements of `ℚ̄_ℓ` with valuations at least `c` has valuation at least `c`. 

### `ellVal_multiset_prod`

 The valuation `ellVal` of a product of integral elements of `ℚ̄_ℓ` is the sum of their
valuations. 

 ### Roots of monic polynomials 

### `splits_of_monic`

 A monic polynomial over `ℤ̄_ℓ = intQpBar ℓ` splits: its roots in `ℚ̄_ℓ` are integral over this
valuation ring, which is integrally closed. 

### `exists_eval_eq_zero_of_monic`

 A monic polynomial of nonzero degree over `ℤ̄_ℓ = intQpBar ℓ` has a root in this ring. 

### `exists_ellVal_eq`

 Every nonnegative rational number `ρ` is the valuation `v = ellVal`, normalised by `v(ℓ) = 1`,
of some element `π` of `ℤ̄_ℓ = intQpBar ℓ`. 

### `isAlgClosed_residueField`

 The residue field of `ℤ̄_ℓ = intQpBar ℓ`, the ring of integral elements of `ℚ̄_ℓ`, is
algebraically closed. 

 ### The Gauss valuation 

### `gaussVal`

 The Gauss valuation `v_ρ(g)` of radius `ρ` of a polynomial `g = ∑ y_i Y ^ i` over
`ℤ̄_ℓ = intQpBar ℓ`: the least of the numbers `v(y_i) + ρ i`, where `v = ellVal`. 

### `gaussVal_le_coeff`

 The Gauss valuation `v_ρ(g)` is at most `v(y_i) + ρ i` for each coefficient `y_i` of `g`. 

### `gaussVal_le_eval`

 At the points `y` with `v(y) ≥ ρ` we have `v(g(y)) ≥ v_ρ(g)`: here `v = ellVal`, and
`v_ρ = gaussVal ρ` is the Gauss valuation of radius `ρ`. 

### `gaussVal_le_eval_zero`

 For a prime `ℓ`, a radius `ρ ≥ 0` and a polynomial `g` over the valuation ring `intQpBar ℓ` of
ℚ̄_ℓ, the Gauss valuation `gaussVal ρ g` is at most `v(g(0))`, the valuation of the constant term of
`g`. Here `gaussVal ρ g` is the least of `v(y_i) + ρ i` over the coefficients `y_i` of `g`, and
`v = ellVal` is the ℓ-adic valuation normalised by `v(ℓ) = 1`. 

### `gaussVal_le_of_isUnit_coeff`

 If the coefficient of `Y ^ d` in `g` is a unit, then the Gauss valuation `v_ρ(g) = gaussVal ρ g`
is at most `ρ d`. 

### `gaussVal_zero_comp_C_mul_X`

 Putting `Y = π Y'`, where `π` in `ℤ̄_ℓ = intQpBar ℓ` has valuation `v(π) = ρ` (`v = ellVal`),
turns the Gauss valuation of radius `ρ` into that of radius `0`: `v₀(g(π Y')) = v_ρ(g)`. 

### `exists_eq_C_mul_map_residue_ne_zero`

 Scaling: a polynomial `g` over `ℤ̄_ℓ = intQpBar ℓ` is `c` times a polynomial `q` whose reduction
to the residue field is nonzero, and `v(c)`, where `v = ellVal`, is the Gauss valuation `v₀(g)` of
radius `0`. 

### `exists_forall_isUnit_eval`

 Finitely many polynomials over `ℤ̄_ℓ = intQpBar ℓ` with nonzero reductions take unit values at
one point: the reductions have finitely many roots, and the residue field is algebraically closed,
hence infinite. 

### `exists_forall_ellVal_eval_eq_gaussVal`

 Generic points: for finitely many polynomials over `ℤ̄_ℓ = intQpBar ℓ` there is one point `y`
with `v(y) ≥ ρ` at which `v(g(y)) = v_ρ(g)` for all of them; here `v = ellVal`, and
`v_ρ = gaussVal ρ` is the Gauss valuation of radius `ρ`. 

### `gaussVal_mul`

 Gauss's lemma: the Gauss valuation `v_ρ` of a product of two integral polynomials is the sum of
their Gauss valuations. Evaluate at a point that is generic for `f`, `g` and `f g`. 

 ### The Gauss valuation and the roots 

### `exists_ellVal_eval_eq_gaussVal`

 For one integral polynomial `f` there is an integral point `y` with `v(y) ≥ ρ` at which
`v(f(y))` is the Gauss valuation `v_ρ(f)`. 

### `gaussVal_X_sub_C`

 For an integral element `α` the Gauss valuation of radius `ρ` of the linear polynomial `Y - α`
is `min(v(α), ρ)`, where `v = ellVal`: evaluation at `0` and the leading coefficient
give `≤`, and a generic point gives `≥`. 

### `gaussVal_prod_X_sub_C`

 For a prime `ℓ`, a radius `ρ ≥ 0` and a multiset `R` of integral elements (elements of the
valuation ring `intQpBar ℓ` of ℚ̄_ℓ), the Gauss valuation `gaussVal ρ` of `∏ (Y - α)` is
`∑ min(v(α), ρ)`, both over `α` in `R`. Here `v = ellVal` is the ℓ-adic valuation normalised by
`v(ℓ) = 1`, and `gaussVal ρ g` is the least of `v(y_i) + ρ i` over the coefficients `y_i` of `g`. 

### `ellVal_eval_eq_of_roots_eq_zero`

 An integral polynomial `q` without integral roots has the same valuation `ellVal` at all
integral points: if `q ≠ 0`, each root `β` in `ℚ̄_ℓ` has `‖β‖ > 1`, so `‖y - β‖ = ‖β‖` for integral
`y`. 

### `exists_eq_mul_prod_roots`

 An integral polynomial `g` is `q ∏ (Y - α)` over its integral roots `α` with multiplicity,
where `v(q(y)) = v₀(g)` at all integral points `y`. Here `v` is the valuation `ellVal` and `v₀`
the Gauss valuation of radius `0`. 

### `gaussVal_eq_add_sum_roots`

 The Gauss valuation `v_ρ(g)` of radius `ρ`, the least of the `v(y_i) + ρ i` for the coefficients
`y_i` of `g`, is `v₀(g) + ∑ min(v(α), ρ)`: the sum is over the integral roots `α` of `g` with
multiplicity, `v` is the valuation `ellVal` and `v₀` the Gauss valuation of radius `0`. 

### `ellVal_eval_eq_add_sum_roots`

 At an integral point `y` an integral polynomial `g` has `v(g(y)) = v₀(g) + ∑ v(y - α)`, the sum
over the integral roots `α` of `g` with multiplicity; `v` is the valuation `ellVal` and `v₀` the
Gauss valuation of radius `0`. 

 ### Powers of elements near `1`, geometric sums and roots of unity 

### `exists_one_add_pow_eq`

 Let `x` be integral with `v(x) ≥ ρ`, for the valuation `v` = `ellVal`, and let `1 ≤ j ≤ m`.
Then some integral `x'` with `(1 + x') ^ j = 1 + x` has `v(x') ≥ ρ / m`: the `j` solutions have
the product `± x`. 

### `geom_sum_range_mul`

 The geometric sum of length `a b` is the geometric sum of length `a` times the geometric sum of
length `b` in `α ^ a`. 

### `le_ellVal_geom_sum`

 If `v(α - 1) ≥ ρ` with `ρ ≤ 1`, where `v` is the valuation `ellVal`, then `∑_{i < ℓ ^ n} α ^ i`
has valuation at least `n ρ`: it is the product of the factors `∑_{i < ℓ} α ^ (i ℓ ^ h)` for
`h < n`, each congruent to `ℓ` modulo `α - 1`, and `v(ℓ) = 1 ≥ ρ`. 

### `ellVal_sub_one_of_isPrimitiveRoot`

 A root of unity `ζ` of order `ℓ ^ (h + 1)` has `v(ζ - 1) = 1 / φ(ℓ ^ (h + 1))`, where `φ` is
Euler's function. 

### `ellVal_pow_sub_one_of_isPrimitiveRoot`

 If `ζ` has order `ℓ ^ (h + 1)`, `j ≠ 0` and the exponent `t = padicValNat ℓ j` of `ℓ` in `j`
is at most `h`, then `v(ζ ^ j - 1) = ℓ ^ t / φ(ℓ ^ (h + 1))`; here `v = ellVal` and `φ` is
Euler's function. 

### `ellVal_pow_sub_one_le`

 Let `ℓ` be a prime and `ζ` an element of the valuation ring of ℚ̄_ℓ with `ζ ^ ℓ ^ h = 1`. Let
`v = ellVal` be the valuation normalised by `v(ℓ) = 1`, which is `-log_ℓ |·|` on integral
elements. If `ρ < 1` and `v(ζ - 1) ≤ ρ / m`, then `v(ζ ^ j - 1) ≤ ρ` for every `j` with
`1 ≤ j ≤ m`. 
