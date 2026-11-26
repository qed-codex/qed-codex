---
{
  "module": "Zeta23/ThmD/BridgeD.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/BridgeD.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/BridgeD.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmD/BridgeD.lean — the Montgomery–Taylor window is an admissible window:
`AdmWindow (phiD ϱ λ L w) L w (cDT ϱ λ)`, using the estimates of Zeta23/ThmD/Window.lean;
the §5 local hypotheses for the D-data then come from Zeta23/ThmD/WindowCore.lean.
-/
```

### `admWindow_phiD`

 **The Montgomery–Taylor window is admissible** (paper §7.1, sentence 1: even, C_c²,
same support, ‖φ_D'‖₁, ‖(φ_D²)'‖₁ ≤ 2, second-derivative norms ≪ 1/w). 

 ## Params-level wrappers (the D-analogue of `Params.localFun`) 

### `_root_.Zeta23.Params.phiD`

 the Montgomery–Taylor window of the parameter set `P` at height `T`. 

### `_root_.Zeta23.Params.localFunD`

 its abstract local data `(φ̂_D, Φ_D, A_{φ_D}, g_D, a_D, b_D)`. 

 ## `b_D ≥ 1/2` for large `L/w`, and the eventual `LocalHypsCore` for the D-data 

### `bStar_ge`

 `b* = 1/2 + sin(2ϑ)/(4ϑ) ≥ 1/2 + 1/π` (Jordan's inequality; `2ϑ = √2 λ ≤ √2 < π/2`). 

### `bv_phiD_ge_half`

 for the Montgomery–Taylor window, `b_D ≥ 1/2` as soon as `L ≥ 4π w` (|b_D − b*| ≤ 4w/L). 

### `localHypsCoreD_eventually`

 **The D-analogue of `Bridge.localHypsEventually`:** for all large `T`, the Montgomery–Taylor
data `P.localFunD T` satisfy §5's `LocalHypsCore` with constant `cDT`. 
