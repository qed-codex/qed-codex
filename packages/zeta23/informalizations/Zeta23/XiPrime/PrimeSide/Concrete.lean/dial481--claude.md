---
{
  "module": "Zeta23/XiPrime/PrimeSide/Concrete.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/Concrete.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/Concrete.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization.

Zeta23/XiPrime/PrimeSide/Concrete.lean — ξ′ component, generalised-coefficient prime side: the
CONCRETE FactsXi instance.

Inputs:  P : Params with P.Valid and λ < 1;  an ADMISSIBLE WINDOW FAMILY win T (Zeta23.AdmWindow
at scale (P.L T, P.w), b ≥ 1/2 — the flat taper and the quartic window are instances, produced by
XiPrime/Window.lean);  a COEFFICIENT FAMILY with CoeffFamily.Hyps (XiPrime/Statement.lean §3;
XiPrime/Coeff.lean proves it for C(N; L_T), D₁);  the pole weight cΠ (1 for ξ′, 2 for Z′);  any
count Ncnt with Ncnt = Tℓ₁/2π + O(l);  H-Γ;  H-MV;  and [prop:PP] for P_c as the named input
'PPInput' (discharged by Zeta23/XiPrime/PrimeSide/PP.lean).
Output: FactsXi for the concrete data, hence (Traces.lean) TracesBoundsXi and the δ-form moments.
-/
```

 ## Named coefficient sums and the [prop:PP] input 

### `sumW2g`

 the diagonal `Σ_{N≤X} ‖c_N‖²/N · g(log N)` 

### `sumSqDivW`

 `Σ_{N≤X} ‖c_N‖²/N` 

### `sumSqW`

 `Σ_{N≤X} ‖c_N‖²` 

### `PPInput`

 **[prop:PP] for P_c as a named input** (the 𝒟/𝒪₁/𝒪₂ split + Montgomery–Vaughan for a
Dirichlet polynomial with arbitrary coefficients; proved in Zeta23/XiPrime/PrimeSide/PP.lean):
for every H-MV constant `C` and taper class `cϱ` there is `K` with, for all (p, F) under LocalHypsCore,
`T ≥ 1`, and all `c` with `c 1 = 0`:
`|𝓜[P_c,P_c] − (T/π)·Σ‖c_N‖²/N·g(log N)| ≤ K·L·(Σ‖c‖²/N + Σ‖c‖² + S₁(c)²)`. 

 ## The concrete data 

### `AdmFamily`

 an admissible window family at scale `(P.L T, P.w)` with `b ≥ 1/2`, eventually in `T`. 

### `Fw`

 taper data of the window at height `T`. 

### `concreteData`

 the concrete ξ′ prime-side data for (P, window family, coefficient family, pole weight). 

 ## Eventual facts: regime, taper hypotheses, coefficient sizes 

### `localHypsCore_eventually`

 the taper hypotheses of §5 for the window family, eventually. 

### `S1_eventually`

 S₁ ≤ C₁ √X · l at x = X, eventually (from H1). 

### `sumSq_eventually`

 Σ‖c‖² ≤ C₂ X l² at x = X, eventually (from H2). 

### `D_bound`

 a bound for the density on [0,1]. 

### `sumSqDiv_eventually`

 Σ‖c‖²/N ≤ C₃ l² at x = X, eventually (from H3 with ε = 1 and the boundedness of D). 

### `gv_deriv_facts`

 C¹ facts for the window moment `g = v² ⋆ v²` of an admissible window. 

 ## The concrete FactsXi 

### `eventually_of_core`

 generic bridge: an EventuallyAtCore-type bound, specialised to the window family, is an
eventual pointwise bound in T. 

### `concreteFacts`

 **FactsXi for the concrete data.** 

### `tracesBoundsXi_concrete`

 **The ξ′ two-trace package for the concrete data** (window family × coefficient family). 
