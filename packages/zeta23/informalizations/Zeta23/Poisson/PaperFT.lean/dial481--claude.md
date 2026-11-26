---
{
  "module": "Zeta23/Poisson/PaperFT.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Poisson/PaperFT.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Poisson/PaperFT.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
The paper's Fourier convention and the bound [eq:hfbound].

Reference: the paper, §2.1 [subsec:weil].
-/
```

 `Zeta23.paperFT (f : ℝ → ℂ) (z : ℂ) : ℂ := ∫ u, f u * cexp (I * z * u)` is defined in
`Zeta23/Defs.lean`: the paper's convention [subsec:weil] "h_f(z) := f̂(z) = ∫ f(u) e^{izu} du",
sign `+i`, no `2π`, complex argument.  This file supplies the dictionary to Mathlib's `𝓕`
(`∫ f(v) e^{-2πi v w} dv`) and the decay bound [eq:hfbound]. 

 Mathlib's `integral_const_mul` / `integral_mul_const` are stated for a general `RCLike L`,
and their instance path (RCLike-derived `NormedAddCommGroup ℂ`) does not match the
directly-synthesized `Complex.instNormedAddCommGroup` under `rw`'s reducible unification.
These ℂ-specialized restatements (same proofs) rewrite reliably. 

### `paperFT_ofReal_eq_fourier`

 Convention dictionary: for REAL argument `s`,
`h_f(s) = 𝓕 f (-s / (2π))` where `𝓕` is Mathlib's Fourier transform. 

### `fourier_eq_paperFT`

 Equivalent form of the dictionary: `𝓕 f w = h_f(-2π w)`. 

 ### [eq:hfbound]

"`|h_f(x+iy)| ≤ e^{|y|Λ_f} min(‖f‖₁, ‖f''‖₁ |x+iy|⁻²)`, `supp f ⊂ [−Λ_f, Λ_f]`, by two integrations
by parts (`h_f(z) = (iz)⁻² ∫ f''(u) e^{izu} du` and `|e^{izu}| = e^{−yu} ≤ e^{|y|Λ_f}` on
`supp f`)."  We prove the two bounds separately, in multiplied-out form. 

### `norm_paperFT_le`

 [eq:hfbound], zeroth order: `supp f ⊆ [−Λ, Λ]` ⇒ `‖h_f(z)‖ ≤ e^{|Im z| Λ} ‖f‖₁`. 

### `paperFT_deriv`

 One integration by parts: `(f')^(z) = −iz · f̂(z)` for `f ∈ C_c¹`. 

### `paperFT_deriv_deriv`

 Two integrations by parts: `(f'')^(z) = −z² · f̂(z)`, i.e. "`h_f(z) = (iz)⁻² ∫ f''(u)e^{izu} du`". 

### `norm_paperFT_mul_sq_le`

 [eq:hfbound], second order: `supp f ⊆ [−Λ, Λ]`, `f ∈ C²` ⇒
`‖h_f(z)‖ · ‖z‖² ≤ e^{|Im z| Λ} ‖f''‖₁`. 

### `norm_paperFT_le_div`

 [eq:hfbound] in the paper's form for `z ≠ 0`: `‖h_f(z)‖ ≤ e^{|Im z|Λ} ‖f''‖₁ / ‖z‖²`. 
