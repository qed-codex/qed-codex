---
{
  "module": "src/Lib/Cohomology/ProjectiveLine/ChernClass.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/ProjectiveLine/ChernClass.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/ProjectiveLine/ChernClass.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tate module, Kummer sequence and the first Chern class of O(1) on the projective line

Let `g` be a functor from `C` to tests over a ring `A`, and let `ℓ` be a prime. The Tate module `𝕋`
of `G_m` along `g` sits in the Kummer sequence. When `A` is local and absolutely integrally closed
and `ℓ` is invertible in `A`, a section `ε` of `𝕋` makes `𝕋` act on every coefficient `M`
(`New.Variety.TorsionCoeff`: killed by `ℓ`, with Zariski descent). On the projective line `ℙ¹`, the
cocycle of `O(1)` and the Kummer class give the first Chern class `η ∈ H²(ℙ¹, 𝕋)`, and the
projective line formula `H(ℙ¹ × S) = H(S) ⊕ η H(S)` is stated as a property of a coefficient.

## Main definitions and results

* `New.Variety.shortExact_kummerSeq`: the Kummer sequence 0 → 𝕋 → Hom(ℚ, G_m) → G_m → 0 is exact.
* `New.Variety.tateGen`, `New.Variety.isCohomEquiv_tensorPoint_tateGen`: a section ε of 𝕋 such that
  S → S ⊗ 𝕋, x ↦ x ⊗ ε, is bijective on Ext(−, F) for S killed by ℓ and F with Zariski descent. Here
  A is local and absolutely integrally closed, and the prime ℓ is invertible in A
  (`New.Variety.InvertsPrime`).
* `New.Variety.TorsionCoeff.tateAction`: the class in Ext⁰(M ⊗ 𝕋, M) inverse to x ↦ x ⊗ ε; it
  commutes with all classes between coefficients (`New.Variety.TorsionCoeff.tateAction_comm`).
* `New.Variety.TorsionCoeff.mulClass`: the product y · ξ of a class y in M with a class ξ in 𝕋,
  natural in M.
* `New.Variety.etaClass`: the class `η ∈ H²(ℙ¹, 𝕋)`, the cocycle class times the Kummer class.
* `New.Variety.TorsionCoeff.etaAt`, `New.Variety.TorsionCoeff.HasLineFormula`: product with `η`;
  `H(ℙ¹ × S) = H(S) ⊕ η H(S)`.

Notions from other files:
* `New.Variety.IsTest`: a test ring A is reduced and absolutely integrally closed, and any a, b ∈ A
  admit an idempotent e with a ∣ eb and b ∣ (1 − e)a.
* `New.Variety.TestOver`: The category of tests over A: the full subcategory of commutative
  A-algebras whose underlying rings are test rings.
* `New.Variety.H`: The group Ext^n(N,F) in the category of functors from C to abelian groups.
* `New.Variety.Cocycle`: A 1-cocycle from F to G: homomorphisms D(f): F(c) → G(d) for f: c → d with
  D(gf) = G(g)D(f) + D(g)F(f). It defines an extension of F by G.

## Relation to the literature

Known; see `Lib.Cohomology.ProjectiveLine.ConstantLineFormula` and
`Lib.PadicComparison.Duality.GoodPairs` for sources.


### `AddMonoidHom.nsmul_comp_mulRight_inv_natCast`

 For an additive map χ from ℚ and a nonzero natural number n, n times the map x ↦ χ(x / n) is
χ. 


## Kummer sequence, Tate module and its action on torsion coefficients

`New.Variety.TotalH N F` is total Ext(N, F), `New.Variety.TotalH.comp` the Yoneda product in diagram
order, and `New.Variety.abTensor` the pointwise tensor product over ℤ.


 ### The Kummer sequence and the Tate module 

### `kummerSeq`

 The Kummer short complex 𝕋 → Hom(ℚ, G_m) → G_m of functors along g, formed by evaluation at
1 and its kernel 𝕋, the Tate module. 

### `tateModule`

 The Tate module 𝕋 of the multiplicative group along g: its value at c is the group of
homomorphisms χ from ℚ to the units of g(c) with χ(1) = 1. It is the first term `X₁` of the
Kummer complex `New.Variety.kummerSeq`, that is, the kernel of evaluation at 1,
Hom(ℚ, G_m) → G_m. A member χ is a compatible system χ(1/n) of n-th roots of unity for all
n ≥ 1, so all primes are included, not only ℓ. 

### `shortExact_kummerSeq`

 Along a functor g to tests over A, the Kummer sequence 0 → 𝕋 → Hom(ℚ, G_m) → G_m → 0, with
last map evaluation at 1, is short exact. 

 ### A generator of the Tate module modulo ℓ 

### `compatibleRootsOfUnity`

 For a prime ℓ invertible in a local, absolutely integrally closed ring A, there is a
homomorphism χ from ℚ to A^× with χ(1) = 1 such that χ(1/ℓ) is a root of the ℓ-th cyclotomic
polynomial. 

### `tateGen`

 The section ε of the Tate module `New.Variety.tateModule` along g, as a map from the constant
functor ℤ (the free abelian group on the one-point functor). At c it is the homomorphism
`New.Variety.compatibleRootsOfUnity` χ: ℚ → Aˣ, with χ(1) = 1 and χ(1/ℓ) a root of the ℓ-th
cyclotomic polynomial, followed by the structure map A → g(c). 

### `tateModule_apply_inv_mem_rootsOfUnity`

 For t in the Tate module at c, the value t(1/ℓ) is an ℓ-th root of unity of the ring g(c):
ℓ • t(1/ℓ) = t(1), which is the unit 1 (written 0, as the group of units is written additively). 

### `tateRoot`

 For a ring map ψ from g(c) to K, the additive map t ↦ ψ(t(1/ℓ)) from the Tate module at c to
the ℓ-th roots of unity of K, written additively. 

### `isPrimitiveRoot_tateRoot_tateGen`

 For a ring map ψ from g(c) to a domain K, the image ψ(ε(1/ℓ)) of the section
ε = `New.Variety.tateGen` is a primitive ℓ-th root of unity. 

### `isCohomEquiv_tensorPoint_tateGen`

 Let A be local and absolutely integrally closed, with the prime ℓ invertible in A. If ℓ kills
every value of S and F satisfies Zariski descent along g (a subfunctor that contains everything near
each maximal ideal of the rings g(c) is dense for F), then the map S → S ⊗ 𝕋, x ↦ x ⊗ ε, induces
bijections on all Ext^n(−, F). Here 𝕋 is the Tate module and ε = `New.Variety.tateGen`. 

 ### The action on coefficients and the product with a class 

### `TorsionCoeff.tateAction`

 The action of the Tate module 𝕋 on a coefficient M: the class in Ext⁰(M ⊗ 𝕋, M) whose
pull-back along x ↦ x ⊗ ε, ε = `New.Variety.tateGen`, is the identity. 

### `TorsionCoeff.pullbackAlong_tensorPoint_tateAction`

 The class `New.Variety.TorsionCoeff.tateAction` of M pulls back along x ↦ x ⊗ ε to the identity
class of M (ε = `New.Variety.tateGen`). 

### `TorsionCoeff.pullbackAlong_tensorPoint_comp_tateAction`

 The generator ε acts as the identity: for a class y in total Ext(S, M), the Yoneda composite of
x ↦ x ⊗ ε, y ⊗ 𝕋 and `New.Variety.TorsionCoeff.tateAction` of M is y (𝕋 the Tate module,
ε = `New.Variety.tateGen`). 

### `TorsionCoeff.tateAction_comm`

 For coefficients K along g and M' along g∘φ, every class T in total Ext(K∘φ, M') commutes
with the actions μ = `New.Variety.TorsionCoeff.tateAction` of the Tate module 𝕋: in diagram
order, μ_K restricted along φ and then T equals T ⊗ 𝕋 and then μ_{M'}. 

### `TorsionCoeff.mulClass`

 The product with a class ξ in total Ext(P, 𝕋), 𝕋 the Tate module `New.Variety.tateModule`. For
S with flat values it is the additive map y ↦ y · ξ from total Ext(S, M) to total Ext(S ⊗ P, M),
where y · ξ is the Yoneda composite S ⊗ P → S ⊗ 𝕋 → M ⊗ 𝕋 → M of S ⊗ ξ, y ⊗ 𝕋 and
`New.Variety.TorsionCoeff.tateAction`. 

### `TorsionCoeff.mulClass_naturality`

 The product is natural in the coefficient. Let φ : C' ⥤ C, K a coefficient along g (an ℓ-torsion
functor with Zariski descent, `TorsionCoeff`) and M' one along φ ⋙ g, and let S have flat values.
Let y be a class in total Ext(S, K), ξ one in total Ext(P, 𝕋) (𝕋 the Tate module) and T one in total
Ext(K∘φ, M'). Restricting the product y · ξ ∈ total Ext(S ⊗ P, K) along φ and composing with T gives
the product of (y restricted, then T) with ξ restricted. 

### `Theory.mulClass_congr_of_eq_on_zeros`

 Let Θ be a theory along g (an ℓ-torsion coefficient F = Θ.functor with Zariski descent that
behaves well on closed loci). Let J be a compatible family of ideals J_c of the rings g(c), and
U = `relFreeAb J.topLocus` (ℤ modulo ℤ[V], V the locus where J is the unit ideal). Let ξ be a class
in Ext²(U, 𝕋), 𝕋 the Tate module. If a, a' : S' → S, between functors with flat values, agree at
every c with J_c = 0, then (a^*y) · ξ = (a' ⊗ U)^*(y · ξ) for every class y in total Ext(S, F). Here
y · ξ in total Ext(S ⊗ U, F) is the Yoneda composite of S ⊗ ξ, y ⊗ 𝕋 and the action of 𝕋 on F. 


## The projective line, the class η and the line formula

The projective line `New.Variety.projLine` sends a ring `B` to the points `(1 + u v : v)`. Along a
ring map the chosen rows change by units, and these units form a cocycle from `ℤ[ℙ¹]` to `𝔾_m`
(`New.Variety.projLine.cocycle`), the cocycle of `O(1)`. For a coefficient `M`, the product with `η`
at a point is `New.Variety.TorsionCoeff.etaAt`; the projective line formula
(`New.Variety.TorsionCoeff.HasLineFormula`) says that `1` and `η` are a basis over the cohomology of
every `S`.

Here `g : C ⥤ TestOver A` is a functor to tests over `A`, `New.Variety.ringOf g` gives the ring of
`g c`, `New.Variety.freeAb` is `Y ↦ ℤ[Y]`, and `New.Variety.H N F n` is `Extⁿ(N, F)` of functors
`C ⥤ Ab`.


 ### The projective line and the cocycle of `O(1)` 

### `projLineSetoid`

 The relation on pairs `(u, v)` whose classes are the points of the projective line. The pair
`(u, v)` stands for the row `(1 + u v, v)`; two pairs are related if the determinant of their rows
is zero. This gives the points `(a : v)` with a representative such that `a ≡ 1 mod v`. 

### `projLine`

 The projective line as a functor (`PointFunctor`) from commutative rings (`CommRingCat`) to
`Type 1`: B goes to the set of points (1 + uv : v) with u, v in B, that is, pairs (u, v) modulo
`New.Variety.projLineSetoid`. 

### `projLinePow`

 The product of copies of the projective line indexed by `ι`. 

### `testOfPoint`

 For a functor of points X, the projection (c, x) ↦ c from pairs of a test c over A and
x ∈ X(c) to tests over A. 

### `projLineAlong`

 The projective line over the tests of `g`. 

### `unimodularRow`

 The homogeneous coordinates `(1 + u v, v)` of a point, for a chosen representative `(u, v)`. 

### `exists_unit_smul_unimodularRow`

 The row `(1 + u v, v)` of a pair `x = (u, v)` is a unit times the row of its point. 

### `eq_and_eq_of_smul_unimodularRow_eq`

 Unit multiples of chosen rows determine both the unit and the point. 

### `rowUnit`

 The unit by which `f` rescales the row of a point (`unimodularRow_map`), extended additively
to the free abelian group on the points. 

### `map_eq_mk_map_out`

 The image under `f` of a point `q` is the class of the image of its chosen representative. 

### `unimodularRow_map`

 The image under `f` of the chosen row of `q` is the unit `New.Variety.projLine.rowUnit` times
the chosen row of the image point of `q`. 

### `add_rowUnit_eq`

 If `f` maps `a` times the row of `q` to `b` times a row, then `b` is the product of `f a` and
the unit `rowUnit f q`. 

### `affinePt`

 The point (x : 1) of the projective line over B. 

### `isUnit_unimodularRow_affinePt_iff`

 The first coordinate of the row of the point `(x : 1)` is a unit exactly when `x` is a unit. 

### `affinePt_eq_map`

 If the image of the row of `q` is proportional to `(x, 1)`, then `q` maps to `(x : 1)`. 

### `isUnit_fst_unimodularRow_map`

 If `f` sends the first coordinate of the row of `q` to a unit, then the row of the image point
also has a unit as first coordinate. 

### `affineChart`

 The complement of `(0 : 1)`: the points whose row has a unit as first coordinate. 

### `basePt`

 The section of the projective line along g whose value at every object c is the base point
(1 : 1) over the ring g(c). 

### `cocycle`

 The 1-cocycle from ℤ[P¹] to G_m along g sending a morphism f and a point q to the transition
unit `New.Variety.projLine.rowUnit` of the chosen rows. 

### `rowDet`

 The determinant `a v' - v a'` of the rows `(a, v)` and `(a', v')` of two points `p`, `p'` of the
projective line. 

### `map_rowDet`

 A ring map `f` sends the determinant of the rows of `p` and `p'` to the value of `rowUnit f` at
`p + p'` times the determinant of the rows of the image points. 

### `eq_iff_unimodularRow_fst_mul_snd_eq`

 Two points of the projective line are equal exactly when their rows have determinant zero. 

 ### The class `η` 

### `etaClass`

 The class `η` in `Ext²(ℤ[ℙ¹], T)`, with `T` the Tate module: the product of the extension class
of the cocycle of `O(1)` and the extension class of the Kummer sequence. 

 ### The product with `η` on a coefficient, and the line formula 

### `TorsionCoeff.etaTensor`

 A family of classes in `Ext²(S ⊗ ℤ[ℙ¹], S ⊗ T)`, with `T` the Tate module, one for each functor
`φ` to tests over `A` and each functor `S` from `D` to abelian groups, not only torsion
coefficients. It is chosen by `exists_isTensorClass` for the class `η` on the category of all tests
over `A`. 

### `TorsionCoeff.isTensorClass_etaTensor`

 The family `etaTensor` tensors the class `η` on the category of all tests over `A` with every
coefficient. 

### `etaTensorClass`

 The class `S ⊗ η` in `Ext²(S ⊗ ℤ[ℙ¹], S ⊗ T)`, defined for every coefficient `S`, flat or not.
It is used through `etaTensorClass_naturality`, `etaTensorClass_of_hasFlatValues` and
`map_restrictAlong_etaTensorClass`. 

### `etaTensorClass_naturality`

 The class `etaTensorClass g S` is natural in the coefficient `S`, for classes of every
degree. 

### `map_restrictAlong_etaTensorClass`

 The class `etaTensorClass g S` is compatible with restriction along a functor `φ`. 

### `freeAbSectionMap`

 A section `q` of `Y` as a map `ℤ[pt] ⟶ ℤ[Y]`. 

### `map_restrictAlong_etaClass`

 The class `η` is compatible with restriction along a functor `φ`. 

### `etaTensorClass_of_hasFlatValues`

 If `S` has flat values, then `etaTensorClass g S` is the image of `η` under the exact functor
`S ⊗ -`. 

### `map_etaClass_eq_zero_of_coboundary`

 If the cocycle of `O(1)`, pulled back along `b`, is the coboundary of a family of units `u`,
then `η` pulls back to zero along `b`. 

### `pullbackAlong_etaClass_eq_zero_of_isUnit`

 The class `η` pulls back to zero along a map `b` into the affine chart, where the first
coordinate of the row is a unit. 

### `exists_etaClass_supported_diagonal`

 For sections `q`, `q'` of the projective line along `g`, the pullback of `η ∈ Ext²(ℤ[ℙ¹], T)`
(`T` the Tate module) along `q + q'` is supported where `q = q'`. That is, there is a family of
ideals `J` such that `q` and `q'` agree where `J` is zero, and the class comes from a class `ξ`
relative to the locus where `J` is the unit ideal. 

### `mapThenComp_eq_comp_map`

 `mapThenComp Φ u x` is `Φ x` followed by `u`. 

### `etaAt`

 The product with `η` at `b : ℤ[pt] ⟶ ℤ[ℙ¹]`, an additive map in `b`: the class in `Ext²(M, M)`
of the composite `M → M ⊗ ℤ[ℙ¹] → (M ⊗ T)[2] → M[2]` of `x ↦ x ⊗ b` (`tensorPoint b`), of `M ⊗ η`
(`etaTensorClass`) and of the action `M.tateAction` of the Tate module `T`. 

### `toTotalH_etaAt`

 As a total class, `M.etaAt b` is the pullback along `x ↦ x ⊗ b` of the product of `M ⊗ η` and
`M.tateAction`. 

### `comp_etaAt`

 The product of a class `y` from `S` to `M` with `M.etaAt b` is the composite of `x ↦ x ⊗ b`,
`S ⊗ η`, `y ⊗ T` and the action `M.tateAction`. 

### `etaAt_naturality`

 Let `K` be a coefficient along `g`, `M'` one along `φ ⋙ g`, and `T` (not the Tate module) a
class of any degree in total Ext from `K` restricted along `φ` to `M'`. Then `T` commutes with the
product with `η` at `b`: restricting `K.etaAt b` along `φ` and composing with `T` is `T` followed by
`M'.etaAt` at `b` restricted. 

### `pullbackAlong_tensorPoint_mulClass`

 Pulling `M.mulClass ζ y` back along `x ↦ x ⊗ σ` equals pulling `M.mulClass (σ^* ζ) y` back along
`x ↦ x ⊗ 1`, where `σ^* ζ` is `ζ` pulled back along `σ`. 

### `mulClass_eq_comp_etaAt`

 Let `S` have flat values. If `ξ` pulled back along `ρ` is `η` pulled back along `b`, then the
product `M.mulClass ξ y` of `y` with `ξ`, pulled back along `x ↦ x ⊗ ρ`, is the product of `y`
with `M.etaAt b`. 

### `comp_etaAt_basePt`

 For `S` with flat values, the product of every class `y` from `S` to `M` with `η` at the base
point of the line is zero. 

### `cupClass`

 The product with `η` on the category of points of the line: `etaAt` at the tautological
point. 

### `lineDegree`

 The degrees of the classes `1` (index `true`) and `η` (index `false`). 

### `lineBasis`

 The two classes `1` (index `true`, degree 0) and `η` (index `false`, degree 2) on the category
of points of the line. 

### `HasLineFormula`

 The projective line formula `H(ℙ¹ × S) = H(S) ⊕ η H(S)`: the classes `1` and `η` are a basis
over the cohomology of every `S`. 

### `map_etaAt_onElements`

 Restricting `M.etaAt b` to the category of points of `X` gives `etaAt` of the restrictions. 
