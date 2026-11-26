---
{
  "module": "src/Lib/Shimura/ArcExtension.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ArcExtension.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ArcExtension.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniformisations over an arc: theta coordinates, Weil pairing and extension of maps

Let `A` be an abelian scheme over an arc `O` (`New.ValuativeArc`, a valuation ring with fraction
field `ℂ`). Let `u : V / Λ ≅ A(O)` be a uniformisation (`New.Uniformisation`) with `Λ = u.lattice`,
and let `L` be a linear system whose coordinates are theta functions (`New.HasThetaCoords`).
Sections of `L` are read as functions on `V`. Lifts of translations then act by twisted
translations, and their commutators are given by the Weil pairing. With these tools, an additive map
`s' : V → A'(O)` that kills `Λ` and has theta coordinates is shown to come from a morphism `A ⟶ A'`
over `O`, not only over `ℂ`.

## Main definitions and results

* `New.Variety.isSeparatingFamily_atGeneric_of_surjective`: the complex points `New.atGeneric` of
  the sections are dense in `A`.
* `New.Variety.thetaEval`, `New.Variety.exists_theta_evaluation`: `H⁰(L)` embeds in the
  functions on `V`, and lifts of translations (`New.Variety.IsTranslationLift`) act by multiples
  of the twisted translations `New.RealComplexForm.thetaShift`.
* `New.Variety.lift_commutator_iff_weil_pairing`: the commutator of two lifts is given by the
  Riemann phase `New.RealComplexForm.riemannPhase`.
* `New.Variety.exists_sections_of_translation_stable`: one scalar puts a finite family of theta
  functions in a stable `O`-module. No orbit of the dual lattice consists only of common zeros.
* `New.Variety.exists_section_of_hasThetaCoords`: a section of `π : A' ⟶ A` through the points
  `s' z`.
* `New.Variety.exists_hom_of_hasThetaCoords`: a homomorphism `A ⟶ A'`, obtained from its graph in
  `A × A'`.

Notions from other files:
* `New.IsAbelianScheme`: a commutative group scheme A over S is abelian if it is smooth and proper
  over S and multiplication by every m ≠ 0 is surjective.
* `New.LineBundle.H0`: The R-module of global sections of L, for a scheme X over R; a section `r`
  has a component `r.val i` (a `New.PointFn`) in each chart `i`.
* `New.IsPosRiemann`: The Riemann form E of B is positive: E(u, iu) > 0 for every u ≠ 0.
* `New.Variety.IsTranslationLift`: The R-linear endomorphism Φ of H⁰(L) is pull-back along the
  translation t_z by the section z followed by some isomorphism t_z^*L ≅ L.

## Relation to the literature

Known result: Homomorphisms and line bundles of abelian schemes extend from the generic fibre. Here
only maps of complex tori that multiply a theta polarisation by an integer are treated, where the
kernel of the polarisation is killed by a unit of the ring, over any valuation ring of the complex
numbers (not noetherian, any rank). The map and the identity of line bundle classes extend together,
and points extend by properness. Source: S. Bosch, W. Lütkebohmert, M. Raynaud, Néron Models (1990),
1.2/8 and 4.4/1; G. Faltings, C.-L. Chai, Degeneration of Abelian Varieties (1990), I.2.7; L.
Moret-Bailly, Pinceaux de variétés abéliennes, Astérisque 129 (1985), II.3.5.

See also `Lib.Shimura.IntegralModel.UniversalFamily` and `Lib.Shimura.Uniformisation.AppellHumbert`.


### `_root_.New.LineBundle.H0.val_eq_transition_mul`

 At a point that lands in the charts `i` and `j`, the components of a global section `r`
differ by the transition function: `r i = g_ij · r j`. 

### `_root_.New.LineBundle.H0.val_eq_zero_of_not_landsIn`

 A component `r.val i` of a global section vanishes at the points outside the chart `i`. 

### `_root_.New.LineBundle.IsFrame.isUnit_apply`

 A frame of `L` is a unit at every point that lands in the chart `i`. 

 ## Sections along a uniformisation as theta functions 

### `isSeparatingFamily_atGeneric_of_surjective`

 Let A be a smooth proper scheme over a valuation ring O with fraction field ℂ, and let
s : Z → (sections of A over O) be surjective. Then A is reduced and the complex points
`atGeneric s z` (the sections restricted to the generic point `Spec ℂ` of `Spec O`) are dense in
A. 

### `_root_.New.HasThetaCoords.holomorphicAt`

 If the linear system `L` is an embedding and has theta functions as coordinates along `s`, the
family of complex points of `s` is holomorphic. 

### `thetaChart`

 For theta coordinates `θ` of `L` along `s`, a chart in which `θ z` does not vanish. 

### `apply_thetaChart_ne_zero`

 The theta function `θ z` does not vanish in the chart `thetaChart h z`. 

### `thetaEval`

 Sections of `L` read as functions on `V`, for theta coordinates `θ` of `L` along `s`: a
section `r` goes to `z ↦ θ z i * r_i (s z)` for a chart `i` with `θ z i ≠ 0`. The value does not
depend on the chart (`New.Variety.thetaEval_eq_iff`). 

### `thetaEval_eq_iff`

 `thetaEval h r` is the function `g` exactly when `r_i = g / θ_i` at each point `s z`, in each
chart `i` with `θ z i ≠ 0`. 

### `thetaEval_coordSection`

 `thetaEval h` sends the coordinate sections to the theta functions. 

### `thetaEval_injective`

 Along a uniformisation, `thetaEval h` is injective: the points `atGeneric u.expMap z` are
dense, so sections that agree there are equal. 

### `exists_thetaEval_eq_smul_thetaShift`

 Along a uniformisation, a lift `Φ` of the translation by `u.expMap a` acts through
`thetaEval h` as a multiple of the shift `B.thetaShift a`. 

### `exists_theta_evaluation`

 Let L have theta coordinates θ_i along s for a lattice Λ. Then r ↦ θ_i·r_i
(`New.Variety.thetaEval`) is an O-linear map from H⁰(L) to functions on V that sends the
coordinates to the θ_i. If Λ and s are the lattice and exponential map of a uniformisation, this
map is injective and sends lifts of translations to scalar multiples of
`New.RealComplexForm.thetaShift`. 

### `lift_commutator_iff_weil_pairing`

 Weil pairing: let L have theta coordinates for B, and let Φ, Ψ lift to L^m the translations
by the images of a, b. Then ΦΨ = c·ΨΦ on all coordinates if and only if
c = exp(2πi m E(a,b)), E the Riemann form of B. 

### `exists_sections_of_translation_stable`

 Let `L` have theta coordinates `θ` of type `(B, χ)` along `u`, `B` be positive, `n` a unit of
`O`, and `N` an `O`-module of sections of `L` containing the coordinate sections. Suppose that each
`a` in the dual lattice `B.dualLattice` has `n • a ∈ u.lattice` (`h_torsion`), and that the
translation by `a` has a lift that preserves `N` (`h_lift`). For finitely many theta functions `f_j`
(elements of `B.thetaSpace χ`, the space that also holds each coordinate `θ_k`) of type `(B, χ)`
with `f_i ≠ 0` there are `γ ≠ 0` and sections `r_j ∈ N` such that: (a) the `k`-th component of `r_j`
at the point `u.expMap z` is `γ f_j(z)/θ_k(z)` whenever `θ_k(z) ≠ 0`; (b) for every field-valued
point `t`, some component of some `r_j` is nonzero at some translate of `t` by `B.dualLattice`. 


## Extension of linear maps to sections and homomorphisms over an arc

`New.HasThetaCoords` says that the coordinates of a linear system at the complex points
`New.atGeneric` are theta functions of type `(B, χ)`. Standing hypotheses: `N` has such coordinates
along `u.expMap`, and the Riemann form of `B` is positive (an instance `IsPosRiemann B`). Further,
`n` is a unit of `O`, and every `a` in the dual lattice of `B` has `n • a ∈ u.lattice`, and the
translation by `u.expMap a` lifts to `N`. Also `s'` kills `u.lattice`, `A'` is proper over `O`, and
`M` is a projective embedding of `A'`.


### `exists_isTranslationLift_top_of_dualLattice`

 The lift of a translation by a point of the dual lattice preserves the module of all
sections. 

### `translation_comp_eq_of_nsmul_mem`

 If `n • z₀` lies in the lattice `u.lattice`, which `s'` kills, then the translation of `A'` by
`s' z₀` followed by `ν`, multiplication by `n`, is `ν`. 

### `atGeneric_comp_translation`

 The translation of `A'` by `s' z₀` moves the complex point `atGeneric s' x` to
`atGeneric s' (x + z₀)`. 

### `comp_translation_eq_translation_comp`

 If the homomorphism `π : A' ⟶ A` sends `s' z` to `u.expMap z`, it carries the translation of
`A'` by `s' z₀` to the translation of `A` by `u.expMap z₀`. 

### `exists_section_of_hasThetaCoords`

 Assume the standing hypotheses from the section head (`h`, `IsPosRiemann B`, unit `n` with
`h_tors_lift`, `s'` killing `u.lattice`, `A'` proper, `hM`). Let `π : A' ⟶ A` be a homomorphism that
sends `s' z` to `u.expMap z`. Let the theta coordinates `f` of `M` along `s'` have the same type
`(B, χ)` as those of `N`. Let `ν^* π^* N ⊗ M ^ m` and `ν^* M ⊗ (π^* N) ^ m` have the same class,
where `ν` is multiplication by `n` on `A'` and `m = n ^ 2`. Then `π` has a section `e` that sends
`u.expMap z` to `s' z` and satisfies `[e^* M] = [N]`. 

### `exists_hom_of_hasThetaCoords`

 Let `u` uniformise the abelian scheme `A` over `O`, and let `N` be a projective embedding of `A`
with theta coordinates of type `(B, χ)` along `u`, where `B` is positive. Let `n` be a unit of `O`
such that each `a` in `B.dualLattice` has `n • a ∈ u.lattice` and translation by `u.expMap a` lifts
to sections of `N`. Let `s'` be a homomorphism from `V` to the sections of a commutative group `A'`
proper over `O` that kills `u.lattice`, and let `M` be a projective embedding of `A'` with theta
coordinates of type `(μ • B, χ ^ μ)` along `s'`. If the classes of `N` and `M` obey the
parallelogram law (`ParallelogramLaw`; through `pull_nsmul_eq_sq_smul`, pulling back along
multiplication by `d` then multiplies the class by `d ^ 2`), then there is a homomorphism
`ψ : A ⟶ A'` that (a) sends `u.expMap z` to `s' z` for all `z`, and (b) satisfies
`ψ^* [M] = μ • [N]`. 
