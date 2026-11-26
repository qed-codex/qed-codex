---
{
  "module": "proof/rates/ClauseBound/ParityChecks/Shape.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Shape.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Shape.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The three layers of a state

In a state of the choice of the checks the network of marks is fed with three layers of clauses on n +
r variables: the clauses of ψ, the incidences, and the clauses not yet decided. This file
proves what the evaluation needs of them (`stShape`): every clause has 1 to k + 1 literals on these
variables; no variable occurs in too many clauses; there are not too many clauses. A variable
of ψ occurs in at most Δ clauses of ψ, and in the incidences of these clauses, of which each clause
has as many as there are checks that contain it; a dummy variable occurs in the incidences of its
check. The numbers of checks that contain a clause, of clauses of a check and of all incidences are
bounded in every state that is tried (`Tent`); the bounds are turned into natural numbers with
(1 + 1/nb)^(2·nb) ≤ 8. 

 ### Powers of 1 + 1/nb 

### `pr_nonneg`

 `pr nb` = 1/nb ≥ 0 (this is not the p of Appendix D of the paper). 

### `pow_two_mul_le`

 (1 + 1/nb)^(2·nb) ≤ e² ≤ 8. 

### `pow_le_two_pow`

 (1 + 1/nb)^N ≤ 2^(⌊3N/(2·nb)⌋ + 1). 

### `le_of_two_pow_lt`

 From 2^c < 16·a·(1 + 1/nb)^N: c ≤ ⌈log₂(16a)⌉ + ⌊3N/(2·nb)⌋. 

 ### Counting in lists 

### `hasV`

 Does the variable v occur in the clause C? 

### `occ_eq`

 The clauses in which v occurs. 

### `hasV_append_singleton`

 A literal more. 

### `hasV_eq_false`

 A variable that is not among those of C does not occur in C. 

### `countP_eq_card`

 The members with a property of a list without repetition of numbers below m, counted as a set. 

### `length_filter_eq_card`

 The clauses with a property, counted by their numbers. 

### `length_filter_flatMap_range`

 The members with a property of a list that is put together from pieces number 0, …, j − 1. 

### `length_flatMap_range`

 The same for the whole list. 

### `card_lam`

 A check as a set has as many members as the list. 

### `getD_ok`

 Every entry of the list of checks, also beyond its end, is a list without repetition of numbers
of clauses. 

### `length_le_of_nodup`

 A list without repetition of numbers below m has at most m members. 

 ### The three layers 

### `getD_lt`

 The variables of the clause number x of ψ are below n. 

### `wfL`

 Every clause of the three layers has 1 to k + 1 literals on the n + r variables. 

### `length_occ_incL`

 The incidences in which v occurs, check by check. 

### `card_col_le`

 The number of the checks 0, …, j that contain the clause x. 

### `occ_incL_le_of_lt`

 A variable of ψ occurs in at most Δ·(⌈log₂(16m)⌉ + ⌊3r/(2·nb)⌋ + 1) incidences. 

### `occ_incL_le_of_ge`

 A dummy variable occurs in at most ⌈log₂(16r)⌉ + ⌊3m/(2·nb)⌋ incidences. 

### `length_incL`

 The number of incidences. 

### `length_incL_le`

 There are at most 16·Δ·LD Δ·r + m incidences, if m ≤ 2·Δ·LD Δ·nb. 

### `le_mul_LD`

 Δ ≤ Δ·LD Δ. 

### `shape_core`

 The shape of the three layers, with the bounds as they come out of the state. 

### `stShape`

 The layers of a state that is tried have the shape that the evaluation asks. 
