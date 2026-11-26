---
{
  "module": "proof/machines/ToTuring/Lib/Nat1.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/Nat1.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/Nat1.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial time for binary numbers: digits, predecessor, sum, difference, comparison, min, max,
equality (`EqT ℕ`).

A number is written as the list of its binary digits, so a function into ℕ is polynomial-time as
soon as some word of digits of
its value is (`ofBits`; `bitsTrim` cuts off the leading zeros). Sum and difference are one and the
same walk, `bitRun`, computed
as a fold of `bitStep`: it goes through two words from the lowest digit and passes on a carry (or a
borrow); the last borrow of
a difference decides the comparison. 

 ### The value of a word of digits 

### `bval`

 The number written by a word, lowest digit first; leading zeros are allowed. This is `ofWord` of
StepMachines/Prog/Chunks.lean
(see `foldr_bit` in Lib/List2.lean); the lemmas on digits are proved for `bval` because its
definition is a fold. 

### `bval_eq`

 A word is worth its lowest digit plus twice the rest; an empty word counts as a zero digit. 

### `bitsTrim`

 The word without its leading zeros (which stand at its end). 

### `of_bits`

 A function into ℕ is polynomial-time if the word of its digits is: both are written in the same
way. 

### `bits`

 The converse of `of_bits`: the word of digits of a polynomial-time number is polynomial-time. 

### `ofBits`

 The number written by a word, lowest digit first, is polynomial-time: the leading zeros are cut
off by `bitsTrim`. 

 ### One fold for sum and difference 

### `bitStep`

 One step of the walk through two words u, v. The state is (carry, rest of u, rest of v, digits
written so far, last one
first); φ maps (carry, digit of u, digit of v) to (new carry, digit to write). A word that has run
out yields zeros. 

### `bitRun`

 The walk through u and v with first carry c, one step for every entry of L: the last carry and
the digits written, lowest
first. 

 ### Sum 

### `addφ`

 Full adder: (carry, x, y) ↦ (new carry, digit). 

 ### Difference and comparison 

### `subφ`

 Full subtractor for x - y - borrow: (borrow, x, y) ↦ (new borrow, digit). 

### `subRun`

 The walk that subtracts b from a. 
