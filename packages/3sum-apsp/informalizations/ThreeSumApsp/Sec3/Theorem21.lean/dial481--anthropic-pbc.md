---
{
  "module": "ThreeSumApsp/Sec3/Theorem21.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 21: 3SUM, the (min,+)-product and APSP reduce to Exact Triangle

Theorem 21 collects known reductions; the paper cites them and gives no proof.

Part (a), 3SUM.
* [CH20, Theorem 5.1], from 3SUM to Convolution-3SUM: `theorem_21a_threeSum_to_convolution`.
* [VW13, Theorem 4.3], from Convolution-3SUM to Exact Triangle: `theorem_21a_convolution_to_exact`.
* The arithmetic of composing the two: `n^{1/2+o(1)}` instances, each on `n^{1/2+o(1)}` vertices per
  part, in `n^{3/2+o(1)}` time (`theorem_21a_compose`, in this file).

Part (b), the (min,+)-product and APSP.
* Repeated squaring computes the distances, and the finite entries are bounded:
  `theorem_21b_repeated_squaring`, `theorem_21b_entries_bounded`.
* [VW13, Theorem 3.3], from Negative Triangle to Exact Triangle: `theorem_21b_negative_to_exact`.
* [VW18, Theorem 4.2 and Lemma 4.1] have no statement in this folder; the reductions are written as
  programs, with proofs (`claim_VW18_Theorem_4_2`).
* The logarithmic factors of the two running times (`theorem_21b_log_factors`, in this file).


 ## Part (a): the two reductions composed 

### `theorem_21a_compose`

 For **Theorem 21(a)**: the arithmetic of the composition of the two reductions.  The first
reduction [CH20] takes time `E₁ = Õ(n^{3/2})` and produces `Num₁` arrays, polylogarithmically many,
of length `N = Õ(n)`; the second [VW13], on an array of length `N`, takes time `E₂ = N^{3/2+o(1)}`
and produces `Num₂ = O(√N)` instances with `size₂ = O(√N)` vertices in each part.  Together:
`n^{1/2+o(1)}` instances, each on `n^{1/2+o(1)}` vertices per part, in `n^{3/2+o(1)}` time, as
Theorem 21(a) says.  The six functions are arbitrary, so the statement is arithmetic only; it is not
applied to the bounds of the two reductions.

NOTE.  The hypothesis on `E₂` is what the time `n^{3/2+o(1)}` of Theorem 21(a) asks of the second
reduction. 

 ## Part (b): the logarithmic factors 

### `clog_two_le`

 `⌈log₂ n⌉ ≤ 3 ln n` for `n ≥ 2`, because `⌈log₂ n⌉ < log₂ n + 1 ≤ 2 log₂ n` and `ln 2 > 2/3`. 

### `theorem_21b_log_factors`

 For **Theorem 21(b)**: the logarithmic factors.  Let `τ` be the time of Exact Triangle and `τ'`
that of Negative Triangle, both on `n^{1/3}` vertices per part.  With `τ' = O(τ log U)`, the bound
`O(n² τ' log U)` of [VW18, Theorem 4.2] becomes `O(n² τ log² U)`, and `⌈log₂ n⌉` products with
`U = n^{κ+1}` cost `O(n² τ log³ n)`.  Here `κ` is the paper's ν, and `τ` stands for the `T(n^{1/3})`
of Theorem 21(b); `τ` and `τ'` are arbitrary numbers, so the statement is arithmetic only.

NOTE.
* Both halves are stated for `U = n^{κ+1}`, the first one too.
* The condition that T(s)/s is nondecreasing, and the like condition of [VW18, Theorem 4.2], do not
  occur. 
