---
{
  "module": "Zeta23/XiPrime/PrimeSide/Moments.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/Moments.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/Moments.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization.

Zeta23/XiPrime/PrimeSide/Moments.lean — ξ′ generalised-coefficient prime side: the
Params-level hat-unit bridge to Statement.lean's 'CoeffMoments'.

CoeffMoments Z Pf F κ: for every δ > 0, eventually
  (1−δ)N ≤ tr M̂ᵀ ≤ (1+δ)N  and  ‖M̂ᵀ‖²_F ≤ (κ+δ)N,
with M̂ᵀ = (Pf T).hat T ((Pf T).GpC T (F.c T)), N = N(T,2T) of Z.  Here: tr M̂ᵀ = tr G̃/(aL) and
‖M̂ᵀ‖²_F = tr G̃²/(aL)² (Zeta23/Assembly Part D, verbatim for the general-coefficient matrix), so the
package TracesBoundsXi of the concrete data (Concrete.lean) plus the window limit
cRatio(λ₁; a_T, b_T, J_T) → c∞ > 0 (XiPrime/Window.lean) give CoeffMoments with
κ = c∞⁻¹.  Stated once for any height-indexed family Pf whose scalars are P's and whose taper data
are those of the window (Pf T).phi T — both 'fun _ => P' (flat) and 'P.atV v' (profile v)
satisfy the three bookkeeping identities by rfl.
-/
```

 ## Entrywise identification of the statement-layer matrices with the abstract-layer traces 

### `_root_.Zeta23.Params.GpCW`

 The fixed-coefficient prime-side matrix with pole weight `cΠ` (`GpC` is the case `cΠ = 1` by rfl;
the Z′ layer uses `cΠ = 2`). 

### `rtrace_tilde_GpCW`

 `tr M̃ᵀ` computed entrywise. 

### `frobSq_tilde_GpCW`

 `‖M̃ᵀ‖²_F` computed entrywise. 

### `MomentsW`

 the CoeffMoments sentence with a general pole weight (`CoeffMoments Z Pf F κ` is the case
`cΠ = 1`, by rfl): for every δ > 0, eventually `(1−δ)N ≤ tr M̂ ≤ (1+δ)N` and `‖M̂‖²_F ≤ (κ+δ)N`. 

 ## CoeffMoments from the trace package and the window limit 

### `momentsW_of_family`

 **CoeffMoments for a height-indexed parameter family** whose scalars are `P`'s and whose taper
data at height `T` are those of the window `(Pf T).phi T` (the three identities hold by `rfl` for
`Pf := fun _ => P` and for `Pf := P.atV v`).  Inputs: P.Valid, λ < 1, the window family is admissible
(Zeta23.AdmWindow, b ≥ 1/2) eventually, CoeffFamily.Hyps, H-Γ, H-MV, [prop:PP] for P_c (PPInput),
H-RvM for `Z`, and the window limit `cRatio(λ₁; a_T, b_T, J_T) → c∞ > 0`.  Output: `CoeffMoments Z Pf Fam c∞⁻¹`. 

### `coeffMoments_of_family`

 **CoeffMoments (pole weight 1) for a height-indexed parameter family** — the statement as a `Prop`. 

### `coeffMoments_flat`

 **CoeffMoments, flat window** (`Pf := fun _ => P`; the window is the tree's own taper `P.phi T`,
admissible with constant `cW` — XiPrime/Window.lean's admWindow_taper gives `cW = P.crho`). 

### `coeffMoments_atV`

 **CoeffMoments, window profile v** (`Pf := P.atV v`; the window at height T is `(P.atV v T).phi T`,
whose eventual admissibility is the hypothesis `hwin`). 
