---
{
  "module": "src/New/Spanning/RemainingTerms/SiegelLemma.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/SiegelLemma.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/SiegelLemma.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Discriminants of sublattices, Siegel's lemma and a height zeta function of subspaces

Let `E` be a CM field containing a primitive 5040th root of unity, `𝔸f E` its finite adeles and
`Ô E` their integers. A lattice is given by an adelic basis: a matrix over `E`, embedded by
`New.Filling.finAdeleMatrix`, times a matrix over the finite adeles. Subspaces `T` of `E^κ` have
heights relative to the lattice `E^κ ∩ u Ô^κ` of a finite adelic unitary matrix `u : New.Gf E κ`.
Here `d T = New.Filling.sublatticeDiscriminant u.val.val_inv T` is the discriminant of `T ∩ u Ô^κ`;
the first argument proves `u u⁻¹ = 1`.

## Main definitions and results

* `New.Filling.sublatticeBasis`, `New.Filling.sublatticeDiscriminant`: a basis and the discriminant
  of the points of a subspace `V` that `H` makes integral.
* `New.Filling.siegel_lemma`: a subspace of codimension `s` is cut out by `s` short vectors.
* `New.Filling.tsum_sublatticeDiscriminant_inv_le`: an explicit bound for `∑ (d T)⁻¹ ^ (#κ + 1)`
  over the subspaces `T` of `E^κ` of codimension `s`. It follows from `New.Filling.siegel_lemma`:
  each `T` is charged to its tuple of vectors, and a packing bound sums over the lattice.

Notions from other files:
* `New.CMType E`: `E` is a CM number field (it extends `NumberField E` and `IsCMField E`) with a
  chosen complex embedding `Φ v` inducing each infinite place `v`.
* `New.IsPrimitiveMatrix O X`: `X` has entries in `O` and a left inverse with entries in `O`.
* `New.genIndex a`: the inverse of the factor by which a unit `a` scales Haar measure, `0` for a
  non-unit.

## Relation to the literature

Known result: Siegel's lemma over number fields (Bombieri–Vaaler). It is stated for lattices in the
genus of the standard hermitian lattice over a stably unramified CM field
(`New.HasPrimitiveRoot5040`: `E` contains a primitive `5040`-th root of unity). A subspace is cut
out by lattice vectors; a power of the product of their norms is bounded by an explicit constant,
depending on the degree, the codimension and the root discriminant, times its discriminant. Source:
E. Bombieri, J. Vaaler, On Siegel's lemma, Invent. Math. 73 (1983).


 ## Adelic matrices, bases along a kernel, and discriminants of subspaces 

### `finAdeleMatrix`

 For a matrix over `E`, the matrix over the finite adeles of `E` obtained by embedding each
entry. 

### `map_conjTranspose`

 A complex embedding of a CM field commutes with conjugation, hence with the conjugate
transpose of matrices. 

 ### Splitting along a kernel 

### `mul_eq_zero_of_colSpan_le_ker`

 If the column span of `y` lies in the kernel of `A`, then `A * y = 0`. 

### `IsKernelExtension`

 The columns of `y` lie in `L` and in the kernel of `A`, and together with the columns of `x`
they form a basis of `L`. `colSpan` is the span of the columns, and `HasLeftInv` says that there is
a left inverse. 

### `IsKernelExtension.finrank_eq`

 The number of columns of `y` is the dimension of `L ⊓ ker A`. 

### `IsKernelExtension.hasLeftInv`

 The columns of `x` and `y` together are independent. 

### `IsKernelExtension.colSpan_fromCols`

 The columns of `x` and `y` together span `L`. 

### `IsKernelExtension.colSpan_le`

 The columns of `y` lie in `L`. 

### `IsKernelExtension.mul_eq_zero`

 The columns of `y` lie in the kernel of `A`. 

### `IsKernelExtension.eq_zero_of_mulVec_mem`

 Only the trivial combination of the columns of `y` lies in the span of those of `x`. 

### `exists_isKernelExtension`

 If `A * x` is invertible and a subspace `L` contains the columns of `x`, then these columns
extend to a basis of `L` by the columns of a matrix `y`, a basis of `L ⊓ ker A`. 

 ### The discriminant of the integral points of a subspace 

### `exists_isPrimitiveMatrix_mul_finAdeleMatrix`

 Let `E` be a CM field containing a primitive `5040`-th root of unity, and let the finite adelic
matrix `H` have a left inverse `L`. A subspace `V` of `E^σ` of dimension `s` has a basis `y` (the
columns of a left invertible matrix over `E`) and an `a ∈ GL_s(𝔸_f)` such that `H y a` is
primitive: it has entries in `Ô` and a left inverse with entries in `Ô`. 

### `sublatticeBasis`

 Let `H` have a left inverse `L`. This is a chosen matrix `m = y a`, with the columns of `y` a
basis of `V` over `E`, `a` invertible over `𝔸_f` and `H m` primitive over `Ô` (integral, with an
integral left inverse); it exists by `exists_isPrimitiveMatrix_mul_finAdeleMatrix`. 

### `exists_sublatticeBasis_eq_finAdeleMatrix_mul`

 The chosen basis is `y a`, with the columns of `y` a basis of `V` over `E` and `a` invertible
over `𝔸_f`. 

### `sublatticeDiscriminant`

 The discriminant `√[det mᴴ m]` of the lattice of adelic points of `V` that `H` makes integral,
for its basis `m = New.Filling.sublatticeBasis hLH V`. Here `[·]` is the generalised index
`New.genIndex`, which is `|N(z)|` at a nonzero `z ∈ E` for the norm `N` from `E` to `ℚ`. So for a
lattice with a basis `x` over `E` the discriminant is `√|N(det xᴴ x)|`. 

### `sublatticeIndex`

 The index of `K ∩ M` in `M` (`0` if infinite), where `M` is the `Ô`-span of the columns of
`Y H m` and `m = New.Filling.sublatticeBasis hLH V` is the basis of the points of `V` that `H`
makes integral. 

### `exists_finAdeleMatrix_mul_eq_sublatticeBasis_mul`

 Let `E` be a CM field containing a primitive `5040`-th root of unity, and let the finite adelic
matrix `H` have a left inverse `L`. The columns of `m = sublatticeBasis hLH V` are an `Ô`-basis of
the adelic points of the subspace `V` that `H` makes integral. Let the matrix `x` over `E` have
`dim V` columns, all in `V`, with `det xᴴ x ≠ 0`. Then for every invertible finite adelic `w` there
is an invertible finite adelic `A` with `x w = m A`. 

### `sublatticeDiscriminant_sq_mul_genIndex_sq`

 Let `E` be a CM field containing a primitive `5040`-th root of unity, and let the finite adelic
matrix `H` have a left inverse `L`. Let `m = sublatticeBasis hLH V` be the chosen `Ô`-basis of the
adelic points of the subspace `V` that `H` makes integral. Let `δ = √[det mᴴ m]` be its discriminant
`sublatticeDiscriminant`. Here `[a]` is the generalised index `genIndex a`: for a unit `a`, the
inverse of the factor by which multiplication by `a` scales Haar measure, and `0` otherwise. If
`x w = m A` for a matrix `x` over `E` and square finite adelic matrices `w` and `A`, then
`δ² [det A]² = [det xᴴ x] [det w]²`. 

### `sublatticeDiscriminant_pos`

 Let `E` be a CM field containing a primitive `5040`-th root of unity, and let the finite adelic
matrix `H` have a left inverse `L`. Suppose the subspace `V` contains the columns of a matrix `x`
over `E` with `dim V` columns and `det xᴴ x ≠ 0`. Then `sublatticeDiscriminant hLH V`, the
discriminant of the lattice of adelic points of `V` that `H` makes integral, is positive. 

### `sublatticeDiscriminant_mul_index_sq_le`

 Let `E` be a CM field containing a primitive `5040`-th root of unity, and let the finite adelic
matrix `H` have a left inverse `L`. Let `δ` be the discriminant `sublatticeDiscriminant` of the
lattice `Λ` of adelic points of `V` that `H` makes integral. Let `Y` be a finite adelic matrix and
`K` an `Ô`-module in the target of `Y`. The index `i = sublatticeIndex hLH V Y K` is that of
`K ∩ Y H Λ` in `Y H Λ`, the image of `Λ` under `Y H`. Let `x` have `s = dim V` columns, all in `V`,
with `det xᴴ x ≠ 0`, and let `w ∈ GL_s(𝔸_f)`. Suppose `H x w` is integral and the columns of
`Y H x w` lie in `K`. Then `(δ i)² ≤ [det xᴴ x] [det w]²`, with `[·]` the generalised index
`genIndex`; also `δ > 0`, and the index is finite. 


## Siegel's lemma and convergence of the height zeta function

`(stdSpace E κ).move (1, u)` is `E^κ` with the form `∑ x_i x̄_i` and the point `u`.
`.baseLattice` is its lattice `E^κ ∩ u Ô^κ`, `.archCoords` the vector of complex coordinates at all
infinite places, and `numInfPlaces E` the number of infinite places.


### `finrank_ker_conjTranspose`

 Let `E` be a CM field with a chosen CM type (`CMType E`), and let `ᴴ` be the conjugate
transpose for its complex conjugation. If `x` is a left invertible `κ × t` matrix over `E` and
`t + s = #κ`, the hermitian orthogonal `ker xᴴ` of its columns has dimension `s`. 

### `ker_conjTranspose_mul_transpose`

 Let `E` be a CM field with a chosen CM type (`CMType E`), and let `x`, `y`, `B` be matrices over
`E`. If the columns of `y` span the hermitian orthogonal `ker xᴴ` of the columns of `x` and `B` is
invertible, then the hermitian orthogonal of the columns of `y Bᵀ` is the column span of `x`. 

### `genIndex_sq_mul_abs_norm_eq`

 Orthogonal lattices have the same discriminant. Let `E` be a CM field with a chosen CM type
(`CMType E`), containing a primitive `5040`-th root of unity, and let `u` be a finite adelic unitary
matrix. Let `x` and `y` be matrices over `E` with `#κ` columns in all and `xᴴ y = 0`. Let `b` and
`a` be invertible over `𝔸_f`, with `u⁻¹ x b` and `u⁻¹ y a` primitive. Then
`[det a]² |N(det yᴴ y)| = [det (x b)ᴴ (x b)]`. Here `[·]` is the generalised index `genIndex`: at a
unit the inverse of the factor by which it scales Haar measure on the finite adeles, so `|N(z)|` at
a nonzero `z ∈ E`, and `0` at a non-unit. `N` is the norm from `E` to `ℚ`. 

### `one_le_ideleAbs_det_mul_sqrt`

 Let `r v` make the columns of `y` orthonormal at each infinite place `v`, with embedding `Φ v`,
and let `a` be invertible over `𝔸_f`. Then `ideleAbs` of the determinant of `mkAdelicGL (r, a)`,
times `√([det a]² |N(det yᴴ y)|)`, is at least `1`. Here `[·]` is the generalised index `genIndex`:
at a unit it is the inverse of the factor by which the unit scales Haar measure on the finite
adeles, and at a non-unit it is `0`. `N` is the norm from `E` to `ℚ`. 

### `norm_archCoords_mulVec`

 Let `r v` make the columns of `y` orthonormal at each infinite place `v`, with embedding `Φ v`.
Then the Euclidean length of `y c` over all infinite places is that of the vectors `(r v)⁻¹ (Φ v c)`
taken together. 

### `frameLength_mkAdelicGL`

 The length `frameLength` of a rational vector `c` at the adelic matrix `mkAdelicGL (r, a)`, with
infinite part `r` and finite part `a`, is the Euclidean length of the vectors `(r v)⁻¹ (Φ v c)` over
all infinite places `v`, with embedding `Φ v`. 

### `mulVec_mem_baseLattice`

 Let `u` be a finite adelic unitary matrix. If `u⁻¹ y Bᵀ` is integral, its `i`-th column shows
that the rational vector `y (B i)` lies in the lattice `((stdSpace E κ).move (1, u)).baseLattice`,
which is `E^κ ∩ u Ô^κ`. 

### `one_le_norm_archCoords`

 Let `u` be a finite adelic unitary matrix. A nonzero vector of the lattice
`((stdSpace E κ).move (1, u)).baseLattice`, which is `E^κ ∩ u Ô^κ`, has Euclidean length at least
`1` over all infinite places. 

### `exists_det_ne_zero_prod_frameLength_le`

 Minkowski's second theorem for the adelic matrix `(r, a)`, with infinite part `r` and finite
part `a`: there is an invertible `B` over `E` such that `a⁻¹ Bᵀ` is integral and the rows `B i`
satisfy `|det (r, a)| * ∏ (len (B i)) ^ (2 f) ≤ (2 f s rd) ^ (f s)`. Here `len c` is the length
`frameLength (mkAdelicGL (r, a)) c`: the Euclidean norm of the vectors `(r v)⁻¹ (Φ v c)` at all
infinite places `v` taken together, with `Φ v` the embedding at `v`. Further, `|·|` is the idele
absolute value, `f` the number of infinite places and `rd` the root discriminant. 

### `siegel_lemma`

 A form of Siegel's lemma (compare Bombieri–Vaaler). A subspace `T` of `E^κ` of codimension `s`
is (a) the hermitian orthogonal of `s` vectors `X i` that are (b) nonzero and in `E^κ ∩ u Ô^κ`, with
(c) `(∏ ‖X i‖) ^ (2 f) ≤ (8 f s rd) ^ (f s) * d`. The length is Euclidean over all `f` infinite
places together and `rd` is the root discriminant. 

### `exists_inv_sublatticeDiscriminant_pow_le_prod`

 Siegel's lemma, raised to the power `k + 1` with `k = #κ`, as a bound for one term of the height
zeta function. A subspace `T` of `E^κ` of codimension `s` is the hermitian orthogonal of `s` nonzero
vectors `X i` of `E^κ ∩ u Ô^κ` with `(d T)⁻¹ ^ (k + 1) ≤ ∏ (‖X i‖⁻¹ ^ (2 n) C)`, where
`n = f (k + 1)`, `C = (8 f k rd) ^ n`, `f` is the number of infinite places and `rd` the root
discriminant. 

### `tsum_sublatticeDiscriminant_inv_le`

 The height zeta function of the subspaces of codimension `s` converges at `k + 1`, `k = #κ`.
Then `∑ (d T)⁻¹ ^ (k + 1) ≤ (200 f k rd) ^ (f (k + 1) s)`, the sum over all subspaces `T` of `E^κ`
of codimension `s`. Here `rd` is the root discriminant of `E` and `f = numInfPlaces E` the number of
infinite places. 
