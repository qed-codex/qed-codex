---
{
  "module": "Zeta23/XiPrime/Inputs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Inputs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Inputs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

### `coeffMoments_flat_D1`

 **P1 for the flat family at the tree's taper**, for any coefficient family with density D₁
(xiCoeffFamily and wCoeffFamily both qualify by rfl), from its (H1)–(H3) and prop:PP for P_c. 

### `coeffMoments_quartic_D1`

 **P1 for the QUARTIC family** Pf := (paramsOf ϱ λ).atV vQuartic, any coefficient family with density D₁:
combines `coeffMoments_atV`, `admFamily_atV_quartic`, and `tendsto_cRatio_quartic_D1`. 

### `coeffMoments_quartic_xi`

 P1 for ξ′, quartic window. 

### `coeffMoments_flat_xi`

 P1 for ξ′ (b_N = C(N; L_T)), flat window. 

### `coeffMoments_flat_w`

 P1 for Z′ (coefficients C(N; ½ l)), flat window. 

 ## P2 — the two-trace transfer, via xiTraceTransfer_of

Remaining inputs: the explicit formula XiEF Z Pf and the coefficient
re-expansion Reexpansion F e ρ₀ A T₀.  Everything else xiTraceTransfer_of
asks for is discharged here: P.Valid, λ/w constancy (rfl), LocalHypsCore eventually (flat:
localHypsCore_eventually ∘ admFamily_taper; quartic: localHypsCoreQ_eventually
transported along atV_toSetting / atV_localFun), H-Γ, a ≥ 1/2 (WindowZeroSide.a_half), H-RvM, and PPUpper
(frobSq_Ppart_le at PPInput := ppInput_of_PP, with H-MV := Zeta23.MV.mv_hilbert). 

### `traceTransfer_flat`

 **P2 for the flat family.** 

### `traceTransfer_quartic`

 **P2 for the quartic family.** 

### `traceTransfer_flat_w`

 **P2 for Z′ (W), flat family**, obtained from `wTraceTransfer_of` and `wReexpansion`; the one
remaining input is the W explicit formula `WEF Z Pf` (see StatementW.lean). 

### `coeffMoments_quartic_w`

 P1 for Z′, quartic window. 

### `traceTransfer_quartic_w`

 **P2 for Z′ (W), quartic family.** 
