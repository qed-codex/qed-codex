---
{
  "module": "Zeta23/Taper/GevreyPhi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper/GevreyPhi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper/GevreyPhi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Taper/GevreyPhi.lean — the L¹ bounds on the iterated derivatives of
the concrete taper φ(u) = ϱ((L/2−|u|)/w) that the Gevrey tail lemma consumes.
-/
```

### `Params.GevreyPhiBound`

 The Gevrey taper bound, as a hypothesis on (P, T): φ = P.phi T (as a ℂ-valued function)
is C^∞ and ‖φ^{(k)}‖_{L¹} ≤ 2B·w·(A/w)^k·k^{sk} for all k ≥ 1  (= 2B w^{1−k} A^k k^{sk}). 
