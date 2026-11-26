---
{
  "module": "Nc/Grp/Steps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Grp/Steps.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Grp/Steps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Sums over contents, one step after the other

A step writes the cells of a set `wr`: it chooses `ω`, with a weight, and the contents of the cells, both as functions
of the cells written before. The sum, over all contents of the cells, of the product of the factors of the steps is
the sum over all executions.


### `ovr`

 Write the cells of `wr`. 

### `WStep`

 A step: a sum over choices of a weight and contents of the cells of `wr`. The sum is given by its values
`sum σ f` at functions `f` of the new contents. 

### `WStep.ι`

 choices 

### `WStep.Om`

 finitely many choices 

### `WStep.wr`

 cells that are written 

### `WStep.w`

 weight 

### `WStep.v`

 contents 

### `WStep.rd`

 cells that are read 

### `phi`

 The factor of a step. 

### `wrs`

 The cells written by a list of steps. 

### `exec`

 The sum over all executions. 

### `Seq`

 Steps read only what has been written before, and write every cell once. 

### `sum_eq_exec`

 **Sums over contents are sums over executions.** 

### `seq_of`

 A criterion for `Seq`. 
