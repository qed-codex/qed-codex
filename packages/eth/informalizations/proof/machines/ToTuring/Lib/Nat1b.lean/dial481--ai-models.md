---
{
  "module": "proof/machines/ToTuring/Lib/Nat1b.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/Nat1b.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/Nat1b.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial time for binary numbers: size, log2, single bits, and numbers computed from a list
(length, sum, counts, index
of an element). 

 Helpers: how the number of binary digits grows, and the folds that compute the functions below. 

### `length`

 The length of a list, in binary: a fold that adds 1 for every element. 

### `size'`

 The number of binary digits of a number: the length of its list of digits. 

### `log2'`

 The binary logarithm, rounded down: the number of binary digits minus 1. 

### `testBit`

 Bit number `g x` of `f x`: a fold over the binary digits that carries the position and the bit
found so far. 

### `sum`

 The sum of a list of numbers: a fold that adds the elements. 

### `countP`

 The number of elements that pass a test: the length of the filtered list. 

### `count`

 The number of occurrences of an element: `countP` with the test of equality (`BEq` as for
`PolyT.beq'`). 

### `idxOf`

 The index of the first occurrence of an element (the length of the list if there is none): a
fold from the right (`BEq` as
for `PolyT.beq'`). 
