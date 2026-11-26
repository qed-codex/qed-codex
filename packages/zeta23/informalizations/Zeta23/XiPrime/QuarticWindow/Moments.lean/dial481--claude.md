---
{
  "module": "Zeta23/XiPrime/QuarticWindow/Moments.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/QuarticWindow/Moments.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/QuarticWindow/Moments.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/QuarticWindow/Moments.lean — the moments of the quartic window vs their scale-free limits
(consumed by the J_T limit in Zeta23/XiPrime/Window.lean).

With φ_Q := P.phiV vQuartic T (= phiM (fQ L) φ), φ_Q² = v(u/L)·φ(u)² on the core and φ differs from the sharp
cutoff 1_{[−L/2,L/2]} only on the two ramps of width w (the generic edge estimate of Zeta23/ThmD/Window.lean,
copied here since it is private there):
  aV_quartic_close :  |a_V − ∫v|  = |L⁻¹∫φ_Q² − 2777/3000|     ≤ 2w/L,
  bV_quartic_close :  |b_V − ∫v²| = |L⁻¹∫φ_Q⁴ − 518783/600000| ≤ 2w/L,
  gV_quartic_close :  |g_{φ_Q}(y) − L·vConv vQuartic (y/L)| ≤ 4w  for y ∈ [0, L]  (g = φ_Q² ⋆ φ_Q²),
hence b_V ≥ 1/2 (already at 8w ≤ L) and the eventual §5 LocalHypsCore for the quartic data
(localHypsCoreQ_eventually).
-/
```

 ### generic edge estimate and scaling 

### `integral_scale`

 substitution: ∫_{−L/2..L/2} g(u/L) du = L · ∫_{−1/2..1/2} g. 

 ### φ_Q² and the profile 

### `mQ`

 the squared modulating factor, globally: m u := max 0 (v(u/L)) = f_Q² ∈ [0,1]. 

 ### a and b 

### `aQ_close`

 |L⁻¹∫φ_Q² − ∫v| ≤ 2w/L. 

### `bQ_close`

 |L⁻¹∫φ_Q⁴ − ∫v²| ≤ 2w/L. 

 ### the autocorrelation vs the sharp one 

### `sharpQ`

 the sharp window 1_{[−L/2,L/2]}·v(·/L). 

### `integral_abs_phiMQsq_sub_sharp`

 ‖φ_Q² − sharp‖₁ ≤ 2w. 

### `autocorr_phiMQsq_close`

 **|g_{φ_Q}(y) − L·vConv vQuartic (y/L)| ≤ 4w for y ∈ [0, L]** (g = φ_Q² ⋆ φ_Q²). 

 ### Params-level exports 

### `bV_quartic_ge_half`

 b_V ≥ 1/2 (indeed ≥ 518783/600000 − 1/4) as soon as 8w ≤ L. 

### `localHypsCoreQ_eventually`

 The §5 `LocalHypsCore` for the quartic data. 
