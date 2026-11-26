---
{
  "module": "ThreeSumApsp/Sec3/Chunks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Chunks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Chunks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Cutting a set of pairs into chunks

Corollary 15 splits the query pairs "into sets of at most n²/√D query pairs", and the proof of
Theorem 17 cuts each set `W_ϱ` "into chunks of at most n²/√D query pairs".  In both, the chunk
number `j` of `S` holds the pairs of `S` whose rank in row-major order, divided by `cap`, is `j`.

* A chunk has at most `cap` pairs (`card_chunk_le`), because different pairs of `S` have different
  ranks (`rankIn_injOn`).
* The first `⌈|S|/cap⌉` chunks cover `S` (`biUnion_chunk`).
* In both uses `cap = ⌊n²/√D⌋`, which is at least 1 for `1 ≤ D ≤ n` (`one_le_queryCap`).


 ### Ranks 

### `pairIndex_injective`

 The position in row-major order determines the pair. 

### `rankIn_lt_rankIn`

 Among the pairs of `S`, a pair that comes earlier in row-major order has a smaller rank. 

### `rankIn_injOn`

 Different pairs of `S` have different ranks. 

### `rankIn_lt_card`

 The rank of a pair of `S` is less than the number of pairs of `S`. 

 ### Chunks 

### `card_chunk_le`

 A chunk has at most `cap` pairs: their ranks are different numbers in `[j cap, (j + 1) cap)`. 

### `biUnion_chunk`

 The first `⌈|S|/cap⌉` chunks cover `S`, because `|S| ≤ ⌈|S|/cap⌉ cap`. 

 ### The size of the chunks in Corollary 15 and in Theorem 17 

### `sqrt_le_natCast`

 `√D ≤ D ≤ n`. 

### `one_le_queryCap`

 The bound `⌊n²/√D⌋` on the size of a chunk is at least 1, because `√D ≤ n ≤ n²`. 
