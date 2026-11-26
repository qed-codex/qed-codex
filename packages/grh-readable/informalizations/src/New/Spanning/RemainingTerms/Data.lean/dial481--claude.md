---
{
  "module": "src/New/Spanning/RemainingTerms/Data.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Data.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Data.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The data of a term and of a pair of terms

The lattice `L_γ` of a term, the common lattice `L₁₂` of two terms, the gauge `𝗀*` with the factor
due to the level, the size of a term, and the terms and pairs that are counted.

We write `X₀` for the definite hermitian space with coordinates `𝔰.κ`, and `z` for the vector that
spans the rest of the middle part.

Here a term is a rational element `γ`, taken with two classes `c` and `c'`, `A` is the span of
`e₁, …, e_ϱ`, `Λ` is the lattice of the class `c`, `M = S.M` is the level and `f` is the number of
infinite places. A term in the cell `j` has `rk A / (A ∩ γ A) = min ϱ j`.

Notions from other files:
* `S.classCoordX₀ c`: the matrix of a basis of `X₀` in the coordinates of `Λ`; it is orthonormal
  for the Gram matrix `S.latticeMiddle` of the middle part of `Λ`.
* `S.translateByClassReps c c' γ`: the adelic element `h_c⁻¹ γ h_c'`, where `h_c` represents `c`.
* `S.HasCellRank j γ`: `γ` lies in the cell `j ≤ ϱ + 1`; there is at most one such `j`.
* `New.link γ`: the pairs of middle coordinates (in `X₀ ⊕ E z`) of `t` and `γ⁻¹ t`, for `t`
  orthogonal to `A` and `γ A`. `New.commonLink γ γ'`: the vectors `x` of `X₀` such that some pair
  `(x, y)` lies in both links, with `x` and `y` orthogonal to `z`.
* `S.maxGauge j c c' γ`: the larger of the gauge `𝗀♯` and `Nm 𝗀`, for a term in the cell `j`.


### `classLatticeX₀`

 The lattice `Λ ∩ X₀` of the class `c`, in rational coordinates: the vectors that
`S.classCoordX₀ c` sends to integral vectors. 

### `termLattice`

 The lattice `L_γ` of a term: the vectors `v` of `Λ ∩ X₀` such that some vector of
`v + M (Λ ∩ A)` is orthogonal to the frame of `γ`, taken in the lattice coordinates of `c` and `c'`
(the frame of `S.translateByClassReps c c' γ`). The condition says that the products of `v` with
this frame are `M` times the products of some vector of `Λ ∩ A` with it. 

### `commonPart`

 The part of the lattice `L_γ` of the term `γ` in `commonLink γ γ'`, the vectors of `X₀` that
are the first entry of a pair, orthogonal to `z`, lying in both links. 

### `pairLattice`

 The common lattice `L₁₂` of two terms: the part of `L_γ ∩ L_γ'` in `commonLink γ γ'`, the
vectors of `X₀` that are the first entry of a pair, orthogonal to `z`, lying in both links. 

### `pairDiscriminant`

 The discriminant of the common lattice `L₁₂` of two terms, a lattice in `commonLink γ γ'`. 

### `linkCorank`

 The corank `c⁺` of two links: the codimension of their intersection in each of them, a link
having the dimension `k + 1`. 

### `levelGauge`

 The gauge `𝗀*` of a term in the cell `j`: `S.maxGauge` times the factor `M ^ (2 j' f)`,
`j' = min ϱ j`, that is due to the congruence level `M`. Here `f` is the number of infinite
places. 

### `discriminantBound`

 The bound `b ^ (n³ f)` for the gauges of near terms and for the discriminants of the pairs
that are counted, where `f` is the number of infinite places. 

### `cellRank`

 The cell rank of a rational element: the index `j` with `S.HasCellRank j γ`, or an unspecified
index if there is none. For an element with a cell rank, `min ϱ (cellRank γ)` is the rank of
`A / (A ∩ γ A)`. 

### `IsNearRepresentativeAtCellRank`

 The term is near, is the chosen element of its orbit `U⁰_c γ U⁰_c'`, where
`U⁰_c = S.classUnipotent₀ c`, and has a cell rank. 

### `IsNearPairOverAgreeingBlock`

 Two near representatives over one block `(c, s, c')` (see `S.termsOver`) whose `s` agrees (see
`S.Agrees`). 

### `termSize`

 The size of a term: `S.orbitBound` at the cell rank and the gauge `S.maxGauge` of the term. 

### `nearRepresentativesOver`

 The near representatives of `T` over the block `(c, s, c')`, that is, with `h_c⁻¹ γ h_c'`
integral and of reduction `s`; there are none unless `s` agrees. 

### `HasCellRank.hasCellRank_cellRank`

 If the rational element `γ` lies in some cell `j` (`S.HasCellRank j γ`:
`New.NormOnePairOccursFrom` `j` holds, the leading minor `D_j` of `S.frameProducts γ` is nonzero,
and `S.termDisc γ ≠ 0` exactly for `j = ϱ + 1`), then it lies in the cell of the index
`S.cellRank γ` chosen among these `j`. 

### `HasCellRank.cellRank_eq`

 If the rational element `γ` lies in the cell `j` (`S.HasCellRank j γ`), then the index
`S.cellRank γ`, chosen among all cells that contain `γ`, is `j`, as there is at most one. 

### `isIntMatrix_conjTranspose_mul_of_classCoordX₀`

 Vectors of `Λ ∩ X₀`, for the lattice `Λ` of the class `c` in the definite space `X₀`, have
integral products. Here `S.classCoordX₀ c` changes from an orthonormal basis of `X₀` to the
coordinates of `Λ`, and integral means with entries in the ring `Ô E` of integral elements of the
finite adeles `𝔸f E`. 

### `one_le_latticeDisc`

 For a subspace `V` of the definite space `X₀` and the lattice `Λ` of the class `c`, the real
number `S.latticeDisc c V` is at least `1`. It is the square root of the generalised index
(`New.genIndex`) of the Gram determinant of a basis of `Λ ∩ V` over `Ô E`: for an integral
determinant this is the square root of the norm of the ideal that it generates, which is at least
`1`. 
