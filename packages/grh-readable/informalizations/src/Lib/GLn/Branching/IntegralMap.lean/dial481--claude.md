---
{
  "module": "src/Lib/GLn/Branching/IntegralMap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/Branching/IntegralMap.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/Branching/IntegralMap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Branching from GL(n+1) to GL(n) × GL(1): integral equivariant branching maps

This file constructs the integral branching map from `GL(n + 1)` to `GL(n) × GL(1)` from its
value at one point, proves its norm bound, and shows that it spans the maps that are equivariant
for the unitary block group. Vectors are coordinates indexed by `New.WeylIndexFamily n κ`
(standard fillings), and `New.schur κ z` is the matrix of `z` in these coordinates. `New.weylRep κ
e` is its twist by `det ^ e` on invertible matrices, `New.weylNormSq` is the squared norm for the
Gram matrix, and `New.GL.blockScalar ι g s` is the matrix `diag(g, s)`.

## Main definitions and results

* `New.SpansBranchingMaps`: a matrix spans the maps that are equivariant for the unitary block
  group.
* `New.GL.exists_int_branching_of_weylKernel`: an integral equivariant matrix from its value at one
  point.
* `New.exists_branching_matrix`: the branching map, its norm bound and its uniqueness.

Notions from other files:
* `New.rankAt`: The number of elements of the finite row type n_τ at the place τ;
  `New.GL.rowEquivFin n τ : n τ ≃ Fin (rankAt n τ)` is the fixed numbering of these rows, and a
  row's position is its number.
* `New.permArray`: For maps e_τ from rows to natural numbers, the array over R whose entry at row
  (τ,a), column i is 1 if e_τ(a)=i and 0 otherwise.
* `New.toPoly`: The linear map from coordinate vectors ξ to polynomials, ξ ↦ Σ_i (Gξ)_i b_i, with G
  the Gram matrix `New.weylGram` (`New.weylGramOver` is its image over another ring) and b_i the
  basis `New.nablaBasis` of products of minors; `New.GL.nablaCombination` is ξ ↦ Σ_i ξ_i b_i.
* `New.weylEval`: For an array y, the evaluation vector `ev_y` with entries b_i(y); its polynomial
  under `New.toPoly` is `New.weylKernel n κ y`.
* `New.GL.branchVector`: the product of the leading minors to the powers `γ` with the new row first
  and to the powers `κ'` with the new row last.

## Relation to the literature

Branching from GL(n+1) to GL(n) with multiplicity one. Here the branching map is given for one
interlacing pair as an integer matrix that is equivariant over every field of characteristic 0 and
satisfies an explicit norm bound, and every unitarily equivariant map is a multiple of it. That it
is non-zero is not part of the statement. Source: Goodman, Wallach 2009, Theorem 8.1.1;
Zhelobenko, Compact Lie Groups and their Representations, 1973, ch. X; Molev, Gelfand-Tsetlin bases
for classical Lie algebras, arXiv math/0211289.


### `_root_.New.SpansBranchingMaps`

 `New.SpansBranchingMaps ι e₀ e A` says that `A` spans the complex maps that are equivariant for
the unitary points of the block group: let `T` be a complex matrix such that, for every tuple `g`
of unitary matrices (`(g τ)ᴴ * g τ = 1`), some `x` with blocks `x τ = diag(g τ, 1)` along `ι`
satisfies `T * ρ_{κ,e}(x) = ρ_{κ₀,e₀}(g) * T`; then `T` is a multiple of `A`. Here `ρ_{κ,e}` is
`New.weylRep κ e`, the Schur matrix times the powers `e τ` of the determinants, and
`New.GL.blockScalar ι g 1` is the block matrix `diag(g τ, 1)`. 

### `exists_cyclic_lower_triangular`

 There is a complex vector `v` whose images `schur κ (diag(g, 1)) *ᵥ v`, for `g` ranging over
tuples of lower triangular matrices on the rows `n τ`, span the whole space: a row vector `r`
killing all of them is zero. Here `schur κ` is the Schur matrix, acting on the vectors indexed by
`WeylIndexFamily N κ`, `diag(g, 1)` is `blockScalar ι g 1`, and "lower triangular" is written
`(g τ)ᵀ.BlockTriangular (rowEquivFin n τ)` for the fixed numbering `rowEquivFin n τ` of the rows.

This cyclic vector gives multiplicity at most one in the branching rule from GL (n + 1) to GL n
(`New.GL.spansBranchingMaps_of_equivariant`). 

### `branchKernel`

 The kernel of the branching map: for arrays `x` (rows `n`) and `y` (rows `N`) over a commutative
ring `S`, the value of `branchVector S ι γ κ'` at `diag(xᵀ, 1) y`, where `xᵀ` is the transposed
square part of `x` in the row order `rowEquivFin`. 

### `detPowToPoly`

 The linear map `θ ↦ toPoly n κ₀ θ * detPow S n d` with `d τ = κ' τ (rankAt n τ)`: the
polynomial of the coordinate vector `θ` times the powers `d τ` of the determinants. 

### `map_branchKernel`

 A ring homomorphism `φ` commutes with `branchKernel`: it sends the kernel at `x` and `y` to
the kernel at `φ ∘ x` and `φ ∘ y`. 

### `branchKernel_borelMul`

 In `y`, `branchKernel` is a semi-invariant of the upper triangular group: replacing `y` by
`borelMul Sigma.fst b y` multiplies it by the diagonal entries of `b` to the powers given by the
weights of `γ` and `κ'`. 

### `branchKernel_blockScalar`

 Let `y'` be the array `diag(g, s) y` and `x'` the array `gᵀ x`. The kernel at `x` and `y'` is
the kernel at `x'` and `y` times the product of the powers
`s τ ^ diagramWeight (rankAt N) γ (τ, 0)`. 

### `detPowToPoly_smul_schur_mulVec`

 Up to the factor `∏ τ, det (g τ) ^ κ' τ (rankAt n τ)`, the Schur matrix of `g` acts on
`detPowToPoly n κ₀ κ' S θ` as the substitution `x ↦ gᵀ x`. 

### `exists_eval_detPowToPoly_eq_mul_branchKernel`

 Let `c` times the product of the two kernels in `hη` be `toPoly n κ₀ η`, and let `y` have new
row `(t, 0, 0, …)` and block `g` on the rows `n τ`. Expanding the minors along the new row,
`branchKernel ι γ κ' x y` is a power of `t` times the product of those two kernels and of
`det ^ d`, with `d τ = κ' τ (rankAt n τ)`, all at `gᵀ x`. So `c` times it is `detPowToPoly` of
a coordinate vector: `η` moved by `g` and scaled. 

### `exists_int_branching_of_weylKernel`

 Let `c • (weylKernel n γ₁ P₁ * weylKernel n κ' P) = toPoly n κ₀ η` for an integer `c` and an
integer vector `η`, where `γ₁ τ h = γ τ (h + 1)`, `P` is the permutation array of the row order
`rowEquivFin` and `P₁` that of `rowEquivFin` shifted cyclically by one. (`New.weylKernel` is the
product of the leading minors to the powers given by the weight; `New.toPoly n κ₀` sends a
coordinate vector to its polynomial.) Then there is an integral matrix `B` with two properties. (a)
Applied on the right to `weylGramOver *ᵥ weylEval n κ₀ P`, the coordinates of `weylKernel n κ₀ P`,
it gives a vector ξ whose polynomial `nablaCombination (γ + κ')` ξ = Σ ξ_i b_i (b_i the basis minor
products) is `c • branchVector ℂ ι γ κ'`; the latter is the product of leading h×h minors to the
powers γ τ h with the added row first and κ' τ h with it last. (b) Over every field of
characteristic zero, `B * schur (γ + κ') (diag(g, s)) = χ • (schur κ₀ g * B)` with `χ = ∏ τ, s τ ^
diagramWeight (rankAt N) γ (τ, 0) * det (g τ) ^ κ' τ (rankAt n τ)`. Here `schur` is the Schur matrix
on the Weyl module and `diag(g, s)` is `blockScalar ι g s`. 

### `spansBranchingMaps_of_equivariant`

 Let `v` be the Gram matrix `weylGramOver` times the evaluation vector at the permutation array
of `rowEquivFin`. Let `B` be an integral matrix such that `nablaCombination` (ξ ↦ Σ ξ_i b_i over the
basis products of minors) sends the row vector `v ᵥ* B` to `c • branchVector ℂ ι γ κ'` with `c ≠ 0`.
Here `branchVector` is the product of the leading minors to the powers `γ`, with the added row
first, and of those to the powers `κ'`, with the added row last. Let `B` also be equivariant over
`ℂ`: `B * schur (γ + κ') (diag(g, 1)) = (∏ τ, det (g τ) ^ κ' τ (rankAt n τ)) • (schur κ₀ g * B)`
for all `g`, where `diag(g, 1)` is `blockScalar ι g 1`. If `e₀ τ = e τ + κ' τ (rankAt n τ)`, then
every complex matrix intertwining weights `(γ + κ', e)` and `(κ₀, e₀)` on the unitary points of the
block group is a multiple of `B` (`New.SpansBranchingMaps`). 

### `_root_.New.exists_branching_matrix`

 Branching from `GL (n + 1)` to `GL n`. Write `κ = γ + κ'`: of the `κ τ h` columns of height `h`,
`γ τ h` lose a box and `κ' τ h` keep theirs, and `κ₀ τ h = κ' τ h + γ τ (h + 1)` for
`0 < h < rankAt n τ`. Columns of height `rankAt n τ` that keep their box become powers of `det`:
`e₀ τ = e τ + κ' τ (rankAt n τ)`. Let all columns of height below `q` lose a box. Write
`ρ = weylRep κ e` and `ρ₀ = weylRep κ₀ e₀`. Then some integral matrix `br` has three properties. (a)
Over every field of characteristic zero, `br ρ(diag(g, s)) = (∏ τ, s τ ^ (diagramWeight (rankAt N) γ
(τ, 0) + e τ)) ρ₀(g) br`. (b) Its operator norm for the Gram norms is at most `L ^ (3 L)` if `L`
bounds the number of boxes of `κ₀` in columns of height `h` with `q ≤ h < rankAt n τ`; the bound is
stated for squared norms. (c) It spans the maps over `ℂ` that are equivariant for the unitary block
group.

Part of the multiplicity-one branching rule from GL (n + 1) to GL n: for a given interlacing pair,
an integral equivariant matrix exists and the multiplicity is at most one. 
