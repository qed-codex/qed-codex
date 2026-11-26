---
{
  "module": "Zeta23/WeilEF/Landau.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/Landau.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/Landau.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/WeilEF/Landau.lean

Landau's lemma (Borel–Carathéodory + Jensen route; Mathlib: Analysis/Complex/BorelCaratheodory,
JensenFormula): zero counts and the partial-fraction expansion of f'/f on disks, specialized to ζ.
`zeta_local_zero_count` is consumed downstream as `RiemannVonMangoldt.local_count`.
-/
```

### `Cf_ne_zero`

 Cf never vanishes on the closed ball over which the zeros were divided out. 

### `f_eq_prod_mul_Cf`

 Away from the zero set, `f = Π (z−ρ)^{m_ρ} · Cf`. 

### `logDeriv_zero_prod`

 logDeriv of the finite zero product: `logDeriv (Π (·−ρ)^{m_ρ}) z = Σ m_ρ/(z−ρ)`
(Mathlib's `logDeriv_prod` + `logDeriv_fun_pow`). 

### `logDeriv_split`

 logDeriv splits into the zero sum plus the regular part, at non-zeros inside the divided
ball. 

### `norm_logDeriv_Cf_le`

 Borel–Carathéodory bound for the regular part: with zeros divided over ‖ρ‖ ≤ 22/25 and
‖f‖ ≤ B on ‖z‖ ≤ 24/25 (f(0) = 1, 2 ≤ B), `‖logDeriv (Cf (22/25) f) z‖ ≤ 44795000 log B` on
‖z‖ ≤ 83/100. 

### `logDeriv_partial_fraction_unit`

 **Landau partial fraction, unit-disk form**: f analytic on the closed unit disk, f(0) = 1,
‖f‖ ≤ B on ‖z‖ ≤ 24/25 (2 ≤ B), finite zero set.  Then for ‖z‖ ≤ 83/100 with f(z) ≠ 0,
logDeriv f z is the sum of m_ρ/(z−ρ) over zeros with ‖ρ‖ ≤ 22/25, up to an error ≤ 44795000 log B. 

### `finite_SetOfZeros`

 The zero set of an analytic function (nonvanishing at the centre) in the closed unit ball is
finite. 

### `logDeriv_partial_fraction_disk`

 **Landau partial fraction on a general disk** (affine rescaling of the unit version):
f analytic on a neighbourhood of closedBall s₀ R, f(s₀) ≠ 0, ‖f‖ ≤ B·‖f(s₀)‖ on the (24/25)R-ball,
2 ≤ B.  The zero set in the (22/25)R-ball is a finite set Z, and on the (83/100)R-ball (off zeros)
logDeriv f is Σ_{ρ ∈ Z} m_ρ/(s−ρ) up to 44795000·(log B)/R. 

### `zeta_logDeriv_partial_fraction`

 **Partial fraction for ζ'/ζ at height t** (|t| ≥ 6): there is a finite set Z — exactly the
ζ-zeros within distance (22/25)·(91/50) of 2+it — such that on the ball of radius 3/2 around
2+it (covering 1/2 ≤ Re s ≤ 2 at height t), away from zeros,
ζ'/ζ(s) = Σ_{ρ ∈ Z} m_ρ/(s−ρ) + O(log(|t|+3)). 
