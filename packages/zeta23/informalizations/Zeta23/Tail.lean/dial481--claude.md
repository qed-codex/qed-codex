---
{
  "module": "Zeta23/Tail.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Tail.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Tail.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Tail.lean — Proposition [prop:tail] (the paper §4.2 "The tail"), assembled for the
concrete objects of Zeta23/Defs.lean.

Paper, verbatim: "Proposition [prop:tail]. Let A₀ ≥ 1 be an absolute constant such that
N(t+1)−N(t) ≤ A₀ log(t+3) for all t ≥ 0. Then for T ≥ T₀,
  ‖Ẽ‖ ≤ θ₀ := 4A₀ C₁² X^{1/2} log(4T)/D₀²,   C₁ := ‖φ″‖₁ = 2‖ϱ″‖₁/w,
so that θ₀ ≤ 32A₀‖ϱ″‖₁² l T^{λ/2−1} ≪ l T^{λ/2−1}. Moreover the trace norm satisfies
‖Ê‖₁ ≤ θ₀/(aL) ≤ 2θ₀/L."
Here E := G − A [eq:AE] is the contribution of the zeros with ordinate γ ∉ I' := (T−D₀, 2T+D₀],
D₀ := T^{1/2} [eq:D0] (including all zeros with γ ≤ 0), Ẽ := E/L,
Ê := E/(aL²) [eq:hatunits].

Structure of the proof (sub-files):
* Zeta23/Tail/RankOne.lean — ‖E‖, ‖E‖₁ ≤ ∑ m_ρ ‖u_ρ‖₂² for E = ∑ m_ρ u_ρ u_ρᵀ  [eq:Enormsum];
* Zeta23/Tail/Grid.lean    — ∑_{k<d} |γ−τ_k|⁻⁴ ≤ L·dist(γ,I)⁻³;
* Zeta23/Tail/Count.lean   — ∑_{γ∉I'} m_ρ dist(γ,I)⁻³ ≤ 4A₀ log(4T)/T, and N(I'∖I) ≪ D₀ l;
* this file              — [eq:hfbound] ⇒ ‖u_ρ k‖ ≤ e^{L/4}C₁|γ−τ_k|⁻², summability of the
  zero-side series entrywise, E = (the series over γ ∉ I'), and the two bounds in the exact
  shapes consumed downstream: ∀ i, |λᵢ(Ẽ)| ≤ θ₀ (for RHLinalg.weyl_posIndexAbove_le) and
  traceNorm Ê ≤ θ₀/(aL) (for [prop:zeroside-rank]).

Hypotheses taken (all proved elsewhere in the repository; none are Lean axioms):
* hloc  — PaperInputs.RvM.local (Hypotheses.lean), two-sided unit-window form;
* hdecay — [eq:hfbound] specialised to f = φ, in the exact shape of
  Zeta23.Params.norm_phiHat_sub_I_mul_le (Taper.lean), with C₁ := P.C1 T = ‖φ″‖₁;
* hEt/hEh — Hermitian-ness of Ẽ, Ê (from the ρ ↦ 1−ρ̄ symmetry).
-/
```

 ### θ₀ and its size 

### `theta0`

 θ₀ := 4 A₀ C₁² X^{1/2} log(4T)/D₀²  [prop:tail], written with K := e^{L/4}·C₁ = X^{1/4}C₁
(so K² = C₁² X^{1/2}) and D₀² = T:  theta0 A₀ K T = 4·A₀·K²·log(4T)/T. 

### `log_four_mul_le_two_mul_l`

 log(4T) ≤ 2 l = 2 log(T/2π) for T ≥ T₀ (≥ 256 ≥ 16π²; uses only π ≤ 4). 

### `theta0_le`

 The "so that" clause of [prop:tail]: with K = e^{L/4} C₁, C₁ ≤ 2‖ϱ″‖₁ (as w ≥ 1),
e^{L/2} = X^{1/2} = (T/2π)^{λ/2} ≤ T^{λ/2}, log(4T) ≤ 2l, D₀² = T:
θ₀ ≤ 32 A₀ ‖ϱ″‖₁² l T^{λ/2−1}. Stated for the concrete L = λ·l of Defs; R stands for ‖ϱ″‖₁. 

 ### The local count from PaperInputs.RvM.local 

### `LocalCount.ofWindowCount`

 From the two-sided local count on Z.N (PaperInputs.RvM.local) to the
finite-sub-family form LocalCount used by Zeta23/Tail/Count.lean, for the family of all
distinct zeros ρ ∈ Z.carrier with ordinate γ_ρ = Im ρ and multiplicity m_ρ = Z.mult ρ. 

 ### The vectors u_ρ and their decay from [eq:hfbound] 

### `uvec`

 u_ρ := (φ̂(γ_ρ − τ_k))_{0≤k<d} ∈ ℂ^d (proof of [prop:tail]; also prop:block's u_ρ). 

### `tau_fin`

 τ_k = T + k·(2π/L) as a real number, for k : Fin d. 

### `d_mul_hgrid_le`

 d·h ≤ T  (d = ⌊LT/2π⌋, h = 2π/L) [eq:fk]. 

### `tau_mem`

 "τ_0,…,τ_{d−1} ∈ [T, 2T)" [eq:fk]. 

### `norm_uvec_le`

 [eq:hfbound] ⇒ decay of the entries of u_ρ for a tail zero ρ:
"φ̂(γ_ρ−τ_k) = φ̂((γ−τ_k) − iy), |φ̂(r−iy)| ≤ e^{L/4}‖φ″‖₁|r−iy|⁻² ≤ X^{1/4}C₁ r⁻² for real
r ≠ 0" (y = β − 1/2, |y| < 1/2 as 0 < β < 1 — the only use of the strip). 

### `norm_sq_uvec_le`

 ‖u_ρ‖₂² ≤ K² · L · dist(γ,I)⁻³ for a tail zero (decay + the grid estimate). 

 ### Summability of the zero-side series and E as the series over γ ∉ I' 

### `TailHyp`

 Standing hypotheses of [prop:tail], bundled to keep signatures short. 

### `TailHyp.hloc`

 PaperInputs.RvM.local (two-sided unit-window local count). 

### `TailHyp.hdecay`

 [eq:hfbound] for f = φ, shape of Zeta23.Params.norm_phiHat_sub_I_mul_le with C₁ := P.C1 T. 

### `finite_notTail`

 The set of zeros in the window I' (complement of the tail) is finite (as a subset of the
carrier subtype). 

### `sA`

 sA := the zeros of 𝒵(I') as a Finset of the carrier subtype. 

### `K`

 K := e^{L/4} C₁. 

### `partial_sum_le`

 Finite partial sums over tail zeros: ∑ m_ρ ‖u_ρ‖₂² ≤ L·θ₀
("(eq:Enormsum) gives ‖E‖ ≤ 4A₀C₁²X^{1/2} L log(4T) D₀⁻² = Lθ₀"). 

### `summable_tail`

 ∑_{γ∉I'} m_ρ ‖u_ρ‖₂² is summable … 

### `tsum_tail_le`

 … with sum ≤ L·θ₀. 

### `summable_Gsummand`

 Each entry series ρ ↦ m_ρ φ̂(γ_ρ−τ_k)φ̂(γ_ρ−τ_l) is summable over ALL distinct zeros
(the absolute convergence of [eq:Gdef]'s first expression, here obtained from [eq:hfbound]
and the local count rather than assumed). 

### `Az_eq_sum`

 A_{kl} [eq:AE] is the finite part of the series: ∑ over the zeros of 𝒵(I'). 

### `hasSum_Ez`

 **E = ∑_{γ∉I'} m_ρ u_ρ u_ρᵀ** [eq:AE]/proof of [prop:tail]: the matrix E := G − A is the
(convergent) sum of the rank-one pieces over the tail zeros. 

### `traceNorm_smul_Ez_le`

 The scaled version: κ•E = ∑ (κ m_ρ) u_ρ u_ρᵀ, and traceNorm (κ•E) ≤ κ·L·θ₀ for κ ≥ 0. 

 ### Proposition [prop:tail] 

### `prop_tail`

 **Proposition [prop:tail]** for the concrete E := G − A of Zeta23/Defs.lean.
With θ₀ := 4A₀C₁²X^{1/2}log(4T)/D₀² (= theta0 A₀ (e^{L/4}C₁) T):
(T1) every eigenvalue of Ẽ = E/L has |λᵢ(Ẽ)| ≤ θ₀ ("‖Ẽ‖ ≤ θ₀", the hypothesis shape of
RHLinalg.weyl_posIndexAbove_le); also ‖Ẽ‖₁ ≤ θ₀;
(T2) ‖Ê‖₁ ≤ θ₀/(aL) for Ê = E/(aL²) ("Moreover the trace norm satisfies ‖Ê‖₁ ≤ θ₀/(aL)";
the further "≤ 2θ₀/L" is a ≥ 1/2, Zeta23.Params.half_le_a).
Hypotheses: T ≥ T₀ (:= 300, explicit), L ≥ 2, the local count (PaperInputs.RvM.local),
[eq:hfbound] for φ (Taper), a > 0, and Hermitian-ness of Ẽ, Ê. 

 ### E is Hermitian (real symmetric) — "since ρ and 1−ρ̄ have the same ordinate, both index
sets are invariant under ρ ↦ 1−ρ̄, so A and E are real symmetric" [eq:AE] 

### `uvec_reflect`

 conj φ̂(z̄) = φ̂(z) ("since φ̂ is real on ℝ") transports u_ρ to u_{1−ρ̄}:
u_{1−ρ̄} = conj u_ρ. 

### `TailHyp.Ez_isHermitian`

 E := G − A is Hermitian, from E = ∑_{γ∉I'} m_ρ u_ρ u_ρᵀ, m_{1−ρ̄} = m_ρ, u_{1−ρ̄} = ū_ρ. 

### `isHermitian_real_smul`

 Real scalings of a Hermitian matrix are Hermitian (for Ẽ = E/L, Ê = E/(aL²)). 

 ### Exports in the shapes consumed by Zeta23/Assembly.lean (Assembly.TailInputs) 

### `TailHyp.tailInputs`

 [prop:tail] packaged as Assembly.TailInputs at height T, with
θ₀ = theta0 A₀ (e^{L/4} C₁) T and B := ‖Ê‖₁ = traceNorm Ê. 

### `NII_le`

 N(I'∖I) = N(T−D₀,T) + N(2T,2T+D₀) ≤ 3A₀·√T·log(4T) ≤ 6A₀·D₀·l for T ≥ T₀
("N(I'∖I) ≪ D₀ l by N(t+1)−N(t) ≤ A₀log(t+3)", [prop:zeroside]). 

### `tendsto_L_atTop`

 L = λ log(T/2π) → ∞; in particular eventually L ≥ 2 (and ≥ 8w, etc.). 

### `eventually_tailInputs`

 **[prop:tail], eventually-in-T form** for thmA_abstract: given the local
count (PaperInputs.RvM.local) and, eventually in T, [eq:hfbound] for φ with constant C₁(T)
(= ‖φ″‖₁, T-independent in value but a T-dependent Lean term), a > 0 and conj φ̂(z̄) = φ̂(z)
(all three from Taper.lean), TailInputs holds eventually with
θ₀(T) = theta0 A₀ (e^{L/4} C₁(T)) T = 4A₀C₁²X^{1/2}log(4T)/T. 

### `eventually_theta0_le`

 **The "so that" clause, eventually**: if C₁(T) ≤ 2R (R = ‖ϱ″‖₁; Taper's C1_le with w ≥ 1),
then θ₀(T) ≤ 32A₀R² · l(T) · T^{λ/2−1} for T ≥ T₀; hence ∃ C, eventually θ₀ ≤ C·l·T^{λ/2−1}. 

### `eventually_NII_le`

 **N(I'∖I) ≪ D₀ l, eventually**: ∃ C, eventually N(I'∖I) ≤ C·√T·l(T) (C = 6A₀). 
