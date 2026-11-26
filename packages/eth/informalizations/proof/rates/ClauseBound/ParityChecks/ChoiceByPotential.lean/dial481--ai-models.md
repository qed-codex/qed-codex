---
{
  "module": "proof/rates/ClauseBound/ParityChecks/ChoiceByPotential.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/ChoiceByPotential.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/ChoiceByPotential.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The choice of the checks by conditional expectations: all statements together

`stepTwo` proves `ParityChecks.ChoiceByPotential` of ParityChecksStatement.lean: it puts together
the theorems on one decision (Martingale.lean), on the sign, the start and the passage from one
check to the next
(Start.lean), on what a potential below 1 gives (Structure.lean) and on the truncated potential
(Approx.lean). 

### `stepTwo`

 The choice of the checks by conditional expectations (`ParityChecks.ChoiceByPotential`): a
variant of Step 2 of Appendix D that chooses the checks by a potential of four terms instead of by
Lemma 13. Here are its mathematical statements, without the program that carries it out. 
