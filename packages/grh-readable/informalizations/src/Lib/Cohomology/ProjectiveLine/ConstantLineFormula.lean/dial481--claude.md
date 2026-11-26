---
{
  "module": "src/Lib/Cohomology/ProjectiveLine/ConstantLineFormula.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/ProjectiveLine/ConstantLineFormula.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/ProjectiveLine/ConstantLineFormula.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The projective line formula for locally constant ℤ/ℓ coefficients

The projective line formula H(ℙ¹ × S) = H(S) ⊕ η H(S) (`New.Variety.TorsionCoeff.HasLineFormula`) is
proved for the theory `New.Variety.Theory.locallyConstant` of locally constant ℤ/ℓ-valued functions
on tests over an absolutely integrally closed valuation ring A, with ℓ invertible, that embeds into
ℂ_ℓ. Here H is total Ext of functors to abelian groups, η is the degree two class
`New.Variety.TorsionCoeff.cupClass`, and `New.Variety.lerayHirsch θ S` is the Leray–Hirsch map w ↦ Σ
θ_i · w_i of a family θ of classes; θ is a Leray–Hirsch basis at S
(`New.Variety.IsLerayHirschBasis`) when this map is bijective.

* `New.Variety.isLerayHirschBasis_lineBasis_of_basis`: the formula over a flat S follows from any
  family θ that contains η and is a Leray–Hirsch basis over S and over S ⊗ ℤ[ℙ¹].
* `New.Variety.hasLineFormula_of_lerayHirsch_ne_zero`: over a valuation ring A the formula holds as
  soon as η acts non-trivially on the point for one coefficient whose tests lie over the generic
  point of A.
* `New.Variety.hasLineFormula_locallyConstant`: the formula for a valuation ring A with an injective
  ring map to ℂ_ℓ.

The formula is reduced to algebraically closed fields k over A
(`New.Variety.hasUniversalPoints_structurePt`), where a Künneth basis contains η unless η · 1 = 0.
That vanishing would spread to the generic point of A; the tilted theory of
`New.Variety.hasLineFormula_tiltTheory` shows that it does not occur for A in ℂ_ℓ.

Notions from other files:
* `New.Variety.TestOver`: The category of tests over A: the commutative A-algebras that are reduced,
  absolutely integrally closed, and in which any a, b admit an idempotent e with a ∣ eb and
  b ∣ (1 − e)a.
* `New.Variety.TorsionCoeff`: A coefficient along g: a functor to abelian groups, killed by ℓ, with
  Zariski descent; a `New.Variety.Theory` is one that also behaves well on closed loci.
* `New.Variety.projLine`: The projective line as a functor on rings; `New.Variety.onePointFunctor`
  is the constant one-point functor and `New.Variety.reprBy A` the functor Hom(A, −).

## Relation to the literature

Known result: the projective line formula for ℤ/ℓ coefficients, where the degree two class is the
Chern class of O(1) given by the Kummer sequence. Here the formula H(ℙ¹ × S) = H(S) ⊕ η H(S) is
stated in Leray–Hirsch form for locally constant ℤ/ℓ coefficients on test rings; the tilted
coefficients serve only to show that η acts non-trivially. Source: SGA 4½ [Cycle]; SGA 5
(Jouanolou); Milne, Étale Cohomology; Scholze, p-adic Hodge theory for rigid-analytic varieties.


### `isLerayHirschBasis_lineBasis_of_basis`

 The projective line formula over a coefficient `S` with flat values, from a family that contains
η. Let Θ be a theory along g and θ a family of classes on the points of ℙ¹ over g, of degrees `d`,
whose member `θ i` is η (`hθ_eta`). If θ is a Leray–Hirsch basis over `S` (`h_base`) and over
`S ⊗ ℤ[ℙ¹]` (`h_line`), then so is the family (1, η) = `New.Variety.TorsionCoeff.lineBasis`, that
is, the projective line formula holds over `S`. 

### `etaOneClass`

 For a test c over A, the class η · 1 with locally constant ℤ/ℓ coefficients L: η of
`New.Variety.Theory.locallyConstant` on the points of ℙ¹, pulled back along
`New.Variety.oneLocConst` (ℤ → L, 1 ↦ the constant 1) and then to the functor
(B, x ∈ ℙ¹(B)) ↦ Hom(c, B). It lies in H²(ℤ[Hom(c, −)], L) on the points of ℙ¹ over tests over A. 

### `map_etaOneClass`

 Pull-back along a map of tests c → d over A sends `New.Variety.etaOneClass` c to
`New.Variety.etaOneClass` d. 

### `comp_restrict_pull_map`

 Pull a class x back along f, restrict it along φ, pull it back along α and compose with T. The
result is the restriction of x composed with T, pulled back along α followed by the restriction
of f. 

### `comp_pull_etaOneClass_eq_pullbackAlong_oneLocConst`

 Let c be a test over A and u a map from the point to the functor d ↦ Hom(c, g(d)), that is, maps
c → g(d) natural in the object d of C. Let T be a class in total Ext from the locally constant
ℤ/ℓ coefficient to M, both restricted to the points of ℙ¹ over g. Pull `New.Variety.etaOneClass` c
back along u to the points of ℙ¹ over g and compose it with T. The result is T composed with
η = `New.Variety.TorsionCoeff.cupClass` of M, pulled back along `New.Variety.oneLocConst`. 

### `etaOneClass_eq_zero_of_hasUniversalPoints`

 Let c be a test over A and u a map from the point to the functor d ↦ Hom(c, g(d)) that has
universal points for the restriction along g of the locally constant ℤ/ℓ coefficient. Suppose that
this restriction is a coefficient along g (`h_torsion`, `h_descent`) and that its class η, pulled
back along `New.Variety.oneLocConst`, is zero. Then `New.Variety.etaOneClass` c is zero. 

 ### Tests over an algebraically closed field 

### `TestOver.restrictScalars`

 For an A-algebra k that is a field, the restriction of scalars functor from test k-algebras to
test A-algebras. 

### `TestOver.structurePt`

 On test k-algebras B, the map from the point to the functor B ↦ Hom_A(k, B) that picks the
structure map k → B. 

### `hasUniversalPoints_structurePt`

 For an algebraically closed field k over A, restriction of scalars from tests over k to tests
over A compares the point with the functor Hom_A(k, −) in the sense of
`New.Variety.Comparison.HasUniversalPoints`, for locally constant ℤ/ℓ-valued functions: an A-map y :
k → B makes B a test over k, universal for y, and the identity of B is bijective on coefficients. 

 ### A valuation ring as a test over itself 

### `TestOver.ofSelf`

 An absolutely integrally closed valuation ring as a test over itself. 

### `pointMap_ofSelf_bijective`

 A, seen as a test over itself, is initial among tests over A: for every test D over A, the point
map from Hom(A, D) to the one-point set is bijective. 

 ### The projective line formula over a valuation ring 

### `lerayHirsch_lineBasis_single_false_eq_zero_of_etaOneClass_eq_zero`

 If every non-zero element of A is a unit in every test g(d) (so every g(d) lies over the generic
point of A) and `New.Variety.etaOneClass` vanishes at the residue field of A at its generic point
(`residueTest (TestOver.ofSelf A) ⊥`, with A seen as a test over itself), then y · η = 0 over the
points of ℙ¹ for every class y of M on the point; here y · η is the Leray–Hirsch map of (1,
η) = `New.Variety.TorsionCoeff.lineBasis` at (y at `false`, 0). 

### `etaOneClass_residueTest_bot_eq_zero`

 If `New.Variety.etaOneClass` vanishes at a test k over A that is a field, then it vanishes at
the residue field of A at its generic point. 

### `hasLineFormula_of_lerayHirsch_ne_zero`

 Let A be a valuation ring that is an absolutely integrally closed local domain (not a separate
hypothesis: it is derived from the stated instances `PreValuationRing A` and `InvertsPrime A ℓ`)
with ℓ invertible, g a functor to tests over A, and M a coefficient along g. Suppose that (a) every
non-zero element of A is a unit in every test g(d), and (b) some y in total Ext(ℤ[pt], M) has
y · η ≠ 0 over the points of ℙ¹, where η is the degree-2 class of
`New.Variety.TorsionCoeff.lineBasis`. The product y · η is written as the Leray–Hirsch map of the
family (1, η) = `lineBasis` at the family with y at the index `false` and 0 at the other index. Then
the projective line formula holds for locally constant ℤ/ℓ-valued functions on tests over A: 1 and η
form a basis of H(ℙ¹ × S) over H(S) for every S. 

### `hasLineFormula_locallyConstant`

 Let `A` be a valuation ring (`PreValuationRing A`) that is local and absolutely integrally
closed, with ℓ invertible in it (`InvertsPrime A ℓ`), and that has an injective ring map to ℂ_ℓ. A
test over `A` is a commutative `A`-algebra whose underlying ring is a test ring. Then the theory
`Theory.locallyConstant`, which sends a test B over `A` to the locally constant functions Spec
B → ℤ/ℓ, satisfies the projective line formula: `1` and `η` form a basis of H(ℙ¹ × S) over H(S) for
every S. 
