---
{
  "module": "proof/rates/CountedRecursion/PolySolverData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PolySolverData.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PolySolverData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The plain functions of the solver

Every plain function of SolverDefs.lean is polynomial-time in what the solver holds. K and
2^{3ℓ'+x₀} are held in unary, so g, their product, and |ℛ| are given in unary; λ, B and ℓ are given
in unary; the number y of a pattern and d are given in binary. 

### `unary_polyT`

 A number given in unary, written in unary. 

### `hLam_unary`

 λ is given in unary. 

### `hLev_unary`

 ℓ is given in unary. 

### `rHead_polyT`

 (ℓ, λ, B) is read off. 

### `rG_unary`

 g, the product of two numbers held in unary, is given in unary. 

### `rD_polyT`

 d is read off. 

### `rLists_polyT`

 The lists are read off. 

### `rRect_unary`

 |ℛ| is given in unary. 

### `nPatterns_polyT`

 «the |𝓘|^{|ℛ|} functions ι». 

### `direction_polyT`

 «the network with the smaller total». 

### `parentAt_polyT`

 The parent that is handed to the callee. 

### `searchInput_polyT`

 What the search is given. 

### `child_polyT`

 The context of the call. 

### `divide_polyT`

 «computing d^{|ℛ|} and dividing by it». 
