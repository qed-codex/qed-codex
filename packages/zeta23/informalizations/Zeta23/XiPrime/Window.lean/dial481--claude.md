---
{
  "module": "Zeta23/XiPrime/Window.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Window.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Window.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Window.lean — the window functional c_λ(v; D) and its limits.

[XF′] Thm 8.1/8.2, Remark 7.2.  Objects (Zeta23/XiPrime/Defs.lean §4):
  vConv v r   = (v⋆v)(r) = ∫_{-1/2}^{1/2−r} v(s)v(s+r) ds,
  jWin D λ v  = 𝒥_D(λ;v) = 2∫₀¹ D(λr)(v⋆v)(r) dr,
  cWin D λ v  = c_λ(v;D) = λ(∫v)²/(∫v² + λ·𝒥_D(λ;v)),      kappaXi λ v = 1/c_λ(v;D₁).
This file is the ξ′ analogue of Zeta23/ThmD/{Limit,Window}.lean (there D(s) = s, v = v*):
 (W1) algebra/positivity: ThmD.cRatio λ (∫v) (∫v²) (𝒥/λ) = c_λ(v;D); c > 0;
 (W2) the abstract T → ∞ limit the prime side consumes (CoeffMoments):
      λ₁(T) → λ, a_T → ∫v, b_T → ∫v², J_T → 𝒥_D(λ;v)/λ  ⟹  cRatio(λ₁(T); a_T, b_T, J_T) → c_λ(v;D),
      and J_T → 𝒥/λ from a POINTWISE autocorrelation comparison |g_T(y) − L·(v⋆v)(y/L)| ≤ C·w on [0,L]
      (J_T := (2/L³)·l·∫₀ᴸ D(y/l)·g_T(y) dy, the prime-side definition verbatim; since L = λ·l EXACTLY,
      D(y/l) = D(λ·y/L) and no continuity of D in λ is needed for this step);
 (W3) the FLAT window end to end: a_T, b_T → 1 and J_T → 𝒥_D(λ;1)/λ for the tree's own taper P.phi;
 (W4) continuity of λ ↦ c_λ(v;D), κ₁(λ,v) on (0,1] ([XF′ Remark 7.2]: "c_λ(v) is continuous in λ ∈ (0,1]
      (a ratio of integrals of the continuous D₁ against v⊗v)") and the λ → 1⁻ devices: from a STRICT
      inequality at λ = 1 to some λ ∈ [1/2,1) (for the ε-free CertFlat/CertQuartic), and the ε-step
      (for the limit form);
 (W5) WindowProfile vFlat / vQuartic (Statement.lean §4).
-/
```

 ## (W1) algebra and positivity 

### `cRatio_eq_cWin`

 the tree's ratio constant at J := 𝒥_D(λ;v)/λ IS c_λ(v;D). 

### `vConv_nonneg`

 (v⋆v) ≥ 0 on [0,1] when v ≥ 0 on the window. 

### `jWin_nonneg`

 𝒥_D(λ;v) ≥ 0 for 0 ≤ λ ≤ 1, D ≥ 0 on [0,1], v ≥ 0 on the window. 

### `cWin_pos`

 c_λ(v;D) > 0 for 0 < λ ≤ 1 when ∫v ≠ 0, ∫v² > 0, 𝒥 ≥ 0. 

 ## (W2) the abstract T → ∞ limit 

### `tendsto_cRatio_cWin`

 generic ratio limit (mirror of ThmD.Limit.tendsto_cRatio_of): any λ₁-like sequence → λ and any data
→ (∫v, ∫v², 𝒥_D(λ;v)/λ) give cRatio → c_λ(v;D). 

### `continuous_vConv`

 (v⋆v) is continuous when v is (parametric interval integral with moving endpoint). 

### `tendsto_JT_of_autocorr_close`

 **J_T → 𝒥_D(λ;v)/λ** from a pointwise autocorrelation comparison, where
J_T := (2/L³)·l·∫₀ᴸ D(y/l)·g_T(y) dy.  Hypotheses: D continuous on [0,1]; v continuous; eventually g_T is
continuous and |g_T(y) − L·(v⋆v)(y/L)| ≤ C·w for y ∈ [0, L]. 

 ## (W3) the flat window, concretely (the tree's taper P.phi; v = vFlat) 

### `kappaXi_vFlat`

 κ₁(λ, flat) = 1/λ + 2∫₀¹ D₁(λr)(1−r) dr  (the ζ analogue is Zeta23.kfun λ = 1/λ + λ/3). 

### `tendsto_a_flat`

 a_T → 1 = ∫ vFlat for the flat taper. 

### `tendsto_b_flat`

 b_T → 1 = ∫ vFlat² for the flat taper. 

### `g_flat_close`

 the flat autocorrelation is within 2w of the sharp one: |g(y) − (L − y)| ≤ 2w on [0, L]. 

### `tendsto_JT_flat`

 **J_T → 𝒥_D(λ; flat)/λ** for the flat taper. 

### `tendsto_cRatio_flat`

 **the flat-window ratio limit**, packaged for CoeffMoments:
cRatio(λ₁(T); a_T, b_T, J_T) → c_λ(1; D) for the tree's taper, any continuous D ≥ 0 on [0,1]. 

 ## (W4) continuity in λ and the λ → 1⁻ devices 

### `continuous_jWin`

 λ ↦ 𝒥_D(λ;v) is continuous (D, v continuous). 

### `continuousOn_cWin`

 λ ↦ c_λ(v;D) is continuous on [0,1] (D ≥ 0 on [0,1], v continuous and ≥ 0 on the window, ∫v² > 0). 

### `continuousOn_inv_cWin`

 λ ↦ κ(λ) := 1/c_λ(v;D) is continuous on (0,1]. 

### `continuousOn_kappaXi`

 **κ₁(·, v) is continuous on (0,1]** for any continuous v ≥ 0 on the window with ∫v ≠ 0. 

### `exists_lt_one_pos`

 from a strict inequality at λ = 1 to one at some λ ∈ [1/2, 1): if f is continuous on [1/2,1]
and 0 < f 1 then 0 < f λ for some λ ∈ [1/2,1). 

### `eps_form_of_continuousOn`

 the λ → 1⁻ ε-step (ξ′ analogue of ThmD.Limit.eps_form_cStar, continuity in place of Lipschitz):
if a rate g is continuous on [1/2,1] and the ε-statement holds with constant g λ at every λ ∈ [1/2,1),
it holds with constant g 1. 

 ## (W5) the two profiles are admissible WindowProfiles 

### `continuousOn_kappaXi_vFlat`

 κ₁(·, vFlat) and κ₁(·, vQuartic) are continuous on (0,1]. 
