---
{
  "module": "Zeta23/XiPrime/ExplicitFormula/PrimeTermJ.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/PrimeTermJ.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/PrimeTermJ.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ExplicitFormula/PrimeTermJ.lean — the prime term of the explicit formula with COMPLEX coefficients
(generalises Zeta23.EF.prime_term of Zeta23/ExplicitFormula.lean).

For k continuous with supp k ⊆ [−L, L], 𝓕k integrable, and any c : ℕ → ℂ:
  Σ_N (c_N k(log N) + c̄_N k(−log N))/√N = ∫ h_k(τ) · P_c(e^L; τ) dτ,
  P_c(X;τ) = (1/π) Σ_{N ≤ X} (Re c_N cos(τ log N) + Im c_N sin(τ log N))/√N   (Zeta23.XiPrime.Pc),
by inversion k(u) = (1/2π)∫ h(r)e^{−iru}dr twice and  c e^{−iθ} + c̄ e^{iθ} = 2(Re c·cos θ + Im c·sin θ).
Also: integrability of h·P_c, additivity of P_c in c, P_{−Λ} = P_X (Zeta23.PX), and hence
ν_c(X) for c = C(·;Λ⋆) splits as ν_X + P_{C+Λ}(X) (nuc_xiCoeff_eq').
-/
```

### `integrable_paperFT_mul_sin`

 h(r)·sin(r y) is integrable in r when h is. 

### `integrable_paperFT_mul_trig`

 the real trigonometric combination attached to a complex coefficient. 

### `mul_cexp_add_conj_mul_cexp`

 c e^{−iθ} + c̄ e^{iθ} = 2 (Re c · cos θ + Im c · sin θ). 

### `c_mul_k_add_conj_mul_k_neg`

 **c·k(y) + c̄·k(−y) = (1/π) ∫ h(τ) (Re c · cos(τy) + Im c · sin(τy)) dτ.** 

### `complex_summand_eq_zero`

 support step: for N ∉ (0, e^L] the N-th summand vanishes (√0 = 0 in Lean for N = 0; k(±log N) = 0 for N > e^L). 

### `integrable_paperFT_mul_Pc`

 h·P_c(e^L) is integrable. 

### `prime_term_complex`

 **Prime term with complex coefficients.**  For k continuous with supp k ⊆ [−L, L], 𝓕k integrable, c : ℕ → ℂ:
Σ_N (c_N k(log N) + c̄_N k(−log N))/√N = ∫ h_k(τ) P_c(e^L; τ) dτ. 

 ### algebra of P_c 

### `Pc_neg_vonMangoldt`

 P_{−Λ}(X) = P_X. 

### `nuc_xiCoeff_eq'`

 ν_c(X) for the ξ′ coefficients c = C(·;Λ⋆) = −Λ + (C + Λ):  ν_c = ν_X + P_{C+Λ}(X). 
