---
{
  "module": "proof/rates/GeneralPieces/GenF/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Lemma 9, the close of the paragraph «Generating functions»: the expansion of f₊ and f₋

The paragraph "Generating functions" ends with the display on the two orders (`stTwoOrders`).
Comparing the coefficients of x^μ·x'^ν in it gives the expansion of f₊ and f₋ (`stExpansion`): the
left sides are f₊ and f₋
(`stY`), the coefficients of e^κ and e^κ' are numbers times powers of ε₊ and ε₋
(`coeff_expW_kap_false`, `coeff_expW_kap_true`), and the coefficients of ⟨𝒩⟩ lie in 𝓛 (`stN1`,
`stN2`, `stN3`). 

### `stExpansion`

 f₊ and f₋ are the same combination of powers of ε₊, or ε₋, times elements of 𝓛. 
