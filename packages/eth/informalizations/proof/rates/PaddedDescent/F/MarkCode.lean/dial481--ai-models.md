---
{
  "module": "proof/rates/PaddedDescent/F/MarkCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkCode.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Marks and layers: the code of the labels

`enc β b x` of proof/rates/PaddedDescent/F/MarkNet.lean cuts the bit string x into blocks of b bits.
A block with j ones is written as j ones, a zero, and then the j positions of
its ones inside the block, β bits each. This file proves the two interface statements on it in
proof/rates/PaddedDescent/F/Interfaces.lean. For 0 < b the code has 1 + β bits for
every one of x and one bit for every block (`stEncLen`). For 0 < b ≤ 2^β a string of known length is
read back from its code, whatever follows the code
(`stEncInj`); so the codes of several strings of known lengths, laid end to end as in a label of the
network, are read back one after the other. At b = 0 there are
no blocks and every code is empty, so 0 < b cannot be left out. 

### `ones`

 The positions, inside block number o, of the ones of x. 

### `blkc`

 The code of block number o of x. 

### `enc_eq`

 The code is the codes of the blocks, laid end to end. 

### `mem_ones`

 p is listed for block o exactly when p < b and x has a one at the place o·b + p. 

### `le_blocks_mul`

 The blocks of b bits cover a string of t bits. 

 ### Reading the code back 

### `eq_of_words`

 Words of β bits of numbers below 2^β, laid end to end, are read back one by one, whatever
follows them. 

### `eq_of_blkc`

 One block is read back, whatever follows it. 

### `eq_of_blocks`

 Several blocks are read back, whatever follows them. 

### `enc_append_inj`

 A string of known length is read back from its code, whatever follows the code. 

 ### The length of the code 

### `length_blkc`

 A block with j ones takes j·(1 + β) + 1 bits. 

### `length_filter_getD`

 The places below M, where M is at least the length of x, that hold a one are as many as the ones
of x. 

### `flatMap_ones`

 The ones of the first N blocks, with their places in x, are the places below N·b that hold a
one. 

### `length_enc`

 The length of the code: 1 + β bits for every one, and one bit for every block. 

### `stEncLen`

 For 0 < b the code of x has 1 + β bits for every one of x and one bit for every block of b bits. 

### `stEncInj`

 For 0 < b ≤ 2^β a string of known length is read back from its code, whatever follows the code. 
