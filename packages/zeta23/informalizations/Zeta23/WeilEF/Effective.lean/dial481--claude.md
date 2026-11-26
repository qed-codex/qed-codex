---
{
  "module": "Zeta23/WeilEF/Effective.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/Effective.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/Effective.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/WeilEF/Effective.lean — effective-EF extractions: explicit numeric constants for the
three remaining existential links in the EF pipeline.

E1. zeta_growth_quarter_explicit : ∀ s, 1/4 ≤ re ≤ 2 → 1 ≤ |im| → ‖ζ s‖ ≤ C₁ * |im| ^ 1
    with a named rational C₁ (the Euler–Maclaurin riemannZeta0
    pieces are all explicitly bounded inside).
E2. zeta_local_zero_count_explicit : N(t,t+1] ≤ A₀ * log(|t|+3) with named A₀
    (ZerosBound at radii (0.84, 0.95)-ish × the B from E1).
E3. mu_increment_explicit : |μ(t+r) − μ(t)| ≤ K(|r| + r²)/t with named K (from
    digamma_stirling's ≤ 3/im² remainder + the explicit main-term derivative).
-/
```

 ## E1: explicit growth constant on the quarter-strip 

### `zeta_growth_quarter_explicit`

 **E1**: ‖ζ(s)‖ ≤ (13/2)·|Im s| on 1/4 ≤ Re s (≤ 2), |Im s| ≥ 1 — the explicit form of
zeta_growth_quarter's ∃-pair: (A, C) = (1, 13/2). 

 ## E1b: the partial fraction with fully numeric constant
`zeta_logDeriv_partial_fraction_explicit` is the forall-form of
Zeta23.WeilEF.zeta_logDeriv_partial_fraction (Landau.lean) with constant 135000000: the same
proof body with the growth input specialized to A := 1, C0 := 13/2 (from
zeta_growth_quarter_explicit, `simpa [Real.rpow_one]`), so A' = max 1 0 = 1, C0 + 2 = 17/2,
and the final numeric fold
  (44795000*50/91)*(log 3 + log (17/2) + 1 + 1) <= 135000000
via log 3 <= 9/8 (3 <= e^(9/8): e*e^(1/8) >= 2.7182818*(1+1/8) = 3.058, add_one_le_exp),
log (17/2) <= log 9 = 2*log 3 <= 9/4; sum <= 43/8; 24612638*43/8 <= 132293000.


 ## E3: explicit mu-increment constant 

### `mu_eq_muq01`

 mu agrees with the chi-side muq at (kappa, q) = (0, 1). 

### `mu_deriv_bound_explicit`

 **E3a**: explicit derivative bound for the ζ-side μ: |μ′(τ)| ≤ (24/π)/|τ| for |τ| ≥ 1. 

### `mu_increment_explicit`

 **E3**: fully explicit μ-increment bound, K = 16: for t ≥ 2 and t + r ≥ 2,
|μ(t+r) − μ(t)| ≤ 16·(|r| + r²)/t.  (Both-endpoints-≥-2 is exactly what the prime-side
consumers use — the Ix-window keeps both points in [T, 2T].)  Proof: MVT with
mu_deriv_bound_explicit; for r ≥ −t/2 the whole segment has |τ| ≥ t/2 so |μ′| ≤ (48/π)/t;
otherwise t + r < t/2 forces |r| > t/2, and |μ′| ≤ 12/π on [2, ∞) gives
|Δμ| ≤ (12/π)|r| ≤ (24/π)·r²/t.  48/π ≤ 16. 

 ## E2(i): explicit local zero count away from the origin 

### `zeta_local_count_explicit_large`

 **E2(i)**: for |t + 1/2| ≥ 6, the unit-window zero count satisfies
N(t, t+1] ≤ 540000000·log(|t|+3) — explicit, via reflection halving
(zetaZeroConfig.N_le_two_mul_half) + the explicit partial-fraction count conjunct
(the half-window {Re ≥ 1/2, ordinate ∈ (t, t+1]} sits inside the counting ball
of radius (22/25)(91/50) around 2 + (t+1/2)i: distance² ≤ (3/2)² + (1/2)² < 1.6016²). 

 ## E2(iii) brick 1: the Gamma-norm bound 

### `norm_Gamma_le_Gamma_re`

 |Γ(z)| ≤ Γ(Re z) for Re z > 0 (integral representation + pointwise norm). 

### `xi`

 ξ(s) := s(s−1)/2·Λ₀(s) + 1/2 — ENTIRE by construction (Λ₀ = completedRiemannZeta₀),
and equal to s(s−1)/2·Λ(s) away from {0, 1} (algebra with Λ = Λ₀ − 1/s − 1/(1−s)). 

### `xi_one_sub`

 The ξ functional equation ξ(1−s) = ξ(s). 

### `Real_Gamma_le_24`

 Γ(x) ≤ 24 on [1/4, 5] (recurrence to [2,4] + monotonicity on [2,∞) + Γ(4) = 6, Γ(5) = 24). 

### `xi_norm_le_right`

 Pointwise bound for ξ on the right half-strip of the disk: for 1/2 ≤ Re s ≤ 10, s ≠ 1,
‖ξ(s)‖ ≤ ‖s‖/2·24·(‖s−1‖·(1/2 + ‖s‖/Re s) + 1). 

### `xi_norm_le_ball`

 Numeric ξ-bound on the counting disk: ‖ξ(s)‖ ≤ 32000 for ‖s − 2‖ ≤ 1992/250 (= 7.968). 

### `zeta_local_count_box`

 **E2(ii): the small-box count.**  For |t + 1/2| < 6, N(t, t+1] ≤ 144 (Jensen/Landau disk
for ξ at centre 2, radius 83/10, with the numeric ball bound ‖ξ‖ ≤ 32000 = 62000·‖ξ(2)‖·…). 

### `zeta_local_zero_count_explicit`

 **E2 — the fully explicit local zero count**:
N(t, t+1] ≤ 540000000·log(|t|+3) for every t ∈ ℝ, unconditionally. 
