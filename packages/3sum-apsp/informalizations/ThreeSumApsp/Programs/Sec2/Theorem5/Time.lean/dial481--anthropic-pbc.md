---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Time.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Time.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Time.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 5 in the light language: the running time, added up

Pure mathematics: no program occurs here.  thm5Shape p w work is the shape of the running time of
the program for Theorem 5.  For the parameters of Section 2.4.4, L = 19 m, and under the hypotheses
of Theorem 5, N ≥ D^18 and at most N²/√D wanted positions, it is at most a numeral times L
N² / D^{1/18} (thm5Shape_le), which is below the bound O(N² log² D / D^{1/18}) of the theorem
(thm5Shape_le_of_wanted).

The proof follows "The cost" in Section 2.4.4.  The shape is a polynomial in the sizes
(thm5Shape_eq), each term of which is a basic quantity times at most L + 1 (shapeOf_le).  The basic
quantities are at most a numeral times X = N² / D^{1/18}: the subsets, tiles and wanted positions
(minutiae_le), the encodings (encodings_le), the entries of the input arrays (bandArrays_le), the
leaves that the pruned recursions visit (work5_le), and N itself (le_rate).


### `work5`

 The work of the pruned recursions of all tiles, for a set W of wanted positions. 

### `rate_eq`

 D^{-1/18} N² is N² / D^{1/18}. 

### `work5_le`

 Section 2.4.4: the work of the pruned recursions is at most 66 (L + 1) N² / D^{1/18}: it is at
most 2 (L + 1) for each leaf that contributes to a wanted entry, and there are at most 33 N² /
D^{1/18} such leaves. 

### `shapeOf`

 The shape as a polynomial in the sizes: lo stands for L - m, d for D, n0 for N₀, k0 for
K₀ = ⌊√K⌋, and nB for the number of bands. 

### `thm5Shape_eq`

 The shape for the parameters of Theorem 5, as this polynomial. 

### `ShapeBounds`

 Each basic quantity of the shape is at most a numeral times X, which stands for
N² / D^{1/18}; the work of the pruned recursions is at most a numeral times (L + 1) X. 

### `shapeOf_le`

 The polynomial, bounded term by term: every term is one of the basic quantities, or one of them
times L + 1 = 19 m + 1, m + 1 or 18 m + 1. 

### `levels_le_pow`

 19 m + 1 ≤ D^18. 

### `levels_le_log`

 19 m + 1 ≤ 20 log D for m ≥ 1, since log D = m log 4 and log 4 ≥ 1. 

 ## The clauses of Section 2.4.4, in terms of X = N² / D^{1/18} 

### `one_le_D`

 D ≥ 1. 

### `D_rpow_le`

 D^{1/18} ≤ D. 

### `le_rate`

 N ≤ N² / D^{1/18}, because D^{1/18} ≤ D ≤ N. 

### `minutiae_le`

 "O(L) operations per subset, per tile, and per position of W": there are at most
18 N² / D^{1/18} of these objects, for any number w ≤ N²/√D of wanted positions. 

### `encodings_le`

 "the encodings cost […] O(2^{-m/9} N²) operations": the encodings of all row bands have at most
2 N² / D^{1/18} entries. 

### `bandArrays_le`

 The entries written into the input arrays of all the bands together:
n_B K₀² N₀ D = (padded N) · K₀ D ≤ 2N · N / D^{1/18}, because K₀ D² ≤ K N₀ ≤ N. 

### `thm5Shape_le`

 **The shape of the running time is O(L N² / D^{1/18})**, in terms of numbers: w ≤ N²/√D wanted
positions, and work within the bound of work5_le. 

### `thm5Shape_le_log`

 **The shape of the running time is O(N² log D / D^{1/18})**, for a set W of wanted positions. 

### `thm5Shape_le_of_wanted`

 **The shape of the running time is within the bound of Theorem 5**, for a set W of wanted
positions. 
