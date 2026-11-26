---
{
  "module": "src/Lib/Cohomology/ProjectiveLine/PerfectLine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/ProjectiveLine/PerfectLine.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/ProjectiveLine/PerfectLine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The perfect projective line glued from two perfect discs has the cohomology of a point

The perfect projective line on p-adic tests S is a model on which classes on ℙ¹ are computed. Its
two discs are represented in the tilt S^♭ by O^♭[ℚ≥0], and its torus by O^♭[ℚ].

* `New.Variety.PerfectLine.gluing`: the gluing map ℤ[torus ⊔ point] → ℤ[two discs]; it is injective
  (a monomorphism). Its cokernel plays the role of the perfect line with the point ∞ killed.
* `New.Variety.PerfectLine.oneSub_comp_gluing`: the operators 1 − (T^s ↦ χ(s) T^s) commute with the
  gluing map.
* `New.Variety.PerfectLine.isCohomEquiv_gluing_tilt`,
  `New.Variety.PerfectLine.isCohomEquiv_gluing_generic`: over each test c the gluing map induces
  bijections on cohomology. This holds for coefficients G(S^♭), where G is built from an O^♭-module
  N and is assumed acyclic on perfect rings. It also holds for S[1/p].
* `New.Variety.PerfectLine.subsingleton_H_cokernel_gluing`: then M ⊗ cokernel has no cohomology, for
  every M with flat values.

Idea: all cohomology is in degree 0, where the map is the splitting of a Laurent polynomial into two
parts according to the sign of the exponent. `New.Period.OFlat` is O^♭, the tilt of the ring of
integers O_C of ℂ_p.

Notions from other files:
* `New.Variety.PadicTest`: A p-adic test: a non-empty family of cells (`New.Variety.IsCell`) with a
  ring map from O_C to their product.
* `New.Variety.freeAb`: The functor sending a set-valued functor Y to Z[Y], whose value at A is the
  free abelian group on Y(A). ℤ[Y] has flat base change (`HasFlatBaseChange`) when tensoring by a
  flat module M commutes with its cohomology with module coefficients.

## Relation to the literature

Known; see `Lib.Cohomology.ProjectiveLine.ConstantLineFormula` for sources.


### `instance {C : Type 1} [Category C] {F A : AbFunctor C} [HasFlatValues F] [HasFlatValues A] : HasFlatValues (abTensor F A)`

 The objectwise tensor product of two functors with flat values has flat values. 

 ### The discs, the torus and the gluing map 

### `monoidAlg`

 For an additive commutative monoid S, the monoid algebra O^♭[S], as a commutative
O^♭-algebra. 

### `charTwist`

 For a character χ of ℚ with values in O^♭ and an additive map f: S → ℚ, the O^♭-algebra
endomorphism T^s ↦ χ(f(s)) T^s of O^♭[S]. 

### `discToTorus`

 For an additive map g: ℚ≥0 → ℚ, the map of monoid algebras O^♭[ℚ≥0] → O^♭[ℚ] over O^♭
sending T^a to T^{g(a)}. 

### `evalZero`

 Evaluation at T = 0: the O^♭-algebra map from O^♭[ℚ_{≥0}] to b sending T^0 to 1 and T^a to 0
for a > 0. 

### `pointOrTorus`

 The family of two `O^♭`-algebras: the ring `O^♭[ℚ]` of the perfect torus at the index `true`,
and the ring `O^♭` of a point at the index `false`. 

### `tiltPointsSum`

 For O^♭-algebras B_i indexed by Bool and an endofunctor ψ of O^♭-algebras (default the
identity), the functor S ↦ ⊔_i Hom(ψ(B_i), S^♭) on p-adic tests. 

### `twoDiscs`

 Two affine lines with all roots of the coordinate: for an endofunctor ψ of O^♭-algebras (default
the identity), the disjoint union of two copies of the functor of points of ψ(O^♭[ℚ_{≥0}]) in the
tilts of p-adic tests. 

### `gluing`

 The map ℤ[torus ⊔ point] → ℤ[two discs] sending a point t of the torus to t⁻¹ in the disc
`false` minus t in the disc `true`, and the point to the origin of the disc `false`. 

 ### Origins, the operator 1 − Δ, and injectivity of the gluing map 

### `origin`

 For a set-valued functor X on p-adic tests (by default the point), the morphism
ℤ[X] → ℤ[two discs] sending every point to the origin T = 0 of the disc with index a. 

### `projFirst`

 The map ℤ[Hom(B_true, S^♭) ⊔ Hom(B_false, S^♭)] → ℤ[Hom(B_true, S^♭)] that keeps the points
of the first part and sends those of the second to 0. 

### `oneSub`

 For endomorphisms Δ_b of the O^♭-algebras B_b, the endomorphism 1 − Δ of the functor S ↦
ℤ[⊔_b Hom(B_b, S^♭)], sending [x] to [x] − [x∘Δ_b]. 

### `charTwist_comp_discToTorus`

 For an additive map `g : ℚ≥0 → ℚ`, twisting `O^♭[ℚ≥0]` by `χ ∘ g` and then sending `T^a` to
`T^{g(a)}` is the same as first sending `T^a` to `T^{g(a)}` and then twisting `O^♭[ℚ]` by `χ`. 

### `pointOrTorusTwist`

 The endomorphism `T^s ↦ χ(s) T^s` of the ring of the torus, and the identity of the ring of
the point. 

### `discTwist`

 The endomorphism `T^s ↦ χ(s) T^s` of the ring of the disc `true`, and `T^s ↦ χ(-s) T^s` of
the ring of the disc `false`. 

### `discTwist_comp_evalZero`

 The twist of either disc fixes the evaluation at `T = 0`. 

### `oneSub_comp_gluing`

 The gluing map commutes with the operators `1 - Δ`, where `Δ` is the twist by `χ` on the
torus and on the two discs, and the identity on the point. 

### `of_mabs_eq_single_nnabs`

 In `O^♭[ℚ]`, the monomial of the absolute value `mabs s` is `T^t` for the rational
`t = s.nnabs`. 

### `instance : Mono gluing`

 The gluing map is a monomorphism: on each test it has a retraction. 

### `perfectRing_tensorLeft_tilt`

 For a test `c` and a perfect `O^♭`-algebra `b`, the algebra `c^♭ ⊗ b` is a perfect ring. 

### `subsingleton_H_freeAb_tiltPointsSum`

 If the coefficient functor `G = – ⊗ N` is acyclic on perfect `O^♭`-algebras (for b perfect,
Hom(b, –^♭) has cohomology G(b) in degree 0 and none above), then `ℤ[⊔_b Hom(ψ(B_b), –^♭)]` has no
cohomology in positive degree with coefficients in `S ↦ G(S^♭)`, for `O^♭`-algebras `B_b` indexed by
`Bool` and an endofunctor `ψ` with the `ψ(B_b)` perfect. 

### `hasFlatBaseChange_freeAb_tiltPointsSum`

 For `O^♭`-algebras `B_b` indexed by `Bool` and an endofunctor `ψ` of `O^♭`-algebras such that
the `ψ(B_b)` are perfect rings, the functor `ℤ[⊔_b Hom(ψ(B_b), –^♭)]` has flat base change. 

### `pairProj`

 The projection of a pair `(y₀, y₁)` of elements of `O^♭[ℚ≥0]` to `y₀` (for `false`) or to
`y₁` (for `true`). 

### `glueLinear`

 The `O^♭`-linear maps that describe the gluing map in degree `0`. A pair `(y₀, y₁)` of
elements of `O^♭[ℚ≥0]` goes to the value `y₀(0)` in the ring `O^♭` of the point, and to
`y₀(T⁻¹) - y₁(T)` in the ring `O^♭[ℚ]` of the torus. 

### `bijective_glueLinear`

 The map `(y₀, y₁) ↦ (y₀(0), y₀(T⁻¹) - y₁(T))` from pairs of elements of `O^♭[ℚ≥0]` to pairs
in `O^♭ × O^♭[ℚ]` is bijective. 

### `hasFlatBaseChange_freeAb_twoDiscs`

 For a test `c`, the target `ℤ[two discs]` of the gluing map formed with the algebras `c^♭ ⊗ B`
has flat base change. 

### `hasFlatBaseChange_freeAb_tiltPointsSum_pointOrTorus`

 For a test `c`, the source `ℤ[torus ⊔ point]` of the gluing map formed with the algebras
`c^♭ ⊗ B` has flat base change. 

### `isCohomEquiv_tensorCoeff_gluing`

 Let `G` be the coefficient functor `b ↦ b ⊗ N` on `O^♭`-algebras, and assume it is acyclic on
perfect algebras: for every perfect `O^♭`-algebra b, the functor S ↦ Hom(b, S^♭) on p-adic tests has
cohomology `G(b)` in degree 0 with coefficients S ↦ G(S^♭). Then for every p-adic test `c`, the
gluing map ℤ[torus ⊔ point] → ℤ[two discs] is an equivalence for the coefficients S ↦ G(S^♭), that
is, it induces bijections on all Extⁿ. Here the discs are the points of c^♭ ⊗ O^♭[ℚ≥0] in tilts, and
the map sends t to t⁻¹ in disc `false` minus t in disc `true`, and the point to the origin of disc
`false`. 

### `isCohomEquiv_gluing_tilt`

 Let `G` be the coefficient functor `b ↦ b ⊗ N` on `O^♭`-algebras, acyclic on perfect
`O^♭`-algebras, and form the gluing map with the algebras `c^♭ ⊗ B`. Its target and its source have
flat base change, and it induces bijections on cohomology with coefficients in `S ↦ G(S^♭)`. 

### `isCohomEquiv_gluing_generic`

 For every test `c`, the gluing map formed with the algebras `c^♭ ⊗ B` induces bijections on
cohomology with coefficients in `genericCoeff`, the coefficients S ↦ S[1/p]. 

### `subsingleton_H_cokernel_gluing`

 The perfect projective line has the cohomology of a point. For an endofunctor ψ of
`O^♭`-algebras, `gluing ψ` is the map ℤ[torus ⊔ point] → ℤ[two discs] of functors on p-adic tests,
where the discs are the points of ψ(O^♭[ℚ≥0]) in tilts; it sends t in the torus to t⁻¹ in the disc
`false` minus t in the disc `true`, and the point to the origin of the disc `false`, so its cokernel
for ψ = id is the perfect line with a point collapsed. Suppose that for every p-adic test `c` the
gluing with ψ = c^♭ ⊗ − induces bijections Extⁿ(ℤ[two discs], F) → Extⁿ(ℤ[torus ⊔ point], F) for all
n; then for every `S` whose values are flat ℤ-modules, every Extⁿ(S ⊗ coker gluing, F) is zero. 
