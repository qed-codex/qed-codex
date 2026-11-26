---
{
  "module": "src/Lib/Adelic/Witt/WittTheorem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Witt/WittTheorem.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Witt/WittTheorem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Witt's theorem over fields and over Ô; quasi-reflections, Eichler maps, frames

`J` is a hermitian matrix over a commutative ring with involution, with form
`h(u, v) = star u ⬝ᵥ J *ᵥ v`, and `New.U J` is the group of invertible `g` with `gᴴ * J * g = J`.
For invertible such `J`, Witt's theorem says that left invertible matrices with equal Gram matrices
differ by an element of `New.U J`. It is proved over a field with nontrivial involution using
quasi-reflections. Let `E` be a CM field that contains a primitive root of unity of order 5040
(`New.HasPrimitiveRoot5040 E`). Over its integral finite adeles `New.Ô E`, invertible hermitian
matrices have orthonormal bases, units fixed by conjugation are norms, and Witt's theorem is proved
for the standard hermitian form and primitive matrices, with an integral unitary matrix. For the
split form `T.splitGram` with `ϱ` hyperbolic planes and middle block `T`, the file then studies the
frame `f = (e₁, …, e_ϱ, z)` (`𝔰.besselFrame`, whose last entry `𝔰.besselFrame 𝔰.top` is `z`) and the
action of the unipotent group `New.Shape.Form.besselU` on it.

## Main definitions and results

* `New.quasiReflection`: the quasi-reflection along `v`, for a unit `σ` with `σ + star σ = h(v, v)`.
* `New.witt_of_quasiReflection_mem`: left invertible `X`, `Y` with the same Gram matrix satisfy
  `g * X = Y` for some `g` in any subgroup of `New.U J` that contains all quasi-reflections.
* `New.witt`: the same with `g` in `New.U J`.
* `New.exists_orthonormal_Ô`: a hermitian matrix invertible over `Ô` is `Ô`-congruent to `1`.
* `New.witt_Ô`: Witt's theorem for primitive `n × k` matrices over `Ô`.
* `New.exists_unitary_eq_eichlerMap`: for hermitian `J`, the Eichler map
  `v ↦ v + h(u, v) x - h(x, v) (u + ς x)` (`New.eichlerMap`) is an isometry if `x` is isotropic, `u`
  is orthogonal to `x` and `ς + star ς = h(u, u)`.

Notions from other files:
* `New.Shape`: the data `𝔰` of a number `ϱ` of hyperbolic planes and a finite index set `κ`. A
  `T : 𝔰.Form A` is a square matrix indexed by `κ` and one more index `z`.
* `New.Shape.Form.splitGram`: the Gram matrix of ϱ hyperbolic planes and a middle space with Gram
  matrix T: identity blocks pair the first and last ϱ indices, T is the middle block, all else is
  zero. Its unitary group is `T.G`.
* `New.Shape.Form.frameGram`: the (ϱ+1) × (ϱ+1) matrix of the products h(f_j, γ f_l) of the frame f
  with its image under γ, where h is the form `New.Shape.Form.splitGram T`.
* `New.frameMatrix`: the submatrix of γ on the rows and columns of the frame.
* `New.intGL`: for a subring O of R, the subgroup GL_n(O) of GL_n(R): matrices with entries in O
  whose inverse has entries in O.

## Relation to the literature

Known; see `Lib.Adelic.Witt.IwasawaDecomposition`, `Lib.DiscreteSeries.Bruhat.FloorGroups` and
`Lib.DiscreteSeries.Bruhat.ComplexPlace` for sources.



## Left invertible and primitive matrices, quasi-reflections

* `New.IsPrimitiveMatrix`: a matrix and some left inverse of it have entries in a subring.


### `HasLeftInv`

 The n × k matrix X over R has a left inverse over R. 

### `colSpan`

 The submodule of R^n spanned by the columns of the matrix X. 

### `IsPrimitiveMatrix`

 The matrix X has entries in the subring O and a left inverse with entries in O. 

### `noncomputable instance [IsLocalRing R] : StarRing (ResidueField R)`

 The involution of a local ring induces an involution of its residue field. 

### `star_dotProduct_mulVec_comm`

 The form h(u, v) = uᴴ J v of a hermitian matrix `J` is hermitian: the conjugate of h(u, v) is
h(v, u). 

### `quasiReflection`

 The quasi-reflection x ↦ x − v σ⁻¹ h(v, x) in U(J), where h(v, x) = vᴴJx, J is hermitian and
invertible, and σ is a unit with σ + σ̄ = h(v, v). 

### `quasiReflection_mulVec`

 The quasi-reflection along `v` with parameter `σ` sends `x` to `x − σ⁻¹ h(v, x) v`. 


## Witt's theorem over a field with involution

Witt's extension theorem for an invertible hermitian matrix `J` over a field with an involution that
is not the identity (some `z - star z` is a unit).

The columns are matched one at a time, each by at most two quasi-reflections that fix the columns
already matched.


### `HasLeftInv.of_ker_le_bot`

 A matrix `X` over a field whose map `x ↦ X *ᵥ x` has trivial kernel has a left inverse. 

### `HasLeftInv.of_ne_zero`

 A nonzero vector over a field, read as a matrix with one column, has a left inverse. 

### `HasLeftInv.exists_dotProduct_mulVec_col_eq_ite`

 If `A` is invertible and `X` has a left inverse, then for each column index `j` some linear form
`x ↦ a ⬝ᵥ A *ᵥ x` is `1` on column `j` of `X` and `0` on the other columns. 

### `Filling.exists_hasLeftInv_colSpan_eq`

 A subspace `L` of `n → R` has a basis written as the columns of an `n × d` matrix `x`, where `d`
is the dimension of `L`: `x` has a left inverse and its column space is `L`. 

### `exists_units_add_star_eq`

 In a field with an involution that is not the identity, every `c` fixed by the involution is
the trace `σ + star σ` of a unit `σ`. 

### `exists_quasiReflection_mulVec_eq`

 Let `J` be hermitian and invertible, with form h(u, v) = uᴴ J v. If h(x, x) = h(y, y) and
h(y, y − x) ≠ 0, then a quasi-reflection along `x − y` sends `x` to `y`. 

### `witt_of_quasiReflection_mem`

 Witt's theorem by quasi-reflections: over a field with involution having some z ≠ z̄, for
invertible hermitian J and a subgroup H of the unitary group U(J) containing all quasi-reflections
x ↦ x − v σ⁻¹ vᴴJx, left invertible X, Y with XᴴJX = YᴴJY satisfy gX = Y for some g in H.

A variant of Witt's extension theorem for nondegenerate hermitian forms. 

### `witt`

 **Witt's theorem.** Let `R` be a field with an involution that is not the identity and let `J`
be an invertible hermitian matrix. Left invertible `X`, `Y` with `Xᴴ * J * X = Yᴴ * J * Y` satisfy
`g * X = Y` for some `g` in the unitary group `U J` of the `g` with `gᴴ * J * g = J`.

Known result: Witt's extension theorem for hermitian forms. 


## Orthonormal bases and norms over Ô

Two consequences of `E` containing a primitive root of unity of order `7! = 5040`
(`New.HasPrimitiveRoot5040`), for the ring `New.Ô` of integral finite adeles of a CM field `E`. This
hypothesis is stronger than `E/E⁺` being unramified at the finite places. It is used through an
element `z` of `Ô E` with `z - star z` a unit (`New.exists_isUnit_sub_star_Ô`), which gives
orthonormal frames over the profinite ring `Ô E` (`New.exists_fixed_orthonormal_frame`).

* `New.exists_orthonormal_Ô`: a hermitian matrix invertible over `Ô` is `Ô`-congruent to `1`.
* `New.exists_unit_star_mul_self_eq`: a conjugation-invariant unit of `Ô` is a norm `star x * x`;
  this is the case of `1 × 1` matrices.


### `exists_isUnit_sub_star_Ô`

 If the CM field `E` contains a primitive root of unity of order 5040, the ring `Ô E` of its
integral finite adeles has an element `z` such that `z - star z` is a unit. 

### `exists_orthonormal_frame_Ô`

 Let the CM field `E` contain a primitive root of unity of order 5040. An invertible hermitian
matrix `b` over the ring `Ô E` of integral finite adeles has an orthonormal frame `g` that is
congruent to `1` modulo the left ideal generated by `b - 1`. 

### `New.exists_orthonormal_Ô`

 Let the CM field `E` contain a primitive root of unity of order 5040, and let `Ô E` be its ring
of integral finite adeles. A hermitian matrix `b` with entries in the finite adeles `𝔸f E`, lying in
`GL_n(Ô E)` (`IsUnimodular (Ô E) b`) satisfies `kᴴ b k = 1` for some `k` in `GL_n(Ô E)`.

An adelic variant, over all finite places at once, of the local fact that unimodular hermitian
lattices in the unramified case have orthonormal bases (Kirschmer). 

### `New.exists_unit_star_mul_self_eq`

 Let the CM field `E` contain a primitive root of unity of order 5040. Every
conjugation-invariant finite adele `u` of `E` that is a local unit at every finite place is the norm
`star x * x` of a unit `x` of the ring `Ô E` of integral finite adeles.

Units are norms in unramified extensions of local fields (cf. Jacobowitz, Kirschmer). This is the
quadratic case of conjugation on `E`, at all finite places at once, split places included. 


## Witt's theorem over Ô

Witt's theorem for the standard hermitian form over the integral finite adeles `New.Ô E` of a CM
field `E`: primitive matrices with the same Gram matrix differ by an integral unitary matrix.

* `New.isPrimitiveMatrix_iff`: a square matrix is primitive over `O` iff it lies in `New.intGL n O`.

The proof finds an invertible `a` with `a * X = Y` and `aᴴ * Y = X`. It then makes `a` unitary with
an orthonormal frame of `aᴴ * a` (`New.exists_orthonormal_frame_Ô`).


### `IsPrimitiveMatrix.exists_map_subtype_eq`

 A matrix that is primitive over the subring `O` (it and some left inverse have entries in `O`)
comes from a left invertible matrix over the ring `O`. 

### `isPrimitiveMatrix_iff`

 A square matrix is primitive over the subring `O` (it and some left inverse have entries in `O`)
iff it is invertible and both it and its inverse have entries in `O`. 

### `isUnit_of_forall_isUnit_reduceAt`

 A square matrix over the ring `Ô E` of integral finite adeles is invertible if its reduction
to the residue field at every finite place is invertible. 

### `exists_isUnit_add_Ô`

 For square matrices `a`, `x`, `y` over the ring `Ô E` of integral finite adeles of a number
field `E`, there is a matrix `c` such that `a + (1 - a * x) * c * (1 - y * a)` is invertible. 

### `exists_isUnit_mul_eq_and_conjTranspose_mul_eq`

 For left invertible matrices `X`, `Y` over the ring `Ô E` of integral finite adeles of a CM
field `E` with `Xᴴ X = Yᴴ Y`, some invertible `a` sends `X` to `Y` while its adjoint sends `Y`
to `X`. 

### `witt_Ô`

 Witt's theorem over the ring `Ô E` of integral finite adeles of a CM field `E` that contains a
primitive root of unity of order 5040: two `n × k` matrices `X`, `Y` with entries in `Ô E`, left
inverses over `Ô E` and `Xᴴ X = Yᴴ Y` satisfy `g X = Y` for some `g` in `stdLevel E n`, the group of
`g` in `GL_n(Ô E)` with `gᴴ g = 1`.

An integral variant of Witt's extension theorem for hermitian forms. It treats only the standard
form, not a general invertible hermitian matrix. 

### `witt_Ô_of_orthonormal`

 Witt's theorem for orthonormal frames over the ring `Ô E` of integral finite adeles of a CM
field `E` that contains a primitive root of unity of order 5040: if the matrices `X` and `Y` over
the finite adeles `𝔸f E` have entries in `Ô E` and Gram matrix `1` for the hermitian form with
matrix `1`, then `g * X = Y` for some `g` in `stdLevel E n`, the group of `g` in `GL_n(Ô E)` with
`gᴴ g = 1`. 


## The unipotent Bessel group acting on the frame

The basis indices `New.Shape.BesselIndex` are `e₁, …, e_ϱ`, then the middle indices (those of `κ`
and `z`), then `e*₁, …, e*_ϱ`.

* `New.eq_one_of_mem_besselU_of_fix`: an element of `New.Shape.Form.besselU` that fixes ϱ vectors
  whose coordinates at `e*₁, …, e*_ϱ` form the identity matrix is trivial.


### `level_besselFrame`

 The vector in position `a` of the frame (e₁, …, e_ϱ, z) has level `a`, where `level` is the
grading of the basis indices for which `New.Shape.Form.besselU` is block unitriangular. 

### `le_level_inr`

 For the grading `level` of the basis indices, for which `besselU` is block unitriangular, the
middle indices (of level ϱ) and those of e*₁, …, e*_ϱ (of level 2ϱ − a in position `a`) have level
at least ϱ. 

### `frameMatrix_unitriangular`

 An element `x` of the block unitriangular group `New.Shape.Form.besselU` acts on the frame
(e₁, …, e_ϱ, z) by an upper unitriangular matrix: `frameMatrix x`, the submatrix of `x` on the
frame, agrees with the identity on and below the diagonal. 

### `mem_besselU0_iff`

 An element of the unitary group `T.G` lies in `besselU0`, the elements of the block
unitriangular group `besselU` that fix each vector of the frame (e₁, …, e_ϱ, z), iff it lies in
`besselU` and its submatrix on the frame is the identity. 

### `apply_inr_of_mem_besselU`

 Let `T.G` be the unitary group of the split form `T.splitGram` on the basis e₁, …, e_ϱ, x_i
(i ∈ κ), z, e*₁, …, e*_ϱ, indexed by `𝔰.BesselIndex`. Let `x'` lie in the Bessel unipotent group
`T.besselU` of isometries that are block upper unitriangular for the levels, with identity middle
block. In the middle rows and the rows e*₁, …, e*_ϱ (the rows `inr i`), and in every column other
than those of e*₁, …, e*_ϱ (the indices `eStar a`), the entries of `x'` are those of the identity
matrix. 

### `eq_one_of_mem_besselU_of_fix`

 Let `besselU` be the group of isometries of the split form `splitGram T` that are block upper
unitriangular. The form is taken on the basis e₁, …, e_ϱ, x_i, z, e*₁, …, e*_ϱ (`BesselIndex`), with
`T` its Gram matrix on X₀ ⊕ ⟨z⟩, where X₀ is spanned by the x_i (i ∈ κ). An element `x'` of
`besselU` is 1 if it fixes ϱ vectors (the columns of `B`) whose coordinates at e*₁, …, e*_ϱ (the
last block of rows, `B.toRows₂.toRows₂`) form the identity matrix. 

### `submatrix_mul_besselFrame`

 An element `x'` of the block unitriangular group `New.Shape.Form.besselU` maps the frame
(e₁, …, e_ϱ, z) into its span. So the frame columns of `M * x'` are those of `M` times
`frameMatrix x'`, the submatrix of `x'` on the frame. The rows of `M` are indexed by an arbitrary
type `m`, and `e : n → m` selects any family of them. 

### `frameMatrix_mul`

 The submatrix on the frame (e₁, …, e_ϱ, z) is multiplicative when the right factor lies in the
block unitriangular group `New.Shape.Form.besselU`. 

### `frameGram_inv_mul_mul`

 Let `Z(γ) = T.frameGram γ` be the matrix of the products `h(f_j, γ f_l)` for the frame
`f = (e₁, …, e_ϱ, z)` and the split form `h` with middle block `T`, whose unitary group is `T.G`.
Suppose `x`, `x'` lie in the Bessel unipotent group `T.besselU`, the isometries that are block upper
unitriangular with identity middle block. If `m = frameMatrix x` and `m' = frameMatrix x'` are their
submatrices on the frame, then `Z(x'⁻¹ γ x) = m'ᴴ Z(γ) m`. 


## Eichler isometries and leading minors of the frame matrix

Eichler maps in the unitary group `New.U J`, and the matrix `Z(γ) = T.frameGram γ` of the products
of the frame with its image under `γ`.

* `New.Filling.frameGram_inv`: `Z(γ⁻¹) = Z(γ)ᴴ` when the split form is hermitian and invertible.


### `eichlerMap`

 The matrix of the Eichler map v ↦ v + h(u, v)x − h(x, v)(u + ςx), where h is the form of J.

A variant of the standard Eichler transformation of a hermitian form, without the usual conditions
on x, u, ς that make it an isometry. 

### `exists_unitary_eq_eichlerMap`

 Let `J` be hermitian, with form h(v, w) = vᴴ J w. Suppose `x` is isotropic for h, `u` is
orthogonal to `x`, and `ς + star ς = h(u, u)`. Then the Eichler map `New.eichlerMap J x u ς` is the
matrix of an element of the unitary group `New.U J`. 

### `Filling.frameGram_eq_frameImage`

 The matrix `T.frameGram γ` is `fᴴ J (γ f)`, where `J = T.splitGram` and `frameImage γ` consists
of the columns of `γ` at the frame indices, so that `f = frameImage 1` is the frame itself. 

### `Filling.frameGram_inv`

 If the split form `T.splitGram` is hermitian and invertible, then `Z(γ⁻¹) = Z(γ)ᴴ` for unitary
`γ`, where `Z(γ) = T.frameGram γ` is the matrix of the products `h(f_j, γ f_l)`. 

### `exists_mulVec_eq_single_det`

 Cramer's rule for the last basis vector: for an `(m + 1) × (m + 1)` matrix `Z` over a
commutative ring, some `y` has `Z y = det Z` times the last basis vector, and the last coordinate
of `y` is the leading `m × m` minor of `Z`. 
