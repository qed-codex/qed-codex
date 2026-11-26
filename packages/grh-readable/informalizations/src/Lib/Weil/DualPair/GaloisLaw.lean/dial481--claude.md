---
{
  "module": "src/Lib/Weil/DualPair/GaloisLaw.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/GaloisLaw.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/GaloisLaw.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Semilinear maps intertwining the Weil action up to σΔ/Δ

This file gives an abstract form of the Galois law for the Weil representation. A map `L` on the
data `𝒮 V` that is semilinear along `σ : ℂ →+* ℂ` may keep the finite part and turn the finite
Heisenberg translation by `x` into that by `b x`, where `σ` takes `ψ z` to `ψ (b b̄ z)` for the
additive character `ψ = New.stdLattice.selfDualAddChar E` of the finite adeles. Such a map also
intertwines the Weil action, on the finite part and for finite points, up to the factor σ(Δ_f)/Δ_f,
with Δ_f the finite multiplier `New.finMultiplier`. Writing `b = u a` with `u` unitary and `a` a
unit of `Ô`, the laws are first proved for `ω(u)⁻¹ L`, which scales translations by `a`. Finite
vectors are read through `finVec x = (0, α x)`, with `α` the idele of the Weil data.

## Main definitions and results

* `New.Space.ScalesTranslations`: the property of a `σ`-semilinear map to keep the finite part and
  to turn the finite translation by `x` into that by `b x`, while `σ` takes `selfDualAddChar E z` to
  `selfDualAddChar E (b b̄ z)`; `New.Space.ScalesTranslations.map_omega` is its law for `ω`, and
  `New.Space.ScalesTranslations.exists_map_schrodingerOp` its law for the vacuum and for the vectors
  `V.schrodingerOp R Ψ V.vacElem` with `Ψ` Schwartz–Bruhat at a set `R` of finite places.
* `New.multiplierRatio`: The factor `σ (Δ g) / Δ g`, for the multiplier `Δ = New.finMultiplier` of a
  finite unitary point `g`.

Notions from other files:
* `New.Space.ϱ`, `New.Space.ω`, `New.Space.vacElem`: The Heisenberg operators, the Weil
  representation and the vacuum vector of the space of data `New.𝒮 V`.
* `New.scalarFin` (`Lib.Weil.DualPair.FiniteAction`): the scalar matrices, as a homomorphism from
  the finite adeles of norm one to `Gf E n`.

## Relation to the literature

Known result: Galois action on CM theta functions and on the finite Weil representation. Here it is
stated for semilinear maps on the finite part of the data that scale the Heisenberg translations,
with an explicit factor; such a map is built from Taylor series of theta functions in
`New.UpperBound.Kernels.JetConjugatesAndBounds`. Source: G. Shimura, Theta functions with complex
multiplication, Duke Math. J. 43 (1976) 673-696; for the rationality of the Weil representation, J.
Trias, On the rationality of the Weil representation and the local theta correspondence, arXiv
2601.16141.


 ### The factor σΔ/Δ 

### `multiplierRatio`

 The factor `σ (Δ g) / Δ g`, for the multiplier `Δ = New.finMultiplier` of a finite unitary point
`g`. 

### `map_finMultiplier_mul_conj`

 An embedding `σ` of `ℂ` into itself fixes the product of the finite multiplier `Δ g` and its
conjugate, which is a natural number. 

### `multiplierRatio_sq`

 Let E be a CM field with Weil data, σ a ring endomorphism of ℂ, and g a point of the finite
adelic unitary group `Gf E n`. Then the square of `multiplierRatio σ g` = σ(Δ g)/Δ g, where
Δ = `New.finMultiplier` is the multiplier of g, equals υ(det g)/σ(υ(det g)). Here `detFin 1 g` is
the determinant of g as a norm-one adele (that of (1, g) in G, all signs being 1), and
υ = `upsilonU1` is the splitting character of the Weil data restricted to norm-one ideles. 

### `map_finMultiplier_div_norm_sq`

 As `σ` fixes the natural number `‖Δ g‖ ^ 2`, it takes `Δ g / ‖Δ g‖ ^ 2`, the constant in the
expansion of `ω(g) vacElem` into translates, to `σ (Δ g) / Δ g` (`multiplierRatio`) times itself.
Here `Δ = finMultiplier` is the multiplier of the Weil action at finite points. 

 ### The scale is a unitary adele times a unit 

### `v_eq_one_of_map_selfDualAddChar`

 Let `selfDualAddChar` be the additive character of the finite adeles for which `Ô` is self-dual.
If a ring endomorphism `σ` of `ℂ` takes `selfDualAddChar z` to `selfDualAddChar (t z)` for all `z`,
then `t` is a unit at every finite place. 

### `exists_unitary_mul_unit`

 If `R ∩ R̄ = ∅` and `b b̄` is a unit at every finite place, then `b` is the product of an adele
of norm one and a unit `a` of the ring `Ô` of integral finite adeles that equals 1 at the places of
`R` (`idem R` is the idempotent adele that is 1 exactly at `R`). 

 ### Maps that scale finite translations 

### `Space.finsum_finHeisenbergOp_unit_smul`

 Let `Λ = stdLattice E n`. A unit `a` of the ring `Ô` of integral finite adeles permutes the
cosets of `Λ ∩ g⁻¹ Λ` in `Λ`. Hence it does not change the sum of the translates of the vacuum by
`g q` (`finHeisenbergOp` is the normalised finite Heisenberg operator), `q` running over these
cosets; this sum is `ω(g) vacElem` up to a scalar (`New.Space.omega_vacElem_sum`). 

### `Space.ScalesTranslations`

 The `σ`-semilinear map `L` on the data of `V` scales finite translations by the finite adele
`b`: it keeps the finite part, spanned by the translates of the vacuum, and turns the translation by
`x` into that by `b x` there, and `σ` acts on the additive character `selfDualAddChar` as
multiplication by `b b̄` does. 

### `Space.ScalesTranslations.map_selfDualAddChar`

 `σ` takes `selfDualAddChar z` to `selfDualAddChar (b b̄ z)`. 

### `Space.ScalesTranslations.map_mem`

 `L` maps the finite part to itself. 

### `Space.ScalesTranslations.map_rho`

 On the finite part, `L ϱ(x) = ϱ(b x) L` for the finite vectors `finVec x`. 

### `map_finHeisenbergOp`

 Suppose the `σ`-semilinear map `L` on 𝒮(V) scales finite translations by `b`: it keeps the
finite part (the span of the translates of the vacuum under the finite Heisenberg operators), turns
the translation by `x` into that by `b x` there, and `σ` acts on `selfDualAddChar` as multiplication
by `b b̄` does. Then for `f` in the finite part, `L (finHeisenbergOp x f) = finHeisenbergOp (b x) (L
f)`, because `σ` takes the phase `semichar x` to `semichar (b x)`. Here `finHeisenbergOp x` is
`semichar x • ϱ (finVec x)`, with the phase `semichar x` = ψ(c₀ x*x / 2), c₀ = `traceOneAdele`. 

### `omega_inv_comp`

 Let `L` be a `σ`-semilinear map on `𝒮 V` that scales finite translations by `u a`, where `a` is
a finite adele and `u` a finite adele of norm one. This means L keeps the finite part spanned by the
translates of the vacuum, turns the translation by x there into the translation by `u a x`, and σ
acts on `selfDualAddChar` as multiplication by (ua)(ua)‾ does. Then `ω(1, u⁻¹) ∘ L` scales finite
translations by `a`, where `ω` is the Weil representation and `scalarFin n u` is the scalar matrix u
in `Gf E n`. 

### `exists_map_vacElem_of_unit`

 If `L` scales finite translations by a unit of the ring `Ô` of integral finite adeles, it sends
the vacuum vector `vacElem` to a multiple of itself. 

### `map_omega_of_unit`

 If `L` scales finite translations by a unit of `Ô`, then `L ω(g) = (σ (Δ g) / Δ g) ω(g) L` on
the finite part, the span of the translates of the vacuum. Here `Δ = finMultiplier` is the
multiplier of the Weil representation `ω`, and `multiplierRatio σ g` is this factor. 

### `_root_.New.map_schrodingerAct_boxIndicator`

 Let `σ` take `selfDualAddChar z` to `selfDualAddChar (a ā z)`, where `a` is `1` on the set `R`
of places. Then `σ` takes the translate by `y` of the box function above `R` to its translate by
`a y`. Here `schrodingerAct R y` is the translation in the Schrödinger model at `R`,
`boxIndicator n R` the indicator of the vectors integral at `R`, and `idem R` the adele that is `1`
exactly at `R`. 

### `map_schrodingerOp_of_map_vacElem`

 Let `L` scale finite translations by an adele `a` that is `1` on a set `R` of places disjoint
from its conjugate, and let `L vacElem = c vacElem`, `vacElem` being the vacuum vector. Then
`L (Ψ ⊗ vacElem) = c ((σ ∘ Ψ) ⊗ vacElem)` for `Ψ` Schwartz–Bruhat at the places of `R`. Here
`Ψ ⊗` is `V.schrodingerOp R Ψ`, the operator on data with component `Ψ` at these places. 

### `exists_eq_unitary_mul_unit`

 For `R` disjoint from its conjugate, the scale `b` is a unitary adele times a unit of `Ô` that
is `1` on `R`. 

### `isUnit`

 Suppose the `σ`-semilinear map `L` on 𝒮(V) scales finite translations by the finite adele `b`:
it keeps the finite part spanned by the translates of the vacuum, turns the translation by `x` into
that by `b x` there, and `σ` acts on `selfDualAddChar` as multiplication by `b b̄` does. Then `b` is
a unit of the finite adeles. 

### `map_omega`

 Let `L` be a `σ`-semilinear map on the data of `V` that scales finite translations by the finite
adele `b`: it preserves the finite part (spanned by the translates of the vacuum), turns translation
by `x` into translation by `b x` there, and `σ` acts on `selfDualAddChar` as multiplication by
`b b̄` does. Then for a finite point `g` and `f` in the finite part,
`L (ω(1, g) f) = (σ (Δ g) / Δ g) • ω(1, g) (L f)`, where `Δ = finMultiplier` is the multiplier of
the Weil representation. This is the Galois law for the finite Weil representation. 

### `exists_map_schrodingerOp`

 Let `L` be `σ`-semilinear and scale finite translations, and let `R` be a set of places disjoint
from its conjugate. There are a number `c` and a unitary adele `u`, acting as a scalar matrix, with
`L vacElem = c ω(u) vacElem` and `L (Ψ ⊗ vacElem) = c ω(u) ((σ ∘ Ψ) ⊗ vacElem)` for all `Ψ`
Schwartz–Bruhat above `R`, where `Ψ ⊗` is `V.schrodingerOp R Ψ`. 
