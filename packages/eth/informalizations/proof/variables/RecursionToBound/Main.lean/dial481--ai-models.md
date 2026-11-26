---
{
  "module": "proof/variables/RecursionToBound/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (a) along the printed Step 5: the end theorems

The statements of proof/variables/RecursionToBound/Defs.lean and where each is proved.
* The numbers of Step 5 (Numbers.lean): `occBoundIsThePrinted`, `boundsGrowWithDelta`,
  `cutOffIsIdle`, `outputsAreWithinTheSetting`.
* The cost (OneOutput.lean, Exponent.lean): `oneOutputCost`, `walkCost`, `exponentIsWithinTheBound`.
* The tree and the code (Tree.lean): `walkTreeIsSparsify`, `outputsAreFew`, `ownDeltaIsBounded`,
  `widthOnTheCode`.
* The guard (Guard.lean): `planFailsOnlyAboveN`. Polynomial time (Cert/Top.lean):
  `countIsPolynomialTime`.
* Here: `countIsRight` (from `outputsAreWithinTheSetting`, `cutOffIsIdle` and `planFailsOnlyAboveN`,
  by Correct.lean), `thmVariablesAForEveryMachine` (from `countIsRight`, `countIsPolynomialTime`,
  `planFailsOnlyAboveN` and `widthOnTheCode`, by End.lean) and `thmVariablesAWithNumberBetween`
  (from `thmVariablesAForEveryMachine`). 

### `countIsRight`

 The function is right in the range of Theorem D (a). 

### `thmVariablesAForEveryMachine`

 **Theorem D (a) for every machine that computes the named function**: for all large n₁ some
machine with finite alphabets computes `count S n₁ Q.pick num` with the exponent
`expo S n₁ Q.pick num`, and every machine that does has the bound of Theorem D (a). 

### `thmVariablesAWithNumberBetween`

 **Theorem D (a), with the printed clause on the number in [e_ℓ, 2e_ℓ]**. 
