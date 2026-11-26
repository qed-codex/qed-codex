---
{
  "module": "proof/consequences/SplitSat/Walk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitSat/Walk.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitSat/Walk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 5: s_3 = 0 implies s_k = 0 for every k ≥ 3, by the reduction that sparsifies and then splits every long clause into clauses of 3 literals with new variables, for machines cut into steps

`reduceCore_decides` holds for every step of a tree that sparsifies width k from the root `rootP`;
`stReduceCore` (= `SplitSat.StReduceCore`) is the case of the procedure behind the Lean form of
Lemma 4, run at width k.
The proof follows `Groundwork.Prog.SatTopK.sat_correct` (proof/consequences/WidthK/Top/Sat.lean)
with three changes. The nodes carry n in unary. There is no reader of the input, so all sizes are
bounded in n + 2; this uses that no clause is written twice. The cost of a leaf is given in n:
by `stLeaf` the 3-CNF of a leaf has N ≤ (1 + (k−3)·B)·n variables, so the procedure D takes at most
c·2^{δ₃N} ≤ c·2^{(δ/3)n} steps on it. There are at most 2^{(δ/3)n} leaves, so the walk takes at most
(c+2)·2^{(2δ/3)n} steps. 

### `reduceCore_decides`

 **The reduction is correct and fast, for every procedure D and every tree.** Let k ≥ 3 and δ >
0; let `step`, from the root `rootP`, sparsify width k with at most 2^{δn/3} leaves of at most B·n
clauses; let D decide 3-SAT with an exponent δ₃ ≥ 0 such that δ₃·(1 + (k−3)·B) ≤ δ/3. Then
`reduceCore step D` decides k-SAT with the exponent δ, in the sense of `DecidesW k`. 

### `stReduceCore`

 **The reduction is correct and fast, for every procedure D**, on the tree of the procedure
behind the Lean form of Lemma 4, run at width k: the statement `SplitSat.StReduceCore`. 
