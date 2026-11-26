---
{
  "module": "proof/rates/CountedRecursion/CaseTwo.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/CaseTwo.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/CaseTwo.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Case (ii) of Lemma 8 applies, and the lemma's L

Proof of Theorem A (b), the step from ℓ to ℓ + 1: so P = g³λ, gP = N, and moreover c_{a,a'} ≤ g²λ =
P/g. Case (ii) of Lemma 8 applies to the network with the smaller total (with B₁ in the role of B):
K divides g and 2ζ²g = 2^{ℓ+x₀−9}K, while 2gK ≤ g² = K_{ℓ+1} gives ln(2gK) ≤ 0.7·log K_{ℓ+1} ≤ 1.4(3x₀+6)2^ℓ,
and 1.4(3x₀+6) ≤ 2^{x₀−9} for x₀ ≥ 18. Also 1/g ≤ ζ, since ζg = 2^{2ℓ+x₀−5}K. So the lemma's L
satisfies K²L ≤ U + 2ζN + K² ≤ (ρ + 3ζ)N + (c/4)g⁴log(2λ) + K².
* `shared_le`: c_{a,a'} ≤ g²λ, for every g (`ClauseBound.Alg.GridNet.gridN_c_le`).
* `caseTwoApplies : CaseTwoApplies`: with `GeneralPieces.Chain.K_dvd_g` and
  `GeneralPieces.Chain.hoeffding_cond`, which is proved there from the sentences of the proof on
  2ζ²g and ln(2gK), one theorem for each.
* `label_first`: K²L ≤ U + 2ζN + K², for L = ⌈(U + 2ζgP)/K²⌉; `labelBound : LabelBound`: the whole
  display, with `GeneralPieces.Chain.inv_g_le_zeta`. 

### `zeta_cast`

 ζ_ℓ as the machines have it, 1/2^{ℓ+5} with the power a natural number. 

### `shared_le`

 «and moreover c_{a,a'} ≤ g²λ». 

### `caseTwoApplies`

 **«Case (ii) of Lemma 8 applies to the network with the smaller total»**: to either network. 

### `label_first`

 «K²L ≤ U + 2ζN + K²», for the lemma's L = ⌈(U + 2ζgP)/K²⌉, P = g³λ. 

### `labelBound`

 **«So the lemma's L satisfies K²L ≤ U + 2ζN + K² ≤ (ρ + 3ζ)N + (c/4)g⁴log(2λ) + K².»** 
