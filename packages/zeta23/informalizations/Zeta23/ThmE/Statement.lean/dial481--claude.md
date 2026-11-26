---
{
  "module": "Zeta23/ThmE/Statement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/Statement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/Statement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/Statement.lean — Theorem E (Dirichlet L-functions): statement layer against Mathlib's
`DirichletCharacter.LFunction`.

Canonical text: the paper §7.2 [subsec:dirichlet], [thm:E], verbatim:
"Let χ be a primitive character modulo q>1, and let N_χ(T₁,T₂), N^s_{0,χ}, N_{d,χ} count the nontrivial
 zeros of L(s,χ) with T₁<γ≤T₂ as in §1; N_χ(T,2T) = (T/2π)log(qT/2π) + O(T).
 THEOREM E. Fix q and a primitive χ mod q. For fixed 0<λ≤1 and T ≥ T₀(λ,q),
 N*_{0,χ}(T,2T) ≥ (H(λ)−o(1))N_χ(T,2T), N^s_{0,χ}(T,2T) ≥ (2F(λ)−1−o(1))N_χ(T,2T) and
 N_{d,χ}(T,2T) ≥ (F(λ)−o(1))N_χ(T,2T); in particular at least (2/3−o(1))N_χ(T,2T) of the zeros of
 L(s,χ) with T<γ≤2T are on the critical line, at least (1/2−o(1))N_χ(T,2T) are simple and on the
 line, and at least (3/4−o(1))N_χ(T,2T) are distinct. Theorem D holds likewise."

This is the only file of the Theorem E development that mentions Mathlib's Dirichlet L-functions.
Mathlib provides: `DirichletCharacter.LFunction χ : ℂ → ℂ` (entire for χ ≠ 1,
`differentiable_LFunction`), `IsPrimitive`, `completedLFunction` with the functional equation
`IsPrimitive.completedLFunction_one_sub` (χ ↔ χ⁻¹, `rootNumber`), `gammaFactor` (parity), and
non-vanishing on Re s ≥ 1 (`LFunction_ne_zero_of_one_le_re`).  Structure mirrors `Zeta23/Statement.lean`:
(1) nontrivial zeros / multiplicity / the six counts; (2) the seam facts `LSeam χ` (classical facts
about L(s,χ), discharged from Mathlib elsewhere in the repository — [thm:E] proof (ii)) and the
abstract `ZeroConfig`; (3) the parameters (parity κ, coefficients χ(n)) for the ε-form statements
of Theorem E (fixed λ ∈ (0,1), then 2/3, 1/2, 3/4), which are proved in Zeta23/ThmE/Final.lean.
-/
```

 ## 1. Nontrivial zeros of L(s,χ) and multiplicity, against Mathlib 

### `IsNontrivialZeroL`

 ρ is a nontrivial zero of L(s,χ): L(ρ,χ) = 0 with 0 < Re ρ < 1  ("count the nontrivial zeros
of L(s,χ) … as in §1"; [thm:E] proof (ii): "all zeros have 0<β<1"). 

### `zeroMultL`

 m_ρ: the order of vanishing of L(·,χ) at ρ (analytic order; toNat sends ⊤ to 0, so
1 ≤ zeroMultL χ ρ encodes "not locally identically zero" and "is a zero"). 

### `zerosInL`

 {ρ nontrivial zero of L(·,χ) : T₁ < γ ≤ T₂}, γ = Im ρ. 

### `NcountL`

 N_χ(T₁,T₂), with multiplicity. 

### `NdistL`

 N_{d,χ}(T₁,T₂): distinct zeros. 

### `N0L`

 N_{0,χ}(T₁,T₂): on the line, with multiplicity. 

### `N0starL`

 N*_{0,χ}(T₁,T₂): on the line, distinct. 

### `N0simpleL`

 N^s_{0,χ}(T₁,T₂): on the line and simple. 

### `NsimpleL`

 N^s_χ(T₁,T₂): simple zeros. 

 ## 2. The seam: the zeros of L(s,χ) as an abstract ZeroConfig  ([thm:E] proof (ii)) 

### `LSeam`

 Classical facts about L(s,χ), χ primitive mod q > 1, needed to instantiate `Zeta23.ZeroConfig` —
obligations discharged from Mathlib elsewhere in the repository, not inputs of the paper.
[thm:E] proof (ii), verbatim:
"the multiset of zeros of L(s,χ) is invariant under ρ ↦ 1−ρ̄ with multiplicities (functional equation
χ ↔ χ̄ composed with conj L(conj s,χ) = L(s,χ̄))".  (The γ ↦ −γ symmetry fails for complex χ; the
abstract layer does not use it — the local count in `RiemannVonMangoldtChi` is two-sided instead.) 

### `LZeros`

 The nontrivial zeros of L(s,χ) with multiplicities, as an abstract zero configuration
(carrier := exactly the nontrivial zeros, mult := exactly the analytic order). 

### `trivial_chainL`

 [eq:trivialchain] for L(s,χ), from the abstract `ZeroConfig.trivial_chain`. 

 ## 3. Theorem E — parameters  ([thm:E]; ε-forms at fixed λ ∈ (0,1), then 2/3, 1/2, 3/4)

The parity is κ := (1−χ(−1))/2, i.e. κ = 0 for χ even and κ = 1 for χ odd, and the coefficient
sequence is c n := χ(n) (n : ℕ cast into ZMod q). The hypotheses are those of `PaperInputsChi`
(Zeta23/ThmE/Hypotheses.lean) at these parameters, for the configuration `LZeros hs`. 

### `parity`

 κ = (1−χ(−1))/2 as a natural number: 0 if χ is even, 1 if χ is odd. 

### `coeff`

 the coefficient character values n ↦ χ(n). 
