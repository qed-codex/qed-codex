---
{
  "module": "Zeta23/WeilEF/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/WeilEF/Main.lean — Final assembly: EF_lit for the concrete ζ zero configuration.
-/
```

### `Hfn_mirror`

 Mirror identity: the left-line test factor is the right-line factor of the reflected test
function: H_k(1 − c − it) = H_{k∘neg}(c + it). 

### `EF_lit_zeta`

 The literature-form Weil explicit formula holds for Mathlib's ζ
(zero set = IsNontrivialZero, multiplicities = analyticOrderAt).  Together with Zeta23.EF.explicitFormulaPaper_of_lit + GammaFacts this yields
ExplicitFormulaPaper (zetaZeros hs) outright.

Assembly: full_line_identity (Contour) splits via logDeriv_completedZeta (XiLogDeriv) into
• ζ-part = prime_side_line (k) + prime_side_line (k ∘ Neg.neg),
    giving −Σ Λ(n)n^{−1/2}(k(log n) + k(−log n)) after sign bookkeeping,
• Γℝ-part = gamma_line_shift + gammaR_bracket → (1/2π)∫ h(r)[Re ψ(1/4+ir/2) − log π]dr,
• zero side: Σ' m_ρ H(ρ) with H(ρ) = h(γ_ρ) (Hfn at ρ = paperFT k ((ρ−1/2)/i) = h(γ_ρ) by
  gammaOf's definition), pole side: H(0) = h(i/2), H(1) = h(−i/2);
EF_lit's Summable clause = EF_zero_sum_summable (ZeroSummability). 

### `EF_lit_zetaZeroConfig`

 **Hypothesis-free form**: [eq:EFstd] holds for the canonical
unconditional ζ zero configuration. 
