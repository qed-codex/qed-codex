---
{
  "module": "proof/threesat/Exits/Decides.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/Decides.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/Decides.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Algorithm 1 decides 3-SAT, and the two proofs of Theorem 2: the implications

Proof of Theorem 2, «Constants and reduction»: «We may assume δ ≤ 1. Let M = M(δ/3) and δ' = δ/(3M)
≤ 1/3. Since e* = 0 < δ'/12 and achievability is monotone in e (Definition 4), (K, δ'/12) is
achievable for infinitely many K. Fix such a K ≥ 72/δ' and put g = 3K⁸ … By Lemma 4 with ε = δ/3, …
it suffices to compute the number of satisfying assignments of a 3-CNF Φ on n variables with m ≤ Mn
clauses, in time O(2^{δ'm}) plus a polynomial in n.» This file uses the reduction for deciding: it
suffices to decide whether such a Φ is satisfiable within that time.
Header of Algorithm 1: «For Theorem 2, ε = δ/3, δ' is as in Section 6, and ℓ is the first level with
K_ℓ ≥ 72/δ' and e_ℓ ≤ δ'/12.»
This file proves five implications of proof/threesat/Exits/AlgDefs.lean, each from its hypotheses.
* `stAlgorithmOf`: Algorithm 1 with the constants of its header, from «it suffices», read for
  deciding, and «Cost» for Count.
* `stProofNamedOf`: the proof of Section 6 for a named machine, from «it suffices», Lemma 1 for the
  algorithm of its proof and its polynomial-time steps; the paragraph «Cost» is generic in the
  algorithm for networks (`Eight.ViaGrouping.count_cost_pos_of`).
* `stDecidesOf`: Theorem 2 for step machines with the machine named, from Algorithm 1 and Lemma 4 as
  an enumeration; «We may assume δ ≤ 1»: the machine for min(δ, 1) serves.
* `stThroughEStarOf`: Theorem 2 by the proof of Section 6.
* `stByAlgorithmOf`: Theorem 2 by Algorithm 1.
`decidesSparse_of` is a step inside the proofs of the first two, not a statement of AlgDefs.lean.
In the last two the bound in steps is taken at δ/2, and the polynomial cost of a step is paid at the
end (`Paper.steps_to_time`); the paper counts operations. 

### `decidesSparse_of`

 A machine that decides every 3-CNF with m clauses within A·2^{δ'm} steps does what the reduction
of the proof of Theorem 2, read for deciding, asks (to decide whether a 3-CNF Φ with m ≤ Mn clauses
is satisfiable, in time O(2^{δ'm}) plus a polynomial in n): the sentence asks for less. 

### `stAlgorithmOf`

 **Algorithm 1 decides 3-SAT, with the constants of its header**: «For Theorem 2, ε = δ/3, δ' is
as in Section 6, and ℓ is the first level with K_ℓ ≥ 72/δ' and e_ℓ ≤ δ'/12.» From «it suffices»,
read for deciding, and «Cost» for Count; Φ is satisfiable if and only if Z > 0. 

### `stProofNamedOf`

 **The proof of Theorem 2 in Section 6, for a named machine**: «Fix such a K ≥ 72/δ' and put g =
3K⁸ … By Lemma 4 with ε = δ/3, … it suffices to compute the number of satisfying assignments of a
3-CNF Φ on n variables with m ≤ Mn clauses, in time O(2^{δ'm}) plus a polynomial in n.» From «it
suffices», read for deciding, Lemma 1 for the algorithm of its proof, and its polynomial-time steps. 

### `stDecidesOf`

 **Theorem 2 in its decision form for step machines, with the machine named.** From Algorithm 1
with the constants of its header and Lemma 4 as an enumeration. «We may assume δ ≤ 1»: the machine
for min(δ, 1) serves. «Let M = M(δ/3)». 

### `stThroughEStarOf`

 **Theorem 2 in its decision form by the proof of Section 6**, sentence by sentence (the comments
quote the paper), from e* = 0, Lemma 4 as an enumeration, and the proof for a named machine. 

### `stByAlgorithmOf`

 **Theorem 2 in its decision form by Algorithm 1**: «For every δ > 0 there is a deterministic
algorithm that computes the number of satisfying assignments of a 3-CNF on n variables, with any
number of clauses, in time O(2^{δn}).» Here in the deciding form. A Turing machine of Mathlib
simulates Sat(ℓ, τ), for the ℓ and τ that belong to δ/2. 
