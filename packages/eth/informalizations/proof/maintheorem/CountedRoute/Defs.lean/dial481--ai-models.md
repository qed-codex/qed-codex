---
{
  "module": "proof/maintheorem/CountedRoute/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/CountedRoute/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/CountedRoute/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The chain from counted operations: definitions and statements

**The paper.** The proof of the Main Theorem starts from ONE algorithm for cliques: Theorem A (b),
on the pieces of Theorem B, gives a deterministic algorithm that, given ℓ, λ, B and query access to
tables, outputs the value of the (K_ℓ, λ)-clique within 2^{e_ℓK_ℓ²λ}·(K_ℓ(λ+B))^{C₀K_ℓ²} operations.
Theorem D (b), first sentence: its pairs (K_ℓ, e_ℓ) satisfy the hypothesis of Theorem D (a). From it
come the
bound in n (Theorem D) and the bound in m (Theorem A (c)), and from these Corollary 11, which is the
Main Theorem.

**The chain in the padding model.** In proof/maintheorem/MainRoute and
proof/maintheorem/NamesInOrder the chain is proved for every solver in the padding model
(`NamesInOrder.OnEverySolver`) and applied to
`RecursionWithPieces.solverAB`, the recursion of Appendix A as a function of a padding string. That
chain does not use the recursion as a machine with query access, operations and queries counted
(`ExplicitCost.cliqueMachine`); this file connects the two.

**What is stated here.**
* `fnN`, `padExpN`, `fnM`, `padExpM`: the two named functions of the chain on the solver that a
  machine E with query access gives (`QueryMachines.Bridge.solverOfMachine`).
* `OnEveryMachineWithQueryAccess`: for EVERY machine E that meets the printed hypothesis of Theorem
  D (a) in counted operations (`ThmVariables.Hypothesis`), with e_ℓ = O((log K_ℓ)^(−1/2)): every
  machine made as Step 6 says has the bound of Theorem D (b); every machine that computes the
  function for the bound in m on the solver that E gives meets the bound in m; every machine
  assembled directly from machines that compute the two named functions and exhaustive counting has
  the bound
  of Corollary 11, which is that of the Main Theorem; and such a machine exists.
* `OnTheCountedRecursion`: there are c, x₀, C₀ and an algorithm, in counted operations, for the
  pieces of Appendix B such that the machine of Theorem A (b) on them meets that hypothesis, with
  e_ℓ ≤ (3x₀+6)/√(log K_ℓ), and the four clauses above hold for it.
* `OnEveryMachineWithQueryAccessFrom`, `OnTheCountedRecursionFrom`, `ClosedStatementsFrom`: how each
  of these is had from the one before.
* Closed statements: `MainTheoremHolds`, `CorMinHolds` and `BoundInMHolds` are the propositions of
  these names in proof/maintheorem/NamesInOrder/Defs.lean; `ThmVariablesBHolds` is
  `MainTheoremForms.ThmVariablesB`.

**What differs from the paper.** The differences are those that
proof/maintheorem/NamesInOrder/Defs.lean, proof/variables/ThmVariables/Defs.lean and
proof/rates/CountedToPadded/Defs.lean list. In particular: only the HYPOTHESIS on E is in counted
operations.
From the first step on, the proofs of Theorems D (a) and A (c) render operations as the length of a
padding string (`QueryMachines.Bridge.SolverOfMachineLevels`), with the number e′_ℓ in [e_ℓ, 2e_ℓ]
that is computed, cut at 1, in the place of e_ℓ, and the constant 2C₀ + 1 in the place of C₀. 

 ### The two named functions on the solver that a machine with query access gives 

### `fnN`

 The function of Steps 1 to 5 of Appendix D (`RecursionToBound.count`) on the solver that the
machine E gives, with the level picked by `pickOf kf K₀`, the fraction `cutFraction num` as the
number between, and exhaustive counting below n₁ and wherever the exponent computed exceeds n. 

### `padExpN`

 The exponent of its padding string. 

### `fnM`

 The function for the bound in m (`ClauseBound.Alg.AM`) on the same solver, with the level picked
by the same program. 

### `padExpM`

 The exponent of its padding string. 

### `ChainOn`

 The four clauses of the chain for the machine E: EVERY machine made as Step 6 says from a
machine that computes the function of Steps 1 to 5 on the solver that E gives has the bound of
Theorem D (b); EVERY machine that computes the function for the bound in m on that solver meets the
bound in m with nothing added; EVERY machine assembled directly from machines that compute the two
named functions on that solver and exhaustive counting has the bound of Corollary 11, which is that
of the Main Theorem, with nothing added; and a machine built directly
from such machines exists. 

 ### The chain 

### `OnEveryMachineWithQueryAccess`

 **The chain from counted operations.** Let E be a machine with query access that meets the
printed hypothesis of Theorem D (a) for K, e, C₀, `kf` and `num`, with any certificate that its
steps are polynomial-time. There is an n₀ such that, if e_ℓ ≤ a/√(log K_ℓ) for all ℓ, for a natural
number a, then `ChainOn` holds for E and every n₁ ≥ n₀. 

### `OnTheCountedRecursion`

 **The chain on the machine of Theorem A (b).** There are c and x₀ with x₀ ≥ 18 and 2^x₀ ≥ c + 7,
C₀, the pieces D of Appendix B (`CountedInstance.AreThePiecesOfAppHalfPieces`) and an algorithm
`Alg` for them, in counted operations, with parameters (1/√2, c + 2) (`PiecesCounted.IsPieces`) and
c^row, c^col ≤ 2λ, such that e_ℓ ≤ (3x₀+6)/√(log K_ℓ) for all ℓ and the machine of Theorem A (b) on
them, `ExplicitCost.cliqueMachine (c + 2) x₀ Alg`, meets the printed hypothesis of Theorem D (a) in
counted operations for the pairs (K_ℓ, e_ℓ) of display (40) at ρ = 1/√2, with K_ℓ computed by
`CliqueLevels.levelsUnder x₀` and the number in [e_ℓ, 2e_ℓ] by
`PairsToBound.fractionHalf`; and, with ANY certificate that its steps are polynomial-time (the
hypothesis says that there is one), `ChainOn` holds for it and all large n₁. 

### `OnEveryMachineWithQueryAccessFrom`

 How the chain from counted operations is had: from the step from counted operations to the
padding string, the facts on the number e′_ℓ, and the chains for every solver in the padding model. 

### `OnTheCountedRecursionFrom`

 How the chain on the machine of Theorem A (b) is had: that machine meets the hypothesis, in
counted operations. 

### `ClosedStatementsFrom`

 The closed statements are read off the chain on the machine of Theorem A (b). By their
statements alone this implication and the two before it show little, as premises and conclusions are
theorems; they record the way of the proof. 

### `MainTheoremHolds`

 **The Main Theorem** (`MainTheoremForms.MainTheoremAllOccur`); here it is read off
`OnTheCountedRecursion`. 

### `CorMinHolds`

 **Corollary 11** (`MainTheoremForms.CorMinAllOccur`); read off `OnTheCountedRecursion`. 

### `BoundInMHolds`

 **The first sentence of Theorem A (c)**, at α′ = 1/2 (`NamesInOrder.BoundInMHolds`); read off
`OnTheCountedRecursion`. 

### `ThmVariablesBHolds`

 **The conclusion of Theorem D (b)** (`MainTheoremForms.ThmVariablesB`); read off
`OnTheCountedRecursion`. 
