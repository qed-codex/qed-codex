---
{
  "module": "proof/variables/RecursionToBound/Correct.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Correct.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Correct.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (a) along the printed Step 5: the function is right

`countIsRight_of` proves `CountIsRight` from three statements taken as hypotheses,
`OutputsAreWithinTheSetting`, `CutOffIsIdle` and `PlanFailsOnlyAboveN`, and uses `widthOnTheCode`,
`walkTreeIsSparsify` and `ownDeltaIsBounded` (Tree.lean) directly.

1. **The input** (`countIsRight_of`). On the code of (k, φ) the function reads n, the clauses, k′ =
   «the largest number of literals in a clause, or 3», the index of the level ℓ of n and the number
   r in [e_ℓ, 2e_ℓ] (`widthOnTheCode`). φ is a k′-CNF and 3 ≤ k′ ≤ k, so k′ ≤ (log n)^(1/4), and the
   cut-off of k′ does nothing.
2. **Without a plan** the padding string has at least 2ⁿ units and the function tries all
   assignments (`CountKSatRate.stBruteC`).
3. **With a plan** n ≥ n₁ and the padding string has at least 2^(`needOutputs` + `needWalk`) units.
   `countAll_eq` shows that the walk returns the number of satisfying assignments:
   * `walk_eq`: the walk returns the sum of the values at the leaves. What is known of the tree
     comes from the general theorem `SparsificationLemma.stTreeG` at Calabro's thresholds, with τ =
     α ≥ k′² and paths cut after (32α)^(2k′)·n steps, which is at least (β₁ + … + β_(k′−1))·n by
     fact (iv) on Calabro's thresholds, `SparsificationLemma.Cal.factIV` (`depth_le`). So the bound
     `stackLenCU` on the length of the walk's state applies (`UniformInK.stStateLenU`).
   * There are at most 2^(εn) leaves (`walkTreeIsSparsify`,
     `SparsificationLemma.StepSparsify.outputs_le`), so 2^(⌈εn⌉+2) units suffice for the rounds.
   * `countOutput_eq`: the value at a leaf is the number of satisfying assignments of its output.
     «An output without clauses counts 2^n.» Every other output Φ is counted by Steps 2 to 4 with
     its own Δ; this count is right by `VariableBound.StCountD`, in the proof
     `RecursionWithPieces.countAB`. Its hypotheses: Φ is a k′-CNF; a variable occurs in at most Δ
     clauses, by the definition of Δ
     (`occ_le_DeltaOf`); so Φ has at most Δ·n clauses; Δ ≤ `occBound` (`ownDeltaIsBounded`), hence Δ
     ≤ n + 1 and n ≥ 29·⌈log₂(2Δ)⌉ + 19; and the padding string fits, because Δ is one of the
     numbers over which `needOutputs` is the maximum (`fitsD_of`).
   * The sum of these numbers over the outputs is the number of satisfying assignments of φ
     (`SparsificationLemma.StepSparsify.count_eq_sum`).
The lemmas stand in the namespace `RecursionToBound.Correct`. 

 ### The number kept by the walk never goes down 

### `le_roundS`

 One round does not lower the number. 

### `iterate_le_iterate`

 Further rounds do not lower the number. 

### `iterate_le_sum`

 The number after any number of rounds is at most the sum of the values of the leaves. 

 ### The walk 

### `depth_le`

 (β₁ + … + β_(k−1))·n ≤ (32α)^(2k)·n, for α ≥ 1 and k ≥ 2: by `SparsificationLemma.Cal.factIV`
the sum is at most 4·(32α)^(k−2). 

### `walk_eq`

 The walk with Calabro's thresholds for α returns the sum of the values at the leaves of the tree
whose paths are cut after (32α)^(2k)·n steps. Hypotheses: k ≥ 2, α ≥ k²; ψ is a k-CNF on n variables
with at most m clauses; the padding string has at least 2·(number of leaves) − 1 units and at least
`stackLenCU k (32α) n m` units;
the sum is below 2^(n+1). 

 ### One output 

### `occ_le_DeltaOf`

 In a k-CNF Φ on n variables every variable, below n or not, occurs in at most Δ clauses, Δ =
`DeltaOf n Φ`: a variable that is not below n does not occur. 

### `nSat_eq_cntN`

 The two definitions here of the number of satisfying assignments of ψ among the 2ⁿ assignments,
`nSat` and `cntN`, agree. 

### `mem_deltas_of`

 A number Δ with 2 ≤ Δ ≤ `occBound k r` and Δ ≤ n + 1 is one of the numbers over which
`needOutputs` is the maximum. 

### `fitsD_of`

 A padding string of at least 2^(`needOutputs`) units fits the count of an output with such a Δ. 

### `countOutput_eq`

 The value at a node whose output Φ is a k-CNF on n variables is the number of satisfying
assignments of Φ. Hypotheses: i is the index of a level; the Δ of Φ is at most n + 1 and at most
`occBound k r`, and n ≥ 29·⌈log₂(2Δ)⌉ + 19; the padding string has at least 2^(`needOutputs`) units. 

 ### All outputs 

### `numSat_le`

 There are at most 2ⁿ satisfying assignments. 

### `numSat_of_nil`

 A formula with an empty clause has no satisfying assignment. 

### `length_le_inLen`

 A k-CNF on n variables without repeated clauses has at most `inLen k n` clauses, for k ≥ 1. 

### `countAll_eq`

 «Run Steps 2 to 4 on each of the … outputs and add the results.» For k ≥ 3, a k-CNF φ on n
variables without repeated clauses, 0 < r, the index of a level, and a padding string of at least
2^(`needOutputs` + `needWalk`) units, `countAll` on (n, φ) is the number of satisfying assignments
of φ; provided that every Δ with
2 ≤ Δ ≤ `occBound k r` has Δ ≤ n + 1 and n ≥ 29·⌈log₂(2Δ)⌉ + 19. 

 ### The function 

### `countIsRight_of`

 The function is right in the range of Theorem D (a); from `OutputsAreWithinTheSetting`,
`CutOffIsIdle` and `PlanFailsOnlyAboveN`. The number n₀ is the one that `OutputsAreWithinTheSetting`
gives for the constant C₀ of the sequence of levels. 
