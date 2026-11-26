---
{
  "module": "proof/sparsification/SparsifyWidthK/SetAlg.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/SetAlg.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/SetAlg.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One step of the branching rule, as sets

This file computes the two children of a step (`light_eq`, `heavy_eq`) and shows that a formula is
satisfied exactly if one of its children is
(`sat_iff`). It uses only the definitions of SparsifyWidthK/Defs.lean and the lemmas on `red` of
StepMachines/Math/Sparsify.lean. At the end the three results are
restated as `StLightEq`, `StHeavyEq` and `StSatIff`, three of the interface statements of
SparsifyWidthK/Interfaces.lean. 

### `red_union'`

 Let no clause of F contain another, and add a set A of proper subsets of clauses of F, none of
which contains another. Then the
inclusion-minimal clauses of F ∪ A are those of A and the clauses of F that contain no member of A. 

### `mem_over`

 The members of `over F i S`: the clauses of F of size i that contain S. 

### `mem_petals`

 A petal is a clause of size j over H, without H. 

### `card_petal`

 All petals have the same size, j - |H|. 

### `exists_over`

 If all thresholds are at least 1, a heart lies in some clause of size j. 

### `light_eq`

 The light child consists of the heart H and the clauses of F that do not contain H. 

### `heavy_eq`

 The heavy child consists of the petals and the clauses of F that contain no petal. 

### `sat_iff`

 Truth values satisfy F exactly if they satisfy the light child or the heavy child. This holds
for all F, j and H. 

### `stLightEq`

 `SetAlg.light_eq` as an interface statement. 

### `stHeavyEq`

 `SetAlg.heavy_eq` as an interface statement. 

### `stSatIff`

 `SetAlg.sat_iff` as an interface statement. 
