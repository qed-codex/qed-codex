---
{
  "module": "src/New/Appendix/DiscreteSeries/StationaryPosition.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/StationaryPosition.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/StationaryPosition.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The stationary position

For weights `μ` and `μ'` on opposite sides of `0`, with alternating signs on each side, there is a
position `(v, i₀)` in which `μ` moves each vector `v_j` to `v_{j + 1}` for `j < j₀`, where
`j₀ = d + 1` is the number of vectors, and `i₀` compresses `μ` to `μ'`
(`IsSteep.exists_isStationary`). The weight `μ` is realized as multiplication by `t` on
polynomials, and the form as a sum of residues.

Throughout, `p = nodal univ μ` and `q = nodal univ μ'` are the monic polynomials with the roots
`μ i` and `μ' j`, and `q_j = nodal (univ.erase j) μ'` is `q / (t - μ' j)`. The roots are indexed
from `0`, the vectors `v₁, …, v_{j₀}` from `1`. The vector `polyVec μ μ' F` is written `[F]`, and
`alternatingSignForm x y` is written `⟨x, y⟩`.

Notions from other files:

* `l.lowestKType`: the highest weight of the lowest `K`-type for the doubled Harish-Chandra
  parameter `l = 2 λ : HCParam ε`, a vector of integers; `intDiagonal` turns it into a diagonal
  matrix.
* `IsSteep l B e`: on `X` the signs `ε` are `+1` and that weight is `0`; on `Fin L` the signs
  are `+, -, …` and the weight decreases strictly in `[-3 B, -B]`.
* `IsPosition ε η d v i₀`: the ranks differ by `2 d + 1`, the columns of `v` are independent, their
  products vanish except that the last column has norm `±1`, and `i₀` is an isometry into their
  orthogonal complement.
* `signMatrix ε` is the diagonal matrix of the signs `ε`, and `formAdjoint ε η A` is the adjoint
  `A†` for the hermitian forms with the signs `ε` and `η`.


### `AreOppositeNodes`

 The reals `μ 0 > μ 1 > …`, the roots of `p = nodal univ μ`, lie below the reals
`μ' 0 < μ' 1 < …`, the roots of `q = nodal univ μ'`. 

### `AreOppositeNodes.strictAnti`

 The roots of `p` decrease. 

### `AreOppositeNodes.strictMono`

 The roots of `q` increase. 

### `AreOppositeNodes.lt`

 Each root of `p` is below each root of `q`. 

### `polyVec`

 The vector `[F]` of a real polynomial `F`, with the coordinates
`F (μ i) |p' (μ i) q (μ i)| ^ (-1 / 2)`, where `p` and `q` are the monic polynomials with the roots
`μ i` and `μ' j`. 

### `isometryScale`

 The factor `|p (μ' j) / q' (μ' j)| ^ (1 / 2)`, where `p` and `q` are the monic polynomials with
the roots `μ i` and `μ' j`. It is chosen to normalize the vector `[q / (t - μ' j)]`. 

### `alternatingSignForm`

 The bilinear form `x₀ y₀ - x₁ y₁ + …` with the alternating signs `+, -, …` on real vectors. 

### `eval_nodal_eq_mul_erase`

 The value of `∏ k, (t - μ' k)` at `a` is `a - μ' j` times the value of the product over
`k ≠ j`. 

### `mul_polyVec_erase`

 Let `q = nodal univ μ'` and `q_j = q / (t - μ' j)`, and write `[F] = polyVec μ μ' F`. Then
`μ [q_j] = μ' j [q_j] + [q]` entrywise, since `t q_j = μ' j q_j + q`. 

### `neg_one_pow_mul_eval_nodal_pos`

 As each `μ i` lies below the `L'` roots of `q = ∏ (t - μ' j)`, the number `q (μ i)` has the
sign `(-1) ^ L'`. 

### `eval_nodal_pos`

 If each `μ i` lies below each `μ' j`, then `nodal univ μ = ∏ i, (t - μ i)` takes a positive
value at each `μ' j`. 

### `polyVec_nodal_ne_zero`

 For opposite nodes no entry of the vector `[q] = polyVec μ μ' q` of `q = ∏ (t - μ' j)` is zero:
it is `q (μ i)` divided by `|p' (μ i) q (μ i)| ^ (1 / 2)`, where `p = ∏ (t - μ i)`. 

### `alternatingSignForm_polyVec`

 Let the decreasing reals `μ i`, the roots of `p = nodal univ μ`, lie below the `L'` increasing
roots `μ' j` of `q = nodal univ μ'`. Here `polyVec μ μ' F` is the vector with the entries
`F (μ i) |p' (μ i) q (μ i)| ^ (-1 / 2)`, and `alternatingSignForm x y` is the alternating sum
`∑ i, (-1) ^ i x i y i`. For the vectors of `F₁` and `F₂` it is `(-1) ^ L'` times the sum of the
residues of `F₁ F₂ / (p q)` at the roots of `p`. 

### `alternatingSignForm_polyVec_X_pow_mul`

 Let the decreasing roots `μ i` of `p = nodal univ μ` lie below the `L'` increasing roots `μ' j`
of `q = nodal univ μ'`. Here `polyVec μ μ' G` is the vector with the entries
`G (μ i) |p' (μ i) q (μ i)| ^ (-1 / 2)`, and `alternatingSignForm x y` is the alternating sum
`∑ i, (-1) ^ i x i y i`. For the vectors of `F` and `t ^ a q` it is `(-1) ^ L'` times the sum of
the residues of `t ^ a F / p`. 

### `alternatingSignForm_polyVec_X_pow_mul_X_pow_mul`

 Let the `L` decreasing roots `μ i` of `p = nodal univ μ` lie below the `L'` increasing roots
`μ' j` of `q = nodal univ μ'`, where `L = L' + 2 d + 1`. Here `polyVec μ μ' F` is the vector with
the entries `F (μ i) |p' (μ i) q (μ i)| ^ (-1 / 2)`, and `alternatingSignForm x y` is the
alternating sum `∑ i, (-1) ^ i x i y i`. For the vectors of `t ^ a q` and `t ^ b q` with
`a + b ≤ 2 d` it is `(-1) ^ L'` if `a + b = 2 d` and `0` otherwise. 

### `alternatingSignForm_polyVec_erase_X_pow_mul`

 Let the `L` decreasing roots `μ i` of `p = nodal univ μ` lie below the `L'` increasing roots
`μ' j` of `q = nodal univ μ'`, where `L = L' + 2 d + 1`, and let `q_j = q / (t - μ' j)`. Here
`polyVec μ μ' F` is the vector with the entries `F (μ i) |p' (μ i) q (μ i)| ^ (-1 / 2)`, and
`alternatingSignForm x y` is the alternating sum `∑ i, (-1) ^ i x i y i`. For the vectors of `q_j`
and `t ^ a q` with `a ≤ 2 d` it is `0`: the residues of `t ^ a q_j / p` add up to `0`, as the
numerator has degree below `L - 1`. 

### `alternatingSignForm_polyVec_nodal_erase`

 Let the `L` decreasing roots `μ i` of `p = nodal univ μ` lie below the `L'` increasing roots
`μ' j` of `q = nodal univ μ'`, where `L = L' + 2 d + 1`, and let `q_j = q / (t - μ' j)`. Here
`polyVec μ μ' F` is the vector with the entries `F (μ i) |p' (μ i) q (μ i)| ^ (-1 / 2)`, and
`alternatingSignForm x y` is the alternating sum `∑ i, (-1) ^ i x i y i`. For the vectors of `q_j`
and `q_j'` it is `0` if `j ≠ j'`, and `(-1) ^ (L' + 1) q' (μ' j) / p (μ' j)` if `j = j'`: the
quotient `q_j / ((t - μ' j') p)` has a pole besides the roots of `p` only when `j = j'`. 

### `isometryScale_mul_alternatingSignForm`

 Let the `L` decreasing roots `μ i` of `p = nodal univ μ` lie below the `L'` increasing roots
`μ' j` of `q = nodal univ μ'`, where `L = L' + 2 d + 1`, and let `q_j = q / (t - μ' j)`. The vectors
of the `q_j`, each scaled by `isometryScale μ μ' j = |p (μ' j) / q' (μ' j)| ^ (1 / 2)`, are
orthogonal for `alternatingSignForm`, and the vector of index `j` has the norm `(-1) ^ j`. 

### `AreSeparatedNodes`

 Any two of the reals `μ i` and `μ' j`, the roots of `p = nodal univ μ` and `q = nodal univ μ'`,
differ by at least `1`, and each `μ i` is within `D ≥ 1` of `0` and of every `μ' j`. 

### `AreSeparatedNodes.one_le`

 The bound is at least `1`. 

### `AreSeparatedNodes.pairwise_left`

 Two roots of `p` differ by at least `1`. 

### `AreSeparatedNodes.pairwise_right`

 Two roots of `q` differ by at least `1`. 

### `AreSeparatedNodes.one_le_abs_sub`

 A root of `p` and a root of `q` differ by at least `1`. 

### `AreSeparatedNodes.abs_sub_le`

 A root of `p` and a root of `q` differ by at most `D`. 

### `AreSeparatedNodes.abs_le`

 The roots of `p` have modulus at most `D`. 

### `one_le_abs_derivative_nodal`

 If the roots `μ i` of `p = ∏ (t - μ i)` differ by at least `1`, then `|p' (μ i)| ≥ 1`, as
`p' (μ i)` is the product of the differences `μ i - μ j` over `j ≠ i`. 

### `abs_eval_nodal_le`

 If `a` is within `D ≥ 1` of each of the `L` nodes `μ i`, the value at `a` of
`nodal s μ = ∏ i ∈ s, (t - μ i)` has modulus at most `D ^ L`. 

### `polyVec_sq_le`

 Let `AreSeparatedNodes μ μ' D` hold: any two of the reals `μ i` and `μ' j` differ by at least
`1`, and each `μ i` is within `D ≥ 1` of `0` and of every `μ' j`. Let `p = nodal univ μ` and
`q = nodal univ μ'`. If `|G (μ i)| ≤ |q (μ i)|`, the square of the entry
`F (μ i) G (μ i) |p' (μ i) q (μ i)| ^ (-1 / 2)` of `polyVec μ μ' (F * G)` is at most
`F (μ i) ^ 2 |G (μ i)|`, as `|p' (μ i)| ≥ 1`. 

### `abs_polyVec_le`

 Let the roots `μ i` of `p = nodal univ μ` and `μ' j` of `q = nodal univ μ'` differ by at least
`1`, with each `μ i` within `D ≥ 1` of `0` and of the `μ' j`, and let `L = L' + 2 d + 1`. For
`a ≤ 2 d` the entry `(μ i) ^ a q (μ i) |p' (μ i) q (μ i)| ^ (-1 / 2)` of the vector
`polyVec μ μ' (X ^ a * q)` has modulus at most `D ^ a |q (μ i)| ^ (1 / 2) ≤ D ^ L`. 

### `abs_isometryScale_mul_le`

 Let the roots `μ i` of `p` and `μ' j` of `q` differ by at least `1`, with each `μ i` within
`D ≥ 1` of `0` and of the `μ' j`, and let `L = L' + 2 d + 1` and `q_j = q / (t - μ' j)`. The entry
`q_j (μ i) |p' (μ i) q (μ i)| ^ (-1 / 2)` of the vector `polyVec` of `q_j`, multiplied by
`isometryScale μ μ' j = |p (μ' j) / q' (μ' j)| ^ (1 / 2)`, has modulus at most
`|p (μ' j) q_j (μ i)| ^ (1 / 2) ≤ D ^ L`. 

### `positionVec`

 The matrix with the columns `v_{a + 1} = [t ^ a q]`, `a ≤ d`, where `q = nodal univ μ'` and
`[F] = polyVec μ μ' F`: through `e : X ⊕ Fin L ≃ n` the column has these coordinates on `Fin L` and
vanishes on `X`. 

### `positionIsometry`

 The matrix `i₀` that, through `e` and `e'`, is `1` on `ℂ^X` and sends the `j`th of the other
basis vectors to the vector `[q_j]`, where `q_j = nodal (univ.erase j) μ'` and
`[F] = polyVec μ μ' F`, scaled by `isometryScale μ μ' j`. 

### `positionVec_apply_inl`

 The columns of `positionVec e μ μ' d` vanish on the coordinates in `X`. 

### `positionVec_apply_inr`

 At the coordinate `e (Sum.inr i)`, the column of index `a` of `positionVec e μ μ' d` equals the
`i`th entry of the real vector `polyVec μ μ' (X ^ a * q)`, where `q = nodal univ μ'`. 

### `positionIsometry_apply_inl`

 The matrix `i₀ = positionIsometry e e' μ μ'` is the identity on `ℂ^X`: its column of index
`e' (Sum.inl x)` is the basis vector of index `e (Sum.inl x)`. 

### `positionIsometry_apply_inl_inr`

 For `j : Fin L'`, the column of index `e' (Sum.inr j)` of `positionIsometry e e' μ μ'` vanishes
on the coordinates `e (Sum.inl x)` with `x` in `X`. 

### `positionIsometry_apply_inr_inr`

 For `i : Fin L` and `j : Fin L'`, the entry of `positionIsometry e e' μ μ'` at
`(e (Sum.inr i), e' (Sum.inr j))` is `isometryScale μ μ' j` times the `i`th coordinate of
`polyVec μ μ' (nodal (univ.erase j) μ')`. 

### `AreSeparatedNodes.norm_positionVec_le`

 Let the nodes differ by at least `1`, with each `μ i` within `D ≥ 1` of `0` and of the `μ' j`,
and let `L = L' + 2 d + 1`. The columns `[t ^ a q]`, `a ≤ d`, of `positionVec` have entries of norm
at most `D ^ L`. 

### `AreSeparatedNodes.norm_positionIsometry_le`

 Let the nodes differ by at least `1`, with each `μ i` within `D ≥ 1` of `0` and of the `μ' j`,
and let `L = L' + 2 d + 1`. The matrix `positionIsometry`, which is `1` on `ℂ^X` and has the scaled
vectors `[q_j]` as its other columns, has entries of norm at most `D ^ L`. 

### `IsSteep.conjTranspose_mul_signMatrix_mul_apply`

 If `l` is steep, so that the signs `ε` are `+1` on `X` and alternate on `Fin L`, the hermitian
form with the matrix `signMatrix ε = diag ε`, taken on a column of `A` and a column of `A'`, is the
standard form on the coordinates in `X` plus the alternating form on the others. 

### `IsSteep.conjTranspose_mul_signMatrix_mul_apply_of_real`

 Let `l` be steep, so that through `e : X ⊕ Fin L ≃ n` the signs `ε` are `+1` on `X` and
`+, -, …` on `Fin L`. Let the column `a` of `A` vanish on `X` and have the real coordinates `f i`
on `Fin L`, and let the column `b` of `A'` have the real coordinates `g i` on `Fin L`. Then the
hermitian form with the matrix `signMatrix ε = diag ε` takes on the two columns the value
`alternatingSignForm f g = ∑ i, (-1) ^ i f i g i`. 

### `AreOppositeNodes.linearIndependent_positionVec`

 If the nodes are opposite and `d < L`, the columns of `positionVec e μ μ' d` are linearly
independent over `ℂ`. 

### `IsSteep.gram_positionVec`

 Let `l` be steep, so that the signs `ε` are `+1` on `X` and `+, -, …` on `Fin L`, let the
decreasing nodes `μ` lie below the increasing nodes `μ'`, and let `L = L' + 2 d + 1`. For the form
with the matrix `signMatrix ε = diag ε`, the products of the vectors `[t ^ a q]`, `a ≤ d`, vanish,
except that `[t ^ d q]` has the norm `(-1) ^ L'`. 

### `IsSteep.gram_positionIsometry_inr`

 If `l` is steep, the nodes are opposite and `L = L' + 2 d + 1`, the columns outside `X` of
`positionIsometry`, which are the scaled `[q_j] = polyVec μ μ' (q / (t - μ' j))`, are orthogonal
with the norms `+1, -1, …` for the form with the matrix `signMatrix ε`. 

### `IsSteep.isPosition`

 Let `l` be steep with respect to `B` and `e` (`IsSteep l B e`): the signs `ε` are `+1` on `X`,
where the weight of the lowest `K`-type is `0`, and `+, -, …` on `Fin L`, where that weight
decreases strictly in `[-3 B, -B]`. Let the signs `η` be `+1` on `X` and `+, -, …` on `Fin L'`,
where `L = L' + 2 d + 1`. Let the decreasing nodes `μ`, the roots of the monic polynomial `p`, lie
below the increasing nodes `μ'`, the roots of the monic polynomial `q`. For a polynomial `F` let
`[F] = polyVec μ μ' F` be the real vector with the entries `F (μ i) |p' (μ i) q (μ i)| ^ (-1 / 2)`.
The columns of `positionVec` are the vectors `[t ^ a q]`, `a ≤ d`, extended by `0` on `X`. The
matrix `i₀ = positionIsometry e e' μ μ'` is `1` on `ℂ^X`, and its column of index `e' (Sum.inr j)`
is `|p (μ' j) / q' (μ' j)| ^ (1 / 2)` times `[q / (t - μ' j)]`. These form a position of `U(η)` in
`U(ε)`: the ranks differ by `2 d + 1`, the vectors are independent with vanishing products except
that the last has norm `±1`, and `i₀` is an isometry into their orthogonal complement. 

### `intDiagonal_mul_positionVec`

 If the weight of the lowest `K`-type of `l` (`l.lowestKType`) is `μ` on `Fin L`, its diagonal
matrix `intDiagonal l.lowestKType` sends each of the first `d` columns `v_{a + 1} = [t ^ a q]` of
`positionVec` to the next column, as `μ [F] = [t F]`; `initCols` keeps these first `d` columns. 

### `AreSeparatedNodes.norm_pow_mulVec_positionVec_le`

 Let the nodes differ by at least `1`, with each `μ i` within `D ≥ 1` of `0` and of the `μ' j`,
let `L = L' + 2 d + 1`, and let the weight of the lowest `K`-type of `l`, acting as a diagonal
matrix, be `μ` on `Fin L`. The first column `v₁` of `positionVec` is `0` on `X` and has the entries
`q (μ i) |p' (μ i) q (μ i)| ^ (-1 / 2)` on `Fin L`. Then for `a ≤ 2 d` the entries of the `a`th
power of the diagonal matrix applied to `v₁`, which are those of `v₁` times `(μ i) ^ a`, have
modulus at most `D ^ L`. 

### `exists_intDiagonal_mul_positionIsometry`

 Let `l` and `k` be Harish-Chandra parameters, each stored as twice its value, and let the
weights of their lowest `K`-types vanish on `X` and be `μ` and `μ'` on the other coordinates; the
weights act as diagonal matrices. The columns `v₁, …, v_{d + 1}` of `positionVec` are the vectors
`[t ^ a q]`, `a ≤ d`, extended by `0` on `X`, and `i₀ = positionIsometry e e' μ μ'` is `1` on `ℂ^X`
and has multiples of the vectors `[q_j]` as its other columns. Then `μ i₀ = i₀ μ'` modulo the span
of the `v_a`, as `μ [q_j] = μ' j [q_j] + v₁`. 

### `IsPosition.formAdjoint_mul_mul_eq`

 In a position `(v, i₀)` of `U(η)` in `U(ε)`, if `M i₀ = i₀ M'` modulo the span of the columns of
`v`, then `i₀† M i₀ = M'`. 

### `IsSteep.exists_isStationary`

 **The stationary position.** Let `l` be steep for `(X, L, B)` with `B ≥ 1`: on `X` the signs `ε`
are `+1` and the weight `μ` of its lowest `K`-type is `0`, and on the other `L` coordinates the
signs are `+, -, …` and `μ` decreases strictly in `[-3 B, -B]`. Let the weight `μ'` of the lowest
`K`-type of `k` vanish on `X`, where the signs `η` are `+1`, and increase strictly in `[0, B']` on
the other `L'` coordinates, where the signs are `+, -, …`. Let `B' ≥ 0` and `L = L' + 2 d + 1`. Then
there is a stationary position `(v, i₀)` with `j₀ = d + 1` vectors. Moreover `v_{j₀}` has the norm
`(-1) ^ L'`, and the entries of the `v_j`, of `i₀` and of `μ ^ a v₁` for `a ≤ 2 d` have modulus at
most `(3 B + B') ^ L`. 
