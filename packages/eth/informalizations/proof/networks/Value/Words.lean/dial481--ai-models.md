---
{
  "module": "proof/networks/Value/Words.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Value/Words.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Value/Words.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «Exactly one»: general facts behind the changes of variables

The sentences «the two copies on every edge agree … one string in {0,1}^λ per edge» (after
Definition 3) and «one string θ_{a,b} ∈ {0,1}^{c_{a,b}} per pair {a,b} of nodes in different groups»
(proof of Lemma 1) are changes of the variable of a sum. The statements `StOneStringPerEdge` and
`StBlocks` say them as «exactly one». This file has what both proofs share:
* `existsUnique_pi`: exactly one choice at every index gives exactly one family;
* `existsUnique_tuple`: exactly one tuple has given entries;
* `existsUnique_of_sum`: if a map i carries all sums over T back to sums over s, then every property
  that exactly one element of T has is had by i(a) for exactly one a in s (take the indicator of the
  property as the summand);
* `getD_chunks_map`: where the block of an index begins when a string is cut into blocks of given
  lengths;
* `star_swap`: the string on an edge is the same seen from either end. 

### `existsUnique_pi`

 If at every index exactly one x is right, then exactly one family is right at every index. 

### `existsUnique_tuple`

 Exactly one tuple has the entries t i at the indices i with P i. 

### `existsUnique_of_sum`

 If Σ_{a ∈ s} F(i a) = Σ_{b ∈ T} F(b) for all F, and exactly one b ∈ T has the property Q, then
exactly one a ∈ s is such that i a has the property Q. (With F the indicator of Q both sums count.) 

### `getD_chunks_map`

 A string w is cut into blocks of the lengths f j, j in the list e. The block of the index i
begins after the blocks of the indices before i, and has f i positions. 

### `star_swap`

 The string of Λ on the edge {w, w'} is the same seen from w and from w'. 
