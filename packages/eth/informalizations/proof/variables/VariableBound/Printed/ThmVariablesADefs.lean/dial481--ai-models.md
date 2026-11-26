---
{
  "module": "proof/variables/VariableBound/Printed/ThmVariablesADefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Printed/ThmVariablesADefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Printed/ThmVariablesADefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (a), its «In particular», and the sentence on n₀: the statements

Definitions only. The file imports proof/rates/ClauseBound/Alg/Interfaces.lean, because the
hypothesis of Theorem D (a) is an algorithm for cliques, and Lean's form of that is the structure
`ClauseBound.Alg.Solver` defined there.

## How the hypothesis of Theorem D (a) is written

* «For a constant C₀ ≥ 1 and all integers ℓ ≥ 0 let K_ℓ ≥ 2 be integers and e_ℓ reals with K_ℓ <
  K_(ℓ+1) ≤ K_ℓ^C₀ and (log K_ℓ)^(−C₀) ≤ e_ℓ ≤ 1»: the fields `K_two`, `K_lt`, `K_le`, `e_ge`,
  `e_le` of `Q : S.Seq e C₀`,
  with K_ℓ = `S.K (Q.idx ℓ)` and e_ℓ = `e ℓ`. C₀ ≥ 1 follows from K_ℓ < K_(ℓ+1) ≤ K_ℓ^C₀.
* «one deterministic algorithm … outputs the value of the (K_ℓ, λ)-clique within 2^(e_ℓ K_ℓ²
  λ)·(K_ℓ(λ+B))^(C₀ K_ℓ²) operations»: the solver S is a polynomial-time function of (pad, index,
  instance) (`S.Poly`) that is right
  whenever the pad has length at least 2^need (`Q.correct`), and need ≤ e_ℓ K_ℓ² λ + C₀ K_ℓ²
  log₂(K_ℓ(λ+B)) (`Q.rate`). So «operations» are replaced by: polynomial time in a pad of that
  length. This assumes less than the
  paper, which bounds the operations by 2^need.
* «K_ℓ … can be computed from ℓ in time polynomial in K_ℓ»: `S.Poly.K`, and `Q.pick`, which finds
  the largest ℓ with K_ℓ at most a bound given in unary (ℓ = 0 if there is none).
* «a number in [e_ℓ, 2e_ℓ] can be computed from ℓ»: `Precision e slU C`. A polynomial-time function
  gives, from ℓ in unary, a number s in unary with 2^(−s) ≤ e_ℓ and 2^s ≤ (2/e_ℓ)^C. For C = 1 this
  says that
  2·2^(−s) is in [e_ℓ, 2e_ℓ].

## What differs from the paper

* The number s must be computed in time polynomial in ℓ; the paper allows time polynomial in K_ℓ.
  Here Lean assumes more than the paper. Its precision is looser: a number in [e_ℓ, 2e_ℓ] gives s
  with C = 2.
* The tables of an instance given to the solver have |W| ≤ 2^B; the paper has |W| < 2^B.
* C₀ is a natural number; the paper allows a real C₀ ≥ 1. Nothing is lost: a real C₀ can be replaced
  by ⌈C₀⌉, because every condition on C₀ gets weaker as C₀ grows (K_ℓ ≥ 2 and log(K_ℓ(λ+B)) ≥ 1).
* The solver must also compute its exponent need in polynomial time, under a bound given in unary
  (the fields `needC`, `needC_eq` and `needC_some` of `S.Poly`); the paper asks nothing of the kind.
  Here Lean assumes more than the paper.
* The solver must be right for every B ≥ 0 (`Solver.Correct` has no condition on B); the paper asks
  this only for B ≥ 1. Here Lean assumes more than the paper.
* The constant C′ of the conclusion comes after the solver, the sequence and the precision function
  with its constant C, and before k, n and the formula. So it does not depend on k; Lean does not
  say that it depends only on C₀ and the
  other constants of the hypothesis.
* `ThmVariablesA` says that SOME machine exists; it does not name the algorithm.
* Machine, input, output and k-CNF are as in `MainTheoremFormsStatement.lean`
  (`MainTheoremForms.CountsWithin`); k is the width written in the input. 

### `Precision`

 From ℓ in unary, `slU` computes in polynomial time a number s in unary with 2^(−s) ≤ e_ℓ and 2^s
≤ (2/e_ℓ)^C. 

### `expVariablesA`

 The exponent of Theorem D (a), as printed: k²·e·n·log(k/e). 

### `timeVariablesA`

 The time of Theorem D (a), rounded down: 2^{C·k²·e·n·log(k/e)}. 

### `timeVariablesAAlpha`

 The time of the «In particular» of Theorem D (a), rounded down: 2^{C·k²·n·log log n/(log n)^α′}. 

### `IsLevel`

 «The largest ℓ with K_ℓ ≤ n^(1/17)»: K_ℓ^17 ≤ n < K_(ℓ+1)^17. 

### `ThmVariablesAFor`

 The bound of Theorem D (a) for the machine M and the constant C: for all n, ℓ and k such that ℓ
is the largest level with K_ℓ ≤ n^(1/17) (so n ≥ K₀^17) and 3 ≤ k ≤ (log n)^(1/4), and every k-CNF φ
on n variables, M computes
the number of satisfying assignments within 2^{C·k²·e·n·log(k/e)} steps, where e = e_ℓ. 

### `ThmVariablesA`

 Theorem D (a). «… Then one deterministic algorithm computes, for all integers n and k with n ≥
K₀^17 and 3 ≤ k ≤ (log n)^(1/4), the number of satisfying assignments of a k-CNF on n variables in
time
2^{O(k² e n log(k/e))}, where e = e_ℓ for the largest ℓ with K_ℓ ≤ n^(1/17).» For every
polynomial-time solver S for cliques with a sequence Q of levels and a precision function slU with
constant C, there are one machine with
finite alphabets and one constant C′ with the bound `ThmVariablesAFor`. 

### `ThmVariablesAInParticular`

 Theorem D (a), last sentence. «In particular, if e_ℓ = O((log K_ℓ)^(−α′)) for a constant α′ > 0,
the time is 2^{O(k² n log log n/(log n)^α′)}.» For every α′ > 0, every natural number c, every
sequence Q of levels with
e_ℓ ≤ c·(log K_ℓ)^(−α′) for all ℓ, every machine M and every C with the bound `ThmVariablesAFor`,
there is a C′ such that for all n ≥ K₀^17, all k with 3 ≤ k ≤ (log n)^(1/4) and every k-CNF φ on n
variables the same M takes at most 2^{C'·k²·n·log log n/(log n)^α′} steps. 

### `StepSparsifyFactsStmt`

 Step 5, the two facts behind the «In particular». «… because log K > (log n)/(17C₀), and
log(k/e) ≤ (C₀ + 1/4)·log log n.» For the level ℓ of n, K = K_ℓ, e = e_ℓ, and 1 ≤ k ≤ (log n)^(1/4). 

### `StepSparsifyLargeStmt`

 Step 5. «… because k log n ≤ en for large n. Here n is large if it exceeds a bound that depends
only on the constants of the hypothesis.» For every C₀ there is an n₁ such that k·log n ≤ e·n for
all n ≥ n₁, all k ≤ (log n)^(1/4)
and all real e ≥ (log n)^(−C₀). 

### `StepSparsifySmallStmt`

 Step 5. «For the finitely many smaller n ≥ K₀^17, and the k ≤ (log n)^(1/4) that go with them,
trying all assignments is within the bound.» Trying all assignments takes time 2^n·n^{O(k)}. For
every C₀ and n₁ there is a c such that n ≤ c·k²·e·n·log(k/e) and
k·log n ≤ c·k²·e·n·log(k/e) for all n with 2 ≤ n < n₁, all k ≥ 3 and all real e with (log n)^(−C₀) ≤
e ≤ 1. 

### `SettingN0Stmt`

 «Setting and parameters», the sentence on n₀. «As log Δ ≤ 4kC₀ log log n ≤ 4C₀ (log n)^(1/4) log
log n, there is an n₀ that depends only on C₀ such that for n ≥ n₀ … Δ ≤ n^(1/(40C₀)), n ≥ 2 log(2Δ)
and r̄ ≤ 10n, M ≤ 14n.»
For every C₀ ≥ 1 there is an n₀ such that for all n ≥ n₀, all k ≤ (log n)^(1/4) and all Δ with 2 ≤ Δ
≤ (log n)^(4kC₀): the two inequalities for log Δ, the two for Δ and n, and r̄ ≤ 10n, M ≤ 14n for
every m with n̄ < m ≤ Δn, where n̄ and
r̄ are the parameters of the text (`AppVariables.IsNb`, `AppVariables.IsRb`), β =
`AppVariables.beta` and M = `AppVariables.Mb`. 
