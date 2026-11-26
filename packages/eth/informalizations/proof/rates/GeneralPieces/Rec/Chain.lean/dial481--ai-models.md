---
{
  "module": "proof/rates/GeneralPieces/Rec/Chain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Rec/Chain.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Rec/Chain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The schedule (40) is a chain of steps that are in order, through case (ii)

This follows the step from ℓ to ℓ+1 in the proof of part (b) of the theorem on the general recursion
(Appendix A), from the display for U = min(U_row, U_col) to the display for K²L, sentence by
sentence; most
theorems quote their sentence. Throughout K, g, ζ are K_ℓ, g_ℓ, ζ_ℓ and N = g⁴λ. The end is
`stChain2`: for pieces with parameters (ρ, c) whose numbers of bits are at most 2λ, and every x₀ ≥
18,
every step g_ℓ·g_ℓ → K_ℓ of the schedule satisfies `LevelOK2` at every label length λ ≥ 1.
Differences from the paper: the program uses one label length for all patterns ι of a level,
computed from an upper bound `ubarG` for U = min(U_row, U_col), where the paper's L depends
on ι; it is ⌊·⌋ + 1 where the paper has ⌈·⌉. The hypothesis 2^x₀ ≥ c + 5 of the theorem is not used
in this file. 

 ### The display for U = min(U_row, U_col) 

### `total_eq_min`

 The network that the program takes on a square grid is "the network with the smaller total": its
total is min(U_row, U_col). 

### `ubar_eq`

 The program's upper bound for U at level ℓ, written out: g(g−1)·gλ + |R|·max_i (c_i^row +
c_i^col). 

### `U_le_ubar`

 U = min(U_row, U_col) is at most the program's upper bound: the minimum is at most the average. 

### `ubar_le_first`

 First inequality of the display, "U ≤ N/g + |R|(4ρλ + c log(2λ))", for the program's upper
bound. 

### `ubar_le_second`

 Second inequality of the display, "N/g + |R|(4ρλ + c log(2λ)) ≤ N(ρ + 1/g) + (c/4)g⁴ log(2λ)":
there are at most g⁴/4 rectangles. 

 ### "Case (ii) of the lemma applies to the network with the smaller total" 

### `K_dvd_g`

 "K divides g". 

### `two_zeta_sq_g`

 "2ζ²g = 2^{ℓ+x₀−9}K". 

### `two_gK_le`

 "2gK ≤ g² = K_{ℓ+1}". 

### `log_two_gK_le`

 "ln(2gK) ≤ 0.7 log K_{ℓ+1}". 

### `logK_succ_le`

 "0.7 log K_{ℓ+1} ≤ 1.4 (3x₀+6) 2^ℓ". 

### `num_le`

 "1.4 (3x₀+6) ≤ 2^{x₀−9} for x₀ ≥ 18". 

### `hoeffding_cond`

 The condition 2ζ²g ≥ K·ln(2gK) of case (ii) holds at every level, by the four sentences above. 

### `zeta_mul_g`

 "ζg = 2^{2ℓ+x₀−5}K". 

### `inv_g_le_zeta`

 "Also 1/g ≤ ζ". 

### `zetaOf_step`

 ζ of the step at level ℓ is ζ_ℓ = 2^{−ℓ−5}. 

 ### The display for K²L 

### `K_sq_L_le_first`

 First inequality of the display, "K²L ≤ U + 2ζN + K²", for the program's label length one level
down and its upper bound for U. 

### `K_sq_L_le`

 The display "K²L ≤ U + 2ζN + K² ≤ (ρ + 3ζ)N + (c/4)g⁴ log(2λ) + K²". 

 ### The schedule 

### `levelOK2`

 Every step of the schedule is in order at every label length. 

### `stChain2`

 `StChain2`: the schedule (40) is a chain of steps g_ℓ·g_ℓ → K_ℓ that ends at K₀ nodes, and every
step is in order at its label length. 
