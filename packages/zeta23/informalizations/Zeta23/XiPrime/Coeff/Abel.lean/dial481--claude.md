---
{
  "module": "Zeta23/XiPrime/Coeff/Abel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/Abel.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/Abel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/Abel.lean — the Mertens/Abel step.

[XF′ Lemma 7.1, proof, input (M)]: from Mertens' first theorem |Σ_{n≤t} Λ(n)/n − log t| ≤ K (K = log 4 + 4,
tree: Cheb.mertensFirst) and Abel summation, for g ∈ C¹[1,x]:
    | Σ_{n≤x} (Λ(n)/n)·g(n) − ∫₁ˣ g(t)/t dt |  ≤  K·( |g(x)| + ∫₁ˣ |g′(t)| dt ),                 (abel_mertens_t)
and, substituting t = eᵘ, for f ∈ C¹[0,y]:
    | Σ_{n≤e^y} (Λ(n)/n)·f(log n) − ∫₀ʸ f(u) du |  ≤  K·( |f(y)| + ∫₀ʸ |f′(u)| du ).             (mertens_step)
Every Mertens-level estimate for the coefficients (the recursion for the k-fold prime sums, the
Chebyshev-type upper bounds, the k = 1 terms) is an instance of mertens_step with a polynomial f.
-/
```

### `KM`

 Mertens' constant K := log 4 + 4. 

### `Mfun`

 M(t) := Σ_{n≤t} Λ(n)/n in the Icc form produced by Mathlib's Abel summation (the n = 0 term is 0). 

### `abel_mertens_t`

 **Abel/Mertens, t-variable.**  For g ∈ C¹[1,x] (derivative g′, given pointwise as HasDerivAt and continuous):
  |Σ_{n≤x} (Λ(n)/n) g(n) − ∫₁ˣ g(t)/t dt| ≤ K (|g(x)| + ∫₁ˣ |g′(t)| dt). 

### `mertens_step`

 **Mertens step, u-variable.**  For f ∈ C¹[0,y] (y ≥ 0):
  |Σ_{n ≤ e^y} (Λ(n)/n) f(log n) − ∫₀ʸ f| ≤ K (|f(y)| + ∫₀ʸ |f′|). 
