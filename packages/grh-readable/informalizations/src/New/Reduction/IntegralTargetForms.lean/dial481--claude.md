---
{
  "module": "src/New/Reduction/IntegralTargetForms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/IntegralTargetForms.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/IntegralTargetForms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The target forms as a twisted lattice

The target forms `D.targetForms` have no evident integral structure, so a target form is called
integral if its lifts are. The maps `Θ_ϑ`, with the inner products, conjugates and integrality of
algebraic forms, make the target a twisted lattice (`New.Data.targetLattice`). Its twists are the
`m`-fold twists `ϑ`, and `ϑ` is allowed at `l` if the norm of its modulus is prime to `l`. The file
identifies the integral vectors, the conjugate norms and the volumes of this lattice.

Notions from other files:
* `New.TwistedLattice`: maps `Θ_ϑ` from a space to inner product spaces with integral structures.
* `New.Data.targetForms`: the target forms, the good forms on the space `Y_0`.
* `New.Data.TameChar`: an automorphic character `ϑ` of `U(1)` of weight `0` whose tame part is
  supported on a finite set `Q` of places, its modulus.
* `New.Data.MFoldTwist`: a twist `ϑ` whose tame part `ψ` has `ψ_w^n ≠ 1` for `w ∈ Q`, `1 ≤ n ≤ m`.
* `New.Data.Θ`: the chain of `m` lifts with twist `ϑ`, from the target forms to forms on `Y_m`.
* `New.Data.lastResidueLevel`: the group of reductions that cuts out the level of the forms on
  `Y_m`.
* `New.LevelPlaces.LevelForm.integralForms`: the forms integral at an embedding `ℂ → ℂ_l`.


### `levelOf_lastResidueLevel_le_chosenLevel`

 Let `ϑ` be a tame character. Its level places, listed by `placeAt`, are the chosen places and
the places of `Q`. The left side is the group of elements of the finite adelic unitary group of
`Y_m` that are integral at every finite place and whose reductions lie in `lastResidueLevel ϑ`, that
is, are `1` at the chosen places and block upper triangular at the places of `Q`. It lies in
`D.chosenLevel`, the integral elements that reduce to `1` at every chosen place. 

### `classAut_lastResidueLevel_eq_bot`

 Let `ϑ` be a tame character, and `K` the level cut out by `lastResidueLevel ϑ`: the integral
elements that reduce to `1` at the chosen places and to a block upper triangular matrix at the
places of `Q`. Then `K` is sufficiently small: for every `g`, the stabiliser
`classAut Γ K g = Γ ∩ gKg⁻¹` of the coset `gK` in the group `Γ = stdRatPoints` of rational points is
trivial. 

### `targetLattice`

 The target forms `D.targetForms` as a twisted lattice. Its twists are the `m`-fold twists `ϑ`:
twists whose tame part `ψ` has `ψ_w^n ≠ 1` for `1 ≤ n ≤ m` and `w` in its modulus, a finite set `Q`
of places. The map at `ϑ` is the chain of lifts `Θ_ϑ` to the forms on `Y_m` with the level and
character of `ϑ` and the weight given by the column counts `D.columnsY` and the last entries
`D.lastEntry D.m`. The lattice at `ι` consists of the forms integral at `ι`, and `ϑ` is allowed at
`l` if the norm `ϑ.normQ` of its modulus is prime to `l`. The coordinates of a form for the
trivial twist are those of its values at representatives of the classes, in the standard basis of
the Weyl module. 

### `mem_integralVectors_targetLattice`

 Let `y` be a target form: an automorphic form on the unitary group of the space `Y_0`, of
principal level at the chosen places, in the image of the idempotent `D.e₀`. Let `ι : ℂ ≃ ℚ̄_l`,
where `l = ι.prime`, and let `ι.place` be the embedding `ℂ → ℂ_l` that it gives. Then `y` is an
integral vector of the twisted lattice at `ι` if and only if `Θ_ϑ y` is integral at `ι.place` for
every `ϑ` with `ϑ.normQ` prime to `l`. 

### `normSqAt_targetLattice`

 Let `y` be a target form, `σ ∈ Aut ℂ`, and `φ = Θ₁ y` the lift of `y` to an algebraic form on
`Y_m` for the trivial twist, of level `K`. The coordinates of `y` in the twisted lattice are those
of the values `φ(g_c)` in the standard basis of the Weyl module, where `g_c` runs over
representatives of the classes `c ∈ Γ\G_f/K`. The left side is the sum over `c` of the squared norms
of the vectors `σ(φ(g_c))` for the Gram matrix of the Weyl module. The right side `‖φ‖²_σ` is the
same sum with the term at `c` divided by `#(Γ ∩ g_c K g_c⁻¹)`. They agree since these stabilisers
are trivial. 

### `volume_targetLattice`

 The volume of the twisted lattice of target forms at `ϑ` is
`chainDeterminant(ϑ) = det (Θ_ϑ* Θ_ϑ)`. 

### `injective_lift_targetLattice`

 For every `m`-fold twist `ϑ`, the map `D.targetLattice.lift ϑ` is injective on the target forms
`D.targetForms`. 
