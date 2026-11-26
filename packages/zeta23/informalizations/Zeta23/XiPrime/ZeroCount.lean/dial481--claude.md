---
{
  "module": "Zeta23/XiPrime/ZeroCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ZeroCount.lean — the Riemann–von Mangoldt formula for the zeros of ξ′.

  theorem xiDeriv_riemannVonMangoldt (hF2 : XiDerivZerosInStrip) (hs : XiDerivSeam) : XiDerivRvM hF2 hs
i.e. Zeta23.RiemannVonMangoldt (xiDerivZeros hF2 hs):
  main        : ∃ C T₀, ∀ T ≥ T₀, |N_{ξ′}(T,2T) − (T/2π)·ℓ₁(T)| ≤ C log T      ([XF′ (F3)]: N_{ξ′} = N + O(log))
  local_count : ∃ A₀ ≥ 1, ∀ t, N_{ξ′}(t,t+1] ≤ A₀ log(|t|+3)                 (ZeroCount/Landau.lean).
Route for main (the Zeta23/RvM route for ζ, with Y := ξ′/Γℝ in place of ζ): argument principle for the
entire function ξ′ on [−1,2]×[T₁,T₂] at good heights, folded onto the right half-contour L by
ξ′(1−s̄) = −conj ξ′(s) (ZeroCount/Contour.lean):  N_{ξ′}(T₁,T₂) = (1/π)·Im ∫_L ξ″/ξ′;  on L,
ξ″/ξ′ = Γℝ′/Γℝ + Y′/Y (Seam.logDeriv_xiDeriv_eq); (1/π)·Im ∫_L Γℝ′/Γℝ = ∫_{T₁}^{T₂} μ EXACTLY
(Zeta23.RvM.gamma_side), whose asymptotic is GammaFacts.int_mu (a theorem: Zeta23.gammaFacts); the Y′/Y part
is O(log T) (ZeroCount/Sides.lean: horizontals by Landau's partial fraction, vertical by three argument
pieces).  (F2) enters only through the ZeroConfig (window geometry / no zeros on Re s = −1, 2).
-/
```

 ### splitting ξ″/ξ′ = Γℝ′/Γℝ + Y′/Y along the half-contour 

 ### the Y′/Y part of the half-contour is O(log T) 

 ### the main term 

### `xiDeriv_rvM_main`

 **Riemann–von Mangoldt main term for ξ′**: |N_{ξ′}(T,2T) − (T/2π)ℓ₁(T)| ≤ C log T for T ≥ T₀
(instance of ZeroCount/GenericRvM.rvM_main_of: good heights, the argument principle + fold, the split
ξ″/ξ′ = Γℝ′/Γℝ + Y′/Y with the Y-part O(log T), and the local count). 

### `xiDeriv_riemannVonMangoldt`

 **H-RvM for the zeros of ξ′** ([XF′ (F3)], rendered as Zeta23.RiemannVonMangoldt for the ξ′ configuration):
both the main count N_{ξ′}(T,2T) = (T/2π)ℓ₁(T) + O(log T) and the two-sided local count. 

### `xiDeriv_riemannVonMangoldt'`

 the same, with the seam discharged: only (F2) remains as a hypothesis. 
