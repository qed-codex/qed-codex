---
{
  "module": "proof/consequences/SplitCount/Sizes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Sizes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Sizes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Small facts for proof/consequences/SplitCount/

Bounds on `size` (the measure of the states of a machine cut into steps) of lists, formulas, numbers
in unary, words and nodes of the tree; `cntN n x ≤ 2^n`; the output function `outW` writes
`SatK.binary`; two inequalities between polynomials.
The same facts are proved, as private theorems that an importing file cannot use, in
proof/machines/StepMachines/Prog/Sat.lean, proof/consequences/WidthK/Top/Sat.lean and
proof/consequences/CountKSat/Top/Count.lean. 

### `size_list_le`

 A list of at most k entries of size at most s has size at most k(s+1) + 1. 

### `size_lit_le`

 A literal on a variable below n has size at most n + 2. 

### `size_fml_le`

 A formula of at most m clauses of at most k literals with variables below n has size at most
m(k(n+3)+2) + 1. 

### `size_unary`

 The size of n in unary is at most 2n + 1. 

### `size_binary`

 The size of a word of n + 1 bits is at most 2(n+1) + 1. 

### `size_nat_le`

 A number below 2^B has size at most B + 1. 

### `size_node_le`

 The size of a node of the tree, from bounds on the formula that is counted at it. 

### `cntN_le`

 There are at most 2^n satisfying assignments on x₀ … xₙ₋₁. 

### `cntN_of_nil`

 A formula with an empty clause has no satisfying assignment. 

### `toWord_eq`

 The ℓ-bit word of y lists the bits 0, …, ℓ − 1 of y. 

### `outW_eq`

 The output function of the machine writes the word of the statement: v in n + 1 bits. 

### `poly_le`

 For s ≥ 1: if x ≤ B·s^d + A·(P·s^e)^A then x ≤ c·s^c with c = B + d + A·P^A + e·A. 
