---
{
  "module": "proof/rates/ClauseBound/ParityChecks/Count.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Count.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Count.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The count for one sparse formula is right

`stCountOL : StCountOL`, from the interface statements on one evaluation (`StEvW`), on the form of
the layers of a state (`StShape`) and on the three sums over marks (`StBridgeB`, `StBridgeA`,
`StBridgeF`), and from `ParityChecks.ChoiceByPotential`, on choosing the checks clause by clause by
a potential (Step 2 of Appendix D uses Lemma 13 instead), through the theorem on the run of the
choice of the checks (`run_ok`).
1. No cut-off of the program is active, so the program's checks are those of the run with the two
   functions `orcA`, `orcB` (`RunF.runF_eq`).
2. The two functions are right modulo 2^β in every state that satisfies the bounds for states that
   are tried (`orcOK`): by `StShape` and `StEvW` the evaluation is the sum `truncW`, which is `sumA`
   or
   `sumB` for the list of checks filled up with empty checks to the length r; by `StBridgeA`,
   `StBridgeB` that sum is, modulo 2^(β+r), 2^r times the value that `orcA`, respectively `orcB` at
   a number i' ≤ i₀, must have; the division by 2^r gives this value modulo 2^β.
3. So the checks of the run are good and satisfy the bounds (`run_ok`). If m ≤ nb there are no
   checks, and the empty list of checks is good because no assignment violates more than nb clauses.
4. The last evaluation is `sumF3`, which is 2^r times the number of satisfying assignments modulo
   2^(β+r) (`StBridgeF`); that number is at most 2^n and β ≥ n + 2. 

### `mkQ`

 The parameters (m, nb, r, i₀, β) with m the number of clauses of ψ. 

 ### Lists of checks 

### `getD_pad`

 Empty checks at the end do not change the entries of a list of checks. 

### `Lof_pad`

 Empty checks at the end do not change the checks as sets. 

### `incL_pad`

 Empty checks at the end do not change the incidences. 

### `wfC_pad`

 A list of at most r checks, filled up with empty checks, is a list of r checks. 

### `lam_subset`

 Without the current check every check is a subset of what it was. 

### `tent_mono`

 The bounds for states that are tried pass to smaller checks. 

### `getD2`

 Two numbers that are at most c, as a list. 

### `getD3`

 Three numbers that are at most c, as a list. 

 ### Residues 

### `toNat_eq`

 If a ≡ 2^r·N modulo 2^(β−1+r+1), β ≥ n + 2 and 0 ≤ N ≤ 2^n, then N is the remainder of a/2^r
modulo 2^(n+1). 

### `nSat_le`

 At most 2^n assignments satisfy ψ. 

 ### The evaluations 

### `ev3`

 An evaluation on the three layers of a state that satisfies the bounds for states that are tried
is exact. 

### `ev2`

 The same on the first two layers. 

### `orcOK`

 The two functions that the choice of the checks asks are right modulo 2^β in every state that
satisfies the bounds for states that are tried. 

### `count_core`

 The count is right, for parameters that satisfy what the choice of the checks needs, or without
checks if there are at most nb clauses. 

 ### The parameters of the program 

### `beta1_le`

 β₁ ≤ m. 

### `beta0_eq_zero`

 β₀ = 0 if m ≤ nb. 

### `stCountOL`

 The count is right. 
