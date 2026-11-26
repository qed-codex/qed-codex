---
{
  "module": "proof/rates/PaddedDescent/F/CertSparsify.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/CertSparsify.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/CertSparsify.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial-time certificates (`PolyT`) for the walk of the sparsification tree in which the
threshold τ is part of the DATA and not a constant of the
machine. The step is `stepK (theta τ) k` of proof/sparsification/SparsifyWidthK. Its certificate in
proof/sparsification/SparsifyWidthK/Poly/Sparsify.lean is for fixed thresholds. There `pickK_eq`
writes the
choice of the rule as a search along the list of the pairs (j, h), each with its threshold θ (j -
h). Here that list depends on τ, but its length does not, and each
of its members is polynomial-time in τ (`polyT_theta`). This gives `polyT_stepKU`, the two children
of a node, for every width k.
One round `roundB` of the depth-first walk follows. 

### `polyT_map_fixed`

 A list of fixed length whose members are polynomial-time functions of x is a polynomial-time
function of x. 

### `polyT_thrPair`

 For every fixed i, the pair (θ i, 2 + β 1 + … + β i) is polynomial-time in τ. 

### `polyT_theta`

 For every fixed i, the threshold θ i is polynomial-time in τ. 

### `polyT_pickKU`

 The choice of the heart and its petals at a node is polynomial-time jointly in τ and the
formula. 

### `polyT_stepKU`

 The two children of a node of the sparsification tree, jointly in τ and the formula. 

### `roundB_eq`

 `roundB` with its case distinctions written by eliminators. 

### `polyT_roundB`

 One round of the depth-first walk is polynomial-time, for a step function and a test that may
depend on the context. 
