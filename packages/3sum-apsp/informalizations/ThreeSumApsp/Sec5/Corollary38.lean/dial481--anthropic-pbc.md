---
{
  "module": "ThreeSumApsp/Sec5/Corollary38.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Corollary38.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Corollary38.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 38

For `d ≤ n^{1/40}` and large `n`, comparison counts are computed in
`O(|P| n^{0.0229} + n²/d^{0.126} + n^{2-1/440} log n)` time.  The algorithm applies Lemma 37 with
`s := ⌈n^{1-1/440}/d⌉` (`blockLen`), pads the product to the inner dimension
`D* := ⌈3d²n^{1/440}⌉` (`Dstar`), and applies Corollary 26 with `N := n` and `D := D*`.

Running times are not defined here.  This file proves that the algorithm is correct and that
Corollary 26 applies (`corollary_38_correct`), and that the times of Corollary 26 and Lemma 37 add
up to the bound (`corollary_38_bound`).  Both rest on the inequalities of the paper's proof.  Each
of them is a lemma, in the paper's order:
* `D'' ≤ 3d²n^{1/440}`, so the product can be padded (`D''_le`, `D''_le_Dstar`);
* `D* ≤ 4n^{23/440}`, so `(D*)^18 ≤ n` (`Dstar_le`, `Dstar_pow_le`);
* `(D*)^{0.437} = O(n^{0.0229})` and `(D*)^{0.063} ≥ d^{0.126}` (`Dstar_rpow_le`,
  `rpow_le_Dstar_rpow`);
* `nD* = O(n^{1.06})`, `nds ≤ 2n^{2-1/440}`, `ds² ≤ 4n^{2-1/440}` (`mul_Dstar_le`,
  `mul_mul_blockLen_le`, `mul_blockLen_sq_le`).


### `Regime`

 The hypotheses of Corollary 38: "Let d ≤ n^{1/40}, and let n be larger than a suitable
constant."  The first four fields are what the proof needs of the size of `n`; they make the
constant large, more than `2^610`. 

### `Regime.one_le_n`

 There is at least one list. 

### `Regime.two_le_rpow`

 The step `2d²n^{1/440} + d + 1 ≤ 3d²n^{1/440}` needs this at `d = 1`. 

### `Regime.four_pow_le_rpow`

 This is equivalent to the step `4^18 n^{0.941} ≤ n`. 

### `Regime.one_le_log`

 This gives `n^{1.06} = O(n^{2-1/440} log n)`. 

### `Regime.one_le_d`

 The standing assumption of Section 5.2: "Throughout, d ∈ [n] is a parameter". 

### `Regime.d_le`

 The hypothesis of the corollary: "Let d ≤ n^{1/40}". 

### `exists_regime`

 There is a suitable constant. 

### `one_le_blockLen`

 `s = ⌈n^{1-1/440}/d⌉ ≥ 1`, the hypothesis of Lemma 37. 

### `le_mul_blockLen`

 `ds ≥ n^{1-1/440}`, since `s = ⌈n^{1-1/440}/d⌉`. 

### `mul_blockLen_le`

 `ds ≤ n^{1-1/440} + d ≤ 2n^{1-1/440}`, since `s = ⌈n^{1-1/440}/d⌉`. 

### `D''_le`

 "so that D'' ≤ 2d²n^{1/440} + d + 1 ≤ 3d²n^{1/440}". 

### `D''_le_Dstar`

 `D'' ≤ D*`: the product of Lemma 37 can be padded to the inner dimension `D*`. 

### `Dstar_le`

 "Since d ≤ n^{1/40}, we have D* ≤ 4n^{23/440}". 

### `Dstar_pow_le`

 "so (D*)^18 ≤ 4^18 n^{0.941} ≤ n", the hypothesis `N ≥ D^18` of Corollary 26. 

### `Dstar_rpow_le`

 "Here (D*)^{0.437} ≤ 4^{0.437} n^{0.437·23/440} = O(n^{0.0229})", with the constant 4. 

### `rpow_le_Dstar_rpow`

 "and (D*)^{0.063} ≥ (3d²)^{0.063} ≥ d^{0.126}". 

### `mul_Dstar_le`

 "nD* = O(n^{1.06})". 

### `self_mul_rpow`

 `n · n^{1-1/440} = n^{2-1/440}`. 

### `mul_mul_blockLen_le`

 "nds ≤ 2n^{2-1/440}". 

### `mul_blockLen_sq_le`

 "ds² ≤ 4n^{2-1/440}": `s ≤ ds ≤ 2n^{1-1/440}`, and `n^{1-1/440} ≤ n`. 

### `corollary_38_bound`

 Proof of Corollary 38: "Corollary 26 ... computes (XY)[r,c] for all (r,c) ∈ P
deterministically in O(|P|(D*)^{0.437} + n²/(D*)^{0.063}) time" and "the time of Lemma 37 itself is
O(nD* + (|P| + nds + ds²) log n) = O(|P| n^{0.0229} + n^{2-1/440} log n)"; together these are at
most a constant times the bound |P| n^{0.0229} + n²/d^{0.126} + n^{2-1/440} log n of the corollary.
`p` is |P|.  The hypothesis 1 ≤ d is the standing assumption of Section 5.2: "Throughout, d ∈ [n] is
a parameter".

NOTE. The time of Lemma 37 is taken as in the library's `Claim.Lemma_37`, so that this is the
arithmetic of `conditional_corollary_38`: it has `log n + 1` in place of `log n`, which makes the
statement stronger. 

### `corollary_38_correct`

 Corollary 38, the part that is not a running time: the counts γ(r,c), (r,c) ∈ P, "with < or with
≤", are the wanted entries of a product with inner dimension D*, which satisfies the hypotheses of
Corollary 26 with N = n (second to fourth conjunct: (D*)^18 ≤ n, and entries of absolute value at
most n), plus the integers γ₂(r,c) of Lemma 37. The first conjunct, D'' ≤ D* (proof of Corollary 38:
"D'' ≤ 2d²n^{1/440} + d + 1 ≤ 3d²n^{1/440}"), says that "pad the product to the inner dimension D*"
only adds zero columns and zero rows: `padInnerCols` and `padInnerRows` would cut off a larger
matrix. `n₀` is the "suitable constant" of the corollary.  The hypothesis 1 ≤ d is the standing
assumption of Section 5.2: "Throughout, d ∈ [n] is a parameter". 
