---
{
  "module": "proof/sparsification/SparsificationLemma/Mach/Walk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Mach/Walk.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Mach/Walk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The walk that collects the outputs

Definitions: the walk `walkL`, which makes one round of the depth-first walk
`Groundwork.Sparsify.round` for each unit of a pad and replaces a state whose word is longer than
the pad by the empty state (`cap`); the code `codeP`, which is `code` with
every unary number cut off at the length of the pad (a variable is a natural number written in
binary, and writing it in unary can take exponentially long, so `code` itself is not polynomial-time
on all lists of formulas); the function `BL` of (input, pad) that writes the outputs; and
the exponent `eL` of the length of the pad.
Theorems, for every step function: the number of nodes on the stack and in the list of results
together never decreases in a round, so it is at most the number of leaves (`total_le_leaves`); what
holds of all
nodes that are ever on the stack holds of all results (`out_of_stack`). Then `walkL_eq`: if the pad
has at least 2·(number of leaves) − 1 units and every state fits under it, `walkL` returns the
leaves. 

 ### Definitions 

### `walkL`

 The depth-first walk of the tree for width k with the thresholds `thetaU τ`, one round for each
unit of the pad; it returns the nodes at which the procedure stops, from left to right. 

### `codeNatP`

 `codeNat`, cut off at the length of the pad. 

### `codeLitP`

 `codeLit`, with the variable cut off at the length of the pad. 

### `codeClP`

 `codeCl`, with the variables cut off at the length of the pad. 

### `codeFmlP`

 `codeFml`, with the variables cut off at the length of the pad. 

### `codeP`

 `code`, with the variables cut off at the length of the pad. 

### `sL`

 The precision written in the input 1^s 0 1^k 0 …. 

### `kL`

 The width written in the input. 

### `dL`

 The number of variables, in unary, and the formula written in the input. 

### `eL`

 The exponent of the length of the pad: ⌊n/2^s⌋ + k + 3·(number of binary digits of the length of
the input) + 9. 

### `BL`

 The function of (input, pad): the code of the list of outputs, if the pad is long enough. The
width is cut off at ⌊log₂(length of the pad)⌋, so that 2^k can be written in unary on every input. 

### `nodeLen`

 An upper bound for the length of the word of a node: a formula of at most 2^k·m clauses of at
most k literals and a side list of at most 2n clauses of at most 2 literals, all on variables below
n. 

 ### The walk, for every step function 

### `total_le_round`

 A round does not decrease the number of nodes on the stack and in the list of results together. 

### `total_mono`

 The same for any number of further rounds. 

### `total_le_leaves`

 After any number of rounds, the stack and the list of results together have at most as many
nodes as there are leaves. 

### `out_of_stack`

 What holds of all nodes that are ever on the stack holds of all results: a result was on the
stack one round before. 

### `walkL_eq`

 If the pad has at least 2·(number of leaves) − 1 units and the word of every state of the walk
is no longer than the pad, then `walkL` returns the leaves. 
