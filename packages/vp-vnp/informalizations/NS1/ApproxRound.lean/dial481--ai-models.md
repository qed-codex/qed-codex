---
{
  "module": "NS1/ApproxRound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/ApproxRound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/ApproxRound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# One round for approximate accelerators

The budgets of the outer program are guessed and multiplied exactly, as in an exact round. The constants of the inner
program are rescaled by ε ↦ ε^r, with r above every exponent in the outer weights. To give the rescaled constants names
of their own the round guesses budgets for all inner calls at once and runs the list program inside the interpreter.


### `rebF`

 Guess budgets with `g`; run the interpreted program `P` on the argument with these budgets. 

### `rebF_kv`

 **The weight of a budget times the runs that use it up**, summed over the budgets. 

### `rebill_kv`

 **A program with renamed constants**: with the names `pre ++ p` for the images under `f` of its constants. 

### `stepA`

 A round: guess budgets with `g`, form the plain instance of `p`, cut it with `G`, apply `F` to (`c`, pieces). 

### `IsAccA`

 **Paper: the definition of an approximate accelerator.** The program `D`, with constants in E[ε,ε⁻¹], has values in pv z + ε E[ε], in `t`
steps, on the instances of size `v ^ (H - 32)` of the universal plain sums of `v ^ H` steps. 

### `IsPreA`

 The same, where runs have to stop only if the sum is plain. 

### `UF_preA`

 The universal program needs no constants. 

### `roundA`

 The program of a round: outer budgets with the names that begin with 0, inner ones with those that begin with 1. 
