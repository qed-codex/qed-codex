---
{
  "module": "proof/rates/PiecesCounted/PaddedData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/PaddedData.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PiecesCounted/PaddedData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From the padding string to counted operations: the data

`AppRunningTime.IsPieces` (`AppRunningTimeStatement.lean`) numbers 𝓘 from 0, and three of its
programs (the two functions of a factorization and the values of the A_i) read a padding string.
`ofPadded P A c shift` (`PiecesCountedStatement.lean`) are the data with 𝓘 shifted and the padding
string fixed at 2^{cλ} units.
They have clauses (a), (b) and the sizes of (c) with the same ρ and c (`ofPadded_is`). Before that,
side lemmas on lists of bits, lists of units and the sorted list of a shifted range. 

 ### Side lemmas 

### `bitsOf_toBits`

 A list of bits of the right length, read as a string and written as a list again. 

### `units_eq`

 A list of units is determined by its length. 

### `sort_image_shift`

 {0, …, n − 1} shifted by s, in increasing order. 

### `toNat_shift`

 The number of a piece in `P` from its number in the shifted index set. 

### `mem_ofPadded`

 The elements of the shifted index set. 

 ### Clauses (a), (b) and the sizes of (c) 

### `ofPadded_is`

 The data made from pieces with a padding string have clauses (a), (b) and the sizes of (c), with
the same ρ and c. 
