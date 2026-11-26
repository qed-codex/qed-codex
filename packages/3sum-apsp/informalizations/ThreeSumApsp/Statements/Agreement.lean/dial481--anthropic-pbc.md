---
{
  "module": "ThreeSumApsp/Statements/Agreement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/Agreement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/Agreement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The notions that are defined twice agree

The end statement defines Exact Triangle, the (min,+)-product, APSP, a matrix written row by row,
the weight of a `k`-clique, "a program solves a problem", `O(n^r)` and "solved in time" with Lean's
core library.  The statements on the reductions and the statements about programs use definitions of
their own, with Mathlib.  This file proves that the two definitions of each notion agree.

* Exact Triangle and the (min,+)-product: the two texts unfold to the same proposition.
* APSP: a path is a walk of finite weight (`exists_walk_of_path`, `path_of_walk`).  So the least
  weight of a path is the least weight of a walk (`isLeast_walkWeight_of_path`), and where there is
  no path every walk has weight `⊤` (`isLeast_walkWeight_of_no_path`).
* The weight of a clique: the two sums run over the same pairs of parts, in another order.
* "A program solves a problem": the two forms name the same word sizes and the same output cells
  (`output_cons`).
* `O(n^r)`: from `T(n)^q ≤ K n^p` follows `T(n) ≤ (K + 1) n^{p/q}` (`le_mul_rpow_of_pow_le`), and a
  bound for all large `n` is a bound from `n = 2` on, with a larger constant.
* "Solved in time": one direction is `SolvedInTime.endStatement`.  For the other, a step bound with
  `T(n)^q ≤ K n^p` from `n = 2` on is at most `(K + 1 + T(0) + T(1)) (n^{p/q} + 1)` at every `n`
  (`le_stepBound_of_bigO`).  The program and the slope of the word size stay the same.


 ## Exact Triangle and the (min,+)-product 

### `agreement_exactTriangle`

 Exact Triangle: `EndStatement.ExactTriangle`, on the three matrices of weights of `T`, asks
whether `T` has a zero triangle. 

### `agreement_minPlusProduct`

 The (min,+)-product: the output cells are right for `EndStatement.MinPlusProduct` exactly if,
read row by row as a matrix, they are the (min,+)-product in the sense of `IsMinPlusProduct`. 

 ## APSP 

### `elim_eq_toTop`

 A missing edge as `⊤`, written with `Option.elim` and with `toTop`. 

### `agreement_apsp_noNegativeCycle`

 APSP, the promise.  A missing edge is `none` in `EndStatement.APSP` and `⊤` in
`NoNegativeCycle`.  No closed `EndStatement.Path` has negative weight exactly if `NoNegativeCycle`
holds. 

### `isLeast_walkWeight_of_path`

 The weight of a lightest path is the least weight of a walk. 

### `isLeast_walkWeight_of_no_path`

 Where there is no path, the walk along the missing edge has weight `⊤`, and so has every other
walk. 

### `output_apsp_iff`

 The output condition of `EndStatement.APSP`, for every pair of vertices. 

### `agreement_apsp_output`

 APSP, the output.  The output cells are right for `EndStatement.APSP` exactly if the first cell
of every pair of vertices holds 0 or 1, and the matrix that has the second cell where the first
holds 1, and `⊤` elsewhere, is the distance matrix in the sense of `IsDistanceMatrix`. 

 ## A matrix row by row, and the weight of a clique 

### `agreement_rowByRow`

 A square matrix written row by row: `EndStatement.rowByRow` and `rowMajor` give the same
list. 

### `agreement_cliqueWeight`

 The weight of a `k`-clique: the sum in `EndStatement.ZeroWeightKClique` is `cliqueWeight`, for
every choice `v` of one vertex in each part.  So that problem asks whether some clique has
`cliqueWeight` 0. 

 ## `O(n^r)`, solving a problem, and solved in time 

### `le_mul_rpow_of_pow_le`

 From `t^q ≤ K n^p` follows `t ≤ (K + 1) n^{p/q}`. 

### `agreement_bigO`

 `T(n) = O(n^r)`, for a rational exponent `r ≥ 0`: `EndStatement.BigO` says the same as
`IsBigOPow`. 

### `le_stepBound_of_bigO`

 A step bound that is `O(n^r)` in the sense of the end statement is at most a constant times
`n^r + 1` at every size, in the form that `SolvedInTimeAt` has for `e = 0`. 

### `agreement_solves`

 "A program solves a problem".  `Problem`, `Admissible`, `output` and `Solves` are the form for
problems with several sizes.  Write a problem `Q` of `EndStatement.lean` in this form: the instances
are those whose numbers have absolute value at most `n^κ`, the size is the one parameter of the word
size and stands in front of the input, and a right answer is a right verdict and a right output.
Then `Solves` says the same as `SolvesWithin`, which is stated through
`EndStatement.Problem.SolvedBy`. 

### `agreement_solvedInTime`

 "Solved in time `O(n^r)`", for a rational exponent `r ≥ 0`: `EndStatement.Problem.SolvedInTime`
says the same as `SolvedInTime` with the real exponent `r` and no logarithmic factor. 
