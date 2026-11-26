---
{
  "module": "Zeta23/ThmD/Concrete.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Concrete.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Concrete.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmD/Concrete.lean — the concrete FactsD instance.
Mirror of Zeta23/PrimeSideB/Traces.lean's concreteData/concreteFacts for the Montgomery–Taylor
window (paper §7.1): plugs BridgeD (P.localFunD, localHypsCoreD_eventually) and the
Core-flipped §5 results into the DataD/FactsD interface of Zeta23/ThmD/Traces.lean, with the
[thm:D]-specific fields discharged by ThmD/PP.lean (sumA2g_close) + ThmD/Window.lean
(gD_deriv_facts, jD_close et al.).  End product: TracesBoundsD for the concrete window, via
tracesBoundsD_of_factsD.
-/
```

### `concreteDataD`

 the concrete D-data: the abstract prime-side expressions evaluated at the
Montgomery–Taylor window data P.localFunD T, plus the moment J_T of [eq:abJ]. 

### `LocalHypsCoreDEventually`

 the CoreD analogue of LocalHypsEventually (= the conclusion of
BridgeD.localHypsCoreD_eventually). 

### `evBound_of_eventuallyAtCoreD`

 the CoreD analogue of PrimeSide.evBound_of_eventuallyAt. 

### `autocorr_eq_zero_of_support`

 vanishing of the autocorrelation beyond the support width. 

### `concreteFactsD`

 **FactsD for the concrete Montgomery–Taylor data.**  Inputs: P.Valid, PaperInputs Z
(H-RvM, H-Γ, H-cheb, H-MV), and the CoreD taper facts eventually (BridgeD). 

### `tracesBoundsD_concrete`

 **TracesBoundsD for the concrete Montgomery–Taylor window.** 
