---
{
  "module": "proof/machines/StepMachines/Math/Sparse.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/Sparse.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/Sparse.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Names for sparse strings of Bell states, used for the label sets `rowLabels` and `colLabels`.
Here a Bell state is a pair of bits (the type `Bell`), one of four.
A string of n Bell states of which at most c differ from a fixed state s₀ is named by a word of
`capW n c` = n + `tb c` bits, where `tb c` is the number of bits of 3^c:
n bits that mark the positions where the string differs from s₀, then one number below 3^(number of
marks), whose digits
in base 3, lowest first, say which of the three other states stands at the marked positions, in
their order. Rows: s₀ is
the singlet, `(true, true)`, and c = n − i; columns: s₀ is Φ⁺, `(false, false)`, and c = i. 

### `sparseLab`

 The strings of n Bell states with at most c states other than s₀. 

### `oth`

 The three states other than s₀, numbered 0, 1, 2. 

### `symAt`

 The state at position k of the string named by the word w. 

### `validW`

 Is the word w (of n + tb c bits) a name? At most c marks, and the number is below 3^(number of
marks). 

 ### The three other states 

### `oth_ne`

 `oth s₀ d` is never s₀. 

### `oth_inj`

 The three numbers 0, 1, 2 name different states. 

### `exists_oth`

 Every state other than s₀ has a number. 

 ### The decoder as a recursion on the list of marks 

### `decL`

 The string named by the marks m and the number Y, read off from left to right: a marked position
takes the lowest
digit of Y in base 3 and removes it. 

### `getD_decL`

 Position k of the recursion is what `symAt` computes directly. 

### `card_getD_range`

 The number of marks among the first n positions. 

### `card_decL`

 The string differs from s₀ exactly at the marked positions. 

### `decL_inj`

 Different names give different strings. 

### `exists_decL`

 Every string has a name. 

### `mem_validWords`

 What it means to be a valid word. 

### `sparse_bijOn`

 The valid words name the strings with at most c states other than s₀, one each. 

### `Code.sparse`

 The code of the strings with at most c states other than s₀: the valid words, decoded by
`symAt`. 

### `card_eq_add_card_ne`

 Every position holds s₀ or another state. 

### `rowLabels_eq`

 At least i singlets: at most n − i states other than the singlet. 

### `colLabels_eq`

 At most i states other than Φ⁺: the label set for columns. 

### `capW_le`

 A name has at most 4n bits. 
