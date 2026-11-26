---
{
  "module": "NS1/Comp.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Comp.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Comp.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Weighted functions computed by formulas

`Does θ F x Q c`: all runs of the formula `F` at the tree `x` stop, they use no named constants, the accepting ones
have cost at most `c`, and for every function of the value their weighted sum is that of the list `Q` of pairs
(weight, value).


### `wsum`

 Weighted sums over a list of pairs (weight, value). 

### `bindW`

 First `Q`, then `R` at the value. 

### `Does`

 The formula computes the weighted list `Q` at `x`. 

### `Gives`

 The formula has the value `o` at `x`, with weight 1. 

### `congr`

 Replace the list by an equivalent one. 

### `plain`

 A computation is a plain sum. 

### `cons`

 Pairs. 

### `app`

 Apply a fixed program to the value. 

### `lett`

 `let`. 

### `letk`

 `let`, with the argument kept. 

### `run`

 Apply a program that is the value of a formula. 

### `either`

 Guess between two formulas. 

### `theta`

 Multiply by a constant of `A`. 

### `after`

 A computation, then a deterministic one. 

### `Does.of_gives`

 The weighted list of a deterministic computation followed by another one. 
