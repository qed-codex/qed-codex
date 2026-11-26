---
{
  "module": "proof/consequences/CountKSatRate/Cert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Cert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Cert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial-time lemmas (`PolyT`) for functions of `proof/consequences/CountKSatRate/Defs.lean`,
for every width k: one step of the counting tree with the threshold τ as data, one round of the walk
that
adds up and the walk itself, the formula of a node, the decoded input and the number of variables
written in it, exhaustive counting `bruteN k`, and the number of the padded input
with its value function as an arbitrary function of a context. The interface statement proved is
`StCertWalkS` of `proof/consequences/CountKSatRate/Interfaces.lean`. 

### `polyT_stepCU`

 The two children of a node of the counting tree, jointly in τ and the node. 

### `roundS_eq`

 `roundS` with its case distinctions written by eliminators. 

### `polyT_roundS`

 One round of the walk that adds up is polynomial-time, for a step function and a value function
that may depend on the context. 

### `leafM_polyT`

 The formula of a node as `countM` gets it is computed in polynomial time. 

### `numC_polyT_aux`

 The number of the padded input, with the decoded input d, the pad, the threshold τ and the value
function as arbitrary functions of a context. 

### `bruteN_polyT_aux`

 The number `bruteN k` with the decoded input d and the pad as arbitrary functions of a context. 

### `stCertWalkS`

 The walk that adds up is polynomial-time jointly in the pad, τ, the root and whatever the value
function depends on. 

### `Cert.decU_pad_polyT`

 The decoded input is polynomial-time in the padded input. 

### `Cert.nK_unary`

 The number of variables written in the input is at most the length of the input, and
polynomial-time. 

### `Cert.bruteN_polyT`

 Exhaustive counting with fuel is polynomial-time. 
