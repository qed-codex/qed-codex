---
{
  "module": "src/Lib/ClassField/HeckeL/IdelicThetaSum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeL/IdelicThetaSum.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeL/IdelicThetaSum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Idelic theta sums over principal ideles as Riemann sums

This file proves the lattice-sum estimate behind the continuation of Hecke `L`-functions to
`s = 1`. Ideles are pairs of a unit of the Minkowski space `mixedSpace K` and a finite idele. The
file defines the principal ideles, the module of an idele, an adelic tent and its theta sum over
the principal ideles. It writes theta sums as Riemann sums over the image of `K`. It shows that
`thetaSum d (r / 3) b` depends, up to an error, only on the module of `b`.

## Main definitions and results

* `New.ZetaIntegral.principalIdeles`: the image of `Kˣ` in the idele group;
  `New.ZetaIntegral.ideleModule` is the module of an idele.
* `New.ZetaIntegral.adelicTent r d`: a tent of height and radius `r` at `1` times the indicator of
  `d * (x - 1) ∈ Ô`.
* `New.ZetaIntegral.thetaSum d r b`: the sum of the tent over the coset of `b` modulo the
  principal ideles. `New.ZetaIntegral.exists_abs_sub_thetaSum_le_mul_rpow`: `thetaSum d (r / 3) b`
  depends only on the module `l` of `b`, up to an error: for each `l > 0` some `i` has
  `|i - thetaSum d (r / 3) b| ≤ C * l ^ δ * thetaSum d r b` for all `b` of module `l`.

Notions from other files:
* `New.finIdeleAbs`: The module |x| of a finite idele x: the adelic absolute value of the idele with
  finite part x and component 1 at infinity.
* `New.Ô`: The subring Ô of finite adeles of K that are integral at every finite place.

## Relation to the literature

Known; see `Lib.ClassField.HeckeL.ContinuationAtOne` for sources.


### `abs_max_sub_max_le_mul_max`

 Lowering a tent changes it little. Let `0 < r` and `0 < ε`, and let `D'` be within `ε * r / 3`
of `D`. Then the tent of height `(r - ε * r) / 3` at distance `D'` is within `ε * max (r - D) 0` of
the tent of height `r / 3` at distance `D`. 

 ### The principal ideles, the module and the test function 

### `principalIdeles`

 The subgroup of principal ideles: the image of K^× in the idele group. 

### `ideleModule`

 The module of an idele, a homomorphism to ℝ: the absolute value of the norm to ℝ of its
infinite part times the module `New.finIdeleAbs` of its finite part. 

### `adelicTent`

 The function on adeles x = (x_∞, x_f) equal to the tent max(r − dist(x_∞, 1), 0) if x_f lies
in 1 + d⁻¹Ô, and 0 otherwise. 

 ### Continuity, scaling and supports 

### `continuous_ideleModule`

 The module of an idele is continuous. 

### `measurePreserving_idele_mul`

 Multiplication by an idele `a` on `mixedSpace K × 𝔸f K` takes the Haar measure `volume` to
`(ideleModule a)⁻¹ • volume`. 

### `ideleModule_principal_eq_one`

 The product formula: a principal idele has module one. 

### `dist_le_and_mem_of_adelicTent_ne_zero`

 Where `adelicTent r d` is nonzero, the infinite part is within `r` of `1` and `d` times the
finite part minus `1` is integral. 

### `hasCompactSupport_adelicTent_mul`

 The tent `adelicTent r d`, composed with multiplication by an idele `a`, has compact support. 

### `abs_adelicTent_add_sub_le`

 Moving `x` by `w` with `‖w.1‖ ≤ ε * r / 3` and `d * w.2` integral, and lowering the tent from
`r / 3` to `(r - ε * r) / 3`, changes `adelicTent` by at most `ε * adelicTent r d x`. 

### `adelicBox`

 The box `ball 0 ρ ×ˢ d⁻¹ Ô` in `mixedSpace K × 𝔸f K`: the points whose infinite part has norm
less than `ρ` and whose finite part times `d` is integral. 

### `exists_principal_mul_mem_box`

 Blichfeldt's lemma for ideles. Let `F` be a fundamental domain for `K` in
`mixedSpace K × 𝔸f K`, and suppose the preimage, under multiplication by `a`, of the box
`ball 0 ρ ×ˢ d⁻¹ Ô` has more volume than `F`. Then for some principal idele `γ` the idele `a * γ`
has infinite part of norm less than `2 * ρ`, and `d` times its finite part is integral. 

 ### Theta sums as Riemann sums over the image of `K` 

### `map_val_val_mem_range_of_mem_principalIdeles`

 A principal idele, as a point of `mixedSpace K × 𝔸f K`, lies in the image of `K`. 

### `principalIdelesToRange`

 A principal idele, as an element of the image of `K` in `mixedSpace K × 𝔸f K`. 

### `discreteTopology_principalIdeles`

 If the image of `K` in `mixedSpace K × 𝔸f K` is discrete, so are the principal ideles: they map
continuously and injectively to it. 

### `hasSum_adelicTent_mul_range`

 Let the image of `K` in `mixedSpace K × 𝔸f K` be discrete. For `ρ ≤ 1`, an idele `b` and a
principal idele `γ`, the sum of `adelicTent ρ d` at the points `b * γ * y`, `y` in the image of
`K`, is its sum at the points `γ' * b`, `γ'` principal. The term of `y = 0` vanishes, and the
nonzero `y` are the principal ideles. 

### `volume_preimage_idele_mul_adelicBox`

 Multiplication by an idele `b`: for `t > 0`, the preimage of `adelicBox d (t * ρ)` has
`(ideleModule b)⁻¹ * t ^ [K : ℚ]` times the volume of `adelicBox d ρ`. 

### `norm_setIntegral_vadd_sub_adelicTent_le`

 One cell of the Riemann sum. Let `F ⊆ closedBall 0 R ×ˢ Ô K` be measurable of volume one, let
`c` be an idele with infinite part of norm less than `t * r / 3` and `d` times its finite part
integral, and let `y` be in the image of `K`. Then the mean over `y + F` of the tent of radius
`(r - R * t * r) / 3` at `c * x` is within `R * t` times the tent of radius `r` at `c * y` of
the tent of radius `r / 3` at `c * y`. 

### `thetaSum`

 The theta sum of radius `ρ` at an idele `b`: the sum of the tent `adelicTent ρ d` over the coset
of `b` modulo the principal ideles. 

### `exists_abs_sub_thetaSum_le_mul_rpow`

 Let `0 < r < 1`, and for an idele `b` let `thetaSum d ρ b` be the sum of the adelic tent
`adelicTent ρ d` of radius `ρ` (built from the finite idele `d`) over the coset of `b` modulo the
principal ideles `Kˣ`. There are `δ > 0` and `C > 0` such that for every `l > 0` some number `i` is
within `C * l ^ δ * thetaSum d r b` of `thetaSum d (r / 3) b`, for all ideles `b` of module `l`. The
bound on `r` makes the tents of radius `r` and `r / 3` vanish at `0`, so the theta sums may be taken
over all of `K`. 

### `exists_abs_sub_thetaSum_le`

 Let `0 < r < 1`, and let `Θ r b` be the theta sum `thetaSum d r b`. (a) The principal ideles
are discrete. (b) The estimate of `exists_abs_sub_thetaSum_le_mul_rpow`, with `|Θ r b|` in the
bound. 
