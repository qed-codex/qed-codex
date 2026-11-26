---
{
  "module": "Zeta23/Taper/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper/Basic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23 — Taper/Basic.lean.  Definitions of the test family
[subsec:family] for generic parameters (ϱ : ℝ → ℝ) (L w : ℝ), and the basic facts of the sentence
after [eq:phidef].  Bodies are literally those of Zeta23/Defs.lean so that
P.phi T = Taper.phi P.ϱ (P.L T) P.w etc. are rfl (bridges in Zeta23/Taper.lean).

Sub-file map (umbrella = Zeta23/Taper.lean):
  Basic   — defs, support/plateau/evenness/C³
  Norms   — [eq:phinorms], [eq:abdef], c_ϱ, C₁, smoothstep
  Strip   — [eq:hfbound] specialized to φ
  Decay   — [eq:gbounds], [eq:psidef], [eq:psiints]
  Fourier — φ̂, Φ real/even/continuous, [eq:PhigA] facts, Plancherel, [eq:Phi2FT]
  Zeta23/Taper.lean — umbrella + the consumer-facing `Params` layer
-/
```

 ### Constants depending only on ϱ  [eq:phinorms] 

### `supDeriv`

 `‖ϱ'‖_∞`. 

### `l1Deriv2`

 `‖ϱ''‖₁`. 

### `cRho`

 [eq:phinorms]: "`c_ϱ := 4‖ϱ'‖_∞ + 4‖ϱ''‖₁ (≥ 4)`".  Body literally equal to `Params.crho`. 

### `smoothstep`

 A concrete admissible profile, witnessing that `TaperProfile` is inhabited: Mathlib's
`Real.smoothTransition` (C^∞, monotone, `0` on `(−∞,0]`, `1` on `[1,∞)`).  Not used by the
paper, which fixes an arbitrary ϱ.  (A polynomial C³ smoothstep `x⁴(35 − 84x + 70x² − 20x³)`
would make the constants `‖ϱ'‖_∞ = 35/16`, `‖ϱ''‖₁ = 35/8` numeric; nothing downstream needs
numeric values, so the library function is used.) 

 ### The taper φ [eq:phidef], a, b [eq:abdef], Φ, g, A_φ [eq:PhigA], ψ [eq:psidef] 

### `phi`

 [eq:phidef]: "`φ(u) := ϱ((L/2 − |u|)/w)`, `u ∈ ℝ`". 

### `aConst`

 [eq:abdef]: "`a := L⁻¹ ∫ φ²`". 

### `bConst`

 [eq:abdef]: "`b := L⁻¹ ∫ φ⁴`". 

### `phiHat`

 `φ̂(z) = h_φ(z) = ∫ φ(u) e^{izu} du` (paper convention, complex argument). 

### `phiHatR`

 `φ̂` on the real line as a real number. 

### `Phi`

 [eq:PhigA]: "`Φ := (φ²)^`" (complex argument). 

### `PhiR`

 `Φ` on the real line as a real number. 

### `g`

 [eq:PhigA]: "`g := φ² ⋆ φ²`", `(v ⋆ v)(y) := ∫ v(u) v(u+y) du`. 

### `Aphi`

 [eq:PhigA]: "`A_φ := φ ⋆ φ`". 

### `psi`

 [eq:psidef]: "`ψ(r) := min(L, 2/|r|, c_ϱ/(w r²))` (`r ∈ ℝ`)".  At `r = 0` the paper's
value is `L` (the other two entries are `+∞`); this is made explicit because Lean's
`2 / 0 = 0`. 

 ### Basic properties of φ (the sentence after [eq:phidef]):
"`φ ∈ C_c³(ℝ)` is even, `0 ≤ φ ≤ 1`, `supp φ = [−L/2, L/2]`, `φ = 1` on `[−L/2+w, L/2−w]`" 

### `phi_eq_zero`

 `φ(u) = 0` for `|u| ≥ L/2`. 

### `phi_eq_one`

 `φ = 1` on `[−L/2 + w, L/2 − w]`. 

### `phi_eq_mul`

 Product form of the taper, valid when `2w ≤ L`: `φ(u) = ϱ((L/2−u)/w)·ϱ((L/2+u)/w)`.
(For `u ≥ 0` the second factor is `1` since `(L/2+u)/w ≥ L/(2w) ≥ 1`; symmetrically for
`u ≤ 0`.)  This is how we prove `φ ∈ C³` despite the `|u|` in [eq:phidef]. 

### `phi_contDiff`

 "`φ ∈ C_c³(ℝ)`". 

### `C1`

 `C₁ := ‖φ''‖₁` [prop:tail]. 
