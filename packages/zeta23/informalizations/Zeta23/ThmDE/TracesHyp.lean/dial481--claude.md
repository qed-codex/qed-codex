---
{
  "module": "Zeta23/ThmDE/TracesHyp.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmDE/TracesHyp.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmDE/TracesHyp.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmDE/TracesHyp.lean — [thm:E], last sentence: "Theorem D holds likewise."
The D-trace interface for a Dirichlet character: Zeta23.ThmD.TracesBoundsD
(Zeta23/ThmD/AssemblyD.lean) with λ₁ ↦ λ_{1,χ} = L/ℓ_{1,χ} (Zeta23.ThmE.lam1q).  Produced by
Zeta23/ThmDE/Traces.lean (FactsDChi ⇒ this), consumed by Zeta23/ThmDE/Endgame.lean.
-/
```

### `TracesBoundsDChi`

 **[eq:ratio-general] for L(s,χ)** with the Montgomery–Taylor window moments (a, b, J) as data:
tr1 = [eq:tr1] (window-general prop:trace); ratio/frhat carry the main term
cRatio(λ_{1,χ}; a, b, J)·N and its hat-units inverse.  Constants may depend on q. 
