---
{
  "module": "src/Lib/DiscreteSeries/Bessel/UnipotentHaarMeasure.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/UnipotentHaarMeasure.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/UnipotentHaarMeasure.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Haar measures on the Bessel unipotent groups 𝖴⁰ ⊆ 𝖴 and σ-finiteness on G₁

Let `𝔰` be a shape and let 𝖴⁰ ⊆ 𝖴 be the Bessel unipotent subgroups (`New.Shape.Form.besselU0`,
`New.Shape.Form.besselU`) of the unitary group `𝔰.G₁`, which is `(𝔰.middleGram 1).G` (so 𝖴⁰ is
`(𝔰.middleGram 1).besselU0`). The elements of 𝖴 are block upper unitriangular for the levels of the
basis indices, and 𝖴⁰ also fixes the frame e_0, …, e_{ϱ-1}, z. The measures `New.Shape.besselHaar₀`
on 𝖴⁰ and `New.Shape.besselHaar` on 𝖴 are images of Lebesgue measure under explicit
parametrisations.

## Main definitions and results

* `New.RealPlace.injective_freeEntries_besselU0`, `New.RealPlace.injective_freeEntries_besselU`: the
  free entries (`New.RealPlace.freeEntries`: the entries at the free positions in the rows e_a, plus
  the imaginary parts at (e_a, e*_a)) are injective on 𝖴⁰ and on 𝖴.
* `New.RealPlace.measurePreserving_freeEntries_besselHaar₀`,
  `New.RealPlace.measurePreserving_freeEntries_besselHaar`: the free entries carry these measures to
  Lebesgue measure.
* `New.RealPlace.isUnimodularHaar_besselHaar₀`: `New.Shape.besselHaar₀` is a two-sided Haar measure
  (`New.RealPlace.IsUnimodularHaar`). An instance gives the same for `New.Shape.besselHaar`.
* `New.RealPlace.eichlerVectors`, `New.RealPlace.eichlerScalars`: the matrices ω and μ that describe
  an element of 𝖴⁰ as an Eichler map with matrix entries (`New.RealPlace.eichlerMatrix`).
* `New.RealPlace.homogeneousBall`: the balls ‖ω‖ ≤ ρ, ‖μ‖ ≤ ρ² in 𝖴⁰. Radii add under multiplication
  (`New.RealPlace.mul_mem_homogeneousBall`), and the volume is proportional to a power of the radius
  (`New.RealPlace.besselHaar₀_homogeneousBall`).
* `New.RealPlace.exists_tube`: there is a compact set whose slices along 𝖴⁰ have controlled measure
  (`New.RealPlace.IsTube`).

Notions from other files:
* `New.Shape.G₁`: The unitary group of the complex hermitian form made of ϱ hyperbolic planes, the
  standard positive form on κ, and one vector z with h(z, z) = −1.
* `New.Shape.BesselIndex`: The index set of the basis e_a; x_i (i in κ), z; e*_a, where a runs over
  `Fin ϱ`. The level is a at e_a, ϱ on the middle block and 2ϱ − a at e*_a (a counted from 0).

## Relation to the literature

No Bessel model is constructed here. This file gives coordinates and Lebesgue–Haar measure on the
unipotent radical and on its subgroup fixing the frame, balls and tubes for the latter, and the
σ-finiteness of Haar measures on the ambient unitary group. Source for the setting: H. Xue, Bessel
models for real unitary groups: the tempered case, Duke Math. J. 172 (2023) 995-1031; R.
Beuzart-Plessis, Astérisque 418 (2020).



## Unimodular Haar measures on 𝖴 and 𝖴⁰, dilations and tubes

Right translations act on the free entries by volume preserving maps
(`New.RealPlace.exists_measurePreserving_freeEntries`), which gives right invariance. Conjugations
by the Bessel subgroup keep Haar measure (`New.RealPlace.measurePreserving_conj_bessel`) because
dilations (`New.RealPlace.exists_dilation`) conjugate each element of 𝖴 into one fixed ball.
`New.RealPlace.IsUnimodularHaar.of_freeEntries` combines the two for a subgroup of 𝖴 cut out by
prescribing entries.


### `mem_besselU0_iff_apply`

 𝖴⁰ is cut out by entries: an element u of G₁ lies in 𝖴⁰ if and only if its entries agree with
those of the identity matrix at every position (i, j) on or below the level diagonal
(level j ≤ level i) and at every position in a column of the frame e_0, …, e_{ϱ-1}, z. 

### `continuous_embedH`

 The embedding `New.RealPlace.embedH` of U(κ) in G₁ is continuous. 

### `IsUnimodularHaar`

 The measure ν on the subgroup S of G₁ is a σ-finite left Haar measure that is also right
invariant, invariant under inversion, and satisfies `New.HasCutoff` for the action of S on G₁: some
measurable weight on G₁ has integral one over each orbit. 

 ### The dilation and conjugation invariance 

### `exists_dilation`

 Dilations. For T ≥ 1 there is a d in G₁ such that conjugation u ↦ d⁻¹ud multiplies the matrix
entry (i, j) by T^{level i − level j}, and ‖d⁻¹ud‖ ≤ 1 + r²‖u‖/T for u in the Bessel unipotent group
𝖴 (`besselU`). Here ϱ is the number of hyperbolic planes, r = `𝔰.r` the number of basis indices, and
the level is a at e_a, ϱ on the middle block and 2ϱ − a at e*_a, with a counted from 0. 

### `measurePreserving_conj_bessel`

 Let `S` be a subgroup of G₁ cut out by asking that the entries at the positions `P` be those of
`1`, and let the Bessel subgroup `New.Shape.Form.besselS` normalise `S`; each of its elements is an
element of 𝖴 times an element `toBesselH w`. Conjugation by an element `s` of the Bessel subgroup
preserves every Haar measure of `S`. 

 ### Lebesgue measure in the free entries is a two-sided Haar measure 

### `exists_measurePreserving_freeEntries`

 Let `S` be cut out by prescribing the entries at the positions `P` to be those of `1`, and let
`p` be the free positions: the pairs `(a, i)` outside `P` in a row e_a with level i < 2ϱ − a. Right
multiplication by `g` in 𝖴 acts on the coordinates `New.RealPlace.freeEntries p` of the elements of
`S` (the entries at the positions in `p` and the imaginary parts of the entries at (e_a, e*_a))
through a volume preserving map `T`. 

### `IsUnimodularHaar.of_freeEntries`

 Let S ≤ 𝖴 be a subgroup of G₁ that is normalised by the Bessel subgroup and is cut out by
prescribing the entries at the positions P to be those of the identity matrix. Give each basis index
a level: i for e_i, ϱ on the middle block, and 2ϱ − i for e*_i. Let p consist of the positions (a,
i) of row e_a that are not in P and have level i < 2ϱ − a. If the coordinates
`New.RealPlace.freeEntries p` are injective on S and carry ν to Lebesgue measure, then ν is a
σ-finite left Haar measure on S that is also right invariant and inversion invariant, and some
measurable weight on G₁ has integral one over each S-orbit (`New.RealPlace.IsUnimodularHaar`). 

### `continuous_unipotentOf`

 `New.RealPlace.unipotentOf`, the parametrisation of 𝖴⁰, is continuous. 

### `continuous_liftUnitriangular`

 `New.RealPlace.liftUnitriangular`, the lift to G₁ (into 𝖴) of the unitriangular (ϱ + 1)×(ϱ + 1)
matrices: its block on the frame e_0, …, e_{ϱ-1}, z has the entries `x : UpperEntries 𝔰.n` above
the diagonal. It is continuous. 

### `isFreeEntry_iff_level`

 The free positions of 𝖴 in row e_a are the columns of level strictly between a and 2ϱ − a. 

### `isFreeEntry₀_iff_level`

 The free positions of 𝖴⁰ in row e_a are the columns outside the frame e_0, …, e_{ϱ-1}, z of
level strictly between a and 2ϱ − a. 

### `sum_isFreeEntry₀_add_sum_diag`

 A sum over the free positions of 𝖴⁰. Let `w` be a function of the positions (row e_a, column i)
and `y` a square array such that `w` at (e_a, e*_b) is `y b a + y a b` for `a < b`. The sum of `w`
over the free positions and of `y` over the diagonal is the sum of `w` over the columns x_i (i in κ)
and of all entries of `y`. 

### `exists_measurePreserving_linearEquiv_freeEntries`

 For q = (a, b) in `𝔰.UnipotentParams`, with a a complex ϱ×κ matrix and b a real ϱ×ϱ matrix, take
the matrix X(aWᴴ + (sk b)Dᴴ) from the linear part of `New.RealPlace.unipotentOf`. Here X, W, D have
columns e_i, x_i, e*_i, and sk is `New.skewOfReal`, the skew-hermitian matrix with real coordinates
b. Its coordinates `New.RealPlace.freeEntries` at the free entries of 𝖴⁰ (`IsFreeEntry₀`: row e_a
with column x_i or e*_b for a < b, plus the imaginary parts at (e_a, e*_a)) are given by a volume
preserving ℝ-linear isomorphism `E` from `𝔰.UnipotentParams` onto
`(Subtype IsFreeEntry₀ → ℂ) × (Fin 𝔰.ϱ → ℝ)`. 

### `exists_freeEntries_unipotentOf_eq_shear`

 The parametrisation `New.RealPlace.unipotentOf` sends q = (a, b), with a a complex ϱ×κ matrix
and b a real ϱ×ϱ matrix, to an element of the frame-fixing unipotent group 𝖴⁰. Read it in the free
entries of 𝖴⁰ (`New.RealPlace.freeEntries` at `New.RealPlace.IsFreeEntry₀`): the complex entries in
row e_a and column x_i (i ∈ κ) or e*_b with a < b, together with the imaginary parts at (e_a, e*_a).
In these coordinates it is a shear (a, b) ↦ (a, b + c(a)) with c continuous, followed by a volume
preserving linear isomorphism E. 

### `injective_freeEntries_besselU0`

 The free-entry coordinates (`New.RealPlace.freeEntries` at `New.RealPlace.IsFreeEntry₀`: the
entries in row e_a and column x_i or e*_b with b > a, together with the imaginary parts at
(e_a, e*_a)) are injective on the unipotent group 𝖴⁰ (`New.Shape.Form.besselU0`) of G₁. 

### `measurePreserving_freeEntries_besselHaar₀`

 The free-entry coordinates (`New.RealPlace.freeEntries` at `New.RealPlace.IsFreeEntry₀`: the
entries in row e_a and column x_i or e*_b with b > a, together with the imaginary parts at (e_a,
e*_a)) carry `New.Shape.besselHaar₀`, the image of Lebesgue measure under
`New.RealPlace.unipotentOf`, to Lebesgue measure. 

### `injective_measurePreserving_freeEntries₀`

 The free entries are coordinates on 𝖴⁰ in which `New.Shape.besselHaar₀` is Lebesgue measure:
they are injective on 𝖴⁰ (`New.RealPlace.injective_freeEntries_besselU0`) and carry this measure
to Lebesgue measure (`New.RealPlace.measurePreserving_freeEntries_besselHaar₀`). 

### `isUnimodularHaar_besselHaar₀`

 `New.Shape.besselHaar₀` is a two-sided Haar measure on 𝖴⁰ with a cutoff for the action on G₁,
in the sense of `New.RealPlace.IsUnimodularHaar`. 

### `injective_freeEntries_besselU`

 Call e_a, for a < ϱ, the first ϱ basis vectors of the Bessel basis e, x_i, z, e*
(`New.Shape.BesselIndex`). The coordinates `New.RealPlace.freeEntries` at
`New.RealPlace.IsFreeEntry` are injective on the Bessel unipotent group 𝖴 (`New.Shape.Form.besselU`)
of G₁. These are the complex entries in row e_a and column e_b or e*_b with b > a, or any column
x_i, z of the middle block, together with the imaginary parts at (e_a, e*_a). 

### `exists_measurableEquiv_freeEntries_eq_prod`

 The free entries of 𝖴 are those of 𝖴⁰ together with the entries above the diagonal
(`UpperEntries 𝔰.n`, with n = ϱ + 1) of the block on the frame e_0, …, e_{ϱ-1}, z. Regrouping
the coordinates accordingly preserves volume. 

### `measurePreserving_freeEntries_besselHaar`

 Let 𝖴 be the Bessel unipotent group of G₁ (`New.Shape.Form.besselU` for
`New.Shape.middleGram 1`). Its elements are the isometries of the hermitian form made of ϱ
hyperbolic planes (basis e_a, e*_a), the standard positive form on κ and a vector z with
h(z, z) = −1, that are block upper unitriangular in the basis e_0, …, e_{ϱ-1}, x_i, z,
e*_{ϱ-1}, …, e*_0. The free-entry coordinates (`New.RealPlace.freeEntries` at
`New.RealPlace.IsFreeEntry`) carry `New.Shape.besselHaar` on 𝖴 to Lebesgue measure. These
coordinates are the complex entries in row e_a and column e_b or e*_b with b > a, or any middle
column x_i or z, together with the imaginary parts of the entries at (e_a, e*_a). 

### `instance : IsUnimodularHaar 𝔰.besselHaar`

 `New.Shape.besselHaar` is a two-sided Haar measure on 𝖴 with a cutoff for the action on G₁, in
the sense of `New.RealPlace.IsUnimodularHaar`. 


### Balls in 𝖴⁰ and tubes along 𝖴⁰

Write e, x, e* for the rows of basis vectors (e_a), (x_i), (e*_a); there are ϱ = n − 1 vectors e_a
and k = |κ| vectors x_i. An element of 𝖴⁰ acts like an Eichler map with matrix entries: it is given
by a k×ϱ matrix ω and a ϱ×ϱ matrix μ with μ + μᴴ = ωᴴ ω. The inverse of (ω, μ) is (−ω, μᴴ), so the
balls are symmetric.


### `eichlerMatrix`

 The matrix of the Eichler map of a pair (ω, μ). It sends e* to e* − x ω − e μ and x to
x + e ωᴴ, and it fixes the frame e_0, …, e_{ϱ-1}, z. 

### `eichlerMatrix_mul`

 The group law: the product of (ω, μ) and (ω', μ') is (ω + ω', μ + μ' + ωᴴ ω'). 

### `coe_unipotentOf_eq_eichlerMatrix`

 For q = (a, b), the element `New.RealPlace.unipotentOf q` is the Eichler map with ω = aᴴ and
μ = ½ a aᴴ − sk b, where sk is `New.skewOfReal`. So b gives the skew-hermitian part of μ. 

### `eichlerVectors`

 Minus the block of u in the rows x_i and the columns e*_a. For u in 𝖴⁰ this is the matrix ω in
u e* = e* − x ω − e μ; its columns are vectors of the span X₀ of the x_i. 

### `eichlerScalars`

 Minus the block of u in the rows e_a and the columns e*_b. For u in 𝖴⁰ this is the matrix μ in
u e* = e* − x ω − e μ. 

### `coe_eq_eichlerMatrix_of_mem_besselU0`

 An element of 𝖴⁰ is the Eichler map of its pair (ω, μ). 

### `coe_mul_eq_eichlerMatrix`

 The group law for two elements of 𝖴⁰, in terms of their pairs (ω, μ). 

### `homogeneousBall`

 The ball of radius ρ in 𝖴⁰, in which ω has degree one and μ degree two: ‖ω‖ ≤ ρ and ‖μ‖ ≤ ρ²,
in the operator norm. 

### `mul_mem_homogeneousBall`

 Radii add under multiplication: the product of an element of the ball of radius ρ and an element
of the ball of radius ρ' lies in the ball of radius ρ + ρ'. 

### `besselHaar₀_homogeneousBall`

 On the frame-fixing unipotent group 𝖴⁰, the measure `besselHaar₀` is the pushforward of Lebesgue
measure under `unipotentOf`. For ρ > 0 it gives `homogeneousBall ρ` (‖ω‖ ≤ ρ, ‖μ‖ ≤ ρ² in operator
norm) mass ρ ^ (2ϱ(k + ϱ)) times that of the ball of radius one, where ϱ = n − 1 is the number of
hyperbolic planes and k = |κ|. 

### `mem_homogeneousBall_of_norm_le`

 An element of 𝖴⁰ of operator norm at most t lies in the ball of radius t. 

### `norm_le_of_mem_homogeneousBall`

 On the ball of radius ρ the operator norm is at most (1 + ρ)². 

### `besselHaar₀_homogeneousBall_add_le`

 Enlarging the radius from r² t to r² t + t, where r is the number of basis indices, at most
triples the volume of a ball. 

### `mem_homogeneousBall_of_mul_mem_smul`

 If ‖y‖ ≤ T and u y lies in the product of the ball of radius ρ in 𝖴⁰ with the set of elements
of G₁ of norm at most T, then u lies in the ball of radius ρ + T². 

### `IsTube`

 `B` is a tube of size `T` along 𝖴⁰ with base `Ω`: a compact set in G₁ of norm at most `T ^ 10`
that contains the `Ω`-translates of the elements of norm at most `T` and meets every orbit of 𝖴⁰ in
measure at most three times that of `Ω`. The measure is `New.Shape.besselHaar₀`, and norms are
operator norms of matrices. 

### `IsTube.isCompact`

 The tube is compact. 

### `IsTube.measurableSet`

 The base is measurable. 

### `IsTube.measure_ne_zero`

 The base has nonzero measure. 

### `IsTube.measure_ne_top`

 The base has finite measure. 

### `IsTube.norm_le`

 The elements of the tube have norm at most `T ^ 10`. 

### `IsTube.mul_mem`

 The tube contains `u * y` for `u` in the base and `y` of norm at most `T`. 

### `IsTube.measure_slice_le`

 For each `y`, the `u` in 𝖴⁰ with `u * y` in the tube have measure at most three times that
  of the base. 

### `IsTube.lintegral_indicator_le`

 Let `B` be a tube of size `T` along 𝖴⁰ with base `Ω` (`New.RealPlace.IsTube`). For every y in
G₁, the `New.Shape.besselHaar₀`-measure of {u ∈ 𝖴⁰ : u·y ∈ B}, written as the integral of the
indicator of `B`, is at most 3 times the measure of `Ω`. 

### `exists_tube`

 Tubes exist. If `T ≥ 8 r`, where r is the number of basis indices of `𝔰.G₁`, then there are a
set `B` in the unitary group G₁ and a set `Ω` in 𝖴⁰ (the elements of the Bessel unipotent group
fixing each frame vector) with the following properties. `B` is compact, its elements have operator
norm at most `T ^ 10`, and it contains the `Ω`-translates of the elements of norm at most `T`. It
also meets every 𝖴⁰-orbit in `New.Shape.besselHaar₀`-measure at most three times that of `Ω`. 

 ## σ-finiteness of Haar measures on G₁ 

### `New.sigmaFinite_G₁`

 A Haar measure on `New.Shape.G₁` is σ-finite. 
