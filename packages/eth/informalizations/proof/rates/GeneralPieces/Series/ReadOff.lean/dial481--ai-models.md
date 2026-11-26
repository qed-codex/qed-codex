---
{
  "module": "proof/rates/GeneralPieces/Series/ReadOff.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Series/ReadOff.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Series/ReadOff.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 9 (Appendix B), on the operators Q_s: paragraph "Reading off" of its proof

For monomials a, b (lists of parts), `qP a b s π σ` is the entry ⟨Q_s(a,b)⟩ = Σ_i
(−1)^i·C(H,i)·⟨a[s−h+i]∘b[h−s−i]⟩, and `qM` is the same with the two factors exchanged.
Multiplying f₊ and f₋ by (ω₁ − ω₂)^H = Σ_i (−1)^i·C(H,i)·ω₁^{H−i}·ω₂^i (`dW_pow`) shows that the
coefficient of ω₁^s·ω₂^{−s} in F is both (`coeff_F_P`, `coeff_F_M`), and that F has no other
monomials (`coeff_F_of_ne`). This gives the three claims for monomials: `qP_eq_qM`, `qP_eq_zero`,
and `sum_qP` with the constant G of the expansion. 

### `dW_pow`

 (ω₁ − ω₂)^H = Σ_i (−1)^i·C(H,i)·ω₁^{H−i}·ω₂^i. 

### `cfP_dW_pow_mul`

 The coefficients of (ω₁ − ω₂)^H·f in 𝓛₊. 

### `cfM_dW_pow_mul`

 The coefficients of (ω₁ − ω₂)^H·f in 𝓛₋. 

### `qP`

 ⟨Q_s(a,b)⟩ for monomials a, b: Σ_{i ≤ H} (−1)^i·C(H,i)·⟨a[s−h+i]∘b[h−s−i]⟩. 

### `qM`

 The same with the two factors of every product exchanged. 

### `Expansion.coeff_F_P`

 F_s = ⟨Q_s(a,b)⟩, from (ω₁ − ω₂)^H·f₊ = F. 

### `Expansion.coeff_F_M`

 F_s is also the sum with the factors exchanged, from (ω₁ − ω₂)^H·f₋ = F. 

### `Expansion.coeff_F_of_ne`

 F has only monomials ω₁^s·ω₂^{−s}. 

### `Expansion.qP_eq_qM`

 Claim (a) for monomials: Q_s(a,b) does not change if the two factors are exchanged in all
products at once. 

### `qP_eq_zero_of_lt`

 For s > E + h all terms of the first sum vanish. 

### `qM_eq_zero_of_lt`

 For s < −E − h all terms of the second sum vanish; here h' ≤ h is used. 

### `Expansion.qP_eq_zero`

 Claim (b) for monomials: Q_s(a,b) = 0 for |s| > E + h. 

### `Expansion.F_eq`

 F = Σ_s F_s·ω₁^s·ω₂^{−s}, with F_s = ⟨Q_s(a,b)⟩. 

### `Expansion.sum_qP`

 Claim (c) for monomials, with the constant of the expansion: Σ_s ⟨Q_s(a,b)⟩ = F(1,1) = G·[π =
σ]. 
