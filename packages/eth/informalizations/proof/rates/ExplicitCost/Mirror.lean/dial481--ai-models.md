---
{
  "module": "proof/rates/ExplicitCost/Mirror.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/Mirror.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/Mirror.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A machine that runs step for step as another, on a wider input

Let w : α → α' widen the input (for instance: put K and g, in unary, beside it).
`Follows M M' w d φ` says that the map φ from the states of M to the states of M' carries the run of
M on a to the run of M' on w a: it commutes with `init`, `step` and `resume`, keeps `out` and `ask`,
and makes a state larger by at most d.
`Mirrors M M' w d` says that there is such a map. Then every run of M on a is a run of M' on w a
with the same result, the same number of own steps and the same list of queries, on states larger by
at most d (`Mirrors.runs`).
For each way to build machines of proof/machines/QueryMachines/CombDefs.lean that the programs of
the proof of Lemma 1 use there is one lemma: if the parts mirror each other, and the plain functions
agree along w, then so do the machines built. The number d is counted along: a construction that
keeps the input in its state (`bind`, the loops) adds the growth of the input. 

### `Follows`

 φ carries the runs of M on a to the runs of M' on w a; states grow by at most d. 

### `Mirrors`

 M' on w a runs step for step as M on a; states grow by at most d. 

### `Follows.reaches`

 A run from s gives a run from φ s. 

### `Mirrors.runs`

 **The same result, own steps and queries**, on states larger by at most d. 

### `Mirrors.within`

 The same in costs. 

### `Mirrors.mono`

 The bound on the growth may be raised. 

 ## One lemma for each construction 

### `mirrors_query`

 One query. 

### `mirrors_const`

 A constant. 

### `Mirrors.mapIn`

 A function applied to the input. 

### `Mirrors.mapOut`

 A function applied to the result. 

### `Mirrors.branch`

 A choice between two machines. 

### `Mirrors.ite`

 A choice by a test. 

### `Mirrors.bind`

 One machine after the other. The first part runs beside a copy of the input. 

### `Mirrors.foldWhile`

 The loop. The body runs beside the point of the loop, which holds a copy of the input. 

### `Mirrors.foldRange`

 The loop over a range. 

### `Mirrors.sumRange`

 The sum over a range. 

### `Mirrors.prodRange`

 The product over a range. 

### `Mirrors.gated`

 A machine behind a test. The test runs beside a copy of the input. 
