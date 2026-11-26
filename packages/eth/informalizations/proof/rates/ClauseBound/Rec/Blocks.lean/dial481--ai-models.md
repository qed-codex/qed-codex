---
{
  "module": "proof/rates/ClauseBound/Rec/Blocks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Rec/Blocks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Rec/Blocks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The blocks of positions

The positions 0, …, n − 1 are cut into δ = ⌈n/h⌉ blocks; position k lies in block k / h. This file
has the elementary facts on this cut that the lemma on the
recombined pieces uses:

* the arithmetic of δ and of the blocks: δ ≤ n ≤ hδ, the block k / h of a position is one of the δ
  blocks, and every block has at most h positions;
* a label is the family of its parts in the blocks (`split`), and block b has 4^{n_b} labels. 

 ### The number of blocks and their sizes 

### `nblk_le`

 There are at most n blocks. 

### `le_mul_nblk`

 The blocks have room for all positions. 

### `div_lt_nblk`

 The block of a position is one of the blocks. 

### `card_blk_le`

 A block has at most h positions. 

 ### A label and its parts in the blocks 

### `family_congr`

 The value of a family of labels on blocks at a position does not depend on how the block of the
position is written. 

### `split`

 A label is the family of its parts in the blocks. 

### `split_apply`

 The part of β in block b has the entries of β. 

### `card_BLab`

 Block b has 4^{n_b} labels. 
