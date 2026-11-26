---
{
  "module": "src/Lib/Cohomology/SmoothBaseChange.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/SmoothBaseChange.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/SmoothBaseChange.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Charted varieties, and smooth base change from a valuation ring to its fraction field

From local charts to whole varieties, for cohomology computed on test rings.

* `New.Variety.algToBaseChange`, `New.Variety.isBijective_algToBaseChange`: the cohomology of the
  base change `Y_A` on all test rings agrees with that of `Y` on tests over `A`
  (`New.Variety.TestOver`).
* `New.Variety.ComparedTheory.mem_of_isClosedClass_of_isCharting`: a class of functors governed by
  `New.Variety.ComparedTheory.IsFiniteLerayHirsch` that contains the point contains every functor
  charted by pieces étale over tori (`New.Variety.IsCharting`).
* `New.Variety.isTestCohomEquiv_baseChangeTransition`: let `A` be a valuation ring of an algebraic
  closure `Ω` of `ℚ`, of residue characteristic `p ≠ ℓ`, and let `Y` be charted; then the mod `ℓ`
  cohomology of `Y_A` and of `Y_Ω` agree.

`D.IsFiniteLerayHirsch N` says that the cohomology of `N` with locally constant `ZMod ℓ`
coefficients is finite and computes that of the theory `D`. The functor
`relFreeAb (offClosedFibre X)` is `ℤ[X] / ℤ[U]`, where `U` consists of the points over the tests in
which the maximal ideal of `A` generates the unit ideal.

Notions from other files:
* `New.Variety.freeAb`: The functor sending a set-valued functor Y to Z[Y], whose value at A is the
  free abelian group on Y(A).
* `New.Variety.IsClosedClass`: A closed class P of functors D → Ab: (a) P contains every zero
  functor N (written `𝟙 N = 0`); (b) for a short exact sequence 0 → X₁ → X₂ → X₃ → 0 with X₁ in P,
  the middle term X₂ is in P exactly when the quotient X₃ is.
* `New.Variety.geomPoints`: The functor of points of the base change `X ×_R Ω` of a scheme `X` over
  `R`.

## Relation to the literature

Known result: Smooth base change, with restriction to the generic fibre bijective on cohomology.
Here it is proved for schemes that are covered by finitely many pieces étale over tori and are not
assumed proper. The base is the valuation ring of a place above p of an algebraic closure of Q, the
coefficients are the constant F_ℓ with ℓ invertible, and the result is deduced from proper base
change and duality on products of projective lines. Source: Artin, SGA 4 Exp. XV 2.1, XVI 1.2
(1973); Stacks Project Tag 0EYQ; for the route through the class of the diagonal, Zavyalov, Poincaré
duality in abstract 6-functor formalisms (arXiv 2301.03821) and Li-Reinecke-Zavyalov (arXiv
2410.08200).


### `algToBaseChange`

 For Y over R, the map sending a point of Y over R in an A-algebra c to the point of the base
change Y_A given by it and the structure map A → c. 

### `isBijective_algToBaseChange`

 Let `Y` be over `Spec R` and `A` an `R`-algebra. For any coefficient `F` on test rings, the map
induced by `algToBaseChange`, from the cohomology of the base change `Y_A` to the cohomology of the
points of `Y` on tests over `A` (`New.Variety.TestOver`: test rings with an `A`-algebra structure),
is bijective in every degree. 

### `ComparedTheory.mem_of_isClosedClass_of_isCharting`

 Let `A` be a valuation ring (`PreValuationRing`) and a `k`-algebra in which `ℓ` is a unit, `D` a
compared theory along `g`, and `P` a closed class of functors on tests over `A` that contains
`ℤ[Hom(A, -)]` and holds at `ℤ[Y]`, for each functor `Y` on tests over `A`, exactly when
`D.IsFiniteLerayHirsch` holds for `ℤ[Y] / ℤ[offClosedFibre Y]`. If the functor `X` on `k`-algebras
is charted by some `V` (`New.Variety.IsCharting`: `V` is Zariski locally all of `X`, and `ℤ[V]` lies
in every closed class containing `ℤ[Spec R]` for each chart `R` of `X` étale over a torus), then `P`
holds at `ℤ[X]`, restricted to tests over `A`. 

### `maximalIdeal_le_radical_span`

 Let `A` be a valuation ring of `Ω` (a `ClosurePlace`) with the prime `p` in its maximal ideal.
Then `A` has rank one: for every nonzero `a ∈ A`, the maximal ideal lies in the radical of `(a)`. 

### `isBijective_restrict_restrictScalars_iff`

 Let `A` be a valuation ring of `Ω` (a `ClosurePlace`) with the prime `p` in its maximal ideal,
and `ℓ` a unit in `A`. For a functor `X` on tests over `A`, restriction of the mod `ℓ` cohomology
from tests over `A` to tests over `Ω` (`New.Variety.TestOver.restrictScalars`) is bijective on
`ℤ[X]` exactly when `ℤ[X] / ℤ[offClosedFibre X]` has no cohomology. 

### `isTestCohomEquiv_baseChangeTransition`

 Let `ℓ` be prime and `A` a valuation ring of the algebraic closure `Ω` of `ℚ` (a `ClosurePlace`)
and an `R`-algebra, with a prime `p` in its maximal ideal and `ℓ` a unit. Suppose `Y` is charted
over `R` (`IsCharted`: its functor of points on `R`-algebras has a subfunctor `V` with
`IsCharting V`). Then pull-back `Hⁿ(Y_A, ℤ/ℓ) → Hⁿ(Y_Ω, ℤ/ℓ)` along `Y_Ω → Y_A` is bijective for all
`n`, where cohomology is computed on test rings with locally constant coefficients. 
