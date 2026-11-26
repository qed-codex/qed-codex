---
{
  "module": "Nc/Price/Cross.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Price/Cross.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Price/Cross.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Lemmas for the crossing inequality

For Paper.prop_crossing (Paper/Crossing.lean): tensors with four legs, the two wires among them, and the compact set of the
pairs (r, l).


### `SplitAB`

 `f` is a sum of `r` products of a function of the first two indices and one of the last two. 

### `SplitAD`

 `f` is a sum of `r` products of a function of the first and the last index and one of the two in the middle. 

### `four`

 A tensor with four legs, of sizes |α|, |β|, |α|, |β|. 

### `le_F_cross`

 The two wires between x and v and between y and u. 

### `quarter`

 The quarter disc of radius √ρ. 

### `exists_quarter`

 If X ≤ min(A + r·s, B + l·t) + δ for all δ > 0 with some (r, l) in the quarter disc, then also for
δ = 0. 
