---
{
  "module": "proof/rates/GeneralPieces/Ring/Bits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Bits.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Bits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The numbers in the proof of the theorem on the pieces with ρ = 1/√2: numbers of bits

The paragraph "Numbers of bits" of that proof in Appendix B, and the sentence on log Δ of the next
paragraph, sentence by sentence. Here h is the least integer ≥ 2 with p(h) ≥ 2^λ, and κ = π√(2/3)/ln 2.
Display (46) of the appendix is the hypothesis `Partitions.Bounds B C`: κ√E − B·log E − C ≤ log p(E)
for E ≥ 1 and log p(E) ≤ κ√E + C. The appendix has B = 1, from the formula of Hardy and Ramanujan;
So where the appendix has log h, there is B·log h here; at B = 1 the statements are those of the
appendix. One may take B ≥ 0 (`bounds_abs`).
Every statement is proved from those before it, in the order of the appendix: p(h−1) < 2^λ
(`p_pred_lt`); κ√(h−1) < λ + B·log h + C for B ≥ 0 (`kappa_sqrt_pred_lt`); h = O(λ²)
(`exists_hOf_le`); κ√h ≤ κ√(h−1) + κ (`kappa_sqrt_le_pred`) ≤ λ + O(log 2λ)
(`exists_kappa_sqrt_le`);
R^row_s ≤ (2h+1)·p(2h+s) and R^col_s ≤ (2h+1)·p(2h−s) (`Rrow_le`, `Rcol_le`); √(2h+s) + √(2h−s) ≤
2√(2h) (`sqrt_add_sqrt_le`); the display
c^row_s + c^col_s ≤ 2√2·κ√h + 2·log(2h+1) + 2C + 2 (`bits_le`) ≤ 2√2·λ + O(log 2λ)
(`exists_bits_le`); log Δ ≤ 2κ√h + log(4h+1) + C (`logb_Delta_le`) = O(λ) (`exists_Delta_le`). 

### `p_pred_lt`

 p(h−1) < 2^λ: by the choice of h if h > 2, and because p(1) = 1 if h = 2. 

### `bounds_abs`

 Display (46) with B holds with |B| as well, because log E ≥ 0 for E ≥ 1. 

### `kappa_sqrt_pred_lt`

 By display (46), for B ≥ 0: κ√(h−1) < λ + B·log h + C. 

### `exists_hOf_le`

 Hence h = O(λ²): log h grows more slowly than √(h−1). 

### `kappa_sqrt_le_pred`

 κ√h ≤ κ√(h−1) + κ, for h ≥ 1. 

### `exists_kappa_sqrt_le`

 And then κ√h ≤ κ√(h−1) + κ ≤ λ + O(log 2λ); on the way, log h = O(log 2λ). 

### `pZ_mono`

 p is nondecreasing, also on the integers. 

### `Rrow_le`

 As p is nondecreasing, R^row_s ≤ (2h+1)·p(2h+s). 

### `Rcol_le`

 As p is nondecreasing, R^col_s ≤ (2h+1)·p(2h−s). 

### `sqrt_add_sqrt_le`

 √(2h+s) + √(2h−s) ≤ 2√(2h), for |s| ≤ 2h. 

### `logb_le_of_le_mul_p`

 By display (46): if 1 ≤ r ≤ k·p(a), then log r ≤ log k + κ√a + C. 

### `bits_le`

 The display, first inequality: c^row_s + c^col_s ≤ 2√2·κ√h + 2·log(2h+1) + 2C + 2, for |s| ≤ 2h. 

### `exists_display_le`

 The display, second inequality: 2√2·κ√h + 2·log(2h+1) + 2C + 2 ≤ 2√2·λ + O(log 2λ). 

### `four_mul_rho`

 4ρ = 2√2 for ρ = 1/√2. 

### `exists_bits_le`

 The display as a whole, in the form of the definition of pieces with ρ = 1/√2: c^row_s + c^col_s
≤ 4ρλ + c·log 2λ. 

### `logb_Delta_le`

 By display (46): log Δ ≤ 2κ√h + log(4h+1) + C. 

### `logb_two_mul_le`

 log(2λ) ≤ λ. 

### `exists_Delta_le`

 So log Δ ≤ 2κ√h + O(log 2λ) = O(λ): Δ ≤ 2^{cλ} for a constant c. 
