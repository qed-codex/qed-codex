---
{
  "module": "proof/statements/AppVariablesStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/AppVariablesStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/AppVariablesStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Appendix D, Steps 1 and 2: parity checks, the cut-off lemma, the family of checks, the search for the checks

Definitions and statements only; every statement is a proposition (`…Stmt`, `LemCutoff`,
`LemFamily`) or a structure of propositions (`StepChoice`), proved in proof/variables/VariableBound.
Imports Mathlib and `ParityChecksStatement.lean`, of which only the first
definitions are used: `ParityChecks.ev` ([q even]), `ParityChecks.sig` (σ_i), `ParityChecks.eta` (η)
and `ParityChecks.tuples`.

## How to read it

* Abstract setting, as in `ParityChecksStatement.lean`: X is the finite set of assignments ξ, E the
  finite set of clauses of Φ, V ξ the set of clauses that ξ violates. Nothing else about formulas is
  used in Steps 1 and 2.
* A check is a `Finset E`; a list 𝓛 of checks is a `List (Finset E)`, which may overlap or repeat;
  (𝓛, Γ) is `L ++ [Γ]`. The paper numbers the checks 1, …, r, Lean 0, …, r − 1.
* Fractions are cleared where the paper compares counts: «at most (16/(15v))·|Ω| indices» is
  15·v·(number) ≤ 16·|Ω|.
* The names follow the paper: n̄ `nb`, r̄ `rb`, s̄ `sb`, t̄ `tb`, β `beta`, M `Mb`, p `pp`, Υ `Ups`.

## What is not here

* The inequalities of the paragraph «Setting and parameters» (the bounds on s̄, on 3m/(n̄+1) and on
  β, r̄ ≤ 2.41·β + 1, r̄ ≤ 10n and M ≤ 14n, p·r̄ < 22·log(2Δ), the bound on t̄): stated in
  proof/variables/VariableBound/Params/Defs.lean, proved in
  proof/variables/VariableBound/Params/Ineq.lean.
* The claim of Lemma 13 that the sets can be listed in time polynomial in m: it is a statement about
  a program, in proof/variables/VariableBound/Field. The number of lists that are tried and the size
  of Υ belong to the program too.
* The networks of Step 3, the cost (Step 4), the sparsification (Step 5) and the end (Step 6), which
  speak of formulas, nodes and machines: proof/variables/VariableBound. 

 ## Step 1: parity checks, and a cut-off modulo a power of 2 

### `allEven`

 ∏_j [ |V_j(ξ)| even ], with V_j(ξ) = Λ_j ∩ V(ξ). 

### `Fsum`

 F(𝓛) = Σ_ξ η(ξ)·∏_j [ |V_j(ξ)| even ]. 

### `Xsum`

 X(𝓛) = Σ_ξ C(|V(ξ)|, n̄ + 1)·∏_j [ |V_j(ξ)| even ]. 

### `tup`

 The tuples (Π_1, …, Π_r) with Π_j ⊆ V_j(ξ) for all j and Σ_j |Π_j| ≤ M'. 

### `ProductStmt`

 Step 1 of Appendix D: if X(𝓛) = 0, then F(𝓛) is the number of satisfying assignments of Φ. 

### `EmptyListStmt`

 If m ≤ n̄, the empty list has X = 0. 

### `LemCutoff`

 Lemma 12 (Cut-off): for a list 𝓛 of r checks, a function φ with integer values, ν ≥ 1 and M' ≥ ν
− 1 + r, Σ_ξ φ(ξ)·∏_j [ |V_j(ξ)| even ] is congruent modulo 2^ν to Σ_ξ φ(ξ)·Σ ∏_j σ_{|Π_j|}, the
inner sum over the tuples
with Π_j ⊆ V_j(ξ) for all j and Σ_j |Π_j| ≤ M'. 

### `XFStmt`

 The congruences after Lemma 12, for r checks, β ≥ 1, M ≥ β − 1 + r, M ≥ n + r (the paper takes r
≤ r̄, M = r̄ + β − 1): X(𝓛) mod 2^β and F(𝓛) mod 2^(n+1) as sums over ξ and tuples (Π_0, …, Π_r). 

### `ResiduesStmt`

 The residues determine the numbers: 0 ≤ X(𝓛) ≤ 2^n·C(m, n̄+1) ≤ 2^(β−1), and 0 ≤ F(𝓛) ≤ 2^n if
X(𝓛) = 0. Here 2^n is any bound for the number of assignments, and β = n + ⌈log C(m, n̄+1)⌉ + 1. 

 ## Step 2: Lemma 13 (Family of checks) 

### `IsFamily`

 What Lemma 13 says of sets Γ_u, u ∈ Ω, of clauses, for the number v: (a) |Γ_u| ≤ 16m/v; (b)
every clause lies in Γ_u for at most (16/(15v))·|Ω| indices u; (c) for every set V of more than v
clauses, |Γ_u ∩ V| is odd for at least |Ω|/4 indices u. 

### `ip`

 The inner product modulo 2 of two strings of s bits. 

### `Gam`

 Γ_u for u = (u₁, u₂, u₃, u₄) ∈ 𝔽⁴: the clauses E such that the first log v − 1 bits of u₁·ϑ_E +
u₂ are 0 and ⟨u₃^ι(E), u₄⟩ = 1. The clauses are numbered, ι(E) = E; v = 2^a; `bits` writes the
elements of 𝔽
as strings of s bits. In Lean, as in the paper, u₃^0 = 1 also for u₃ = 0. 

### `Om`

 Ω: the u ∈ 𝔽⁴ with |Γ_u| ≤ 16m/v. 

### `LemFamily`

 Lemma 13 (Family of checks), without its claim on the time: for v = 2^a with 2 ≤ v ≤ m and a
field 𝔽 with 2^s elements, 16m ≤ 2^s < 32m, the sets Γ_u, u ∈ Ω, have 0 < |Ω| < (32m)⁴ and (a), (b),
(c). That Ω is not empty is in the printed proof (|Ω| ≥ (15/16)·|𝔽|⁴), not in the printed statement;
Step 2 needs it. 

 ## Setting and parameters 

### `IsNb`

 n̄ is the power of two with n/(2·log(2Δ)) < n̄ ≤ n/log(2Δ), written without the real number
log(2Δ): (2Δ)^n̄ ≤ 2^n < (2Δ)^(2n̄). The paper also has n ≥ 2·log(2Δ), which gives n̄ ≥ 2; this
definition allows n̄ = 1. 

### `beta`

 β = n + ⌈log C(m, n̄+1)⌉ + 1. 

### `IsRb`

 r̄ is the least j ≥ 0 with 3^j·2^β < 4^j. 

### `Mb`

 M = r̄ + β − 1. 

### `pp`

 p = 16/(15·n̄). 

### `IsTb`

 t̄ is the least c ≥ 0 with 2^c ≥ m·(1+p)^r̄. 

 ## Step 2: finding the checks 

### `load`

 load(E): the number of checks of the list that contain the clause E. 

### `Ups`

 Υ(𝓛) = (4/3)^r·X(𝓛)/2^(β−1) + (1+p)^(r̄−r)·2^(−t̄)·Σ_E 2^load(E). 

### `Reached`

 The lists that the algorithm reaches: the empty list; and, if 𝓛 is reached and X(𝓛) > 0, a list
(𝓛, Γ_u), u ∈ Ω, with the smallest Υ. 

### `StepChoice`

 Step 2 (finding the checks). Each field names its hypotheses, chosen among: X has at most 2^n
elements; n̄ ≥ 1 (n̄ need not be the n̄ of the paper, and m > n̄ is not assumed); β = n + ⌈log C(m,
n̄+1)⌉ + 1 for m the number of clauses
(`beta`), and r̄, t̄ as in the paper for this β and m (`IsRb`, `IsTb`); Γ_u, u ∈ Ω, a family with
(a), (b), (c) of Lemma 13 for v = n̄ (`IsFamily`). 

### `StepChoice.avgX`

 for a family as in Lemma 13 with v = n̄: the average of X(𝓛, Γ_u) over u ∈ Ω is at most
  (3/4)·X(𝓛) 

### `StepChoice.avgCol`

 for n̄ ≥ 1 and a family as in Lemma 13 with v = n̄: the average of 2^[E ∈ Γ_u] over u ∈ Ω is
  at most 1 + p 

### `StepChoice.avgUps`

 for n̄ ≥ 1, a family as in Lemma 13 with v = n̄, any β, r̄, t̄ and a list of r < r̄ checks:
  the average of Υ(𝓛, Γ_u) over u ∈ Ω is at most Υ(𝓛) 

### `StepChoice.ups_le`

 for at most 2^n assignments, n̄ ≥ 1, β, r̄, t̄ as in the paper and a family as in Lemma 13
  with v = n̄: every list that is reached has at most r̄ checks and Υ ≤ 2 

### `StepChoice.x_le`

 under the hypotheses of `ups_le`: every reached list has X(𝓛) ≤ (3/4)^r·2^β 

### `StepChoice.progress`

 for any β, r̄, t̄ and any sets Γ_u, if Ω is not empty: a reached list with X(𝓛) > 0 has a
  reached extension (𝓛, Γ_u), u ∈ Ω 

### `StepChoice.ends`

 under the hypotheses of `ups_le`: a reached list of r̄ checks has X = 0; with `ups_le`, the
  loop ends after at most r̄ rounds with X(𝓛) = 0 

### `StepChoice.structure_`

 the bounds at the end of Step 2, under the hypotheses of `ups_le`: every list whose X or F is
  needed (a reached list, or one with X > 0 and one more Γ_u, u ∈ Ω) has r ≤ r̄, |Λ_j| ≤ s̄ =
  16m/n̄, load(E) ≤ t̄ + 2 
