---
{
  "module": "Zeta23/GammaFacts/StirlingVert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/GammaFacts/StirlingVert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/GammaFacts/StirlingVert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/GammaFacts/StirlingVert.lean — Stirling for the digamma function on vertical lines.  Target: the H-Γ field `GammaFacts.stirling`
  "μ(τ) = (1/2π) log(|τ|/2π) + O(τ⁻²)  (|τ| ≥ 1)"   [eq:mufacts]
via the COMPLEX asymptotic  ψ(w) = log w − 1/(2w) + O(1/(Im w)²)  for 0 < Re w ≤ 1,
|Im w| ≥ 1, proved from the partial-fraction series (Zeta23.DigammaSeries)
WITHOUT Euler–Maclaurin:  on each unit interval
   1/(x+w) = 1/(m+w) − (x−m)/(m+w)² + (x−m)²/((m+w)²(x+w))        (exact algebra),
so ∫_m^{m+1} dx/(x+w) = 1/(m+w) − 1/(2(m+w)²) + ε_m, |ε_m| ≤ 1/(3|m+w|²|Im w|), while the
left side is log(m+1+w) − log(m+w) (FTC for Complex.log on the slit plane) and telescopes.
-/
```

 ### ℂ-specialized interval-integral constant rules (the RCLike-generic Mathlib versions do
not match ℂ's default instance path under `rw`; cf. Zeta23.integral_const_mul_C) 

 ### Elementary bounds for points in the right half-plane 

### `abs_im_le_norm_add`

 for `x ≥ 0` real and `0 < re w`: `‖x + w‖ ≥ |im w|`. 

 ### The antiderivative `F(x) = log(x + w)` on `[0, ∞)` 

### `integral_inv_add_eq_log_sub`

 FTC: `∫_m^{m+1} dx/(x+w) = log(m+1+w) − log(m+w)` for `m ≥ 0`. 

 ### The per-interval expansion 

### `inv_add_expand`

 exact algebra: `1/(x+w) = 1/(m+w) − (x−m)/(m+w)² + (x−m)²/((m+w)²(x+w))`. 

### `eps`

 the per-interval remainder `ε_m(w) := ∫_m^{m+1} (x−m)²/((m+w)²(x+w)) dx`. 

### `integral_inv_add_eq`

 `∫_m^{m+1} dx/(x+w) = 1/(m+w) − 1/(2(m+w)²) + ε_m`. 

### `norm_eps_le`

 bound: `‖ε_m‖ ≤ 1/(3 ‖m+w‖² |im w|)`. 

 ### The sequence `z_n := n + 1 + w` 

### `natp1_cast`

 cast alignment with the real-parametrized lemmas. 

### `inv_natp1_eq`

 (I1) `1/z_n = [log z_{n+1} − log z_n] + (1/2)/z_n² − ε_{n+1}`. 

### `rho`

 the second-order telescoping remainder `ρ_n := 1/(z_n² z_{n+1})`. 

### `inv_natp1_sq_eq`

 (I2) `1/z_n² = (1/z_n − 1/z_{n+1}) + ρ_n`. 

### `partial_sum_eq`

 (I3) the partial sums of the digamma series, rearranged. 

 ### Bounds: `Σ_{n<N} 1/‖z_n‖² ≤ 2/|im w|` by a real telescoping 

 ### Summability of the remainders and tsum bounds 

 ### Limits 

### `tendsto_harmonic_sub_clog`

 `Σ_{n<N} 1/(n+1) − log(N+1+w) → γ`. 

 ### The exact identity and the Stirling bound 

### `digamma_eq`

 **Exact**: `ψ(w) = log(1+w) − 1/w − 1/(2(1+w)) − ½Σρ + Σε` for `0 < re w`, `|im w| ≥ 1`. 

### `log_one_add_sub_log`

 `log(1+w) − log w = 1/w − 1/(2w²) + ε_0`. 

### `digamma_stirling`

 **Stirling for ψ on the right half-plane strip**:
`‖ψ(w) − log w + 1/(2w)‖ ≤ 3 / (im w)²` for `0 < re w`, `|im w| ≥ 1/2`. 

 ### Real part on vertical lines, and the H-Γ field for μ 

### `re_digamma_stirling`

 `|Re ψ(a+it) − ½ log(a²+t²)| ≤ 4/t²` for `0 < a ≤ 1`, `|t| ≥ 1/2`
(Re log w = log ‖w‖ = ½log(a²+t²); |Re 1/(2w)| = a/(2(a²+t²)) ≤ 1/(2t²)). 

### `re_digamma_stirling'`

 and with `log |t|` in place of `½log(a²+t²)`: error `≤ (4 + a²/2)/t² ≤ 5/t²`. 

### `mu_stirling`

 **H-Γ [eq:mufacts], Stirling clause** in the exact shape of `Zeta23.GammaFacts.stirling`:
`|μ(τ) − (1/2π) log(|τ|/2π)| ≤ C/τ²` for `|τ| ≥ 1`, with `C = 20/(2π) ≤ 4`. 
