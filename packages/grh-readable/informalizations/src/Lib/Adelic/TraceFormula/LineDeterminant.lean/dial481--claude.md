---
{
  "module": "src/Lib/Adelic/TraceFormula/LineDeterminant.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/LineDeterminant.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/LineDeterminant.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Traces on the range of an idempotent from traces of a raising operator

Let `T⁺`, `T⁻` be adjoint operators on a finite-dimensional inner product space with
`T⁺ * T⁻ = d • (1 + c • e)`, where `d, c > 0`, `e` is idempotent and `A` commutes with `T⁺` and
`T⁻`. The traces of the `A ^ l * T⁺ ^ i`, `l, i ≥ 1`, determine the trace of `A` on the range of `e`
(`LineRelation.trace_mul_mean_eq`): on the generalised eigenspace of `A` for each non-zero
eigenvalue they give the eigenvalues of `T⁺`, hence the dimension and
`|det T⁺| ^ 2 = d ^ dim * (1 + c) ^ rank e`.

The first section collects what traces determine on generalised eigenspaces; in particular the
traces of all powers of an operator determine its characteristic polynomial
(`charpoly_eq_of_trace_pow_eq`).


### `restrictGenEigenspace`

 For an operator `T` that commutes with `A`, the restriction of `T` to the generalised
eigenspace of `A` for `μ`. 

### `restrictGenEigenspace_pow`

 Restriction to a generalised eigenspace of `A` commutes with taking powers. 

### `trace_restrictGenEigenspace_mul`

 If `T` commutes with `A`, then on the generalised eigenspace of `A` for `μ` the trace of
`A * T` is `μ` times the trace of `T`, because `A - μ` is nilpotent there and commutes with `T`. 

### `trace_restrictGenEigenspace_pow_mul`

 If `T` commutes with `A`, then on the generalised eigenspace of `A` for `μ` the trace of
`A ^ l * T` is `μ ^ l` times the trace of `T`. 

### `trace_pow_mul_eq_sum`

 Let `T` commute with `A` and let the finite set `S` contain all eigenvalues of `A`. Then the
trace of `A ^ l * T` is the sum over `μ ∈ S` of `μ ^ l` times the trace of `T` on the generalised
eigenspace of `A` for `μ`. 

### `eq_of_sum_pow_mul_eq`

 The sequences `l ↦ μ ^ l`, `μ : ℂ`, are linearly independent: two combinations of them that
agree for all `l` have the same coefficients. 

### `exists_finset_maxGenEigenspace_eq_bot`

 Given operators `A` and `A'` and a number `μ`, there is a finite set that contains `μ` and all
eigenvalues of `A` and of `A'`. 

### `trace_restrictGenEigenspace_eq`

 Let `T` commute with `A` and `T'` with `A'`. If the traces of `A ^ l * T` and `A' ^ l * T'`
agree for all `l`, then so do the traces of `T` and `T'` on the generalised eigenspaces of `A`
and `A'` for each `μ`. 

### `trace_restrictGenEigenspace_eq_of_ne_zero`

 Let `T` commute with `A` and `T'` with `A'`. If the traces of `A ^ (l + 1) * T` and
`A' ^ (l + 1) * T'` agree for all `l`, then so do the traces of `T` and `T'` on the generalised
eigenspaces of `A` and `A'` for each non-zero `μ`. 

### `trace_restrictGenEigenspace_one`

 The trace of the identity on a generalised eigenspace is the dimension of that space. 

### `charpoly_eq_of_finrank_maxGenEigenspace_eq`

 Operators whose generalised eigenspaces have the same dimensions for every `μ` have the same
characteristic polynomial, as these dimensions are the multiplicities of its roots. 

### `charpoly_eq_of_trace_pow_eq`

 Operators `A` and `A'` with the same traces of all powers have the same characteristic
polynomial. 

### `charpoly_eq_of_trace_pow_succ_eq`

 Two invertible operators with the same traces of all positive powers have the same
characteristic polynomial. 

### `det_one_add_smul_of_isIdempotentElem`

 For an idempotent `e`, the determinant of `1 + c e` is `(1 + c) ^ rank e`. 

### `LineRelation`

 The line relations among operators `T⁺ = Tp`, `T⁻ = Tm`, `e` and `A`: `T⁻` is the adjoint of
`T⁺`, `e` is idempotent, `T⁺ T⁻ = d (1 + c e)` with `c, d > 0`, and `A` commutes with `T⁺` and
`T⁻`. They are meant for the stabiliser of a line in `GL_n(𝒪)`, `𝒪` a local ring with residue
field of order `q`: there `e` is the mean over `GL_n(𝒪)` (whence `mean` in the names of the
lemmas), `d = q ^ (n - 2)` and `c = q ^ n - 1`. 

### `LineRelation.d_pos`

 The constant `d` is positive. 

### `LineRelation.c_pos`

 The constant `c` is positive. 

### `LineRelation.idem`

 `e` is idempotent. 

### `LineRelation.adjoint`

 `T⁻` is the adjoint of `T⁺`. 

### `LineRelation.mul_eq`

 `T⁺ T⁻ = d (1 + c e)`. 

### `LineRelation.commute_plus`

 `A` commutes with `T⁺`. 

### `LineRelation.commute_minus`

 `A` commutes with `T⁻`. 

### `commute_mean`

 Under the line relations, `A` commutes with `e`, which is a polynomial in `T⁺ T⁻`. 

### `mapsTo_mean`

 Under the line relations, a subspace that is stable under `T⁺` and `T⁻` is stable under `e`,
as `e` is a linear combination of `T⁺ T⁻` and the identity. 

### `restrict`

 The line relations (`T⁺`, `T⁻` adjoint, `T⁺ T⁻ = d (1 + c e)`, `A` commuting with both) pass
to a subspace that is stable under `A`, `T⁺` and `T⁻`. 

### `restrict_maxGenEigenspace`

 The line relations (`T⁺`, `T⁻` adjoint, `T⁺ T⁻ = d (1 + c e)`, `A` commuting with both) hold
for the restrictions of `A`, `T⁺`, `T⁻` and `e` to the generalised eigenspace of `A` for `α`. 

### `norm_det_sq`

 For operators with `T⁻` adjoint to `T⁺` and `T⁺ T⁻ = d (1 + c e)`, `e` idempotent, one has
`|det T⁺| ^ 2 = det (T⁺ T⁻) = d ^ dim B * (1 + c) ^ rank e`. 

### `finrank_range_eq_of_charpoly_eq`

 Let `A, T⁺, T⁻, e` and `A', T⁺', T⁻', e'` satisfy the line relations (`T⁺`, `T⁻` adjoint,
`T⁺ T⁻ = d (1 + c e)`) for the same `c, d > 0`. If `T⁺` and `T⁺'` have the same characteristic
polynomial, then `e` and `e'` have the same rank: the polynomial gives the dimension and
`det T⁺`, hence the rank. 

### `finrank_range_restrictGenEigenspace_eq`

 Let `A, T⁺, T⁻, e` and `A', T⁺', T⁻', e'` satisfy the line relations (`T⁺`, `T⁻` adjoint,
`T⁺ T⁻ = d (1 + c e)`, `A` commuting with both) for the same `c, d > 0`. If the traces of
`A ^ (l + 1) * T⁺ ^ (i + 1)` and `A' ^ (l + 1) * T⁺' ^ (i + 1)` agree for all `l, i`, then for
each non-zero `α` the idempotents `e` and `e'` have the same rank on the generalised eigenspaces
of `A` and `A'` for `α`. 

### `trace_mul_mean_eq`

 Let `A, T⁺, T⁻, e` and `A', T⁺', T⁻', e'` satisfy the line relations (`T⁺`, `T⁻` adjoint,
`T⁺ T⁻ = d (1 + c e)`, `A` commuting with both) for the same `c, d > 0`. If the traces of
`A ^ (l + 1) * T⁺ ^ (i + 1)` and `A' ^ (l + 1) * T⁺' ^ (i + 1)` agree for all `l, i`, then so do
the traces of `A * e` and `A' * e'`, which are those of `A` and `A'` on the ranges of `e` and
`e'`. 
