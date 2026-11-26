---
{
  "module": "proof/rates/GeneralPieces/Series/Expansion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Series/Expansion.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Series/Expansion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The lemma on the operators Q_s: the series f₊ and f₋, and what the comparison of coefficients in the two orders gives

Here a and b are lists of positive integers, the parts of μ and ν, so h' = a.sum, h = b.sum and H =
h' + h. The monomials t^σ, t^σ' of the paper are the multisets π, σ here, and
⟨X⟩ is the entry (π, σ) of the matrix of X. E is the weight of σ; it is not asked that π has the
same weight (if not, all entries below vanish).
`fP` and `fM` are f₊ ∈ 𝓛₊ and f₋ ∈ 𝓛₋ in the form of the paragraph "Reading off" of the proof of
Lemma 9. The structure `Expansion` says what the paragraph "One Laurent polynomial" gets by
comparing the
coefficients of x^μ·x'^ν in the display of that proof that writes both orders with 𝒩 =
e^{A⁺}e^{B⁺}e^{A⁻}e^{B⁻}: f₊ and f₋ are the same combination of powers of ε₊, or ε₋, times elements
of 𝓛. The later paragraphs use nothing else. 

### `mul2_eq_zero`

 b[r'] vanishes on monomials of weight below −r', and so does every product a[r]∘b[r']. 

### `fP`

 f₊ = Σ_r ⟨a[r]∘b[−r]⟩·ω₁^{r−h'}·ω₂^{−r−h}, written as a series in ω₂: the exponent of ω₂ is j =
−r − h, and it starts at j = −E − h. 

### `fM`

 f₋ = Σ_r ⟨b[−r]∘a[r]⟩·ω₁^{r−h'}·ω₂^{−r−h}, written as a series in ω₁: the exponent of ω₁ is j =
r − h', and it starts at j = −E − h'. 

### `cfP_fP`

 The coefficients of f₊. The start of the series cuts nothing off: there are no terms for r > E. 

### `cfM_fM`

 The coefficients of f₋. The start of the series cuts nothing off: there are no terms for r < −E. 

### `Expansion`

 What the comparison of the coefficients of x^μ·x'^ν in the display with 𝒩 in the proof of Lemma
9 gives, for the entry (π, σ): finitely many terms (Γ_c, N_c, n_c), a number, an exponent
N_c ≤ H and an element n_c of 𝓛, the same for both signs, with f₊ = Σ_c Γ_c·ε₊^{N_c}·n_c in 𝓛₊ and
f₋ = Σ_c Γ_c·ε₋^{N_c}·n_c in 𝓛₋. In the paper c is a pair of splittings
μ = μ' ∪ μ'', ν = ν' ∪ ν'', with Γ_c = μ!·ν!·Γ_{μ',ν'}, N_c = |μ'| + |ν'| and n_c = n_{μ'',ν''}. The
terms with N_c = H are those with μ'' = ν'' = ∅: there n_c = [π = σ], and their Γ_c add
up to the number G = μ!·ν!·Γ_{μ,ν}, a parameter of the structure because it is the same for all π,
σ. The last field is "for E = 0 we have ⟨𝒩⟩ = 1". 

### `Expansion.terms`

 The terms (Γ_c, N_c, n_c). 

### `StExpansion`

 The expansion exists for all monomials a, b with positive parts and every entry (π, σ) whose
monomials have no part 0, with one number G that does not depend on π and σ. 
