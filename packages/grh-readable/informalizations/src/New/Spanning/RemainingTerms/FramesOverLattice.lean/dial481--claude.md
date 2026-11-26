---
{
  "module": "src/New/Spanning/RemainingTerms/FramesOverLattice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/FramesOverLattice.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/FramesOverLattice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Counting frames over a lattice of small discriminant

Modulo moves, few frames of near terms have a lattice `L_γ^M` that contains a given lattice `L` of
small discriminant (`New.Filling.IsFrameSet.encard_le`, and for the terms of one label
`New.Filling.encard_setOf_isNearTermAt_and_le_termLattice_le`). After the cell rank and the matrix
of products are fixed, the frames are sorted in three rounds: by the lift of `L`, by the part in
`X₀`, and by the part in the isotropic space.

Notions from other files:

* `New.frameImage γ`: the frame `γ f` of `γ`, the image of the standard frame
  `f = (e₁, …, e_ϱ, z)` of `n = ϱ + 1` vectors; `S.frameProducts γ` is the matrix of products of
  `f` with `γ f`.
* `S.classUnipotent₀ c`: the group of moves for the class `c`.
* `S.HasCellRank j γ`: the element `γ` has cell rank `j ≤ ϱ + 1`: from the index `j` on, the flags
  of `f` and `γ f` share vectors whose two leading coefficients have the same norm, and the leading
  minor of order `j` of the matrix of products is nonzero; a further condition singles out
  `j = ϱ + 1`.
* `S.sharedVectors j γ`: the matrix whose columns `k ≥ j` are the coordinates in the isotropic
  space of the columns of `γ f · adj Y`, the others being `0`. Here `Y` consists of the first `j`
  rows of the matrix of products completed by rows of `1`; for `γ` of cell rank `j` these columns
  lie in the spans of both frames.
* `S.termLattice c c' γ`: the lattice `L_γ^M` of the `v ∈ Λ ∩ X₀` such that some vector of
  `v + M (Λ ∩ X)` is orthogonal to `γ f`, where `Λ` is the lattice of `c` and `X` is the isotropic
  space spanned by `e₁, …, e_ϱ`.
* `New.genIndex d`: the generalised index of an idele `d`, the inverse of the factor by which `d`
  scales Haar measure.


### `encard_le_of_encard_range_le`

 Colour the elements of `A` by `φ` with at most `N` colours, so that elements of one colour are
related by `R`. If every nonempty set of pairwise related elements of `A` has at most `x` elements,
then `A` has at most `N * x` elements. 

### `encard_le_of_colouring`

 Let `E` be a CM field with a primitive 5040-th root of unity. Let `K` and `K'` be modules of
vectors of finite adeles over the ring `Ô E` of integral finite adeles, with `K ∩ K'` of finite
index in `K'`. Attach to each element of `A` a family `f a`, indexed by `ι`, of vectors of `K'`. If
every nonempty subset of `A` whose families are congruent modulo `K` has at most `x` elements, then
`A` has at most `[K' : K ∩ K'] ^ card ι * x` elements. 

### `one_add_two_mul_pow_le_pow`

 For `b ≥ 3` we have `1 + 2 b ^ m ≤ b ^ m'` whenever `m < m'`. 

### `mem_besselU0_of_mem_classUnipotent₀`

 A move fixes the standard frame. 

### `mul_mem_termsOver_of_mem_classUnipotent₀`

 A move for the class `c` keeps the set of terms over `(c, s, c')`. 

### `HasCellRank.mul_of_mem_classUnipotent₀`

 A move keeps the cell rank of an element. 

### `IsFrameSet`

 A frame set for the class `c`: a set of near terms `(c', γ)` over blocks `(c, s, c')`, for any
`s`, whose frames are different modulo moves, the elements of the unipotent group of level `M`
that fix the standard frame. 

### `IsFrameSet.near`

 The terms are near. 

### `IsFrameSet.mem_termsOver`

 The terms lie over blocks with the first class `c`. 

### `IsFrameSet.separated`

 Terms whose frames agree after moves are equal. 

### `IsFrameSet.mono`

 A subset of a frame set is a frame set. 

### `IsFrameSet.isIntegral_frameProducts`

 The matrix of products of the standard frame with the frame of a term of a frame set has
integral entries. 

### `IsFrameSet.encard_range_frameProducts_le`

 Let `E` be a CM field, `S` admissible filling data over `E`, and `c` a class. Let `B` be a frame
set for `c`: near terms over blocks with the first class `c`, whose frames differ modulo moves, the
unipotent elements of level `M` that fix the standard frame. The terms of `B` have at most
`b ^ (270 n³ f)` matrices of products of the standard frame with their frame. Here `b = S.b` is the
size parameter of `S`, `n` is the length of the frame and `f` the number of infinite places. 

### `varrho_add_two_le_b_pow`

 There are `ϱ + 2` cell ranks, and `ϱ + 2 ≤ b ^ (2 f)` with `f` the number of infinite places. 

### `isIntegral_sharedVectors`

 Let `γ` be a term over the block `(c, s, c')`: a rational element such that `h_c⁻¹ γ h_c'`, for
the representatives of the classes `c` and `c'`, is integral with reduction `s`. The entries of its
matrix of shared vectors for the index `j` are algebraic integers. 

### `IsFrameSet.encard_range_sharedVectors_le`

 Let `B` be a frame set whose terms all have cell rank `j`: from the index `j` on, the flags of
the standard frame `f` and of the frame `γ f` share vectors, and the leading minor of order `j` of
their matrix of products is nonzero. Then there are at most `b ^ (366 n⁴ f')` matrices
`S.sharedVectors j γ`. Here `b = S.b` is the size parameter of `S`, `n = ϱ + 1` the length of the
frame and `f'` the number of infinite places. 

### `exists_frameImage_mul_eq_of_sub_mem`

 Let `γ` and `γ'` have the same integral matrix of products `Z` with nonzero leading minor of
order `j`, the same shared vectors and the same part in the anisotropic space `X₀`. Let `c`, `c'`,
`c''` be any three classes, with representatives `h_c`, `h_c'`, `h_c''`. If the first `ϱ` rows of
the frames of `h_c⁻¹ γ h_c'` and `h_c⁻¹ γ' h_c''` are congruent modulo `d = S.frameModulus j Z`,
then some `u ∈ S.classUnipotent₀ c`, a move for `c`, carries the frame of `γ` to the frame of
`γ'`. 

### `IsFrameSet.encard_le_of_sharedVectors_eq`

 Let `E` be a CM field with a primitive 5040-th root of unity and `S` admissible filling data
over `E`. Take near terms of cell rank `j` (from the index `j` on, the flags of the standard frame
and of the frame of the term share vectors, and the leading minor of order `j` of their matrix of
products is nonzero), with frames different modulo moves and one matrix of products `Z`. Let `Y` be
the first `j` rows of `Z` completed by rows of `1`. Suppose that the terms have the same matrix of
shared vectors (the coordinates in the isotropic space of the columns `k ≥ j` of `γ f · adj Y`,
which lie in the spans of both frames) and that their frames have one part in the anisotropic space
`X₀` after the moves `u`, unipotent elements of level `M` that fix the standard frame. Let
`d = M det (Y Yᴴ)`. Then there are at most `[d] ^ (n ϱ)` terms, where `[d]` is the generalised
index and `n = ϱ + 1`. 

### `IsFrameSet.encard_le_of_framePartX₀_eq`

 **The part in the isotropic space.** Let `E` be a CM field with a primitive 5040-th root of
unity and `S` admissible filling data over `E`. Let `B` be a frame set for the class `c`: near terms
whose frames differ modulo moves, the unipotent elements of level `M` that fix the standard frame.
Suppose the terms of `B` all have cell rank `j`: from the index `j` on, the flags of the standard
frame and of the frame of the term share vectors, and the leading minor of order `j` of their matrix
of products is nonzero. Suppose also that they all have the matrix of products `Z`. Finally, suppose
that after moves `u` in `S.classUnipotent₀ c` their frames all have one part in the anisotropic
space `X₀`. Then `B` has at most `b ^ (366 n⁴ f) · [d] ^ (n ϱ)` terms. Here `b = S.b`, `n = ϱ + 1`
is the length of the frame and `f` the number of infinite places. `[d]` is the generalised index of
`d = S.frameModulus j Z = M det(Y Yᴴ)`, where `Y` is the first `j` rows of `Z` completed by rows of
`1`. 

### `IsFrameSet.encard_le_of_conjTranspose_mul_eq`

 **The part in `X₀`, the anisotropic space.** Let `E` be a CM field with a primitive 5040-th root
of unity and `S` admissible filling data over `E`. Take near terms of cell rank `j`, with frames
different modulo moves and one matrix of products `Z`, whose leading minor of order `j` is `δ`.
Suppose that after the moves `u` the parts in `X₀` of the frames have the same products with the `r`
independent columns of `y`, and `r + l = k`, the rank of `X₀`. Then there are at most
`[d] ^ (l n) · b ^ (366 n⁴ f) · [d'] ^ (n ϱ)` terms, where `d = M δ`, `d' = S.frameModulus j Z`,
`[·]` is the generalised index, `b = S.b`, `n = ϱ + 1` the length of the frame and `f` the number of
infinite places. 

### `IsFrameSet.encard_le_of_le_termLattice`

 **Lifts of `L`.** Let `E` be a CM field with a primitive 5040-th root of unity and `S`
admissible filling data over `E`. Take near terms `γ` of cell rank `j`, with frames different modulo
moves and one matrix of products `Z`, whose lattices `L_γ^M` contain the lattice `L ⊆ Λ ∩ X₀` of
corank `l` with the basis `y a`. Let `d` be `M` times the leading minor of order `j` of `Z`, and
`d' = S.frameModulus j Z`. Then there are at most `disc(L) ^ (2 ϱ) · [d] ^ (l n) · b ^ (366 n⁴
f) · [d'] ^ (n ϱ)` terms. Here `[d] = genIndex d` is the inverse of the factor by which `d` scales
Haar measure, `disc(L)` is the square root of the generalised index of the Gram determinant of a
basis of `L`, `b = S.b`, `n = ϱ + 1` and `f` is the number of infinite places. 

### `IsFrameSet.encard_le_of_frameProducts_eq`

 The terms of a frame set with one cell rank `j` and one matrix of products `Z`, whose lattices
`L_γ^M` contain a lattice `L` of corank `l` and discriminant at most `b ^ (n³ f)`, number at most
`b ^ ((366 n⁴ + 2 n³ (ϱ + l n + n ϱ)) f)`; here `n = ϱ + 1` is the length of the frame and `f` the
number of infinite places. 

### `IsFrameSet.encard_le`

 **Frames over a lattice.** Let `L ⊆ Λ ∩ X₀` be a lattice of corank `l` and discriminant at most
`b ^ (n³ f)`, and `B` a frame set for the class `c`: near terms `(c', γ)` with `γ` over some block
`(c, s, c')` (that is, `h_c⁻¹ γ h_c'` is integral with reduction `s`), whose frames are different
modulo moves. Suppose that each term has a cell rank `j` and that `L ⊆ L_γ^M`. Then `B` has at most
`b ^ (2000 n⁶ (l + 1) f)` elements. Here `L_γ^M` is the lattice of the `v ∈ Λ ∩ X₀` such that some
vector of `v + M (Λ ∩ X)` is orthogonal to the frame of `γ`, where `Λ` is the lattice of `c`, `X`
the isotropic and `X₀` the anisotropic space; `b = S.b` is the size parameter, `n` the length of the
frame and `f` the number of infinite places. 

### `encard_setOf_isNearTermAt_and_le_termLattice_le`

 Let `E` be a CM field with a primitive 5040-th root of unity and `S` admissible filling data
over `E`, of level `M = p₀ p₁` (`S.M`) and size parameter `b = S.b`. Let `Λ` be the lattice of the
class `c`, `X₀` the anisotropic space (of dimension `𝔰.k`), `X` the isotropic space, `n` the length
of the frame and `f` the number of infinite places. Let `L ⊆ Λ ∩ X₀` be a lattice of rank `r`, with
`r + l = 𝔰.k`, and discriminant at most `b ^ (n³ f)`. Then at most `b ^ (2000 n⁶ (l + 1) f)` pairs
`p = (c', γ)` with `S.IsNearTermAt c t p` have `L ⊆ S.termLattice c c' γ`. The condition
`S.IsNearTermAt c t p` says three things. First, `γ` is a near term from `c'` to `c` and is the
representative picked in its double coset. Second, `γ` has some cell rank `j`: from the index `j`
on, the flags of the standard frame and of `γ`'s frame share vectors, and the leading minor of order
`j` of their matrix of products is nonzero. Third, `γ` has label `t`, the position of its reduction
in its coset of `S.reducedImage besselS`, the image in `S.ResidueGL` of the integral points of the
Bessel group. 
