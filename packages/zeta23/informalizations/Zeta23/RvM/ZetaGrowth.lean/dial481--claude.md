---
{
  "module": "Zeta23/RvM/ZetaGrowth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/ZetaGrowth.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/ZetaGrowth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/RvM/ZetaGrowth.lean — growth of ζ in vertical strips (consumed by the Landau/Jensen
local zero count and the Backlund S(T) bound).

CONTENT:
* `norm_riemannZeta_le_of_re_pos` — the explicit half-plane bound
      ‖ζ(s)‖ ≤ 1/2 + 1/‖1 − s‖ + ‖s‖ / Re s        (0 < Re s, s ≠ 1),
  from the N = 1 case of the summation-by-parts representation
      ζ(s) = Σ_{n≤N} n^{-s} − N^{1−s}/(1−s) − N^{−s}/2 + s ∫_N^∞ (⌊x⌋ + 1/2 − x) x^{−s−1} dx
  [Tit86, (2.1.4) / §2.1], which is `riemannZeta0` / `Zeta0EqZeta` in the PrimeNumberTheoremAnd
  port Zeta23/FromPNTPlus/ZetaBounds.lean (Apache-2.0, see README § Provenance).
* `riemannZeta_linear_growth` — for every δ > 0:  ‖ζ(σ+it)‖ ≤ (5/2 + δ⁻¹)·|t|  (σ ≥ δ, |t| ≥ 1)
  [Tit86, §5.1: ζ(s) = O(|t|) uniformly in σ ≥ δ], and the ∃-constant corollaries
  (`zeta_growth`, `zeta_growth_quarter`).
* `norm_riemannZeta_sub_one_le` — ‖ζ(s) − 1‖ ≤ π²/6 − 1 for Re s ≥ 2, hence the two-sided bounds
  0 < 2 − π²/6 ≤ ‖ζ(s)‖ ≤ π²/6 there (the Jensen/Landau disc centre 2 + it needs ζ ≠ 0 and a
  lower bound at the centre) [Tit86, §9.2 uses |ζ(2+iT)| ≥ … > 0].
* `analyticOnNhd_riemannZeta` — ζ is analytic on any set avoiding 1 (Mathlib's
  differentiableAt_riemannZeta, repackaged for the Jensen hypotheses).

NOT here: anything for Re s ≤ 0 (that needs the functional equation + Γ-ratio growth, i.e.
Stirling); no consumer in this repository needs it (σ ≥ 1/4 suffices).
-/
```

 ## Analyticity away from the pole 

### `analyticOnNhd_riemannZeta`

 ζ is analytic on a neighbourhood of every set not containing 1. 

 ## The half-plane bound  [Tit86, (2.1.4) with N = 1] 

### `norm_riemannZeta_le_of_re_pos`

 **Explicit half-plane bound.** For 0 < Re s and s ≠ 1,
‖ζ(s)‖ ≤ 1/2 + 1/‖1 − s‖ + ‖s‖ / Re s.
Proof: `Zeta0EqZeta` (PNT+ port) with N = 1 gives ζ(s) = 1/2 − 1/(1−s) + s∫_1^∞ (⌊x⌋+1/2−x)x^{−s−1}dx,
and `ZetaBnd_aux1b` bounds the integral by 1/Re s. 

 ## Linear growth in σ ≥ δ  [Tit86, §5.1] 

### `riemannZeta_linear_growth`

 **Linear growth of ζ in every right half-plane σ ≥ δ > 0**, explicit constant:
‖ζ(s)‖ ≤ (5/2 + δ⁻¹)·|Im s| for Re s ≥ δ, |Im s| ≥ 1. 

### `zeta_growth`

 ∃-constant form: for every δ > 0 there is C > 0 with
‖ζ(s)‖ ≤ C·|Im s| whenever Re s ≥ δ and |Im s| ≥ 1. 

### `zeta_growth_quarter`

 Polynomial-growth form (the shape used in Zeta23/WeilEF/Landau.lean):
∃ A C, 0 < C ∧ ∀ s, 1/4 ≤ Re s → Re s ≤ 2 → 1 ≤ |Im s| → ‖ζ s‖ ≤ C·|Im s|^A  (we give A = 1;
the upper constraint on Re s is not used). 

### `zeta_growth_right_at`

 **Consumer interface (Zeta23/RvM/LocalCount.lean).** Polynomial growth to
the right of σ = 0.15, uniform down to small |Im s| as long as s keeps distance ≥ 1 from the pole:
∃ A C, 0 < C ∧ ∀ s, 0.15 ≤ Re s → 1 ≤ ‖s − 1‖ → ‖ζ s‖ ≤ C·(|Im s| + 3)^A.  (We give A = 1, C = 20/3.) 

 ## Bounds on Re s ≥ 2 (the Jensen disc centre)  

### `norm_riemannZeta_sub_one_le`

 For Re s ≥ 2: ‖ζ(s) − 1‖ ≤ Σ_{n≥2} n^{−2} = π²/6 − 1. 

### `pi_sq_div_six_sub_one_lt_one`

 π²/6 − 1 < 1 (π < 3.15 ⇒ π² < 9.93 < 12). 

### `norm_riemannZeta_ge_of_two_le_re`

 Lower bound at the Jensen disc centre: 0 < 2 − π²/6 ≤ ‖ζ(s)‖ for Re s ≥ 2. 

### `one_third_lt_two_sub_pi_sq_div_six`

 1/3 < 2 − π²/6 (π < 3.15 ⇒ π²/6 < 1.654). 

### `zeta_lower_bound_two`

 **Consumer interface.** ‖ζ(2 + it)‖ ≥ 1/3 for all real t. 

### `riemannZeta_ne_zero_of_two_le_re`

 ζ does not vanish on Re s ≥ 2 (of course Mathlib has this for Re s ≥ 1:
`riemannZeta_ne_zero_of_one_le_re`; restated for convenience). 

### `norm_riemannZeta_le_of_two_le_re`

 Upper bound on Re s ≥ 2: ‖ζ(s)‖ ≤ π²/6. 
