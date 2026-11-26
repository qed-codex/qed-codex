---
{
  "module": "Zeta23/ThmDE/Concrete.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmDE/Concrete.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmDE/Concrete.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmDE/Concrete.lean — the concrete FactsDChi instance:
Zeta23/ThmE/TracesChi.lean's concreteFactsChi (the χ prime side from PaperInputsChi) re-run for the
Montgomery–Taylor window data P.localFunD T (BridgeD: LocalHypsCore eventually), with the
[eq:gbounds] sandwich replaced by the coprime partial-summation step (Zeta23/ThmDE/PP.lean) and the
window moments (a_D, b_D, J_D) kept symbolic — exactly as Zeta23/ThmD/Concrete.lean does for ζ.
End product: TracesBoundsDChi for the concrete window (tracesBoundsDChi_concrete), plus the
identification of the Params-level χ-traces of the window-realizing family P.atD with these data.
-/
```

### `atD_trGtildeChi`

 the Params-level χ prime-side traces of 'P.atD T' at height T are the abstract-layer χ-traces
of the D-data (rfl bridges + atD_localFun). 

### `concreteDataDChi`

 the concrete χ-D data: the abstract χ prime-side expressions at the Montgomery–Taylor window
data P.localFunD T, plus J_T [eq:abJ] and the coprime sum. 

### `autocorr_eq_zero_of_support`

 vanishing of the autocorrelation beyond the support width. 

### `concreteFactsDChi`

 **FactsDChi for the concrete Montgomery–Taylor data of L(s,χ).** Inputs: P.Valid, 1 ≤ q,
unimodular coefficients, PaperInputsChi (H-RvM(χ), H-Γ(χ), H-cheb, H-cheb-coprime, H-MV), and the
CoreD taper facts eventually (BridgeD). 

### `tracesBoundsDChi_concrete`

 **TracesBoundsDChi for the concrete Montgomery–Taylor window and L(s,χ).** 
