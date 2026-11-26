---
{
  "module": "ThreeSumApsp/Sec3/Theorem21b/PathsAndWalks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21b/PathsAndWalks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21b/PathsAndWalks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Paths of the end statement and walks with weights in `WithTop ℤ`

The end statement speaks of a directed graph as a function into `Option ℤ` and of
`EndStatement.Path`, an inductive predicate.  The definitions for APSP in `PaperStatements.lean`
speak of weights in `WithTop ℤ`, of walks as lists of vertices, and of `IsDistanceMatrix`.  This
file shows that the two agree.

* A missing edge is the weight `⊤` (`toTop`).
* A path of weight `d` is a walk of weight `d`, and a walk of finite weight is a path
  (`exists_walk_of_path`, `path_of_walk`).
* So "no negative cycles" carries over (`noNegativeCycle_toTop`), and a distance matrix has `⊤`
  where there is no path and the least weight of a path elsewhere (`not_path_of_dist_eq_top`,
  `isLeast_path_of_dist_eq_coe`).
* `reachable_or_not` says this of two numbers that are written down for a pair of vertices, and
  `output_apsp` is the output condition of `EndStatement.APSP`.


### `toTop`

 An optional weight, as a weight or `⊤`. 

### `exists_walk_of_path`

 A path of weight `d` is a walk of weight `d`. 

### `path_of_walk`

 A walk of finite weight `d` is a path of weight `d`. 

### `noNegativeCycle_toTop`

 No closed path of negative weight: no closed walk of negative weight. 

### `dist_le_of_path`

 The distance is at most the weight of every path. 

### `not_path_of_dist_eq_top`

 Where the distance is `⊤` there is no path. 

### `isLeast_path_of_dist_eq_coe`

 A finite distance is the weight of a path, and no path is lighter. 

### `reachable_or_not`

 Two numbers written down for the pair `(i, j)` as APSP asks: 0 if the distance is `⊤`, and 1 and
the distance otherwise.  Then either the first is 1 and the second is the least weight of a path, or
the first is 0 and there is no path. 

### `output_apsp`

 The output condition of `EndStatement.APSP` is the either-or of `reachable_or_not` for every
pair of vertices. 
