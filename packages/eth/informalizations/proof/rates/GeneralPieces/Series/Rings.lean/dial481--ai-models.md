---
{
  "module": "proof/rates/GeneralPieces/Series/Rings.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Series/Rings.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Series/Rings.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The lemma on the operators Q_s, paragraph "Series": the rings 𝓛, 𝓛₊, 𝓛₋ and the two inverses of ω₁ − ω₂

𝓛 = ℚ[ω₁, ω₁⁻¹, ω₂, ω₂⁻¹] is the additive monoid algebra of ℤ × ℤ over ℚ, so that the coefficient of
ω₁^x·ω₂^y is `F.coeff (x, y)`. 𝓛₊, the ring of the series
Σ_{j ≥ j₀} q_j(ω₁)·ω₂^j with Laurent polynomials q_j, is Mathlib's ring of Laurent series over the
Laurent polynomials. 𝓛₋ is the same Lean type, read with ω₁ and ω₂ exchanged:
the outer variable is ω₁ there. So everything is proved once, for a ring `S` with an inner variable
u and an outer variable v, and then read twice.
Here: both rings contain 𝓛 (`toP`, `toM`, with the same coefficients: `cfP_toP`, `cfM_toM`; `toP` is
injective), ω₁ − ω₂ has the inverse ε₊ in 𝓛₊ and ε₋ in 𝓛₋, and the coefficients of the powers of ε₊
(`eps_pow_succ`). 

### `L`

 𝓛 = ℚ[ω₁, ω₁⁻¹, ω₂, ω₂⁻¹]. 

### `S`

 The series Σ_{j ≥ j₀} q_j(u)·v^j with Laurent polynomials q_j over ℚ. 

### `Lp`

 𝓛₊: the ring `S` with u = ω₁ and v = ω₂. 

### `Lm`

 𝓛₋: the ring `S` with u = ω₂ and v = ω₁. 

### `mo`

 The monomial u^x·v^y. 

### `cf`

 The coefficient of u^x·v^y. 

### `cf_mo_mul`

 Multiplication by a monomial shifts the coefficients. 

### `cf_sum`

 The coefficients of a finite sum. 

### `diag`

 The series Σ_{j ≥ j₀} c_j·u^{d−j}·v^j, all of whose monomials have total degree d. 

 ### Both rings contain 𝓛 

### `moHom`

 The monomials of `S` as a homomorphism of monoids. 

### `moHom'`

 The same with the two exponents exchanged. 

### `toP`

 𝓛 → 𝓛₊: ω₁ goes to u and ω₂ to v. 

### `toM`

 𝓛 → 𝓛₋: ω₁ goes to v and ω₂ to u. 

### `cfP`

 The coefficient of ω₁^x·ω₂^y in an element of 𝓛₊. 

### `cfM`

 The coefficient of ω₁^x·ω₂^y in an element of 𝓛₋. 

### `W`

 The monomial ω₁^x·ω₂^y of 𝓛. 

### `cfP_toP`

 An element of 𝓛 has the same coefficients in 𝓛₊. 

### `cfM_toM`

 An element of 𝓛 has the same coefficients in 𝓛₋. 

### `toP_injective`

 𝓛₊ contains 𝓛. 

 ### The two inverses of ω₁ − ω₂ 

### `eps`

 Σ_{j ≥ 0} u^{−j−1}·v^j. 

### `cf_sub_mul`

 (u − v)·f, coefficient by coefficient. 

### `sub_mul_eps`

 (u − v)·Σ_{j ≥ 0} u^{−j−1}·v^j = 1. 

### `dW`

 ω₁ − ω₂. 

### `epsP`

 ε₊ = Σ_{j ≥ 0} ω₁^{−j−1}·ω₂^j. 

### `epsM`

 ε₋ = −Σ_{j ≥ 0} ω₂^{−j−1}·ω₁^j. 

### `dW_mul_epsP`

 ε₊ is the inverse of ω₁ − ω₂ in 𝓛₊. 

### `dW_mul_epsM`

 ε₋ is the inverse of ω₁ − ω₂ in 𝓛₋. 

### `eps_pow_succ`

 The powers of Σ_{j ≥ 0} u^{−j−1}·v^j: its (N+1)-st power is Σ_{j ≥ 0} C(j+N, N)·u^{−j−N−1}·v^j. 
