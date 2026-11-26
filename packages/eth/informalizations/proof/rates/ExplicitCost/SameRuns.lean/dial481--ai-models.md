---
{
  "module": "proof/rates/ExplicitCost/SameRuns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/SameRuns.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/SameRuns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The machine that reads K and g runs as `Printed.tableQ K g`

`entrySameRuns : EntrySameRuns`. The input of `Printed.tableQ K g asked` is widened by K and g in
unary (`widen`). Along this map every plain function of `entryData` agrees with that of `tableQ K g`
(after K and g have been read off as lengths, by definition), so the lemmas of Mirror.lean, one for
each construction, give a map of states.
The growth of the states is counted by these lemmas, from the state types: one copy of (K, g) in a
pending query, one more beside the test before a factor, one more in the point of the loop over the
factors, one more in the point of the loop over the terms: four. 

### `widenC`

 K and g, in unary, put beside the input of Definition 2(iii). 

### `widen`

 The same for the input of the machine for an entry. 

### `size_unary`

 The size of a number in unary. 

### `size_widenC`

 One copy of K and g in unary. 

### `size_widen`

 The widened input of the machine is larger by one copy of K and g in unary. 

### `size_map_fst`

 A pair grows as its first component does. 

### `kOf_widen`

 The K that the machine reads off the widened input. 

### `gOf_widen`

 The g that the machine reads off the widened input. 

 ## The four procedures: one query each 

### `mirrors_mem`

 «Is z ∈ S_a?»: one query, the same with K and g beside the input. 

### `mirrors_W`

 W_a(z): one query, the same with K and g beside the input. 

### `mirrors_Ψ`

 Ψ_{a,b}(z, z'): one query, the same with K and g beside the input. 

### `mirrors_f`

 f_{a,b}(z, θ): one query, the same with K and g beside the input. 

 ## The plain functions agree 

### `widen₁`

 The input of a term, widened. 

### `widen₂`

 The input of a factor, widened. 

### `size_widen₁`

 The widened input of a term is larger by at most one copy of K and g in unary. 

### `size_widen₂`

 The widened input of a factor is larger by at most one copy of K and g in unary. 

### `qW_widen`

 The query (a, z_a) is the same on the widened input. 

### `qF_widen`

 The query ((a, b), (z_a, θ_{a,b})) is the same on the widened input. 

### `qMb_widen`

 The query (b, z_b) is the same on the widened input. 

### `qPsi_widen`

 The query ((a, b), (z_a, z_b)) is the same on the widened input. 

### `isOne_widen`

 The test «this factor is 1» is the same on the widened input. 

### `isW_widen`

 The test «this factor is a value of W_a» is the same on the widened input. 

### `isPsi_widen`

 The test «this factor is a value of Ψ_{a,b}» is the same on the widened input. 

### `nPairs_widen`

 The number of factors of a term is the same on the widened input. 

### `nStates_widen`

 The number of terms of an entry is the same on the widened input. 

### `validB_widen`

 The test «all appended bits are 0» is the same on the widened input. 

 ## The machines 

### `mirrors_wData`

 [z_a ∈ S_a]·W_a(z_a): the pending query and the copy beside the test. 

### `mirrors_psiData`

 [z_a ∈ S_a][z_b ∈ S_b]·Ψ_{a,b}(z_a, z_b). When the second test begins the copy beside the first
is gone. 

### `mirrors_fData`

 [z_a ∈ S_a]·f_{a,b}(z_a, θ_{a,b}). 

### `mirrors_termData`

 One factor. 

### `mirrors_entryData`

 **One entry**: four copies of K and g. 

### `entrySameRuns`

 **For each K and g the machine runs as `Printed.tableQ K g` does.** 
