---
{
  "module": "proof/threesat/Printed/Achievable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/Achievable.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/Achievable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Around Definition 4

The sentences that the paper prints with Definition 4, for `Printed.Achievable`
(PrintedStatement.lean), in which own steps and queries are counted once each.
* `stMono`: «If (K, e) is achievable, so is (K, e₁) for every e₁ ≥ e.»
* `stBrute`, `stHalf`: «Trying all 2^{λK(K−1)/2} choices of one string per edge shows that (K, ½) is
  achievable for every K, so e* ≤ ½.» The count is not made again: with the tables built in,
  `bruteMachine K` is the step machine `Groundwork.brute` of this development on a procedure that
  answers in one step (`bruteMachine_close`), `Groundwork.Prog.bruteE_correct` bounds its steps, and
  `QueryMachines.stClose` reads that number as own steps plus queries.
* `stAnswerEachQuery`: the step that the proof of Lemma 1 makes with Definition 4.
* `eStar_le`, `eStar_nonneg`, `achievable_of_eStar_lt`: what an infimum gives, for the proof of
  «Hence e* = 0». 

 ### Monotone in e 

### `AchievedBy.mono`

 The same machine and the same constant do for every larger e. 

### `stMono`

 «If (K, e) is achievable, so is (K, e₁) for every e₁ ≥ e.» 

 ### The input in unary, and the answers of the tables 

### `length_unary`

 The number n in unary has n units. 

### `size_unary`

 The number n in unary has size 2n + 1. 

### `tables_eq_some`

 The tables answer only the queries of Definition 3, and with the entry. 

 ### Brute force 

### `bruteMachine_poly`

 Brute force has polynomial-time steps. 

### `bruteMachine_achieves`

 «Trying all 2^{λK(K−1)/2} choices of one string per edge»: brute force does what Definition 4
asks for (K, ½). 

### `stBrute`

 «(K, ½) is achievable», by brute force. 

 ### e* 

### `achievable_half`

 «(K, ½) is achievable for every K». 

### `half_mem`

 ½ is one of the numbers of which e* is the infimum. 

### `nonneg_of_mem`

 All of these numbers are at least 0, since e ≥ 0 is a part of Definition 4. 

### `eStar_le`

 If (K, e) is achievable for infinitely many K, then e* ≤ e. 

### `eStar_nonneg`

 0 ≤ e*. 

### `achievable_of_eStar_lt`

 If e > e*, then (K, e) is achievable for infinitely many K. 

### `stHalf`

 «… shows that (K, ½) is achievable for every K, so e* ≤ ½.» 

 ### «Answer each of its at most … queries by computing the entry» 

### `stAnswerEachQuery`

 The machine of Definition 4 asks at most as many queries as it takes operations; and with each
query answered by a step machine within t steps it takes at most 3·t times as many steps (t + 2 ≤ 3t
steps for a query, one for an own step). 
