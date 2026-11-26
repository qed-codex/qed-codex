---
{
  "module": "proof/consequences/PrintedOrder/Deciding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/PrintedOrder/Deciding.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/PrintedOrder/Deciding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, Corollary 5 through the implication

«Theorem 2 gives s_3=0, which is the negation of ETH. By a theorem of Impagliazzo, Paturi and Zane
[…], which rests on their Sparsification Lemma, s_3 = 0 implies s_k = 0 for every k ≥ 3» (proof of
Corollary 5)
* `stThreeSatFamily`: `SplitSat.stCore3` gives, for each exponent δ₃ > 0, a level ℓ and a threshold
  parameter τ; choosing them gives a family of procedures for 3-SAT.
* `hostedFrom`: from the implication for machines cut into steps (`SplitSat.StImplication`, a
  hypothesis), taken at δ/2, and the host theorem (`SplitSat.exists_simulates`,
  `decidesTM_of_simulates`): k-SAT on Turing machines from ANY family of procedures for 3-SAT.
  `stHosted`: the same on `SplitSat.stImplication`.
* `endThroughImplication`: Corollary 5 from the family, `StHosted` and `SplitSat.StTiedThreeTM`,
  which are hypotheses; `eth_and_seth_false`: on their proofs.
The implication is for machines cut into polynomial-time steps, not for arbitrary algorithms. 

### `stThreeSatFamily`

 **«Theorem 2 gives s_3=0», for machines cut into steps**: there is a family of procedures for
3-SAT, one for each exponent δ₃ > 0, each with polynomial-time steps, and each member is the machine
of Theorem 2 in its decision form without the part that reads the input, at some level ℓ and
threshold parameter τ. From `SplitSat.stCore3`, by choice. 

### `hostedFrom`

 **k-SAT on Turing machines from any family of procedures for 3-SAT**, from the implication for
machines cut into steps, which is a hypothesis. The implication is taken at δ/2; a Turing machine
simulates the machine that it gives, with polynomial overhead. 

### `stHosted`

 **k-SAT on Turing machines from any family of procedures for 3-SAT, through the implication**:
`hostedFrom` on `SplitSat.stImplication`. 

### `endThroughImplication`

 **Corollary 5 in the order of its printed proof**, from three statements taken as hypotheses:
«s_k = 0 for every k ≥ 3. Hence s_∞ = 0, and both ETH and SETH are false.» At k = 3 the Turing
machine is that of `SplitSat.StTiedThreeTM` («Theorem 2 gives s_3=0»); at k > 3 the family of
`StThreeSatFamily` is handed to `StHosted`; then the general `SatK.sTM_eq_zero_of`. 

### `eth_and_seth_false`

 **Corollary 5**, in the wording of PaperSentencesStatement.lean: `endThroughImplication` on
`stThreeSatFamily`, `stHosted` and `SplitSat.stTiedThreeTM`. For k > 3 the way is: Theorem 2 gives
the family, the implication gives the machine for k-SAT, a Turing machine simulates it. 
