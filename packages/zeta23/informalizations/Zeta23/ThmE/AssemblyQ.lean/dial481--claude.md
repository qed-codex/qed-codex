---
{
  "module": "Zeta23/ThmE/AssemblyQ.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/AssemblyQ.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/AssemblyQ.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/AssemblyQ.lean — the §6 assembly generalized to conductor q.

Everything ζ-free in Zeta23/Assembly.lean that mentioned ℓ₁ = l + (2log2−1) is reproved here with
ℓ_{1,χ} = l + c_q, c_q := log q + 2log2 − 1 ([thm:E] proof (iii): "ℓ₁ replaced by ℓ_{1,χ} :=
log(qT/2π) + 2log2 − 1, and λ₁ = L/ℓ_{1,χ} → λ as q is fixed").  The matrix-level parts
(seamA, seamA_BC, BlockInputs, TailInputs), the H/F algebra and the ε-machinery of Zeta23/Assembly.lean
are reused verbatim — only the λ₁/ℓ₁-dependent steps and the prime-side identification change.
Every constant below may depend on q (q fixed; recorded for [rem:otherL](i)).
-/
```

 ## Q1. Scalars: ℓ_{1,χ} = l + c_q and λ_{1,χ} 

### `cq`

 `c_q := log q + 2 log 2 − 1`; `c_1 = c₀`. 

### `ell1q_eq`

 `ℓ_{1,χ}(T) = l(T) + c_q` for `T > 0`. 

### `Hfun_lam1q_ge`

 `H(λ_{1,χ}) ≥ H(λ) − c_q/(λ l)` (the §6 step "H(λ₁) ≥ H(λ) − 1/(λl)" with c₀ → c_q; exact
identity `H(λ) − H(λ₁) = c_q/(λl) − (λ−λ₁)/3`). 

### `Ffun_lam1q_ge`

 `F(λ_{1,χ}) ≥ F(λ) − c_q/l`. 

 ## Q2. Growth under H-RvM(χ) 

### `eventually_N_ge_chi`

 H-RvM(χ) ⇒ `N_χ(T,2T) ≥ T l /(4π)` eventually. 

### `eventually_N_le_chi`

 H-RvM(χ) ⇒ `N_χ(T,2T) ≤ K_q · T l` eventually for some constant; `K_q = 1 + c_q` works
(ℓ_{1,χ} ≤ (1 + c_q) l once l ≥ 1). 

### `eventually_clam_bounds_chi`

 `cλ_χ = 1/λ_{1,χ} + λ_{1,χ}/3` eventually in `[0, 2/λ + 1/3]`. 

 ## Q3. The prime-side identification and seam B for L(s,χ) 

### `GpChi`

 The prime-side matrix for L(s,χ) ([eq:Gdef] second expression with ν_{X,χ}), as a complex
matrix (entries real). 

### `seamBChi`

 **Seam B for L(s,χ)** (mirror of `Assembly.seamB` with ℓ₁ → ℓ_{1,χ}, λ₁ → λ_{1,χ}): given the
bridge `Z.Gz P T = GpChi`, [eq:tr1]/[eq:tr2]-χ at height T and RvM(χ) in the form
`T ℓ_{1,χ}/2π ≤ N + RN`:  `|tr Ĝ − N| ≤ C₁√X/a` and the ‖Ĝ‖_F² bound with `cλ = 1/λ_{1,χ} + λ_{1,χ}/3`. 

 ## Q4. Theorem E at fixed `λ < 1`, abstract zero configuration (mirror of Assembly Part F3/F4) 

### `thmE_A_abstract`

 **Theorem E first bound at fixed `λ ∈ (0,1)`, abstract zero configuration** ([thm:E] with §6's
proof; mirror of `Assembly.thmA_abstract` with ℓ₁ → ℓ_{1,χ}, λ₁ → λ_{1,χ}, ν_X → ν_{X,χ}).  Same
abstract inputs; all constants may depend on q. 

 ## Q5. Theorem E bounds 2 and 3 (mirror of Assembly Part F4) 

### `thmE_BC_core`

 **Theorems E.B / E.C core at fixed `λ ∈ (0,1)`, abstract zero configuration** (mirror of
`Assembly.thmBC_core` with the χ-scalars). 
