---
{
  "module": "Zeta23/ThmE/IntMuChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/IntMuChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/IntMuChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/IntMuChi.lean — the [eq:muints]-type integrals for μ_χ: the
int_mu / int_mu_sq fields of GammaFactsChi κ q.

Route: the proofs are generic in the function — with explicit
constants (`int_g_explicit`, `int_g_sq_explicit`; the ∃-forms and the fixed-q μ_χ forms are their corollaries)
for an arbitrary continuous g with |g(τ) − (1/2π)log(|τ|/2π)| ≤ C/τ² (section Generic). Then μ_χ = g + (log q)/(2π) with
g := μ_χ − (log q)/(2π), since the conductor cancels in the Stirling field:
  μ_χ(τ) − (1/2π)log(q|τ|/2π) = g(τ) − (1/2π)log(|τ|/2π),
and ell1q q T = ell1 T + log q, so
  ∫_T^{2T} μ_χ = T·ell1q/(2π) + O(1/T),   ∫_T^{2T} μ_χ² = (T·ell1q²/4π²)(1 + O(l⁻²)).
-/
```

### `int_g_explicit`

 Explicit-constant form of `int_g_of_stirling` (constants depend only on the Stirling constant C). 

### `int_g_sq_explicit`

 Explicit-constant form of `int_g_sq_of_stirling` (constants depend only on the Stirling constant C). 

### `int_g_of_stirling`

 **[eq:muints].1 given Stirling**: ∫_T^{2T} g = Tℓ₁/(2π) + O(1/T)  (∃-form, from `int_g_explicit`). 

### `int_g_sq_of_stirling`

 **[eq:muints].2 given Stirling**: ∫_T^{2T} g² = (Tℓ₁²/4π²)(1 + O(ℓ⁻²))  (∃-form, from `int_g_sq_explicit`). 

 ## μ_χ 

 ## q-uniform versions for μ_χ (constants depend only on the Stirling constant) 

### `int_muq_uniform`

 **q-uniform GammaFactsChiBounded.int_mu**: given the Stirling constant C (q-free), the error
constant is C and the threshold is 1, for every κ, q ≥ 1. 

### `int_muq_sq_uniform`

 **q-uniform GammaFactsChiBounded.int_mu_sq**: constants depend only on the Stirling constant C:
threshold T₀(C) := max (2π e⁴) (32π²(C(1+C)+1)) (≥ 2π e² and ≥ 1 automatically), error constant
K(C) := 8(1+2log²2)+1 + 4π·|C|. The log q of μ_χ never multiplies: 2c₀·|E₂| ≤ 2c₀C/T is absorbed by
ell1q ≥ 2π·c₀ (i.e. ell1q ≥ log q). 

 ## μ_χ at fixed q (∃-forms, from the q-uniform versions) 

### `int_muq_of_stirling`

 **GammaFactsChi.int_mu** from continuity + the Stirling field of μ_χ. 

### `int_muq_sq_of_stirling`

 **GammaFactsChi.int_mu_sq** from continuity + the Stirling field of μ_χ. 
