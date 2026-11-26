---
{
  "module": "src/Lib/PadicHodge/Kisin/FrameTheorem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Kisin/FrameTheorem.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Kisin/FrameTheorem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The frame theorem for Kisin modules and stability under normalising Galois elements

Let `L` be a lattice datum over a Kummer chart `k`. The ring `S` of `k` has a variable `z` and the
element `E = z ^ e * unit + p`, and `k.frobE m` is `φ ^ m E`; `phiInvToBdR 0` is the map
`Ainf → BdR`. Let `h = L.jumpBound` and `τ = [ε^{1/p}] − 1`. A form is an `Ainf`-linear map
`W(C♭) ⊗ L → B_dR`. Those in `L.forms` are `Γ'`-equivariant on `1 ⊗ L`. They cut out the
`Ainf`-module `L.kisinAinf` and the Kisin module `N = L.kisinModule` over `S`. `L.ainfLattice` is
`Ainf ⊗ L`; `L.fracSpan` holds the `x` with `r • x ∈ L.ainfLattice` for some non-zero divisor `r` of
`Ainf`, and `L.frobKisinAinf l` is `φ ^ l (L.kisinAinf)`.

## Overview of this theory

A chart (`New.Lift.Chart`) is a `Λ`-algebra map `Λ⟦X⟧ → A_inf`, with `Λ = W(𝔽_{p^f})`. It sends `X`
to a non-unit Teichmüller lift `z = [ϖ^♭]`. It sends some `X^e V + p`, with `V` a unit, to a
generator `E` of `ker θ`. `S` is its image. `B⁺` (`New.Period.BPlus`) receives `A_inf` and maps to
`B_max` (`New.Period.Bmax`) and `B_dR`. Its `S`-subalgebra `S_B` (`New.Lift.Chart.bicommutant`) is
the `p`-adic closure of `S[E/p]` with `p` inverted
(`New.Lift.Chart.adjoinEDivPClosure_eq_bicommutant`). Put `μ = [ε] - 1`, with `ε` a compatible
system of `p`-power roots of unity, and `τ = φ⁻¹ μ`.

* Let `K` be the field fixed by an open subgroup `G_K` of `Gal(ℚ̄_p/ℚ_p)`. There is a Kummer chart
  (`New.Lift.KummerChart`) with `Λ` and `θ z` fixed by `G_K` and `e f = [K : ℚ_p]`
  (`New.Lift.exists_kummerChart`).
* Let `c` be a chart for `G_K` (`IsChartOf`). Let `T` be a crystalline `ℤ_p`-lattice with action
  `ρ`, whose jumps (the `k` with `New.Period.jump` nonzero) lie in `[-a, b]`. In a basis of `T`
  there are three objects. The first is `P`, invertible over `B_max`, with `ρ(g) · g P = P`. The
  second is a unit `v` with `E τ v = μ`. The third is `U` over `B⁺`, whose image in `B_max` is
  `(E τ)^a P`. This `U` satisfies the predicate `IsPeriodMatrix` with height `a + b` and Frobenius
  factor `v^a` (`New.Lift.Chart.IsChartOf.exists_isPeriodMatrixOf`).
* Take such a `U` of height `h` and factor `v`. There are `Q` and `Q'` over `A_inf`, `Z` over `S_B`
  and `B` over `S` with `Q Q' = τ^h`, `U Z = E^h Q` and `φ Q = v Q B`
  (`New.Lift.Chart.IsPeriodMatrix.exists_frame`).
* On a Kummer chart, let `h = jumpBound`. Let `N` be the `S`-module `kisinModule` and `M` its
  `A_inf`-span `kisinAinf`. Then `τ^h` maps `M` into `ainfLattice` and back, and `E^h φ N ⊆ N`. Take
  a crystalline form `λ` (`crysForms`, valued in `B_dR`). Then `E^h λ(N)` lies in the image of
  `S_B`. Suppose `d ∈ A_inf` is such that `d ∣ E^m r` in `B⁺` forces `d ∣ r`. Then `x ∈ M` lies in
  `d M` once, for one `n`, `E^n λ(x) ∈ d B⁺` for all such `λ`
  (`New.Lift.KummerChart.JumpLattice.mem_smul_kisinAinf_of_crysForms`).

This is a substitute, in the form needed here, for part of Kisin's theorem on the module of a
crystalline lattice (Kisin 2006; Bhatt–Morrow–Scholze 2018). The inclusion `E^n N ⊆ S φ N` and an
equivalence of categories are not stated.

Contents of the files. `Charts`: coordinates and an approximation lemma.
`Bicommutant`: extension to `B⁺`.
`PeriodMatrixBasis`: `U`, and `Q` with `det Q ≠ 0`. `PeriodMatrixFrame`: `p ∤ det Q`, hence the
frame. `KummerChartDeRham`: the different, and values in `B_dR`. `Modules`: `M`, `N` and the
`B_dR`-valued forms. `FrameTheorem`: `N` as the `S`-span of the columns of `τ^{-h} Q`, using
`Lib.PadicHodge.RadiusLemma`.

## Main definitions and results

* `New.Lift.KummerChart.JumpLattice.frame_theorem`: a relation `∑ c i • v i = 0` among vectors of
  `L.valueFieldPoints L.fracSpan` still holds after applying any `k.S`-linear `f : Ainf → k.S` to
  the coefficients (`New.Lift.KummerChart.JumpLattice.FrameProperties`).
* `New.Lift.KummerChart.JumpLattice.valueFieldPoints_frobKisinAinf_eq_span`: the vectors of
  `φ ^ l (L.kisinAinf)` on which all forms in `L.forms` take values in `k.valueField 0` form the
  `S`-span of `φ ^ l N`.
* `New.Lift.KummerChart.JumpLattice.smul_mem_kisinAinf`: an element `g` that conjugates `Γ'` into
  itself preserves the module `New.Lift.KummerChart.JumpLattice.kisinAinf`. The reason is that
  conjugation by `g` keeps forms `Γ'`-equivariant
  (`New.Lift.KummerChart.JumpLattice.conjForm_mem_forms`).

Notions from other files:
* `New.Lift.KummerChart.JumpLattice`: A finite free O-module with an action of Γ, crystalline over
  Γ', together with a finite set of integers for each embedding of O in `ℂ_[p]` that contains the
  jumps at that embedding. It also carries finite sets of integers indexed by `Letter`, which this
  file does not use directly.
* `New.Lift.KummerChart.JumpLattice.Ambient`: The module W(C^♭)⊗L for the lattice underlying L;
  `DiagTensor.mk 1 t` is the vector 1 ⊗ t.
* `New.Lift.KummerChart.JumpLattice.kisinAinf`: The x in A_inf[1/τ] ⊗ L with μ(φ^n x) in B_dR^+ for
  all n ≥ 1 and all μ in `L.forms`, where τ = [ε^{1/p}] − 1. The Kisin module consists of those x on
  which all forms in `L.forms` take values in the subfield `k.valueField 0` of B_dR.

## Relation to the literature

Known; see `Lib.PadicHodge.Kisin.PeriodMatrixFrame` and `Lib.PadicHodge.Kisin.Modules` for sources.


 ## The frame theorem: spanning and bounded height 

### `exists_functional_extend`

 Every `ℤ_[p]`-linear map `f` from the lattice `L` to `BdR` is the restriction of some
form `μ` to the vectors `1 ⊗ t`. 

### `equivariant_iff_basisValues`

 Let `μ` and `μ'` be forms, `g ∈ Γ`, and let `A` be an invertible matrix over `BdR` with
`ρ(g) * g(A) = A`, where `ρ(g)` is the matrix of `g` in the basis `finBasis ℤ_[p] L.Carrier`. Then
`μ'(1 ⊗ g t) = g • μ(1 ⊗ t)` for all `t` if and only if
`basisValues μ' ᵥ* A = g • (basisValues μ ᵥ* A)`; here `basisValues` is the vector of values
of a form on the basis vectors `1 ⊗ e i`. 

### `kisinAinf_le_fracSpan`

 The module `L.kisinAinf` lies in `L.fracSpan`: a power of `τ` is a non-zero divisor of
`Ainf`. 

### `instance : IsTorsionFree Ainf L.Ambient`

 The module `W(C♭) ⊗ L` has no `Ainf`-torsion. 

 ### A frame of the lattice

The proof of `frame_theorem` reads everything off a frame of `L` (`Frame`): the period matrix
`(E * τ) ^ a • M` of `L`, with `a = L.jumpBound`, and the frame `Q`, `Q'`, `Z`, `Y`, `B` that
`New.Lift.Chart.IsPeriodMatrix.exists_frame` gives for it. 

### `latticeVec`

 The vector `∑ i, t i • (1 ⊗ e i)` of `L.ainfLattice` with coordinates `t` in the basis
`e = finBasis ℤ_[p] L.Carrier`. 

### `frobPowToBdR`

 The ring map `Bmax → BdR` that applies `φ ^ m` and then maps to `BdR`. 

### `Frame`

 A frame of the lattice `L`, with `a = L.jumpBound`: a period matrix `U` made from an invertible
matrix `M` (`New.Lift.Chart.IsPeriodMatrixOf`), the matrices `Q`, `Q'`, `Z`, `Y`, `B` of
`New.Lift.Chart.IsPeriodMatrix.exists_frame`, and vectors `n i` such that `τ ^ a • n i` is the
vector of `L.ainfLattice` with coordinates the column `i` of `Q`. 

### `Frame.M`

 An invertible matrix over `Bmax` with invariant columns. 

### `Frame.U`

 The period matrix, over `BPlus`. 

### `Frame.v`

 The unit `μ / (E * τ)` of `Ainf`. 

### `Frame.isPeriodMatrixOf`

 The period matrix is made from `M` by the factor `(E * τ) ^ a`, with unit `v`. 

### `Frame.Q`

 The frame matrix over `Ainf` whose columns give the basis. 

### `Frame.Q'`

 An inverse of `Q` up to `τ ^ (a + a)`. 

### `Frame.Z`

 The matrix over `BPlus` with entries in `k.bicommutant` that carries `U` to
  `E ^ (a + a) • Q`. 

### `Frame.Y`

 An inverse of `Z` up to `E ^ (a + a)`. 

### `Frame.B`

 The matrix over `S` through which the Frobenius acts on `Q`. 

### `Frame.Q_mul_Q'`

 `Q * Q' = τ ^ (a + a)`. 

### `Frame.Z_mem`

 The entries of `Z` lie in `k.bicommutant`. 

### `Frame.U_mul_Z`

 `U * Z = E ^ (a + a) • Q`. 

### `Frame.Y_mul_Z`

 `Y * Z = E ^ (a + a)`. 

### `Frame.map_frobEnd_Q`

 The Frobenius acts on `Q` by `φ Q = v ^ a • (Q * B)`. 

### `Frame.exists_smul_Z`

 The elements of `FixesThetaZ` act on `Z` through matrices over `Ainf`. 

### `Frame.n`

 The vectors `τ ^ (-a) • Qᵀ i`. 

### `Frame.tau_pow_smul_n`

 `τ ^ a • n i` has the coordinates of the column `i` of `Q`. 

### `nonempty_frame`

 Every lattice has a frame. 

### `comb`

 The combination `F.comb m t = ∑ i, t i • φ ^ m • F.n i`. 

### `smul_comb_eq_latticeVec`

 `(φ ^ m τ ^ a) • F.comb m t`, with `a = L.jumpBound`, is the vector of `L.ainfLattice` with
coordinates `φ ^ m Q * t`. 

### `tau_pow_smul_sum_eq_latticeVec`

 `τ ^ a • ∑ i, t i • F.n i`, with `a = L.jumpBound`, is the vector of `L.ainfLattice` with
coordinates `Q * t`. 

### `mem_forms_iff`

 A form `μ` lies in `L.forms` if and only if, for any `m`, its coordinates
`basisValues μ ᵥ* φ ^ m M` in the frame are fixed by every `g ∈ Γ'`. The reason is that the
columns of `M` are invariant. 

### `coord_mem_hodgeFil_zero_and_mem_valueField`

 For a form `μ ∈ L.forms`, each coordinate `(basisValues μ ᵥ* φ ^ m M) ν` lies in `hodgeFil 0`
and in the field `valueField 0`, being fixed by `Γ'`. 

### `frobE_pow_smul_apply_comb`

 The values of a form on `F.comb m t` in terms of the frame: with `a = L.jumpBound`,
`φ ^ m E ^ a • μ (F.comb m t)` is the product of the coordinates `basisValues μ ᵥ* φ ^ m M` with
`φ ^ m Z * t`. 

### `frobE_pow_mul_apply_smul_n`

 The case `t = Pi.single i 1` of `frobE_pow_smul_apply_comb`: the value of a form on
`φ ^ m • F.n i`. 

### `n_mem_kisinAinf`

 The frame vectors `F.n i` lie in `L.kisinAinf`. 

### `phi_pow_smul_n_mem_valueFieldPoints`

 Each vector `φ ^ l • F.n i` lies in `L.valueFieldPoints (L.frobKisinAinf l)`: all forms in
`L.forms` take values in the field `valueField 0` on it. 

### `phiInvToBdR_frobE_pow_mul_mem_of_forall_crysForms`

 Crystalline forms detect the coefficients of `F.comb m t`, up to the factor
`φ ^ m E ^ (a + a)` with `a = L.jumpBound`. Let `W` be a `BPlus`-submodule of `BdR`. If
`μ (F.comb m t) ∈ W` for every crystalline form `μ`, then `φ ^ m E ^ (a + a) * t i` maps into `W`
for every `i`. 

### `exists_comb_eq_tau_pow_smul_of_mem_ainfLattice`

 For `x ∈ L.ainfLattice` and `a = L.jumpBound`, `τ ^ a • x` is a combination `F.comb 0 t` of
the `F.n i`. 

### `sum_map_smul_eq_zero_of_sum_smul_eq_zero`

 Clause (a) of `frame_theorem`: an `S`-linear map `f : Ainf → S` carries a linear relation among
vectors of `L.valueFieldPoints L.fracSpan` to the relation with coefficients `f (c i)`. 

### `exists_smul_comb_eq_of_dvd`

 If `w` divides every coefficient `t i`, then `F.comb 0 t` is `w` times a combination of the
`F.n i`. 

### `comb_phi_pow_smul`

 Applying `φ ^ m` to `F.comb 0 t` gives the combination of the `φ ^ m • F.n i` with the
coefficients `φ ^ m • t i`. 

### `tau_dvd_of_forall_crysForms`

 The test for `τ`: if every crystalline form sends `φ ^ (m + 1) • F.comb 0 t` into `hodgeFil 1`,
for every `m`, then `τ` divides every coefficient `t i`. 

### `exists_comb_eq_of_exists_comb_eq_tau_pow_smul`

 Let `x ∈ L.kisinAinf`. If `τ ^ N • x` is a combination `F.comb 0 t` of the `F.n i`, then so is
`x`: the powers of `τ` are removed one at a time by the test for `τ`. 

### `span_n_eq_kisinAinf`

 The frame vectors `F.n i` span `L.kisinAinf` over `Ainf`. 

### `span_phi_pow_smul_n_eq_valueFieldPoints`

 The vectors `φ ^ l • F.n i` span `L.valueFieldPoints (L.frobKisinAinf l)` over `S`. 

### `linearIndependent_n`

 The vectors `F.n i` are linearly independent over `Ainf`: crystalline forms detect the
coefficients. 

### `span_n_eq_kisinModule`

 The frame vectors `F.n i` span the Kisin module over `S`. 

### `pow_smul_mem_span_of_mem_valueFieldPoints`

 Clause (b) of `frame_theorem`. Let `3 e ≤ p ^ l` and `e A ≤ p ^ l δ`. Then `p ^ (4 δ)` times a
vector `x` of `L.valueFieldPoints (L.frobKisinAinf l)` lies in the `S`-span of the vectors `y`
of that module with `g • μ y - μ y ∈ hodgeFil A` for all `μ ∈ L.forms` and all `g ∈ Γ'`. 

### `exists_mem_bicommutant_of_mem_kisinModule`

 Clause (d) of `frame_theorem`: for a crystalline form `μ` and `y` in the Kisin module,
`E ^ a • μ y` with `a = L.jumpBound` is the image of an element of `k.bicommutant`. 

### `mem_smul_kisinAinf_of_forall_crysForms`

 Clause (e) of `frame_theorem`. Suppose `d` divides `r` whenever `d` divides `E ^ m r` in
`BPlus`. If every crystalline form `μ` has `E ^ n • μ x` in `BPlus ∙ d`, then `x ∈ L.kisinAinf` lies
in `d • L.kisinAinf`. 

### `tau_pow_smul_mem_ainfLattice_of_mem_kisinAinf`

 Clause (f) of `frame_theorem`: `τ ^ a`, with `a = L.jumpBound`, carries `L.kisinAinf` into
`L.ainfLattice`. 

### `tau_pow_smul_mem_kisinAinf_of_mem_ainfLattice`

 Clause (g) of `frame_theorem`: `τ ^ a`, with `a = L.jumpBound`, carries `L.ainfLattice` into
`L.kisinAinf`. 

### `frobEUnit_pow_smul_phi_smul_mem_kisinModule`

 Clause (h) of `frame_theorem`: `E ^ a • φ`, with `a = L.jumpBound` and `E` the unit
`k.frobEUnit 0` of `W(C♭)`, maps the Kisin module into itself. 

### `FrameProperties`

 The properties of `L.kisinAinf` and of the Kisin module `L.kisinModule` given by the frame
theorem, with `a = L.jumpBound`, `S = k.S` the ring of the Kummer chart and `E = k.E`. 

### `FrameProperties.sum_map_smul_eq_zero`

 (a) An `S`-linear map `f : Ainf → S` carries a relation `∑ i, c i • v i = 0` among vectors of
  `L.valueFieldPoints L.fracSpan` to the relation `∑ i, f (c i) • v i = 0`. 

### `FrameProperties.pow_smul_mem_span_of_mem_valueFieldPoints`

 (b) If `3 e ≤ p ^ l` and `e A ≤ p ^ l δ`, then `p ^ (4 δ)` times a vector of
  `L.valueFieldPoints (L.frobKisinAinf l)` lies in the `S`-span of the vectors `y` of that module
  with `g • μ y - μ y ∈ hodgeFil A` for every `μ ∈ L.forms` and every `g ∈ Γ'`. 

### `FrameProperties.kisinAinf_eq_span_kisinModule`

 (c) `L.kisinAinf` is the `Ainf`-span of the Kisin module. 

### `FrameProperties.exists_mem_bicommutant_pow_smul_eq`

 (d) For a crystalline form `μ` and `y` in the Kisin module, `E ^ a • μ y` is the image of an
  element of `k.bicommutant`. 

### `FrameProperties.mem_smul_kisinAinf_of_forall_crysForms`

 (e) Let `d ∈ Ainf` divide `r` whenever it divides `E ^ m r` in `BPlus`. Then `x ∈ L.kisinAinf`
  lies in `d • L.kisinAinf` once, for one `n`, `E ^ n • μ x ∈ BPlus ∙ d` for every crystalline form
  `μ`. 

### `FrameProperties.tau_pow_smul_mem_ainfLattice`

 (f) `τ ^ a` carries `L.kisinAinf` into `L.ainfLattice`. 

### `FrameProperties.tau_pow_smul_mem_kisinAinf`

 (g) `τ ^ a` carries `L.ainfLattice` into `L.kisinAinf`. 

### `FrameProperties.frobEUnit_pow_smul_phi_smul_mem_kisinModule`

 (h) `E ^ a • φ`, with `E` the unit `k.frobEUnit 0` of `W(C♭)`, maps the Kisin module into
  itself. 

### `FrameProperties.exists_span_eq_kisinModule_linearIndependent`

 (i) Some vectors `v i`, one for each index of a basis of `L`, span the Kisin module over `S`,
  span `L.kisinAinf` over `Ainf`, and are linearly independent over `Ainf`. 

### `frame_theorem`

 The frame theorem for the lattice `L` over the Kummer chart `k`: `L` has the nine properties of
`FrameProperties`. This gives part of Kisin's theorem: it shows `E ^ a φ N ⊆ N` but not the
finite-height inclusion `E ^ n N ⊆ S φ N`. That theorem concerns the module attached to a
crystalline lattice, for Kummer charts. 

### `kisinAinf_eq_span_kisinModule`

 `kisinAinf` is the A_inf-module of those x in A_inf[1/τ] ⊗ L with μ(φ^n x) ∈ B_dR⁺ for all n ≥ 1
and all Γ'-equivariant forms μ (`forms`). It equals the A_inf-span of the Kisin module
`kisinModule`, the S-module of its elements on which all these forms take values in the field
`k.valueField 0`. This is the field `kisinAinf_eq_span_kisinModule` of `frame_theorem`. 

### `exists_mem_bicommutant_pow_smul_eq_of_mem_kisinModule`

 Let `μ` be a crystalline invariant form of `L` (`crysForms`: an invariant functional
W(C^♭) ⊗ L → `BdR` whose restriction to 1 ⊗ L comes from a ℤ_p-linear map L → `Bmax`), and let `y`
be a vector of the Kisin module of `L`. Let `jumpBound` be the least a such that all Hodge–Tate
jumps of `L` lie in [−a, a]. Then `E ^ jumpBound • μ y` is the image in `BdR` of an element of
`bicommutant`, the ring S_B ⊂ `BPlus` of the chart, which is the closure of S[E/p] in `BPlus` with p
inverted. 

### `mem_smul_kisinAinf_of_crysForms`

 Crystalline forms detect divisibility in `kisinAinf`. Let powers of `E` cancel from `d`: if `d`
divides `E ^ m * r` in `BPlus`, then `d` divides `r` in `Ainf`. If `x` lies in `kisinAinf` and, for
one `n`, the values `E ^ n • μ x` of all crystalline invariant forms `μ` are `BPlus`-multiples of
`d`, then `x` lies in `d • kisinAinf`. 

### `tau_pow_jumpBound_smul_mem_ainfLattice_of_mem_kisinAinf`

 Multiplication by `tau ^ jumpBound` maps `kisinAinf` into `ainfLattice`. 

### `tau_pow_jumpBound_smul_mem_kisinAinf_of_mem_ainfLattice`

 Multiplication by `tau ^ jumpBound` maps `ainfLattice` into `kisinAinf`. 

### `exists_span_eq_kisinModule_linearIndependent`

 For a jump lattice `L`, there is a family `v` in W(C^♭) ⊗ L, indexed by `Fin` of the ℤ_p-rank of
`L`, that is linearly independent over `Ainf`. Its `S`-span is the Kisin module of `L`, and its
`Ainf`-span is `kisinAinf`, the A_inf-module of the x in A_inf[1/τ] ⊗ L with μ(φ^n x) ∈ B_dR^+ for
all n ≥ 1 and all invariant forms μ. 

### `valueFieldPoints_frobKisinAinf_eq_span`

 For a jump lattice `L` (a finite free `O`-module with a `Γ`-action, crystalline over `Γ'`), the
vectors of `L.frobKisinAinf l`, the image of `kisinAinf` under `φ ^ l`, on which all forms in
`L.forms` take values in the field `valueField 0` ⊂ B_dR form the `S`-span of the image of the Kisin
module `L.kisinModule` under `φ ^ l`. 

### `mem_saturateBy_of_mem_kisinAinf`

 Some power of `tau` multiplies a vector of `kisinAinf` into `ainfLattice`. 

### `free_kisinModule`

 For a jump lattice `L` (a finite free `O`-module with a `Γ`-action, crystalline over `Γ'` of the
Kummer chart `k`), the Kisin module is free over `S`. This module consists of the x in `kisinAinf`
on which all `Γ'`-equivariant forms take values in the field `valueField 0`. 

### `saturateBy_tau_span_kisinModule`

 After inverting `tau`, the `Ainf`-span of the Kisin module and `ainfLattice` agree: they have
the same saturation by the powers of `tau`. This is a case of the comparison over `A_inf[1/μ]` for
Breuil–Kisin–Fargues modules (Bhatt–Morrow–Scholze 2018, Lemma 4.26), before the Frobenius twist. 

### `mem_kisinAinf_iff_crysForms`

 In W(C^♭) ⊗ L, `kisinAinf` is the A_inf-module of those `x` in A_inf[1/τ] ⊗ L with
μ(φ^n x) ∈ B_dR⁺ for all n ≥ 1 and all μ in `L.forms`. Then `x` lies in `kisinAinf` if
and only if two conditions hold. First, some power of `tau` = [ε^{1/p}] − 1 multiplies `x` into
`ainfLattice`, the A_inf-span of the elements 1 ⊗ y with y in L. Second, for some `n` and every `μ`
in `crysForms`, `E ^ n • μ x` is the image in `BdR` of an element of `BPlus`; here `crysForms` are
the invariant forms whose restriction to 1 ⊗ L comes from a Z_p-linear map L → `Bmax`, and `E` is
`k.E`. 

### `apply_sum_sub_coord₀_smul_eq_zero_of_mem_crysForms`

 Let the vectors `v i` lie in the Kisin module of `L`, and let `u i ∈ Ainf`. Suppose that for
every `ν` in `crysForms` (the invariant A_inf-linear functionals to B_dR whose restriction to 1 ⊗ L
comes from a Z_p-linear map L → B_max), `E ^ n • ν (∑ i, u i • v i)` is the image in `BdR` of an
element of `bicommutant`, the elements of B^+ = A_max[1/p] whose multiplication commutes with every
S-linear endomorphism of B^+ preserving the image of A_max. Then every `μ` in `crysForms` vanishes
on `∑ i, (u i - k.coord₀ (u i)) • v i`, where `k.coord₀ (u i)` is the coordinate of `u i` in S for
the chosen topological basis of `Ainf` over S, i.e. the coordinate that is the identity on S. 

### `mem_kisinModule_iff_crysForms`

 Let `x` be a vector of W(C^♭) ⊗ L, for a lattice `L` with jump sets over the Kummer chart `k`
with ring S. Then `x` lies in the Kisin module of `L` if and only if two conditions hold. First,
some power of `tau` = [ε^{1/p}] − 1 multiplies `x` into `ainfLattice`, the A_inf-span of the 1 ⊗ y
with y in L. Second, for some `n` and every `μ` in `crysForms` (the invariant A_inf-linear
functionals to B_dR whose restriction to 1 ⊗ L comes from a Z_p-linear map L → B_max), `E ^ n • μ x`
is the image in `BdR` of an element of `bicommutant`, the elements of B^+ = A_max[1/p] whose
multiplication commutes with every S-linear endomorphism of B^+ preserving the image of A_max, which
equals `adjoinEDivPClosure` by `Chart.adjoinEDivPClosure_eq_bicommutant`. 

 ## Galois elements normalising a subgroup 

### `pow_smul_gal_sub_mem_span_of_dvd`

 For the Kummer chart `k`, let `k.bicommutant` be its ring S_B: the elements of `BPlus` whose
multiplication commutes with every `k.S`-linear map of `BPlus` keeping the image of A_max,
equivalently the closure of `S[E/p]` in `BPlus` with `p` inverted. Let `E` be the chart's element
`k.E`. If `g ∈ G_p` and `d ∈ BPlus` are such that `d` divides `g • y - y` for every `y` in
`k.bicommutant`, and `x ∈ BdR` has `E ^ m • x` equal to the image of an element of `k.bicommutant`,
then `E ^ (2 * m) • (g • x - x)` is a `BPlus`-multiple of the image of `d` in `BdR`. 

### `conjForm_mem_forms`

 Let `g ∈ Γ` satisfy `g Γ' g⁻¹ ⊆ Γ'`, and let `μ` be a `Γ'`-equivariant form (`forms`). Then the
conjugate `conjForm μ g`, the form `y ↦ g⁻¹ • μ (g • y)`, is `Γ'`-equivariant. 

### `smul_mem_kisinAinf`

 Let `g ∈ Γ` satisfy `g Γ' g⁻¹ ⊆ Γ'`. Then `g`, acting through `inr`, maps the module `kisinAinf`
of `L` into itself. 
