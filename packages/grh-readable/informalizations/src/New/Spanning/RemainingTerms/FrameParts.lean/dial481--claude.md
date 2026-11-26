---
{
  "module": "src/New/Spanning/RemainingTerms/FrameParts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/FrameParts.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/FrameParts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The part in `X₀` of a frame, moves, and lifts of a lattice

The lemmas that are used to count, round by round, the frames over a lattice `L ⊆ Λ ∩ X₀`, where `Λ`
is the lattice of a class. A move is a unipotent element of the congruence level `M` that fixes the
standard frame. For a term, `Ξ₀` consists of the first `ϱ` rows of the matrix of products, and `δ`
is the leading minor of that matrix whose order is the cell rank of the term.

Notions from other files:
* The frame is `e₁, …, e_ϱ, z`, `A` is the isotropic space spanned by the `e_i`, and `X₀` is the
  space with the indices `𝔰.κ`; `frameMiddle` takes the coordinates in `X₀ ⊕ Ez` of a frame.
* `frameProducts γ` is the matrix of products of the frame with its image under `γ`.
* `translateByClassReps c c' γ` is `h_c⁻¹ γ h_c'`, and `γ ∈ termsOver c s c'` says that it
  stabilises the standard lattice and has the reduction `s`.
* `classCoordX₀ c` gives the coordinates of vectors of `X₀` in the lattice `Λ` of the class `c`;
  `classLatticeX₀ c` is `Λ ∩ X₀`.
* `termLattice c c' γ` consists of the vectors `v` of `Λ ∩ X₀` such that some vector of
  `v + M (Λ ∩ A)` is orthogonal to the frame of `γ`.

## Main definitions and results

* `New.Filling.exists_framePartX₀_mul_eq_sub_smul`: every row `η` of vectors of `Λ ∩ X₀` gives a
  move, which subtracts `M η Ξ₀` from the part in `X₀` of a frame.
* `New.Filling.exists_isLift`, `New.Filling.exists_conjTranspose_mul_eq_of_row_mem`: if `L` lies in
  the lattice of a term, it lifts linearly to vectors orthogonal to the frame; two lifts in one
  coset of the products with vectors of `L` differ by the products with a rational row `η`.
* `New.Filling.complementLattice`: the lattice `P = Λ ∩ X₀ ∩ L^⊥`, which has the corank of `L` as
  its rank.
* `New.Filling.HasCellRank.exists_framePartX₀_sub_eq`: parts in `X₀` that are congruent modulo
  `M δ` differ by `M η Ξ₀`.


 ## Matrices and lattices over the finite adeles 

### `exists_mul_eq_of_finAdeleMatrix_mul_eq`

 A linear system `M w = T` over `E` that has a solution `s` over the finite adeles
(`finAdeleMatrix` reads a rational matrix there) has rational solutions near `s`: every open set
that contains `s` contains one. 

### `exists_isIntMatrix_mul_eq_of_col_mem`

 A matrix whose columns lie in the column lattice of `ξ` is `ξ` times an integral matrix. 

### `colLattice_smul`

 Scaling a matrix by an idele scales the lattice spanned by its columns. 

### `injective_restrictScalars_mulVecLin`

 Multiplication by an adelic matrix with a left inverse is injective. 

### `isIntMatrix_mul_finAdeleMatrix_inv_smul`

 Let the idele `d` be the nonzero number `δ`. If the columns of the rational matrix `v` lie in
`d` times the lattice of the vectors that `H` makes integral, then `H` makes `δ⁻¹ v` integral. 

### `submoduleIndex_colLattice_mul`

 Let `m` have a left inverse, and let `A` be invertible over the finite adeles, with integral
entries. Then the lattice spanned by the columns of `m A` has index `[det A]`, the generalised
index, in the lattice spanned by the columns of `m`. 

### `submoduleIndex_colLattice_gram_transpose`

 Let the columns of the rational matrix `y` be independent, and let `L` be the lattice with the
basis `B = y a`, where `Bᴴ B` is integral. The rows of the products of `B` with the vectors of `L`
are the integral combinations of the rows of `Bᴴ B`. Their index among all integral rows, that is
the index of `L` in its dual lattice, is the square of `discriminant r L`, which is by definition
the square root of the generalised index of the Gram determinant `det (Bᴴ B)`. 

### `coe_mem_saturatedLattice`

 Let the adelic matrix `H` have a left inverse. A rational vector of the subspace `V` that `H`
makes integral lies in the saturated lattice of `V`, the lattice of the vectors in the adelic span
of `V` that `H` makes integral. 

### `submoduleIndex_smul_saturatedLattice`

 Let the adelic matrix `H` have the left inverse `H'`, and let `Λ` be the saturated lattice of
the subspace `V`, the lattice of the vectors in the adelic span of `V` that `H` makes integral. For
a finite idele `d` in `Ô`, the index of `d Λ` in `Λ` as additive groups is `[d] ^ dim V`. Here
`[d] = genIndex d` is the generalised index, the inverse of the factor by which `d` scales Haar
measure on the finite adeles. 

 ## The part in `X₀` of a frame, and moves 

### `framePartX₀`

 The part in `X₀` of the frame of `γ`: the coordinates at the indices `𝔰.κ` of the images of the
frame vectors. 

### `frameProducts_castSucc_apply`

 The product of an isotropic frame vector with the image of a frame vector is the coordinate of
the image at the dual isotropic vector. 

### `frameProducts_top_apply`

 The product of `z` with the image of a frame vector is `-N` times the coordinate of the image
along `z`. 

### `apply_inr_besselFrame_eq`

 Two frames with the same products and the same part in `X₀` agree outside the isotropic
space. 

### `exists_framePartX₀_mul_eq_sub_smul`

 Let `E` contain a primitive 5040th root of unity, let `S` be a filling of shape `𝔰` with the
congruence level `M = S.M`, and let the `ϱ` columns of `η` be rational vectors of `Λ ∩ X₀`. Then
there is a move `u`, that is, a rational unipotent element of level `M` for `Λ` that fixes the
standard frame, with the following property. For every `γ`, the coordinates in `X₀` of the frame of
`u γ` (`framePartX₀`) are those of the frame of `γ` minus `M η Ξ₀`. 

### `frameMiddle_translateByClassReps`

 The middle part of the frame of the translate by class representatives `h_c⁻¹ γ h_c'`, in the
coordinates of the lattice of the class `c`: the part in `X₀` is carried over by `S.classCoordX₀ c`,
and the part along `z` stays. 

### `frameMiddle_translateByClassReps_mul_classCoordX₀`

 The `frameMiddle` of the translate gives the coordinates in `X₀ ⊕ Ez` of the image of the frame
under `γ`, in the basis of the lattice `h_c Λ₀` of `c`. Take the products of these vectors with the
columns of `S.classCoordX₀ c`, using the Gram matrix `S.latticeMiddle (𝔸f E)` of `X₀ ⊕ Ez` in the
lattice basis. They equal the conjugate transpose of `framePartX₀ γ`, the coordinates in `X₀` of
that image, embedded in the finite adeles. 

### `col_framePartX₀_sub_mem`

 Let `Λ` be the lattice of the class `c`. The parts in `X₀` of two frames of terms over `c` with
the same matrix of products differ by vectors of `Λ ∩ X₀`. 

 ## Lifts of a lattice 

### `IsLift`

 Let `L` be the lattice with the basis `y a`, where `y` is rational and `a` is adelic, let
`e_1, …, e_ϱ` be the basis of the isotropic space `A` and of the lattice `Λ ∩ A`, and let `M = S.M`.
The matrix `w` gives a linear map from `L` to `M (Λ ∩ A)`, namely `y t ↦ M ∑ e_i (w t)_i`, such that
each vector of `L` plus its image is orthogonal to the frame of `γ`. 

### `IsLift.isIntMatrix`

 The map takes the basis `y a` into `M (Λ ∩ A)`. 

### `IsLift.orthogonal`

 The lifted vectors are orthogonal to the frame of `γ`. 

### `exists_isLift`

 The lattice `L_γ = S.termLattice c c' γ` consists of the vectors `v` of `Λ ∩ X₀` such that some
vector of `v + M (Λ ∩ A)` is orthogonal to the frame of `γ`. If the lattice spanned by the columns
of `y a` lies in `L_γ`, then it has a rational lift: a linear map to `M (Λ ∩ A)`, given by a
rational matrix `w`, such that each vector plus its image is orthogonal to the frame of `γ`. 

### `submoduleIndex_gram_eq_discriminant_sq`

 Let `E` contain a primitive 5040th root of unity. Let `L ⊆ Λ ∩ X₀` have the basis `B = y a`,
where `Λ` is the lattice of the class `c` and the columns of `y` are independent. The lattice
spanned by the rows of `Bᴴ B` has the index `(disc L) ^ 2` in the integral rows: this is the index
of `L` in its dual. 

### `exists_conjTranspose_mul_eq_of_row_mem`

 Let `Λ` be the lattice of the class `c`, and let `L ⊆ Λ ∩ X₀` have the basis `m = y a`, where
the columns of the rational matrix `y` are independent. Let `w` be a rational matrix such that each
row of `w a` is an integral combination of the rows of the Gram matrix `mᴴ m`; that is, the map
`y t ↦ w t` is given by products with vectors of `L` over the finite adeles. Then it is given by the
products with a row `η` of rational vectors of `Λ ∩ X₀`. 

### `IsLift.exists_conjTranspose_framePartX₀_mul_eq_neg`

 Let `L ⊆ Λ ∩ X₀` have the basis `m = y a`, with `Λ` the lattice of the class `c` and the columns
of `y` independent. Let `M = S.M` be the congruence level, let `Ξ₀` be the first `ϱ` rows of the
matrix of products of the standard frame with its image under `γ`, and write `F(γ) = framePartX₀ γ`
for the coordinates in `X₀` of that image. Let `w` be a lift of `L` for `γ`: the matrix `w a` is
integral and `F(γ)ᴴ y + M Ξ₀ᴴ w = 0`. Let each row of `w' a - w a` be an integral combination of the
rows of `mᴴ m`. Then `F(u γ)ᴴ y = -M Ξ₀ᴴ w'` for some move `u ∈ S.classUnipotent₀ c`. 

 ## The lattice orthogonal to `L` 

### `complementLattice`

 The lattice `P = Λ ∩ X₀ ∩ L^⊥`, where `Λ` is the lattice of the class `c` and the columns of `y`
span the same space as `L`. 

### `coe_mem_complementLattice`

 Let `Λ` be the lattice of the class `c`. A rational vector of `Λ ∩ X₀` that is orthogonal to the
columns of `y` lies in the lattice `P = complementLattice c y`. 

### `submoduleIndex_smul_complementLattice`

 Let `Λ` be the lattice of the class `c`, and let `P` be the lattice of the vectors of `Λ ∩ X₀`
orthogonal to the columns of `y`. If these `r` columns are independent and `r + l = k`, then `P` has
the rank `l`: for a finite idele `d` in `Ô`, the index of `d P` in `P` is `[d] ^ l`, where `[d]` is
the generalised index. 

 ## Congruent parts in `X₀` 

### `HasCellRank.sum_norm_sq_sub_mul_inv_lt_one`

 Let `γ` and `γ'` have the same matrix `Z` of products of the standard frame with its image, and
the cell rank `j`. For `γ` this means, with `D_i` the leading minor of order `i` of `Z`: for some
`t` with `t star t = 1` and every index `a ≥ j`, the flags of the frame and of its image share a
vector with leading coefficients `t` and `1` at `a`; `D_j ≠ 0`; and
`S.termDisc γ = |D_{ϱ+1}|² - N² |D_ϱ|²`, with `N = S.N`, is nonzero exactly when `j = ϱ + 1`. Let
`Y` be the first `j` rows of `Z` completed by rows of `1`, and let `v` be the difference of the
coordinates in `X₀` of the two images of the frame. The last column and the columns `k ≥ j` of
`v Y⁻¹` have length below `1` under the complex embedding `Φ w` of every infinite place `w`, as each
is the difference of two vectors of squared length at most `1/5`. 

### `HasCellRank.exists_framePartX₀_sub_eq`

 Let `E` contain a primitive 5040th root of unity, and let `S` have the congruence level
`M = S.M`. Let `γ` and `γ'` have the same integral matrix `Z = S.frameProducts γ` of products of the
standard frame with its image, with the leading minor `δ` of order `j`. Let both have the cell rank
`j`: the flags of the frame and of its image share vectors at all indices from `j` on, up to a
number of norm one, `δ ≠ 0`, and `S.termDisc`, formed from the last two leading minors of `Z`, is
nonzero exactly when `j = ϱ + 1`. Let the idele `d` be the number `M δ`. If the coordinates in `X₀`
of the images of the frame under `γ'` and `γ` (`framePartX₀`) are congruent modulo `d (Λ ∩ X₀)`,
with `Λ` the lattice of the class `c`, then they differ by `M η Ξ₀`, where the columns of `η` are
rational vectors of `Λ ∩ X₀` and `Ξ₀` consists of the first `ϱ` rows of `Z`. 

### `HasCellRank.exists_framePartX₀_mul_eq_of_sub_mem`

 Let `γ` and `γ'` have the same matrix `Z = S.frameProducts γ`, with integral entries, of
hermitian products of the standard frame `(e₁, …, e_ϱ, z)` with its image under `γ`, and let `δ` be
the leading minor of `Z` of order `j`. Let both have cell rank `j` (`S.HasCellRank j`): the flags of
the frame and of its image share vectors at all indices from `j` on, up to a number of norm one,
`δ ≠ 0`, and `S.termDisc`, formed from the last two leading minors of `Z`, is nonzero exactly when
`j = ϱ + 1`. Let the idele `d` equal `M δ`. Suppose the coordinates in the definite summand `X₀` of
the images of the frame under `γ'` and `γ` (`framePartX₀`) are congruent modulo `d (Λ ∩ X₀)`. Then
`framePartX₀ (u γ') = framePartX₀ γ` for some `u ∈ S.classUnipotent₀ c`. 

 ## The moduli of the second and the third round 

### `genIndex_algebraMap_le_pow_of_norm_sq_le`

 An element of `E` whose squared absolute value is at most `b ^ e` at every infinite place has
generalised index at most `b ^ (e f)`, where `b = S.b` and `f` is the number of infinite places. 

### `IsNear.genIndex_M_mul_leadingMinor_le`

 Let `S` be admissible, with size parameter `b = S.b` and `M = S.M`, the product of the two level
primes. Let `ϱ = 𝔰.ϱ` and `n = 𝔰.n = ϱ + 1`, and let `f` be the number of infinite places. Let `γ`
be near: for some archimedean point `y`, both `y` and `γ⁻¹ y` lie in `S.boxedPoints`. Let
`δ = leadingMinor (S.frameProducts γ) j` be the leading minor of order `j ≤ ϱ + 1` of the matrix of
products of the standard frame with its image under `γ`. The generalised index of `M δ`, the
absolute value of its norm to `ℚ`, is at most `b ^ (2 n³ f)`. 

### `frameModulus_mem_integralAdeles_of_isIntegral`

 If `Z` has integral entries, then the modulus `S.frameModulus j Z = M det (Y Yᴴ)` is integral,
where `M = S.M` and `Y` consists of the first `j` rows of `Z` completed by rows of `1`. 

### `IsNear.genIndex_frameModulus_le`

 Let `S` be admissible, with the size parameter `b = S.b` and the congruence level `M = S.M`, let
`n = ϱ + 1`, and let `f` be the number of infinite places. Let `γ` be near: for some archimedean
point `y`, both `y` and `γ⁻¹ y` lie in `S.boxedPoints`. Let `δ` be the leading minor of any order
`j ≤ ϱ + 1` of the matrix of products of the standard frame with its image under `γ`. The modulus
`S.frameModulus` is `M δ star δ`. Its generalised index, the absolute value of its norm to `ℚ`, is
at most `b ^ (2 n³ f)`. 
