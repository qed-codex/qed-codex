---
{
  "module": "proof/networks/Variance/Var.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Variance/Var.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Variance/Var.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The mean and the variance of Y, along the printed sentences

«Each ordered pair (a,b) contributes with probability 1/K², so 𝔼Y_{γ,γ'} = U/K². … Hence Var
Y_{γ,γ'} ≤ Σ_{(a,b)∈[g]²: a≠b} c_{a,b}·4P = 4PU» (proof of Lemma 1). Y is the sum of c_{a,b} times
the indicator of (a,b). So its mean is the sum of c_{a,b} times the probability of (a,b)
(`stSoMean`), and its variance is the sum of
c_p·c_q times the covariance of the indicators of p and q (`stVarIsSumOfCov`). The step «Hence»
(`stHence`) holds for any numbers in the place of the covariances that vanish for disjoint pairs and
are bounded otherwise. `stVarOf` puts the sentences together. The two moments of
proof/networks/Groundwork/Net/Colouring.lean are not used. 

### `stSoMean`

 «so 𝔼Y_{γ,γ'} = U/K²», from the two statements before it: Y_{γ,γ'} is the sum of c_{a,b} over
the ordered pairs (a, b) that contribute (`StYIsSum`), and «Each ordered pair (a,b) contributes with
probability 1/K²» (`StPairProb`). 

### `stMean`

 «so 𝔼Y_{γ,γ'} = U/K²». 

### `stVarIsSumOfCov`

 The variance of Y is the sum of c_p·c_q·Cov(p, q) over all pairs of ordered pairs. 

### `stHence`

 **«Hence»**, for any numbers κ(p, q) in the place of the covariances: if κ vanishes for disjoint
pairs, κ(p, q) ≤ m for all pairs and m ≥ 0, then Σ_p Σ_q c_p·c_q·κ(p, q) ≤ Σ_p c_p·4P·m = 4PU·m, for
c symmetric with (i) of Definition 2. 

### `stVarOf`

 «Hence Var Y_{γ,γ'} ≤ 4PU», put together from the sentences before it. 

### `stVar`

 «Hence Var Y_{γ,γ'} ≤ Σ_{(a,b)∈[g]²: a≠b} c_{a,b}·4P = 4PU». 
