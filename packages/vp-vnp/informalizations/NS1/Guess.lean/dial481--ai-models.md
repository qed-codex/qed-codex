---
{
  "module": "NS1/Guess.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Guess.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Guess.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Guessing the budgets and multiplying by the powers of the constants


### `comb`

 The constants `c, c², c⁴, …` (`n` of them); the names are `0, 10, 110, …`. 

### `expand`

 The powers `c ^ (2 ^ b)`, `b < B`, of all constants. 

### `combVal`

 The power of `c` that has a given name. 

### `lk`

 The constant with a given name: `l ++ 1^b ++ 0` names the power `2 ^ b` of the constant with the name `l`. 

### `pw`

 The name of the power `2 ^ b`. 

### `InB`

 Names of powers `2 ^ b`, `b < B`, of the constants. 

### `Leaf`

 Names of the constants. 

### `gbit`

 Guess a bit; if it is 1, multiply by the constant with the name `p`. 

### `gw`

 Guess the digits of a number; multiply by the powers of a constant. `ν i` is the exponent in the name that is
used for the power `2 ^ i`. 

### `gcomb`

 The budgets of the powers of a constant. 

### `gt`

 The budgets of all powers `2 ^ b`, `b < B`, of all constants. 

### `RelG`

 A run that guesses a budget and multiplies by the powers of the constants. 

### `gt_ev`

 Runs of `gt` = budgets. The hypothesis: the names that are used name the right powers. 
