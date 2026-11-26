---
{
  "module": "src/New/UpperBound/Objects/PoincareMap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/PoincareMap.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/PoincareMap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Poincaré map

The Poincaré map `𝒫 = D.poincareAt g t : 𝒜(X₀) → 𝒜(Y₀)` sends a source form `φ` to the form that
represents the Bessel period of `φ` in the Petersson inner product.

Notions from other files:
* `V.Form e`: the automorphic forms of archimedean type `e` on the adelic unitary group
  `G E s = GInf E s × Gf E n` of `V`; `V.quotMeasure` integrates over the quotient by the rational
  points, and `HasLevel z J` says that `z` is right invariant under `J ⊆ Gf E n`.
* `D.SourceForm` is the space `𝒜(X₀)` of algebraic forms on the definite unitary group of `X₀`,
  with values in a Weyl module and of level `D.levelX 0`. `D.principalForms (D.spaceY 0)` is the
  space `𝒜(Y₀)` of forms on the group `G₀` of `Y₀` whose archimedean type is the discrete series of
  doubled parameter `D.paramW` and whose level is `J_M = D.chosenLevel`, the group of integral
  finite adelic points that reduce to `1` at every prime divisor of `D.piM`.
* `Y.besselGroup` is the adelic Bessel subgroup `R(𝔸)` of a grading `Y`, and `Y.besselMeasure`
  integrates over `[R] = R(F) \ R(𝔸)`. For `Y = D.gradingY 0` the group is written `R₀`.
* `Y.sourceFn t φ` is the function `𝒲_φ (u h) = ψ_U (u) · t (ρ (h_∞⁻¹) φ (h_f))` on `R(𝔸)`. Here
  `u` is unipotent, `h` lies in the unitary group of `X`, `ψ_U` is the generic character,
  `ρ = conjWeylRep` is the action on the values of `φ`, and `t` is a linear form on these values.

## Relation to the literature

See `New.UpperBound.Seesaw.SeesawIdentity` for related work.


### `bijective_flip_innerₛₗ`

 On an inner product space `F` of finite dimension, every conjugate linear form is `y ↦ ⟨y, z⟩`
for a unique vector `z` (Riesz). 

### `rieszMap`

 The linear map that sends `x` to the vector representing the conjugate linear form `B x`. 

### `inner_rieszMap`

 The inner product of `y` with `rieszMap B x` is `B x y`. 

### `Form.levelTrace`

 The sum of the right translates of a form `z` under the chosen representatives of
`K / (J ∩ K)`, for subgroups `J` and `K` of the finite adelic group. 

### `Form.levelTrace_apply`

 The value of `z.levelTrace J K` at `x` is the sum, over the cosets `q` in `K ⧸ J.subgroupOf K`,
of `z (x * (1, q.out))`. This is the value of `z` at `x` translated on the right by the chosen
representative of `q`. 

### `Form.hasLevel_levelTrace`

 If a form `z` is right invariant under `J`, then the sum of its translates under
representatives of `K / (J ∩ K)` is right invariant under `K`. 

### `Form.integral_levelTrace_mul`

 Let `y` be a form of level `K` and `z` any form. The integral against `y` of the sum of the
translates of `z` under representatives of `K / (J ∩ K)` is `[K : J ∩ K]` times the integral of
`z · y`, both over the quotient of `G` by its rational points. 

### `IsEquivariant.integrable_mul`

 Let `W` be an equivariant function on `R(𝔸)`: it is continuous and left invariant under `R(F)`,
and `W (u r) = ψ_U (u) W (r)` for `u` in the subgroup `U^{≥2}(𝔸)` of elements for which `u - 1`
raises the grading by at least `2`. Let `y` be an automorphic function on the unitary group `G E ε`
of `V`, and let `x` be a point of `G E ε`. Then `r ↦ W r * y (r * x)` is integrable over
`[R] = R(F) \ R(𝔸)`, because it is continuous on a compact quotient. 

### `isEquivariant_sourceFn`

 For a source form `φ` on `X₀`, the function `𝒲_φ = sourceFn t φ` on the Bessel group `R₀(𝔸)`
of `D.gradingY 0` is continuous, left invariant under the rational points, and transforms by the
generic character under the unipotent part. 

### `besselPeriod`

 The Bessel period `∫_{[R₀]} 𝒲_φ (r) conj (y (r g)) dr`, linear in the source form `φ` and
conjugate linear in the form `y` on `Y₀`. Here `g` is an archimedean point of `G₀`, and `𝒲_φ` is
formed with the linear form `t`. 

### `besselPeriod_apply`

 Let `g` be an archimedean point of the unitary group `G₀` of `Y₀`, let `φ` be a source form and
`t` a linear form on the Weyl module of its values. Let `y` be a form on `G₀` of discrete series
type `D.paramW` and principal level `D.chosenLevel`. Then `D.besselPeriod g t φ y = ∫_{[R₀]} 𝒲_φ (r)
conj (y (r g)) dr`. 

### `poincareAt`

 The Poincaré map `𝒫 : 𝒜(X₀) → 𝒜(Y₀)` for an archimedean point `g` of `G₀` and a linear form
`t`: the form `𝒫 φ` represents the Bessel period of `φ`. The measure on `[R₀]` is `besselMeasure`;
another Haar measure on `R₀(𝔸)` would multiply `𝒫` by a positive constant, which can be absorbed
in `t` by `poincareAt_smul`. 

### `inner_poincareAt`

 The defining property of the Poincaré map `𝒫 = D.poincareAt g t`. Let `g` be an archimedean
point of the unitary group `G₀` of `Y₀`, let `φ` be a source form and `t` a linear form on the Weyl
module `ρ = conjWeylRep` of its values. Let `y` be a form on `G₀` of level `D.chosenLevel` whose
archimedean type is the discrete series of doubled parameter `D.paramW`. Then the Petersson product
`⟨y, 𝒫 φ⟩` is the Bessel period `∫_{[R₀]} 𝒲_φ (r) conj (y (r g)) dr`. 

### `poincareAt_smul`

 Scaling the linear form `t` scales the Poincaré map `𝒫 = D.poincareAt g t` by the same factor,
so that a change of the Haar measure can be absorbed in `t`. 

### `integral_mul_poincareAt`

 Let `z` be a form on `G₀`, right invariant under `J`, whose archimedean type is conjugate to
that of the values of `𝒫 = D.poincareAt g t`. Then `[J_M : J ∩ J_M] ∫_{[G₀]} z · 𝒫 φ` is the sum
over representatives `γ` of `J_M / (J ∩ J_M)` of `∫_{[R₀]} 𝒲_φ (r) z (r g γ) dr`. 
