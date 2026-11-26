---
{
  "module": "src/Lib/PadicHodge/PeriodRings/AxTheorem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/PeriodRings/AxTheorem.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/PeriodRings/AxTheorem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tilting, Fontaine's θ, the ring O_C and Ax's theorem on Galois invariants in ℂ_p

This file studies the absolute Galois group `New.Gp` of `ℚ_p`, its action on `ℂ_p`, and its
invariants. For `p`-adically complete rings in which `p` is not a unit, the untilt and Fontaine's
`θ` are natural, and they are onto if the ring is also absolutely integrally closed. Ax's theorem
then describes the elements of `ℂ_p` fixed by a subgroup `J` of `New.Gp` as limits of algebraic
elements fixed by `J`.

## Main definitions and results

* Tilting for a ring `R` in which `p` is not a unit. `New.Variety.tiltMap` makes Mathlib's
  `PreTilt R p` functorial. For `p`-adically complete `R`, the untilt `x ↦ x^♯` and Fontaine's `θ`
  are natural in `R` (`New.Variety.untilt_tiltMap`, `New.Variety.fontaineTheta_map_tiltMap`). Both
  are onto if `R` is absolutely integrally closed
  (`New.Variety.fontaineTheta_surjective_of_isAbsIntegrallyClosed`). The tilt of a `p`-adically
  complete valuation ring is a valuation ring.
* The Galois group `New.Gp` of `ℚ̄_p / ℚ_p` and its cyclotomic character `New.cyclotomicGp`.
* The continuous isometric action of `New.Gp` on `ℂ_p` (`New.completionAction`), which restricts
  to an action by ring automorphisms on the ring of integers `New.OC`.
* `O_C` is `p`-adically complete and absolutely integrally closed, with `O_C[1/p] = ℂ_p`.
* `New.Period.ax_mem_closure_fixedField`: Ax's theorem; an element fixed by a subgroup `J` is a
  limit of algebraic elements fixed by `J`.
* `New.Period.exists_algebraic_of_fixed_near_one`: an element fixed by a neighbourhood of `1` is
  algebraic.

Notions from other files:
* `New.cyclotomicChar`: the ℓ-adic cyclotomic character Γ → ℤ_ℓ^× of a group Γ that acts on a
  field Ω by ring automorphisms; `New.cyclotomicGp` is the case Γ = `New.Gp p`, Ω = ℚ̄_p, ℓ = p.

## Relation to the literature

Known; see `Lib.PadicHodge.PeriodRings.DeRhamPeriods` and `Lib.PadicHodge.TateSen` for sources.


 ## Functorial tilting, Fontaine's θ and the Galois action on ℂ_p 

 ### Functoriality of the tilt and of `θ` 

### `tiltMap`

 The tilt `PreTilt R p` is the inverse limit of `R / p` along `x ↦ x ^ p`. A ring homomorphism
`f : R → R'` induces the ring homomorphism `tiltMap f` between the tilts, which applies `f` modulo
`p` to each component. 

### `coeff_tiltMap`

 If `y ∈ R` lifts the `n`-th component of `x` in `R / p`, then `f y` lifts the `n`-th component
of `tiltMap f x` in `R' / p`. 

### `tiltMap_id`

 The identity of `R` induces the identity of its tilt. 

### `tiltMap_comp`

 The map of tilts induced by a composite is the composite of the induced maps. 

### `wittVector_ringHom_ext_of_teichmuller`

 Let b be a perfect ring of characteristic p and R a p-adically separated commutative ring.
Two ring homomorphisms W(b) → R that agree on all Teichmüller lifts are equal. 

### `untilt_tiltMap`

 The untilt commutes with the maps of tilts: `(tiltMap f x)^♯ = f (x^♯)` for `p`-adically
complete `R` and `R'`. 

### `fontaineTheta_map_tiltMap`

 Fontaine's `θ` is natural: it commutes with a ring map `f` and the map of Witt vectors of
the tilts that `f` induces. 

### `untilt_dvd_iff`

 Let R be a p-adically complete, integrally closed domain in which p is not a unit. For x, y
in the tilt of R, x^♯ divides y^♯ in R if and only if x divides y. 

### `untilt_eq_zero_iff`

 Let R be a p-adically complete, integrally closed domain in which p is not a unit. An element
x of the tilt of R has untilt x^♯ = 0 exactly when x = 0. 

### `untilt_surjective_of_isAbsIntegrallyClosed`

 Let R be a p-adically complete ring in which p is not a unit. If R is absolutely integrally
closed (every monic polynomial of positive degree over R has a root in R), then every element of R
is the untilt x^♯ of an element x of the tilt. 

### `fontaineTheta_surjective_of_isAbsIntegrallyClosed`

 Let R be a p-adically complete ring in which p is not a unit. If R is absolutely integrally
closed, then Fontaine's `θ : W(tilt R) → R` is onto. 

### `instance : IsDomain (PreTilt R p)`

 The tilt of a `p`-adically complete valuation ring is an integral domain. 

### `instance : ValuationRing (PreTilt R p)`

 The tilt of a `p`-adically complete valuation ring is a valuation ring. 

 ### The Galois group of `ℚ_p` and its action on `ℂ_p` 

### `Gp`

 The absolute Galois group G_p = Gal(Q̄_p over Q_p). 

### `OC`

 The ring of integers `valRingCp p` of `ℂ_p` (its elements of norm at most `1`) as a type, for
the prime `p` fixed by the class `ThePrime p`. 

### `intQpBar`

 The valuation ring of ℚ̄_p. 

### `Selmer.valuation_intQpBar_le_iff`

 The valuation of the valuation ring `intQpBar p` of `ℚ̄_p` orders elements as the norm does. 

### `completionAction`

 The action of `Gp p` on `PadicAlgCl p` extends to an action by ring homomorphisms on its
completion `ℂ_p`. 

### `cyclotomicGp`

 The p-adic cyclotomic character of the absolute Galois group of Q_p, obtained from its
action on the algebraic closure of Q_p. 

### `instance : Fact ¬IsUnit (p : OC)`

 `p` is not a unit in `O_C`, as `‖p‖ < 1`. 

### `OC.exists_dvd_pow`

 In `O_C`, a nonzero element `t` divides some power of any non-unit `s`. 

### `instance : Away (p : OC) ℂ_[p]`

 `ℂ_p` is the localization `O_C[1/p]`. 

### `instance : IsAdicComplete (span {(p : OC)}) OC`

 `O_C` is `p`-adically complete. 

### `instance : IsAbsIntegrallyClosed OC`

 `O_C` is absolutely integrally closed: every monic polynomial of positive degree over `O_C`
has a root in `O_C`. 


## Ax's theorem on invariants of subgroups of the Galois group

For Ax's theorem one halves a bound on the number of points of a `J`-stable set at each step,
replacing the set by the roots of `∑ t, (X - t) ^ 2 ^ k`, where `t` runs over some of its points.
The losses in distance multiply to at most a factor `16`.


### `norm_pow_sub_one_le_norm_sub_one`

 In an ultrametric normed field, if `‖ζ‖ ≤ 1` then `‖ζ ^ a - 1‖ ≤ ‖ζ - 1‖` for every `a`. 

### `norm_zeta_sub_one_pow`

 If `ζ` is a primitive `p ^ (m + 1)`-th root of unity in an ultrametric normed field `F`, then
`‖ζ - 1‖ ^ φ (p ^ (m + 1)) = ‖p‖`, where `φ (p ^ (m + 1)) = p ^ m (p - 1)`. 

### `pow_le_norm_aeval`

 Let K be algebraically closed, L a normed field over K, f in K[X] with leading coefficient
a, x in L, r ≥ 0. If ‖x − w‖ ≥ r for every root w of f, then ‖f(x)‖ ≥ ‖a‖ r^(deg f). 

### `axRadius`

 The radii in the proof of Ax's theorem: `axRadius ε k = ε / 16 * 2 ^ ((2 * k + 4) / 2 ^ k)`.
Let `x ∈ ℂ_p` be fixed by a subgroup `J` of `G_p`, and let every point of `ℚ̄_p` fixed by `J` be
at distance at least `ε` from `x`. Then every point of a `J`-stable set with at most `2 ^ k`
elements is at distance at least `axRadius ε k` from `x` (`axRadius_le_norm_sub_of_mem`). 

### `axRadius_succ_pow`

 The radii satisfy `axRadius ε (k + 1) ^ 2 ^ k = (2 ^ (k + 1))⁻¹ * axRadius ε k ^ 2 ^ k`: both
sides are `(ε / 16) ^ 2 ^ k * 2 ^ (k + 3)`. 

### `inv_le_norm_natCast_padic`

 A positive integer `n ≤ m` has `p`-adic norm at least `1 / m`. 

### `axRadius_succ_le_norm_sub_of_mem`

 The induction step of Ax's theorem. Let `x ∈ ℂ_p` be fixed by a subgroup `J` of `G_p`, and let
`ε > 0`. If every point of a `J`-stable multiset of points of `ℚ̄_p` with at most `2 ^ k` distinct
elements is at distance at least `axRadius ε k` from `x`, then every point `z` of a `J`-stable
multiset `S` with at most `2 ^ (k + 1)` distinct elements is at distance at least
`axRadius ε (k + 1)` from `x`. 

### `axRadius_le_norm_sub_of_mem`

 The claim in the proof of Ax's theorem. Let `x ∈ ℂ_p` be fixed by a subgroup `J` of `G_p`, let
`ε > 0`, and let every point of `ℚ̄_p` fixed by `J` be at distance at least `ε` from `x`. Then every
point of a `J`-stable multiset `S` of points of `ℚ̄_p` with at most `2 ^ k` distinct elements is at
distance at least `axRadius ε k` from `x`. 

### `ax_mem_closure_fixedField`

 Ax's theorem (a known result), the nontrivial inclusion of the Ax–Sen–Tate theorem: let `J` be
a subgroup of `G_p`. Every `x ∈ ℂ_p` fixed by `J` lies in the closure of the image, under the
inclusion `coe'` of `ℚ̄_p` into its completion `ℂ_p`, of the fixed field of `J` in `ℚ̄_p`. 

### `exists_algebraic_of_fixed_near_one`

 If `x ∈ ℂ_p` is fixed by every `g` in some neighbourhood of the identity of `G_p`, then `x` is
the image `coe' y` of an element `y` of `ℚ̄_p` under the inclusion of `ℚ̄_p` into `ℂ_p`. 
