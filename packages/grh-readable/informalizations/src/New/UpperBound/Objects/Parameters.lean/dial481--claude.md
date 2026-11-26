---
{
  "module": "src/New/UpperBound/Objects/Parameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Parameters.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Parameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Index sets, signs and parameters of the grids; the parameters of every step correspond

Two grids of unitary groups, `Y` and `Ỹ`, with nodes `(i, j)`, are treated together by a flag `z`
(`false` for `Y`, `true` for `Ỹ`). A node has a base block of `r` (in `Ỹ`, `r + 1`) indices, `i`
added blocks of one kind and `j` of another (`New.BlockIndex`). For `z = false` the node `(i, j)` is
`Y^i_j` with its parameter. For `z = true` it is `Ỹ^j_i` with the negative of its parameter, so that
one formula serves both grids. An offset `o` shifts the second kind of block; the grids have
`o = 0`, and the nodes with `i = 0` are the intervals `[o + 1, o + j]` of the triangles.

* `New.Data.GridIndex`, `New.Data.gridSigns`, `New.Data.gridParam`: index set, signs and doubled
  parameter of a node.
* `New.Data.gridDiagEquiv`: at `(j, j)`, `j ≤ m`, `Ỹ` is `Y` plus one vector of sign `(-1)^j`.
* `New.Data.gridParam_interlace`: at the node `(m, m)` the parameter of `Y` and that of `Ỹ`
  (`-gridParam true`) interlace.
* `New.Data.gridCentres`, `New.Data.isParam_gridParam`: the parameter of a node consists of a stem
  and the blocks of a set of centres (`New.CentreSystem`).
* `New.Data.paramsCorrespond_grid_succ_left`, `New.Data.paramsCorrespond_grid_succ_right`,
  `New.Data.paramsCorrespond_leftPair`: each step inserts a block, so the parameters correspond
  (`New.ParamsCorrespond`).

Notions from other files:
* `New.Data`: the admissible data `D`, with `m` (even) lifts, the rank `r` (odd), `k = r + 1 - m`,
  `t = 5 r`, the gap `Δ = D.gap = 2 halfGap` and the set `D.Φ` of infinite places.
* `New.Data.RowIndex`: an index set with `r` elements, numbered by `New.Data.basisNumber`.
* `New.Data.liftWeight`: the centre `w_j = κ_j = κ + (j + 1/2) Δ` at an infinite place, with
  `κ = D.weight`, the gap `Δ = D.gap` and `Δ / 2 = D.halfGap`.
* `New.Data.targetParameter`: the target parameter, the vector
  `λ^Y = ([k - 1]; -κ_{1/2}, -κ_{3/2}, …)`, with entries numbered from `0`; the entry `r` is
  `-κ_{m+1/2}`.
* `New.ParamsCorrespond γ γ' l l' s s'`: at each infinite place, the doubled parameters `l` (signs
  `s`) and `l'` (signs `s'`) satisfy the block rule (`New.IsBlockRule`) for the weights `γ`, `γ'`.


### `GridIndex`

 The index set of the node `(i, j)`. For `z = false` (grid `Y`) it is `D.RowIndex` with `i`
and then `j` blocks of length `t`. For `z = true` (grid `Ỹ`) it is `D.RowIndex ⊕ Unit` with `i`
blocks of length `t + 1` and `j` blocks of length `t - 1`. 

### `gridIndex_true`

 The index set `D.GridIndex true i j` of the node `(i, j)` of grid `Ỹ` is `D.RowIndex ⊕ Unit`
with `i` blocks `Fin (D.t + 1)` and then `j` blocks `Fin (D.t - 1)`. 

### `gridNumber`

 The numbering of the base index set: `D.basisNumber` on `D.RowIndex`, and `r` for the extra
point of grid `Ỹ`. 

### `gridBlockEquiv`

 A chosen splitting of the index set of the node `(i, j)` into blocks. An index becomes either a
base number or a pair `(l, b)` of a block of the first or second kind and a position in that block.
At the node `(0, 0)` the base number is the one under `D.gridNumber z`; otherwise the bijection is
arbitrary (`New.BlockIndex.equivSum`). 

### `entrySign_eq_ite`

 The sign `entrySign o j a` is `-1` if `o + a + min (a - o) j` is odd and `1` otherwise, the
subtraction being truncated at `0`. 

### `gridSigns`

 The signs at the node `(i, j)` with offset `o`; the grids are the case `o = 0`, the triangles
the case `i = 0`. The base index with number `n` has the sign `entrySign o j (n + 1 - k)`, and the
added blocks have the sign `+1`. 

### `gridParam`

 The doubled parameter at the node `(i, j)` with offset `o` and the infinite place `τ`: an
integer vector on the index set (`HCParam`). For `o = 0` it is twice the
parameter of `Y^i_j` if `z = false`, and minus twice the parameter of `Ỹ^j_i` if `z = true`; see
`gridParam_false` and `neg_gridParam_true`. A block of length `s` centred at `c` has the doubled
entries `2c + s - 1, 2c + s - 3, …, 2c - s + 1`. 

### `gridParam_false`

 Grid `Y`: `D.gridParam false o i j τ` is twice `D.targetParameter τ` on the base, with blocks of
length `t` centred at `w_l` (`1 ≤ l ≤ i`) and at `-w_(o+l)` (`1 ≤ l ≤ j`). All entries are lowered
by `1` if `i + j` is odd. 

### `gridParam_true`

 Grid `Ỹ`: `D.gridParam true o i j τ` is twice `D.targetParameter τ`, plus `1`, on the base, with
blocks of length `t + 1` centred at `w_l` (`1 ≤ l ≤ i`) and blocks of length `t - 1` centred at
`-w_(o+l)` (`1 ≤ l ≤ j`). 

### `neg_gridParam_true`

 The doubled parameter of `Ỹ^j_i` is minus `gridParam true 0 i j`, entry by entry: minus twice
`D.targetParameter τ`, minus `1`, on the base, and rising blocks of length `t + 1` centred at `-w_l`
(`1 ≤ l ≤ i`) and of length `t - 1` centred at `w_l` (`1 ≤ l ≤ j`). 

### `signsY`

 The signs of the space `Y_j` on its index type `D.Y j` (`D.RowIndex` and `j` blocks of length
`t`), which is the node `(0, j)` of grid `Y` with offset `0`. 

### `paramY`

 Twice the parameter of the space `Y_j` at each infinite place, on the index type `D.Y j`
(`D.RowIndex` and `j` blocks of length `t`): the node `(0, j)` of grid `Y` with offset `0`. 

### `gridWeight`

 A step between two nodes inserts the block of a centre `±w_{l+1}`, and each of the two nodes has
a weight: if its index type `n` has cardinality `N`, the weight at `τ` is `⌊N/2⌋ - w_{l+1}(τ)` for
`c = true` and `⌈N/2⌉ - w_{l+1}(τ)` for `c = false`. The ceiling is written `(N + 1) / 2`. 

### `gridHarmonic`

 The product over the infinite places of the field `D.E` of the chosen joint harmonic
polynomials (`New.jointHarmonic`) for the nodes `(a, b)` and `(i, j)` of grid `z` with offset `o`.
The weights are `D.gridWeight c l`, where `l` gives the centre `±w_{l+1}` of the step and `c` the
rounding. The parameters are negated (`negIf`) if `d` is true, as for the step from `(i, j)` to
`(i + 1, j)` (see `paramsCorrespond_grid`). 

 ### Ranks and numbers of negative signs 

### `card_gridIndex`

 The node `(i, j)` has rank `r + i t + j t` in grid `Y`, and `r + 1 + i (t + 1) + j (t - 1)` in
grid `Ỹ`, where it is the space `Ỹ^j_i`. 

### `negCount_gridSigns_eq_sum`

 The negative signs of the node `(i, j)` with offset `o` all lie on the base, so their number
is that of the `n < r + z` with `entrySign o j (n + 1 - k) = -1`. 

### `negCount_gridSigns`

 With offset `0`, the node `(i, j)` has `⌊(m - j)/2⌋` negative signs in grid `Y` and
`⌊(m - j + 1)/2⌋` in grid `Ỹ` (the space `Ỹ^j_i`), where `m - j` is truncated at `0`. 

### `gridSigns_true_zero`

 With offset `0`, the signs of grid `Ỹ` at the node `(0, 0)` are those of `D.Y 0` (`D.signsY 0`),
with the sign `+1` at the extra point. 

### `exists_equiv_diagonal_signs`

 On the diagonal, with offset `0`, the signs of `Ỹ` are, up to a bijection of the index types,
the signs of `Y` together with one more sign `(-1) ^ min j m`. 

### `gridDiagEquiv`

 A bijection from the index set of `Y` at `(j, j)` plus one point to that of `Ỹ`. It is the
identity for `j = 0`. Otherwise it is chosen to match the signs (`exists_equiv_diagonal_signs`). 

### `sumElim_gridSigns_comp_gridDiagEquiv_symm`

 For `j ≤ m` and offset `0`, the signs of `Ỹ` at `(j, j)` are, through `D.gridDiagEquiv j`,
those of `Y` together with the sign `(-1)^j` at the extra point. 

 ### Gaps, interlacing and sizes of the parameters 

### `card_gridIndex_mod_two`

 The parity of the size of the index set `D.GridIndex z i j` of the node `(i, j)`: it is even in
grid `Ỹ` (`z = true`), and in grid `Y` (`z = false`) it is odd iff `i + j` is even. 

### `liftWeight_add_gap_le`

 The weights `D.liftWeight a τ` increase by at least `D.gap` from `a` to any `b > a`, and by at
least `2 * D.gap` if `b > a + 1`. 

### `gridSigns_eq_one`

 For `m ≤ j` and offset `0`, all signs at the node `(i, j)` are `+1`. 

### `sum_ite_lt_sub_two_mul`

 The number of entries above `x` of the falling block `A, A - 2, …` of length `n` is
`⌊(A + 1 - x) / 2⌋`, clamped to the interval `[0, n]`. 

### `sum_ite_lt_add_two_mul`

 The number of entries above `x` of the rising block `A, A + 2, …` of length `n` is
`⌊(A + 2 n - 1 - x) / 2⌋`, clamped to the interval `[0, n]`. 

### `max_min_succ_sub_max_min_mem_Icc`

 Two blocks with step `2` and the same centre `c`, of lengths `n + 1` and `n`, interlace. The
left side is the number of entries above `x` of the longer block, less that of the shorter one. It
is `1` if `x` is below an integer `low ≤ c - n`, it is `0` if `x` is not below an integer
`high ≥ c + n`, and it is always `0` or `1`. 

### `targetParameter_sub_one_add`

 The entry `D.k - 1 + a` of `D.targetParameter τ` is `D.halfGap - D.liftWeight (a + 1) τ`. 

### `sum_ite_targetParameter_sub_sum_ite_mem_Icc`

 The base case of `gridParam_interlace`. Let `λ_n = D.targetParameter τ n` be the entries of the
target parameter and `s = 2 λ_(k-1)`. The number of `n < k` with `x < -2 λ_n - 1`, less the number
of `n < k - 1` with `x < 2 λ_n`, is `1` if `x < s`, is `0` if `-s - 1 ≤ x`, and is always `0` or
`1`. 

### `gridParam_interlace`

 At the infinite place `τ` and with offset `0`, the entries of the parameters of the node
`(m, m)` of grid `Ỹ` (doubled, these are `-gridParam true`) and of grid `Y` (flag `false`)
alternate in decreasing order, the
first coming from `Ỹ`: for every integer `x`, the number of doubled entries above `x` on `Ỹ^m_m`,
less that on `Y^m_m`, is `0` or `1`. 

### `abs_gridParam_le`

 For `i, j ≤ m` and offset `0`, all entries of the doubled parameter at the node `(i, j)` have
absolute value at most `⌈20 b⌉`, where `b = D.b = exp D.logB`. 

### `card_gridIndex_le`

 For `i, j ≤ m`, the node `(i, j)` of either grid has rank at most `2 * D.n m`, where
`D.n m = k + m (t + 1)`. 

 ### The centres of a grid and the blocks of its nodes 

### `targetParameter_strictAnti`

 The entries of the target parameter at `τ` are strictly decreasing. 

### `two_mul_targetParameter_le`

 The entries of the target parameter are at most `k / 2`. 

### `liftWeight_succ_add_gap_le`

 For `l < l'`, the weight `D.liftWeight (l' + 1) τ` exceeds `D.liftWeight (l + 1) τ` by at least
the gap `D.gap`. 

### `halfGap_le_targetParameter_add_liftWeight`

 For `p < D.posRank j = D.k + j - 1`, the entry `p` of the target parameter at the infinite place
`τ` lies at least `D.halfGap` above the centre `-D.liftWeight j τ`: `D.halfGap ≤ D.targetParameter τ
p + D.liftWeight j τ`. 

### `targetParameter_add_liftWeight_le_neg_halfGap`

 For `D.posRank j = D.k + j - 1 ≤ p`, the entry `p` of the target parameter lies at least
`D.halfGap` below the centre `-D.liftWeight j τ`. 

### `targetParameter_add_liftWeight_gap`

 The centre `-D.liftWeight j τ` is at distance at least `D.halfGap` from the entries of
`D.targetParameter τ`. The entry `p` lies above it if `p < D.posRank j = k + j - 1`, and below it
otherwise. The two cases are `halfGap_le_targetParameter_add_liftWeight` and
`targetParameter_add_liftWeight_le_neg_halfGap`. 

### `gridCentres`

 The centres of the grid `z` at `τ`: for `l < m` an up centre `w_(l+1)`, named `inl l`, and a
down centre `-w_(l+1)`, named `inr l`. The lengths are `t` in grid `Y`, and `t + 1` and `t - 1` in
grid `Ỹ`. The stem is the parameter on the base. In grid `Ỹ` this is the negative of the system of
the spaces `Ỹ^i_j`, whose up and down centres are exchanged. 

### `gridBlocks`

 The centres whose blocks are present at the node `(i, j)` with offset `o`: the up centres
`l < i` and the down centres `o ≤ l < o + j`. 

### `gridBlocks_succ_left`

 The step from `(i, j)` to `(i + 1, j)` adds the up centre `i`. 

### `gridBlocks_succ_right`

 The step from `(i, j)` to `(i, j + 1)` adds the down centre `j + o`. 

### `gridBlocks_succ_right_eq_insert_first`

 The node `(i, j + 1)` with offset `o` has the centres of the node `(i, j)` with offset `o + 1`
and the down centre `o`. 

### `gridBlocks_subset`

 For `i ≤ D.m` and `o + j ≤ D.m`, the centres `gridBlocks o i j` of the node `(i, j)` with offset
`o` lie in the centres `(D.gridCentres τ z).centres` of the grid `z` at `τ`. 

### `isSeparated_gridCentres`

 At an infinite place `τ` of the field `D.E`, the centres `±w_(l+1)(τ)`, `l < m`, of the grid `z`
are separated by `Δ - t - 2`. The block lengths have the parity of the size of the stem, the
parameter on the base. For each centre `c`, the doubled entries of the stem and of the blocks of the
other centres are at distance at least `Δ - t - 2` plus the block length of `c` from `2c`. 

### `entrySign_eq_mul_sign`

 The sign `entrySign o j a` is `-1` if `o + a + min (a - o) j` is odd and `1` otherwise. Let
`a ≤ D.m`. Let `y` be a doubled entry with `y ≤ 2 * D.liftWeight (l + 1) τ` for all `l ≥ i`. For `l`
outside `[o, o + j)`, let `y < -2 * D.liftWeight (l + 1) τ` hold exactly if `l < a`. Then
`entrySign o j a` is `(-1) ^ o` times the sign of `y` in `D.gridCentres τ z`, the centres of grid
`z` at the place `τ` (`CentreSystem.sign`). 

### `gridParam_add_lowering`

 The doubled entries at the node `(i, j)` of grid `z` with offset `o` and the infinite place `τ`,
after the lowering is undone; the lowering is `1` in grid `Y` for odd `i + j`, else `0`. Read `z` as
`0` or `1`, and put `λ_n = D.targetParameter τ n` and `w_a = D.liftWeight a τ`. The base entry with
number `n` is `2 λ_n + z`. The entry at the position `b` of the block `l` is
`2 w_(l+1) + (t + z) - 1 - 2 b` for a block of the first kind (`l < i`) and
`-2 w_(o+l+1) + (t - z) - 1 - 2 b` for a block of the second kind (`l < j`). 

### `gap_le_abs_targetParameter_sub`

 Take two entries of the target parameter with numbers `n` and `n'`, where
`n + 1 - D.k ≠ n' + 1 - D.k` (truncated subtraction). They differ by at least the gap `D.gap`. 

### `three_mul_halfGap_le_abs_targetParameter_add_liftWeight`

 For `l < j`, if the base entry with number `n` at the node `(i, j)` with offset `o` has sign
`entrySign o j (n + 1 - D.k) ≠ 1`, then `D.targetParameter τ n` is at distance at least
`3 * D.halfGap` from the block centre `-D.liftWeight (o + l + 1) τ`. The reason is that the two
entries of the target parameter next to this centre have the sign `+1`. 

### `gridParam_injective`

 At an infinite place `τ` the doubled parameter of the node `(i, j)` of grid `z` with offset `o`
takes distinct values at distinct indices. 

### `even_gridParam_add_card_sub_one`

 Each entry of the doubled parameter `D.gridParam z o i j τ` at the node `(i, j)` has the parity
of `card (D.GridIndex z i j) - 1`, the size of the index set minus one. 

### `two_mul_gap_le_abs_gridParam_sub`

 At the infinite place `τ`, two entries of the doubled parameter at a node whose signs differ
are at least `2 * D.gap = 4 * D.halfGap` apart. 

### `hasGap_gridParam`

 The doubled parameter `D.gridParam z o i j τ` at the node `(i, j)` with offset `o` has, at the
infinite place `τ`, the gap `D.gap` for the signs of the node (`HasGap`): its entries are distinct,
have the parity of the rank minus one, and differ by at least `2 * D.gap` where the signs differ. 

### `gridSigns_eq_mul_sign`

 Let `o + j ≤ m`, with `o = 0` (the grids) or `i = 0` (the triangles). For every infinite place
`τ`, the sign at the index `x` of the node `(i, j)` with offset `o` is `(-1) ^ o * (-1) ^ N`. Let
`y` be the doubled entry `gridParam` at `τ` and `x`, plus `1` if the stem of `D.gridCentres τ z` and
the set `gridBlocks o i j` both have odd size. Then `N` is the number of centres outside
`gridBlocks o i j` that are up and below `y / 2`, or down and above `y / 2`. 

### `isParam_gridParam`

 Let `τ` be an infinite place of the field `D.E`, let `o + j ≤ m`, and let `o = 0` or `i = 0`.
The doubled parameter at `τ` of the node `(i, j)` of grid `z` with offset `o` is the parameter of
the set `gridBlocks o i j` in the system `D.gridCentres τ z`. 

 ### The parameters at the two ends of a step correspond 

### `mul_card_gridIndex_add_pow_three_le`

 The separation `D.gap - D.t - 2` of the centres is at least `500 (N + N') ^ 3` for the ranks
`N`, `N'` of two nodes `(i, j)`, `(i', j')` of a grid with `i, j, i', j' ≤ m`. 

### `paramsCorrespond_grid_succ_left`

 For `i + 1 ≤ D.m`, `j ≤ D.m` and offset `0`, the negated parameters of the nodes `(i, j)` and
`(i + 1, j)` correspond (`ParamsCorrespond`). The weight of a node with `N` indices is
`D.gridWeight z i`. The step inserts the block of the up centre `D.liftWeight (i + 1) τ`. 

### `gridWeight_not`

 The weight of the character of a step that inserts the block of the down centre `-w_(l+1)` is
this centre plus half the rank of the node, rounded down. 

### `paramsCorrespond_grid_succ_right`

 The parameters correspond along the edge from `(i, j)` to `(i, j + 1)`, in the grids (`o = 0`)
and in the triangles (`i = 0`). At each infinite place `τ` they satisfy the block rule `IsBlockRule`
for the weights `D.gridWeight (!z) (j + o)` of the two nodes (see `gridWeight_not`). The step
inserts the block of the down centre `-D.liftWeight (j + o + 1) τ`. 

### `paramsCorrespond_grid`

 Both kinds of step in one statement, for arguments that treat them together: `isLeft = true` is
`paramsCorrespond_grid_succ_left` and `isLeft = false` is `paramsCorrespond_grid_succ_right`. The
equation `h_step` fixes the target `(i', j')` and the weights: at a node of rank `N` the weight
`D.gridWeight weightGrid weightIdx` is `N / 2`, rounded down if `weightGrid` is true and up
otherwise, less `w_(weightIdx+1)`. The target satisfies `i' ≤ m` and `j' + o ≤ m`, and it lies in a
grid (`o = 0`) or in a triangle (`i' = 0`). 

### `paramsCorrespond_neg_gridParam_insert_first`

 Adding the first block of an interval, for `i + j < m`: the node `(0, j)` with offset `i + 1`
and the node `(0, j + 1)` with offset `i` have corresponding negated parameters: at each infinite
place they satisfy the block rule `IsBlockRule` for the weight that is, at each end, the rank `N`
minus `D.gridWeight (!z) i`. 

### `paramsCorrespond_leftPair`

 Adding or removing the first block of an interval, for `i + j < m`: the negated parameters of
the node `(0, j)` with offset `i + 1` and of the node `(0, j + 1)` with offset `i` correspond, in
both directions. 
