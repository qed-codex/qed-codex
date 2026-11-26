---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Instances/Classes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Instances/Classes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Instances/Classes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The classes W_ϱ of the pairs (proof of Theorem 17)

"For ϱ ∈ ℤ_p let W_ϱ be the set of edges (a,b) ∈ A × B with w(a,b) ≡ ϱ (mod p)".  (The cutting of
the classes into chunks, with which the sentence goes on, is a routine of its own.)

classes(rab, n, p, cls, cur, qi, qj) sorts the n² pairs (a, b) by the residue of w(a,b), which is in
the cell rab + a n + b, keeping the row-major order within a class: a stable counting sort.  It
writes the rows of the sorted pairs to qi, their columns to qj, and the places where the classes
start to cls.  The row and the column of the current pair are kept in two counters, so that no
division is needed.  `classes_meets` proves this, within `tClasses n p` steps, a number linear in
n² + p.

The routine has five phases.  Between them the state is described by `ClsState`:

* `clsZero_ends`: the counters are cleared;
* `clsCount_ends`: the sizes of the classes are counted;
* `clsPrefix_ends`: prefix sums turn the sizes into the starts;
* `clsCopy_ends`: the starts are copied to cur, the next free places;
* `clsPlace_ends`: each pair goes to the next free place of its class (`ClsPlaced.step` for the
  memory, `clsPlaceOne_ends` for the program), and row and column step to the next pair.

The place of a pair is its place `sortPos` in a stable sort; `getD_sortedIdx` and
`segN_map_sortedIdx` identify what stands there with the lists of the specification.


 ## The pure side: the lists of the specification and the places of a stable sort 

### `clsKey`

 The key of the pair number i. 

### `length_classIdx`

 The size of a class, as a count of keys. 

### `sum_length_classIdx`

 The sizes of the classes before `r` add up to the number of smaller keys. 

### `getD_classStarts`

 An entry of the list of the starts. 

### `getD_sortedIdx`

 The pair number i stands at its place in the list of all the pairs, class after class. 

### `length_sortedIdx`

 All the pairs are listed if all the keys are below `p`. 

### `segN_map_sortedIdx`

 What stands at the places of a stable sort is the list of the pairs, class after class. 

 ## The routine 

### `Rab`

 Local 0 of classes: the address of the residues. 

### `Size`

 Local 1 of classes: the number n of vertices of a part. 

### `Prime`

 Local 2 of classes: the prime p. 

### `Cls`

 Local 3 of classes: the address of the starts of the classes. 

### `Cur`

 Local 4 of classes: the address of the next free places. 

### `Rows`

 Local 5 of classes: the address of the rows of the sorted pairs. 

### `Cols`

 Local 6 of classes: the address of their columns. 

### `Pairs`

 Local 7 of classes: the number n² of pairs. 

### `Idx`

 Local 8 of classes: a counter. 

### `Addr`

 Local 9 of classes: an address. 

### `Row`

 Local 10 of classes: the row of the current pair. 

### `Col`

 Local 11 of classes: its column. 

### `Place`

 Local 12 of classes: its place. 

### `clsZero`

 cls[t] := 0 for t ≤ p. 

### `clsCount`

 cls[rab[i] + 1] += 1 for i < n². 

### `clsPrefix`

 cls[t] += cls[t - 1] for t = 1, …, p. 

### `clsCopy`

 cur[t] := cls[t] for t < p. 

### `clsPlaceOne`

 The pair number i, which is (row, col), goes to the next free place of its class. 

### `clsPlace`

 All pairs go to their places. 

### `classesBody`

 classes(rab, n, p, cls, cur, qi, qj). 

### `tClasses`

 The time of classes. 

### `ClassesArgs`

 The arguments of classes, and the list `RAB` of the residues, which stands at `rab`. 

### `ClassesArgs.vals`

 The values of the arguments of classes. 

### `ClassesArgs.locals`

 The locals of classes: the arguments, the number n² of pairs, and the five that change. 

### `ClassesArgs.Same`

 Only cells of the four areas that classes writes have changed. 

### `ClassesPre`

 What classes assumes: the residues, below p, stand at rab; behind them lie, in this order, the
four areas cls, cur, qi and qj that it writes; everything is inside the memory. 

### `ClassesPre.key_lt`

 The keys are below p. 

### `ClassesPre.read`

 The residues lie before the areas that are written, so they can be read at any time. 

### `ClsState`

 A state of classes between two phases: the locals hold the arguments and n², only the four areas
have been written, and R holds of the memory. 

### `ClsZeroed`

 After the first phase: the counters are 0. 

### `ClsCounted`

 After the second phase: the cell t + 1 holds the size of the class t. 

### `ClsStarts`

 After the third phase: the cell t holds the start of the class t. 

### `clsZero_ends`

 cls[t] := 0 for t ≤ p. 

### `clsCount_ends`

 cls[rab[i] + 1] += 1 for i < n². 

### `clsPrefix_ends`

 cls[t] += cls[t - 1] for t = 1, …, p. 

### `ClsCopied`

 After the fourth phase: cur holds the starts as well. 

### `clsCopy_ends`

 cur[t] := cls[t] for t < p. 

### `ClsPlaced`

 While the pairs are placed, before the pair number i: cls holds the starts, cur the next free
place of each class, and the pairs before i stand at their places. 

### `ClsPlaced.step`

 **The pair number i is placed**: its row and its column are written to its place, and the next
free place of its class moves on. 

### `clsPlaceOne_ends`

 **The pair number i is written to its place.** 

### `clsPlace_ends`

 All pairs go to their places. 

### `classes_meets`

 **classes** writes the starts of the classes and the rows and columns of the pairs, class after
class. 
