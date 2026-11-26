---
{
  "module": "proof/variables/VariableBound/Top/CorrectB.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/CorrectB.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/CorrectB.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # When the merged function takes the algorithm for the bound in m, and its exponent is the smaller one

Part of the proof of Corollary 11, «computing the two exponents … and running only the algorithm
with the smaller one» (here the two exponents are computed exactly). `useMD_enc`: on the code of a
k-CNF the algorithm for the bound in m is taken
exactly if every variable occurs, there is a clause, and its exponent is not the larger one.
`stExpBD`: the exponent of the merged function is at most that of the algorithm for the bound in n,
and,
if every variable occurs and there is a clause, at most that of the algorithm for the bound in m. 

### `useMD_enc`

 On the code of (k, φ), k ≥ 1, φ a k-CNF, the algorithm for the bound in m is taken exactly if
every variable occurs, there is a clause, and its exponent is not the larger one. Given
`UniformInK.StAllOccU` and `StDecM`. 

### `stExpBD`

 For k ≥ 1 and a k-CNF: the exponent is at most that of the algorithm for n, and, if all
variables occur and there is a clause, at most that of the algorithm for m. 
