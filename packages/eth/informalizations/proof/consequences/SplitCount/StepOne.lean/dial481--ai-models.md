---
{
  "module": "proof/consequences/SplitCount/StepOne.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/StepOne.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/StepOne.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Corollary 6 at k = 3 (here called step 1): Theorem 2 counts

For every δ' > 0, the proof of Theorem 2 (Section 6), with K and g chosen from δ' as there (we may
assume δ' ≤ 1), computes Z, and hence the number Z·2^{n'} of satisfying assignments of a 3-CNF with
m ≥ 1 clauses in which n' of the n variables do not occur, in time O(2^{δ'm}) plus a polynomial in
n; with no clauses the number is 2^n.
* `stStepOneFor`: the number Z·2^{n'} of satisfying assignments, for every machine that computes Z:
  one more step, which multiplies by 2^{n'} (`Occ.timesFree`); that the product is the number of
  satisfying assignments is `Occ.stCountOcc`.
* `stComputesZ`: the proof of Theorem 2 computes Z: Lemma 1 for the algorithm of its printed proof
  (`Eight.ViaGrouping.stLemGrouping`) and «Cost» of Section 6 (`Eight.ViaGrouping.count_cost_of`).
* `stCountIsNetworkMachine`, `stStepOne`: COUNT of Algorithm 1 at level ℓ is that machine at K = K_ℓ
  with CLIQUE(ℓ). 

### `stStepOneFor`

 **Step 1: from Z to the number Z·2^{n'} of satisfying assignments.** If Cnt computes Z as
Section 6 says, with the exponent δ' ≥ 0 and the constant A, then `timesFreeAfter Cnt` does what
step 1 says, with the same exponent and some constant A'. 

### `stComputesZ`

 **The proof of Theorem 2, with K and g chosen from δ' as there, computes Z.** For 0 < δ' ≤ 1, K
≥ 2 with K ≥ 72/δ', g = 3K⁸ and any algorithm E for cliques on K nodes with the exponent δ'/12, the
algorithm of the printed proof of Lemma 1 with E, run on the network of Φ on g clusters, computes Z
as Section 6 says. 

### `stCountIsNetworkMachine`

 COUNT of Algorithm 1 at level ℓ is the machine of `StComputesZ` at K = K_ℓ and E = CLIQUE(ℓ):
g_ℓ = 3K_ℓ⁸ by definition. 

### `stStepOne`

 **Step 1 for COUNT of Algorithm 1.** For 0 < δ' ≤ 1 and every level ℓ with K_ℓ ≥ 72/δ' and e_ℓ ≤
δ'/12, `countThree ℓ` does what step 1 says. 
