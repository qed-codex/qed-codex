---
{
  "module": "Zeta23/XiPrime/Hardy/EFContour/Rectangle.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFContour/Rectangle.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFContour/Rectangle.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/EFContour/Rectangle.lean — the rectangle identities at a fixed height R for the two W-integrands.

Rectangle Q := [1−c, c] × [−R, R], 1 < c ≤ 5/4, R > 0; z = (1−c) − iR, w = c + iR (the FullLine/Limit convention);
H = WeilEF.Hfn k (entire).  Every identity is the POLE-FREE weighted argument principle
Zeta23.Analytic.rectangleIntegral'_mul_logDeriv (f analytic on Q, f ≠ 0 on ∂Q, zeros of f in Q listed) applied to:
  G := (Γℝ)⁻¹ (entire; zeros in Q: {0}, simple)                         ⇒ (1/2πi)∮ H·G′/G       = H(0)
  G∘(1−·)     (entire; zeros in Q: {1}, simple)                         ⇒ (1/2πi)∮ H·(G∘(1−·))′/… = H(1)
  q := s(s−1) (FullLine.mulSubOne; zeros 0,1 simple)                    ⇒                          H(0) + H(1)
  p := s(s−1)² (Poles.polarPoly; zeros 0 simple, 1 double)              ⇒                          H(0) + 2H(1)
  Wreg := p·W filled in at 0,1 (Poles.Wreg; analytic on Q; zeros = W's off {0,1}, same orders) ⇒ Σ_{W(ρ)=0} ord_ρ(W)·H(ρ)
and on ∂Q (no point of ∂Q is 0 or 1, and W ≠ 0 on ∂Q by hypothesis):
  Γℝ′/Γℝ = −G′/G,  (Γℝ′/Γℝ)(1−s) = (G∘(1−·))′/(G∘(1−·))(s),  L₂ = ½[Γℝ′/Γℝ(s) + Γℝ′/Γℝ(1−s)],  1/s + 1/(s−1) = q′/q,
  W′/W = Wreg′/Wreg − p′/p.  Hence
  rect_Lminus : (1/2πi)∮ H·(Lfn − L₂)   = ½(H(0) + H(1)),
  rect_FZ     : (1/2πi)∮ H·(L₂ + W′/W)  = Σ_{ρ∈Q, ρ∉{0,1}, W(ρ)=0} ord_ρ(W)·H(ρ) − (3/2)(H(0) + H(1)).
-/
```

 ### §1. The rectangle: corners, membership, border 

### `zc`

 lower-left corner (1−c) − iR. 

### `wc`

 upper-right corner c + iR. 

### `re_bounds_of_mem`

 points of the closed rectangle lie in the strip −2 < Re < 3. 

### `border_ne_zero_one`

 0 and 1 are interior points; no border point is 0 or 1. 

 ### §2. The four explicit pieces 

### `rect_invGammaℝ`

 (a) (1/2πi)∮ H·G′/G = H(0). 

### `rect_invGammaℝ_one_sub`

 (b) (1/2πi)∮ H·(G∘(1−·))′/(G∘(1−·)) = H(1). 

### `rect_mulSubOne`

 (c) (1/2πi)∮ H·q′/q = H(0) + H(1), q = s(s−1). 

 #### the polar polynomial p = q · (s−1) 

### `differentiable_subOne`

 s ↦ s − 1. 

### `subOne`

 the second factor, as a named function to keep elaboration syntactic. 

### `analyticOrderAt_of_nat`

 from a (nonzero) natural order back to the ℕ∞ order. 

### `rect_polarPoly`

 (d) (1/2πi)∮ H·p′/p = H(0) + 2·H(1). 

 ### §3. The W piece 

### `rect_Wreg`

 (e) (1/2πi)∮ H·Wreg′/Wreg = Σ_{ρ ∈ Q, ρ ∉ {0,1}, W(ρ)=0} ord_ρ(W)·H(ρ), provided W ≠ 0 on ∂Q. 

 ### §4. The border identities and linear combination 

### `L2_border`

 on ∂Q:  L₂ = ½ (G∘(1−·))′/(G∘(1−·)) − ½ G′/G. 

### `Lminus_border`

 on ∂Q:  Lfn − L₂ = −½ G′/G − ½ (G∘(1−·))′/(G∘(1−·)) + q′/q. 

### `FZ_border`

 on ∂Q (W ≠ 0 there):  L₂ + W′/W = ½ (G∘(1−·))′/… − ½ G′/G + Wreg′/Wreg − p′/p. 

### `borderIntegrable_of_continuousOn`

 H·φ is integrable along ∂Q when φ is continuous at every border point. 

### `continuousOn_logDeriv_border`

 logDeriv f is continuous on ∂Q when f is analytic and nonzero at every border point. 

### `rect'_lincomb`

 linearity of the normalised rectangle integral in the test integrand (four-term form). 

### `rect_Lminus`

 **(1/2πi)∮ H·(Lfn − L₂) = ½(H(0) + H(1)).** 

### `rect_FZ`

 **(1/2πi)∮ H·(L₂ + W′/W) = Σ_{W(ρ)=0 in Q, ρ ∉ {0,1}} ord_ρ(W)·H(ρ) − (3/2)(H(0) + H(1))**, if W ≠ 0 on ∂Q. 
