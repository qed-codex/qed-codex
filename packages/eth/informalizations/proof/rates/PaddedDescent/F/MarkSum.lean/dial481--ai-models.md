---
{
  "module": "proof/rates/PaddedDescent/F/MarkSum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkSum.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkSum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Marks and layers: the values of the networks of the admissible profiles add up to the cut-off sum

A layer is one of the sets of clauses in the list Ls, and `layP Ls P i` is the set of the members of
P in layer i. The layers, and the cut-off at w members in every layer, are a variant of the cut-off
of Appendix D that the paper does not state.
The value of the network of a profile y counts, with signs, the pairs (σ, P) with the profile y
(StMarkVal). Every P has exactly one profile, and that profile is admissible exactly if P has at
most w members in every layer (StProfSum).
So the sum over the admissible profiles counts, with signs, the pairs (σ, P) in which P has at most
w members in every layer, and for a fixed σ that signed number is the product of the cut-off sums
(StPiSum). 

### `stMarkSum`

 The central identity, from the value of one network, the sum over the profiles and the sum over
the sets of violated clauses. 
