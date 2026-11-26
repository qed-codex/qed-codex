---
{
  "module": "proof/rates/GeneralPieces/Top/CaseI.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Top/CaseI.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Top/CaseI.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The top levels of Theorem A(c), by case (i) of Lemma 8

"Let K = K_ℓ, e = e_ℓ for the largest ℓ with K_ℓ ≤ m^{1/9}, and g = 3K⁸ ≤ m": a network on g = 3K⁸
nodes is rebalanced to K nodes and handed to the algorithm for cliques. `val_caseI` calls the lemma
(`GeneralPieces.grouping_general`) in case (i), with ζ = 1/(2K); `Lof_le_of` compares the lemma's L =
⌈(U + gP/K)/K²⌉ with the string lengths of the cliques that the programs build, which are computed
from an upper bound for U.
`stCountG2` is the statement for the network of a k-CNF (the bound in m), `stValS2` the one for any
network (the bound in n). 

### `sized_mono`

 A network with parameter P is one with every parameter P' ≥ P. 

### `pow_le_two_pow`

 K^g ≤ 2^(g·size K). 

### `Lof_le_of`

 With ζ = 1/(2K), the lemma's L = ⌈(U + gP/K)/K²⌉ is at most ⌊(K³ + K·Ub + gP)/K³⌋ for every Ub ≥
U. 

### `one_le_div`

 1 ≤ ⌊(K³ + r)/K³⌋. 

### `val_caseI`

 A network on g = 3K⁸ nodes, rebalanced to K nodes by case (i) of Lemma 8 and handed to a correct
algorithm for cliques, gives its value, if β, the string length of the clique handed on, is at
least the lemma's L and the length of the padding string `pad` is at least each of the five powers
`f1`–`f5`, which bound the work. 

### `stValS2`

 The algorithm for cliques at the index i, fed with the rebalanced network, returns the value of
the network. 

### `stCountG2`

 "So P = 2k⌈m/g⌉, B = 1, U < 2km": the algorithm for cliques at the index i, fed with the
rebalanced network of a k-CNF ψ, returns the value of that network. Here the values of the network
are 0 and ±1,
and B = 0 because bounds are "at most 2^B". 
