---
{
  "module": "proof/variables/VariableBound/Printed/VariablesA/Setting.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Printed/VariablesA/Setting.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Printed/VariablesA/Setting.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sentence on n₀ of «Setting and parameters»

`settingN0 : ParamIneq → SettingN0Stmt`, with n₀ = 2^((640·C₀²)²). Write y = log n and t = y^(1/4).
Then k ≤ t, log log n = 4·log t ≤ 4t, so log Δ ≤ 4·k·C₀·log log n ≤ 16·C₀·t², and this is at most
y/(40C₀) = t⁴/(40C₀) as soon as
t² ≥ 640·C₀². Then log(2Δ) ≤ 1 + y/40, so that n ≥ 29·log(2Δ) + 19, which is the condition under
which `VariableBound.ParamIneq.large` has display (61). 

### `lg_le_id`

 log t ≤ t for t > 0. 

### `settingN0`

 «Setting and parameters», the sentence on n₀, from the inequalities of that paragraph
(`VariableBound.ParamIneq`, of which only display (61) under n ≥ 29·log(2Δ) + 19 is used). 
