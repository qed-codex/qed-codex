---
{
  "module": "proof/variables/VariableBound/Printed/ThmVariablesA.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Printed/ThmVariablesA.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Printed/ThmVariablesA.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (a) of Appendix D: its last sentence and a fact of Step 5

Two statements of proof/variables/VariableBound/Printed/ThmVariablesADefs.lean, collected here in
the namespace `MainTheoremForms` under the names of the statements: the last sentence of Theorem D (a)
and the bound k·log n ≤ e·n of Step 5. 

### `thmVariablesAInParticular`

 Theorem D (a), last sentence: if e_ℓ ≤ c·(log K_ℓ)^(−α′) for all ℓ, with α′ > 0, a machine with
the bound of Theorem D (a) takes at most 2^{C'·k²·n·log log n/(log n)^α′} steps, for n ≥ K₀^17 and 3
≤ k ≤ (log n)^(1/4). 

### `stepSparsifyLarge`

 Step 5: k·log n ≤ e·n for n ≥ n₁(C₀), k ≤ (log n)^(1/4) and e ≥ (log n)^(−C₀). 
