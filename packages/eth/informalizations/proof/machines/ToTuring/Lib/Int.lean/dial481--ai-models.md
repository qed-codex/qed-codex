---
{
  "module": "proof/machines/ToTuring/Lib/Int.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/Int.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/Int.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial time: integers, as a sign and an absolute value. The word of an integer is the word
of the pair
(negative?, absolute value), so every operation on integers is an operation on such pairs. 

### `sgn`

 Is the integer negative? 

### `mkZ`

 The integer with the given sign (true: negative) and absolute value. 

### `sgn_mkZ`

 The sign of `mkZ s n`: zero is not negative. 

### `natAbs_mkZ`

 The absolute value of `mkZ s n`. 

### `rep`

 An integer as the pair of its sign and its absolute value. 

### `sgn'`

 The sign of an integer in polynomial time. 

### `natAbs`

 The absolute value of an integer in polynomial time. 

### `mkZ'`

 An integer from its sign and absolute value in polynomial time. 

### `natCast`

 A natural number as an integer in polynomial time. 

### `toNat`

 `Int.toNat` (a negative integer goes to 0) in polynomial time. 

### `negZ`

 The negation of an integer in polynomial time. 

### `add_eq`

 The sum of two integers from their signs and absolute values. 

### `addZ`

 The sum of two integers in polynomial time. 

### `subZ`

 The difference of two integers in polynomial time. 

### `mul_eq`

 The product of two integers from their signs and absolute values. 

### `mulZ`

 The product of two integers in polynomial time. 

### `decide_ltZ`

 The test `<` on integers in polynomial time: the sign of the difference. 

### `decide_leZ`

 The test `≤` on integers in polynomial time: the sign of the difference. 

### `instance : EqT ℤ`

 The test of equality on integers in polynomial time: compare signs and absolute values. 
