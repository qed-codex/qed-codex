---
{
  "module": "Zeta23/ThmE/PrimeSideChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/PrimeSideChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/PrimeSideChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 ## Definitions: the χ-analogues of GentryA / trGtA / trGt2A / MtotalA 

### `GentryChiA`

 `G_{kl}` for L(s,χ), abstract-taper form (mirror of `GentryA` with `ν_{X,χ}`). 

### `trGtChiA`

 `tr G̃` for L(s,χ) (abstract). 

### `trGt2ChiA`

 `tr G̃²` for L(s,χ) (abstract). 

### `MtotalChiA`

 `𝓜` for L(s,χ): the bilinear form of [eq:Mdef] with `ν_{X,χ}` in both slots. 

 ## The six §5-χ obligations (proofs mirror Zeta23/PrimeSideA.lean) 

 ## The large-T regime for χ: elementary consequences 

### `muq_abs_le`

 From H-Γ(χ)'s Stirling bound: `|μ_χ| ≤ C·l` on `[T, 2T]` for large `T` (C = C(κ,q)). 

### `PXc_abs_le`

 `|P_{X,c}(τ)| ≤ √X` for `X` large (mirror of `PX_abs_le`; only `‖c‖ ≤ 1` is used). 

 ## The P-part Fourier identities for χ (Core-typed; phases via the complex Dirichlet kernel) 

### `integral_phiHat_sq_mul_sin_core`

 Core copy of `integral_phiHat_sq_mul_sin` (the original is typed over full `LocalHyps`). 

### `integral_phiHat_sq_mul_cos_shift_core`

 Core copy of `integral_phiHat_sq_mul_cos_shift`. 

### `integral_phiHat_sq_re_twist_core`

 `∫ φ̂(r)² Re(z·e^{−i(t+r)y}) dr = 2π A_φ(y)·Re(z e^{−ity})` — the phase-twisted Fourier identity. 

 ## μ_χ increments and positivity (mirrors of the ζ-side lemmas; constants depend on κ, q) 

### `muq_linear_bound`

 Crude global bound: |μ_χ(τ)| ≤ M + |τ| (mirror of mu_linear_bound; q enters only M). 

### `muq_increment_bound`

 Increment bound (mirror of mu_increment_bound, unified K(|r| + r²)/t shape). 

### `muq_nonneg_eventually`

 μ_χ ≥ 0 far out (mirror of mu_nonneg_eventually; uses q ≥ 1 ⇒ log(qτ/2π) ≥ log(τ/2π)). 

 ## The complex Dirichlet kernel bound (mirror of the cosine-kernel lemmas) 

### `abs_sin_mul_norm_geom_le`

 `|sin(θ/2)|·‖Σ_{k<d} e^{ikθ}‖ ≤ 1` (geometric sum; complex mirror of
`abs_sin_mul_abs_sum_cos_le`). 

### `Aphi_mul_norm_tauKernel_le`

 Mirror of Aphi_mul_sum_cos_le for the complex kernel: A_φ(y)·‖Σ_{k<d} e^{−iτ_k y}‖ ≤ L²/(2 log 2). 

### `integral_phiHat_sq_mul_sin_shift_core`

 sin-analogue of the shifted Fourier identity. 

### `P_part_chi_eq`

 **P-part of [prop:trace] for χ at one grid point** (cos/sin-split form):
    ∫ φ̂(r)² P_{X,c}(t+r) dr = −2 Σ_{n≤X} a_n A_φ(log n)·((c n).re cos(t log n) + (c n).im sin(t log n)). 

### `PXc_continuous`

 `P_{X,c}` is continuous in τ. 

 ## Diagonal decomposition and the trace bounds for χ 

### `muq_part_bound`

 μ_χ-part bound at one grid point (mirror of mu_part_bound, K(|r|+r²)/t shape). 

### `muq_part_integrable`

 Integrability of φ̂(r)² μ_χ(t+r). 

### `PXc_part_integrable`

 Integrability of φ̂(r)² P_{X,c}(t+r) (bounded × integrable). 

### `GentryChiA_diag_eq`

 Diagonal decomposition for χ: G_kk = μ_χ-part + P-part (no Π). 

### `sum_P_part_chi_bound`

 Sum of the P-parts over the grid (mirror of sum_P_part_bound via the complex kernel). 

### `prop_trace_chi`

 **[prop:trace] for L(s,χ)** ([thm:E] (iii); no Π-part, μ → μ_{κ,q}, ℓ₁ → ℓ_{1,χ}):
`tr G̃ = aL·N + O_q(L√X)` for any `N` with `|N − Tℓ_{1,χ}/2π| ≤ A log T` (the H-RvM(χ) main shape).
Constants depend on (cϱ, λ, A, κ, q, the H-Γ(χ)/H-cheb constants). 

### `eq_Msplit_chi`

 **[eq:Msplit] for L(s,χ)**: three terms only (`Π_X ≡ 0`):
`𝓜 = 𝓜[μ_χ,μ_χ] + 𝓜[P,P] + 2𝓜[μ_χ,P]`. 

### `muq_nuBound`

 μ_χ satisfies the `NuBound` μ-part: `|μ_χ(τ)| ≤ C₀·l + log⁺(|τ|/4T)` for large `T`
(three ranges: |τ| ≤ 1 via the linear bound; 1 ≤ |τ| ≤ 4T and |τ| > 4T via Stirling). 

### `lem_ends_chi`

 **[lem:ends] for L(s,χ)**: `tr G̃² = 𝓜 + O_q(L·l·log l·(l² + X))` (same error shape as ζ:
`B_χ = ℓ_{1,χ} + 4√X ≤ C_q(l + √X)` and the ψ-tail machinery is coefficient-independent). 
