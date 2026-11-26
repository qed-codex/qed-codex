---
{
  "module": "proof/rates/ClauseBound/ParityChecks/TopDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/TopDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/TopDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From a clique solver to #k-SAT on n variables, along Appendix D: the function, the exponent of the pad, and the interface lemmas

As in proof/rates/ClauseBound/TopN/Defs.lean (level picked for n^{1/17}, precision s, sparsification
with the threshold 2^{4s+17}, walk through the counting tree), but a leaf is counted by `countOL`.
Two constants have no
explicit value and are parameters: c (the networks are used only if Δ ≤ (⌊log₂ n⌋ + 1)^c) and n₀
(and only if n ≥ n₀). 

### `valO`

 The count of the formula of a node of the counting tree, by `countOL`, with the bound Δ =
2^(betaN k s) on the number of clauses in which one variable occurs. 

### `numOL`

 The number of satisfying assignments of the formula written in p.1, by the walk through the
counting tree. 

### `restO`

 The exponent of a pad that suffices for everything but the networks: the list of profiles, the
lists of the checks, the rounds of the walk, the stack of the walk. 

### `needO`

 The exponent of a pad that suffices for n variables at the index i with precision s. 

### `planAtO`

 The exponent `needO`, if the networks can be used and the exponent is at most n; otherwise
`none`: exhaustive counting is used. 

### `planO`

 The plan for the input x. 

### `eO`

 THE exponent function: the exponent of the plan, or n. 

### `AO`

 THE function: the number of satisfying assignments of the formula written in p.1, in n + 1 bits,
when the pad p.2 is long enough. 

 ### BudgetOL.lean 

### `StBudgetO`

 The budgets other than those of the networks. 

 ### TopOL.lean: correctness, for the n₀ that belongs to c 

 ### CertTopOL.lean 

 ### ArithOL.lean: the exponent is O_k(e·n·(s+1)) 

### `StArithO`

 For a suitable c, and every n₀: with l the level picked for n and s = s(l), the exponent of the
pad is at most A·n·e_l·(s+1). 

 ### EndOL.lean 

### `StEndO`

 The end theorem for the bound in n, along Appendix D, for a solver with a sequence of levels. r
is any function that dominates e_l·(s(l)+1) at the level picked for n and is not too small. 
