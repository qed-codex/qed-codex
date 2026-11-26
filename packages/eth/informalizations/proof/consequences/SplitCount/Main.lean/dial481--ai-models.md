---
{
  "module": "proof/consequences/SplitCount/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Corollary 6: the choice of δ', and the corollary from the tied statement

«The constants in O(n) depend on k and ε, so choosing ε = δ/3 first and then δ' small enough gives
time O(2^{δn}).»
* `deltaPrime_facts`: δ' = `deltaPrime δ w Bl` is positive, at most 1, and small enough.
* `stCountsAt`: `stStepOne`, for a level ℓ of Algorithm 1, put into «this suffices» (`stSuffices`).
* `endFrom`: Corollary 6 in the wording of PaperSentencesStatement.lean, both halves from the tied
  statement `StTiedTM`, which is taken as a hypothesis. 

### `deltaPrime_facts`

 «then δ' small enough»: for δ > 0 and w ≥ 3, δ' = `deltaPrime δ w Bl` is positive, at most 1,
and δ'·(1 + 3(w − 3))·(Bl + 1) ≤ δ/3. 

### `stCountsAt`

 **The choice of δ', with the machine named.** Under the hypotheses of `StCountsAt`,
`engineSplit step ℓ` serves as the procedure for #k-SAT with the exponent δ. 

### `endFrom`

 **Corollary 6**: «For every k ≥ 3 and δ > 0 there is a deterministic algorithm that computes the
number of satisfying assignments of a k-CNF on n variables in time O(2^{δn}). For k = 3 this says
that the counting version #ETH of ETH is false.»
The statement is `PaperSentences.CorCounting` of PaperSentencesStatement.lean, for Turing machines.
Here it is drawn from the tied statement `StTiedTM` as a hypothesis: both halves take the Turing
machine of that statement, which simulates `COUNTsplit k ℓ τ`; the second half at k = 3, by
`CountKSat.EndLemmas.not_CountETH_TM_of`. 
