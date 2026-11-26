---
{
  "module": "proof/rates/CountedRecursion/CountBase.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/CountBase.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/CountBase.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The count at the depth 0

In the proof of Theorem A (b), for ℓ = 0 brute force sums 2^{λK₀(K₀−1)/2} ≤ 2^{e₀K₀²λ} terms, each
at a cost of at most (K₀(λ+B))^{C₅}. The cost of the solver at the depth 0 is written out in
`solverCost`: 2^{λK₀(K₀−1)/2}·(K₀ + 1 + K₀t) if a query to the tables costs t.
For t ≥ 1 this is at most t times the bound of the theorem, for every C₀ ≥ 1: K₀ + 1 + K₀t ≤ 3K₀t ≤
t·(2K₀)² ≤ t·(K₀(λ+B))^{C₀K₀²}; the inequality of the exponents of 2 is
`GeneralPieces.Rate.brute_le`. 

### `base_count`

 The arithmetic on natural numbers: A(k + 1) + Akt ≤ t·(A·X^n) for 1 ≤ k, 2k ≤ X, n ≥ 2, t ≥ 1. 

### `countBaseFrom`

 `CountBaseFrom`. 

### `countBase`

 `CountBase`. 
