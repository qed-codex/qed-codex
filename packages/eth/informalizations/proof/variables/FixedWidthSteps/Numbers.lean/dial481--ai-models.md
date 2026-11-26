---
{
  "module": "proof/variables/FixedWidthSteps/Numbers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/FixedWidthSteps/Numbers.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/FixedWidthSteps/Numbers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sentences about numbers

Proofs of `ChainOfInequalities`, `RateOfThePairs`, `ConditionsHoldEventually`, `ReadAsThree`
(RouteDefs.lean) and of `FixedWidth.ProvisoHolds`, from part (a) of the theorem on the general
recursion (proof/rates/GeneralPieces/Num/PartA.lean, PartAUse.lean, Asymptotic.lean) and from the
remarks on the proof of part (c) (proof/rates/GeneralPieces/Num/Remarks.lean, Between.lean). 

### `chainOfInequalities`

 e_ℓ ≥ ½ρ^ℓ ≥ 2^{−ℓ−1} ≥ 1/log K_ℓ, and a number between 0.85ρ^ℓ and ρ^ℓ lies in [e_ℓ, 2e_ℓ]. 

### `rateOfThePairs`

 e_ℓ ≤ (3x₀+6)/(log K_ℓ)^{α'}. 

### `conditionsHoldEventually`

 The conditions n ≥ K₀^17 and k ≤ (log n)^{1/4} hold for all but finitely many n when k is fixed. 

### `readAsThree`

 A formula with k ≤ 2 is read as a 3-CNF. 

### `provisoHolds`

 «… as is the case for ρ = 11/12 and for ρ = 1/√2.» The numbers are those of
proof/rates/GeneralPieces/Num/Between.lean: 11^ℓ/12^ℓ, and 2^{−ℓ/2} for even ℓ, (7/5)·2^{−(ℓ+1)/2}
for odd ℓ. They are computed from ℓ alone, in time polynomial in ℓ. 
