---
{
  "module": "proof/consequences/Sat3Graph/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, the proof of Corollary 7: the decision problems from 3-SAT alone (definitions and statements only)


Here every decider has the procedure D for 3-SAT as a PARAMETER (`SplitSat.Decides3 D δ₃ c`: on (N
in unary, a 3-CNF with variables below N and no clause written twice) the bit «satisfiable» within
c·2^{δ₃N} steps, on states of size at most c·(N+2)^c), and each statement is for EVERY such D:
* `askSized gates D`: on (n in unary, s, ψ) put Γ beside ψ (`SizeCircuit.withGamma`), split every
  long clause (`Eight.Width.widthP`), ask D. `StAskSized`: the answer says whether ψ has a
  satisfying assignment with exactly s true variables; the 3-CNF has O(n) variables as soon as ψ has
  width at most 3, or O(n) clauses.
* Independent Set, Clique, Vertex Cover: `askSized` behind the reader of the formula for independent
  sets, of the complement graph, or with n − s (`Complement.readClique`, `readCover`). The formula
  has up to n² clauses, of 2 literals: no new variable is needed for them.
* k-Coloring: the k-CNF on kn variables of the proof of Corollary 7, its n long clauses split: (2k − 3)·n
  variables at most.
* Dominating Set: the tree of the proof of Corollary 7 that shortens the clauses to w literals; at
  each leaf `askSized`; «yes» if some leaf passes.

Different from the paper. (1) The paper applies Theorem 2 to an arbitrary algorithm. Here D ranges
over the machines cut into steps whose states stay of polynomial size. (2) The paper cites
Impagliazzo, Paturi and Zane for four of the five problems; here the reductions are those of the
proof of Corollary 7 (Γ, complements, the formula for colorings), used for deciding. (3) The
splitting is that of the proof of Corollary 6 (see proof/consequences/SplitSat/Defs.lean).
(4) In the tree for Dominating Set, Γ is put beside the formula at each leaf, and the variables that
    a branch has set to false stay, with one-literal clauses; the paper adds the clauses to Γ first
    and speaks of «the variables not yet set». (5) The statements assume s ≤ n (see `DecidesGraph`
    below).
(6) Time is counted in steps of machines cut into steps. Reading the code of (G, s), building Γ,
    striking out repeated clauses and splitting the long clauses are done when the input is handed
    over (`Stepped.mapIn`) and cost no step; in DOM the same work is done at each leaf inside the
    step that reaches it. That each of these pieces is polynomial-time is what `StCert` says.
This file has no theorem. 

### `askSized`

 ψ and Γ, every long clause split; ask D. 

### `StAskSized`

 **For EVERY procedure D for 3-SAT.** Let gates test the size with at most a·(n+1) gates; let w
and B be numbers, δ > 0, and let D decide 3-SAT with an exponent δ₃ ≥ 0 such that δ₃·(a + 1 + B) ≤
δ. On (n in unary, s, ψ), for s ≤ n and ψ of width at most w on x₀ … xₙ₋₁ with (w − 3)·|ψ| ≤ B·(n+1)
(no condition on |ψ| if w ≤ 3), `askSized gates D` says, within c'·2^{δn} steps and on states of
size at most c'·(n+2)^{c'},
whether ψ has a satisfying assignment with exactly s true variables. 

### `DecidesGraph`

 A machine cut into steps decides the property p of (G, s), s ≤ n, on the code of (G, s), within
c·2^{δn} steps, on states of size polynomial in n. 

### `INDEP`

 The decider for Independent Set (the first of the three deciders for sets of vertices that need
no tree): the reader of the formula for independent sets, then `askSized`. 

### `CLIQUE`

 The decider for Clique: the reader that hands over the formula for independent sets of the
complement graph, then `askSized`. 

### `COVER`

 The decider for Vertex Cover: the reader that hands over n − s and the formula for independent
sets of the graph, then `askSized`. 

### `DOM`

 The decider for Dominating Set: read the input, walk the tree that shortens the clauses to w
literals, ask at each leaf. 

### `COLOR`

 The decider for k-Coloring: the k-CNF on kn variables, its long clauses split; ask D. 

### `StSets`

 **Independent Set, Clique, Vertex Cover from 3-SAT, for EVERY procedure D**: if δ₃·(a + 1) ≤ δ. 

### `StDominating`

 **Dominating Set from 3-SAT, for EVERY procedure D**: each leaf has O(n) clauses, so that
splitting them into clauses of 3 literals with new variables gives a 3-CNF on O(n) variables. Let
the tree for w have at most 2^{δn/2} leaves (`GraphProblems.ShortensD w (δ/2)`; a leaf has at most
3n clauses), and δ₃·(a + 1 + 3·(w − 3)) ≤ δ/2, with w − 3 = 0 for w ≤ 3. 

### `StColoring`

 **k-Coloring from 3-SAT, for EVERY procedure D**: for k ≥ 3, if δ₃·(2k − 3) ≤ δ. 

### `StCert`

 The steps of the five deciders are polynomial time if those of D are and the circuits are
computed in polynomial time. 

### `HostedFor`

 A Turing machine with finite alphabets simulates the machine Ms, cut into steps, with polynomial
overhead (`SplitSat.Simulates`) and decides the property p of (G, s), s ≤ n, within ⌊c·2^{δn}⌋
steps. 
