---
{
  "module": "Zeta23/RvM/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/RvM/Defs.lean — shared vocabulary for the Riemann–von Mangoldt argument.

Target: Zeta23.RiemannVonMangoldt Zeta23.zetaZeroConfig (Zeta23/Hypotheses.lean), i.e.
  main        : ∃ C T₀, ∀ T ≥ T₀, |N(T,2T) − (T/2π)·ell1 T| ≤ C log T      ([Tit86, Thm 9.4])
  local_count : ∃ A₀ ≥ 1, ∀ t, N(t,t+1] ≤ A₀ log(|t|+3)                      ([Tit86, Thm 9.2]),
                see Zeta23.RvM.zetaZeroConfig_local_count (Zeta23/RvM/LocalCount.lean).
Route for main: argument principle for Λ = completedRiemannZeta
on the rectangle [−1,2]×[T₁,T₂] at zero-free ordinates, folded onto its right half L by
Λ(1−s̄) = conj Λ(s):  N(T₁,T₂) = (1/π)·Im ∫_L Λ'/Λ;  then Λ'/Λ = ζ'/ζ + Γℝ'/Γℝ (Γℝ = Complex.Gammaℝ,
π^{−s/2}Γ(s/2)), and (1/π)·Im ∫_L Γℝ'/Γℝ = ∫_{T₁}^{T₂} μ exactly (μ = Zeta23.mu), whose asymptotic
∫_T^{2T} μ = T·ell1 T/(2π) + O(1/T) is GammaFacts.int_mu. The ζ'/ζ part is O(log T)
(Backlund on the horizontals, |log ζ| ≤ log 3 on σ = 2). Hence: riemannVonMangoldt (hΓ : GammaFacts).
-/
```

### `GoodHeight`

 T is a zero-free ordinate: no nontrivial zero of ζ has Im ρ = T. 

### `halfContour`

 The right half-contour L = [½+iT₁ → 2+iT₁ → 2+iT₂ → ½+iT₂] integral of F, as three interval
integrals (bottom rightwards, right side upwards with ds = i dt, top leftwards). 
