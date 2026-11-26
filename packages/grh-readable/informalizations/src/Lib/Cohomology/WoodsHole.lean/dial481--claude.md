---
{
  "module": "src/Lib/Cohomology/WoodsHole.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/WoodsHole.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/WoodsHole.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Woods Hole (half of Atiyah–Bott): maps killed under λ_h on Hodge classes are h-null

The main theorem, `New.Variety.ellAdicCohom.woods_hole`: if a combination `∑ b_i u_i` of maps
`W → Y` kills all Hodge classes of `Y` under the Hodge–Tate map `λ_h` (`New.Variety.hodgeTateMap`),
then for every `c : W → Y` the local terms of weight `h` at the coincidences of `c` and the `u_i`
add up to zero (`New.Variety.IsNullFamily`). The proof pulls back the diagonal class of
`New.Variety.exists_diagonal_local_terms`, writes it as a sum of cross products
(`New.Variety.kunneth`) and takes the coefficient of `t ^ h` in the scaling parameter `t`: a linear
form does this (`Polynomial.exists_dual_eval_mul_eq_coeff_mul`), the pull-back of a cross product is
`New.Variety.map_scaledGraph_baseChange_cross`, and
`New.Variety.sum_mul_hodgeTateMap_scaledGraph_eq_zero` is the vanishing of the weighted sum.
`New.Variety.HodgeH` is Hodge cohomology, `New.Variety.algPoints` the functor of points, and
`New.Variety.HasAtlas` a finite cover by charts with `d` étale coordinates.

## Overview of this theory

Throughout, `ℓ` is a fixed prime. Cohomology of a functor `X` to sets, with coefficients in a
functor `F` to abelian groups, is `Extⁿ(ℤ[X], F)`. Here `ℤ[X]` is the free abelian group functor on
`X`, and the Ext is taken in functors on test objects: rings, or pairs of a ring and a module.

On absolutely integrally closed rings `A` (every monic polynomial of positive degree has a root),
locally constant functions on `Spec A` give `𝔽_ℓ`-cohomology. Their Witt vectors give
`ℤ_ℓ`-cohomology. `New.Variety.ellAdicCohom` is `X ↦ ℚ_ℓ ⊗ Hⁿ(X ×_R Ω, ℤ_ℓ)`, for `X` over a ring
`R` and an `R`-algebra `Ω`. Test objects may also be pairs `(B, M)` of a `k`-algebra `B` and a
`B`-module `M`. On these, `New.Variety.HodgeH` of a functor `N` in degree `q` is `Ext^q` from
`(B, M) ↦ N(B ⊕ M)` to `(B, M) ↦ ⋀_B M`.

* `New.Variety.IsProperOver.proper_base_change`: let `A` be an absolutely integrally closed local
  domain that is a valuation ring, with `ℓ` a unit in `A`. Let `Y` be proper over `Spec A`. Then
  restriction from `Y` to its closed fibre is bijective on `𝔽_ℓ`-cohomology in every degree.
* `New.Variety.isTestCohomEquiv_baseChangeTransition`: let `A` be a valuation ring of an algebraic
  closure `ℚ̄` of `ℚ`, with a prime `p` in its maximal ideal and `ℓ` a unit. Let `A` be an algebra
  over a ring `R`, and let `Y` over `R` be built from charts étale over tori
  (`New.Variety.IsCharted`). Then pull-back `Hⁿ(Y_A, 𝔽_ℓ) → Hⁿ(Y_ℚ̄, 𝔽_ℓ)` is bijective for all `n`.
* `New.Variety.ellAdicCohom.woods_hole`: let `R ⊆ E → k ⊆ ℚ̄_p`, with `E` a field of characteristic
  0 and `k` algebraically closed. Let `Y` be proper and `W` projective over `R`. Let `Y` over `E`
  and `W` over `k` have atlases of dimension `d`. Let `uᵢ : W ⟶ Y` be maps, and let `bᵢ ∈ k` be
  almost all zero. Let `λ_h` be the Hodge–Tate map `New.Variety.hodgeTateMap h`. Assume that
  `h > d`, or that `∑ bᵢ λ_h(uᵢ^* x) = 0`, read over `k`, for all `x` of degree at most `d` in
  `HodgeH` of `Y` over `E`. Then `New.Variety.IsNullFamily` holds: for `c : W ⟶ Y`, if each
  coincidence `c y = uᵢ y`, `y ∈ W(k)`, has a tangent polynomial `P` with `P(1) ≠ 0`, the terms
  `bᵢ · (coefficient of degree h of P) / P(1)` add up to zero.

These replace proper base change (SGA 4, XII) and smooth base change (SGA 4), here with coefficients
`𝔽_ℓ` over such rings. They also replace half of the holomorphic Lefschetz (Woods Hole) formula of
Atiyah and Bott, for `h`-forms and correspondences. No comparison with étale or coherent cohomology
is stated.

Structure of the development. `Etale`: descent, Mayer–Vietoris, limits, `ℓ`-adic coefficients.
`ProperBaseChange`: cover `X` by points with values in valuation rings, and reduce to the valuation
rings of a single field. `LerayHirsch`, `TorsionTheories`, `ProjectiveLine`: `1` and the first Chern
class of `O(1)` form a basis of the cohomology of `ℙ¹`. With duality from `Lib.PadicComparison`,
`SmoothBaseChange` follows. `Hodge`: point classes, the Künneth formula, local terms of the
diagonal. `PointClass`: the Hodge–Tate map of `Lib.PadicComparison` keeps distinct point classes
independent, by reduction to `ℙᵈ` and `ℙ¹`.

## This file

Notions from other files:
* `New.Variety.HodgeH.baseChange`: Base change: for an E-algebra k, the additive map from the Hodge
  cohomology over E of N to that over k of N restricted to k-algebras.

## Relation to the literature

Known result: Half of the holomorphic Lefschetz (Woods Hole) formula for h-forms and
correspondences. No trace is computed here. The statement is that if a combination of pull-backs
kills the Hodge classes of degree at most the dimension d under the Hodge–Tate map λ_h, then the z^h
coefficients of the local terms det(1−zA)/det(1−A) at simple coincidences add up to zero. Source:
M. F. Atiyah, R. Bott, A Lefschetz fixed point formula for elliptic complexes II, Ann. of Math. 88
(1968) 451-491; G. Kondyrev, A. Prikhodko, Holomorphic Atiyah-Bott formula for correspondences,
Arnold Math. J. (2022); SGA5 III 6.12.


### `Polynomial.exists_dual_eval_mul_eq_coeff_mul`

 Let `k` be an infinite field and `h` a natural number. Some linear form `L` on the functions
`k → k` reads off the coefficient of `X ^ h` on polynomial functions: for every polynomial `Q` and
`a` in `k`, `L` sends `t ↦ Q(t) * a` to the coefficient of `X ^ h` in `Q`, times `a`. 

### `New.Variety.map_scaledGraph_baseChange_cross`

 Let `f g : W ⟶ X` be maps from a functor on `k`-algebras to a functor on `E`-algebras restricted
to `k`-algebras, and `t` in `k`. Pulling the cross product `x × y` of two Hodge classes of `X` back
along `scaledGraph t f g` (`w ↦ (f (s_t w), g w)`, where `s_t : (a, m) ↦ (a, t m)` scales the module
part of `A ⊕ M`), after base change to `k`, gives the cup product of the scaled pull-back
`s_t f^* x` and of `g^* y`, restricted to the diagonal of `W`. 

### `New.Variety.sum_mul_hodgeTateMap_scaledGraph_eq_zero`

 The vanishing half of the Woods Hole argument. Let `u i : W ⟶ Y` be maps over `R` and `b i ∈ k`
almost all zero. Assume that `Y` over `E` (`algPointsOf E R Y`, the functor of `E`-algebra points of
`Y`) has an atlas of dimension `d`, and that `h > d` or the sum of the `b i • λ_h ((u i)^* x)` is
zero for the Hodge classes `x` of `Y` of degree at most `d`, where `λ_h` is the Hodge–Tate map
`hodgeTateMap`. Let `c : W ⟶ Y`, and let `φ` be a linear form on `PairH` of `W`, the target of
`λ_d`: total cohomology on pairs `(S, M)` of `Z[W](B_{S,M})` with coefficients `S[1/p]`. Let `L` be
a linear form on `k → k` that reads off the coefficient of `t ^ h` on polynomial functions. Then for
every class `z` of `Y × Y`, the sum over `i` of `b i` times `L` of `t ↦ φ (λ_d (Φ t i z))` is zero.
Here `Φ t i z` is `z` pulled back along `(u i ∘ s_t, c)` (`New.Variety.scaledGraph`), with
`s_t : (a, m) ↦ (a, t m)` on the square-zero extension `B ⊕ M` of a `k`-algebra `B`. 

### `New.Variety.ellAdicCohom.woods_hole`

 Half of the Atiyah–Bott formula. Let `Y` be proper and `W` projective over `R`, a subalgebra of
`E`; let `R → E → k → ℚ̄_p` with `E`, `k` fields of characteristic 0 and `k` algebraically closed
(`EmbeddedInQpBar p k`); let `Y` over `E` and `W` over `k` have atlases of dimension `d`
(`New.Variety.HasAtlas`: finitely many charts with `d` étale coordinates). Let `u i : W ⟶ Y` be maps
and `b i ∈ k` almost all zero. Assume that `h > d`, or that `∑ b i • λ_h ((u i)^* x) = 0` for every
Hodge class `x` of `Y` over `E` of degree `q ≤ d`, read over `k`, with `λ_h` the Hodge–Tate map
`New.Variety.hodgeTateMap h`. Then `∑ b i [u i]` is `h`-null: for every `c : W ⟶ Y`, the local terms
of weight `h` at the coincidences of `c` and the `u i` add up to zero (`New.Variety.IsNullFamily`).

