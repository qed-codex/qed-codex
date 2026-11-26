---
{
  "module": "proof/variables/SparsifyThenCount/CorrectB.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/SparsifyThenCount/CorrectB.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/SparsifyThenCount/CorrectB.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The merged function is right

`stCorrectBDG : StCorrectBDG` holds for any family of thresholds that serves: the merged function
returns the number of satisfying assignments if the pad has the length that the
exponent `VariableBound.eBD` asks for. The test `VariableBound.useMD` and the exponent are those of
proof/variables/VariableBound and do not name the thresholds. Where the test holds, every variable
occurs and there is a clause (`VariableBound.CorrectB.useMD_enc`), which is what the
correctness of the algorithm for the bound in m needs (`StCorrectM`); elsewhere the function is
`ADG`, which is right by `StCorrectDG`. 

### `stCorrectBDG`

 The merged function, run with thresholds that serve, is right on every k-CNF, for every k ≥ 1
and every n, when the pad has length at least 2^(eBD …); given that the two algorithms are right
(`StCorrectDG`, `StCorrectM`), the test on the
variables (`UniformInK.StAllOccU`) and the decoder (`StDecM`). 
