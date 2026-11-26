---
{
  "module": "proof/variables/VariableBound/Search/Correct.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Search/Correct.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Search/Correct.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 2 of Appendix D as a program: the search is right

Proves `VariableBound.StSearchD`.

* Lists of numbers against sets: load(E) is the number of lists that contain E (`load_chksD`), Σ_E
  2^load(E) is `loadSum` (`sum_load`), a list of distinct numbers below m has as many members as its
  set (`card_setD`).
* Υ(𝓛) is `upsNum` over a positive denominator that depends only on the number of checks (`ups_eq`),
  so the candidates of one round compare by `upsNum` as by Υ.
* `argminD` returns a member of the list with the smallest key (`argminD_spec`).
* Every list that the loop passes through consists of candidates and is reached in the sense of
  `AppVariables.Reached` (`Inv`); by the bounds of Step 2 on a list of checks
  (`VariableBound.stepChoice`) it, and it with one more candidate if X > 0, has `StructD`, so `evX`
  is only asked where it is right (`round_inv`), and the cut-off by the pad does nothing, because
  the word of such a list fits under it (`fold_inv`).
* After j rounds, X = 0 or the list has j checks (`fold_inv`); a reached list of r̄ checks has X = 0. 

 ### Lists of numbers and sets of clauses 

### `chksD_append`

 The list (𝓛, l) of lists of numbers is the list (𝓛, Γ) of sets. 

### `length_chksD`

 The two forms of a list of checks have the same length. 

### `load_chksD`

 load(E) is the number of lists that contain the number of E. 

### `sum_map_range`

 The sum of a list of values at 0, …, m − 1 is the sum over `Fin m`. 

### `sum_load`

 Σ_E 2^load(E) is `loadSum`. 

### `card_setD`

 A list of distinct numbers below m has as many members as its set of clauses. 

 ### Υ as a fraction 

### `den`

 The denominator of Υ for a list of r checks. 

### `den_pos`

 The denominator is positive, for n̄ ≥ 1. 

### `ups_eq`

 Υ(𝓛) is `upsNum` over the denominator, for n̄ ≥ 1. 

 ### The first member with the smallest key 

### `stepD`

 One step of `argminD`, written with `Option.elim`. 

### `argminD_eq`

 `argminD` is the fold of `stepD`. 

### `fold_stepD`

 The fold of `stepD` from a pair (l₀, key l₀) ends in a pair (l, key l), where l is l₀ or a
member of the list, and key l is at most key l₀ and at most the keys of all members. 

### `argminD_spec`

 On a list that is not empty, `argminD` returns a member with the smallest key. 

 ### The loop 

### `Inv`

 What holds of every list the loop passes through: its checks are candidates, and as a list of
sets it is reached by the algorithm of Step 2 of Appendix D (`Reached`). 

### `Hyp`

 The hypotheses of `StSearchD` on the parameters and on the candidates. 

### `structD_of`

 Under `Hyp`, the bounds of Step 2 on the number of checks, their sizes and the loads pass from
sets to lists of numbers, for a list of candidates. 

### `structD_inv`

 The bounds of Step 2 on a list of checks, first case, under `Hyp`: a list with `Inv`. 

### `structD_more`

 The bounds of Step 2 on a list of checks, second case, under `Hyp`: a list with `Inv` and X > 0,
and one more candidate. 

### `round_inv`

 Under `Hyp`, one round keeps `Inv`; it leaves a list with X = 0 as it is and makes a list with X >
0 longer by one check. Here `evX` returns X(𝓛) on every list with these bounds (`StructD`). 

### `fold_inv`

 Under `Hyp`, after j rounds the list has `Inv`, and X = 0 or it has j checks. Here `evX` returns
X(𝓛) on every list with these bounds (`StructD`), and the word of every such list fits under the
pad. 

### `stSearchD`

 Step 2, the algorithm as a program: under the hypotheses listed at `StSearchD`, the list that
`searchD` finds has the bounds of Step 2 (`StructD`) and X = 0. 
