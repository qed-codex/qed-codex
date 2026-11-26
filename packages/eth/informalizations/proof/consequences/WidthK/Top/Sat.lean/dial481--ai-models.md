---
{
  "module": "proof/consequences/WidthK/Top/Sat.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/WidthK/Top/Sat.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/WidthK/Top/Sat.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 k-SAT in c·2^{δn} steps as a program: decode the input, walk the sparsification tree
depth-first, test every leaf.

This file follows `proof/machines/StepMachines/Prog/Sat.lean` (the same for 3-SAT) line by line,
with the width 3 replaced by k ≥ 1. The decoder, the step and the
root of the tree are parameters here; what is needed of the last two is the definition `Sparsifies`.
The result is `sat_correct`. 

### `decF`

 The formula written in the input, as read by `dec`. 

### `satMK`

 The k-SAT machine: decode the input by `dec`, answer false if there is an empty clause,
otherwise walk the tree of `step` from `root`
and answer true iff some leaf passes the test. M is the test of a leaf (a count that is positive iff
the leaf is satisfiable). 

### `Sparsifies`

 `step` and `root` sparsify width k. For ψ with variables below n and nonempty clauses of at most
k literals, the tree of depth Dd·n has at most
2^{εn} leaves, a leaf has at most Bl·n clauses, ψ is satisfied exactly if some leaf is, and after
every round of the walk the stack holds at most
Dd·n + 1 formulas of at most |ψ|·Sk clauses. 

 ### Sizes 

### `size_fml_le`

 A bound on the size of a formula of at most m clauses of at most k literals with variables below
n. 

### `length_enc`

 The length of the code: n + 1 bits for n, then k slots of ⌊log₂(2n)⌋ + 1 bits for every clause. 

### `cOf`

 The constant c of `sat_correct`, from the constants of the three size bounds in its proof and
the constant A of the test of a leaf. 

### `final_bound`

 The sizes that occur in the proof of `sat_correct` are at most c·N^c, where N is the length of
the input plus 1. 

 ### k-SAT in c·2^{δn} steps 

### `sat_correct`

 Let `step`, `root` sparsify width k with at most 2^{δn/3} leaves of at most Bl·n clauses, let
`dec` decode, and let M return, on m clauses of ≤ k
literals, within A·2^{δ'm} steps (δ'·Bl ≤ δ/3) and size A·(size φ)^A, an integer that is positive
iff φ is satisfiable. Then `satMK dec step root M`
decides every encoded k-CNF on n variables within c·2^{δn} steps and within size polynomial in the
length of the input. 
