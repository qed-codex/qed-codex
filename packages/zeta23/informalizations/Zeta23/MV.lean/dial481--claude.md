---
{
  "module": "Zeta23/MV.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/MV.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/MV.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/MV.lean — the Montgomery–Vaughan weighted Hilbert inequality: literature (diagonal, y = x)
form ⇒ the bilinear (x, z) form H-MV of Zeta23/Hypotheses.lean.

Purpose (trust reduction): Zeta23.MVHilbert C — what [prop:PP]/[prop:cross] consume —
is the BILINEAR inequality |Σ_{r≠s} x_r z̄_s/(λ_r−λ_s)| ≤ C (Σ|x_r|²/δ_r)^{1/2} (Σ|z_r|²/δ_r)^{1/2}.
The published theorem is the case z = x.  The paper, [lem:MV] and its proof,
verbatim: "Lemma (Montgomery–Vaughan). Let λ_1,…,λ_R be distinct real numbers and
δ_r := min_{s≠r}|λ_r−λ_s|. Then for all complex x_r, z_r,
  |Σ_{r≠s} x_r z̄_s/(λ_r−λ_s)| ≤ (3π/2)(Σ_r |x_r|²/δ_r)^{1/2}(Σ_r |z_r|²/δ_r)^{1/2}.
Proof. For z = x this is the weighted ("generalised") Hilbert inequality of Montgomery and Vaughan
[MV74, Theorem 2]; see also [Mon94, Chapter 7]. Any absolute constant in place of 3π/2 would
suffice below. In general, let H be the Hermitian matrix with entries i/(λ_r−λ_s) off the
diagonal and 0 on it, and Δ := diag(δ_r^{1/2}). The case z = x says |y*(ΔHΔ)y| ≤ (3π/2)‖y‖₂² for
all y, i.e. ‖ΔHΔ‖ ≤ 3π/2 since ΔHΔ is Hermitian; hence
|x*Hz| = |(Δ⁻¹x)*(ΔHΔ)(Δ⁻¹z)| ≤ (3π/2)‖Δ⁻¹x‖₂‖Δ⁻¹z‖₂."

Literature statement transcribed (H. L. Montgomery and R. C. Vaughan, "Hilbert's inequality",
J. London Math. Soc. (2) 8 (1974), 73–82, Theorem 2 = the "generalised" weighted form, their
(1.8)): if λ_1,…,λ_R are distinct reals, δ_r := min_{s≠r}|λ_r − λ_s|, then for all complex x_r,
  |Σ_{r≠s} x_r x̄_s / (λ_r − λ_s)| ≤ (3π/2) Σ_r |x_r|²/δ_r.
(The constant 3π/2 was later improved — Preissmann 1984 — but the paper says any absolute
constant suffices, and the headline result only needs ∃ C, so C is kept abstract: MVDiag C.)
As in Zeta23.MVHilbert we allow any admissible δ (δ_r > 0, δ_r ≤ |λ_r − λ_s| for s ≠ r); the right
side is antitone in δ, so this is equivalent to the min-gap δ of the literature.

We derive the bilinear form with constant 2C (not C) by POLARIZATION of the sesquilinear form plus
the scaling x ↦ t x, z ↦ z/t — an elementary route that avoids operator norms; the factor 2 is
immaterial (∃ C).  Result: Zeta23.MVHilbert_of_diag : 0 ≤ C → MVDiag C → MVHilbert (2 * C), and
Zeta23.exists_MVHilbert_of_diag for the ∃-forms used by PaperInputs.MV.
-/
```

### `MVDiag`

 **MV74 Theorem 2 (weighted Hilbert inequality), literature = diagonal form**, with an
abstract absolute constant C (MV74: C = 3π/2): for distinct real frequencies λ_r and admissible
gaps δ_r (0 < δ_r ≤ |λ_r − λ_s| for all s ≠ r), and all complex x_r,
  |Σ_{r≠s} x_r x̄_s/(λ_r − λ_s)| ≤ C · Σ_r |x_r|²/δ_r.
Same binder shape as Zeta23.MVHilbert with z := x. 

### `coef`

 The sesquilinear form B(x,z) := Σ_{r≠s} x_r z̄_s/(λ_r−λ_s), written with a coefficient
c_{rs} (0 on the diagonal) so that (bi)linearity is by ring. 

### `N2`

 the weighted ℓ² quantity Σ |x_r|²/δ_r. 

### `polar_term`

 Polarization, termwise (sesquilinear, two index slots):
4 a b̄' = (a+b)(a'+b')^* − (a−b)(a'−b')^* + i(a+ib)(a'+ib')^* − i(a−ib)(a'−ib')^*. 

### `B_polar`

 Polarization of B. 

### `N2_polar`

 The weighted norms of the four polarization vectors add up to 4(N2 x + N2 z)
(parallelogram law in ℂ, termwise). 

### `B_scale`

 Scaling invariance: B(t x, t⁻¹ z) = B(x, z) for real t ≠ 0. 

### `norm_B_le_add`

 Step 1: from the diagonal bound, |B(x,z)| ≤ C (N2 x + N2 z). 

### `norm_B_le_sqrt`

 Step 2: scaling + AM–GM turn C(N2 x + N2 z) into 2C √(N2 x) √(N2 z). 

### `MVHilbert_of_diag`

 **Bilinear Montgomery–Vaughan from the literature form**: MVDiag C ⇒ MVHilbert (2C)
(the paper's [lem:MV] "In general …" step, here via polarization + scaling instead of the
operator norm of ΔHΔ; constant 2C instead of C, immaterial for ∃C). 

### `exists_MVHilbert_of_diag`

 ∃-form, matching PaperInputs.MV's shape: (∃ C > 0, MVDiag C) → (∃ C > 0, MVHilbert C). 
