---
{
  "module": "proof/variables/VariableBound/Field/Ring.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Ring.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Ring.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The programs compute in the ring

R is a commutative ring in which 2 = 0, r an element of R, and g a word of s bits with r^s =
`decR r g`; so r is a root of X^s + g. For words of s bits, `xorW` is the sum, `mulX g` the product
with r,
`mulW g` the product and `powW g` the power of what the words stand for (`decR r`), and all of them
give words of s bits (`powW g` only for s ≥ 1). 

 ### Lengths 

### `length_xorW`

 The sum is as long as the shorter word. 

### `length_zeroW`

 The word 0 is as long as g. 

### `length_oneW`

 The word 1 is as long as g, if g is not empty. 

### `length_mulX`

 X·w is as long as g, if w is. 

### `length_mulW`

 x·y is as long as g, if x is. 

### `powW_succ`

 One more factor. 

### `length_powW`

 u^e is as long as g, if g is not empty. 

 ### Values 

### `bitR_xor`

 In a ring with 2 = 0, the exclusive or of two bits is their sum. 

### `decR_xorW`

 In a ring with 2 = 0, `xorW` is the sum, for words of the same length. 

### `decR_zeroW`

 The word 0 stands for 0. 

### `decR_oneW`

 The word 1 stands for 1. 

### `decR_concat`

 A bit at the upper end of a word w of n bits adds that bit times r^n. 

### `decR_mulX`

 In a ring with 2 = 0 and for r^s = `decR r g` (r a root of X^s + g), `mulX g` is the product
with r, for a word w of s bits, s the length of g. 

### `decR_mulW`

 In a ring with 2 = 0 and for r^s = `decR r g` (r a root of X^s + g), `mulW g` is the product,
for a word x of s bits, s the length of g, and any word y. 

### `decR_powW`

 In a ring with 2 = 0 and for r^s = `decR r g` (r a root of X^s + g), `powW g` is the power, for
s ≥ 1 the length of g and any word u. 
