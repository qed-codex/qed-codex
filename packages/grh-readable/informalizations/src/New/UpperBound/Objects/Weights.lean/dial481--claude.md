---
{
  "module": "src/New/UpperBound/Objects/Weights.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Weights.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Weights.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Harish-Chandra parameters, weights and lift diagrams of the definite spaces

A weight is given by its last entry and by the number of columns of each height of its Young diagram
at each infinite place of `E`. This file fixes the weights on the spaces `X_j` and `Y_m`. It defines
the Harish-Chandra parameters of the `X_j` and of `Y_m` in decreasing order, the highest weights
`μ(X_j)` and `μ(Y_m)`, and the diagrams of the lifts between the `X_j`. It computes the columns and
bounds the rows of these diagrams, and it shows that `μ(X_m)` and `μ(Y_m)` interlace. It also
computes `n_τ = |μ(X_m)_τ| - |μ(Y_m)_τ|`, where `|·|` is the sum of the entries.

## Main definitions and results

* `New.Data.columnCount`, `New.Data.lastEntry`: the columns and the last entry of the weight on
  `X_j`.
* `New.Data.keptColumns`, `New.Data.columnsY`: the columns of the weight on `Y_m`, obtained by
  branching.
* `New.Data.paramX`, `New.Data.weightX`, `New.Data.liftDiagram`: the doubled parameters and the
  weights of the `X_j`, and the diagrams of the lifts.
* `New.Data.weightX_eq`, `New.Data.weightY_eq`: the weights in terms of their columns.
* `New.Data.branchExponent_eq`: the formula for `n_τ`.

Notions from other files:
* `New.Data`: data `D` for parameters `P : New.Parameters`. They give a CM field `E`, the number
  `m = D.m` of lifts and a rank `r = D.r`. From these come `k = D.k = r + 1 - m`, `t = D.t = 5 r`,
  the ranks `n_j = D.n j = k + j (t + 1)` and the gap `Δ = D.gap = 2 * D.halfGap = 2 r ^ 8`.
* `X_j`, `Y_m`: the standard definite hermitian spaces over `E` of ranks `n_j` and `n_m - 1`. Lift
  `j + 1` is the theta lift from forms on `U(X_j)` to forms on `U(X_{j+1})`. Branching is the
  restriction of representations from `U(X_m)` to `U(Y_m)`. This file has only their weights.
* `New.Data.Φ`: the set of infinite places of `E`.
* `New.Data.a`, `New.Data.aPlaces`: the integer `a = x b`, for the scales `x` and `b` of the data,
  and the set of `a`-places, the places `≡ 1` modulo `P.q₀`.
* `New.Data.liftWeight`: the weight `κ_j(σ) = κ(σ) + (j + 1/2) Δ` at `σ`, with `κ = D.weight`. It is
  not to be confused with the column count `New.Data.columnCount`.
* `New.Data.targetParameter`: the sequence `λ^Y = (k/2 - 1, …, 1 - k/2; -κ_{1/2}, -κ_{3/2}, …)` at a
  place, where `κ_{i - 1/2} = κ_i - Δ / 2`.


 ## The column diagrams of the weights 

### `columnCount`

 The number of columns of height `h` at the place `τ` of the weight on the definite space `X_j`
of rank `n_j = k + j (t + 1)`, for `h < n_j` (see `weightX_eq`); here `k = D.k` and `t = D.t`. For
`h = 1` it is `D.a` at the places in `D.aPlaces` and `0` elsewhere; for `h = k ≠ 1` it is
`κ_1(τ) − ⌊(k + t + 1) / 2⌋`, with `κ_1(τ) = D.liftWeight 1 τ`; for `h > k` with `h ≡ k` mod `t + 1`
it is the gap `D.gap` minus `t + 1`; else it is `0`. Subtraction is that of natural numbers. 

### `columnCount_le`

 Bound on the number of columns of height `h` at `τ`, with the count at height one replaced by
`a`: `D.columnCount τ h` (or `a` if `h = 1`) is at most `a` (if `h = 1`) plus `D.liftWeight 1 τ` (if
`h = D.k`) plus the gap `D.gap`. 

### `lastEntry`

 The last entry of the weight on `X_j` at the place `τ` (see `weightX_eq`): it is `0` for
`j = 0`, else `⌊n_{j−1} / 2⌋ − κ_j(τ)`, with `n_j = D.n j` the rank `k + j (t + 1)` and
`κ_j(τ) = D.liftWeight j τ`. 

### `keptColumns`

 Let `m = D.m` be the number of lifts, and let `X_m`, `Y_m` be the definite spaces of ranks `n_m`
and `n_m - 1`. For `h < n_m` this is the number of columns of height `h` of the weight on `X_m` that
keep their height under branching to `Y_m` (see `weightY_eq`). It is `Δ / 2 − (t + 1) / 2`, with
`Δ / 2 = D.halfGap` half the gap, if `h ≥ k` and `h ≡ k` mod `t + 1`, and `0` otherwise. 

### `columnsY`

 The number of columns of height `h` at `τ` of the weight on `Y_m`, for `h < n_m - 1` (see
`weightY_eq`): the kept columns of height `h`, and the columns of height `h + 1` of the weight on
`X_m` that are not kept. 


## Parameters, weights and lift diagrams of the definite spaces

Parameters are doubled, so that they are integers; weights are not doubled. Entries and rows are
numbered from `0`.


### `twiceBlockEntry`

 Twice the entry `p` of the block `[n] = ((n - 1) / 2, (n - 3) / 2, …, (1 - n) / 2)`. 

### `sum_twiceBlockEntry`

 The entries of the block `[n]` have sum `0`. 

### `n_even`

 Each rank `n_j = k + j (t + 1)` is even, as `k` is even and `t` is odd. 

 ### The parameters and weights of the spaces `X_j` 

### `firstRowExcess`

 The number `a_τ`: it is `a` at the places in `D.aPlaces` (the `a`-places) and `0` elsewhere. 

### `paramX`

 Twice the Harish-Chandra parameters of the `X_j` at the place `τ`, in decreasing order: first
`λ^X = [k] + (a_τ, 0, …, 0)`, then the blocks `-κ_i + [t + 1]` for `i = 1, 2, …`. The parameter of
`X_j` consists of the first `n_j` entries. That they decrease follows from `weightX_eq`. 

### `paramX_block`

 The sequence `D.paramX τ` lists twice the Harish-Chandra parameters of the definite spaces `X_i`
at the place `τ`. For `b < t + 1`, with `t = D.t`, its entry at position `n_j + b` is twice entry
`b` of the block `-κ_{j+1} + [t + 1]`. Here `n_j = D.n j` is the rank of `X_j`,
`κ_{j+1} = D.liftWeight (j + 1) τ` and `[t + 1] = (t / 2, (t - 2) / 2, …, -t / 2)`. 

### `weightX`

 Entry `p` of the highest weight `μ(X_j)` at the place `τ`: the decreasing parameter less the
block `[n_j]`, where `n_j = D.n j` is the rank of `X_j`. Both `D.paramX τ` and `twiceBlockEntry` are
doubled, and the division by `2` is exact (`two_mul_weightX`). 

### `two_mul_weightX`

 The division by `2` in the definition of the weight `μ(X_j) = D.weightX j τ` is exact: twice the
weight is the doubled parameter `D.paramX τ` less the doubled block `[n_j]`. 

### `liftDiagram`

 Row `p` at the place `τ` of the diagram `μ_{j+1}^+ = μ(X_j) + κ_{j+1} - n_{j+1} / 2` of lift
`j + 1`, the theta lift from forms on `U(X_j)` to forms on `U(X_{j+1})`. Here `μ(X_j)` is the weight
`D.weightX j τ`, `κ_{j+1} = D.liftWeight (j + 1) τ` and `n_j = D.n j` is the rank of `X_j`. The
diagram has `n_j` rows and is continued by `0`. 

### `weightX_succ`

 For each entry `p < n_{j+1}`, the weight `μ(X_{j+1})` is
`(μ_{j+1}^+, 0, …, 0) + n_j / 2 - κ_{j+1}`, where `μ_{j+1}^+` is `D.liftDiagram j τ`, `n_j` is the
rank `D.n j` and `κ_{j+1}` is `D.liftWeight (j + 1) τ`. 

### `liftDiagram_zero`

 For `p < k` the rows of the first diagram are given by
`μ_1^+ = (a_τ, 0, …, 0) + κ_1 - n_1 / 2`, where `a_τ` is `D.firstRowExcess τ`, `κ_1` is
`D.liftWeight 1 τ` and `n_1` is the rank `D.n 1`. 

### `liftDiagram_succ`

 The recursion `μ_{j+2}^+ = (μ_{j+1}^+, 0, …, 0) + Δ - t - 1` of the lift diagrams, in the rows
`p < n_{j+1}`: each further lift adds the gap `Δ = D.gap` less the step `t + 1` of the ranks. 

 ### The columns and rows of the diagrams 

### `cast_columnCount_k`

 There are `κ_1 - n_1 / 2` columns of height `k`; this number is not negative. 

### `cast_columnCount_n_succ`

 There are `Δ - t - 1` columns of height `n_{j+1}`; this number is not negative. 

### `columnCount_eq_zero_of_lt_k`

 No column has a height below `k` other than `1`. 

### `not_dvd_sub_k`

 A height `u` strictly between `n_j` and `n_{j+1}` is none of the ranks `n_i`: the step
`t + 1` of the ranks does not divide `u - k`. 

### `columnCount_eq_zero_of_mem_Ioo`

 No column has a height strictly between the ranks `n_j` and `n_{j+1}`. 

### `cast_sum_columnCount_Ioo_k`

 The number of columns of height strictly between `p` and `k` is `a_τ = D.firstRowExcess τ` for
`p = 0` and `0` otherwise, as only the height `1` occurs below `k`. 

### `sum_columnCount_Ioo_succ`

 For `p < n_j`, the columns of height strictly between `p` and `n_{j+1}` are those of height
strictly between `p` and `n_j` and those of height `n_j`. 

### `liftDiagram_eq_sum_columnCount`

 Let `μ_{j+1}^+ = D.liftDiagram j τ` be the Young diagram of lift `j + 1` at the place `τ`. It
has `D.columnCount τ u` columns of each height `u` below the rank `n_{j+1} = D.n (j + 1)`, and no
others: row `p`, numbered from `0`, has one box for each such column of height above `p`. The
numbers `D.columnCount τ u` are common to all lifts; only the range of heights depends on `j`. 

### `liftDiagram_le`

 Let `j < D.m`, where `D.m` is the number of lifts. Row `p` of the diagram
`μ_{j+1}^+ = D.liftDiagram j τ` of lift `j + 1` has a bound that depends on `p`. For `p = 0` the row
is at most `a_τ + κ_{j+1}`. For `0 < p < D.k` it is at most `κ_{j+1}`. Otherwise it is at most
`D.m * Δ`. 

### `weightX_eq`

 The weight `μ(X_j)` at `τ` has `D.columnCount τ u` columns of each height `u < n_j`, and its
last entry is `D.lastEntry j τ`: for `p < n_j` the entry `p` is the last entry plus the number of
columns of height above `p`. 

### `lastEntry_eq`

 The last entry of the weight `μ(X_j)` at `τ` is `n_{j+1} / 2 - κ_{j+1}` plus the number
`D.columnCount τ (D.n j)` of columns of full height `n_j` in the diagram `D.liftDiagram j τ` of lift
`j + 1`, which has `n_j` rows. Here `n_j = D.n j` is the (even) rank of `X_j` and
`κ_{j+1} = D.liftWeight (j + 1) τ` is the weight of the character of lift `j + 1`. 

 ### The parameter and the weight of `Y_m` 

### `two_mul_targetParameter_of_lt`

 The first `k - 1` entries of the sequence `λ^Y = D.targetParameter τ` form the block
`[k - 1] = (k / 2 - 1, …, 1 - k / 2)`, where `k = D.k` is the (even) rank of `X_0`; both sides are
doubled. 

### `targetParameter_k_sub_one_add`

 The entry `k - 1 + i` (with `k = D.k`) of the parameter `λ^Y = D.targetParameter τ` is
`-κ_{i + 1/2} = Δ / 2 - κ_{i+1}`, where `Δ / 2 = D.halfGap` and
`κ_{i+1} = D.liftWeight (i + 1) τ`. 

### `sortedParamY`

 Twice the Harish-Chandra parameter of `Y_m` at the place `τ`, in decreasing order: first
`[k - 1]`, then for `i = 1, 2, …` the entry `-κ_{i - 1/2}` followed by the block `-κ_i + [t]`. Here
`[n] = ((n - 1) / 2, …, (1 - n) / 2)` is the block of `twiceBlockEntry`, `κ_i = D.liftWeight i τ`
and `κ_{i - 1/2} = κ_i - D.halfGap`. The block `[k - 1]` and the `-κ_{i - 1/2}` are the entries of
`D.targetParameter τ`. The parameter consists of the first `n_m - 1` entries. 

### `sortedParamY_n_sub_one`

 In `D.sortedParamY τ`, twice the Harish-Chandra parameter of `Y_m` (the definite space of rank
`n_m - 1`, `m = D.m`) at `τ` in decreasing order, entry `k - 1 + j` of `λ^Y = D.targetParameter τ`
stands at position `n_j - 1`. Here `n_j = D.n j = k + j (t + 1)` with `k = D.k` and `t = D.t`; both
sides are doubled. 

### `sortedParamY_block`

 In `D.sortedParamY τ`, twice the Harish-Chandra parameter of `Y_m` at `τ` in decreasing order,
entry `b < t` of the block `-κ_{j+1} + [t]` stands at position `n_j + b`, with `t = D.t`; both sides
are doubled. 

### `weightY`

 Entry `p` of the highest weight `μ(Y_m)` at the place `τ`: the decreasing parameter less the
block `[n] = ((n - 1) / 2, …, (1 - n) / 2)` for the rank `n = n_m - 1` of `Y_m`. Both
`D.sortedParamY τ` and `twiceBlockEntry` are doubled, and the division by `2` is exact
(`two_mul_weightY`). 

### `sortedParamY_sub_paramX`

 Let `λ`, `λ'` be the decreasing Harish-Chandra parameters of `X_m` and `Y_m` at the place `τ`,
so that `D.paramX τ` and `D.sortedParamY τ` are `2 λ` and `2 λ'`, with entries numbered from `0`.
Then `λ'_p - λ_{p+1} - 1 / 2` is the number `D.keptColumns (p + 1)` of columns of height `p + 1` of
the weight on `X_m` that keep their height under branching to `Y_m`; both sides are doubled. 

### `twiceBlockEntry_n_sub_one`

 The block `[n_m - 1]` is `[n_m]` without its first entry, raised by `1 / 2`; both sides are
doubled. Here `[n] = ((n - 1) / 2, …, (1 - n) / 2)` and `n_m = D.n D.m` is the rank of `X_m`. 

### `weightY_eq_weightX_add`

 The highest weights `μ = μ(X_m)` and `μ' = μ(Y_m)` at `τ` satisfy
`μ'_p = μ_{p+1} + D.keptColumns (p + 1)`, where the last term counts the columns of height `p + 1`
that keep their height under branching. 

### `two_mul_weightY`

 The division by `2` in the definition of the weight `μ(Y_m) = D.weightY τ` is exact: twice the
weight is the doubled parameter `D.sortedParamY τ` less the doubled block `[n_m - 1]`. 

### `keptColumns_le_columnCount`

 The columns of height `u` that keep their height under branching are at most as many as all
columns of height `u` at `τ`. With `μ = μ(X_m)`, `μ' = μ(Y_m)` and `u = p + 1 < n_m` this is
`μ'_p - μ_{p+1} ≤ μ_p - μ_{p+1}`. Together with `μ_{p+1} ≤ μ'_p` (`weightY_eq_weightX_add`) it says
that the weights interlace. 

### `keptColumns_eq_zero_of_lt_k`

 No column of height `u < k` keeps its height under branching, where `k = D.k` is the rank of
`X_0`. 

### `keptColumns_n_sub_one`

 With `m = D.m` and `n_m = D.n D.m`, `D.keptColumns (n_m - 1) = 0`: no column of height `n_m - 1`
of the weight on `X_m` keeps its height under branching to `Y_m`. Hence the weights `μ(X_m)` and
`μ(Y_m)` have the same last entry. 

### `sum_columnsY_add_keptColumns`

 For `u ≤ N`, the sum of `D.columnsY τ v` over heights `u ≤ v < N`, plus `D.keptColumns N`,
equals the sum of `D.columnCount τ v` over `u < v ≤ N`, plus `D.keptColumns u`. The `keptColumns`
terms telescope. 

### `weightY_eq`

 The weight `μ(Y_m) = D.weightY τ` at `τ` has `D.columnsY τ u` columns of each height
`u < n_m - 1`, and its last entry is `D.lastEntry D.m τ`, the last entry of `μ(X_m)`: for
`p < n_m - 1` the entry `p` is the last entry plus the number of columns of height above `p`. 

### `keptColumns_le_halfGap`

 At most `Δ / 2 = D.halfGap` columns of each height keep their height under branching. 

### `columnCount_sub_keptColumns_le_halfGap`

 At most `Δ / 2 = D.halfGap` columns of each height `u > k` lose a box under branching. 

### `columnsY_le`

 The weight `μ(Y_m)` at `τ` has at most `Δ = D.gap` columns of each height `u ≥ k`. 

 ### The exponent of the branching map 

### `branchExponent`

 The number `n_τ = |μ(X_m)_τ| - |μ(Y_m)_τ|`, where `|μ|` is the sum of the entries of `μ`. 

### `sum_paramX`

 The first `n_j = D.n j` entries of `D.paramX τ` are twice the Harish-Chandra parameter of `X_j`
at `τ`. Their sum is twice `a_τ - (t + 1) (κ_1 + ⋯ + κ_j)`. 

### `sum_sortedParamY`

 The first `n_m - 1` entries of `D.sortedParamY τ` are twice the Harish-Chandra parameter of the
definite space `Y_m` at the place `τ`, in decreasing order. For each `j`, the sum of the first
`n_j - 1` entries is twice `-(κ_{1/2} + ⋯ + κ_{j - 1/2}) - t (κ_1 + ⋯ + κ_j)`. The case `j = m` is
twice the sum of the entries of the parameter of `Y_m`. 

### `branchExponent_eq`

 The exponent `n_τ = |μ(X_m)_τ| - |μ(Y_m)_τ|`, where `|μ|` is the sum of the entries of the
weight `μ`, equals `a_τ - m Δ / 2`. 

### `branchExponent_eq_sum_columns`

 Let `|μ|` be the sum of the entries of a weight `μ`. The exponent
`n_τ = |μ(X_m)_τ| - |μ(Y_m)_τ|` is the number of columns of `μ(X_m)` that lose a box under branching
to `Y_m`, plus the last entry of `μ(X_m)`. Of the `D.columnCount τ u` columns of height
`u < n_m = D.n D.m`, all but `D.keptColumns u` lose a box. This is the form of the exponent in
`New.exists_branching_matrix`. 

### `sum_branchExponent`

 The sum of the exponents `n_τ` over the `f` infinite places of `E` is `#Φ_a · a - f m Δ / 2`,
where `Φ_a = D.aPlaces` is the set of `a`-places and `Δ / 2 = D.halfGap`. 
