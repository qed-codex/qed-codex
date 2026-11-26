---
{
  "module": "src/Lib/Adelic/Reduction/FiniteVolume.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Reduction/FiniteVolume.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Reduction/FiniteVolume.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Adelic reduction theory, Mahler's criterion and finite volume of the arithmetic quotient

This file develops reduction theory for `GL_n` over the adeles: every adelic frame `y` has a
rational basis `Y` such that `y⁻¹ Y` lies in one fixed compact set after its columns are scaled by
powers of `2` at the infinite places. For a hermitian space `V` (`New.Space`), a weighted Haar
measure on the adelic unitary group `G` computes integrals over `[G] = V.Γ \ G`.

## Main definitions and results

* `New.Core.exists_isCompact_profileBases`: one compact set `M` bounds a reduced basis at every `y`.
* `New.exists_isBoundedDualBasis`: Mahler's criterion for frames of forms that may vary. The
  criterion for the unitary group of one space is `New.Space.mahler_criterion` in
  `Lib.Adelic.Reduction.DefiniteClassSums`.
* `New.Space.quotMeasure`: for a space `V` with rational points `New.Space.Γ`, the measure
  `Subgroup.quotMeasure` on `G` for counting measure on `Γ`. It integrates `Γ`-invariant functions
  over `[G] = Γ \ G`.
* `New.Space.lintegral_encard_ne_top`: the count of rational `n × t` matrices is integrable over
  `V.Γ \ G` if `2 t < n`.
* `New.Space.isFiniteMeasure_quotMeasure`: finite volume, the case `t = 0`.

Notions from other files:
* `New.𝔸`: the ring `ℂ ^ f × 𝔸_f`, one copy of `ℂ` for each infinite place of `E` times the finite
  adeles. It is the adele ring of `E` when `E` is totally complex; `New.toAdele` embeds `E` in it.
* `New.ideleAbs`: the module (adelic absolute value) of an idele.
* `New.Core.twoAtInfinity`: the idele of `E` that is `2` at all infinite places and `1` at the
  finite places.
* `New.Core.profileBases M x y`: the `Y` in `GL_n(E)` with `y⁻¹ Y (D x)⁻¹ ∈ M`, where
  `D x = New.Core.dyadicDiag x` is diagonal with entries `twoAtInfinity E ^ x i`. The integer vector
  `x` is called the profile of such a basis.
* `New.Space`: a matrix `J` over `E` and a point `x` in `GL_n(𝔸)` with `xᴴ J x` equal to `diag s` at
  the infinite places, for signs `s`, and `1` at the finite places.

## Relation to the literature

Known results: reduction theory for adele groups (the compactness criterion of Mahler and Godement,
finite covolume) and Weil's convergence criterion. Finite volume is proved here only for unitary
groups over CM fields, by counting reduced bases, and Weil's criterion only when twice the number of
vectors is below the rank. The adelic Minkowski theorems come from
`Lib.Adelic.Reduction.MinkowskiTheorems`, with crude explicit constants. Source: A. Borel, Some
finiteness properties of adele groups over number fields, Publ. IHES 16 (1963), 4.5-5.8; A. Weil,
Sur la formule de Siegel dans la théorie des groupes classiques, Acta Math. 113 (1965), Prop. 8;
Bombieri-Vaaler, On Siegel's lemma, Invent. Math. 73 (1983).

For the adelic points of unitary groups and their Haar measures, see
`Lib.Adelic.Unitary.WeakApproximation`.


 ## Reduced rational bases in a compact set of adelic matrices 

### `exists_mul_twoAtInfinity_pow_mul_eq_toAdele`

 Minkowski's first theorem in rank one. Let `a` be an idele such that `a` times `2 ^ N` at the
infinite places has adelic absolute value greater than `(2 * rootDiscr E) ^ f`, with `rootDiscr E`
the root discriminant of `E`, where `f = numInfPlaces E` is the number of infinite places. Then this
product times some `b` in the closed unit box (absolute value at most `1` at the infinite places, in
the ring `Ô E` of integral finite adeles at the finite places) is a non-zero element `ξ` of `E`. 

### `isCompact_setOf_le_ideleAbs_det`

 For a compact set `M` of adelic `n × n` matrices and `c > 0`, the invertible matrices `A` that
lie in `M` and whose determinant has adelic absolute value `ideleAbs A.det` at least `c` form a
compact subset of `GL n (𝔸 E)`, where `𝔸 E` is the ring of adeles of `E`. 

### `exists_compact_gram_entry`

 Let `M` and `K` be compact. There is a compact set `B` of adeles such that, whenever the Gram
matrix `yᴴ J y` lies in `K` and `Y` is a rational basis with `y⁻¹ Y (dyadicDiag x)⁻¹ ∈ M` (that is,
`Y ∈ profileBases M x y`), every entry `(Yᴴ J Y) i j`, divided by `2 ^ (x i + x j)` at the infinite
places, lies in `B`. Here `dyadicDiag x` is diagonal with entries `2 ^ x i` at the infinite places
and `1` at the finite places, and `toAdele` embeds `E` in its adeles. 

### `exists_isCompact_profileBases`

 For a CM field `E`, there are a compact set `M` of invertible adelic matrices and an integer `c`
such that every `y` in `GL n (𝔸 E)` has a profile `x : n → ℤ` and a rational basis `Y` with
`y⁻¹ Y (dyadicDiag x)⁻¹ ∈ M` (that is, `Y ∈ profileBases M x y`), where `dyadicDiag x` is diagonal
with entries `2 ^ x i` at the infinite places and `1` at the finite places. Moreover `∑ i, x i ≤ c`
whenever `ideleAbs y.det ≥ 1`. 


## Mahler's criterion for frames of varying forms

Let an adelic frame `y` of a rational form `J` have its Gram matrix in a compact set. Take the
basis dual to a reduced basis at `y` (`New.Core.exists_isCompact_profileBases`), with some of its
columns set to zero. This matrix is bounded at `y` and has one of finitely many Gram matrices
(`New.exists_isBoundedDualBasis`).


### `finitePartGL`

 The finite part of an invertible adelic matrix. 

### `formDual`

 The basis `W` dual to `Y` for the form `J`, so that `Yᴴ J W = 1`. 

### `projectionOff`

 The diagonal matrix with entry `0` at the indices in `s` and `1` at the others. 

### `formDualOff`

 The basis dual to `Y` for the form `J`, with the columns indexed by `s` set to zero. 

### `IsBoundedDualBasis`

 The columns of `Y` indexed by `s` span an isotropic subspace for `J`, and the basis `W` dual to
`Y` is bounded at the frame `y`: the finite part of `W⁻¹ y` lies in `Cf`, and the matrix `Z` made
from `W` by setting the columns indexed by `s` to zero has `y⁻¹ Z ∈ C` and `Zᴴ J Z ∈ F`. 

### `IsBoundedDualBasis.isotropic`

 The columns of `Y` indexed by `s` span an isotropic subspace. 

### `IsBoundedDualBasis.gram_mem`

 The Gram matrix of the remaining dual columns lies in `F`. 

### `IsBoundedDualBasis.frame_mem`

 The remaining dual columns, in the coordinates of `y`, form a matrix in `C`. 

### `IsBoundedDualBasis.finitePart_mem`

 The finite part of `W⁻¹ y`, for the whole dual basis `W`, lies in `Cf`. 

### `star_frame_mul_gram_eq_star_dyadicDiag_inv_mul`

 For `m = y⁻¹ Y (dyadicDiag x)⁻¹`, the product of `mᴴ` with the Gram matrix `yᴴ J y` is
`(dyadicDiag x)⁻¹ᴴ W⁻¹ y`, where `W = formDual J Y` is the basis dual to `Y` for the form `J`.
Here `dyadicDiag x` is diagonal with entries `2 ^ x i` at the infinite places and `1` at the
others. 

### `star_dyadicDiag_inv_mul_projectionOff`

 The conjugate transpose of `(dyadicDiag x)⁻¹` times the projection off `s` is diagonal, with
entry `0` at the indices in `s` and, at the other indices `j`, the idele that is `2 ^ (-x j)` at
the infinite places and `1` at the finite ones. 

### `exists_isBoundedDualBasis`

 Mahler's criterion for frames of forms that may vary, by the dual of a reduced basis. Given a
compact `K`, there are a finite `F` and compact `C`, `Cf` such that, for each invertible `J` over
`E` and adelic frame `y` with `yᴴ J y ∈ K`, some rational basis `Y` and set `s` of its columns
satisfy `New.IsBoundedDualBasis`. That is, the columns in `s` span an isotropic subspace; the
basis dual to `Y`, with its columns in `s` set to zero, has its Gram matrix in `F` and lies in `C`
in the coordinates of `y`; and the whole dual basis is bounded at the finite places by `Cf`. 


## Haar measure on the adelic unitary group and integration over [G]

The `volume` on the adelic unitary group `New.G` is a Haar measure: `G` is a product whose first
factor `GInf` carries a product (pi) Haar measure, and `volume` on `G` is the product measure.


### `Space.quotMeasure`

 The measure on `G E s` that computes integrals over the quotient `V.Γ \ G E s` by the rational
points of the space `V`: Haar measure weighted by a cutoff for counting measure on `V.Γ`, chosen so
that integrating `∑ γ : V.Γ, F (γ • g)` against it gives `∫⁻ F` for `volume`. 

 ## Finite volume of [G] and integrability of counts of rational matrices 

### `Core.eq_of_add_smul_eq_of_hermitian`

 If `θ - star θ` is invertible, then `S + θ • T` determines the hermitian matrices `S`, `T`. 

### `Core.encard_hermitian_le`

 For a compact set `B` of adelic matrices there is a finite constant `C` such that, for all
`x : n → ℤ`, at most `C * (2 ^ numInfPlaces E) ^ ∑ i, ∑ j, (x i + x j)₊` hermitian matrices `T`
over `E` land in `B` when `T i j` is scaled by `2 ^ (-(x i + x j))` at the infinite places. Here
`numInfPlaces E` is the number of infinite places, and `twoAtInfinity E` is the idele that is `2`
at these places and `1` at the finite ones. 

### `Space.ideleAbs_det_x`

 The module (adelic absolute value) of the determinant of the point `V.x` of a space is `1`. 

### `Core.unitBoxGL`

 The invertible adelic matrices with entries in the closed unit box (absolute value at most `1`
at the infinite places, integral at the finite places) and determinant of module at least `1`. 

### `Core.two_pow_sq_le_encard_profileBases`

 From one basis `Y` of profile `x` one gets many: with `T = ∑ (x i - x j)₊`, the number
`2 ^ (2 * numInfPlaces E * T)` is at most `((2 * rootDiscr E) ^ numInfPlaces E) ^ card (n × n)`
times the number of bases of profile `x` for `M * unitBoxGL E n`. These come from adding to column
`j` of `Y` the columns `i` times integers of `E` of size less than `2 ^ (x j - x i)`. Here
`profileBases M x y` is the set of rational `Y` with `y⁻¹ Y (dyadicDiag x)⁻¹ ∈ M`, where
`dyadicDiag x` is diagonal with entries `2 ^ x i` at infinity and `1` at the finite places.
`numInfPlaces E` is the number of infinite places and `rootDiscr E` the root discriminant.
`unitBoxGL E n` is the set of invertible adelic matrices with entries of absolute value at most `1`
at infinity and integral at the finite places, and determinant of module at least `1`. 

### `Space.exists_isCompact_gram_entry_mem`

 For a compact `M` there is a compact set `S` of adeles that holds the Gram entries
`(Yᴴ V.J Y) i j`, divided by `2 ^ (x i + x j)` at the infinite places, for every space `V` with
signs `s` and every rational basis `Y` with `V.x⁻¹ Y (dyadicDiag x)⁻¹ ∈ M`. 

### `Space.exists_perm_natAbs_add_le`

 If `Y` is a basis of profile `x` at the point of `V` (that is,
`V.x⁻¹ Y (dyadicDiag x)⁻¹ ∈ M`) and `∑ i, x i ≤ c`, then `x` is nearly symmetric about `0`: for
some permutation `σ` all `|x (σ i) + x i|` are at most a constant `B`, which depends only on the
compact set `M`, on `c` and on the signs `s`. 

### `Core.sum_toNat_neg_add_le`

 The inequality of exponents behind `Space.lintegral_encard_ne_top`. Write `ν = ∑ (-x i)₊`,
`P = ∑ (x i + x j)₊` and `T = ∑ (x i - x j)₊`. Suppose `|x (σ i) + x i| ≤ B` for a permutation `σ`,
and that `2 m` is less than the number `N` of indices whenever there is at least one index. Then
`4 m ν + 2 P + ∑ |x i| ≤ 4 T + 6 (N + 1) ^ 2 B`. 

### `Space.encard_profileBases_mul_le_lintegral`

 For `g` in the adelic unitary group `G E s`, a basis at `g` is a rational `Z` in
`profileBases N x (V.move g).x`, that is, one with `(V.x * g)⁻¹ Z (dyadicDiag x)⁻¹ ∈ N`; its Gram
matrix is `Zᴴ V.J Z`. Let `𝒯` hold the Gram matrices of all bases, and for each such matrix `T`
let `r T` be a basis at `A T` with Gram matrix `T`. If `B` contains every group element whose
adelic matrix `G.adeleMatrix` lies in `N * N⁻¹`, then the number of bases at `g`, times a weight
`w`, is at most the sum over `γ ∈ V.Γ` and `T ∈ 𝒯` of `w` times the indicator of `γ g ∈ A T * B`. 

### `Space.lintegral_ne_top_of_le_encard_profileBases`

 Unfolding over the rational points `V.Γ` of the adelic unitary group `G E s`, for a hermitian
space `V` over a CM field `E` with its point `V.x`. Suppose that for each `g`, `f g` is at most
`ω x` times the number of rational bases of some profile `x` at the moved point
`(V.move g).x = V.x * g`, that is, of `Y` with `(V.x * g)⁻¹ Y (dyadicDiag x)⁻¹` in the compact set
`N`, where `dyadicDiag x` is diagonal with entries `2 ^ x i` at the infinite places and `1` at the
finite places. Bases with the same Gram matrix differ by `V.Γ`, and there are
`O(2 ^ (numInfPlaces E * ∑ i, ∑ j, (x i + x j)₊))` Gram matrices of profile `x`, so `f` has finite
integral against `V.quotMeasure` (the measure on `G E s` that integrates invariant functions over
`V.Γ \ G`) if `ω x` times this power of `2` is summable over `x`. 

### `Space.exists_encard_le_of_mem_profileBases`

 Let `M` and `Ω` be compact. There is a finite `C` such that, if `g` lies in the adelic unitary
group `G E s` and `Y` is a rational basis of profile `x` at the moved point `V.x * g`, then at most
`C * 4 ^ (numInfPlaces E * #t * ∑ (-x i)₊)` rational `n × t` matrices `ξ` satisfy
`(V.toRatCoords g)⁻¹ ξ ∈ Ω`, where `V.toRatCoords g = V.x * g * V.x⁻¹` and `numInfPlaces E` is the
number of infinite places. The hypothesis on `Y` means `(V.x * g)⁻¹ Y (dyadicDiag x)⁻¹ ∈ M`, for
the diagonal matrix `dyadicDiag x` with entries `2 ^ x i` at the infinite places and `1` at the
finite ones. 

### `Space.lintegral_encard_ne_top`

 Let `Ω` be a compact set of adelic `n × t` matrices, and suppose `2 * card t < card n` unless
`n` is empty. For `g` in the adelic unitary group `G E s`, count the rational `n × t` matrices `ξ`
with `(V.toRatCoords g)⁻¹ ξ ∈ Ω`, where `V.toRatCoords g = V.x * g * V.x⁻¹`. This count has a finite
integral over the quotient `V.Γ \ G` by the rational points, that is, against `V.quotMeasure`. 

### `Space.isFiniteMeasure_quotMeasure`

 The quotient `V.Γ \ G` of the adelic unitary group by its rational points has finite volume.

This is the finite volume theorem for adelic quotients in the case of unitary groups over CM
fields of hermitian forms with an adelic orthonormal frame, of any rank and signs. 
