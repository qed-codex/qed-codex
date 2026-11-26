---
{
  "module": "proof/rates/ClauseBound/Group/Sample.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Group/Sample.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Group/Sample.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Hoeffding's inequality for sampling without replacement, as a count

Let e_n be the sum of the products of x over the n-subsets of a set of N elements, x ≥ 0. First e_n
≤ C(N, n)·(mean of x)ⁿ, a case of Maclaurin's inequality (`esymm_le`). The proof is
an induction on the set: with one more element a, e_{k+1} = e_{k+1}' + x_a·e_k'; by the induction
hypothesis and two identities between binomial coefficients this is at most
C(N, k+1)·u^k·((k+1)·w − k·u), where u is the old mean and w the new one; and (k+1)·w·u^k ≤ w^{k+1} +
k·u^{k+1}.

Then the exponential moment: the number of n-subsets S with Σ_{i ∈ S} c_i ≥ a, times e^{θa}, is at
most the sum over all n-subsets of ∏_{i ∈ S} e^{θ c_i}, so at most
C(N, n)·(mean of e^{θ c_i})ⁿ. The mean is bounded by convexity and Hoeffding's lemma on two points,
and θ = 4t/R. 

### `tangent_le`

 (k+1)·w·u^k ≤ w^(k+1) + k·u^(k+1) for u, w ≥ 0. 

### `sum_powersetCard_insert`

 The sum of the products over the (k+1)-subsets when one element is added. 

### `esymm_le`

 The sum of the products over the n-subsets is at most C(N, n) times the n-th power of the mean. 

### `avg_exp_le`

 The mean of e^{θ c_i} is at most exp(θ·mean + (θR)²/8) if all c_i lie in [0, R]. 

### `card_sample_tail_le`

 Among the n-subsets S of s, at most the fraction exp(−2nt²) has Σ_{i ∈ S} c_i ≥ n·(mean of c) +
t·n·R, if all c_i lie in [0, R]. 
