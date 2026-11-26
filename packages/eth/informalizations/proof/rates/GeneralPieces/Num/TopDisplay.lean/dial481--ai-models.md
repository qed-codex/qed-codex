---
{
  "module": "proof/rates/GeneralPieces/Num/TopDisplay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Num/TopDisplay.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Num/TopDisplay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The top level of part (c) of the theorem on the general recursion: the level and the display

The proof of part (c) in Appendix A, sentence by sentence, as far as it is arithmetic: K ≥ m^{1/90}
at the largest ℓ with K_ℓ ≤ m^{1/9};
the display «… ≤ 2ekm + O(km/K + K⁸ log K + K² log(km))»; and «every term after 2ekm is
O(k·m^{1−1/90})».
`top_level` collects the sentences for the schedule of the theorem, and `top_arith` draws from it
the inequality that the top level of this development asks for (the exponent is O(k·m·e_ℓ));
`stTopArith2` is that inequality for a general sequence of levels.

What differs from the text. The cost of the algorithm of this development is the exponent `needTop`
of a pad: the maximum of four budgets (g·(number of bits of K) for the search through the groupings,
P·(2g/K + 1) for a table entry, (K−1)·L for the arguments, and the exponent of the clique
algorithm), not the logarithm of a sum of products. The display is proved for
`needTop` (`needTop_le_display`), and `solver_terms_le` bounds its first two terms. The term
O(log(km)) of the text, which stands for factors polynomial in km, has no counterpart: such factors
are in the
polynomial running time in the length of the pad. L is `lamTopK` = ⌊1 + (2km + gP/K)/K²⌋, the text's
L with the bound 2km in place of U, where the text has U < 2km. The values have
absolute value at most 1 = 2⁰, whereas the text takes B = 1 (values below 2^B), so B' is P·(2g/K). 

 ## The level 

### `m_lt_pow`

 «By (a), K ≥ m^{1/90}»: if K_{ℓ+1} > m^{1/9} then m < K_ℓ^90. 

### `root90_le`

 m^{1/90} ≤ K if m ≤ K^90. 

### `K_ge_root90`

 «By (a), K ≥ m^{1/90}», for the largest ℓ with K_ℓ ≤ m^{1/9}. 

 ## The display 

### `sq_L_le`

 K²·L ≤ K² + 2km + g·P/K: the text's K²·L ≤ U + 2ζgP + K² with ζ = 1/(2K) and U ≤ 2km. 

### `arg_le_km`

 K·(L + B') ≤ 32·km. 

### `nine_le_log`

 log(km) ≥ 9. 

### `solver_terms_le`

 The first two terms of the display: e·K²·L + C₀·K²·log(K(L+B')) ≤ 2ekm + 5·km/K +
(2C₀+1)·K²·log(km), for 0 ≤ e ≤ 1. 

### `needTop_le_display`

 The display for the exponent of the algorithm of this development: at an index i with K⁹ ≤ m, 0
≤ e ≤ 1 and the bound of part (b),
`needTop` ≤ 2ekm + A·(km/K + K⁸·log K + K²·log(km)) with A = 2C₀ + 15. 

 ## Every term after 2ekm is O(k·m^{1−1/90}) 

### `logb_le_two_mul`

 log y ≤ 2y for y ≥ 1. 

### `root_pow`

 (m^{1/(9d)})^{9d} = m. 

### `root_pow_pred`

 m^{1−1/(9d)} = (m^{1/(9d)})^{9d−1}. 

### `root_le`

 m^{1/(9d)} ≤ K if m ≤ K^{9d}. 

### `terms_le_gen`

 «… and every term after 2ekm is O(k·m^{1−1/90})», with any d ≥ 2 in place of 10: if m^{1/(9d)} ≤
K ≤ m^{1/9}, then with t = m^{1/(9d)} one has t ≤ K ≤ t^d, log K ≤ 2dt and
log(km) ≤ 2k + 18dt, so the three terms are at most 1, 2d and 2 + 18d times k·m^{1−1/(9d)}. 

### `terms_le`

 «… and every term after 2ekm is O(k·m^{1−1/90})», for m^{1/90} ≤ K ≤ m^{1/9}. 

### `needTop_le_main_gen`

 The exponent of the algorithm of this development is at most 2ekm + A'·k·m^{1−1/(9d)} with A' =
(3 + 20d)·(2C₀ + 15), at an index with m^{1/(9d)} ≤ K ≤ m^{1/9}. 

### `needTop_le_main`

 The exponent of the algorithm of this development is at most 2ekm + A'·k·m^{1−1/90} with A' =
203·(2C₀ + 15), at an index with m^{1/90} ≤ K ≤ m^{1/9}. 

 ## The exponent is O(k·m·e) 

### `logb_pow_le_real`

 (log t)ⁿ ≤ n!·2ⁿ·t for real t ≥ 1. 

### `one_le_mul_root`

 m^{−1/(9d)} is small against e: if K ≤ t^d and e ≥ (log K)^{−C₀}, then 1 ≤
d^{C₀}·C₀!·2^{C₀}·e·t. 

### `Atop`

 The constant of `needTop_le_kme` and of `top_arith`. 

### `kme_of_main`

 The end of the proof of the first sentence of part (c): an exponent X ≤ 2ekm + A'·k·m^{1−1/(9d)}
is O(k·m·e), because e ≥ (log K)^{−C₀}, K ≤ m^{1/9}, and m^{−1/(9d)} is smaller than any power of
1/log m, up to a
constant. (The text compares both terms with km/(log m)^{α'}; the top level of this development asks
for a multiple of k·m·e.) 

### `needTop_le_kme`

 The same for the exponent of the algorithm of this development, at an index with m^{1/(9d)} ≤ K
≤ m^{1/9}. 

### `stTopArith2`

 Part (c) as an inequality, in the form that the top level of this development asks for
(`ClauseBound.Alg.StTopArith`), proved through the display: with ℓ the level picked for m, the
exponent is at most A·k·m·e_ℓ.
For a general sequence of levels K_{ℓ+1} ≤ K_ℓ^{C₀} takes the place of K_{ℓ+1} ≤ K_ℓ^{10}, so d =
max(C₀, 2) takes the place of 10. 

 ## The top level for the schedule of the theorem 

### `top_level`

 The proof of part (c) up to its display, for the algorithm of this development with the schedule
K_ℓ, e_ℓ and any x₀ ≥ 18. Given parts (a) and (b) in the form of a sequence of indices Q, and m ≥
K₀⁹, let ℓ be
the level that the algorithm picks for m. Then K_ℓ ≤ m^{1/9} < K_{ℓ+1} (it is the largest such ℓ),
K_ℓ ≥ m^{1/90}, the exponent is at most
2·e_ℓ·k·m + A·(km/K_ℓ + K_ℓ⁸·log K_ℓ + K_ℓ²·log(km)), and at most 2·e_ℓ·k·m + 203·A·k·m^{1−1/90},
where A = 2C₀ + 15. 

### `top_arith`

 Part (c) as an inequality for the schedule of the theorem, from `top_level`: with ℓ the level
picked for m ≥ K₀⁹, the exponent, at most 2·e_ℓ·k·m + O(k·m^{1−1/90}), is at most
`Atop C₀ 10`·k·m·e_ℓ. This is what the top level in m is given for the schedule;
`stTopArith2` is the same for a general sequence of levels. 
