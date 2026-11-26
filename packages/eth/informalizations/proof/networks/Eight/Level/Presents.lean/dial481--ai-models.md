---
{
  "module": "proof/networks/Eight/Level/Presents.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Level/Presents.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Level/Presents.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proposition 3 through Lemma 2 from the eight-square identity: the procedures present the network

The counterpart of proof/networks/SingleBitPieces/Level/Presents.lean for the pieces of Lemma 2 from
the eight-square identity. `stPresents_of`: the procedures `levelNet g tr` (a weight by g queries to
the tables of the clique, a value of a factor in one step) compute the weights and the factors of
the network
`netOfι g tr λ y Rm`, the row network or the column network of ι : ℛ → {0, …, ⌈λ/3⌉}, within a·(B +
λ)^a·t steps (t the cost of a query to the tables of the clique, not ⌈λ/3⌉) and size S + a·(size c +
B + λ)^a. In the paper it is the sentence «Both networks satisfy
Definition 2 with … τ = poly(B + λ)» in the proof of Proposition 3.
Here the values of the pieces have ⌈λ/3⌉ ≤ 2λ bits, so `presentsP8` proves the statement for pieces
whose values have at most 2λ bits. The lemmas of proof/networks/SingleBitPieces/Level/Presents.lean
that hold for any family of pieces
(`W_eq`, `f_eq`, `time_W`, `time_f`, `size_f`) are used as they are; they ask for y < (λ + 1)^{|ℛ|},
which follows from y < (⌈λ/3⌉ + 1)^{|ℛ|}. 

### `tOf_le`

 ⌈λ/3⌉ ≤ λ. 

### `netP8`

 The network of a level given by procedures, for any pieces. 

### `presentsP8`

 The procedures present the network, for any pieces that factor through at most 2λ bits and have
values of at most 2λ bits. 

### `stPresents_of`

 **Proof of Proposition 3**, «Both networks satisfy Definition 2 … with τ = poly(B + λ)»: the
procedures of a level present the row network and the column network of ι : ℛ → {0, …, ⌈λ/3⌉},
within a·(B + λ)^a·t steps, where t is the cost of a
query to the tables of the clique. Same as in the paper; the paper does not speak of sizes. 
