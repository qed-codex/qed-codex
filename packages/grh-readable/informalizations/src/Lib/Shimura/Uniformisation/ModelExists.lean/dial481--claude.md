---
{
  "module": "src/Lib/Shimura/Uniformisation/ModelExists.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Uniformisation/ModelExists.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Uniformisation/ModelExists.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Every full complex object is modelled on a point (g, ℓ)

From a complex point of a family of abelian schemes back to linear algebra: an object `x` over `ℂ`
with structure map `Φ v₀` (the complex embedding of `E` at the fixed infinite place `v₀`) on `𝓞 E`
and a full structure `e` (a trivialisation of all torsion, `New.ThetaObject.FullLevelStructure`) is
a complex torus described by an adelic frame `g` and a reflection `ℓ`.

* `New.Variety.exists_torusModel`: a polarised period map on `ℂ^d` for `(g, ℓ)` and a model of `x`
  on it whose torsion points are those of `e`, with `ℓ` a reflection.
* `New.Variety.exists_torusModel_of_isPeriodMap`: the same model on a given period map `Q` whose
  exponential lifts the torsion points of `e`; the frame is found from the Weil pairing of `e`.

`New.ThetaObject.TorusModel` is a model of `x` on a given polarised period map `Q`
(`New.ThetaTori.PeriodMap`). It is a uniformisation of `x.groupScheme` whose kernel is the period
lattice.

Notions from other files:
* `New.ψf`: the additive character of the finite adeles with ψ_f(x) = exp(2πi Tr_{E/ℚ}(a)) for any a
  in E with x − a integral. In the code `𝐞 t` is exp(2πi t).
* `New.ThetaObject.groupScheme`: The group scheme with O_E-action of an object x over S: the
  pull-back of the abelian scheme of the family along x : S → base.
* `New.ThetaObject.baseHom`: For an object x over Spec R, the ring homomorphism O_E → R induced by x
  and the structure morphism of the base of the family to Spec O_E.
* `New.ThetaObject`: An object of the family X over a scheme T: a morphism from T to the base of X.

## Relation to the literature

Known; see `Lib.Shimura.Uniformisation.AppellHumbert` for sources.


### `exists_fourierChar_riemannForm_eq_ψf_xiForm`

 Let `u` uniformise `x.groupScheme`, with theta coordinates `θ` of type `(B, χ)` for
`x.lineBundle`, and let the torsion point of `e` at the class of `m *ᵥ y` be `u.expMap (Q y)` for
each `y` in `Eⁿ`. Then there is a unit `ε` (from the Weil pairing of `e`) such that on vectors of
`Eⁿ`, `𝐞` of the Riemann form of `B` pulled back by `Q` is `ψf` of the form `xiForm D.ξ`,
`(a, b) ↦ D.ξ · bᴴ a` on adelic vectors (`y` enters as `frameCoords 1 y`), with the matrix
`ε mᴴ m`. 

### `exists_map_eq_and_eq_polarisationForm_of_fourierChar_eq`

 Let `R` be a real bilinear form on `(E ⊗ ℝ)ⁿ` and `M` an `n × n` matrix of finite adeles such
that `𝐞 (R y z) = ψf (ξ · zᴴ M y)` for all `y`, `z` in `Eⁿ`, where `ψf` is the standard additive
character of the finite adeles and `ξ = D.ξ`, with `Φ v₀ ξ` of zero real part and positive imaginary
part. Then `M` is the image of a matrix `β` over `E`, and `R` is the polarisation form of `β`,
namely `(y, z) ↦ Σ_v 2 Re(Φ_v(ξ) z_vᴴ Φ_v(β) y_v)` summed over the infinite places `v`. 

### `exists_torusModel_of_isPeriodMap`

 Let `x` over `ℂ` have structure map `Φ v₀` on `𝓞 E` and full structure `e`, let `u` uniformise
`x.groupScheme` by `V`, and let `Q : (E ⊗ ℝ)ⁿ ≃ V` be a period map for `ℓ` (`i` acts as `i ℓ` at
`v₀`, as `i` elsewhere) with `u.expMap ∘ Q` `𝓞 E`-linear, sending `y` in `Eⁿ` to the torsion point
of `e` at the class of `m *ᵥ y`, and with `u.lattice` in `Q (Eⁿ)`. Then for some adelic frame `g`, a
polarised period map `Y` for `(g, ℓ)` on `V` has a model `M` of `x` with `e`'s torsion points. 

### `lattice_subset_range_of_expMap_eq_torsionPoint`

 Let `u` uniformise `x.groupScheme` and let the real-linear map `P` lift the torsion points of
`e` on the vectors of `½ (𝓞 E)ⁿ`: for `y` in `Eⁿ` with `2 y` integral, `u.expMap (P y)` is the
torsion point of `e` at the class of `y`. Then `P (Eⁿ)` contains the lattice `u.lattice`. 

### `exists_expMap_apply_cmEmbedding_eq_smul`

 Let `u` uniformise `x.groupScheme` by `Fin (abelianDim E D.Index) → ℂ`, and let `d` be the real
basis of `E ⊗ ℝ` (as `InfinitePlace E → ℂ`) given by an integral basis of `E`. The action of
`𝓞 E` on `x.groupScheme` lifts through `u` to an `ℝ`-linear map `G` from `E ⊗ ℝ` to the
complex-linear maps of that space: `u.expMap (G c z) = c • u.expMap z` for `c` in `𝓞 E`. 

### `exists_matrix_torsionPoint_eq_expMap`

 Let `u` uniformise `x.groupScheme` by `V`, and let `Q : (E ⊗ ℝ)ⁿ ≃ V` be such that
`u.expMap ∘ Q` is `𝓞 E`-linear and lifts the torsion points of `e` on the vectors of `½ (𝓞 E)ⁿ`.
Then there is an adelic matrix `m` such that `u.expMap (Q y)` is the torsion point of `e` at the
class of `m *ᵥ y` for every `y` in `Eⁿ`. 

### `expMap_apply_toRealVectors_eq_torsionPoint_of_two_smul_mem_ker`

 Let `u` uniformise `x.groupScheme` by `Fin (abelianDim E D.Index) → ℂ`, let `G` lift the action
of `𝓞 E` through `u`, and let `l j` lift the torsion point of `e` at the class of `e_j / 2`.
The real-linear map `P = ∑ j, (w ↦ G (w j) (2 l j))` lifts the torsion points of `e` on the
vectors of `½ (𝓞 E)ⁿ`: for `y` in `Eⁿ` with `2 y` integral, `u.expMap (P y)` is the torsion
point of `e` at the class of `y`. 

### `bijective_of_lattice_subset_range`

 Let `u` uniformise `x.groupScheme` by `V = Fin (abelianDim E D.Index) → ℂ`. A real-linear map
`P` from `(E ⊗ ℝ)ⁿ` to `V` whose image of `Eⁿ` contains the lattice `u.lattice` is bijective: the
lattice spans `V`, and the two real dimensions agree. 

### `isPeriodMap_vecMulVec_sub_one_of_sub_smul_eq`

 Let `Q : (E ⊗ ℝ)ⁿ ≃ V` carry the action of `E ⊗ ℝ` on `(E ⊗ ℝ)ⁿ` to an action `G` on `V`, and
let `Q Y` be an eigenvector of `G` with eigenvalue `c v₀` for each `c`. Suppose that `Im Φ(β) ≠ 0`
for `β = D.β`, and that `G (star β) - Φ(β)` (through `x.baseHom`, which is `Φ v₀` on `𝓞 E`) sends
`Q w` to `(η ⬝ᵥ w_{v₀}) • Q Y` for a vector `η`. Then `Q` is a period map (`i` acts as `i ℓ` at
`v₀`, as `i` elsewhere) for the matrix `ℓ = (Y · v₀) η'ᵀ - 1`, where `η' = (I / Im Φ(β)) η`. 

### `exists_torusModel`

 Let `x` be an object over `ℂ` whose structure map on `𝓞 E` is `Φ v₀` (`hρ`), with full
structure `e`. Then there are an adelic frame `g`, a complex matrix `ℓ` and a dimension `d` such
that `x` has a model `m` on a polarised period map `Y` for `(g, ℓ)` on `ℂ^d`, whose torsion points
are those of `e`, and `ℓ` is a reflection: `ℓ = u wᵀ - 1` for vectors `u`, `w` with `w ⬝ᵥ u = 2`, so
`ℓ` fixes the line of `u` and is `-1` on the kernel of `w`. 
