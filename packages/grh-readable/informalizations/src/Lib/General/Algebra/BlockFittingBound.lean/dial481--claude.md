---
{
  "module": "src/Lib/General/Algebra/BlockFittingBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/BlockFittingBound.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/BlockFittingBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A matrix of relations with small block determinant valuation

Linear algebra over a discrete valuation ring O (written `DVR O`) with normalized valuation
v = `addVal O` and fraction field K. The valuation of a determinant of relations is bounded by the
length of a module of solutions, taken modulo an element p or in K/O.

* `New.Selmer.exists_rows_addVal_det_le`: let ψ : A → M_d(O) be onto, N an A-submodule of A^ι, p ≠ 0
  and b < v(p). If the vectors modulo p killed by ψ(N) lie in a module of length at most b, then
  some square matrix B with rows in N has v(det ψ(B)) ≤ b, with ψ(B) read as a block matrix.
* `New.Selmer.divQuot`: the map x ↦ x/p from O/p to K/O (`New.Selmer.DivisibleQuot`). For p ≠ 0 it
  is injective with image the p-torsion.
* `New.Selmer.exists_rows_addVal_det_le_of_divisible`: the same bound when the vectors with entries
  in K/O killed by ψ(N) lie in a module of length at most b. It follows from the form modulo p and
  is the form that Ribet's lemma uses.

The idea: as ψ is onto, any d linear forms in the span of the rows of the ψ(t), t ∈ N, are the rows
of one ψ(t). So a basis of this span, divided into groups of d forms, gives B. The length of the
solutions bounds the determinant of such a basis by the duality lemma
`New.exists_matrix_addVal_det_le_length` for lattices in O^n.

## Relation to the literature

General linear algebra over a discrete valuation ring (elementary divisors).


### `New.Selmer.exists_rows_addVal_det_le`

 Let O be a discrete valuation ring (`DVR O`) with normalized valuation v = `addVal O`, let
ψ : A → M_d(O) be onto, N an A-submodule of A^ι, p ≠ 0 and b < v(p). Write `QuotSpan p` for O/p,
on whose vectors indexed by d the matrices act by multiplication. If all w in ((O/p)^d)^ι with
∑ j, ψ(t j) • w_j = 0 for every t ∈ N lie in a submodule Z of length at most b, then some square
matrix B with rows in N has v(det ψ(B)) ≤ b, where ψ(B) is read as a block matrix. 

### `DivisibleQuot`

 The divisible module K/O, where K = Frac(O). 

### `divQuot`

 Division by `a`, from O/a to K/O: the class of t goes to the class of t/a. 

### `exists_divQuot_eq`

 An element of K/O killed by `a ≠ 0` is the image of some x in O/a under division by `a`. 

### `addVal_le_length_torsionBy`

 Let `X` be a torsion module over a discrete valuation ring `O` with additive valuation `v`. If
the `a`-torsion of `X` is not all of `X`, then it contains a copy of `O / a`, so its length is at
least `v(a)`. 

### `exists_rows_addVal_det_le_of_divisible`

 Let O be a discrete valuation ring with normalized valuation v = `addVal O` and fraction field
K, and write `DivisibleQuot O` for K/O. Let ψ : A → M_d(O) be onto and N an A-submodule of A^ι.
If all w in ((K/O)^d)^ι with ∑ j, ψ(t j) • w_j = 0 for every t ∈ N lie in a submodule Z of length
at most b, then some square matrix B with rows in N has v(det ψ(B)) ≤ b, where ψ(B) is read as a
block matrix. A matrix acts on (K/O)^d by multiplication. 
