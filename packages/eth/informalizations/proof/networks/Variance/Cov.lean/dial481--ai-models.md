---
{
  "module": "proof/networks/Variance/Cov.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Variance/Cov.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Variance/Cov.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The indicators of the ordered pairs

«Each ordered pair (a,b) contributes with probability 1/K² … The indicators of two ordered pairs
have covariance 0 if the pairs are disjoint and at most 1 otherwise, and by (i) the ordered pairs
that meet a fixed pair have c-values summing to at most 4P.» (Proof of Lemma 1.)
The three facts behind these sentences are `Eight.SecNetworks.pair_prob`, `cov_disjoint` and
`meeting_le` (proof/networks/Eight/SecNetworks_Grouping.lean); here they are brought into the form
of proof/networks/Variance/Defs.lean, and Y is written as the sum of c_{a,b} over the ordered pairs
that contribute. 

### `sum_ordered`

 A sum over the ordered pairs of distinct nodes, as a double sum. 

### `sum_ordered_c`

 The total U is the sum of c_{a,b} over the ordered pairs. 

### `stYIsSum`

 Y_{γ,γ'} is the sum of c_{a,b} over the ordered pairs that contribute. 

### `stPairProb`

 «Each ordered pair (a,b) contributes with probability 1/K²». 

### `stCovDisjoint`

 «The indicators of two ordered pairs have covariance 0 if the pairs are disjoint»: both
contribute with probability 1/K⁴ = (1/K²)·(1/K²). 

### `stCovLeOne`

 «and at most 1 otherwise»: an event has probability at most 1. 

### `stMeeting`

 «by (i) the ordered pairs that meet a fixed pair have c-values summing to at most 4P». 
