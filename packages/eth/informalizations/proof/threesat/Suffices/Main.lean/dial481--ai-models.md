---
{
  "module": "proof/threesat/Suffices/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Suffices/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Suffices/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The reduction to sparse formulas by Lemma 4 with ε = δ/3 (deciding form)

The sentence of the proof of Theorem 2, with both of its printed clauses: the machine for sparse
formulas is asked to work only for m ≤ Mn clauses, and it may take «a polynomial in n» more.
`stSufficesOf` proves it from its three hypotheses. The run of lines 1 to 4 of Algorithm 1
(`StLoopRuns`) is applied with t = ⌈A·2^{δn/3} + A(n+1)^A⌉: every formula that Lemma 4 produces is a
3-CNF on the same n variables with at most M·n clauses (field `sparse`), so the machine for sparse
formulas answers on it within t steps, because δ'·m ≤ δ'·M·n = δn/3.
The answer is right because φ is satisfiable if and only if at least one of them is (field `sat`).
There are at most 2^{δn/3} formulas (field `few`), so the count of the total time (`StTotal`) gives
c·2^{δn} steps. A formula with an empty clause is answered «unsatisfiable» at once.
`stPrintedGivesSparse`: the printed property gives the property `Eight.SufficesSparse`, on which the
proofs of Theorem 2 in this development stand. 

### `stSufficesOf`

 **By Lemma 4 with ε = δ/3, it suffices to decide whether a 3-CNF Φ with m ≤ Mn clauses is
satisfiable, in time O(2^{δ'm}) plus a polynomial in n (the deciding form of the paper's sentence,
which counts)** (proof of Theorem 2), from the run of the loop, the count of the total time and the
polynomial-time steps of the loop. 

### `stSuffices`

 **By Lemma 4 with ε = δ/3, it suffices to decide whether a 3-CNF Φ with m ≤ Mn clauses is
satisfiable, in time O(2^{δ'm}) plus a polynomial in n (the deciding form of the paper's sentence,
which counts)** (proof of Theorem 2), for every enumeration for ε = δ/3: its constant M, and lines 1
to 4 of Algorithm 1 with its parameter τ. 

### `stPrintedGivesSparse`

 The printed sentence, «… with m ≤ Mn clauses …, in time O(2^{δ'm}) plus a polynomial in n»,
gives the property used elsewhere in this development: a machine that works for every number of
clauses, with no polynomial added, does what the deciding form of the printed sentence asks. 
