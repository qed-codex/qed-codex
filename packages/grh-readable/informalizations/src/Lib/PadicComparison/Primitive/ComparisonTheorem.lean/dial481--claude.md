---
{
  "module": "src/Lib/PadicComparison/Primitive/ComparisonTheorem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/Primitive/ComparisonTheorem.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/Primitive/ComparisonTheorem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The primitive comparison theorem and finiteness of p-adic cohomology

This file concerns a proper scheme `Y` over `R` that is charted over an algebraic closure `Ω` of `ℚ`
(`New.Variety.IsCharted`). A p-adic test is a product of valuation rings over `O_C`, the integers of
`ℂ_p`, and `O^♭` is the tilt of `O_C`. The primitive comparison theorem compares the mod `p`
cohomology of `Y`, tensored with `O^♭`, with the cohomology of its points in p-adic tests with
tilted coefficients.

## Main definitions and results

* `New.Variety.finite_and_primitive_comparison`: let `Y` be proper over `R` and charted over `Ω`,
  and assume `IsAcyclicOnPerfect (moduleCoeff (tensorCoeff M))`. Then `Y_Ω` has flat base change and
  finite mod `p` cohomology, and the comparison map is bijective.
* `New.Variety.finite_padic_cohomology`: the cohomology with coefficients `ℤ_p` is finitely
  generated; hence `New.Variety.ellAdicCohom R Ω n`, which is `ℚ_p ⊗` this module, is
  finite-dimensional at `Y`.
* `New.Variety.ellAdicCohom.continuous_galoisAction`: the Galois action
  `New.Variety.ellAdicCohom.galoisAction` is continuous, tested on a vector and a linear map to
  `Q̄_p ^ N`. Modulo `p ^ k` a class is defined over finitely many elements of `Ω`, so it is fixed
  by an open subgroup.

Notions from other files:
* `New.Variety.genericTestOver`: The functor sending a p-adic test with ring R to R[1/p], a test
  over Ω with algebra structure through Ω → ℂ_p.
* `New.Variety.primitiveMap`: The natural map O^♭ ⊗ LC(Spec S[1/p], 𝔽_p) → S^♭ on p-adic tests S,
  with LC the locally constant functions; its source is `New.Variety.oFlatLocConst`.
* `New.Variety.HasFlatBaseChange` N: M ⊗ Hⁿ(N, Φ) → Hⁿ(N, M ⊗ Φ) is bijective for flat M.
* `New.Variety.testPoints`: For R → O_C, the functor sending an R-scheme X to the functor S ↦ X(S)
  of its points over R in p-adic tests.
* `New.Variety.H`: `H N F n` is Extⁿ(N, F) among functors to abelian groups; for
  `N = freeAb X = ℤ[X]` it is the cohomology Hⁿ(X, F). `testIncl ⋙ X` restricts `X` to test rings.

## Relation to the literature

Known result: Finiteness and Galois continuity of p-adic étale cohomology. The result is stated for
cohomology on test rings, not identified with étale cohomology, of proper schemes charted over an
algebraic closure of Q, with constant coefficients, where integral coefficients are the Witt vectors
of the mod p functions. Finiteness is lifted from finiteness modulo p, which comes from the
primitive comparison. Source: SGA 4, Exp. XIV (Artin), finiteness for proper morphisms; Scholze 2013
Thm 1.1; by duality, Zavyalov arXiv 2301.03821 Appl. 1.3.4.

See also `Lib.PadicComparison.HodgeTate.PeriodMap`.


 ## The primitive comparison theorem and flat base change 

### `PadicTest.bijective_generic_points`

 The valuative criterion in a p-adic test `c`. Its ring `c.ProdRing` is the product of a
non-empty family of valuation rings (cells) with a ring map from O_C, and
`c.GenericRing = c.ProdRing[1/p]`. Let `Y` be proper over `R`, and make `Spec c.ProdRing` and
`Spec c.GenericRing` schemes over `R` by `a : Spec c.ProdRing ⟶ Spec R` and
`b : Spec c.GenericRing ⟶ Spec R`. The map `Spec c.GenericRing → Spec c.ProdRing` is a map over `R`:
`w` says that `b` is the restriction of `a`, and `r` is the trivial map of the one-point base of
`Over`, so `w` is `Spec.map (algebraMap c.ProdRing c.GenericRing) ≫ a = b ≫ 𝟙 _`. Then restriction
`Y(c.ProdRing) → Y(c.GenericRing)` of points over `R` is bijective. 

### `toGenericPoints`

 For a scheme Y over R, the map Y(S) → Y(S[1/p]), natural in the p-adic test S; `he` says that
R → Ω → ℂ_p agrees with R → O_C → ℂ_p. 

### `ComparedTheory.isFiniteLerayHirsch_freeAb_iff_relFreeAb`

 Let `Ω` be a field in which `ℓ` is invertible and `D` a compared theory on tests over `Ω`
(`New.Variety.ComparedTheory`). Then `D.IsFiniteLerayHirsch` (the classes `D.comparison` form a
Leray–Hirsch basis and the total cohomology is finite) holds for `ℤ[X] = freeAb X` iff it holds for
`ℤ[X] / ℤ[U]` (`relFreeAb`), where `U = offClosedFibre X` is the part of `X` away from the special
fibre. Over a field `U` does not count: the maximal ideal of `Ω` is zero, so `U` has points only
over the zero ring. 

### `hasFlatBaseChange_algPointsOf`

 The points of a proper `Y` over `R` on tests over `Ω` have flat base change: the functor is
covered by affine pieces (`isAffinelyCovered_algPointsOf`). 

### `hasFlatBaseChange_geomPoints`

 Flat base change for the points of `Y_Ω` on test rings, for `Y` proper over `R`. Restriction
from all test rings to tests over `Ω` is bijective on cohomology (`isBijective_algToBaseChange`)
and commutes with base change (`baseChangeMap_pull`), and on tests over `Ω` flat base change holds
by `hasFlatBaseChange_algPointsOf`. 

### `tiltReprIsoGenericRepr`

 The functors `S ↦ Hom(O^♭, S^♭)` (maps of `O^♭`-algebras) and `S ↦ Hom(Ω, S[1/p])` (maps of
tests over `Ω`) on `p`-adic tests are isomorphic: each value is a single point, since `O^♭` and
`Ω` are initial. 

### `oFlatLocConstOfSelfIso`

 The locally constant functions on `Spec Ω`, tensored with `O^♭` (`oFlatLocConst` at the test
`Ω`), are `O^♭` itself: on the spectrum of a field the locally constant functions are
constant. 

### `finite_and_primitive_comparison`

 Primitive comparison. Let `Ω` be algebraically closed with a map to `ℂ_p`, `Y` proper over `R`
and charted over `Ω` (`IsCharted`), and `M` an `O^♭`-module. Assume `ac`: for each perfect
`O^♭`-algebra `b`, the functor `S ↦ Hom(b, S^♭)` on p-adic tests, with coefficients `S ↦ S^♭ ⊗ M`,
has cohomology `b ⊗ M` in degree 0. Write `X` for the points of `Y_Ω` on test rings. Then (a) the
cohomology of `Y_Ω` commutes with flat extension of coefficients; (b) each `Hⁿ(Y_Ω, 𝔽_p)` is finite;
(c) if moreover `R` maps to `O_C` compatibly (`he`), then `primitiveMap ⊗ M` induces a bijection in
every degree, along `toGenericPoints` followed by `algToBaseChange` (points of `Y` over tests over
`Ω` taken as points of `Y_Ω`). Here `primitiveMap` is the natural map `O^♭ ⊗ LC(Spec S[1/p]) → S^♭`,
with `LC` the locally constant `𝔽_p`-valued functions. The bijection goes from the cohomology of
`Y_Ω` with coefficients `A ↦ O^♭ ⊗ LC(Spec A) ⊗ M` to that of `S ↦ Y(S)` on p-adic tests with
coefficients `S^♭ ⊗ M`. Only (c) uses the map `R → O_C`. 

 ## Finite generation of p-adic cohomology and continuity of the Galois action 

### `finite_padic_cohomology`

 For `Y` proper over `R` and charted over `Ω`, the cohomology `Hⁿ(Y_Ω, ℤ_p)`, computed on test
rings, is a finitely generated `ℤ_p`-module. 

### `instance {n : ℕ} : Module.Finite ℚ_[p] (ellAdicCohom R Ω n ⟨Y⟩)`

 For `Y` proper over `R` and charted over `Ω`, the `p`-adic cohomology `ℚ_p ⊗ Hⁿ(Y_Ω, ℤ_p)` is
finite-dimensional over `ℚ_p`. 

### `ellAdicCohom.continuous_galoisAction`

 Let `Y` be proper over `R` and charted over `Ω`, and `Gal(Ω/K)` the profinite Galois group of
`Ω` over a field `K`, acting `R`-linearly. For a class `x` in `Vⁿ(Y) = ℚ_p ⊗ Hⁿ(Y_Ω, ℤ_p)` and a
`ℚ_p`-linear map `l : Vⁿ(Y) → Q̄_p ^ N`, the map `g ↦ l (g x)` is continuous. 
