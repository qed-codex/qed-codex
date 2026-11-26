---
{
  "module": "proof/networks/Eight/ViaGrouping/Search.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Search.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Search.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Lemma 1, «The algorithm», first three sentences: the search for a good grouping

«Being good depends only on the numbers c_{a,b}. Go through all K^g groupings (a constant) and fix
the first good one. Let L = max{1, ⌊(U + gP/K)/K²⌋}, so that Y_{γ,γ'} ≤ L.»
* `goodP_iff`: on a network in the sense of Definition 2 the test `goodP` of the program says yes to
  the number x exactly if the grouping number x is good as printed (`SecNetworks.Good`: (G1) at most
  2g/K nodes in a group, (G2) with the given P).
* `exists_goodP`: for g = 3K⁸ the test says yes to some x < K^g. The good grouping comes from the
  paragraph «A good grouping exists» (`SecNetworks.groupingFacts`,
  proof/networks/Eight/SecNetworks_Grouping.lean).
* `stSearch : StSearch`: so the first x < K^g to which the test says yes exists, and the grouping
  number x is good.
* `lamP_eq`, `Y_le_of_good`: the number `lamP` of the program is L; «so that Y_{γ,γ'} ≤ L».
* `searchP_runs`: the search takes 2·K^g steps (one step for a test, one to go on), on states of
  size at most 4·(size of the context + size of K^g) + 10. So the search through the groupings is
  counted: «(a constant)».

Different from the paper: one test of a grouping counts as one step of the step machine; the search
runs through all K^g numbers and keeps the first good one. 

 ## The numbers of the program are the numbers of the network 

### `presentsP`

 The procedures `Np.toPaperNetwork` present the network `N.toPaperNetwork`; that the algorithm of
Definition 2 (iii) receives B is not needed for this. From `SecNetworks.presents_toPaperNetwork`,
applied to Np with the number B put in. 

### `Uc_eq_U`

 The sum of the given numbers c_{a,b} that the program forms is the total U. 

### `lbLen_eq_Y`

 The number of bits between two groups that the program forms is Y_{γ,γ'}. 

### `goodP_iff`

 «Being good depends only on the numbers c_{a,b}»: the test of the program says yes to x exactly
if the grouping number x is good as printed, with (G1) as printed and with the given P in (G2). 

 ## The first good grouping 

### `grouping_number`

 Every grouping has a number below K^g: its values are the digits in base K. 

### `exists_goodP`

 For g = 3K⁸ the test says yes to some number below K^g: «a good grouping exists»
(`SecNetworks.groupingFacts`), from c_{a,b} = c_{b,a} and (i) of Definition 2. 

### `stSearch`

 **«Go through all K^g groupings and fix the first good one.»** For g = 3K⁸ there is a first
number x < K^g to which the test says yes, and the grouping number x is good as printed. 

 ## The number L 

### `lamP_eq`

 The number that the program passes to the algorithm for cliques is L = max{1, ⌊(U + gP/K)/K²⌋},
written max{1, ⌊(KU + gP)/K³⌋}. 

### `Y_le_of_good`

 «… so that Y_{γ,γ'} ≤ L», for a good grouping. 

 ## The run of the search 

### `searchP_runs`

 The search, for any procedures and any context: 2·K^g steps, on states of size at most 4·(size
of c + size of K^g) + 10; the result is the first x < K^g to which the test says yes, if there is
one. Both bounds but for the size of c depend on K and g only: «(a constant)». 
