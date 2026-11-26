---
{
  "module": "NS1/DSteps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/DSteps.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/DSteps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The interpreter of steps and templates


### `gets`

 The values of a trie. 

### `DStep`

 Steps. 

### `DStep.pick`

 choose an option (a list of assignments) from the list that the table has at the value of `p` 

### `DStep.op`

 `dst := φ (value of p, value of q)` 

### `DStep.bits`

 if the value of `p` is not empty: guess a bit list for `dst` 

### `DStep.check`

 reject if the value of `p` is empty 

### `tree`

 As a tree. 

### `exec`

 The states after the step; `m` is the length of guessed bit lists. 

### `cost`

 A bound for the cost. `mb`: the number of digits of `m`. 

### `dstepF`

 The program of a step; the argument is (step, trie); `n` is the length of guessed bit lists, in binary. 

### `execAll`

 The states after a list of steps. 

### `dstepsF`

 All steps: `w` gives the trie. 

### `Tm`

 Templates. 

### `Tm.c`

 a fixed tree 

### `Tm.get`

 the value at a path 

### `Tm.cons`

 a node 

### `Tm.ifeq`

 `a` if the value at `p` is `t`, else `b` 

### `Tm.app`

 concatenation of lists 

### `tree`

 As a tree. 

### `expand`

 Fill in the values. 

### `cost`

 The cost. 

### `tmRec`

 Recursive call of the expansion. 

### `tmB`

 The program that fills in templates. The argument is (this program, (template, trie)). 

### `tmF`

 Fill in a template: `t` gives the template, `w` the trie. 

### `tmsF`

 Fill in all templates of a list. 
