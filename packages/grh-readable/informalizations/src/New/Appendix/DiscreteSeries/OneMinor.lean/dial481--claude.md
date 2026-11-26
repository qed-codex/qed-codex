---
{
  "module": "src/New/Appendix/DiscreteSeries/OneMinor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/OneMinor.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/OneMinor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One minor near the identity

Estimates for one principal minor `det_S`, in terms of the blocks that cross the set `S` of indices,
that is, the entries `(i, j)` with exactly one of `i`, `j` in `S`: its size on a unitary matrix
(`norm_principalMinor_sq_le_exp`), and its form on `kᴴ ĝ k` for `k` unitary and block diagonal and
`ĝ = reducedExp ε o Z` for a small `Z` in the Lie algebra of `U(J)`, with `o` injective and
`o i < o j` whenever `i ∈ S` and `j ∉ S` (`exists_principalMinor_conj_reducedExp_eq_cexp`): up to an
error, `exp (tr P Z + ‖[P, Z]‖² / 4)`, where `P` is the projection to `S` and `‖[P, Z]‖` is the norm
of the two blocks of `Z` that cross `S`. A third estimate for one minor is
`exists_det_one_add_proj_mul_eq_exp` in `New.Appendix.DiscreteSeries.MinorSecondOrder`.

The matrix `ĝ` differs from `exp Z` by unipotent factors. Block diagonal triangular factors multiply
Flensted-Jensen's coefficient by a character of their diagonal if the matrices involved are
accretive (`flenstedJensen_triangular_mul_mul_triangular`), so for small `Z` the coefficient is the
same at `ĝ` and at `exp Z` (`flenstedJensen_reducedExp`).

All norms of matrices are Frobenius norms, and `ε : n → ℤˣ` is a vector of signs. Notation:
* `principalMinor X p`, `coordProj p`: the principal minor `det_S X` and the diagonal projection for
  the set `S` of indices satisfying `p`.
* `blockDiagAlg ε`: the matrices that vanish at `(i, j)` whenever `ε i ≠ ε j`.
* `lowerMask ε o Z`: the matrix that keeps the entries `(i, j)` of `Z` with `o j < o i` and
  `ε i = ε j`.

## Relation to the literature

See `New.Appendix.DiscreteSeries.Periods` for related work.


 ### The size of one minor 

### `norm_det_sq_le_exp`

 The square of `|det Y|` is at most `exp (tr (Yᴴ Y - 1))`; this trace is real. 

### `principalMinor_eq_det_coordProj`

 The principal minor of `X` on the indices satisfying `p` is `det (1 + P (X - 1))`, where `P` is
the diagonal projection to these indices. 

### `conjTranspose_mul_self_one_sub_mul_mul`

 For a unitary matrix `k` and an orthogonal projection `P`, the crossing block
`M = (1 - P) k P` satisfies `Mᴴ M = P - P kᴴ P k P`. 

### `norm_lie_sq_of_unitary`

 For a unitary matrix `k` and an orthogonal projection `P`, the Frobenius norms of the
commutator and of the block `(1 - P) k P` satisfy `‖[P, k]‖² = 2 ‖(1 - P) k P‖²`. 

### `norm_principalMinor_sq_le_exp`

 Size of one minor: let `k` be a unitary matrix, `S` the set of indices satisfying `p`, and
`P = coordProj p` the diagonal projection to `S`. Then the principal minor of `k` on `S` satisfies
`|det_S k|² ≤ exp (-‖[P, k]‖² / 2)`. 

 ### Unipotent factors 

### `exp_apply_eq_one_apply_of_le`

 Let the integer vector `o` order the indices, and let the matrix `u` be strictly lower
triangular for this order, that is, its entry `(i, j)` vanishes whenever `o i ≤ o j`. Then at these
positions the entry of `exp u` is the entry of the identity matrix. In particular, the diagonal
entries of `exp u` are `1`. 

### `exp_neg_lowerMask_apply_of_le`

 The entry `(i, j)` of `exp (-u)` with `o i ≤ o j` is that of the identity matrix, where
`u = lowerMask ε o Z` keeps the entries `(i, j)` of `Z` with `ε i = ε j` and `o j < o i`. 

### `exp_neg_lowerMask_mem_blockDiagAlg`

 The matrix `exp (-u)` is block diagonal for the signs `ε`, where `u = lowerMask ε o Z` keeps
the entries `(i, j)` of `Z` with `ε i = ε j` and `o j < o i`. 

### `isBorelMatrix_exp_neg_lowerMask`

 The matrix `exp (-u)` is invertible and lower triangular for the order `o`
(`IsBorelMatrix (-o)`), where `u = lowerMask ε o Z` keeps the entries `(i, j)` of `Z` with
`ε i = ε j` and `o j < o i`. 

### `diagChar_exp_neg_lowerMask`

 The product `diagChar w (exp (-u)) = ∏ i, exp (-u) i i ^ w i` over the diagonal entries of
`exp (-u)` is `1`, where `u = lowerMask ε o Z` keeps the entries `(i, j)` of `Z` with `ε i = ε j`
and `o j < o i`. 

### `reducedExp`

 The matrix `ĝ = exp (-u) exp Z exp (-v)`, where `u = lowerMask ε (-o) Z` and
`v = lowerMask ε o Z` are the strictly lower and strictly upper triangular parts, in the order of
decreasing `o`, of the block diagonal (compact) part of `Z` for the signs `ε`. 

### `det_reducedExp`

 Let `ĝ = reducedExp ε o Z = exp (-u) exp Z exp (-v)`, where `u = lowerMask ε (-o) Z` and
`v = lowerMask ε o Z` keep the entries of `Z` at equal signs that are strictly triangular in the
one or the other direction for the order `o`. Then `det ĝ = exp (tr Z)`, as `u` and `v` have trace
`0`. 

### `norm_mul_sub_one_le`

 If `X` and `Y` are within `ρ` and `σ` of the identity in the Frobenius norm, then their product
is within `ρ σ + ρ + σ` of it. 

### `flenstedJensen_reducedExp`

 Let `ε` be a vector of signs; a matrix is block diagonal if its entry `(i, j)` vanishes whenever
`ε i ≠ ε j`. Let the integer vector `l = 2λ : HCParam ε` be a doubled Harish-Chandra parameter of
gap `h`: its entries are distinct and congruent to `card n - 1` mod 2, and `|λ i - λ j| ≥ h`
whenever `ε i ≠ ε j`. Let `Z` have Frobenius norm at most `1 / 20`. Flensted-Jensen's coefficient
`l.flenstedJensen 1 z` is the integral of `|m_Λ k|² / m_{-λ-ρ} (kᴴ z k)` over the group `K` of
unitary block diagonal matrices `k`, divided by the integral of `|m_Λ k|²`. Here `m_w` is the
product of principal minors `weightMinors w`, `Λ` is the highest weight of the lowest `K`-type, `ρ`
is the half sum of the roots positive for `l`, and the argument `1` is the matrix `g` in the general
numerator `m_Λ (g k) conj (m_Λ k)`. This coefficient takes the same value at `z = exp Z` and at
`z = reducedExp ε l Z = exp (-u) exp Z exp (-v)`. Here `u = lowerMask ε (-l) Z` keeps the entries
`(i, j)` of `Z` with `ε i = ε j` and `l i < l j`, and `v = lowerMask ε l Z` keeps those with
`ε i = ε j` and `l j < l i`. 

### `norm_apply_le`

 The absolute value of an entry of a matrix is at most the Frobenius norm of the matrix. 

### `norm_lie_coordProj_apply`

 The entry `(i, j)` of the commutator of `X` with the diagonal projection to the indices
satisfying `p` has the norm of `X i j` if exactly one of `p i`, `p j` holds, else it is `0`. 

### `lie_coordProj_entryMask`

 Keeping only the entries `(i, j)` with `r i j`, by `entryMask r`, commutes with taking the
commutator with the diagonal projection `coordProj p`. 

### `norm_conj_sub_eq`

 Conjugation by a unitary matrix `k` moves an orthogonal projection `P` by `‖[P, k]‖`. 

### `norm_lie_le_add`

 Let `A`, `P`, `Q` be complex square matrices, with the Frobenius norm. If `‖A‖ ≤ δ`, the norm of
the commutator `[P, A]` grows by at most `2 δ ‖Q - P‖` when `Q` replaces `P`. 

### `sum_norm_conj_coordProj_sub_le`

 Let `k` be a unitary matrix and let `P = coordProj p` be the diagonal projection to the indices
satisfying `p`. The absolute values of the diagonal entries of `k P kᴴ - P` have sum at most
`‖[P, k]‖²`, the squared Frobenius norm of the commutator. 

### `norm_trace_conj_coordProj_mul_sub_le`

 Let `o` be injective, let `k` be unitary and block diagonal for the signs `ε`, and let
`‖Z‖ ≤ δ` in the Frobenius norm. Let `P = coordProj p` be the diagonal projection to the indices
satisfying `p`, and let `u = lowerMask ε (-o) Z` and `v = lowerMask ε o Z` be the two strictly
triangular parts of `Z` inside the blocks of `ε`. Then the trace of `k P kᴴ (-u + Z - v)` differs
from the trace of `P Z` by at most `δ ‖[P, k]‖²`. 

### `norm_mul_proj_le`

 Multiplication on the right by an orthogonal projection does not increase the Frobenius
norm. 

### `norm_cross_le`

 The block `P A (1 - P)` of a matrix `A`, which maps the kernel of an orthogonal projection `P`
to its range, has Frobenius norm at most that of the commutator `[P, A] = P A - A P`. 

### `norm_cross_sub_le`

 For an orthogonal projection `P`, consider the block `P A (1 - P)` of a matrix `A`, which maps
the kernel of `P` to its range. If `‖A‖ ≤ δ` in the Frobenius norm, then these blocks for two
orthogonal projections `P` and `Q` differ in Frobenius norm by at most `2 δ ‖Q - P‖`. 

### `norm_crossTrace_sub_le`

 Let `P` and `Q` be orthogonal projections and let `A` and `B` be matrices with `‖A‖, ‖B‖ ≤ δ`
and `‖[P, A]‖, ‖[Q, B]‖ ≤ ζ`. Then `crossTrace Q A B = tr (Q A (1 - Q) B)` differs from
`crossTrace P A B` by at most `4 δ ‖Q - P‖ ζ`. 

### `norm_crossTraceSum_sub_le`

 Let `P` and `Q` be orthogonal projections, and let `A₁`, `A₂`, `A₃` be matrices of Frobenius
norm at most `δ` whose commutators with `P` and with `Q` have Frobenius norm at most `ζ`. Then
`crossTraceSum Q A₁ A₂ A₃`, the sum of `tr (Q Aᵢ (1 - Q) Aⱼ)` over `i ≤ j` with the terms `i = j`
halved, differs from `crossTraceSum P A₁ A₂ A₃` by at most `18 δ ‖Q - P‖ ζ`, with `‖Q - P‖` the
Frobenius norm. 

### `crossTrace_coordProj`

 For the coordinate projection `P` onto the indices satisfying `p`, the trace
`crossTrace P A B = tr (P A (1 - P) B)` is the sum of `A i j * B j i` over `i` inside and `j`
outside the set. 

### `norm_lie_coordProj_neg_lowerMask_le`

 Let `P` be the coordinate projection onto the indices satisfying `p`. Passing from `Z` to
`-lowerMask ε o Z`, minus its strictly triangular part for the order `o` inside the blocks of `ε`,
does not increase the Frobenius norm of the commutator with `P`. 

### `apply_of_mem_unitaryLie`

 Let `Z` lie in the Lie algebra of `U(J)`, where `J` is the diagonal matrix of the signs `ε`.
Then `Z` is skew-Hermitian on the entries at equal signs (the compact part) and Hermitian on the
entries at opposite signs (the noncompact part). 

### `norm_lie_coordProj_sq_of_mem_unitaryLie`

 Let `Z` lie in the Lie algebra of `U(J)`, that is, `Zᴴ J + J Z = 0`, where `J = signMatrix ε` is
the diagonal matrix of the signs `ε`. Let `P = coordProj p` be the diagonal projection to the set
`S` of indices satisfying `p`. Then the squared Frobenius norm `‖[P, Z]‖²` of the commutator is
twice the sum of `|Z j i|²` over `i` in `S` and `j` outside `S`, because `|Z i j| = |Z j i|`. 

### `crossTraceSum_coordProj_eq`

 Let `P = coordProj p` be the diagonal projection to the indices satisfying `p`, on which `o` is
smaller than on the other indices, and let `Z` lie in the Lie algebra of `U(J)`, where
`J = signMatrix ε` is the diagonal matrix of the signs `ε`. Let `(A₁, A₂, A₃) = (-u, Z, -v)`, where
`u = lowerMask ε (-o) Z` and `v = lowerMask ε o Z` are the two strictly triangular parts of `Z`
inside the blocks of `ε`. Then `crossTraceSum P A₁ A₂ A₃`, the sum of `tr (P Aᵢ (1 - P) Aⱼ)` over
`i ≤ j` with the terms `i = j` halved, is a quarter of the squared Frobenius norm of the
commutator `[P, Z]`. 

### `principalMinor_conj_eq_det`

 For a unitary matrix `k`, the principal minor of `kᴴ X k` on the indices satisfying `p` is
`det (1 + k P kᴴ (X - 1))`, where `P` is the coordinate projection onto these indices. 

### `mul_sq_add_add_le_mul_sq_add_sq`

 For `δ, κ, ζ ≥ 0` and `ζ ≤ x + κ`, the error terms of
`exists_principalMinor_conj_reducedExp_eq_cexp` satisfy `δ κ² + 18 δ κ ζ + 10⁴ δ ζ² ≤ 10⁵ δ (x² +
κ²)`. 

### `exists_principalMinor_conj_reducedExp_eq_cexp`

 Let `o` be injective, let `S` be the set of indices satisfying `p`, on which `o` is smaller than
on the other indices, and let `P = coordProj p` be the coordinate projection onto `S`. Let `Z` lie
in the Lie algebra of `U(J)`, where `J = signMatrix ε` is the diagonal matrix of the signs `ε`, with
`‖Z‖ ≤ δ ≤ 1 / 20`, and let `k` be unitary and block diagonal for the signs `ε`. Then the principal
minor on `S` of `kᴴ ĝ k`, where `ĝ = reducedExp ε o Z = exp (-u) exp Z exp (-v)` for the two
strictly triangular parts `u`, `v` of `Z` inside the blocks of `ε`, is
`exp (tr (P Z) + ‖[P, Z]‖² / 4 + r)` with `‖r‖ ≤ 10⁵ δ (‖[P, Z]‖² + ‖[P, k]‖²)`. 
