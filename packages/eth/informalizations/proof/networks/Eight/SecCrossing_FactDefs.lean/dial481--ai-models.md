---
{
  "module": "proof/networks/Eight/SecCrossing_FactDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_FactDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_FactDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 2(b): the factorization of the product that belongs to one set Q of blocks (a statement only)

Proof of Lemma 2(b): the product with C at the blocks in Q and R at the others has a row-wise
factorization (f_Q, f'_Q) through 3(t − i) + 6i bits, whose index θ' lists the blocks s = 1, …, t in
order.
`StChunk` says this for a fixed Q, in both directions at once: the sum over all words θ' of the
product of the two functions is the product over the blocks. The four strings are called a, b
(arguments of the first function) and
a', b' (arguments of the second). A block that is not wide contributes Σ_k ψ_k(a,b)·ψ_k(b',a') =
R(a,b,a',b'); a wide block contributes Σ_{k,k'} [(a,b) = (k,k')]·R(k,a',k',b') = R(a,a',b,b'). 

### `lenW`

 The number of bits of θ': 3 for each block and 3 more for each wide block. 

### `StChunk`

 The factorization of the product that belongs to Q. 
