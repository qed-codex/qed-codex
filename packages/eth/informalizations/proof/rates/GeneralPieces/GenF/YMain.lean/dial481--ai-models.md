---
{
  "module": "proof/rates/GeneralPieces/GenF/YMain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/YMain.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/YMain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 9 (Appendix B), on the operators Q_s: f₊ = ⟨Y(a, ω₁)·Y(b, ω₂)⟩ as a coefficient of ⟨e^{A⁺}e^{A⁻}·e^{B⁺}e^{B⁻}⟩

The expansions e^{B⁺}e^{B⁻} = Σ_ν x'^ν·Y(t^ν, ω₂)/ν! and e^{A⁺}e^{A⁻} = Σ_μ x^μ·Y(t^μ, ω₁)/μ! are
put into the form of the interface statements `StY1`, `StY1'`, `StOp0`, `StY2` and `StXo`, and
composed by `stY_of`. 

### `stY`

 μ!·ν! times the coefficient of x^μ·x'^ν in ⟨e^{A⁺}e^{A⁻}·e^{B⁺}e^{B⁻}⟩ is f₊ = ⟨Y(a, ω₁)·Y(b,
ω₂)⟩. 
