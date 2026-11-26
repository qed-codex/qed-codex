---
{
  "module": "src/Lib/PadicHodge/Kisin/PeriodMatrixBasis.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Kisin/PeriodMatrixBasis.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Kisin/PeriodMatrixBasis.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Period matrices over a chart: lattice bases and existence for crystalline lattices

This file studies period matrices over a chart `c` (`New.Lift.Chart`). `A_inf ⊂ B⁺ = A_max[1/p]` are
the period rings `New.Period.Ainf`, `New.Period.BPlus`, and `amaxImage` is the image of `A_max` in
`B⁺`. A chart gives a subring `S` of `A_inf` with elements `z` and `E`. Here `E` is `ξ` times a
unit, and `ξ` generates the kernel of `θ`. `S_B` denotes `New.Lift.Chart.bicommutant`. Write
`μ = [ε] - 1` (`New.Period.mu`) and `τ = [ε^{1/p}] - 1` (`New.Period.tau`). Then `E τ` is `μ` times
a unit.

## Main definitions and results

* `New.Lift.Chart.IsPeriodMatrix`: period matrices `U` over `B⁺` of height `h`.
* `New.Lift.Chart.IsPeriodMatrix.exists_basis`: a basis `Q`, `Z` for `U`
  (`New.Lift.Chart.IsPeriodBasis`): the `x` over `A_inf` with `E ^ h x ∈ U S_B ^ d` are the `S`-span
  of the columns of a nonsingular matrix `Q`.
* `New.Lift.Chart.IsChartOf.exists_mem_bicommutant_of_fixed`: elements of `New.Period.Bmax` fixed by
  `Γ` come from `c.bicommutant`, an `S`-subalgebra of `New.Period.BPlus` in which `p` is invertible
  (defined as a commutant, `New.Lift.Chart.bicommutant`).
* `New.Lift.Chart.IsChartOf.exists_isPeriodMatrixOf`: if the Hodge–Tate jumps lie in `[-a, b]`, an
  invariant basis `M` gives the period matrix `(E τ) ^ a M` of height `a + b`
  (`New.Lift.Chart.IsPeriodMatrix`).

Notions from other files:
* `New.Period.mu`, `New.Period.tau`, `New.Period.xi`: The elements μ = [ε] − 1, τ = [ε^{1/p}] − 1
  and ξ = ∑_{i<p} [ε^{1/p}]^i of A_inf, with ξτ = μ; brackets denote Teichmüller lifts, and ε = (1,
  ζ_p, ζ_{p²}, …) is `New.Period.epsTilt`.
* `New.Lift.Chart.z`, `New.Lift.Chart.E`: For a chart, the images in S of X and of the series X^e
  A + p, A a unit of Λ[[X]]. Here Λ = `New.Lift.WittFq` = W(F_{p^f}).
* `New.Period.jump`: The multiplicity of an integer as a Hodge–Tate jump of ρ at an embedding.
* `New.Lift.Chart.IsChartOf`: The field of the chart contains the field fixed by the image of j:
  Γ → G_p: every g in G_p that fixes Λ pointwise and fixes θ(z) lies in the image of j.
* `New.Lift.Chart.extendToBPlus`: a chosen `S`-linear extension to `B⁺` of an `S`-linear map
  `A_inf → A_inf`; it maps `amaxImage` into itself.
* `New.Period.frobEnd`: the Frobenius endomorphism `φ` of the period rings.

## Relation to the literature

Known; see `Lib.PadicHodge.Kisin.PeriodMatrixFrame` for sources.



## Lifting the exponent and bases for period matrices

Denominators are bounded uniformly: first in `A_max`, then in `A_inf` by
`New.Period.exists_Ainf_eq_of_contraction`.


 ### Lifting the exponent 

### `isUnit_geom_sum`

 If `x - 1` is not a unit of `A_inf` and `p ∤ m`, then `1 + x + ⋯ + x ^ (m - 1)` is a unit. 

### `lifting_the_exponent`

 Lifting the exponent. Let f: A_inf → R be a surjective ring map, v a non-unit dividing x − 1,
with p·f(x − 1)·f(v) dividing f(x − 1)^p. For n ≠ 0, f(x^n − 1) divides p^{v_p(n)} f(x − 1). 

### `tau_pow_dvd_of_frobEnd_tau_pow_dvd`

 Let `b` be in `B⁺` and let `φ` be `frobEnd`. If `φ(τ) ^ n` divides `φ(b)`, then `τ ^ n` divides
`b`. The case `n = 1`: if `φ(τ)` divides `φ(a)`, then `θ(φ^j a) = 0` for all `j ≥ 1`, which gives
`τ ∣ a`. 

### `associated_E_mul_tau_mu`

 `E τ` and `μ` are associated in `A_inf`, as `E` is `ξ` up to a unit and `ξ τ = μ`. 

### `associated_smul_E`

 `E` is associated in `A_inf` to its translate `g E` by any `g` in `Gal(ℚ̄_p/ℚ_p)`. 

### `associated_teichmuller_pow_p_pow_sub_one`

 For every `a`, the element `[ε] ^ p ^ a - 1 = φ^a μ` of `A_inf` is associated to the product
of `τ = [ε^{1/p}] - 1` and the `φ^b E = c.frobE b` for `b ≤ a`. Here `[ε]` is the Teichmüller lift
of `epsTilt`. 

### `associated_teichmuller_pow_sub_one`

 For a chart `c`, take `S` to be its ring inside `A_inf` and `φ` the Frobenius of `S`. The chart
is a Λ-algebra map Λ[[X]] → A_inf sending a series X^e A + p to `E`, which is ξ times a unit. Then
for `n ≠ 0`, the element `[ε] ^ n - 1` of `A_inf` is associated to the product of
`τ = [ε^{1/p}] - 1` with the `φ^a(E) = c.frobE a` for `a ≤ v_p(n)`, where `[ε]` is the Teichmüller
lift of `epsTilt`, ε = (1, ζ_p, ζ_{p²}, …) ∈ O^♭. 

### `exists_tau_mul_E_eq_mul_epsTilt_pow_sub_one`

 For `n ≠ 0`, the element `[ε] ^ n - 1` divides `τ E (p ^ v_p(n) + β z)` in `A_inf` for some
`β`. 

### `IsPeriodMatrix`

 `U` over `B⁺` is a period matrix of height `h`, with the unit `v` of `A_inf` as Frobenius
factor: `U` divides `(E τ) ^ h`; `φ(U) = v U F` with `F` over `S_B` and invertible over `B⁺`; every
`g` satisfying `c.FixesThetaZ` (`g` fixes Λ pointwise and fixes θ(z)) acts on `U` through matrices
over `A_inf`; and divisibility of `U y` by `E ^ h` is kept when `c.extendToBPlus f` is applied to
`y`. 

### `IsPeriodMatrix.exists_mul_eq_smul_one`

 `U` divides the scalar matrix `(E τ) ^ h` over `B⁺`; here `E τ` is `μ` up to a unit. 

### `IsPeriodMatrix.exists_frob`

 `φ(U) = v U F` for a matrix `F` with entries in `S_B` that has a left inverse over `B⁺`. 

### `IsPeriodMatrix.exists_gal`

 If `g` satisfies `c.FixesThetaZ`, then `U = ρ g(U)` for a matrix `ρ` over `A_inf`. 

### `IsPeriodMatrix.extendToBPlus_stable`

 If `E ^ h` divides `U y`, it divides `U y'`, where `y'` is `y` with the extension
  `c.extendToBPlus f` of an `S`-linear map `f` applied to each coordinate. 

### `E_ne_zero`

 `E` is nonzero, being associated to the prime `ξ`. 

### `E_ne_zero'`

 `E` is nonzero as an element of the subring `S`. 

### `frobEnd_extendToBPlus_eq_extendToBPlus_frobEnd_of_comm`

 Let `f`, `f'` be `S`-linear maps `A_inf → A_inf` with `φ ∘ f' = f ∘ φ`, where `φ` is `frobEnd`.
Then the same holds for their extensions `c.extendToBPlus` to `B⁺`: the difference of the two
sides is additive, keeps `amaxImage` and vanishes on the image of `A_inf`. 

### `frobeniusConj`

 Let `ψ` be a right inverse of `φ = frobEnd` on `A_inf`, and let `φ` be injective. For an
`S`-linear map `f` on `A_inf`, the map `ψ ∘ f ∘ φ` is again `S`-linear, since `φ` maps `S` into
itself. 

### `exists_p_pow_mul_mem_amaxImage`

 Let `e` divide `μ`. There is `k`, depending only on `U`, `h` and `e`, such that
`U y = e ^ h w` with `y` over the image of `A_max` puts `p ^ k w` over the image of `A_max`. 

### `exists_mulVec_eq_smul_of_frobEnd`

 Let `W` invert `U` up to `(E τ) ^ h`, let `F'` be a left inverse of `F`, and suppose that
`U a = r x'` implies `F φ(a) = φ(r) y` for every `r` in `A_inf` and `a` over `B⁺`, where `φ` is
`frobEnd`. Then `U y' = E ^ h x'` has a solution `y'` over `B⁺`: `φ (W x')` is divisible by
`φ(τ) ^ h`, hence `W x'` by `τ ^ h` (`tau_pow_dvd_of_frobEnd_tau_pow_dvd`), and
`y' = τ ^ (-h) W x'`. 

### `rank_le_card_of_sum_smul_eq_zero_iff`

 Let `P` be an `S`-submodule of `A_inf ^ d` whose members `j` have vectors `y j` over `S_B`
with the same `A_inf`-linear relations as the `j`. Then the rank of `P` over `S` is at most `d`:
the coordinates `c.extendedCoord i` turn an `A_inf`-relation among members of `P` into
`S`-relations. 

### `IsPeriodBasis`

 `Q` over `A_inf` and `Z` over `B⁺` form a basis for the period matrix `U` of height `h`: `Q` is
nonsingular, `Z` lies over `c.bicommutant` with `U Z = E ^ h Q`, the columns of `Q` span the `x`
that have solutions over `c.bicommutant`, and `Q` controls divisibility for solutions over `B⁺`. 

### `IsPeriodBasis.det_ne_zero`

 `Q` is nonsingular. 

### `IsPeriodBasis.mem_bicommutant`

 The entries of `Z` lie in `c.bicommutant`. 

### `IsPeriodBasis.mul_eq`

 `U Z = E ^ h Q` over `B⁺`. 

### `IsPeriodBasis.exists_mulVec_eq`

 Every `x` over `A_inf` with `U y = E ^ h x` for some `y` over `c.bicommutant` is `Q s` with
  `s` over `c.S`. 

### `IsPeriodBasis.dvd_dotProduct`

 If `U y = E ^ h x` with `y` over `B⁺`, `p ∤ δ` and `l Q = δ g`, then `δ` divides `l · x`. 

### `mulVec_injective`

 A period matrix acts injectively on vectors over `B⁺`, since `U W` is a nonzero scalar
matrix. 

### `exists_mulVec_mulVec_eq_smul`

 The field `exists_mul_eq_smul_one` read on vectors: there is a matrix `W` over `B⁺` with
`U (W x) = (E τ) ^ h x` for every vector `x`. 

### `exists_pow_mul_mem_amaxImage`

 A single power `p ^ m` puts every vector `w` with `U (c.extendToBPlus f ∘ y) = E ^ h w` into
`amaxImage`, where `y` over `B⁺` runs through the solutions of `U y = E ^ h x` with `x` over
`A_inf`, and `f` through the `S`-linear maps `A_inf → A_inf`. 

### `exists_frobenius_preimage`

 Descent along Frobenius. Let `U` be a period matrix of height `h` with Frobenius factor `v` for
the chart `c` (`IsPeriodMatrix`), and let `f` be a `c.S`-linear map of `A_inf`. Suppose
`U y = E ^ h x` with `x` over `A_inf`, and `U (c.extendToBPlus f ∘ y) = E ^ h w`. Then there are
`x'`, `y'`, `w'`, `f'` satisfying the same two equations with `φ w' = v E ^ h w`, where `φ` is
`frobEnd`. The proof takes `x' = φ⁻¹ (v E ^ h x)` and `f' = φ⁻¹ f φ`. 

### `exists_ainfToBPlus_eq_pow_mul`

 Let `U` be a period matrix of height `h` with Frobenius factor `v` for the chart `c`
(`IsPeriodMatrix`). A single power `p ^ N` puts into the image of `A_inf` every vector `w` with
`U (c.extendToBPlus f ∘ y) = E ^ h w`, for every `c.S`-linear map `f` of `A_inf` and every `y` over
`BPlus` with `U y = E ^ h x`, `x` over `A_inf`. These vectors lie in `amaxImage` after one power of
`p` and are closed under descent along Frobenius, so `exists_Ainf_eq_of_contraction` applies. 

### `exists_spanning_matrix`

 Let `U` over `B⁺` be a period matrix of height `h` with Frobenius factor `v`. The `x` over
`A_inf` for which `U y = E ^ h x` has a solution `y` with entries in `S_B` (`c.bicommutant`, the
closure of `S[E/p]` in `B⁺` with `p` inverted) form an `S`-module spanned by the columns of a square
matrix `Q` over `A_inf`; moreover `U Z = E ^ h Q` for a matrix `Z` with entries in `S_B`. 

### `dvd_dotProduct_of_dvd_dotProduct_pow_smul`

 If `p` does not divide `δ`, then `δ ∣ l · (p ^ n x)` gives `δ ∣ l · x`. 

### `exists_dotProduct_pow_smul_sub_mul_mem_span_pow`

 The approximation step of `dvd_dotProduct_of_spanning`. Let `U` be a period matrix of height `h`
with Frobenius factor `v` for `c` (`IsPeriodMatrix`). Let `Q` over `A_inf` be such that every `x`
with `U y = E ^ h x` for some `y` over `S_B = c.bicommutant` equals `Q s` with `s` over `c.S`. Let
`U y = E ^ h x` with `x` over `A_inf` and `y` over `BPlus`, and let `l Q = δ g` over `A_inf`. Then
for some `N` and every `m`, some `z` has `l · (p ^ N x) - δ z` in the ideal `(p, ξ) ^ m` of
`A_inf`. 

### `dvd_dotProduct_of_spanning`

 Let `U` be a period matrix of height `h` (`hU`), and let `Q` span the solutions over
`c.bicommutant` (`hQ`): every `x` over `A_inf` with `U y = E ^ h x` for some `y` over
`c.bicommutant` is `Q s` with `s` over `c.S`. Let `U y = E ^ h x` with `y` over `B⁺` only. If `δ`,
not divisible by `p`, divides the row `l Q` (`l Q = δ g`), then `δ` divides `l · x`. 

### `exists_basis`

 Every period matrix `U` has a basis `Q`, `Z` in the sense of `New.Lift.Chart.IsPeriodBasis`:
the nonsingular `Q` over `A_inf` spans the `x` with `U y = E ^ h x` solvable over `c.bicommutant`,
and `U Z = E ^ h Q`. 


## Period matrices of crystalline lattices with bounded jumps

`ρ` is a representation of `Γ` on a free `ℤ_p`-module with basis `e` (matrices
`New.Period.repMatrix ρ e g`), `𝒥.toGp` maps `Γ` onto an open subgroup of `Gal(ℚ̄_p/ℚ_p)`, and `c`
is a chart for it (`hc : IsChartOf c 𝒥.toGp`). Here `Bmax = BPlus [1/μ]`, `BdRPlus ⊂ BdR` with
`t = tUnit`, `hodgeMatrix P k = P diag (t ^ k i)`, `hodgeFil s` is the filtration `t ^ s BdRPlus`,
and the prime `p` is fixed by the instance `[ThePrime p]`.


### `_root_.New.Period.HasInvariantColumns`

 The columns of `M` are the coordinates, in the basis `e`, of vectors of `B ⊗ T` fixed by `Γ`:
`ρ(g) * g M = M`, where `ρ(g)` is the matrix of `ρ g` in `e` and `g` acts on entries through
`toGp`. 

### `IsPeriodMatrixOf`

 `U` over `BPlus` is the period matrix of `ρ` in the basis `e` made from the matrix `M` over
`Bmax` with invariant columns by the factor `(E τ) ^ a`. Here `v` is the unit `μ / (E τ)`. Its
height is `a + b` and its Frobenius factor is `v ^ a`. 

### `IsPeriodMatrixOf.hasInvariantColumns`

 The columns of `M` are invariant vectors. 

### `IsPeriodMatrixOf.E_mul_tau_mul`

 The unit `v` is `μ / (E τ)`. 

### `IsPeriodMatrixOf.isPeriodMatrix`

 `U` is a period matrix of height `a + b` with Frobenius factor `v ^ a`. 

### `IsPeriodMatrixOf.map_eq_smul`

 `U = (E τ) ^ a M` over `Bmax`. 

### `_root_.New.Period.matrixAction`

 The action of an element of `FrobGal` on matrices over `Bmax`, entry by entry; `(.ofAdd n, 1)`
acts as `φ ^ n` and `(1, g)` as `g` in `Gal(ℚ̄_p/ℚ_p)`. 

### `_root_.New.Period.frobTwist`

 The twist `φ ^ n M` of an invertible matrix over `Bmax` by a power of Frobenius. 

### `_root_.New.Period.IsCrystalline.exists_hasInvariantColumns`

 A crystalline `ρ` (`Bmax ⊗ T` has a `Bmax`-basis of `Γ`-invariant vectors) has an invertible
matrix over `Bmax` with invariant columns. 

### `_root_.New.Period.HasInvariantColumns.frobTwist`

 Frobenius commutes with the Galois action, so `φ ^ n M` has invariant columns if `M` has. 

### `_root_.New.Period.HasInvariantColumns.exists_hodge_frame`

 An invertible matrix `M` over `Bmax` with invariant columns has a Hodge frame
`M Y = W diag (t ^ k i)` with `Y` fixed by `Γ`, and this product has invariant columns. 

### `_root_.New.Period.HasInvariantColumns.jump_ne_zero`

 If `W diag (t ^ k i)` has invariant columns, then each `k i` is a Hodge–Tate jump of `ρ`. 

### `_root_.New.Period.mem_hodgeFil_of_mul_eq_hodgeMatrix`

 A matrix `B` with `B Q = P diag (t ^ k i)`, `Q` invertible over `BdRPlus` and `s ≤ k i` for all
`i`, has entries in `hodgeFil s`. 

### `exists_map_eq_pow_smul`

 If all Frobenius twists of `B` have entries in `hodgeFil (-m)`, then `(E τ) ^ m B` lies over
`BPlus`. 

### `exists_map_eq_pow_smul_of_hasInvariantColumns`

 Let the jumps of `ρ` lie in `[-a, b]` and let `M` be invertible over `Bmax` with invariant
columns. Then `(E τ) ^ a M` and `(E τ) ^ b M⁻¹` lie over `BPlus`. 

### `IsChartOf.exists_mem_bicommutant_of_fixed`

 Let `c` be a chart for `toGp` (`hc`). An element of `Bmax` fixed by `Γ` comes from
`c.bicommutant`. 

### `IsChartOf.exists_transition_matrix`

 Let `c` be a chart for `toGp` (`hc`). The transition matrix of two invertible matrices with
invariant columns has entries in `c.bicommutant`. 

### `IsChartOf.exists_mulVec_extendToBPlus_eq_smul`

 Let `c` be a chart of `𝒥.toGp : Γ →* G_p` (`hc`), let `M` be invertible over `Bmax` with columns
`Γ`-invariant for `ρ` in the basis `e`, and let `U` over `BPlus` have image `(c.E * tau) ^ a • M` in
`Bmax`. If `U y = E ^ n w` for some `w` over `BPlus`, then `U (c.extendToBPlus f ∘ y) = E ^ n w'`
for some `w'`. Here `c.extendToBPlus f` is the chosen extension to `BPlus` of the `c.S`-linear map
`f` of `A_inf`. 

### `IsChartOf.exists_isPeriodMatrixOf`

 Let `c` be a chart of `𝒥.toGp : Γ → G_p` (`hc`), let `ρ` be crystalline with Hodge–Tate jumps at
the identity embedding in `[-a, b]`, and let `e` be a `ℤ_p`-basis of `T`. Then there are an
invertible matrix `M` over `Bmax`, whose columns (in the basis `e`) are invariant under
`toGp g ⊗ ρ g` for all `g`, and a unit `v = μ / (E τ)` of `Ainf`. With these, `U = (E τ) ^ a M` is a
period matrix of `ρ` over `BPlus` of height `a + b` with Frobenius factor `v ^ a`
(`IsPeriodMatrixOf`).

This does part of the work usually done by Kisin's theorem on the module attached to a crystalline
lattice: it supplies only a period matrix over `B⁺` for jumps in `[-a, b]`, not the Frobenius-stable
submodule itself. 
