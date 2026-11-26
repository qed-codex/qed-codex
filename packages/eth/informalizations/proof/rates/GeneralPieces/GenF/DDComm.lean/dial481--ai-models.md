---
{
  "module": "proof/rates/GeneralPieces/GenF/DDComm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/DDComm.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/DDComm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 9 (the operators Q_s), proof, paragraph "Generating functions": differentiations commute with each other

The derivations J_n^-(ω_1) of the paper (written J_n^-(u) here, with u in the place of ω_1) of the
polynomials in the t_k commute, because they map every t_k to a constant; so do the operators that
stand beside the variables in A⁻. 

### `JmU_comm`

 J_n^-(u) and J_m^-(u) commute. 

### `DD_comm`

 The operators that stand beside the variables in A⁻ commute. 
