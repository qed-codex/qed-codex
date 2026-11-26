---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/WordSize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/WordSize.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/WordSize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 30 in the light language: limits that are polynomial in N

"Word size", proof of Theorem 30.  For every exponent c of the bound N^c on the entries there are
limits (`lim30`) that the two routines preCore and queryAt can live with (`lim30_ok`) and that are
at most 2^9 ((N + 1) (D + 1))^(20 + 2c) (`small_lim30`).  The exponents are generous: since (10^L)²
≤ N^5, every quantity that depends on L is at most B = (N + 1)^5 (`below`), the block has at most
222 B⁴ cells (`top_sub_le_pow`), and the word bound `word30` is a sum of seven terms, each at most a
small multiple of (N + 1)^(20 + 2c) (`word30_le`).  What the two routines ask of the limits is
`Lim30`, in their specifications.  The polynomial bound is for a block whose base address b0 is at
most 10 (N + 1)³; the end theorems, which put the block behind the input, show this of their b0
(`b0_le`, `wantedB0_le`, `blockAt_le`).


### `card_boxes_le`

 There are at most `11^L` cubes. 

### `numBands_le`

 The number of bands is at most `N + 1`. 

### `N0_le_N`

 `N₀ ≤ N` under the hypotheses of Theorem 30. 

### `Hyp30.D_le_N`

 `D = 4^m ≤ N₀ = 3^{L-m} ≤ N`, since `L ≥ 10 m`. 

### `Below`

 Everything that depends on `L` is at most `B`; see `below` for `B = (N + 1)^5`. 

### `below`

 "Since N ≥ N₀ = 3^{L-m} and L ≥ 10m, we have 10^L ≤ N^{5/2}": so all these quantities are at
most `(10^L)² ≤ N^5`. 

### `top_sub_le_pow`

 The length of the block is at most `222 B⁴`. 

### `word30`

 The word bound: the sum of everything that has to fit in a word. 

### `word30_parts`

 Each summand is below the word bound. 

### `lim30`

 The limits of Theorem 30. 

### `lim30_ok`

 The two routines can live with these limits. 

### `cast_le_word30`

 A number that is at most the base address of the block, or at most `L`, fits in a word. 

### `pow_le_word30`

 The bound `N^c` on the entries fits in a word. 

### `abs_params_le_word30`

 The parameters `m`, `L`, `t`, which stand in the input, fit in a word. 

### `word30_le`

 The word bound is polynomial in `N`. 

### `small_lim30`

 **The limits of Theorem 30 are polynomial in `N`.** 
