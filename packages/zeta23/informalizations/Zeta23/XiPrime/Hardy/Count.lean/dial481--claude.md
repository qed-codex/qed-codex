---
{
  "module": "Zeta23/XiPrime/Hardy/Count.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/Count.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/Count.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/Count.lean — Riemann–von Mangoldt for the non-real zeros of W.

  riemannVonMangoldt_W (hZ : WZerosInStrip t₀) (hs : WSeam t₀) : RiemannVonMangoldt (wZeros hZ hs)
i.e. |N_W(T,2T) − (T/2π)ℓ₁(T)| ≤ C log T (T ≥ T₀) and the two-sided local count N_W(t,t+1] ≤ A₀ log(|t|+3).
Route: the local count and the horizontal O(log T) bounds are the generic two-line Landau/Jensen
machine (Zeta23/XiPrime/ZeroCount/Generic.lean) instantiated at f := W with the inputs of Hardy/TwoLine.lean; the main
term comes from the argument principle for Ω = Γℝ·W (Hardy/Contour.lean): N_W = (1/π)Im∫_L Ω′/Ω, Ω′/Ω = Γℝ′/Γℝ + W′/W,
the Γℝ-part and the μ-bookkeeping being the generic ZeroCount/GenericRvM.rvM_main_of (Zeta23.RvM.gamma_side), and the W-part O(log T)
(horizontals: Generic; the vertical Re s = 2: W = ζ·(ζ′/ζ + L₂) with each factor of positive real part there, so
each turns by at most π — Zeta23/XiPrime/ZeroCount/ArgBound.lean + vertical_two).
-/
```

 ### the vertical side Re s = 2: W = ζ·G, G := ζ′/ζ + L₂ 

### `Gw`

 G := ζ′/ζ + L₂ (so W = ζ·G where ζ ≠ 0). 

### `logDeriv_hardyW_eq_of_zeta_ne`

 W = ζ·G near any non-real point where ζ ≠ 0; hence logDeriv W = ζ′/ζ + G′/G there (if also G ≠ 0). 

### `vertical_boundW`

 **the vertical side**: for t₁ from hardyW_two_line_lower and t₁ ≤ T₁ ≤ T₂,
|Im ∫_{T₁}^{T₂} (W′/W)(2+it)·i dt| ≤ 2π. 

 ### the Generic two-line machine at f := W 

### `hardyW_generic_inputs`

 the packaged Generic hypotheses for W (t₁ from the two-line lower bound). 

### `horizontal_boundW`

 **horizontal sides**: |Im ∫_{1/2}^{2} (W′/W)(σ+iT) dσ| ≤ C log(|T|+3) at good heights |T| ≥ t₁. 

### `local_countW`

 **local count** for any ZeroConfig whose carrier consists of non-real W-zeros with m = wMult. 

 ### splitting Ω′/Ω = Γℝ′/Γℝ + W′/W along the half-contour 

 ### the W-part of the half-contour is O(log T) 

 ### the main term 

### `hardyW_rvM_main`

 **Riemann–von Mangoldt main term for W**: |N_W(T,2T) − (T/2π)ℓ₁(T)| ≤ C log T for T ≥ T₀
(instance of ZeroCount/GenericRvM.rvM_main_of: Zc := wZeros, Good := GoodHeightW, Λ := Ω, residual = the W half-contour). 

### `riemannVonMangoldt_W`

 **H-RvM for the non-real zeros of W** (|Im| ≥ t₀): main count + two-sided local count. 

### `riemannVonMangoldt_W'`

 with the seam discharged: only the strip hypothesis (and t₀ > 0) remain. 
