---
{
  "module": "proof/variables/SparsifyThenCount/Tied.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/SparsifyThenCount/Tied.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/SparsifyThenCount/Tied.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The merged function for thresholds Θ and its exponent function are an algorithm

`stAlgSG`: for thresholds Θ that serve and a solver with a sequence of levels, the merged function
(sparsification with the thresholds Θ, then the count of each output) with its exponent function is
an algorithm for the two rates in the sense of `VariableBound.Decide.Alg`. Only the first two of
its five hypotheses name the thresholds: the merged function is right (`StCorrectBDG`) and
polynomial-time (`StCertBDG`). The other three are those of proof/variables/VariableBound: the
exponent is at most those of the two algorithms merged
(`VariableBound.StExpBD`), and the two inequalities for the number of steps
(`VariableBound.StTimeD`, `ClauseBound.Both.StTimeM`). The steps from an algorithm to a machine and
to the statements that name no function are generic and are not repeated. 

### `stAlgSG`

 For thresholds Θ that serve (with the bound Lc) and a solver with a sequence of levels: the
merged function for Θ and its exponent function are an algorithm for the rates rn and rm. Given: the
merged function is right (`StCorrectBDG`), it and the exponent function are polynomial-time
(`StCertBDG`), the exponent is at most those of the two algorithms merged (`StExpBD`), and the two
inequalities for the number of steps
(`StTimeD`, `StTimeM`). 
