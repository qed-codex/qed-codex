---
{
  "module": "Zeta23/XiPrime/ExplicitFormula/JTerm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/JTerm.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/JTerm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ExplicitFormula/JTerm.lean — evaluation of the correction functional J for a two-bump test function on
a line Re s = c.  [XF′ Thm 4.2 proof (b)–(e); Thm 9.2 (b)–(e).]  ONE generic theorem
JcorrG_estimate (abstract E′/E-on-the-line dE, abstract frozen-parameter map Lpar, line c; inputs: continuity and a
uniform bound for dE, its conjugation symmetry, the freezing estimate and the uniform bound for the frozen Dirichlet
object D_c(Λ; t) := B(c+it)/(Λ − A(c+it))), with two instances: ξ′ (c = 5/4, dE = dEE, Lpar = Lstar, complex) here —
Jcorr_estimate — and W (dE = dE2 c, Lpar = L2star, real) in Hardy/EFJTermW.lean — JcorrW_estimate.
   JcorrG c dE k = Σ'_N [cJ N · k(log N) + conj(cJ N) · k(−log N)]/√N + Err,
   ‖Err‖ ≤ K · ( (W + W′)/(T log T) · 1/(4+(a−b)²) + W/T² ).
The tsum is ∫ paperFT k · Pc_X(cJ) by PrimeTermJ.prime_term_complex.
-/
```

 ## The generic layer 

### `DfroG`

 the frozen Dirichlet object on the line c:  D_c(Λ; t) := B(c+it)/(Λ − A(c+it)). 

### `continuous_DfroG_of`

 continuity of t ↦ L(a, c+it) transported to D_c via an L-series identity. 

### `JcorrG`

 the correction functional on the line c against an abstract dE:  (1/2π)∫ HwC c k t · dE t. 

### `JcorrG_estimate`

 **The generic J-term estimate** on a line Re s = c for an abstract "E′/E on the line" dE and an abstract fixed
parameter map Lpar (ξ′: c = 5/4, dE = dEE, Lpar = Lstar; W: dE = dE2 c, Lpar = L2star).  All analytic input enters
through the five hypotheses; all constants are packaged in K, T₀. 

 ## The ξ′ instance: c = 5/4, dE = dEE, Λ⋆ = Lstar(τ⋆) 

### `Dfro`

 the frozen Dirichlet object on the line 5/4, D(Λ⋆; t) := B(5/4+it)/(Λ⋆ − A(5/4+it)) (= DfroG (5/4)). 

### `Jcorr_estimate`

 **the ξ′ J-term estimate** at c = 5/4 — instance of JcorrG_estimate with Expansion's freeze_on_line /
frozen_uniform / derivE_div_E_uniform. 
