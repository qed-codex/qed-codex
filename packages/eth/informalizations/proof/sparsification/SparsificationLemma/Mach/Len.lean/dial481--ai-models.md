---
{
  "module": "proof/sparsification/SparsificationLemma/Mach/Len.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Mach/Len.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Mach/Len.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The function of (input, pad) writes the outputs

`BL_eq`: on the input 1^s 0 1^k 0 code(φ), with k ≥ 1, s ≥ `s0U k` and φ a k-CNF without an empty
clause, and with the pad of 2^(eL …) units, `BL` is the code of the list of outputs for τ =
2^(4s+17).
The steps:
* `len_node_le`, `len_state_le`: a node that is ever on the stack has a word of length at most
  `nodeLen k n m`, m the number of clauses of φ (`UniformInK.StTreeU` bounds these nodes), and the
  stack and the list of results together never hold more nodes than the tree has leaves
  (`total_le_leaves`, proof/sparsification/SparsificationLemma/Mach/Walk.lean). So if L bounds the
  number of leaves, the word of a state has length at most L·(nodeLen k n m + 2) + 6.
* `map_walkL`: under a pad of this length the walk returns the leaves of the tree whose side list
  starts with the clauses xᵢ ∨ ¬xᵢ; their outputs are those of the tree that starts with the empty
  side list (`StOutputsSame`).
* `pad_enough`: 2^(eL …) units suffice for L = 2^(⌊n/2^s⌋+1), which bounds the number of leaves by
  `UniformInK.StLeavesU`, because k, n and m are at most the length of the input.
* `codeP_eq`: the variables of the outputs are below n, so the cut-off in the code does nothing. 

 ### The length of the word of a state 

### `len_node_le`

 The word of a node with the bounds of `UniformInK.StTreeU` has length at most `nodeLen k n m`. 

### `len_state_le`

 The word of a state with at most L nodes, each with a word of length at most b, has length at
most L·(b + 2) + 6. 

 ### The walk returns the outputs 

### `map_walkL`

 For k ≥ 1, τ ≥ k², τ ≥ 8k and a k-CNF ψ on n variables: if L is at least Σ_{j ≤ kn/τ} C(bsumU τ
k · n, j), which bounds the number of leaves, and the pad has at least 2L − 1 units and at least
L·(nodeLen k n m + 2) + 6 units, m the number of clauses of ψ, then the walk returns nodes whose
outputs are `outTau k n τ ψ`, and every variable of the outputs is below n. 

 ### The code 

### `codeNatP_eq`

 The cut-off does nothing to a number that is at most the length of the pad. 

### `codeP_eq`

 The cut-off does nothing to a list of formulas whose variables are at most the length of the
pad. 

 ### Reading the input 

### `dec_encIn`

 From 1^s 0 1^k 0 code(φ) the function reads s, k, n and φ. 

### `length_encIn`

 The input has s + k + n + 3 + m·k·(⌊log₂ 2n⌋ + 1) symbols, m the number of clauses of φ. 

### `eL_encIn`

 The exponent of the pad on the input 1^s 0 1^k 0 code(φ). 

### `isKCNF_toN`

 A k-CNF without an empty clause, read with natural numbers as variables, is a k-CNF on n
variables. 

 ### The pad is long enough 

### `pad_enough`

 2^(a + k + 3·size N + 9) units suffice for 2^(a+1) nodes, if k, n and m are at most N. 

 ### The function writes the outputs 

### `BL_eq`

 On 1^s 0 1^k 0 code(φ), for k ≥ 1, s ≥ `s0U k` and φ a k-CNF without an empty clause, and with
the pad of 2^(eL …) units, `BL` is the code of the list of outputs for τ = 2^(4s+17). 
