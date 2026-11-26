---
{
  "module": "Zeta23/Statement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Statement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Statement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Statement.lean — the statement layer.

Canonical text: the paper, §1 [Results], [eq:trivialchain], [thm:A], [thm:B], [thm:C].

It (1) defines nontrivial zeros, multiplicity (via analyticOrderAt) and the six counting functions of
§1 directly against Mathlib; (2) packages the "seam" facts needed to view them as an abstract
Zeta23.ZeroConfig (structure ZetaSeam — classical facts about ζ, established from Mathlib elsewhere in
the repository, not paper inputs); (3) states Theorems A, B, C in ε-form (fixed λ ∈ (0,1) with
constant H(λ), F(λ), then the 2/3, 1/2, 3/4 liminf wrappers via λ → 1⁻);
(4) proves the sanity anchors connecting to Mathlib's RiemannHypothesis and [eq:trivialchain].
-/
```

 ## 1. Nontrivial zeros and multiplicity, against Mathlib 

### `IsNontrivialZero`

 ρ is a nontrivial zero of ζ: "ρ = β + iγ runs over the nontrivial zeros of ζ(s)" [Results],
rendered as ζ(ρ) = 0 with 0 < Re ρ < 1 (the critical strip). Mathlib's RiemannHypothesis phrases
"nontrivial" as "not of the form −2(n+1) and ≠ 1"; every strip zero is nontrivial in that sense
(lemma IsNontrivialZero.not_trivial below); the converse (all such zeros lie in the open strip) is
classical (nonvanishing on Re s ≥ 1 and, via the functional equation, on Re s ≤ 0) and is not
needed for the statements. 

### `zeroMult`

 m_ρ, "the multiplicity of ρ" [Results]: the order of vanishing of ζ at ρ, via Mathlib's
analyticOrderAt (ℕ∞-valued; toNat sends ⊤ to 0, so 1 ≤ zeroMult ρ encodes BOTH "ζ is not locally
identically zero at ρ" and "ρ is a zero" — see ZetaSeam.one_le_mult). 

### `zerosIn`

 {ρ nontrivial zero : T₁ < γ ≤ T₂}, γ = Im ρ  [Results] (positive-ordinate window; NOT |γ|). 

### `Ncount`

 N(T₁,T₂) := #{ρ : T₁ < γ ≤ T₂} "(counted with multiplicity)"  [Results]. 

### `Ndist`

 N_d(T₁,T₂) := #{ρ : T₁ < γ ≤ T₂} "(each distinct point counted once)"  [Results]. 

### `N0`

 N₀(T₁,T₂) := "the number of zeros on the critical line with T₁ < γ ≤ T₂ counted with …
multiplicity"  [Results]. 

### `N0star`

 N₀*(T₁,T₂) := same "without multiplicity"  [Results]. This is what Theorem A bounds. 

### `N0simple`

 N₀ˢ(T₁,T₂) := #{ρ : T₁ < γ ≤ T₂, β = 1/2, m_ρ = 1}  [Results]. 

### `Nsimple`

 Nˢ(T₁,T₂) := "the number of simple zeros" with T₁ < γ ≤ T₂  [Results]. 

 ## 2. The seam: ζ's zeros as an abstract ZeroConfig 

### `ZetaSeam`

 Classical facts about ζ needed to instantiate Zeta23.ZeroConfig; these are established from
Mathlib elsewhere in the repository (identity theorem + ζ(2) ≠ 0 for one_le_mult; functional equation
riemannZeta_one_sub / completedRiemannZeta_one_sub + Γ-nonvanishing + conjugation symmetry at the
level of analyticOrderAt for the reflection facts; isolated zeros + the pole at 1 for finiteness),
and are not inputs of the paper. Paper [subsec:weil]: "The multiset {(γ_ρ,m_ρ)} is invariant under
γ ↦ γ̄ (i.e. ρ ↦ 1−ρ̄; multiplicities agree because conj ξ(conj s) = ξ(s) = ξ(1−s))". 

### `ZetaSeam.one_le_mult`

 H-fin: at a nontrivial zero the analytic order is finite and ≥ 1. 

### `ZetaSeam.reflect_zero`

 H-symm (set): ρ ↦ 1 − conj ρ preserves nontrivial zeros. 

### `ZetaSeam.mult_reflect`

 H-symm (multiplicity). 

### `ZetaSeam.finite_window`

 local finiteness: finitely many nontrivial zeros with T₁ < γ ≤ T₂. 

### `zetaZeros`

 The nontrivial zeros of ζ with their multiplicities, as an abstract zero configuration.
carrier := {ρ | IsNontrivialZero ρ} exactly, mult := zeroMult exactly (seam requirement: H-EF's
W then ranges over exactly the nontrivial zeros weighted by exactly the analytic order). 

 ## 3. Sanity anchors (connection to Mathlib's existing statement of RH) 

### `IsNontrivialZero.not_trivial`

 A strip zero is a "nontrivial zero" in the sense inlined in Mathlib's RiemannHypothesis:
not a trivial zero −2(n+1) (those have real part ≤ −2) and not the pole 1. 

### `RH_implies_on_line`

 Mathlib's RiemannHypothesis puts every nontrivial zero (in our sense) on the critical line. 

### `RH_implies_all_on_line`

 Sanity anchor 1: under Mathlib's RiemannHypothesis all counted zeros are on the
line, so the on-line counts equal the full counts, with and without multiplicity. No other
hypotheses. 

### `trivial_chain`

 Sanity anchor 2 [eq:trivialchain], verbatim: "trivially N₀ˢ ≤ N₀* ≤ N₀ ≤ N,
N₀ˢ ≤ Nˢ ≤ N_d ≤ N". Needs the seam facts (finiteness of the window; m_ρ ≥ 1), nothing from the
paper. 

 ## 4. Theorems A, B, C

The headline theorems Zeta23.thmA, thmA_cumulative, thmA_lam, thmB, thmB_cumulative, thmB_lam, thmC,
thmC_cumulative, thmC_lam are proved in Zeta23/Final.lean (their types display the full trust base:
literature explicit formula, Riemann–von Mangoldt, Montgomery–Vaughan, Γ-facts), on top of the
versions Zeta23.thmA_of_traces etc. in Zeta23/Main.lean (thm:traces as an explicit hypothesis). This file
stays light (definitions + anchors) so that it can be read and imported cheaply.

Paper [thm:A], verbatim: "Let 0 < λ ≤ 1 be fixed. There are constants c(λ) > 0 and T₀(λ) such that
for all T ≥ T₀(λ)   N₀*(T,2T) ≥ (H(λ) − c(λ) loglogT/logT) N(T,2T),
and for λ < 1 the factor loglog T may be omitted. In particular
  liminf_{T→∞} N₀*(T,2T)/N(T,2T) ≥ 2/3,   liminf_{T→∞} N₀*(T)/N(T) ≥ 2/3".
Formal target: the ε-forms, for each fixed λ ∈ (0,1) with constant
H(λ) (resp. 2F(λ)−1, F(λ)), which absorb c(λ)/log T; then the 2/3 (resp. 1/2, 3/4) forms via
sup_{λ<1} H(λ) = H(1) = 2/3 etc. The effective c(λ) forms are not stated. 

### `ThmA_statement`

 The statement of Theorem A (2/3, dyadic ε-form) as a Prop, for reference; Zeta23.thmA proves it. 

### `ThmB_statement`

 The statement of Theorem B (1/2, dyadic ε-form). 

### `ThmC_statement`

 The statement of Theorem C (3/4, dyadic ε-form). 
