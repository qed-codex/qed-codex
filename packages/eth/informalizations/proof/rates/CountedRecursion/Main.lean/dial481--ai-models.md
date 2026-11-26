---
{
  "module": "proof/rates/CountedRecursion/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem A (b) on counted operations: the end theorems

Every statement «… From» of RecursionDefs.lean is an implication from statements of other steps or
of other parts of this development. Each is fed with theorems, here or in the file of its step, so
that every step and the theorem itself stand without hypotheses.

**Fed here**, in the order of the printed proof: `ChildIsGoodFrom`, `ProcedureCostFrom`,
`SolverStepFrom`, `RecursionMeetsFrom`, `RecursionCountedUpToFrom`, `RecursionPluggedFrom`,
`RecursionSolvesFrom`.
**Fed in the file of the step:** `BothNetworksFrom` (BothNetworks.lean); `ChainBaseFrom`,
`ChainExponentFrom` (Chain.lean); `BoundBelowFrom` (LevelBound.lean); `CountBaseFrom`
(CountBase.lean); `CountStepFrom` (CountStep.lean); `TotalCountFrom` (TotalCount.lean);
`TotalRoomFrom` (TotalRoom.lean); `RoomIsWithinTheBoundFrom` (RoomWithin.lean); `RecursionPolyFrom`,
`RecursionWithPolyFrom` (PolyEnd.lean).
**Proved without premises, in their own files:** `solverBase`, `expansion`, `patternsFew`,
`pairIsProduct`, `listsAgree`, `totalsAre`, `smallerTotal`, `caseTwoApplies`, `labelBound`,
`labelCrude`, `crudeBounds`, `chainLabel`, `chainLevels`, `exponentFits`, `readAsRuns`,
`readAsPoly`, `pricesScale`, `numbersRun`, `numbersPoly`, `recursionPoly`. Of these, `readAsPoly`
and `numbersPoly` are premises of no «… From»; they are used inside the certificates
(PolyRules.lean, PolySolver.lean).
**Where «Crude bounds give L ≤ N + 1» is used:** for the L of a call, in `procedureCostFrom`, where
the cost of an entry asks L ≤ 2gP (`labelCrude`); at the bounds along the recursion the same clause
is part of `chainLabel`, from which `chainBase` gets K(L + B') ≤ Ξ^{c+5}.
**Used as lemmas and not as premises:** e_ℓ ≥ 0 in `recursionSolvesFrom`
(`GeneralPieces.PartA.e_ge_half_pow`, a sentence of the printed proof of part (a)); `listsAgree` in
`totalsAre` and `smallerTotal`, which have no «… From».
**From other parts of this development:** Lemma 8 up to the call, its L, and the cost of an entry
(`groupingWithCall`, `labelLengthIsL`, `entryCostExplicit`: proof/rates/ExplicitCost); «whose value
is that of the network» (`Value.stValueEqualsZ`); the tower (`QueryMachines.Tower.towerRuns`,
`towerPoly`, `costShape`); the rule of substitution (`QueryMachines.stSubstWithin`); from the oracle
of the pieces to their algorithm (`PiecesCounted.oracleFromAlgorithm`); part (a) of the theorem
along its printed proof (`partAPrinted`, PartAPrinted.lean, from
proof/rates/GeneralPieces/Num/PartA.lean). 

### `childIsGood`

 A call goes to the (K_ℓ, L)-clique of the groups of the network with the smaller total, for some
function ι from the rectangles to the indices of the pieces. 

### `procedureCost`

 One entry of the callee's tables. 

### `solverStep`

 The solver at a level ℓ + 1. 

### `recursionMeets`

 The solver and the procedure meet the specification. 

### `recursionCountedUpTo`

 Theorem A (b) with the pieces as a priced oracle that is asked only about strings of at most Λ
bits. 

### `recursionPlugged`

 **Theorem A (b), with the pieces computed by their algorithm.** 

### `recursionSolves`

 **Theorem A (b)**, in the one form that is also the hypothesis of Theorem D (a). 
