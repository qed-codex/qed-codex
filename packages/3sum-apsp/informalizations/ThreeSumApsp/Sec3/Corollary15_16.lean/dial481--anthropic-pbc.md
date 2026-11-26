---
{
  "module": "ThreeSumApsp/Sec3/Corollary15_16.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Corollary15_16.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Corollary15_16.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollaries 15 and 16: the number of pieces, and the bound for few query pairs

The theorems about programs are `wordRam_corollary_15` and `wordRam_corollary_16`.  This file has
two computations from the text around the corollaries.

* **Corollary 15.**  Its pieces are the chunks of `W` with `cap = ⌊n²/√D⌋`.  There are at most
  `⌈|W|√D/n²⌉ + 1` of them (`Corollary15.split`).  The program cuts `W` into pieces of
  `splitCap n D = max(1, ⌊n²/√D⌋)` pairs, and there are at most `2(n² + |W|√D)/n²` of these
  (`ceil_div_splitCap_le`, which the running-time claim uses).  So `n²` operations for each piece
  are `O(n² + |W|√D)` in all (`Corollary15.pieces_cost`).  Nothing else rests on
  `Corollary15.split` and `Corollary15.pieces_cost`.
* **After Corollary 16.**  For `|W| = O(n²/√D)` its bound is `O(n²/D^{0.063})`
  (`Corollary16.bound_le_of_card_le`; nothing else rests on it).


 ### Corollary 15 

### `le_of_pow_eighteen_le`

 `D ≤ D^18 ≤ n`. 

### `sqrt_add_one_le_div`

 Under the hypotheses of Corollary 15, `√D + 1 ≤ n²/√D`, because `(√D + 1)√D ≤ 2D ≤ D² ≤ n²`. 

### `card_div_queryCap_le`

 The inequality behind the number of pieces in Corollary 15: `|W|/⌊r⌋ ≤ |W|/r + 1` for
`r = n²/√D`.  It holds because `y = |W|/r` is at most `√D ≤ r − 1`, so that
`|W| = y r ≤ (y + 1)(r − 1) ≤ (y + 1)⌊r⌋`. 

### `Corollary15.split`

 **Corollary 15**, proof: "apply the theorem to each of at most ⌈|W|√D/n²⌉ + 1 pieces".  (That
`D` is a power of four is needed to apply Theorem 5, not to count the pieces.) 

### `sq_div_sqrt_le_two_mul_splitCap`

 A piece has at least half of `n² / √D` query pairs. 

### `ceil_div_splitCap_le`

 The number of pieces: `⌈w / cap⌉ ≤ 2 (n² + w √D) / n²`. 

### `Corollary15.pieces_cost`

 **Corollary 15**, the arithmetic behind "solves it deterministically in time O((n² + |W|√D) log²
D / D^{1/18})": the number of pieces times `n²` is at most `2(n² + |W|√D)`. 

 ### After Corollary 16 

### `Corollary16.bound_le_of_card_le`

 After **Corollary 16**: "For |W| = O(n²/√D), which is what the reductions below produce, the
running time in Corollary 16 is O(n²/D^{0.063})."

NOTE.  Corollary 16 states no lower bound on `D`; this computation is stated for `D ≥ 1`. 
