---
{
  "module": "Zeta23/XiPrime/Hardy/ZeroFree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/ZeroFree.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/ZeroFree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 ## §1. Algebra: L₋, and ζ′/ζ + L₂ = ξ′/ξ − L₋ 

### `Lm`

 L₋(s) := ½(L(s) − L(1−s))  (L = Seam.Lfn = Γℝ′/Γℝ + 1/s + 1/(s−1)). 

### `logDeriv_Gammaℝ_offreal`

 Γℝ′/Γℝ(s) = −½log π + ½ψ(s/2) at every non-real s (Zeta23.RvM.logDeriv_Gammaℝ off the half-plane). 

### `Lm_eq`

 L₋(s) = 1/s + 1/(s−1) + ¼[ψ(s/2) − ψ((1−s)/2)] off the real axis. 

### `L2_eq_digamma`

 L₂(s) = −½log π + ¼[ψ(s/2) + ψ((1−s)/2)] off the real axis. 

### `logDeriv_zeta_add_L2`

 ζ′/ζ + L₂ = ξ′/ξ − L₋ on Re s > 0, s ∉ ℝ, ζ(s) ≠ 0. 

### `hardyW_eq_mul`

 W = ζ·(ζ′/ζ + L₂) wherever ζ ≠ 0. 

 ## §2. Stirling, real parts 

### `norm_digamma_sub_log_le`

 ‖ψ(z) − log z‖ ≤ 4 for Re z > 0, |Im z| ≥ 1. 

### `re_digamma_ge`

 Re ψ(z) ≥ log|Im z| − 4 for Re z > 0, |Im z| ≥ 1. 

### `digamma_add_nat_offreal`

 iterated functional equation off the real axis: ψ(z + n) = ψ(z) + Σ_{k<n} 1/(z + k). 

### `re_digamma_half_one_sub_ge`

 Re ψ((1−s)/2) ≥ log(|Im s|/2) − 5 for Re s ≥ 1, |Im s| ≥ 2 (iterate down from Re ∈ (1/2, 3/2]). 

### `re_L2_ge`

 Re L₂(σ+it) ≥ ½ log|t| − C for σ ≥ 1, |t| ≥ 2. 

### `abs_re_Lm_le`

 |Re L₋(σ+it)| ≤ C/t² for 1 ≤ σ ≤ 2, |t| ≥ 4. 

 ## §3. The zero sum: Re ξ′/ξ(σ+it) ≥ N_T/(8t²) 

### `NT`

 N_T := number of nontrivial zeros ρ of ζ with |Im ρ| ≤ T, counted with multiplicity. 

### `sum_mult_one_sub_re`

 reflection symmetry of the multiset:  Σ_{|γ|≤T} m_ρ (1 − β_ρ) = Σ_{|γ|≤T} m_ρ β_ρ,  hence = N_T/2. 

### `re_logDeriv_xi_ge`

 Re ξ′/ξ(σ+it) ≥ N_T/(8t²) for 1 ≤ σ ≤ 2 and |t| ≥ max(2, 2T). 

### `exists_NT_ge`

 N_T → ∞ (Riemann–von Mangoldt). 

 ## §4. W ≠ 0 on Re s ≥ 1, |Im s| ≥ t₀ 

### `wZerosInStrip_holds`

 **(Z6), unconditionally**: there is a height t₀ > 0 above which every zero of W = ζ′ + L₂ζ lies in the
open critical strip 0 < Re s < 1. 
