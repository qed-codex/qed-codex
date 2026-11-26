---
{
  "module": "ThreeSumApsp/Machine/Solving.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Machine/Solving.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Machine/Solving.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The notions of solving are monotone

That the program `P` with slope `b` solves the problem on the instances in `dom` within time `T`, at
every admissible word size, stays true for a larger slope, a smaller set of instances and a larger
time bound (`Solves.mono`).  The same holds for a two-stage data structure (`IsDataStructure.mono`).

* The item statements on the problems of the end statement use `SolvesWithin`.  It is `Solves` for
  the problem `ofEnd Q`, whose instances carry their size and a bound on their numbers
  (`solvesWithin_iff`, `solvedInTimeAt_iff`).

* A statement "there are a program and a constant `C` such that the time is at most `C f(x)`" stays
  true for every bound `g` with `f = O(g)`: `exists_solves_of_dominated`, and
  `exists_isDataStructure_of_dominated` for a data structure.
* For the bounds `O(n^a (log n)^e)` in one size: a larger exponent (`SolvedInTime.mono_exponent`),
  and a larger exponent that absorbs the logarithms (`SolvedInPolylogTime.solvedInTime`).


 ## The problems of the end statement as problems in the sense of `Problem` 

### `Bounded`

 An instance of a problem of the end statement, with its size `n` and a bound `U` on its
numbers. 

### `Bounded.n`

 The size. 

### `Bounded.U`

 The bound on the absolute values of the numbers of the input. 

### `Bounded.x`

 The instance. 

### `Bounded.bounded`

 The numbers are bounded. 

### `Bounded.abs_le`

 The numbers of the input of a bounded instance are within the bound. 

### `ofEnd`

 A problem of the end statement as a `Problem`, read as `EndStatement.Problem.SolvedBy` reads it:
the size is the one parameter of the word size, it stands in cell 0 in front of the input, the
verdict has to be `accept` exactly if the answer is yes, and the output has to be right. 

### `output_cons`

 `EndStatement.Problem.SolvedBy` counts the output cells as `1 + len + i`, and `output` counts
them as `(len + 1) + i`. 

### `solvesWithin_iff`

 `SolvesWithin` is `Solves` for the problem `ofEnd Q`, on the instances with `U = n^κ`. 

### `solvedInTimeAt_iff`

 `SolvedInTimeAt` in terms of `Solves`. 

 ## Monotonicity 

### `Solves.mono`

 `Solves` stays true for a larger slope, a smaller set of instances and a larger time bound. 

### `IsDataStructure.mono`

 `IsDataStructure` stays true for a larger slope, a smaller set of instances and larger
bounds. 

 ## Bounds up to a constant 

### `exists_solves_of_dominated`

 A program that solves a problem in time `O(f)` solves it in time `O(f')` if `f = O(f')`. 

### `exists_isDataStructure_of_dominated`

 A data structure with the bounds `O(f)`, `O(f)`, `O(g)` is one with the bounds `O(f')`, `O(f')`,
`O(g')` if `f = O(f')` and `g = O(g')`. 

 ## Bounds in one size 

### `SolvedInTimeAt.of_eventually_le`

 The bound `O(n^a (log n)^e)` may be replaced by a bound `O(n^a' (log n)^e')` that is at least as
large, up to a constant, for all large `n`. 

### `SolvedInTime.mono_exponent`

 A bound `O(n^a (log n)^e)` is a bound `O(n^a' (log n)^e)` for `a ≤ a'`. 

### `SolvedInTime.solvedInPolylogTime`

 A bound `O(n^a (log n)^e)` is a bound `O(n^a (log n)^{O(1)})`. 

### `SolvedInPolylogTime.solvedInTime`

 A bound `O(n^a (log n)^{O(1)})` is a bound `O(n^a')` for `a < a'`. 
