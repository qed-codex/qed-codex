---
{
  "module": "proof/variables/SparsifyThenCount/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/SparsifyThenCount/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/SparsifyThenCount/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Polynomial time of the function that sparsifies with the thresholds of Step 5 and counts each output by Steps 1 to 4 as printed, and the bound of Step 6

**What is proved.**
* `certDGc`: for thresholds that serve and every polynomial-time solver, the function `ADG Θ` is
  polynomial-time, if `pick` and `slU` are.
  The certificate of the walk is that of proof/sparsification/StepSparsify
  (`StepSparsify.stCertWalkSG`, `StepSparsify.stCertNoTaut`); the count of one sparse formula is
  polynomial-time in the pad by `VariableBound.certCountDc` (Steps 1 to 4).
* `certBDGc`: the same for the merged function `ABDG Θ` and the exponent function `eBD`.
* `timeDGc`: Step 6, the number of steps of a padding machine with the exponent function `eD` is
  within the bound in n with k² in the exponent;
  it uses the arithmetic of the exponent of Steps 4 and 5 (`VariableBound.arithDc`,
  `VariableBound.stPlanLeD`), which does not know the thresholds. 

### `certDGc`

 For thresholds that serve and every polynomial-time solver, the function `ADG Θ` is
polynomial-time, if `pick` and `slU` are. 

### `certBDGc`

 For thresholds that serve and every polynomial-time solver, the merged function `ABDG Θ` and the
exponent function `eBD` are polynomial-time, if `pick` and `slU` are. 

### `timeDGc`

 Step 6: the number of steps of a padding machine with the exponent function `eD` is within the
bound in n with k² in the exponent; the constant does not depend on k. 
