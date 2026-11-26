---
{
  "module": "proof/rates/CountedRecursion/SolverDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/SolverDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/SolverDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The solver, and the one machine for all levels

Definitions only; nothing is stated or proved here.

**The text** (Theorem A (b)): «One deterministic algorithm, given ℓ ≥ 0, λ, B ≥ 1 and query access
to tables with |W_w| < 2^B, outputs the value of the (K_ℓ, λ)-clique within
2^{e_ℓK_ℓ²λ}(K_ℓ(λ+B))^{C₀K_ℓ²} operations.» Its proof: «For ℓ = 0, brute force …» «For the step
from ℓ to ℓ + 1 … d^{|ℛ|}Z = Σ_ι Z_ι over the |𝓘|^{|ℛ|} … functions
ι : ℛ → 𝓘, and each Z_ι is the value of the row network and of the column network.» «Case (ii) of
Lemma 8 applies to the network with the smaller total.» «The set 𝓘 and the numbers d, c^row_i,
c^col_i are computed once.» «… finding the numbers c_{a,a'} and the totals of both networks for one
ι; adding one Z_ι; computing d^{|ℛ|} and dividing by it.»

**What is here.** `solver c x₀`: a machine whose input is the context of an instance and which may (1)
call the solver on another context, (2) query the tables of its instance, (3) query the pieces. At ℓ =
0 it is `Printed.bruteMachine (2^x₀)`. At ℓ = ℓ' + 1 it runs, one after the other
(`QueryMachine.bind`; each stage sees the results of all earlier ones):
1. `numbersM x₀`: 2^{3ℓ'+x₀} and K = K_ℓ' in unary (2ℓ' steps); g = g_ℓ' is their product;
2. one query for 𝓘, one for d, one for each c^row_i, one for each c^col_i: 2|𝓘| + 2 queries to the
   pieces;
3. the loop over the numbers y < |𝓘|^{|ℛ|} of the patterns ι. For one y: the direction of the
   network with the smaller total and the input of Definition 2(iii) for it are plain functions of
   what has been computed; `groupingCall` (module `ExplicitCost.GroupingDefs`: the procedure of
   Lemma 8 up to its call) finds the first grouping x, for ζ = 1/2^{ℓ'+5}, and makes ONE call, which
   is passed on as a call of the context (ℓ', L, B') with the parent (K, g, λ, B, the lists, the
   direction, y, x); the result is added;
4. one step: the division by d^{|ℛ|}.
`recursion c x₀` is the tower of `solver c x₀` and `procedure c` (GridProcedures.lean).

«The algorithm uses ℓ, the pieces, the totals U^row, U^col and the constant c (through x₀ and B₁),
but neither ρ nor e_ℓ»: the definitions have the parameters c and x₀ and no ρ. 

### `SolQuery`

 The queries of the solver: a call, a query to the tables of its instance, a query to the pieces. 

 ### What has been computed before the loop 

### `Stage₁`

 (ℓ, λ, B), with (2^{3ℓ'+x₀}, K) in unary. 

### `Stage₂`

 … with the list of 𝓘. 

### `Stage₃`

 … with d. 

### `Stage₄`

 … with the numbers c^row_i. 

### `Ready`

 … with the numbers c^col_i: all that the loop over the patterns reads. 

### `rHead`

 The parts of it: (ℓ, λ, B). 

### `rK`

 K = K_ℓ'. 

### `rG`

 g = g_ℓ' = 2^{3ℓ'+x₀}·K. 

### `rD`

 d. 

### `rLists`

 The list of 𝓘 and the numbers c^row_i, c^col_i. 

### `rRect`

 |ℛ|, the number of rectangles of the g × g grid. 

### `nPatterns`

 «the |𝓘|^{|ℛ|} functions ι : ℛ → 𝓘». 

 ### One pattern 

### `direction`

 «the network with the smaller total»: the column network if its total is smaller, else the row
network. 

### `parentAt`

 The parent that is handed to the callee for the pattern y = v.2 and the grouping x. 

### `searchInput`

 What the search is given: ζ = 2^{−ℓ'−5} as the fraction 1/2^{ℓ'+5} = 1/2^{ℓ+4}, K and g, and the
input of Definition 2(iii) for the network with the smaller total. 

### `child`

 The context of the call. The procedure of Lemma 8 names the grouping x and (K, L, B'), L = ⌈(U +
2ζgP)/K²⌉, B' = ⌈2gP/K⌉ + g²B₁ (`callOf`, module `ExplicitCost.GroupingDefs`); the solver calls (ℓ',
L, B') with the parent made from what it holds and x. 

### `patternValue`

 Z_ι: **the procedure of Lemma 8 up to the call** (`groupingCall`: «find the first such grouping
among all K^g», then the call), on the network with the smaller total; its call is passed on as a
call of the solver (`QueryMachine.subst`, which lets the call be made from what the solver holds; 2
operations). 

 ### The stages 

### `capsLoop`

 The numbers c^row_i (tr = false) or c^col_i (tr = true), one query for each i in the list. 

### `sumAndDivide`

 «adding one Z_ι», for all ι; then «computing d^{|ℛ|} and dividing by it». 

### `levelSolver`

 The solver at a level ℓ = ℓ' + 1. 

### `baseSolver`

 The solver at the level 0: «brute force» on K₀ = 2^{x₀} nodes. 

### `solver`

 **The solver.** Of the context it reads (ℓ, λ, B) only; the parent is for the procedure, and is
not kept in the states of the solver. 

### `recursion`

 **The one machine for all levels**: its input is the context of the outermost instance, (ℓ, λ,
B) in unary; it has query access to the tables of that instance and to the pieces. «The algorithm
uses ℓ, the pieces, the totals U^row, U^col and the constant c (through x₀ and B₁), but neither ρ
nor e_ℓ»: this is visible in the type, since the definition has the parameters c and x₀ and no
others. 

### `recursionWith`

 The same with the pieces computed by their algorithm (`PiecesCounted.withAlgorithm`): a query to
the tables is passed on, a query to the pieces is answered by running Alg. This machine has query
access to the tables alone. 

### `cliqueMachine`

 **The algorithm of Theorem A (b)**, in the form in which `CliqueLevels.Solves` speaks of it: the
input is (ℓ, λ, B) in unary, a query to the tables is answered by an integer, the result is an
integer. 
