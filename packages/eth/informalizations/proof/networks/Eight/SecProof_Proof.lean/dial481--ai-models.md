---
{
  "module": "proof/networks/Eight/SecProof_Proof.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecProof_Proof.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecProof_Proof.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemmas for the section «Proof of Theorem 2» (Section 6 of the paper)

The file is named after its counterpart proof/networks/Paper/SecProof_Proof.lean. It holds one
definition and three small lemmas for the proof of Theorem 2.

What that proof takes from Lemma 4: the deciding form of the step «it suffices to compute the number
of satisfying assignments of a 3-CNF Φ on n variables with m ≤ Mn clauses, in time O(2^{δ'm})», with
Lemma 4 in its form for deciding, is the statement `SufficesSparse δ M S`, a property of a constant
M and of a construction S of machines.
For the paragraph «Constants and reduction»: δ' = δ/(3M) ≤ 1/3 for δ ≤ 1 and M ≥ 1, and a K ≥ 72/δ'
is at least 2. Finally, a machine that decides 3-SAT within c·2^{δn} steps does so for every larger
δ. 

 ## What the proof of Theorem 2 takes from Lemma 4 

### `SufficesSparse`

 The deciding form, as used for Theorem 2 in its decision form, of «it suffices to compute the
number of satisfying assignments of a 3-CNF Φ on n variables with m ≤ Mn clauses, in time
O(2^{δ'm})», δ' = δ/(3M), as a property of the constant M and of a construction S of machines:
whenever the step machine `Mc` returns, for every formula Φ
with m clauses of at most 3 literals, within A·2^{δ'm} steps an integer that is positive exactly if
Φ is satisfiable, the machine `S Mc` decides 3-SAT on n variables within c·2^{δn} steps; and the
steps of `S Mc` are polynomial time if those of `Mc` are.
Different from the paper: `Mc` is asked to work for every m, not only for m ≤ Mn; there is no «plus
a polynomial in n»: steps are counted, and a step may take time polynomial in the size of Φ; the
states of `Mc` must have polynomial size. 

 ## Lemmas for the proof of Theorem 2 

### `delta'_le`

 «Let … δ' = δ/(3M) ≤ 1/3», for δ ≤ 1 and M ≥ 1. 

### `two_le_of_le`

 A number K ≥ 72/δ' with δ' ≤ 1/3 is at least 2 (even at least 216), as the definition of
«achievable» in the paper asks. 

### `decidesInSteps_mono`

 A machine that decides 3-SAT within c·2^{δn} steps does so within c·2^{δ₁n} steps for every δ₁ ≥
δ. 
