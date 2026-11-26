---
{
  "module": "Zeta23/GammaFacts/Complete.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/GammaFacts/Complete.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/GammaFacts/Complete.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/GammaFacts/Complete.lean — assembly of H-Γ:
All nine fields of Zeta23.GammaFacts ([eq:mufacts] + the Γ-halves of [eq:muints])
are proved: even/smooth (Zeta23/GammaFacts.lean), monotoneOn/mu_zero_le/
neg_one_lt_mu_zero/deriv_bound (Zeta23/GammaFacts/Mu.lean, via the digamma
partial-fraction series), stirling (Zeta23/GammaFacts/StirlingVert.lean, C = 20/2π),
int_mu/int_mu_sq (Zeta23/GammaFacts/IntMu.lean, from stirling + FTC).
-/
```

### `gammaFacts_of_stirling`

 GammaFacts from any Stirling bound for μ (the only analytically deep field). 

### `gammaFacts`

 **H-Γ, unconditionally.** 
