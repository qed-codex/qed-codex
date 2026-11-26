---
{
  "module": "src/New/Determinant/AuxiliaryForms/GridPaths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/GridPaths.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/GridPaths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Monotone paths through two square grids, and their turns

The combinatorics of the paths along which forms are moved through the two grids of unitary groups,
the grid of the `Y^i_j` and the grid of the `Ỹ^i_j`. Here only the indices occur.

A path goes from `(m, 0)` to `(0, m)` by steps up (`j` grows) or left (`i` falls) and meets the
diagonal once, at some `(l, l)`. Its first half lies in the grid of the `Ỹ` and its second half in
that of the `Y`. Both halves are recorded in one shape, as paths from `(0, m)` to `(l, l)` by steps
down or right. The half in the grid of the `Y` is read backwards, the way conjugate forms move. The
half in the grid of the `Ỹ` is read forwards, the way forms move, with the two indices exchanged: a
step left is recorded as a step down, and a step up as a step right.

## Main definitions and results

* `New.GridPath`: a monotone path in one grid. `New.TwoGridPath`: a path through both grids, given
  by two halves that meet on the diagonal.
* `New.TwoGridPath.Turn`: a turn replaces a node `(i, j)` by `(i + 1, j + 1)`.
* `New.TwoGridPath.exists_turn`: every path but the last can be turned.
* `New.TwoGridPath.turn_induction`: induction backwards along turns, one at each `(i, j)` with
  `i, j < m`, from the last path to the first.


### `GridPath`

 A monotone path in a grid from the node `(a₀, b₀)` to the node `(a, b)`: each step lowers the
second index or raises the first. 

### `GridPath.nil`

 The path without steps. 

### `GridPath.down`

 A path followed by the step from `(a, b + 1)` to `(a, b)`. 

### `GridPath.right`

 A path followed by the step from `(a, b)` to `(a + 1, b)`. 

### `append`

 One path followed by another. 

### `column`

 The path down the first column, from `(0, m)` to `(0, b)`. 

### `row`

 The path along the row `m`, from `(0, m)` to `(a, m)`. 

### `squares`

 The unit squares between the first column and the steps down of a path, each named by its
corner with the least indices: the step from `(a, b + 1)` to `(a, b)` contributes the `(i, b)` with
`i < a`. 

### `column_of_lt`

 The path down the first column from `(0, m)` to `(0, b)`, for `b < m`, is the one to
`(0, b + 1)` followed by a step down. 

### `le_and_le`

 Along a path from `(a₀, b₀)` to `(a, b)` the first index does not fall and the second does
not grow. 

### `eq_row`

 The only path from `(0, m)` to `(a, m)` is `row m a`, the one that stays in the row `m`. 

### `squares_append`

 The squares to the left of the steps down of `p` followed by `q` are those of `p` and those
of `q`. 

### `bounds_of_mem_squares`

 A square `s` to the left of a step down of a path from `(a₀, b₀)` to `(a, b)` lies to the left
of the column `a` and between the rows `b` and `b₀`. 

### `squares_row`

 The path along a row has no step down, hence no squares. 

### `notMem_squares_down_right_append`

 Let a path follow `q` to `(i, j + 1)`, step down to `(i, j)`, step right to `(i + 1, j)` and
follow `r`. Then the unit square with lower left corner `(i, j)` is not among the `squares` of the
path, the unit squares to the left of its steps down. 

### `squares_right_down_append`

 Let a path follow `q` to `(i, j + 1)`, go to `(i + 1, j)` in two steps and follow `r`. If it
passes through `(i + 1, j + 1)` instead of `(i, j)`, then its set of `squares`, the unit squares to
the left of its steps down, gains the square with lower left corner `(i, j)`. 

### `exists_corner_or_eq_down_or_eq`

 A path from `(a₀, b₀)` to `(a, b)` has a corner `(i, j)`, where it comes down and leaves to the
right, or ends with a step down, or has no step down (`b = b₀`). 

### `TwoGridPath`

 A path from `(m, 0)` to `(0, m)` by steps up or left, through the two grids. It meets the
diagonal at `(l, l)` with `l = diagonalIndex`. Both halves are recorded as paths from `(0, m)` to
`(l, l)`: `half false` is the part after the diagonal read backwards, in the grid of the `Y`, where
`(a, b)` is `Y^a_b`, and `half true` is the part before the diagonal with the two indices
exchanged, in the grid of the `Ỹ`, where `(a, b)` is `Ỹ^b_a`. 

### `TwoGridPath.diagonalIndex`

 The index `l` of the node `(l, l)` at which the path meets the diagonal. 

### `TwoGridPath.half`

 The halves in the two grids, each recorded as a path from `(0, m)` to the diagonal node. 

### `first`

 The first path, through `(0, 0)`: it goes left from `Ỹ^m_0` to `Ỹ^0_0` and up from `Y^0_0` to
`Y^0_m`, so both halves are recorded as going down the first column. 

### `last`

 The last path, through `(m, m)`: it goes up from `Ỹ^m_0` to `Ỹ^m_m` and left from `Y^m_m` to
`Y^0_m`, so both halves are recorded as going along the row `m`. 

### `Turn`

 `Turn Γ (i, j) Γ'`: the path `Γ` reaches `(i, j)` from the right and leaves it upwards, and `Γ'`
arises from `Γ` by replacing the node `(i, j)` by `(i + 1, j + 1)`. 

### `Turn.inner`

 A turn off the diagonal, at a corner `(a, b)` where one half comes down and leaves to the
  right. For `half true` the node has the indices `(b, a)`. 

### `Turn.diagonal`

 A turn on the diagonal: both halves end with a step down. 

### `squares`

 The unit squares between the first path and `Γ`, each named by its corner with the least
indices: the `(i, j)` with `i, j < Γ.diagonalIndex`, the squares of `Γ.half false`, and the mirror
images in the diagonal of the squares of `Γ.half true`. 

### `mem_squares`

 The unit square with least corner `s` lies between the first path, through `(0, 0)`, and the
path `Γ` if and only if both indices of `s` are less than `Γ.diagonalIndex`, or `s` lies to the left
of a step down of `Γ.half false`, or its mirror image `s.swap` lies to the left of a step down of
`Γ.half true`. 

### `diagonalIndex_le`

 A path from `(m, 0)` to `(0, m)` meets the diagonal at a node with indices at most `m`. 

### `squares_subset`

 Let `Γ` be a path from `(m, 0)` to `(0, m)` by steps up or left. The set `Γ.squares` of unit
squares between `Γ` and the path `first m` through `(0, 0)`, each named by its corner `(i, j)` with
the least indices, has only members with `i, j < m`. 

### `squares_first`

 No unit square lies between the first path, through `(0, 0)`, and itself. 

### `squares_last`

 For the last path `last m`, the one through `(m, m)`, the set `(last m).squares` is exactly the
`(i, j)` with `i, j < m`, that is `range m ×ˢ range m`. 

### `Turn.squares_eq`

 Let `Γ` and `Γ'` be paths in `TwoGridPath m` with `Γ.Turn s Γ'`. Then `s ∉ Γ.squares`, and
`Γ'.squares` is `Γ.squares` with `s` inserted. 

### `Turn.mem_product`

 If a path from `(m, 0)` to `(0, m)` has a turn at the node `s = (i, j)`, then `i, j < m`. 

### `Turn.exists_corner_of_lt`

 Let `Γ'` arise from `Γ`, a path from `(m, 0)` to `(0, m)` by steps up or left, by replacing the
node `(i, j)` by `(i + 1, j + 1)`, where `i < j`. The turn takes place in `Γ.half false`, the part
of `Γ` after the diagonal node `(Γ.diagonalIndex, Γ.diagonalIndex)`, read backwards from `(0, m)`.
This half splits as a path `q` to `(i, j + 1)`, a step down, a step right and a path `r` to the
diagonal. The path `Γ'` has these two steps exchanged, and has the same diagonal node and the same
other half. 

### `Turn.exists_half_true_eq_of_gt`

 Let `Γ'` arise from `Γ`, a path from `(m, 0)` to `(0, m)` by steps up or left, by replacing the
node `(i, j)` by `(i + 1, j + 1)`, where `j < i`. The turn takes place in `Γ.half true`, the part
of `Γ` from `(m, 0)` to the diagonal node `(Γ.diagonalIndex, Γ.diagonalIndex)`, recorded with the
two indices exchanged, so that the node `(i, j)` appears as `(j, i)`. This half splits as a path
`q` to `(j, i + 1)`, a step down, a step right and a path `r` to the diagonal. The path `Γ'` has
these two steps exchanged, and has the same diagonal node and the same other half. 

### `Turn.exists_eq_down_and_eq_right`

 A turn at `(j, j)` takes place on the diagonal: both halves reach `(j, j + 1)`, and their last
step, down to `(j, j)`, is replaced by the step right to `(j + 1, j + 1)`. 

### `exists_turn`

 Every path `Γ` from `(m, 0)` to `(0, m)` by steps up or left, other than `last m`, has a
turn. 

### `turn_induction`

 Let a property of a path and a finite set of index pairs hold for the last path, through
`(m, m)`, and the empty set. Suppose that for each turn at `s` from `Γ` to `Γ'` and each set `T`
without `s`, it passes from `Γ'` and `T` to `Γ` and `insert s T`. Then it holds for the first path,
through `(0, 0)`, and the set of all `(i, j)` with `i, j < m`. 
