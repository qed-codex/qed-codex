---
{
  "module": "proof/networks/Eight/SecCrossing_Chunk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_Chunk.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_Chunk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 2(b): the factorization of the product that belongs to one set Q

In the proof of Lemma 2(b), the display that defines R and C and observation (a) after Definition 1
give this product a row-wise factorization (f_Q, f'_Q) through 3(t − i) + 6i bits, whose index θ'
lists the indices of the blocks s = 1, …, t in this order.
The file proves `StChunk`: for a fixed Q, the sum over all words θ' of the product of the two
functions is the product over the blocks. The proof is observation (a) (a product of functions of
separate arguments factors through the
sum of the numbers of bits) carried out by induction on the number of blocks: a word θ' for t + 1
blocks is a word for t blocks followed by the index of the last block, the first t factors read only
the first part and the last
factor reads only the second, so the sum splits into a product of two sums. 

 ### Words 

### `sum_words_add`

 A sum over the words of m + n bits is a double sum: a word of m bits followed by a word of n
bits. 

### `blkAt_append_left`

 The three bits from position j on of u ++ v are those of u, if they lie inside u. 

### `blkAt_append_right`

 The three bits from position |u| + j on of u ++ v are those of v from position j on. 

### `sum_words_three`

 A sum over the words of 3 bits is a sum over the blocks. 

### `sum_words_six`

 A sum over the words of 6 bits is a sum over the pairs of blocks. 

 ### The length of θ' 

### `off_eq_lenW`

 The index of the block number s begins where the indices of the s earlier blocks end. 

### `lenW_succ`

 One more block makes θ' longer by 6 bits if the block is wide, by 3 bits if not. 

### `lenW_mono`

 The length of θ' grows with the number of blocks. 

 ### What a factor reads 

### `topAt_append_left`

 The factor of the block number s < t in the first function reads only the part of θ' that
belongs to the first t blocks. 

### `botAt_append_left`

 The same for the second function. 

 ### One block 

### `sum_last`

 A block that is not wide: Σ_k ψ_k(a,b)·ψ_k(b',a') = R(a,b,a',b'), the definition of R. A wide
block: Σ_{k,k'} [(a,b) = (k,k')]·R(k,a',k',b') = R(a,a',b,b'), the factorization through all 6 bits
of (a,b). Here u is the part
of θ' before the index of the block number t. 

 ### All blocks 

### `stChunk`

 «This product has a row-wise factorization (f_Q, f'_Q) through 3(t − i) + 6i bits, whose index
θ' lists the indices of the blocks s = 1, …, t in this order». The paper states this row-wise and
obtains it from
observation (a) after Definition 1; here it is proved for both directions, and the induction behind
that observation is written out. 
