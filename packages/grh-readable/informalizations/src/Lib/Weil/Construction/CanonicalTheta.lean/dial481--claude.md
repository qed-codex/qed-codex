---
{
  "module": "src/Lib/Weil/Construction/CanonicalTheta.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/CanonicalTheta.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/CanonicalTheta.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Independence of the theta functional of the chosen group element; transport and sums

The theta functional `New.Space.θ` of a space `V` is defined by transporting a theta functional of
the standard space `New.signedSpace E s` along a chosen group element. Such a functional exists by
`New.exists_isThetaFunctional_signedSpace`.

* `New.CoordChange.exists_theta_omega_map`: a vacuum-preserving change of coordinates
  (`New.CoordChange`) that respects rational vectors transports theta functionals, up to a factor of
  modulus one.
* `New.Space.exists_mapsTo_ratVectors`: a group element that matches the rational vectors of two
  spaces exists, by Landherr's theorem.
* `New.Space.theta_omega_eq_of_mapsTo_ratVectors`: `θ` does not depend on the chosen element, since
  two choices differ by a rational point.
* `New.Space.theta_omega_rho_vacElem_eq_prod_lineTheta`: with any element that matches the rational
  vectors, `θ ∘ ω(g)` of the translates of the vacuum is a product of the rank one theta functions
  `New.lineTheta`.
* `New.Space.theta_move`: moving the point of `V` by `γ` changes `θ` to `θ ∘ ω(γ)`.
* `New.Space.theta_boxProd`: `θ` is multiplicative on orthogonal sums.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to diag(s) at the infinite places and 1 at the finite places.
* `New.𝒮`: The Banach space 𝒮(V) of integrable functions c on 𝔸^n with c(x) = ∫ c(y)β(y,x)e(x−y) dy,
  under the L¹ norm; β is the adelic bicharacter and e the vacuum function `New.vacuumFn`.
* `New.signedSpace`: the standard space with matrix diag(s), a sum of lines.
* `New.Space.IsThetaFunctional`: A theta functional of V: a bounded θ on
  `Model (adelicHeisenberg E s)`, invariant under the rational Heisenberg operators, with
  |θ(ρ(x)vac)|² of mean 1 over 𝔸^n modulo rational points.
* `New.Space.boxProd`: For a splitting of the coordinates, the product 𝒮(V₁) × 𝒮(V₂) → 𝒮(V).

## Relation to the literature

Known; see `Lib.Weil.MixedModel.ZeroTerm` for sources.


### `_root_.New.CoordChange.exists_theta_omega_map`

 Let `σ` be an isometric ring endomorphism of ℂ that is an involution. Let `D` be a change of
adelic coordinates `D.φ` from 𝔸^n to 𝔸^{n₁} that keeps the Heisenberg bicharacter up to `σ`, with
induced map `D.map : 𝒮 V₁ → 𝒮 V`, and let `g : G E s` be such that `g • x` is a rational vector of
`V` whenever `D.φ x` is a rational vector of `V₁`. Then there is `c : ℂ` with `‖c‖ = 1` such that
`V₁.θ f = c * σ (V.θ (V.ω g (D.map f)))` for all `f : 𝒮 V₁`. 

### `exists_mapsTo_ratVectors`

 Let `V` and `W` be two hermitian spaces with a point (a matrix `J` over `E` and a point `x` in
`GL_n(𝔸)`) over the CM number field `E` with Weil data, and suppose they have the same signs `s`.
Then some `g` in the adelic unitary group `G E s` carries the rational points of `V` (the vectors
`x_V⁻¹ y`, `y ∈ E^n`) into those of `W`. 

### `_root_.Matrix.mulVec_col_apply_eq_mul_apply`

 Entry `j` of `M *ᵥ (column i of N)` is the entry `(j, i)` of `M * N`. 

### `theta_omega_eq_of_mapsTo_ratVectors`

 The functional `θ_V` does not depend on the group element chosen in its definition: for every
`g` in the adelic unitary group `G E s` that carries the rational vectors of the sum of lines with
signs `s` into the rational vectors of `V`, the functional `θ_V ∘ ω(g)` is the fixed theta
functional of the sum of lines. 

### `theta_omega_rho_vacElem_eq_prod_lineTheta`

 The law that fixes the phase of `θ`: for every `g` that carries the rational vectors of the
sum of lines into those of `V`, the value of `θ_V ∘ ω(g)` on the translate of the vacuum by `x`
is the product of the rank-one theta values at the coordinates of `x`. 

### `theta_eq_theta_omega`

 Let `W` and `V` be hermitian spaces with a point over the CM number field `E` with Weil data.
Both have the same signs `s`, and `g` is an element of the adelic unitary group `G E s`. If `g`
carries the rational points of `W` (the vectors `x_W⁻¹ y`, `y ∈ E^n`) into those of `V`, then for
every `f` in the Banach space `𝒮 V` the theta functionals satisfy `W.θ f = V.θ (V.ω g f)`, that is,
`θ_W = θ_V ∘ ω(g)` with `ω` the Weil representation. The statement makes sense because `𝒮` and `ω`
depend only on the signs. 

### `theta_move`

 Let `V = (J, x)` be a hermitian space with a point over the CM number field `E` with Weil data,
and let `γ` be in the adelic unitary group `G E s`. The space `V.move γ = (J, xγ)` has the same
matrix as `V` and its point moved by `γ`. Its theta functional is `θ_V ∘ ω(γ)`, that is,
`(V.move γ).θ f = V.θ (V.ω γ f)` for every `f` in the Banach space `𝒮 V`, where `ω` is the Weil
representation. 

### `vacElem_apply_eq_prod_lineTheta`

 If `V` has the rational points of the sum of lines (`V.vecAtPoint y`, the vector `x_V⁻¹ y`,
equals that of the sum of lines for every `y ∈ E^n`), the theta function of its vacuum,
`x ↦ V.vacElem x`, which is `θ_V` at the translate `ϱ(x)` of the vacuum, is the product of the
rank-one theta values at the coordinates. 

### `theta_boxProd`

 The functional `θ` is multiplicative: if the point of `V` is the block sum of the points of
`V₁` and `V₂` along `e`, then `θ_V (f₁ ⊠ f₂) = θ_{V₁} f₁ * θ_{V₂} f₂`. 
