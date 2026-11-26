---
{
  "module": "Challenge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Challenge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Challenge.lean — the TRUSTED comparator challenge module: WHAT IS CLAIMED.

Seventeen theorem statements about the zeros of Mathlib's `riemannZeta` and of Mathlib's
`DirichletCharacter.LFunction`, each with proof `sorry`: the ε-forms of the headline assertions of
Theorems A–E of the paper "More than two thirds of the zeros of the Riemann zeta function are simple and on the critical line", each at the constant stated in the paper. Writing N(T₁,T₂)
for the number of nontrivial zeros with T₁ < Im ρ ≤ T₂ counted with multiplicity, N₀* / N₀ˢ / N_d
for the distinct on-line / simple on-line / distinct counts (all defined from Mathlib alone in
ChallengeDeps.lean, inlined below), and "liminf_{T→∞} X(T)/N(T) ≥ c" as
"∀ ε > 0, ∃ T₀, ∀ T ≥ T₀, (c − ε)·N(T) ≤ X(T)":
  * Theorem A: N₀*/N ≥ 2/3 (dyadic windows (T,2T] and cumulative windows (0,T]);
  * Theorem B: N₀ˢ/N ≥ 2/3 (both forms);   * Theorem C: N_d/N ≥ 5/6 (both forms);
  * Theorem D: with the Montgomery–Taylor constant c₁* = `cMT` (§3 below), on dyadic windows
    N₀*/N ≥ 2 − 1/c₁*, and — dyadic and cumulative — N₀ˢ/N ≥ 2 − 1/c₁* and N_d/N ≥ (3 − 1/c₁*)/2;
  * Theorem E: for every primitive Dirichlet character χ mod q > 1, the analogues of A, B, C (dyadic)
    for the zeros of L(s,χ), and ("Theorem D holds likewise") the three Theorem-D bounds for L(s,χ).
Solution.lean (untrusted) proves exactly these statements by delegating to the Zeta23 library;
github.com/leanprover/comparator checks statement equality, that only the axioms propext,
Classical.choice, Quot.sound are used, and replays the proofs through the kernel. See README.md here.

The `sorry`s below are deliberate (this is the challenge side); expect "declaration uses 'sorry'"
warnings when building this module.
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

### `two_thirds_on_critical_line`

 **Theorem A — at least 2/3 of the nontrivial zeros of ζ lie on the critical line** (dyadic
windows): for every ε > 0 and all sufficiently large T, (2/3 − ε)·N(T,2T) ≤ N₀*(T,2T), i.e.
liminf_{T→∞} N₀*(T,2T)/N(T,2T) ≥ 2/3. The zeros with T < Im ρ ≤ 2T are counted WITH multiplicity on
the left and as DISTINCT points of the critical line on the right. 

### `two_thirds_on_critical_line_cumulative`

 **Theorem A**, cumulative form: liminf_{T→∞} N₀*(T)/N(T) ≥ 2/3 (windows (0,T]). 

### `two_thirds_simple_on_critical_line`

 **Theorem B**: at least 2/3 of the nontrivial zeros of ζ are *simple and* on the critical
line (dyadic windows). 

### `two_thirds_simple_on_critical_line_cumulative`

 cumulative form: liminf_{T→∞} N₀ˢ(T)/N(T) ≥ 2/3. 

### `five_sixths_distinct`

 **Theorem C**: at least 5/6 of the nontrivial zeros of ζ are distinct (dyadic windows). 

### `five_sixths_distinct_cumulative`

 cumulative form: liminf_{T→∞} N_d(T)/N(T) ≥ 5/6. 

### `montgomery_taylor_on_critical_line`

 **Theorem D — the optimal (Montgomery–Taylor) window**: liminf_{T→∞} N₀*(T,2T)/N(T,2T) ≥ 2 −
1/c₁* (= 3/2 − cot(1/√2)/√2 = 0.67250…), with c₁* = `cMT`. 

### `montgomery_taylor_simple_on_critical_line_mult`

 **Theorem D**, simple zeros: with the optimal window, at least 2 − 1/c₁* (= 0.67250…) of the zeros are
*simple and* on the critical line (the same constant as for N₀*). 

### `montgomery_taylor_simple_on_critical_line_mult_cumulative`

 cumulative form: liminf_{T→∞} N₀ˢ(T)/N(T) ≥ 2 − 1/c₁*. 

### `montgomery_taylor_distinct_mult`

 **Theorem D**, distinct zeros: at least (3 − 1/c₁*)/2 (= 0.83625…) of the zeros are distinct. 

### `montgomery_taylor_distinct_mult_cumulative`

 cumulative form: liminf_{T→∞} N_d(T)/N(T) ≥ (3 − 1/c₁*)/2. 

### `dirichlet_two_thirds_on_critical_line`

 **Theorem E — Dirichlet L-functions**: for every primitive Dirichlet character χ modulo q > 1,
at least 2/3 of the nontrivial zeros of L(s,χ) with T < Im ρ ≤ 2T (counted with multiplicity) are
matched by distinct zeros on the critical line, for all large T. 

### `dirichlet_two_thirds_simple_on_critical_line`

 **Theorem E**: for every primitive Dirichlet character χ mod q > 1, at least 2/3 of the
nontrivial zeros of L(s,χ) are simple and on the critical line (dyadic windows). 

### `dirichlet_five_sixths_distinct`

 **Theorem E**: at least 5/6 of the nontrivial zeros of L(s,χ) are distinct (χ primitive
mod q > 1; dyadic windows). 

### `dirichlet_montgomery_taylor_on_critical_line`

 **Theorem E, "Theorem D holds likewise"**: for χ primitive mod q > 1, liminf_{T→∞}
N*_{0,χ}(T,2T)/N_χ(T,2T) ≥ 2 − 1/c₁* (= 0.67250…). 

### `dirichlet_montgomery_taylor_simple_on_critical_line_mult`

 **Theorem E (optimal window)**: at least 2 − 1/c₁* (= 0.67250…) of the zeros of L(s,χ)
are simple and on the critical line. 

### `dirichlet_montgomery_taylor_distinct_mult`

 **Theorem E (optimal window)**: at least (3 − 1/c₁*)/2 (= 0.83625…) of the zeros of
L(s,χ) are distinct. 
