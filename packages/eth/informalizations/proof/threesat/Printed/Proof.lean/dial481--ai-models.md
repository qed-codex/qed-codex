---
{
  "module": "proof/threesat/Printed/Proof.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/Proof.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/Proof.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The proof of Theorem 2 in Section 6, and Algorithm 1, from `Printed.Achievable` (Definition 4 with a bound on the sizes of the states)

Section 6, «Constants and reduction» and «Cost». What is taken as a hypothesis in each theorem is
named in its statement: «it suffices …» in its deciding form (`Suffices.StSuffices`) and Lemma 4 as
an enumeration (`Enumerate.StEnumeration`), which are proved in proof/threesat/Suffices/ and
proof/threesat/Enumerate/; Lemma 1 for the algorithm of its proof (`StGroupingTied`,
`StGroupingPoly`, `StOnProcedures`) and «(K_ℓ, e_ℓ) is achievable» (`StClique`), which are proved in
this folder.
* `stProofNamed_of`: the proof of Section 6 for ANY machine that does what Definition 4 asks for (K,
  δ'/12);
* `stAlgorithm_of`: Sat(ℓ, τ) decides 3-SAT within c·2^{δn} steps, ℓ the first level with K_ℓ ≥
  72/δ' and e_ℓ ≤ δ'/12 (the header of Algorithm 1); `stDecides_of`: the same for every δ > 0;
* `threeSat_through_eStar_of`, `threeSat_by_algorithm_of`: Theorem 2 for Turing machines of Mathlib,
  in the two ways. 

### `decidesSparse_of_cost`

 Since Φ is satisfiable if and only if Z > 0: a machine that counts within A·2^{δ'm} steps does
what the deciding form of the paper's reduction asks: decide whether a 3-CNF Φ with m ≤ Mn clauses
is satisfiable, in time O(2^{δ'm}) plus a polynomial in n. 

### `stProofNamed_of`

 **The proof of Theorem 2 in Section 6, from the printed definition.** Let 0 < δ ≤ 1, M = M(δ/3)
and τ the constant and the parameter of Lemma 4, δ' = δ/(3M) ≤ 1/3, K ≥ 72/δ', g = 3K⁸. For any
machine that does what Definition 4 asks for (K, δ'/12): Lemma 1 for the algorithm of its proof; the
network of Φ and «Cost»; «it suffices …». 

### `stAlgorithm_of`

 **Algorithm 1 decides 3-SAT, with the constants of its header**: ε = δ/3, M and τ from Lemma 4,
δ' = δ/(3M), and ℓ the first level with K_ℓ ≥ 72/δ' and e_ℓ ≤ δ'/12. From «it suffices …» in its
deciding form and «Cost» for Count. 

### `stDecides_of`

 **Theorem 2 in its decision form for step machines, with the machine named.** «We may assume δ ≤
1»: the machine for min(δ, 1) serves. From Algorithm 1 with the constants of its header and Lemma 4. 

### `threeSat_through_eStar_of`

 **Theorem 2 in its decision form by the proof of Section 6**: «Since e* = 0 < δ'/12 and
achievability is monotone in e (Definition 4), (K, δ'/12) is achievable for infinitely many K. Fix
such a K ≥ 72/δ'». The bound in steps is proved for δ/2, and the polynomial cost of a step is paid
at the end (`Paper.steps_to_time`). 

### `threeSat_by_algorithm_of`

 **Theorem 2 in its decision form by Algorithm 1**: a Turing machine of Mathlib simulates Sat(ℓ,
τ). 
