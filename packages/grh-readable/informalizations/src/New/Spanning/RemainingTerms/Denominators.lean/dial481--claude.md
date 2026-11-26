---
{
  "module": "src/New/Spanning/RemainingTerms/Denominators.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Denominators.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Denominators.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Denominators: bases of `A⁺ / I_γ` and `γ A⁺ / I_γ`

Let `γ` be a rational point of the unitary group that has the cell rank `j`. This file gives bases
of `A⁺ / I_γ` and `γ A⁺ / I_γ`: the first `j` vectors of the frame with `z_N`, and their images
under `γ`. The basis of `γ A⁺ / I_γ` is proved from the cell rank alone; the basis of `A⁺ / I_γ` is
proved when `E` contains a primitive `5040`-th root of unity (`HasPrimitiveRoot5040 E`). Under the
same hypothesis the determinant `New.Filling.subframeMinor` of the products of the two lists is not
zero (`New.Filling.HasCellRank.subframeMinor_ne_zero`); so the two quotients pair perfectly.

Here `n = ϱ + 1` and `N = S.N` is the prime of the data `S`. The basis vectors `e_1, …, e_{n-1}`
span the isotropic space `A`, the basis vector `z_N` has the product `-N` with itself, and
`A⁺ = A + E z_N` is the span of the frame `e_• = (e_1, …, e_{n-1}, z_N)`, which the code indexes
from `0`. The rank of `A / I_γ` is `min j (n - 1)`.

* `New.Filling.HasCellRank.linearIndependent_mkQ_frameImage_one_and_sup_eq`,
  `New.Filling.HasCellRank.linearIndependent_mkQ_frameImage_coe_and_sup_eq`: the two bases modulo
  `I_γ`; `New.Filling.HasCellRank.linearIndependent_mkQ_frameImage_and_sup_eq` states both.

Notions from other files:
* `frameImage M` is the matrix whose columns are the frame `M e_•`, and `colSpan` is the span of the
  columns, so `A⁺ = colSpan (frameImage 1)`.
* `commonIsotropic γ` is the space `I_γ = A ∩ γ A`.
* `subframeIndices j` is the set of indices of the first `j` vectors of `e_•` and of `z_N`.
* `S.frameProducts γ` is the matrix of the hermitian products (Gram matrix `S.ratGram`) of `e_•`
  with `γ e_•`, and `δ_j` is its leading minor of order `j`.
* `S.HasCellRank j γ` says: for one `ζ` with `ζ ζ̄ = 1` and every index `l ≥ j`, the flags of `e_•`
  and `γ e_•` share a vector with leading coefficients `ζ` and `1` at `l`; `δ_j ≠ 0`; and `j = n`
  exactly when `𝗀 = S.termDisc γ = |δ_n|² - N² |δ_{n-1}|²` is nonzero.


### `mulVec_eq_submatrix_mulVec_of_eq_zero_off`

 A combination of the columns of `F` whose coefficients vanish outside `s` is a combination of
the columns with indices in `s`. 

### `linearIndependent_mkQ_col_and_colSpan_sup_eq`

 Let `I` lie in the column space of `F`. Suppose that no nonzero combination of the columns with
indices in `s` lies in `I`, and that any coefficients outside `s` occur in a combination of all
columns that lies in `I`. Then the columns with indices in `s` are a basis of the column space
modulo `I`. 

### `HasCellRank.frameProducts_mulVec_eq_zero_of_shared`

 Let `γ` have the cell rank `j`: at every index `l ≥ j` (counted from `0`) the flags of the frame
`e_• = (e_1, …, e_ϱ, z_N)` and of `γ e_•` share a vector with leading coefficients `ζ` and `1` (one
`ζ` with `ζ ζ̄ = 1`), the leading minor of order `j` of the matrix `S.frameProducts γ` of their
products is nonzero, and `j = ϱ + 1` exactly when `S.termDisc γ ≠ 0`. Then a vector with
coefficients `x` in `e_•` (the columns of `frameImage 1`) and `y` in `γ e_•` is orthogonal to the
first `j` vectors of `e_•`; its products with `e_•` are the entries of `S.frameProducts γ *ᵥ y`. 

### `HasCellRank.eq_zero_of_frameProducts_mulVec_eq_zero`

 Let `γ` have the cell rank `j`: at every index `l ≥ j` (counted from `0`) the flags of the frame
`e_• = (e_1, …, e_ϱ, z_N)` and of `γ e_•` share a vector with leading coefficients `ζ` and `1` (one
`ζ` with `ζ ζ̄ = 1`), the leading minor of order `j` of the matrix `S.frameProducts γ` is nonzero,
and `j = ϱ + 1` exactly when `S.termDisc γ ≠ 0`. The entries of `S.frameProducts γ` are the products
of `e_•` (rows) with `γ e_•` (columns) in the hermitian form with Gram matrix `S.ratGram`. Let `y`
vanish at every index `≥ j`, and let the combination of `γ e_•` with coefficients `y` be orthogonal
to the first `j` vectors of `e_•`. Then `y = 0`. 

 ### The subframe of the first `j` vectors and `z_N` 

### `HasCellRank.eq_zero_of_mem_commonIsotropic`

 Let `γ` have the cell rank `j`: at every index `l ≥ j` (counted from `0`) the flags of the frame
`e_• = (e_1, …, e_ϱ, z_N)` and of `γ e_•` share a vector with leading coefficients `ζ` and `1` (one
`ζ` with `ζ ζ̄ = 1`), the leading minor of order `j` of the matrix `S.frameProducts γ` of their
products is nonzero, and `j = ϱ + 1` exactly when `S.termDisc γ ≠ 0`. Then no nonzero combination of
the first `j` vectors of `γ e_•` (the columns of `frameImage γ`) and its last vector `γ z_N`, whose
indices form `subframeIndices j`, lies in `commonIsotropic γ = A ∩ γ A`, where
`A = ⟨e_1, …, e_ϱ⟩`. 

### `HasCellRank.exists_mem_commonIsotropic`

 Let `γ` have the cell rank `j`: at every index `l ≥ j` (counted from `0`) the flags of the frame
`e_• = (e_1, …, e_ϱ, z_N)` and of `γ e_•` share a vector with leading coefficients `ζ` and `1` (one
`ζ` with `ζ ζ̄ = 1`), the leading minor of order `j` of the matrix `S.frameProducts γ` of their
products is nonzero, and `j = ϱ + 1` exactly when `S.termDisc γ ≠ 0`. Here `S.termDisc γ` is
`|δ_{ϱ+1}|² - N² |δ_ϱ|²`, where `δ_i` is the leading minor of order `i` of `S.frameProducts γ` and
`N = S.N`. Put `A = ⟨e_1, …, e_ϱ⟩`, `A_{≤j} = ⟨e_1, …, e_j⟩` and
`I_γ = commonIsotropic γ = A ∩ γ A`. Let `M` be a square matrix of the size of `γ` such that, if
`S.termDisc γ` vanishes, `M A = M A_{≤j} + I_γ`; both `1` and `γ` are such. Then any coefficients
`x a` at the indices `j ≤ a < ϱ` (those outside `subframeIndices j`) occur in a combination of the
frame `M e_•` (the columns of `frameImage M`) that lies in `I_γ`. 

### `frameImage_one_mulVec_mem_commonIsotropic_iff`

 Let `e_• = (e_1, …, e_ϱ, z_N)` be the frame, let `A = ⟨e_1, …, e_ϱ⟩`, write
`I_γ = commonIsotropic γ = A ∩ γ A`, and recall that `frameImage M` is the matrix with columns
`M e_•`. The combination of `e_•` with coefficients `x` lies in `I_γ` exactly when the combination
of `γ⁻¹ e_•` with the same coefficients lies in `I_{γ⁻¹}`, as `γ⁻¹` carries the one to the
other. 

### `HasCellRank.linearIndependent_mkQ_frameImage_coe_and_sup_eq`

 Let `γ` have the cell rank `j`: at every index `l ≥ j` (counted from `0`) the flags of the frame
`e_• = (e_1, …, e_ϱ, z_N)` and of `γ e_•` share a vector with leading coefficients `ζ` and `1` (one
`ζ` with `ζ ζ̄ = 1`), the leading minor of order `j` of the matrix `S.frameProducts γ` of their
products is nonzero, and `j = ϱ + 1` exactly when `S.termDisc γ ≠ 0`. Then the first `j` vectors of
`γ e_•` (the columns of `frameImage γ`) and its last vector `γ z_N`, whose indices form
`subframeIndices j`, are a basis of `γ A⁺ / I_γ`. Here `γ A⁺` is the span of `γ e_•` and
`I_γ = commonIsotropic γ = A ∩ γ A`, where `A = ⟨e_1, …, e_ϱ⟩`. 

### `HasCellRank.linearIndependent_mkQ_frameImage_one_and_sup_eq`

 Let `γ` have the cell rank `j`: at every index `l ≥ j` (counted from `0`) the flags of the frame
`e_• = (e_1, …, e_ϱ, z_N)` and of `γ e_•` share a vector with leading coefficients `ζ` and `1` (one
`ζ` with `ζ ζ̄ = 1`), the leading minor of order `j` of the matrix `S.frameProducts γ` of their
products is nonzero, and `j = ϱ + 1` exactly when `S.termDisc γ ≠ 0`. If `E` contains a primitive
`5040`-th root of unity, the first `j` vectors of `e_•` (the columns of `frameImage 1`) and its last
vector `z_N`, whose indices form `subframeIndices j`, are a basis of `A⁺ / I_γ`. Here `A⁺` is the
span of `e_•`, `A = ⟨e_1, …, e_ϱ⟩` and `I_γ = commonIsotropic γ = A ∩ γ A`. 

### `HasCellRank.linearIndependent_mkQ_frameImage_and_sup_eq`

 Let `γ` have the cell rank `j`: at every index `l ≥ j` (counted from `0`) the flags of the frame
`e_• = (e_1, …, e_ϱ, z_N)` and of `γ e_•` share a vector with leading coefficients `ζ` and `1` (one
`ζ` with `ζ ζ̄ = 1`), the leading minor of order `j` of the matrix `S.frameProducts γ` of their
products is nonzero, and `j = ϱ + 1` exactly when `S.termDisc γ ≠ 0`. Let `E` contain a primitive
`5040`-th root of unity, let `A⁺` be the span of `e_•` (the columns of `frameImage 1`) and
`I_γ = commonIsotropic γ = A ∩ γ A`, where `A = ⟨e_1, …, e_ϱ⟩`. Then the subframe of the first `j`
vectors of `e_•` and `z_N` (indices `subframeIndices j`) is a basis of `A⁺ / I_γ`, and its image
under `γ` (columns of `frameImage γ`) is a basis of `γ A⁺ / I_γ`. 
