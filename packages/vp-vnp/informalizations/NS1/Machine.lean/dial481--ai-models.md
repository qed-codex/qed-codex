---
{
  "module": "NS1/Machine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Machine.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Machine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Sum machines

Data are binary trees. A program is a formula of a small functional language; it is applied to a tree. A formula may
guess a bit, reject, multiply the weight of the run by a fixed constant `θ` of the ring `A` (named by a list of
bits), or by a constant that is *only named* (`mul`); the names are kept in the *bill* of the run. `run a b` applies
the program that is the value of `a` to the value of `b`. Every step costs 1.

`Ev θ F x l`: all runs of the formula `F` at the tree `x` stop, and `l` is the list of the accepting runs.


### `Tree`

 Binary trees. 

### `Tree.nil`

 the empty tree 

### `Tree.cons`

 a tree with two subtrees 

### `hd`

 First subtree. 

### `tl`

 Second subtree. 

### `size`

 The number of nodes. 

### `len`

 The length of a tree as a list. 

### `path`

 A tree as a list of bits. 

### `toList`

 A tree as a list of trees. 

### `num`

 The number `k` as a tree. 

### `one`

 The bit 1. 

### `bit`

 A bit. 

### `ofBits`

 A list of bits as a tree. 

### `Fm`

 Formulas. 

### `Fm.quote`

 a fixed tree 

### `Fm.id`

 the argument 

### `Fm.hd`

 first subtree 

### `Fm.tl`

 second subtree 

### `Fm.cons`

 a tree with two given subtrees 

### `Fm.ite`

 if the value of `a` is not empty then `b` else `c` 

### `Fm.run`

 apply the program that is the value of `a` to the value of `b` 

### `Fm.guess`

 guess a bit 

### `Fm.fail`

 reject 

### `Fm.theta`

 multiply the weight by the constant of `A` that is named by the value of `a` 

### `Fm.mul`

 multiply the weight by the constant that is named by the value of `a` 

### `code`

 Formulas as trees. 

### `ofTree`

 Every tree is read as a formula. 

### `Run`

 An accepting run: its cost, its weight, the names of the constants it wants, its value. 

### `Run.cost`

 number of steps 

### `Run.th`

 weight 

### `Run.bill`

 names of constants that the run multiplies by 

### `Run.out`

 value 

### `seq`

 One run after the other. 

### `tick`

 One more step, with value `o`. 

### `det`

 A run without guesses and weights. 

### `Ev`

 All runs of the formula at the tree stop; the list of the accepting runs. 

### `Ev.unique`

 The list of the accepting runs is determined. 

### `Hl`

 All runs stop. 

### `evl`

 The accepting runs (if all runs stop). 

### `Dt`

 A run without guesses and weights. 

### `Run.delay`

 Weights and costs of runs after a step without guesses. 

### `lett`

 `let`: apply `body` to the value of `e`. 
