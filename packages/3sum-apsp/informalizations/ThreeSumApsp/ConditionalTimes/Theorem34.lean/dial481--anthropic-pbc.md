---
{
  "module": "ThreeSumApsp/ConditionalTimes/Theorem34.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/ConditionalTimes/Theorem34.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/ConditionalTimes/Theorem34.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 34 from Theorems 22 and 33

Write `m = ⌈n^μ⌉`. The (min,+)-product of an `n × m` matrix by an `m × n` matrix is cut into
`⌈n/m⌉²` products of `m × m` matrices, at a cost of `O(m² (1 + log u))` each for the copying (the
claim `hcut`), and Theorem 22 computes each of them.

1. The entries are at most `n^{1-μ} (log n + 1)^e ≤ n ≤ m²` (`eventually_entries_le`,
   `natCast_le_thinDim_rpow_two`; the second is where `μ ≥ 1/2` is used). Theorem 22 is stated for
   the bound `m^κ` on the entries (`κ` is the paper's ν); we take `κ = 2`, and `hrelax` lets the
   algorithm run on smaller entries.
2. There are at most `(2n/m)²` products (`natCeil_div_le_two_mul`), and `1 + log u ≤ 2 log n`
   (`one_add_logU_le`).
3. The total is `Õ(n^{2-2μ} m^{3-δ}) = Õ(n^{2+μ-μδ})`, where `3 - δ` is the exponent of Theorem 22
   (`isPowPolylog_total`).

This gives `rectMinPlus_of_minPlusInPolylog`. With `δ = ε'/3` the bound is `O(n^{2+μ-ε₁})` for
`ε₁ = με'/6`, so Theorem 33 applies (`conditional_theorem_34`).


### `one_le_thinDim`

 `1 ≤ ⌈n^μ⌉` for `n ≥ 1`. 

### `thinDim_le_self`

 `⌈n^μ⌉ ≤ n` for `μ ≤ 1` and `n ≥ 1`. 

### `natCast_le_thinDim_rpow_two`

 `n ≤ m²` for `m = ⌈n^μ⌉` and `μ ≥ 1/2`. 

### `eventually_entries_le`

 The bound `n^{1-μ} (log n + 1)^e` on the entries is at most `n` for large `n`, for `μ > 0`. 

### `one_add_logU_le`

 `1 + logU u ≤ 2 log n` for `u ≤ n` and `n ≥ 3`. 

### `natCeil_div_le_two_mul`

 `⌈n/m⌉ ≤ 2 n/m` for `1 ≤ m ≤ n`. 

### `isPowPolylog_total`

 Step 3: `(2n/m)² (G(m) + c m² · 2 log n) = Õ(n^{2+μ-μδ})` if `G(s) = Õ(s^{3-δ})`, where
`m = ⌈n^μ⌉`, `μ > 0` and `δ ≤ 1`. 

### `rectMinPlus_of_minPlusInPolylog`

 The first half of the proof of Theorem 34: if the (min,+)-product of square
matrices is computed in `Õ(n^{3-δ})` time (`h22`; Theorem 22 has `δ = ε'/3`), then the product of an
`n × n^μ` matrix by an `n^μ × n` matrix with entries up to `n^{1-μ} (log n + 1)^e` is computed in
`Õ(n^{2+μ-μδ})` time: "Theorem 22 computes each of them in Õ((n^μ)^{3-ε'/3}) time, and all of them
in Õ(n^{2+μ-με'/3}) time". `μ ≤ 1` is used for the number of blocks. 

### `conditional_theorem_34`

 The deduction of **Theorem 34** from Theorems 22 and 33: "Theorem 22 computes each of them in
Õ((n^μ)^{3-ε'/3}) time, and all of them in Õ(n^{2+μ-με'/3}) time. This is O(n^{2+μ-ε₁}) for any
constant ε₁ < με'/3, so [CVX21, Theorem 3.1] applies, in the deterministic form of Theorem 33, since
the algorithm of Theorem 22 is deterministic." Here `ε' = 0.00175` (Theorem 19). `μ` is a real
parameter; 1/2 ≤ μ ≤ 1 holds for the paper's μ (Section 5.1). The conclusion `Claim.Theorem_34 M μ`
is literally the conclusion of `h33`. So what this theorem checks is that the premise of Theorem 33
holds for some ε₁ > 0.

The entries: the paper's proof bounds them by "Õ(n^{1-μ}) ≤ Õ(n^μ), because μ ≥ 1/2", and Theorem
22, applied to matrices of size n^μ, allows entries up to (n^μ)^ν for every constant ν. Here
n^{1-μ}(log n + 1)^e ≤ n ≤ (n^μ)² for large n, which is the case `κ = 2` of `h22` (`κ` is the
paper's ν), used through `hrelax`. So μ ≥ 1/2 is used only for n ≤ (n^μ)²; with a larger exponent,
any μ > 0 would do. 
