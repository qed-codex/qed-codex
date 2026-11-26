---
{
  "module": "proof/networks/Variance/Grouping.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Variance/Grouping.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Variance/Grouping.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From the variance of Y to the first good grouping

«… = 4PU ≤ 4gP², and by Chebyshev Pr(Y_{γ,γ'} > U/K² + gP/K³) ≤ 4K⁶/g = 4/(3K²). By a union bound
over the fewer than K²/2 pairs of groups, some pair violates this bound with probability less than
2/3. … so a good grouping exists.» and «Go through all K^g groupings (a constant) and fix the first
good one.» (proof of Lemma 1.)
The proofs are those of proof/networks/Eight/SecNetworks_Grouping.lean (`cheb_Y`, `some_pair`,
`groupingFacts`) and proof/networks/Eight/ViaGrouping/Search.lean (`exists_goodP`, `stSearch`), with
the step before each in its hypotheses; so they rest on the variance of
proof/networks/Variance/Var.lean. The sentences on the sizes of the groups are taken from
SecNetworks_Grouping.lean as they are (`cheb_size`, `some_group`), and so are
`total_le`, `card_pairs_lt`, `Y_symm`, `exists_good_of` and Chebyshev's inequality as a count
(`cheb_count`). `cheb_count` is private in SecNetworks_Grouping.lean; the line
`import all Eight.SecNetworks_Grouping` is there only to reach it. 

### `stTotalLe`

 «4PU ≤ 4gP²»: U ≤ gP, by (i) of Definition 2. 

### `Y_le_total`

 Y_{γ,γ'} ≤ U: a sum over some of the ordered pairs. 

### `stChebOfVar`

 «and by Chebyshev Pr(Y_{γ,γ'} > U/K² + gP/K³) ≤ 4K⁶/g», from Var Y ≤ 4PU and U ≤ gP: the
deviation is gP/K³, so the bound is 4gP²·K⁶/(gP)². The proof is that of `Eight.SecNetworks.cheb_Y`,
from the two hypotheses. 

### `stSomePairOfCheb`

 «By a union bound over the fewer than K²/2 pairs of groups, some pair violates this bound with
probability less than» (K²/2)·(4K⁶/g): the union runs over the pairs γ < γ' only, since Y_{γ,γ'} =
Y_{γ',γ}. The proof is that of `Eight.SecNetworks.some_pair`, from the hypothesis. 

### `stGroupingOf`

 **«A good grouping exists»**: the steps of the paragraph at g = 3K⁸, with the numbers 4/(3K²),
2/3, K/g, 1/3 of the text, from the bound on the variance of Y through Chebyshev and the union bound
over the pairs of groups. 

### `groupingFacts`

 «A good grouping exists», with the numbers of the text, on the variance summed from the
covariances. (Not the theorem of the same name in `Eight.SecNetworks`.) 

### `stSearchOfGrouping`

 **«Go through all K^g groupings (a constant) and fix the first good one.»** For g = 3K⁸ there is
a first number x < K^g to which the test says yes, and the grouping number x is good as printed;
from «a good grouping exists». 

### `stSearch`

 «Go through all K^g groupings (a constant) and fix the first good one», on the variance summed
from the covariances. (Not the theorem of the same name in `Eight.ViaGrouping`.) 
