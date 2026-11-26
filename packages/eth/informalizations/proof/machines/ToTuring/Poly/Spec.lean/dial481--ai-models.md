---
{
  "module": "proof/machines/ToTuring/Poly/Spec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Spec.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Spec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 What it means that the transformers of the module `StepMachines.Prog.Spec` keep `IsPolyT` (every
step is polynomial-time):
if the lengths they are given are `Unary` and the procedures `IsPolyT`, so is the machine they
build. `IsPolyT` is data and
the predicates below are propositions, hence `Nonempty`. 

### `Evaluator.Keeps`

 `E` keeps `IsPolyT`: if the length `lam` is `Unary` and the procedure `R` is `IsPolyT`, then so
is `E.app lam R`. 

### `PNet.Keeps`

 The lengths `n` and `cap` are `Unary` and the two procedures `W` and `f` are `IsPolyT`. 

### `NetEvaluator.Keeps`

 `NE` keeps `IsPolyT`: if the network `Np` satisfies `PNet.Keeps`, then `NE.app Np` is `IsPolyT`. 
