---
{
  "module": "NS1/Postpone.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Postpone.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Postpone.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Constants are postponed

`WF` applied to (program, (argument, budgets)) has, as plain weighted sum, the sum of the weights of the runs whose
names of constants are exactly the given budgets. Summed over all budgets with the powers of the constants this is
the value of the program.


### `KT`

 A trie with constants of `R` at its leaves. 

### `KT.none`

 no constant 

### `KT.leaf`

 one constant 

### `KT.node`

 constants whose names begin with 0, constants whose names begin with 1 

### `nds`

 The number of nodes. 

### `ht`

 The height: a bound for the length of names. 

### `lookup`

 The constant with a given name (0 if there is none). 

### `words`

 Numbers with `J` digits. 

### `val`

 The value of a number. 

### `budg`

 All budgets with `J` digits for the names of a trie, with the products of the powers of its constants. 

### `ok`

 The bill uses up the budgets. 

### `part`

 The names that begin with a given bit. 

### `sum_budg`

 **All budgets together.** 

### `wt`

 The weight of a run, if the named constants are `κ`. 

### `val`

 The value of a list of runs. 

### `pval`

 The value of a list of runs without named constants. 

### `WF`

 Apply a program; then check that the budgets are used up. The argument is (program, (argument, budgets)). 

### `WF_ev`

 **Lemma 1, one bill**: `WF` is plain; it has the runs whose bill is the budget. 

### `val_eq_sum_budg`

 **Lemma 1 (postponing).** The value of a list of runs is the sum, over all budgets, of the powers of the constants
times the sums of the weights of the runs that use up the budgets. 
