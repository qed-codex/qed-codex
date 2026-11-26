---
{
  "module": "proof/networks/Variance/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Variance/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Variance/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «Hence Var Y ≤ Σ c_{a,b}·4P = 4PU», summed from the covariances (definitions and statements only)

Proof of Lemma 1, «A good grouping exists»: «Each ordered pair (a,b) contributes with probability
1/K², so 𝔼Y_{γ,γ'} = U/K². The indicators of two ordered pairs have covariance 0 if the pairs are
disjoint and at most 1 otherwise, and by (i) the
ordered pairs that meet a fixed pair have c-values summing to at most 4P. Hence Var Y_{γ,γ'} ≤
Σ_{(a,b)∈[g]²: a≠b} c_{a,b}·4P = 4PU ≤ 4gP².»
proof/networks/Eight/SecNetworks_Grouping.lean states these sentences (`pair_prob`, `mean_Y`,
`cov_disjoint`, `meeting_le`, `var_Y`), but proves `mean_Y` and `var_Y` from the two moments of
proof/networks/Groundwork/Net/Colouring.lean (`sum_Ys`, `sum_Ys_sq`), not from the sentences before
them.
This folder proves them along the printed words: Y is the sum of c_{a,b} times the indicator of
(a,b); so its mean is the sum of the probabilities and its variance is the sum of c_p·c_q·Cov(p,q)
over all pairs of ordered pairs; the disjoint ones give 0, the others at most 1;
for each p the c-values of the q that meet p sum to at most 4P. Then the sentences that rest on the
variance of Y (Chebyshev for Y, the union bound over the pairs of groups) are also proved on top of
this. The sentences on the SIZES of the groups («A group has mean size g/K and variance at most g/K,
so it exceeds 2g/K with probability at most K/g; … some group does so with probability at most K²/g
< 1/3»)
do not rest on the variance of Y; the paper gives no derivation of the two moments of the size, and
their proofs in SecNetworks_Grouping.lean (`mean_size`, `var_size`, `cheb_size`, `some_group`) are
used as they are. So are `total_le` («4PU ≤ 4gP²»: U ≤ gP), `card_pairs_lt`, `Y_symm` and
`exists_good_of` (the last union bound).

**How the statements follow the paper's steps.** A step «hence» is stated, where that is possible,
for ARBITRARY data that satisfy what the paper derives it from (`StHence`, `StChebOfVar`,
`StSomePairOfCheb`): such a statement cannot be proved without using its hypotheses. The other
implications (`StSoMean`, `StGroupingOf`, `StSearchOfGrouping`) are between closed propositions.

As in SecNetworks_Grouping.lean, **probabilities are counts** over the K^g groupings χ : [g] → [K],
with denominators cleared: «Pr(E) = p» reads #{χ | E} = p·K^g. So the covariance of two indicators,
Pr(both) − (1/K²)², is multiplied by K⁴·K^g (`cov`).
This file has no proofs. 

### `ordered`

 The ordered pairs (a, b) of distinct nodes. 

### `Contributes`

 The ordered pair p = (a, b) «contributes» to Y_{γ,γ'} under the grouping χ: a ∈ G_γ and b ∈
G_{γ'}. 

### `Meets`

 The ordered pair q meets the ordered pair p: they have a node in common. «Disjoint» is the
negation. 

### `cov`

 The covariance of the indicators of the ordered pairs p and q (pairs of distinct nodes),
multiplied by K⁴·K^g: Pr(both contribute) − (1/K²)·(1/K²) becomes K⁴·#{χ | both contribute} − K^g. 

### `StYIsSum`

 Y_{γ,γ'} is the sum of c_{a,b} over the ordered pairs that contribute (γ ≠ γ', so a pair (a, a)
never contributes). 

### `StPairProb`

 «Each ordered pair (a,b) contributes with probability 1/K²». 

### `StMean`

 «so 𝔼Y_{γ,γ'} = U/K²». 

### `StVarIsSumOfCov`

 The variance of a sum of multiples of indicators is the sum of the covariances: Var Y_{γ,γ'} =
Σ_p Σ_q c_p·c_q·Cov(p, q), both sides multiplied by K⁴·K^g. The paper uses this without words, in
«Hence». 

### `StCovDisjoint`

 «The indicators of two ordered pairs have covariance 0 if the pairs are disjoint». 

### `StCovLeOne`

 «and at most 1 otherwise» (it holds for all pairs). 

### `StMeeting`

 «by (i) the ordered pairs that meet a fixed pair have c-values summing to at most 4P». 

### `StVar`

 «Hence Var Y_{γ,γ'} ≤ Σ_{(a,b)∈[g]²: a≠b} c_{a,b}·4P = 4PU»: Σ_χ (Y − U/K²)² ≤ 4PU·K^g,
multiplied by K⁴. Word for word the statement of `Eight.SecNetworks.var_Y`. 

### `StHence`

 **The step «Hence»**, for arbitrary numbers κ(p, q) in the place of the covariances and an
arbitrary bound m ≥ 0 in the place of 1: if κ(p, q) = 0 for disjoint pairs and κ(p, q) ≤ m for all
pairs, then Σ_p Σ_q c_p·c_q·κ(p, q) ≤ Σ_p c_p·4P·m = 4PU·m, for c symmetric with (i). 

### `StVarOf`

 «Hence Var Y ≤ 4PU», put together: the variance is the sum of the covariances; these are 0 for
disjoint pairs and at most 1 otherwise; the step «Hence». 

### `StSoMean`

 «so 𝔼Y = U/K²», with what it rests on in its hypotheses. 

### `StTotalLe`

 «4PU ≤ 4gP²»: U ≤ gP, by (i). (The statement of `Eight.SecNetworks.total_le`.) 

### `VarBound`

 Var Y_{γ,γ'} ≤ 4PU, for given numbers c, P and groups γ, γ' (multiplied by K⁴·K^g). 

### `ChebBound`

 Pr(Y_{γ,γ'} > U/K² + gP/K³) ≤ 4K⁶/g, for given numbers c, P and groups γ, γ' (the event
multiplied by K³). 

### `StChebOfVar`

 **«and by Chebyshev Pr(Y_{γ,γ'} > U/K² + gP/K³) ≤ 4K⁶/g»**, from the bound on the variance and U
≤ gP, for arbitrary numbers c and P for which these two hold. 

### `StSomePairOfCheb`

 **«By a union bound over the fewer than K²/2 pairs of groups, some pair violates this bound with
probability less than»** (K²/2)·(4K⁶/g), from the bound for each pair of groups, for arbitrary
symmetric numbers c for which that bound holds. 

### `StGroupingOf`

 The paragraph at g = 3K⁸ with the numbers of the text (`Eight.SecNetworks.GroupingFacts`), from
the bound on the variance of Y through the two steps above; its fields on the sizes of the groups
are `Eight.SecNetworks.cheb_size` and `some_group`, and the last union bound is
`Eight.SecNetworks.exists_good_of`. 

### `StSearchOfGrouping`

 «Go through all K^g groupings (a constant) and fix the first good one»
(`Eight.ViaGrouping.StSearch`), from «a good grouping exists». 
