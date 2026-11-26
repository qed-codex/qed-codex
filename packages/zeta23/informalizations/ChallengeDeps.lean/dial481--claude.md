---
{
  "module": "ChallengeDeps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/ChallengeDeps.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/ChallengeDeps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
ChallengeDeps.lean — the TRUSTED definition layer for the comparator challenge
(see README.md, "Verifying the statements").

Everything the challenge statements in Challenge.lean mention is defined HERE, from Mathlib alone:
the nontrivial zeros of Mathlib's `riemannZeta` (resp. of Mathlib's `DirichletCharacter.LFunction χ`),
their multiplicity via Mathlib's `analyticOrderAt`, the standard counting functions of the
critical-line literature, and the Montgomery–Taylor constant c₁* of Theorem D, written out in
closed form. This module imports NOTHING from Zeta23/. A reader auditing WHAT is claimed needs to
read only this file and Challenge.lean (trusting Mathlib and the Lean kernel); the proofs live in the
Zeta23 library and are checked against these statements by github.com/leanprover/comparator
(statement equality + axiom audit + kernel replay), via Solution.lean.

This file contains exactly the definitions the challenge statements depend on (the statements'
constants and what their definitions unfold to) — if a definition is not needed by a statement, it is
not here. Each `def` line of §1 is character-for-character the corresponding one in
Zeta23/Statement.lean §1, and each of §2 the one in Zeta23/ThmE/Statement.lean §1 (docstrings are
reworded for a reader without the rest of the repository; §3's cMT is the paper's displayed closed
form, proved equal to the library's `Zeta23.ThmD.cStar 1` on the solution side). The copies live
in the root namespace (Zeta23's live in `Zeta23` / `Zeta23.ThmE`) so that Solution.lean can import both this
module and the Zeta23 development without name clashes.
-/
```

 ## 1. Nontrivial zeros of ζ and the counting functions (Theorems A–D) 

### `IsNontrivialZero`

 ρ is a nontrivial zero of the Riemann zeta function: ζ(ρ) = 0 with 0 < Re ρ < 1 (the open
critical strip). Every zero in the strip is "nontrivial" in the usual sense (it is neither a trivial
zero −2(n+1), of real part ≤ −2, nor the pole s = 1); the converse — that every zero other than the
trivial ones lies in the open strip — is classical and is not needed to state the theorems. 

### `zeroMult`

 m_ρ, the multiplicity of ρ: the order of vanishing of ζ at ρ, via Mathlib's `analyticOrderAt`
(ℕ∞-valued; `toNat` sends ⊤ to 0, so `1 ≤ zeroMult ρ` encodes both "ζ is not locally identically
zero at ρ" and "ρ is a zero"). 

### `zerosIn`

 The nontrivial zeros with ordinate in the window (T₁, T₂]: {ρ | ζ(ρ) = 0, 0 < Re ρ < 1,
T₁ < Im ρ ≤ T₂}. (Positive-ordinate window, not |Im ρ|.) 

### `Ncount`

 N(T₁,T₂): the number of nontrivial zeros with T₁ < Im ρ ≤ T₂, counted WITH multiplicity
(`∑ᶠ` is Mathlib's finite sum; that the window contains finitely many zeros is proved on the
solution side, not assumed). 

### `Ndist`

 N_d(T₁,T₂): the number of nontrivial zeros with T₁ < Im ρ ≤ T₂, each distinct zero counted
once. 

### `N0star`

 N₀*(T₁,T₂): the number of DISTINCT zeros ON the critical line Re ρ = 1/2 with
T₁ < Im ρ ≤ T₂. This is what Theorems A and D bound from below. 

### `N0simple`

 N₀ˢ(T₁,T₂): the number of SIMPLE zeros (multiplicity exactly 1) ON the critical line with
T₁ < Im ρ ≤ T₂. 

 ## 2. The same for a Dirichlet L-function L(s,χ) (Theorem E)

`χ.LFunction` is Mathlib's `DirichletCharacter.LFunction χ : ℂ → ℂ`, the analytic continuation of
L(s,χ) (for a character χ mod q, `q ≠ 0`). 

### `IsNontrivialZeroL`

 ρ is a nontrivial zero of L(s,χ): L(ρ,χ) = 0 with 0 < Re ρ < 1. 

### `zeroMultL`

 m_ρ: the order of vanishing of L(·,χ) at ρ (via `analyticOrderAt`, as for ζ). 

### `zerosInL`

 the nontrivial zeros of L(·,χ) with T₁ < Im ρ ≤ T₂. 

### `NcountL`

 N_χ(T₁,T₂): nontrivial zeros of L(s,χ) with T₁ < Im ρ ≤ T₂, with multiplicity. 

### `NdistL`

 N_{d,χ}(T₁,T₂): distinct zeros. 

### `N0starL`

 N*_{0,χ}(T₁,T₂): on the line, distinct. 

### `N0simpleL`

 N^s_{0,χ}(T₁,T₂): on the line and simple. 

 ## 3. The Montgomery–Taylor constant of Theorem D 

### `cMT`

 c₁* := √2·tan ϑ / (1 + ϑ·tan ϑ) at ϑ = 1/√2 — the paper's closed form for the optimal-window
constant c*_λ = √2·tan ϑ/(1 + ϑ·tan ϑ), ϑ = λ/√2, at λ = 1. Numerically c₁* = 0.7532960…
(= 2·tan(1/√2)/(√2 + tan(1/√2)); 1/c₁* = 1/2 + 2^{-1/2}·cot(2^{-1/2}) is the Montgomery–Taylor
constant). Theorem D's proportions here are 2 − 1/c₁* = 0.67250… (for N₀* and N₀ˢ) and
(3 − 1/c₁*)/2 = 0.83625… (for N_d); the decimals are NOT part of the formal statements. 
