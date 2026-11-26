---
{
  "module": "src/Lib/Weil/Periods/Equivariant.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Equivariant.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Equivariant.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The character `ψ_U` and the function `𝒲_φ`

Let `Y` be a grading of the hermitian space `V` (`New.Grading`): a splitting of its basis into a
set `X` and a string of `s` vectors. It gives the Bessel group `R = U ⋊ H`
(`New.Grading.besselGroup`). Here `U` (`New.Grading.unipotent`) is the group of points whose matrix
in rational coordinates, minus `1`, raises grades, and `H` is the unitary group of the standard
definite space on `X`, embedded by `New.Grading.inclX`. Write `U^{≥2}` for the points whose matrix
minus `1` raises grades by at least `2`.

This file defines the projection `R → H` (`New.Grading.leviPart`) and the function
`ψ_U (u) = ψ (½ ȷ tr (𝔢 u))` (`New.Grading.unipotentChar`). It shows that `ψ_U` is a character on
`U^{≥2}(𝔸)`, trivial on rational points and invariant under conjugation by `H(𝔸)`. It defines
`ψ_U`-equivariant functions on `[R]` (`New.Grading.IsEquivariant`) and the function `𝒲_φ`
(`New.Grading.sourceFn`) of an algebraic form `φ`. It shows that `𝒲_φ` is `ψ_U`-equivariant when `s`
is odd, since then `U = U^{≥2}`, and that it is the only such function with its values on `H`.

Notions from other files:
* `New.Grading.gradeOf`: the grade of a basis index, `0` on `X` and `s - 1 - 2 i` on the string
  vector `i`.
* `New.HasDegreeGe w' w d x`: the matrix `x` raises grades by at least `d`, that is `x b a = 0`
  whenever `w' b < w a + d`.
* `New.Grading.shift`: the rational endomorphism `𝔢` of `V` that sends each string vector to a
  multiple of the next one and kills `X` and the last string vector.
* `New.algFormCoeff 1 t φ`: the function `h ↦ t (conjWeylRep κ e h_∞⁻¹ (φ h_fin))` on `H(𝔸)` of an
  algebraic form `φ` and a linear functional `t` on its values.

## Relation to the literature

Known; see `Lib.Weil.Periods.Unfolding` for sources.


 ### The factor in `H` of an element of `R = U ⋊ H` 

### `leviPart`

 The factor `h ∈ H` of an element `u h` of `R = U ⋊ H`: the continuous homomorphism `R → H`
given by `New.Grading.exists_besselGroup_proj`, a retraction of `New.Grading.inclX` with kernel
`U`. 

### `leviPart_inclX`

 The projection `R → H` is a retraction of the inclusion of `H`. 

### `leviPart_eq_one_iff`

 The kernel of the projection `R → H` is `U`. 

### `leviPart_mem_Gamma`

 The projection `R → H` sends rational points to rational points. 

### `leviPart_mul_inclX`

 For `u ∈ U` and `a ∈ H`, the factor in `H` of `u a` is `a`. 

### `mk_one_snd_mem_unipotent`

 If `u` lies in `U`, so does its finite part `(1, u_fin)`. 

### `inclX_mk_one_snd`

 The inclusion of `H` sends the finite part `(1, a_fin)` of `a` to the finite part of the
inclusion of `a`. 

### `leviPart_snd_eq_one`

 The factor in `H` of a real point of `R` (a point with finite part `1`) is a real point. 

 ### The character `ψ_U` 

### `degreePart`

 The part of degree `d` of a matrix on the basis of `V`: it keeps the entries `(b, a)` with
`gradeOf b = gradeOf a + d` and replaces the others by `0`. 

### `degreePart_eq_zero`

 A matrix that raises grades by at least `d'` has no part of degree `d < d'`. 

### `degreePart_two_ratCoordMatrix_mul`

 On `U^{≥2}` the part of degree `2` of the matrix in rational coordinates is additive:
`(u u')₂ = u₂ + u'₂`, because `(u - 1) (u' - 1)` raises grades by at least `4`. 

### `shift_apply_eq_zero`

 The shift `𝔢` lowers grades by `2`: its entry `(a, b)` vanishes unless
`gradeOf b = gradeOf a + 2`. 

### `trace_shift_mul`

 Let `𝔢 = Y.shift` be the matrix that kills `X` and the last string vector and sends each string
vector to a multiple of the next one, so that it lowers grades by `2`. Then for every adelic matrix
`A` on the basis of `V`, `tr (𝔢 A) = tr (𝔢 A₂)`, where `A₂ = Y.degreePart 2 A` keeps only the
entries `(b, a)` with `gradeOf b = gradeOf a + 2`. 

### `commute_shift_ratCoordMatrix_inclX`

 The matrix in rational coordinates of a point of `H` commutes with the shift `𝔢`. 

### `hasDegreeGe_conj`

 Conjugation by an element `r` of `R` keeps the property that the matrix of `u`, minus `1`,
raises grades by at least `d`. 

### `unipotentChar`

 The function `ψ_U (u) = ψ (½ ȷ tr (𝔢 u))` on `G`, where `ψ` is the standard additive character,
`ȷ` is the element of the Weil data, `𝔢 = Y.shift`, and `u` stands for its matrix in rational
coordinates. 

### `unipotentChar_mul`

 For a grading `Y` presenting `V` as `X ⊕ J_s`, and Weil data on `E`, consider
`ψ_U (u) = ψ (½ ȷ tr (𝔢 u))` (`Y.unipotentChar`, with `𝔢 = Y.shift` and `u` taken as its matrix in
rational coordinates). This function is multiplicative on elements `u` of `G` for which `u - 1`
raises grades by at least `2`: `ψ_U (u u') = ψ_U (u) ψ_U (u')`. So on `U^{≥2}(𝔸)` the function `ψ_U`
is a character. 

### `unipotentChar_of_mem_Gamma`

 For a grading `Y` presenting `V` as `X ⊕ J_s`, and Weil data on `E`, the function
`ψ_U (u) = ψ (½ ȷ tr (𝔢 u))` (`Y.unipotentChar`, with `𝔢 = Y.shift`) equals `1` at every rational
point `u ∈ V.Γ` of `G`, not only on the unipotent part. 

### `unipotentChar_conj`

 The function `ψ_U` is invariant under conjugation by `H(𝔸)`. 

 ### Equivariant functions and the function `𝒲_φ` 

### `IsEquivariant`

 A function `W` on `R(𝔸)` is `ψ_U`-equivariant if it is continuous, left invariant under `R(F)`
(a function on `[R] = R(F) \ R(𝔸)`), and `W (u r) = ψ_U (u) W (r)` for `u ∈ U^{≥2}(𝔸)`. 

### `IsEquivariant.continuous`

 The function is continuous. 

### `IsEquivariant.rat_mul`

 The function is left invariant under `R(F)`. 

### `IsEquivariant.unipotent_mul`

 The function transforms by `ψ_U` under `U^{≥2}(𝔸)`. 

### `sourceFn`

 The function `𝒲_φ (u h) = ψ_U (u) (φ (h_fin), π_X (h_∞) v_*)` on `R(𝔸)`. The vector `v_*` enters
through the linear form `t = (·, v_*)`. The values of `φ` transform under `ȟ = ᵗh⁻¹`
(`conjWeylRep`), and `(ȟ ζ, π_X (h) v) = (ζ, v)`, so the second factor is `t (ȟ_∞⁻¹ φ (h_fin))`,
which is `algFormCoeff 1 t φ h`. 

### `sourceFn_mul`

 Let `u` lie in the unipotent subgroup `U = Y.unipotent`, and let `a` lie in `H`, the adelic
unitary group of the standard definite space on `X`, embedded by `inclX`. Then the source function
`𝒲_φ = Y.sourceFn t φ` of the algebraic form `φ` satisfies
`𝒲_φ (u a) = ψ_U (u) · algFormCoeff 1 t φ a`, where `ψ_U = Y.unipotentChar` and the second factor is
`t (ρ(a_∞⁻¹) φ(a_fin))` with `ρ = conjWeylRep`. For `t = (·, v_*)` this is the formula
`𝒲_φ (u a) = ψ_U (u) (φ (a_fin), π_X (a_∞) v_*)`. 

### `sourceFn_gramForm_mul_inclX`

 This is the case `t = gramForm v` of `New.Grading.sourceFn_mul`, where `v` stands for the
complex conjugate of `v_*` and `gramForm` is the Gram pairing `(ξ, η) ↦ ξ* G η`. Let `u` lie in the
unipotent subgroup `Y.unipotent`, and let `a` lie in the adelic unitary group of the standard
definite space on `X`, embedded by `inclX`. Then the source function of the algebraic form `φ`
satisfies `Y.sourceFn (gramForm v) φ (u a) = ψ_U (u) · gramForm (conjWeylRep κ e a.1 v) (φ.1 a.2)`,
where `a.1` is the infinite (real) part of `a` and `a.2` is its finite part. 

### `sourceFn_inclX`

 On `H`, the function `𝒲_φ` is the coefficient function `algFormCoeff 1 t φ` of `φ`. 

### `algFormRep_apply`

 The algebraic form `algFormRep κ e a φ` is the right translate `g ↦ φ (g a)`. 

### `sourceFn_mul_inclX`

 Right translation of `𝒲_φ` by a finite point of `H` is right translation of `φ`. 

### `isEquivariant_sourceFn`

 If `X^⊥` (the string) has odd rank `s`, so that `U = U^{≥2}`, then `𝒲_φ = Y.sourceFn t φ` is a
`ψ_U`-equivariant function on `[R]`. Here `𝒲_φ (u h) = ψ_U (u) (φ (h_fin), π_X (h_∞) v_*)`, with
`t = (·, v_*)`. Equivariant means continuous, left `R(F)`-invariant, and
`𝒲_φ (u r) = ψ_U (u) 𝒲_φ (r)` for `u ∈ U^{≥2}(𝔸)`. 

### `IsEquivariant.eq_sourceFn`

 Let the grading `Y` of `V` have a string of odd length `s`, so that `U = U^{≥2}`. A
`ψ_U`-equivariant function `W` on `R(𝔸)` that agrees on `H` with `algFormCoeff 1 t φ`, the values
of `𝒲_φ` there, is `𝒲_φ`. 

### `besselReal`

 The group `R(F_∞)` of real points of `R`. 

### `instance : IsClosed (Y.besselReal : Set (GInf E ε))`

 The group `R(F_∞)` of real points of `R` is closed. 
