---
{
  "module": "proof/networks/SingleBitPieces/Level/Presents.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/SingleBitPieces/Level/Presents.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/SingleBitPieces/Level/Presents.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proposition 3: lemmas on the procedures that present the network
The lemmas hold for any pieces. This folder uses them for a variant of the pieces of Lemma 2 made
from single bits, with ρ = (log 12)/4, which the paper does not use.
The procedure for the weights (a weight by g queries to the tables of the clique) and the function
for the factors (a value in one step) compute the weights and the factors of the row network or the
column network of ι (`W_eq`, `f_eq`). The lemmas after them bound the steps by a·(B + λ)^a·t and the
sizes by S + a·(size c + B + λ)^a, where a = `sideA g`. They serve the sentence «Both networks
satisfy Definition 2 with
… τ = poly(B + λ)» in the proof of Proposition 3. The file follows
proof/machines/StepMachines/Prog/SidePresents.lean, which does the same for the networks of
`Groundwork`; there a value of a factor takes about 4·4^λ steps. The weights and factors of the
network on words are those of proof/rates/ClauseBound/Alg/GridPresents.lean (`gridN_W`, `gridN_f`,
`gridFf_eq`). 

### `sideChk_eq`

 The test of the procedure `sideChk` for the weights is the test of the grid with g rows and g
columns. 

### `W_eq`

 What the procedure for the weights (`sideWv` with `sideChk`) computes is the weight of the
network, for any pieces. 

### `f_eq`

 The plain function for the factors computes the factor of the network, for any pieces. 

 ### The arithmetic of the bounds 

### `size_int_le`

 A number with at most b bits. 

### `time_W`

 The steps of the weights. 

### `time_f`

 One step. 

### `size_f`

 The sizes of the factors: the query, and the value with at most g·B + 2g²λ bits. 
