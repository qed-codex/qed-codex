---
{
  "module": "src/Lib/General/Groups/BesselGroups.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/BesselGroups.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/BesselGroups.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Block triangular groups, unipotent Bessel groups, Levi and parahoric subgroups

This file treats matrix groups over a commutative ring `R`, with an involution where unitary groups
are concerned. The space has the basis `e₁, …, e_ϱ`, then a middle block, then `e*₁, …, e*_ϱ`; the
index type is `New.SplitIndex ϱ μ`. The form `New.Shape.Form.splitGram T` consists of `ϱ` hyperbolic
planes and the middle Gram matrix `T`. In `New.Shape.BesselIndex` the middle block is `κ` and one
more vector `z`.

The file also defines the Kronecker product of a finite family of matrices and the character
`New.wave` of `ℂ`.

* `New.BesselIndex.level`, `New.Shape.besselFrame`, `New.Shape.Form.frameGram`: the levels of the
  basis vectors, the frame `(e₁, …, e_ϱ, z)`, and the products of the frame with its image under
  a matrix `γ`.
* `New.parabolic`, `New.agreeWithOneOn`, `New.unitriangular`: the block upper triangular matrices
  for a level function, the invertible matrices that agree with the identity on the entries picked
  out by a relation, and the block upper triangular matrices with all diagonal blocks `1`.
* `New.Shape.Form.besselU`, `New.Shape.Form.besselU0`: subgroups of the unitary group
  `New.Shape.Form.G` cut out by such conditions, where `New.U` is the unitary group of a Gram
  matrix.
* `New.levi`, `New.parahoric`: the Levi subgroups and the parahoric subgroups of `GL_k` over a
  commutative local ring.

## Relation to the literature

Known; see `Lib.DiscreteSeries.Bruhat.FloorGroups` for sources.


### `Shape`

 The shape of a hermitian space with ϱ hyperbolic planes, a summand X₀ and a vector z: the
number ϱ, a finite index set κ for X₀, and one index k₀ in κ. 

### `Shape.ϱ`

 The number ϱ of hyperbolic planes. 

### `Shape.κ`

 The index set of a basis of X₀. 

### `Shape.fintypeIndex`

 The instance that κ is finite. 

### `Shape.k₀`

 A distinguished index in κ. 

 ### Tensor products of matrices and a character 

### `kroneckerPi`

 The Kronecker product of a finite family of matrices A s: the entry at (β, α) is the product
over s of the entries of A s at (β s, α s). 

### `kroneckerPi_mul`

 The Kronecker product of the products A s * B s is the product of the Kronecker product of the
matrices A s and that of the matrices B s. 

### `wave`

 The function `c ↦ exp (c - conj c)`, a character of `ℂ` of absolute value `1`. 

 ### The basis, its levels, the form and the frame 

### `SplitIndex`

 The index set made of ϱ indices, a middle set μ, and ϱ further indices, as a disjoint union. 

### `Shape.MiddleIndex`

 The index set of a basis of X₀ ⊕ ⟨z⟩: the indices κ of X₀ and one more index for z. 

### `Shape.BesselIndex`

 The index set of the basis e₁, …, e_ϱ, x_i (i in κ), z, e*₁, …, e*_ϱ, whose middle block is κ
plus one point. 

### `Shape.n`

 The number n = ϱ + 1 of vectors in the frame (e_1, …, e_ϱ, z). 

### `Shape.indexX₀`

 The index, in the basis of the whole space, of the basis vector j of X₀. 

### `Shape.z`

 The index of z in the basis of the whole space. 

### `Shape.top`

 The last position in the frame (e_1, …, e_ϱ, z), that of z. 

### `Shape.Form`

 The square matrices over R indexed by `New.Shape.MiddleIndex`, used as Gram matrices on
X₀ ⊕ ⟨z⟩. 

### `Shape.k`

 The rank k of X₀: the number of elements of κ. 

### `Shape.r`

 The rank r of the whole space: the number of elements of the basis index set
`New.Shape.BesselIndex`. 

### `BesselIndex.level`

 The natural-number level of a basis index: i for index i of the first block, ϱ on the middle
block, 2ϱ−i for index i of the last block. 

### `eStar`

 The index of the basis vector e*_a, in the last of the three blocks. 

### `Floors.hyperbolicGram`

 The Gram matrix of hyperbolic planes indexed by σ plus the form T: identity blocks pair the
two copies of σ, and T is the middle block. 

### `Shape.besselFrame`

 The indices of the frame (e₁, …, e_ϱ, z) among the basis indices. 

### `Shape.middleGram`

 For N in R, the diagonal matrix on κ plus one point with entries 1 on κ and −N at the extra
point. 

### `Shape.Form.splitGram`

 The Gram matrix of ϱ hyperbolic planes and a middle space with Gram matrix T: identity
blocks pair the first and last ϱ indices, T is the middle block, all else is zero. 

 ### Block triangular groups 

### `parabolic`

 The subgroup of GL_n(R) of matrices that are block upper triangular for the level function
lev. 

### `blockHom`

 The homomorphism sending a block upper triangular invertible matrix to its diagonal block of
level a. 

### `agreeWithOneOn`

 Let r be a relation on the indices such that r i j implies r i k or r k j for every k. This is
the group of invertible matrices over R that agree with the identity matrix at every entry (i, j)
with r i j. 

### `unitriangular`

 The group of block upper triangular matrices all of whose diagonal blocks are the identity. 

### `mem_agreeWithOneOn`

 A matrix lies in `agreeWithOneOn r R h_split` exactly when it agrees with the identity matrix
at every entry (a, b) with r a b. 

### `conj_mem_unitriangular`

 If `d` is block upper triangular and `u` is block upper unitriangular, both for the level
function `lev`, then `d⁻¹ * u * d` is block upper unitriangular for `lev`. 

### `det_eq_one_of_unitriangular`

 A matrix has determinant `1` if it is block upper unitriangular for the level function `lev`,
that is, agrees with the identity matrix at every entry (a, b) with `lev b ≤ lev a`. 

 ### Minors, diagonal scalings, frame matrices and the unitary group 

### `leadingMinor`

 The leading principal minor of order `l`: the determinant of the upper left `l × l` block of the
`i × i` matrix `Z`, for `0 ≤ l ≤ i`. 

### `Filling.scaleAt`

 The diagonal matrix on μ with entry p at the index k₀ and 1 at every other index. 

### `frameImage`

 The columns of γ at the frame indices, that is the image γf of the frame f = (e₁,…,e_ϱ,z). 

### `Shape.Form.frameGram`

 The (ϱ+1) × (ϱ+1) matrix of the products h(f_j, γ f_l) of the frame f with its image under γ,
where h is the form `New.Shape.Form.splitGram T`. 

### `Shape.Form.G`

 The unitary group of the form `New.Shape.Form.splitGram T` on the whole space: the invertible
matrices that preserve this Gram matrix. 

### `frameMatrix`

 The square submatrix of γ on the rows and columns of the frame (e₁, …, e_ϱ, z). 

 ### The Bessel groups, Levi and parahoric subgroups 

### `Shape.Form.besselU`

 The Bessel unipotent group 𝖴: the isometries of `New.Shape.Form.splitGram T` that are block
upper unitriangular for the levels `New.BesselIndex.level`, so that their middle diagonal block
is the identity. 

### `Shape.Form.besselFixer`

 The fixer of the frame in the unitary group: the elements that fix each of its vectors. 

### `Shape.Form.besselU0`

 The elements of the Bessel unipotent group 𝖴 that fix each vector of the frame. 

### `levi`

 The Levi subgroup of a labelling τ of the indices: matrices in GL_k(W), W local, whose (i,j)
entry vanishes whenever τ(i) ≠ τ(j). 

### `parahoric`

 The parahoric subgroup of a labelling τ: matrices in GL_k(W), W local, whose (i,j) entry
lies in the maximal ideal whenever τ(i) < τ(j). 
