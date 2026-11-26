---
{
  "module": "src/New/Determinant/AuxiliaryForms/DiagonalTurns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/DiagonalTurns.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/DiagonalTurns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Turns on the diagonal, and the transfer of periods from the first path to the last

A turn on the diagonal replaces the node `(j, j)` of a path through the two grids by
`(j + 1, j + 1)`. A seesaw moves the period to the space `S = Ỹ^(j+1)_j = Y^(j+1)_j` common to both
paths, where the line contributes a theta kernel. There the line is reversed and the two maps are
exchanged, and a second seesaw moves the period on. Together with the turns off the diagonal this
transfers the periods from the first path to the last.

## Main definitions and results

* `New.Data.columnPeriod`, `New.Data.rowPeriod`: the integrals over the group of `S`.
* `New.Data.isProportional_of_columnPeriod`, `New.Data.IsProportional.exists_rowPeriod_eq_mul`: the
  seesaws.
* `New.Data.exists_columnLineKernel_eq`: reversing the line.
* `New.Data.exists_transfersPeriods_of_turn`: one turn, with the absolute value of its constant.
* `New.Data.exists_transfersPeriods_first_last`: the `m ^ 2` turns composed.

Notions from other files:
* `D.gridSpace 0 false a b` is the space `Y^a_b` and `D.gridSpace 0 true a b` is `Ỹ^b_a`; their
  bases are indexed by `D.GridIndex`.
* `modKernel S T a b 𝔪 Ψ p` is the theta kernel of the pair `(S, T)` with characters `a`, `b` of
  `[U(1)]`, for a function `Ψ` on matrices modulo `𝔪` and a polynomial `p`. On a space of rank `k`
  the character `a` gives the splitting character `New.AutChar.spaceChar`, the base change of `a`
  times `υ ^ (-k)`.
* `D.GridForm false a b` holds the conjugate forms on `Y^a_b`, and `D.GridForm true a b` the forms
  on `Ỹ^b_a`. In sums over tuples of matrices, one for each edge, the letter `S` names the tuple.
* `IsProportional Γ Ψ Ξ`, written `Ψ ∝ Ξ`: the periods of `Ψ` on the path `Γ` are multiples of `Ξ`
  by numbers that depend neither on the twist nor on the forms.
* `TransfersPeriods Γ' Γ k c`: path data `Ψ'` on `Γ'` give path data `Ψ` on `Γ`, with the bound for
  the number of roots of unity in a value multiplied by `k`, and `Ψ ∝ Ξ` implies `Ψ' ∝ Ξ / c`.
* `D.HasAbsUpToNormPower c f`: `‖c ϑ‖² = C (Nm Q)ᵏ (f ϑ)²`, with `Q` the modulus of the twist `ϑ`
  and with `C`, `k` independent of `ϑ`.


### `subdiagEquiv`

 The renumbering of the bases that identifies `Ỹ^(j+1)_j` with `Y^(j+1)_j`. 

### `gridSigns_subdiagEquiv`

 The renumbering `subdiagEquiv` carries the signs of `Ỹ^(j+1)_j` to those of `Y^(j+1)_j`. 

### `gridSpace_subdiagEquiv`

 The space `Ỹ^(j+1)_j` is the space `Y^(j+1)_j` with its basis renumbered by `subdiagEquiv`. 

### `subdiagMap`

 The identification of the group of `Ỹ^(j+1)_j` with that of `Y^(j+1)_j`. 

### `reindex_subdiagMap`

 The map `subdiagMap` is a right inverse of the renumbering of the group of `Y^(j+1)_j`. 

### `height_subdiagMap`

 The identification of the groups of `Ỹ^(j+1)_j` and `Y^(j+1)_j` preserves heights. 

### `subdiagWeight`

 A function of moderate growth on the group of `S = Y^(j+1)_j`, as a weight for periods of a
form on `Ỹ^(j+1)_j` against a form on `Y^(j+1)_j`. 

### `columnLineKernel`

 The kernel `θ^j_(v,p)` of the pair from the line `E ẽ_j`, the summand that `Ỹ^j_j` has beyond
`Y^j_j`, to `S = Y^(j+1)_j`, for the point mass at the column `v` modulo `𝔪 = gridModulus ϑ` and
the polynomial `p`, at `u ^ j` on the line. Here `u` is the scalar `flipScalar` of `U(1)` of the
modulus `𝔪`, used to reverse a line. The character `gridChar ϑ false j` of `S` is that of a
horizontal edge at the index `j`, here the edge from `Y^j_j`. The line has the splitting character
`υ⁻¹`, given by the trivial character of `[U(1)]`; it completes the character of `Y^j_j` to that
of `Ỹ^j_j`. 

### `columnLineKernel_weightFn`

 The weight function of `columnLineKernel` at a point `g` of the group of `Ỹ^(j+1)_j` is the
theta kernel from the line `E ẽ_j` to `S = Y^(j+1)_j`, for the point mass at the column `v` and the
polynomial `p`, taken at `flipScalar ^ j` on the line and at the image `subdiagMap g` of `g` in the
group of `S`. 

### `rowLineKernel`

 The kernel `θ^(j+1)_(v',p)` of the pair from `S = Y^(j+1)_j` to the line `E ẽ_(j+1)`, the
summand that `Ỹ^(j+1)_(j+1)` has beyond `Y^(j+1)_(j+1)`, for the point mass at the row `v'` modulo
`𝔪 = gridModulus ϑ` and the polynomial `p`, at `u ^ (j + 1)` on the line, with `u = flipScalar`. The
character `gridChar ϑ true j` of `S` is that of a vertical edge at the index `j`, here the edge to
`Ỹ^(j+1)_(j+1)`. The line has the splitting character `υ`, given by `upsilonU1`; it completes the
character of `Y^(j+1)_(j+1)` to that of `Ỹ^(j+1)_(j+1)`. 

### `rowLineKernel_weightFn`

 The weight function of `rowLineKernel` at a point `g` of the group of `Ỹ^(j+1)_j` is the theta
kernel from `S = Y^(j+1)_j` to the line `E ẽ_(j+1)`, for the point mass at the row `v'` and the
polynomial `p`, taken at the image `subdiagMap g` of `g` in the group of `S` and at
`flipScalar ^ (j + 1)` on the line. 

### `diagonalCorner`

 The corner for a turn at `(j, j)`, that is the six nodes at which such a turn changes a path. A
node `(z, a, b)` is `Y^a_b` for `z = false` and `Ỹ^b_a` for `z = true`. The turn removes the nodes
`low = Y^j_j` and `lowExt = Ỹ^j_j`, keeps `fst = Y^j_(j+1)` and `snd = Ỹ^(j+1)_j`, and adds
`high = Y^(j+1)_(j+1)` and `highExt = Ỹ^(j+1)_(j+1)`. The type `Unit` indexes the line by which
`lowExt` exceeds `low` and `highExt` exceeds `high`; the basis of `snd` is numbered as that of
`Y^(j+1)_j`. 

### `downPath`

 The path that continues both halves `q` down to `(j, j)`. 

### `rightPath`

 The path that continues both halves `q` to `(j + 1, j + 1)`. 

### `edges_downPath`

 The path through `(j, j)` has the edges of the halves `q b` in the grids `b` (`false` for that
of the `Y`) and the old edges of the corner, from `Y^j_j` and `Ỹ^j_j` to the nodes that it keeps. 

### `edges_rightPath`

 The path through `(j + 1, j + 1)` has the edges of the halves `q b` in the grids `b` and the new
edges of the corner, from the nodes that it keeps to `Y^(j+1)_(j+1)` and `Ỹ^(j+1)_(j+1)`. 

### `columnPeriod`

 The integral `I^S(Ψ; z, p)` over the group of `S = Y^(j+1)_j`, on the path through `(j, j)`. The
halves `q b` are monotone paths from `(0, m)` to `(j, j + 1)`, and `formMap` carries a form along
one of them by the matrices of the edges, by a `liftMove` (lift) where the first index grows and a
`transposedMove` (transposed lift) where the second drops. The `periodPairing` integrates the kernel
of the line times the form that reaches `S` in the grid of the `Ỹ` times the conjugate form that
reaches it through `Y^j_j`, translated by the point `z` of the archimedean group `GInf`. This is
summed against `Ψ` over the tuples `S` in `tuplesOn`, one matrix for each edge. The triple `x` holds
the twist and the two initial forms, and `D.Φ` indexes the infinite places. 

### `rowPeriod`

 The integral `I^S(Ψ; z, p)` over the group of `S = Y^(j+1)_j`, on the path through
`(j + 1, j + 1)` that continues the halves `q b`, which are monotone paths from `(0, m)` to
`(j, j + 1)`: as `columnPeriod`, with the kernel to the line `E ẽ_(j+1)`, and with the conjugate
form reaching `S` by a lift to `Y^(j+1)_(j+1)` (`liftMove`) and a transposed lift
(`transposedMove`). 

### `gridChar_subdiag`

 The characters `gridChar ϑ c l` of an edge of index `l`, vertical for `c = true` and horizontal
for `c = false`, agree at `Ỹ^(j+1)_j` and at `Y^(j+1)_j`, as the ranks are equal. 

### `modKernel_eq_columnLineKernel_mul`

 The kernel of the edge from `Ỹ^j_j = Y^j_j ⊕ E ẽ_j` to `Ỹ^(j+1)_j`, at the points `h ⊕ u ^ j`
(with `u = flipScalar`) and `g`, is the product of the kernel `columnLineKernel` of the line at `g`
and the kernel of the edge from `Y^j_j` to `S = Y^(j+1)_j` at `h` and `subdiagMap g`. The matrix `X`
of the edge is cut into columns, and the polynomial is a product of `A` in the variables of `Y^j_j`
and `B` in those of the line. 

### `rowLineKernel_mul_modKernel`

 The product of the kernel `rowLineKernel` of the line at `g` and the kernel of the edge from
`S = Y^(j+1)_j` to `Y^(j+1)_(j+1)` at `subdiagMap g` and `h` is the kernel of the edge from
`Ỹ^(j+1)_j` to `Ỹ^(j+1)_(j+1) = Y^(j+1)_(j+1) ⊕ E ẽ_(j+1)` at the points `g` and `h ⊕ u ^ (j + 1)`,
with `u = flipScalar`. 

### `isProportional_of_columnPeriod`

 Seesaw on the path through `(j, j)`: if all integrals `columnPeriod hj q Ψ z p` are multiples of
`Ξ` by constants that do not depend on the twist and the forms, then so are the periods of `Ψ` on
the path. 

### `IsProportional.exists_rowPeriod_eq_mul`

 Seesaw on `rightPath q`, the path through `(j + 1, j + 1)` that continues the halves `q`: if
`IsProportional (rightPath q) Ψ Ξ` holds, i.e. the periods of `Ψ` on that path are multiples of `Ξ`
by constants independent of the twist and the forms, then there is `β` with
`rowPeriod hj q Ψ z p x = β * Ξ x` for every `x : D.PeriodTriple`. 

### `modKernel_eq_sum_single`

 The theta kernel is linear in the function `Ψ` on matrices modulo `𝔪`: it is the sum of the
kernels of the point masses, weighted by `Ψ`. 

### `exists_columnLineKernel_eq`

 Reversing the line: the kernel from the line `E ẽ_j = Ỹ^j_j ⊖ Y^j_j` with column `v` is, up to a
factor `c` with `‖c‖² = (Nm 𝔪) ^ (-rk S)`, the Fourier transform of the kernels to the line
`E ẽ_(j+1)` with rows `v'`, with respect to an additive character `ψ`. Here `𝔪 = gridModulus ϑ` and
`S = Y^(j+1)_j`. The map `τ` of polynomials does not depend on the twist. 

### `isTurn_diagonalCorner`

 The corner on the diagonal, which removes the nodes `Y^j_j`, `Ỹ^j_j` and adds `Y^(j+1)_(j+1)`,
`Ỹ^(j+1)_(j+1)`, is a turn of a path whose other edges are those of two halves `q` from `(0, m)` to
`(j, j + 1)`. These edges avoid the removed nodes and do not end at the added ones; at one kept node
the old edge is vertical and the new one is not; opposite edges of the corner have equal characters.
An admissible family has at `Ỹ^(j+1)_(j+1)` its element at `Y^(j+1)_(j+1)` extended by `1` on the
line, and it stays admissible if any `k` is put at `Y^j_j` and `k ⊕ 1` at `Ỹ^j_j`. 

### `char_diagonalCorner`

 The character of the corner on the diagonal is the inverse product of the characters `edgeChar`
modulo `𝔪` of the edges `Y^j_j → Y^j_(j+1)` (`columnEdge`) and `Y^j_j → Y^(j+1)_j` (`rowEdge`),
since the edge from `Ỹ^j_j` to `Ỹ^(j+1)_j` has the character of the latter. 

### `card_column_le_vectorCountBound`

 For `S = Y^(j+1)_j` the number of columns modulo `𝔪`, the modulus `gridModulus ϑ`, is at most
`vectorCountBound ϑ`. 

### `periodPairing_columnLineKernel_eq`

 If the kernel from the line with column `v` is `c` times the Fourier transform of the kernels to
the line with rows `v'`, the same holds for their `periodPairing`, the integral of such a kernel
against a form `φ` on `Ỹ^(j+1)_j` and a form `y` on `Y^(j+1)_j` translated by the point `z` of the
archimedean group `GInf`. 

### `columnPeriod_eq_mul_rowPeriod`

 Reversing the line and crossing the square `(j, j)`, for one triple `x` of a twist and two
forms. Suppose the kernels from the line for the polynomial `p` (`columnLineKernel`) are `c` times
the Fourier transforms of the kernels to the line for the polynomial `p'` (`rowLineKernel`), the
exchange on the square with identification `σ` of its sides holds with factor `C`, and `Ψ`, with `X`
and `v'` put on the new edges by `newTuple`, corresponds under `σ` to the Fourier transform of `Ψ'`
in the column of the line. Then `columnPeriod` of `Ψ'` for `p` is `c * C` times `rowPeriod` of `Ψ`
for `p'`. 

### `exists_transfersPeriods_diagonal`

 One turn on the diagonal, at `j < m`. There are numbers `c ϑ ≠ 0` of absolute value
`turnRatio j j ϑ` up to a constant and a power of `Nm Q`, with `Q` the modulus of the twist `ϑ`,
such that the following holds for all pairs `q` of monotone paths from `(0, m)` to `(j, j + 1)`, one
in each grid. Path data `Ψ'` on `downPath q` give path data `Ψ` on `rightPath q`, with the bound for
the number of roots of unity in a value multiplied by `vectorCountBound = (Nm 𝔪) ^ (2 * n_m)`, where
`𝔪 = gridModulus ϑ` and `n_m = D.n D.m`, and `Ψ ∝ Ξ` implies `Ψ' ∝ Ξ / c`. 

### `exists_transfersPeriods_of_turn`

 One turn. For `i, j < m` there are numbers `c ϑ ≠ 0`, of absolute value `turnRatio i j` up to a
constant and a power of `Nm Q`, with `Q` the modulus of `ϑ`, such that for every turn at `(i, j)`
path data `Ψ'` on the old path give path data `Ψ` on the new one, with the bound for the number of
roots of unity in a value multiplied by `vectorCountBound = (Nm 𝔪) ^ (2 * n_m)`, where
`𝔪 = gridModulus ϑ` and `n_m = D.n D.m`, and `Ψ ∝ Ξ` implies `Ψ' ∝ Ξ / c`. 

### `exists_transfersPeriods_first_last`

 There are numbers `c ϑ ≠ 0` whose absolute value is the product over `i, j < m` of
`turnRatio i j ϑ`, up to a constant and a power of `Nm Q`, with `Q` the modulus of the twist `ϑ`,
such that path data `Ψ'` on the first path give path data `Ψ` on the last, with the bound for the
number of roots of unity in a value multiplied by `vectorCountBound ^ m ^ 2`, and `Ψ ∝ Ξ` implies
`Ψ' ∝ Ξ / c`. 
