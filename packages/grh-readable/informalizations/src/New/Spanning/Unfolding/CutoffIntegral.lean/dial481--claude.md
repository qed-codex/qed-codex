---
{
  "module": "src/New/Spanning/Unfolding/CutoffIntegral.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/CutoffIntegral.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/CutoffIntegral.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Bessel kernel and the integral of a class cutoff over the real unipotent group

This file proves that the kernel `New.Filling.besselKernel`, the tensor
`besselFn(y) ⊗ besselFn(γ⁻¹ y)^*` of Bessel functions at the infinite places, is continuous.
It bounds the amplitude `New.Filling.amplitude` by the integral of the norms
`New.Filling.amplitudeMajorant`. It then computes the integral of a class cutoff
`S.classCutoff c` over the real unipotent group as `S.unipotentCovolume`. The group is unfolded
one coordinate at a time (`New.Filling.rowCoords`). The integral is then a product of covolumes of
explicit lattices.

## Main definitions and results

* `New.Filling.enorm_amplitude_le`: the norm of the amplitude
  `∫ β_c(y) β_c'(γ⁻¹ y) W(y) ⊗ W(γ⁻¹ y)^* dy` is at most the integral of the norm of its integrand.
* `New.Filling.lintegral_classCutoff_eq_unipotentCovolume`: let `E` contain a primitive 5040th
  root of unity and let `S` be admissible. For every class `c` and archimedean point `y`, the
  integral of the cutoff `u ↦ S.classCutoff c (u y)` over the real unipotent group 𝖴_∞, for the
  product of the Haar measures `New.Shape.besselHaar`, is the number `S.unipotentCovolume`.

Notions from other files:
* `New.Filling.besselFn`: for a tuple `i` of coordinates (`New.Filling.BesselCoord`), the product
  over the places `v` of the `i v`-th coordinate of `W side (y v)`.
* `New.Filling.M`, `New.Filling.classUnipotent`: the level M = p₀ p₁, the product of the two primes
  `S.levelPrime`; the rational points u of 𝖴 with h_c⁻¹ u h_c in the principal congruence
  subgroup K(M).
* `New.Shape.Form.besselU`, `New.Shape.Form.besselS`: the group 𝖴 of block upper unitriangular
  isometries, and the Bessel subgroup, which 𝖴 generates together with the unitary group of the
  standard form on κ.
* `New.Filling.IsAdmissible`: the standing hypotheses. The level `sourceLevel` is the preimage of
  K(M), `reduction` is onto, and size inequalities hold between b, M and ϖ, κ_v, N, the second
  moments, the number of Bessel coordinates, an index and the constant `scaledSiegelConst`.
* `New.Filling.unipotentCovolume`: an explicit positive number built from M, N, |κ|, ϱ, the
  discriminant of E and the scales of the frame at the infinite places.



## Continuity of the Bessel kernel and the bound of an amplitude

First facts on the kernel `New.Filling.besselKernel`, the tensor `besselFn(y) ⊗ besselFn(γ⁻¹ y)^*`
of Bessel functions at the infinite places. The amplitude `New.Filling.amplitude`, its integral
against the cutoffs `New.Filling.classCutoff`, is bounded by the integral of the norms
`New.Filling.amplitudeMajorant` (`New.Filling.enorm_amplitude_le`).


### `continuous_besselFn`

 Each coordinate of the product of the local Bessel functions is continuous on G_∞. 

### `continuous_besselKernel`

 The kernel `y ↦ W(y) ⊗ W(γ⁻¹ y)^*` is continuous on G_∞. 

### `enorm_besselKernel`

 The norm of `W(y) ⊗ W(γ⁻¹ y)^*` is the product of the norms of the local factors. The factor at
the infinite place `v` is the Bessel function `(S.besselSystem v).besselFn side`, full or cut
according to `side`, and `S.ratToInf γ` is the image in G_∞ of the rational element `γ`. 

### `enorm_amplitude_le`

 The norm of the amplitude `∫ β_c(y) β_c'(γ⁻¹ y) W(y) ⊗ W(γ⁻¹ y)^* dy` is at most the integral of
the norm of its integrand. 


## Integral of a class cutoff over the real unipotent group

`New.Filling.lintegral_classCutoff_eq_unipotentCovolume` computes the covolume of the arithmetic
unipotent group `S.classUnipotent c` of a class `c` in the real unipotent group (a copy of
`New.Shape.Form.besselU` at each infinite place, with the Haar measure `New.Shape.besselHaar`): the
cutoff `S.classCutoff c`, whose translates under `S.classUnipotent c` sum to `1`, has integral
`S.unipotentCovolume`.

The group is unfolded one coordinate at a time by `New.Filling.existsUnique_mul_mem_box`. The basis
is e_a, the middle block, e*_a (`New.Shape.BesselIndex`); the coordinates of a unipotent element are
the free entries of each row e_a (positions `New.RealPlace.IsFreeEntry`) and the imaginary part of
its entry at e*_a. Each coordinate is additive once the earlier ones vanish; the integral is then a
product of covolumes of explicit lattices.


### `besselU_mul_apply_eq_add`

 Additivity of an entry in the row of e_a, for x and u in the Bessel unipotent group of G₁. Let
the column j be e*_a or free for the row (`IsFreeEntry`: e_b or e*_b with b > a, or a column of the
middle block). If the free entries of u vanish in the rows e_b with b > a and in the row e_b with
j = e*_b, and the entries of u at (e_b, e*_b), b > a, are real, then the (e_a, j) entry of x·u is
the sum of those of u and x. 

### `exists_classBasis_eq_fromBlocks`

 Let `E` contain a primitive 5040th root of unity and let `S` be admissible. The basis matrix
`classBasis c` of the lattice of the class `c` differs from the identity only in its middle block
`M`, and the generalised index (`genIndex`, the inverse Haar modulus) of `det M` is `N ^ (-f)`.
Here `N = S.N` is the prime `π π̄` of `S` and `f` is the number of infinite places of `E`. 

### `classUnipotent_sub_one_div_M_row_integral`

 Let `E` contain a primitive 5040th root of unity and let `S` be admissible. Let `γ` lie in
`S.classUnipotent c`, the rational unipotent elements that the representative of the class `c`
conjugates into the principal congruence subgroup of level `S.M`. Then the row of γ − 1 at e_a,
divided by `S.M`, has integral coordinates in the basis `classBasis c` of the lattice of `c`. 

### `det_toSquareBlockProp_isFreeEntry`

 If `b` differs from the identity only in its middle block, then its square block on the free
columns (`IsFreeEntry`) of the row e_a has the determinant of `b`. 

### `transpose_toSquareBlockProp_mulVec`

 If `b` differs from the identity only in its middle block, then the entries of `l ᵥ* b` in the
free columns (`IsFreeEntry`) of the row e_a depend only on the entries of `l` in these columns. 

### `classUnipotentToInf`

 The embedding of `S.classUnipotent c` into the real unipotent group 𝖴_∞, the product over the
infinite places of the Bessel unipotent group of G₁. 

### `freeRowCoords`

 The free entries (`IsFreeEntry`) of the row e_a of a point `u` of the real unipotent group
𝖴_∞, at all infinite places. 

### `imRowCoords`

 The imaginary parts of the entry at (e_a, e*_a) of a point `u` of the real unipotent group
𝖴_∞, at all infinite places. 

### `rowCoords`

 The coordinates of a point `u` of the real unipotent group 𝖴_∞, grouped by rows: for each row
e_a, its free entries (`freeRowCoords`) and the imaginary parts of its entry at e*_a
(`imRowCoords`), at all infinite places. 

### `measurePreserving_rowCoords`

 The map `rowCoords` sends a point of the real unipotent group 𝖴_∞ to the free entries of its
rows e_a and the imaginary parts (real numbers) of its entries at (e_a, e*_a), at all infinite
places of `E`. It carries the product over the infinite places of the Haar measure `besselHaar` to
Lebesgue measure on these coordinates. 

### `lintegral_classCutoff_eq_measure`

 Unfolding. Let `E` contain a primitive 5040th root of unity and let `S` be admissible. The
cutoff `S.classCutoff c` is a measurable function G_∞ → [0, ∞], on tuples `y` of points of `G₁` at
the infinite places, whose left translates under the congruence group `S.classUnipotent c` of
rational unipotent elements add up to `1`. Let `B` be a measurable subset of the real unipotent
group 𝖴_∞ that meets each coset `u Γ` of the image `Γ` of `S.classUnipotent c` under
`classUnipotentToInf c` in exactly one point. Then the integral over 𝖴_∞ of
`u ↦ S.classCutoff c (u y)` is the measure of `B`, both for the product of the Haar measures
`𝔰.besselHaar`. 

### `star_inv_mul_apply_eStar_eq_neg`

 Let `γ ∈ S.classUnipotent c`. If, at an infinite place `v`, right multiplication by `γ` adds the
(e_a, e*_a) entry of `γ` to that of every unipotent `x`, then the (e_a, e*_a) entry of `γ` divided
by the level `S.M` is skew: the complex conjugation `star` of the CM field `E` changes its sign. 

### `isIntegral_inv_mul_apply_eStar`

 For admissible `S` and `γ ∈ S.classUnipotent c`, the (e_a, e*_a) entry of `γ` is the level
`S.M` times an algebraic integer. 

### `prod_norm_basisScale_sq_div_eq`

 The volume of the fundamental domain for the free entries (`IsFreeEntry`) of the row e_a, of
which there are 2(ϱ − 1 − a) + k + 1, is `(∏ v, S.M ^ 2 / S.frameScaleSq v a) / volÔ E` to that
power. Here `S.basisScale v j` is the scale of the basis vector `j` at the place `v`,
`S.frameScaleSq v a` is the square of the scale of e_a, `S.M` is the level, and `volÔ E` is
2^r₂/√|disc E|, with r₂ the number of complex places. 

### `unipotentCovolume_eq_prod`

 The number `S.unipotentCovolume` is the product, over the rows e_a, of the covolumes of the
lattice of free entries and of the lattice of imaginary parts at e*_a. 

### `rowCoords_mul_fst`

 If the free entries (`freeRowCoords`) and the imaginary parts of the (e_d, e*_d) entry
(`imRowCoords`) of `u` vanish in every row e_d with d > a, then the free entries of `x * u` in the
row e_a are the sum of those of `u` and of `x`. 

### `mul_apply_eStar_of_rowCoords`

 If the free entries of `u` vanish in the rows e_d with d ≥ a and the imaginary parts at
(e_d, e*_d) vanish for d > a, then at each place right multiplication by `u` adds the (e_a, e*_a)
entry of `u` to that of `x`. 

 In this section `c` is a class and e_a is a row; `S` is admissible unless this is omitted. 

### `freeBlock`

 The transpose of the square block of the lattice basis `classBasis c` on the free columns
(`IsFreeEntry`) of the row e_a, as an invertible matrix. 

### `isUnit_basisScale_ratio`

 For each `a`, the scales `S.M / S.basisScale v (inl a) * S.basisScale v j` are nonzero for all
infinite places `v` and all `j` with `IsFreeEntry (a, j)`. Here `inl a` indexes the basis vector
e_a. So this family of scales is a unit. 

### `freeLattice`

 The lattice of free entries of the row e_a for the class `c`: the vectors with entries
`S.M / S.basisScale v e_a * S.basisScale v j * Φ v (x j)`, for the rational vectors `x` on the free
columns `j` such that `freeBlock c a *ᵥ x` is integral. Here `S.basisScale v j` is the scale of the
basis vector `j` at the infinite place `v`, and `Φ v` is the chosen complex embedding at `v`. 

### `exists_fundamental_domain_freeLattice`

 Let `S` be a filling of shape `𝔰` over the CM field `E` containing a primitive 5040th root of
unity, with `S` admissible. For `c` in `S.Classes`, the lattice `freeLattice c a` of free entries of
the row e_a has a measurable strict fundamental domain. Its volume is `((∏ v, S.M ^
2 / S.frameScaleSq v a) / volÔ E) ^ (a.rev + (𝔰.k + 1) + a.rev)`, the exponent being the number of
free columns. 

### `rowCoords_fst_mem_freeLattice`

 Let `E` contain a primitive 5040th root of unity and let `S` be admissible. The free entries
(`IsFreeEntry`) of the row e_a of the real image of any `γ ∈ S.classUnipotent c` lie in
`freeLattice c a`, the lattice of rescaled rational vectors `x` on the free columns with
`freeBlock c a *ᵥ x` integral. 

### `exists_rowCoords_fst_eq`

 Let `E` contain a primitive 5040th root of unity and let `S` be admissible. Fix a class `c` and
a row e_a; its free columns (`IsFreeEntry`) are e_b and e*_b with b > a and the middle block. Let
`l` lie in `freeLattice c a`: its entries are the rescaled complex embeddings of a rational vector
`x` on the free columns with `freeBlock c a *ᵥ x` integral, `freeBlock c a` being the transposed
block of the lattice basis of `c` on these columns. Then `l` is the vector of free entries in the
row e_a of the real image of some `γ ∈ S.classUnipotent c`, for which all coordinates `rowCoords`
vanish in the rows e_d with d > a. 

### `rowCoords_snd_mem_imSkewLattice`

 Let `E` contain a primitive 5040th root of unity and let `S` be admissible. Suppose that at the
place `v`, right multiplication by the image `classUnipotentToInf c γ v` of `γ ∈ S.classUnipotent c`
adds its (e_a, e*_a) entry to that of every `x` in `besselU`. Then the imaginary parts of this entry
of `classUnipotentToInf c γ` at all places form a vector `(S.M / S.frameScaleSq w a * Im Φ_w(s))_w`
for an integer `s` of `E` with `star s = -s` (`imSkewLattice`). 

### `exists_rowCoords_snd_eq`

 Let `E` contain a primitive 5040th root of unity. Fix a class `c` and a row e_a. Let `l` be a
vector `(S.M / S.frameScaleSq v a * Im Φ_v(s))_v` for an integer `s` of `E` with `star s = -s`
(`imSkewLattice`). Then `l` is the vector of imaginary parts at (e_a, e*_a) of the real image of
some `γ ∈ S.classUnipotent c` whose other coordinates `rowCoords` vanish. 

### `exists_box_existsUnique_rowCoords_mem`

 Let `S` be admissible and `c` a class, with finite adelic representative h_c. The group
`S.classUnipotent c` consists of the rational unipotent `γ` with h_c⁻¹ γ h_c in the principal
congruence subgroup of level `S.M`; let `Γ` be its image in the real unipotent group 𝖴_∞. In the
basis e₁, …, e_ϱ, middle block, e*₁, …, e*_ϱ, the map `rowCoords` sends a point of 𝖴_∞ to the free
entries of each row e_a and the imaginary parts of the entries at (e_a, e*_a), at all infinite
places. There are measurable sets `F a` and `F' a` such that each coset `u Γ` has exactly one point
with coordinates in the box over them. The product of the volumes of all `F a` and `F' a` is the
explicit number `S.unipotentCovolume`, which does not depend on `c`. 

### `lintegral_classCutoff_eq_unipotentCovolume`

 Let `E` contain a primitive 5040th root of unity and let `S` be admissible. For every class `c`
and archimedean point `y`, the integral of the cutoff `u ↦ S.classCutoff c (u y)` over the real
unipotent group 𝖴_∞, for the product of the Haar measures `New.Shape.besselHaar`, is the number
`S.unipotentCovolume`, which depends neither on `c` nor on `y`.

A case of the covolume computation for Heisenberg radicals, with a fixed product Haar measure in
place of Tate's self-dual measures. 
