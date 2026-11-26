---
{
  "module": "Zeta23/ThmE/GammaFactsChiProof.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/GammaFactsChiProof.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/GammaFactsChiProof.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/GammaFactsChiProof.lean — H-Γ(χ) as a theorem.
The nine fields of `ThmE.GammaFactsChi κ q` for
  μ_χ(τ) := (1/2π)[log(q/π) + Re ψ(1/4 + κ/2 + iτ/2)],   κ ≤ 1, q ≥ 1,
proved from the abscissa-parametrized digamma toolkit (Zeta23/GammaFacts/Mu.lean:
re_digamma_vertical / re_digamma_mono at any a ∈ (0,1)), the complex Stirling theorem for ψ
(Zeta23/GammaFacts/StirlingVert.lean), the trigamma series (Zeta23/Analytic/Stirling.lean) and the
FTC computations of Zeta23/GammaFacts/IntMu.lean re-run with log(qτ/2π) in place of log(τ/2π).
Key remark: in the Stirling field the conductor constant cancels:
  μ_χ(τ) − (1/2π)log(q|τ|/2π) = (1/2π)[Re ψ(a + iτ/2) − log(|τ|/2)],  a := 1/4 + κ/2 ∈ {1/4, 3/4},
so the ζ proof applies verbatim at abscissa a.
-/
```

### `absc`

 the abscissa `a := 1/4 + κ/2`. 

### `muq_eq`

 `μ_χ(τ) = (1/2π)·Re ψ(a + i·τ/2) + (1/2π)·log(q/π)`. 

 ### even 

 ### monotone, minimum at 0 

 ### Stirling (the conductor constant cancels) 

### `muq_stirling_const`

 Stirling for μ_χ with the explicit, conductor-free constant 20/(2π). 

 ### μ_χ(0) > −1 

 ### smooth 

### `analyticAt_digamma'`

 ψ is analytic on the right half-plane. 

 ### μ_χ′ ≪ 1/|τ| (mirror of MuFields.mu_deriv_bound at abscissa a ≥ 1/4) 

 ### The bundle 

### `gammaFactsChi_of_int`

 H-Γ(χ) from the two integral fields (supplied by Zeta23/ThmE/IntMuChi.lean from
`muq_stirling` + continuity by the FTC computations with log(qτ/2π)). 

### `gammaFactsChi`

 **H-Γ(χ), unconditionally** (parity κ ≤ 1, modulus q ≥ 1): all nine fields are theorems
(the two ∫ fields via Zeta23/ThmE/IntMuChi.lean). 

### `gammaFactsChi_uniform`

 **H-Γ(χ) with one constant for all parities κ ≤ 1 and all moduli q ≥ 1**
(`GammaFactsChiBounded`; consumed by the q-uniform RvM(χ)): every constant and threshold
above is conductor-free (the Stirling constant 20/2π, the derivative constant 24/π, and
int_muq_uniform / int_muq_sq_uniform whose constants are explicit in the Stirling constant). 
