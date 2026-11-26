---
{
  "module": "proof/variables/VariableBound/Net/Total.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Total.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Total.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 3, «Profiles»: the values of the networks of the admissible profiles add up to the right side of display (65)

The value of the network of a profile y is the sum of the terms of the pairs (ξ, P) that belong to y
(StVal). For g > 0, well-formed data and a set P of places of objects, exactly one admissible
profile has P if P is within
the limits |Π₀| = n̄ + 1 (for F: ≤ n̄) and |Π₁| + … + |Π_r| ≤ M, and none otherwise (StProf). So the
sum over the admissible profiles is the sum of the terms of the pairs (ξ, P) with P within the
limits, which is the right side of
display (65) (StTuples). The same argument as in proof/rates/PaddedDescent/F/MarkSum.lean. 

### `stTotal`

 Step 3, «Profiles»: «each right side of (65) is the sum of the values of the networks of the
admissible profiles», for g > 0 nodes and well-formed data (the formula Φ and the list 𝚲 of checks).
Conditional: the statements StVal (the value of one
network), StProf (the sum over the profiles) and StTuples (the sum over the sets of objects) are
hypotheses here; `VariableBound.Net.Main.total` supplies them. 
