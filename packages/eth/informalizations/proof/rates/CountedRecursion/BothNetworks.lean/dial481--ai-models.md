---
{
  "module": "proof/rates/CountedRecursion/BothNetworks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/BothNetworks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/BothNetworks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «Definition 2 holds with B₁ = gB + g²(2λ)^c in the role of B and with τ = 2^{cλ}Ξ^{C₂}»

`bothNetworksFrom : BothNetworksFrom` and `bothNetworks : BothNetworks`, with C₂ = 2c + 6 (proof of
Theorem A (b)). The parts:
* the network is a network with the parameters g³λ and B₁, c_{a,a'} ≤ g²λ, and the input that the
  procedure writes is its input: PatternIs.lean, ParentNumbers.lean;
* every query of Definition 2(iii) that the network answers is answered by the four procedures as
  one machine (`Printed.ProcsQ.answer`): the runs of RowWeightRun.lean, RowPairRun.lean,
  RowFactorRun.lean, whose costs and sizes are explicit;
* `cost_le`, `room_le`: these are at most (2^{cλ} + 2 + tq)·Ξ^{C₂} and Ξ^{C₂}; the size of the
  parent is `size_mkParent_le` (ParentSize.lean). 

 ## The arithmetic 

### `xi_facts`

 What is used of g, λ, B: with Ξ = g²(λ + B). 

### `cost_le`

 The costs of the four procedures are at most (2^{cλ} + 2 + tq)·Ξ^{C₂}. 

### `room_le`

 The sizes of the states of the four procedures are at most Ξ^{C₂}. Here sp is the size of the
parent, sQ that of the query. 

 ## The four procedures as one machine 

### `size_row_le`

 The size of the number of a row is at most g + 1. 

### `size_sq_le`

 The size of the number g². 

### `answer_within`

 **Every query of Definition 2(iii) is answered by the procedures.** 

### `bothNetworksFrom`

 The two networks, assuming that Ψ is the product that `rowPair` computes (used for the run of
`rowPair`) and that the numbers read from the lists are those of the pieces (used for the input that
the procedure writes and for the runs of `rowPair` and `rowFactor`). What the grid needs of the
pieces is taken from `cutsOK_piecesOf`. C₂ = 2c + 6. 

### `bothNetworks`

 **«Definition 2 holds with B₁ = gB + g²(2λ)^c in the role of B and with τ = 2^{cλ}Ξ^{C₂}.»** 
