---
{
  "module": "Zeta23/XiPrime/PrimeSide/PP.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/PP.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/PP.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization; bracketed labels such as [prop:PP] refer to the paper.
-/
```


# [prop:PP] for a general-coefficient Dirichlet polynomial  (ξ′ prime side)

The ξ′ theorem's prime side ([XF′] Thm 8.1) is the paper's
§5 computation with the prime density P_X replaced by the Dirichlet polynomial with ARBITRARY complex
coefficients
    P_c(X; τ) = (1/π) Σ_{N ≤ X} (Re c_N cos(τ log N) + Im c_N sin(τ log N))/√N  = Zeta23.XiPrime.Pc X c τ
(Zeta23/XiPrime/Defs.lean).  This file evaluates the bilinear form 𝓜[P_c, P_c] = PrimeSide.Mform Φ T P_c P_c
(paper §5 "Evaluation of 𝓜": the 𝒟/𝒪₁/𝒪₂ split + Montgomery–Vaughan) ONCE for
general weights: writing c_N = ‖c_N‖ e^{i arg c_N},
    P_c(τ) = (1/π) Σ_N w_N cos(τ log N − arg c_N),   w_N := ‖c_N‖/√N,
a single family of phase-shifted cosines, so the phased kernels AminusPh/AplusPh of Zeta23/ThmE/PPChi.lean
(and everything kernel-side in Zeta23/PrimeSideB/PPKernel.lean, which is generic in the frequencies and
phases) apply verbatim.  The three estimates are proved for an ARBITRARY real weight w ≥ 0 with w 1 = 0
and arbitrary phases (section GeneralWeights), then specialised to w = ‖c‖/√· (section Results).

Main result (NON-asymptotic: one (p, F), no T₀, no coefficient hypothesis beyond c 1 = 0):

* prop_PP_c — the three-term form
    |𝓜[P_c,P_c] − (T/π) Σ_N ‖c_N‖²/N g(log N)|
        ≤ K₁(cϱ)·L·Σ‖c_N‖²/N  +  K₂·C·L·Σ‖c_N‖²  +  K₃·L·(Σ‖c_N‖/√N)²
  with K₁ = (8+8cϱ)/(2π²) (𝒟: ∫Φ²|x| ≤ (8+8cϱ)L), K₂ = 32π/(2π²) (𝒪₁: H-MV with Σ w_N²·2N = 2Σ‖c_N‖²,
  ∫Φ² ≤ 2πL), K₃ = (2π/log 2)/(2π²) (𝒪₂: |A⁺(y,y′)| ≤ 2∫Φ²/(y+y′), y, y′ ≥ log 2 — this is where
  c 1 = 0 is used: the frequency log 1 = 0 must carry zero weight);
* prop_PP_c' — the same with one constant KPP C cϱ, shaped exactly as the named input
  Zeta23.XiPrime.PPInput of Zeta23/XiPrime/PrimeSide/Concrete.lean, whose four sums
  Σ‖c‖²/N·g, Σ‖c‖²/N, Σ‖c‖², Σ‖c‖/√N are written here LITERALLY over Finset.Ioc 0 ⌊X⌋₊ (the bodies of
  sumW2g / sumSqDivW / sumSqW / S1), so that PPInput closes by defeq without this file importing the
  assembly.


 ## The magnitude/phase form of P_c 

### `re_mul_cos_add_im_mul_sin`

 Re c · cos θ + Im c · sin θ = ‖c‖ · cos(θ − arg c). 

### `wcoef`

 the general weight  w_N := ‖c_N‖/√N. 

### `Pc_eq_sum`

 The magnitude/phase form:  P_c(X; τ) = (1/π) Σ_N w_N · cos(τ·log N − arg c_N)
(mirror of ThmE.PXc_eq_sum; sign +1/π here). 

 ## [prop:PP] for a general real weight w and phases φ

Everything in this section is about the phased cosine polynomial  Q(τ) := Σ_{N≤X} w_N cos(τ log N − φ_N)
with ARBITRARY w, φ : ℕ → ℝ; the hypotheses 0 ≤ w, w 1 = 0 enter only the 𝒪₂ estimate. 

### `cosPolyPh`

 Q(τ) := Σ_{N ∈ primeRange X} w_N cos(τ log N − φ_N). 

### `Mform_cosPolyPh`

 **[eq:MPP] for Q** (mirror of Mform_PXc_PXc): bilinearity, the per-pair phased
decomposition Mform_cos_cos_ph, and the diagonal/off-diagonal split:
  𝓜[Q,Q] = ½ ( Σ_n w_n² A⁻(y_n,y_n) + Σ_{n≠m} w_n w_m A⁻_ph + Σ_{n,m} w_n w_m A⁺_ph ). 

### `diag_estimate_w`

 **𝒟 for Q** (mirror of diag_estimate): with ∫Φ²cos(xy) = 2πg(y) [eq:Phi2FT],
  |½ Σ w_n² A⁻(y_n,y_n) − πT Σ w_n² g(y_n)| ≤ ½ (Σ w_n²) ∫Φ²|x|. 

### `w_eq_zero_or_two_le`

 for n ∈ primeRange X: either n = 1 (where the weight vanishes) or 2 ≤ n. 

### `O2_estimate_w`

 **𝒪₂ for Q** (mirror of O2_estimate; "since y_n + y_m ≥ 2 log 2 the second inner
integral is O(1)"):  |Σ_{n,m} w_n w_m A⁺_ph| ≤ (∫Φ²/log 2)·(Σ w_n)², for w ≥ 0 with w 1 = 0. 

### `MV_size_le_w`

 H-MV size bookkeeping for a general weight (mirror of MV_size_le₂): if |M_n| ≤ W on the range then
  C·√(Σ (w_n M_n)²·2n)·√(Σ w_n²·2n) ≤ 2CW·Σ w_n² n   (both slot orders). 

### `MV_four`

 One H-MV application with a bounded multiplier M (|M_n| ≤ W := ∫Φ²) in either slot and either
trig function: the four shapes of off-diagonal sums met in 𝒪₁ are each ≤ 2CW·Σ w_n² n. 

### `O1_bound_w`

 **𝒪₁ for Q** (mirror of O1_bound): the exact evaluation sub_mul_AminusPh_eq splits
Σ_{n≠m} w_n w_m A⁻_ph into eight off-diagonal trigonometric sums, each an H-MV sum with one bounded
multiplier (C^∓, S^∓, all ≤ ∫Φ² in modulus):  |Σ_{n≠m} w_n w_m A⁻_ph| ≤ 16·C·(∫Φ²)·Σ_n w_n² n. 

 ## Assembly: [prop:PP] for P_c 

### `Mform_Pc_Pc`

 [eq:MPP] for P_c:  𝓜[P_c,P_c] = (1/2π²)·(𝒟-sum + 𝒪₁-sum + 𝒪₂-sum) with weights w_N = ‖c_N‖/√N and
phases arg c_N ((1/π)·(1/π) = 1/π², as (−1/π)² in the ζ case). 

### `KPP`

 the single constant of the PPInput-shaped form. 

### `prop_PP_c`

 **[prop:PP] for the general-coefficient Dirichlet polynomial P_c — three-term form.**
For ONE (p, F) under the window-generic taper hypotheses LocalHypsCore, T ≥ 1, an H-MV constant C ≥ 0,
and any c : ℕ → ℂ with c 1 = 0:
  |𝓜[P_c,P_c] − (T/π)·Σ_{N≤X} ‖c_N‖²/N·g(log N)|
      ≤ (8+8cϱ)/(2π²)·L·Σ‖c_N‖²/N  +  32π/(2π²)·C·L·Σ‖c_N‖²  +  (2π/log 2)/(2π²)·L·(Σ‖c_N‖/√N)²,
all sums over N ∈ Finset.Ioc 0 ⌊X⌋₊ (= PrimeSide.primeRange X). 

### `prop_PP_c'`

 **[prop:PP] for P_c — PPInput-shaped form** (one constant KPP C cϱ; literally the body of
Zeta23.XiPrime.PPInput in Zeta23/XiPrime/PrimeSide/Concrete.lean with K := KPP C cϱ). 
