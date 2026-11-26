---
{
  "module": "Zeta23/XiPrime/Seam.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Seam.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Seam.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Seam.lean — the seam facts for ξ′.

Discharges `XiDerivSeam` (Zeta23/XiPrime/Statement.lean §2) given (F2):
  theorem xiDerivSeam_of_strip (hF2 : XiDerivZerosInStrip) : XiDerivSeam
((F2) is used ONLY for finite_window, via compactness of [0,1]×[T₁,T₂]; the other three fields are
unconditional theorems below), and exports the classical symmetry/analytic facts about ξ and ξ′ that
ZeroCount/** and ExplicitFormula/** consume:
  §1  ξ = s(s−1)/2 · Γℝ · ζ on Re s > 0 (s ≠ 1); Schwarz reflection ξ(s̄) = conj ξ(s) (all s);
      ξ′(1−s) = −ξ′(s), ξ′(s̄) = conj ξ′(s), and the logDeriv forms (all s, no side conditions: ξ′ entire);
  §2  ξ′ ≢ 0 (finite analytic order everywhere), multiplicity facts, reflection invariance of the order,
      finiteness of zeros in compact sets, the seam;
  §3  h(s) := s(s−1)/2·Γℝ(s), L := h′/h = Γℝ′/Γℝ + 1/s + 1/(s−1) (`Lfn`),
      ξ′ = h′ζ + hζ′ and logDeriv ξ = L + ζ′/ζ on Re s > 0, and Y := ξ′/Γℝ with its closed form
      Y = (s − 1/2)ζ + s(s−1)/2·(Γℝ′/Γℝ·ζ + ζ′)  (the object every zero-count estimate is about:
      analytic on Re s > 0, same zeros and orders as ξ′ there, polynomial growth).
-/
```

 ### §1. ξ against Γℝ·ζ; reflection symmetries of ξ and ξ′  [XF′ (F1)] 

### `xi_eq_Gammaℝ_mul_zeta`

 for Re s > 0, s ≠ 1:  ξ(s) = s(s−1)/2 · (Γℝ(s) · ζ(s)). 

### `xi_conj`

 **Schwarz reflection for ξ**: ξ(s̄) = conj ξ(s) for every s (ξ is entire and real on (1,∞)). 

### `xiDeriv_conj`

 ξ′(s̄) = conj ξ′(s). 

### `deriv_xiDeriv_conj`

 (ξ′)′(s̄) = conj (ξ′)′(s). 

### `xiDeriv_one_sub`

 **ξ′(1−s) = −ξ′(s)** (differentiate ξ(1−s) = ξ(s)). 

### `deriv_xiDeriv_one_sub`

 (ξ′)′(1−s) = (ξ′)′(s). 

### `logDeriv_xiDeriv_one_sub`

 logDeriv ξ′ (1−s) = −logDeriv ξ′ (s) — at EVERY s (at a zero both sides are 0). 

### `logDeriv_xiDeriv_conj`

 logDeriv ξ′ (s̄) = conj (logDeriv ξ′ s) — at every s. 

### `logDeriv_xiDeriv_one_sub_conj`

 the fold symmetry: logDeriv ξ′ (1 − s̄) = −conj (logDeriv ξ′ s), every s. 

### `xiDeriv_reflect`

 ξ′(1 − s̄) = −conj ξ′(s)  (Zeta23.reflect ρ = 1 − conj ρ). 

 ### §2. ξ′ ≢ 0; multiplicities; finiteness; the seam  [XF′ (F1), (F3) "locally finite"] 

### `analyticOrderAt_xiDeriv_ne_top`

 ξ′ is not identically zero near any point (else ξ would be constant, but ξ(2) = π/6 ≠ 1/2 = ξ(1)). 

### `analyticOrderNatAt_xiDeriv`

 analyticOrderNatAt ξ′ = xiDerivMult (definitional). 

### `one_le_xiDerivMult_iff`

 1 ≤ m_{ρ} ↔ ξ′(ρ) = 0. 

### `analyticOrderAt_xiDeriv_one_sub`

 the analytic order of ξ′ is invariant under s ↦ 1 − s … 

### `analyticOrderAt_xiDeriv_conj`

 … and under s ↦ s̄. 

### `xiDerivMult_reflect`

 m_{1−ρ̄} = m_ρ  [XF′ (F1)]. 

### `xiDeriv_zeros_finite_of_isCompact`

 zeros of ξ′ in a compact set are finite. 

### `finite_window_of_strip`

 under (F2) every height window is finite. 

### `xiDerivSeam_of_strip`

 **The ξ′ seam**, given (F2) (used only for finite_window). 

 ### §3. h, L = h′/h, and Y = ξ′/Γℝ  [XF′ §0, Lemma 2.1]

h(s) := s(s−1)/2 · Γℝ(s) (so ξ = h·ζ on Re s > 0, s ≠ 1), L := h′/h = Γℝ′/Γℝ + 1/s + 1/(s−1)
([XF′]'s L(s) = 1/s + 1/(s−1) − ½log π + ½ψ(s/2), via Zeta23.RvM.logDeriv_Gammaℝ), and
Y(s) := ξ′(s)/Γℝ(s).  Y is the function all the zero-count estimates of this development are about:
it is analytic on Re s > 0 with the SAME zeros and multiplicities as ξ′ there (Γℝ is analytic and
zero-free on Re s > 0), and unlike ξ′ it has only polynomial growth in |Im s| (closed form below), so
Jensen/Landau on discs centred at 2 + it inside Re s > 0 apply to it exactly as they do to ζ in
Zeta23/RvM/LocalCount.lean. 

### `Lfn`

 L(s) := Γℝ′/Γℝ(s) + 1/s + 1/(s−1)  (= h′/h). 

### `Yfn`

 Y(s) := ξ′(s) / Γℝ(s). 

### `xiDeriv_eq_of_re_pos`

 ξ′ on Re s > 0, s ≠ 1, by differentiating ξ = s(s−1)/2·Γℝ·ζ. 

### `xiDeriv_eq_Gammaℝ_mul_Yfn`

 ξ′ = Γℝ · Y on Re s > 0. 

### `Yfn_eq`

 **closed form of Y** on Re s > 0, s ≠ 1:  Y = (s − ½)ζ + s(s−1)/2 · (Γℝ′/Γℝ · ζ + ζ′). 

### `analyticOrderAt_Yfn`

 Y and ξ′ have the same analytic order on Re s > 0. 

### `Yfn_conj`

 Y(s̄) = conj Y(s). 

### `logDeriv_xiDeriv_eq`

 logDeriv ξ′ = Γℝ′/Γℝ + Y′/Y on Re s > 0 wherever ξ′ ≠ 0. 

### `logDeriv_xi_eq`

 **logDeriv ξ = L + ζ′/ζ** on Re s > 0, s ≠ 1, ζ(s) ≠ 0  [XF′ Lemma 2.1: ξ′/ξ = L − A]. 

### `xiDeriv_eq_xi_mul`

 ξ′ = ξ · (L + ζ′/ζ)  (Re s > 0, s ≠ 1, ζ(s) ≠ 0 — in particular on Re s ≥ 1)  [XF′ Lemma 2.1]. 

### `Yfn_eq_factor`

 the factorisation used on the line Re s = 2:  Y = s(s−1)/2 · ζ · (L + ζ′/ζ). 

### `xiZerosAreZetaZeros`

 in the open strip the zeros of ξ are the zeros of ζ (Statement §1's sanity Prop). 
