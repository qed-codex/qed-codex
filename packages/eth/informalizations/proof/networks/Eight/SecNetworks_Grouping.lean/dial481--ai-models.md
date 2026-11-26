---
{
  "module": "proof/networks/Eight/SecNetworks_Grouping.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecNetworks_Grouping.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecNetworks_Grouping.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Lemma 1, «A good grouping exists»: every sentence with the paper's numbers

The paragraph chooses χ(a) ∈ [K] independently and uniformly for each of the g nodes. Here **probabilities
are rendered as counts** over the K^g groupings χ : [g] → [K], with denominators cleared:
«Pr(E) ≤ p» reads #{χ | E} ≤ p·K^g, «𝔼X = m» reads Σ_χ X(χ) = m·K^g, and «Var X ≤ v» reads Σ_χ (X(χ)
− m)² ≤ v·K^g. No measure theory is used.

The sentences, in the order of the text: `Y_symm`, `pair_prob`, `mean_Y`, `cov_disjoint`,
`meeting_le`, `var_Y`, `total_le`, `cheb_Y`, `card_pairs_lt`, `some_pair`, `mean_size`, `var_size`,
`cheb_size`, `some_group`,
and the closing theorem `groupingFacts : GroupingFacts` (g = 3K⁸: 4/(3K²), < 2/3, K/g, < 1/3, a good
grouping exists).

The two moments of Y and of the size of a group are taken from
proof/networks/Groundwork/Net/Colouring.lean, which counts groupings with prescribed values;
`pair_prob`, `cov_disjoint` and `meeting_le` state in the paper's words the three lemmas on which
its moments of Y rest (`card_two`, `card_four`, `sum_meet`) and are not used again below. Its bound
on the variance of Y, 4PU/K², is sharper than the 4PU of the paper
(a pair that meets a fixed pair is given covariance at most 1/K² there, at most 1 in the paper);
`var_Y` states the paper's 4PU, and both uses of Chebyshev and all three union bounds below are made
from the paper's numbers. 

 ### Passage to the lemmas on counts (which want c_{a,a} = 0) 

### `off`

 The numbers c_{a,b} with 0 on the diagonal. 

### `var_of_moments`

 From the first two moments to the variance, denominators cleared: if Σ Y·A = N·m and Σ Y²·A² ≤
N·m² + V, over N points, then Σ (A·Y − m)² ≤ V. 

### `cheb_count`

 Chebyshev's inequality as a count, denominators cleared: if Σ (A·X − m)² ≤ V, then the number of
points with t·(A·X − m) > s, times s², is at most t²·V. 

 ### The shared bits between two groups 

### `Y_symm`

 «let Y_{γ,γ'} = Y_{γ',γ} be the sum of c_{a,b} over all a ∈ G_γ and b ∈ G_{γ'}»: the equality,
from c_{a,b} = c_{b,a}. 

### `pair_prob`

 «Each ordered pair (a,b) contributes with probability 1/K²». 

### `mean_Y`

 «so 𝔼Y_{γ,γ'} = U/K²». 

### `cov_disjoint`

 «The indicators of two ordered pairs have covariance 0 if the pairs are disjoint»: both pairs
contribute with probability 1/K⁴ = (1/K²)·(1/K²). («and at most 1 otherwise» needs no proof:
indicators are at most 1.) 

### `meeting_le`

 «by (i) the ordered pairs that meet a fixed pair have c-values summing to at most 4P». 

### `var_Y`

 «Hence Var Y_{γ,γ'} ≤ Σ_{(a,b) : a ≠ b} c_{a,b}·4P = 4PU»: Σ_χ (Y − U/K²)² ≤ 4PU·K^g, multiplied
by K⁴. 

### `total_le`

 «4PU ≤ 4gP²»: U ≤ gP, by (i). 

### `cheb_Y`

 «and by Chebyshev Pr(Y_{γ,γ'} > U/K² + gP/K³) ≤ 4K⁶/g», for every g. The event is multiplied by
K³. Proved from `var_Y` and `total_le`: the deviation is gP/K³, so the bound is 4gP²·K⁶/(gP)². 

### `card_pairs_lt`

 «the fewer than K²/2 pairs of groups»: there are K(K − 1)/2 pairs γ < γ'. 

### `some_pair`

 «By a union bound over the fewer than K²/2 pairs of groups, some pair violates this bound with
probability less than» (K²/2)·(4K⁶/g), for every g: the union runs over the pairs γ < γ' only, since
Y_{γ,γ'} = Y_{γ',γ}. 

 ### The sizes of the groups 

### `mean_size`

 «A group has mean size g/K». 

### `var_size`

 «and variance at most g/K»: Σ_χ (|G_γ| − g/K)² ≤ (g/K)·K^g, multiplied by K². 

### `cheb_size`

 «so it exceeds 2g/K with probability at most K/g», for every g: Chebyshev with deviation g/K. 

### `some_group`

 «by a union bound over the K groups, some group does so with probability at most K²/g», for
every g. 

 ### g = 3K⁸ 

### `exists_good_of`

 «By a union bound over these two events, the grouping fails to be good with probability less
than 1, so a good grouping exists.» From «less than 2/3» and «less than 1/3». 

### `groupingFacts`

 **«A good grouping exists»**: the steps of the paragraph at g = 3K⁸, with the numbers 4/(3K²),
2/3, K/g, 1/3 of the text. Same as in the paper, but for probabilities written as counts over the
K^g groupings. 
