---
{
  "module": "ThreeSumApsp/Sec3/Theorem19.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem19.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem19.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 19 and Remark 20: Exact Triangle in truly subcubic time (Section 3.3)

Theorem 19 applies the reduction of Theorem 17 with `D` about `n^{1/18}` and `g = ⌈D^η⌉`, and solves
each instance by a corollary of Section 3.1: by Corollary 15 with `η = 1/36`, where `D` is the
largest power of four with `D ≤ n^{1/18}`, and by Corollary 16 with `η = 0.0315`, where
`D = ⌊n^{1/18}⌋`.  This file has the arithmetic of the proof.  The deduction of the running time
from Theorem 17 that uses it is `Theorem19.explicit_of_theorem_17_corollary_15` and
`Theorem19.explicit_of_theorem_17_corollary_16`, and the theorem about programs is
`wordRam_theorem_19`.

1. Both choices of the parameters, `paramD₅` with `paramG₅` and `paramD₂₆` with `paramG₂₆`, are a
   `Theorem19.Choice` (`Theorem19.choice_theorem_5`, `Theorem19.choice_corollary_26`).  So they
   satisfy the hypotheses of Theorem 17 and of the two corollaries (`Choice.sixteen_le`,
   `Choice.le_n`, `Choice.one_le_ceil`, `Choice.ceil_le_sqrt`, `Choice.pow_eighteen_le`).
2. By the cost analysis for a general choice (`Theorem19.exists_total_le`), the number of instances
   times the cost of one instance, plus the additional time of Theorem 17, is
   `O(n^{3-1/648} log² n)`, respectively `O(n^{3-0.00175} log n)` (`Theorem19.total_theorem_5`,
   `Theorem19.total_corollary_26`).  The step "O(n^{3−ε'} log n) ≤ O(n^{3−ε_T})" of the
   statement is the general fact that a larger exponent absorbs logarithms
   (`IsPowPolylog.isBigOPow`); it is applied in `Theorem19.second_of_explicit`.

NOTE.  "Assume n is larger than a constant depending on ν": the two choices of `D` below are stated
for `n ≥ 16^18`, which makes `D ≥ 16`.

Remark 20 explains the values of `η`: the exponents `η - γ` of the instances and `-η` of the scans
balance at `η = γ/2` (`remark_20_balance`, `remark_20_numbers`), and the straightforward algorithm
for the instances gives back the bound `n³` (`remark_20_brute_force`).


 ### The two choices of the parameters 

### `paramD₅_largest_pow_four`

 `paramD₅ n` is what the proof of Theorem 19 asks for: "the largest power of four with
D ≤ n^{1/18}". 

### `Theorem19.Choice.of_largest_pow_four`

 The largest power of four with `D ≤ n^{1/18}` is at least 16 and at least `n^{1/18}/4`. 

### `Theorem19.choice_theorem_5`

 Proof of Theorem 19, by Theorem 5: "Let D be the largest power of four with D ≤
n^{1/18}, so that D ≥ n^{1/18}/4, and let g := ⌈D^{1/36}⌉." 

### `Theorem19.choice_corollary_26`

 Proof of Theorem 19, by Corollary 26: "Let D := ⌊n^{1/18}⌋ and g := ⌈D^{0.0315}⌉", and
"D ≥ n^{1/18}/2". 

 ### The costs added up 

### `Theorem19.total_theorem_5`

 **Theorem 19, first bound**, the costs added up: "so the time is
O(n^{3−1/648} log² n)".  The left side is the bound of Theorem 17 at `D = paramD₅ n` and
`g = paramG₅ n`: the number of instances times the bound of Corollary 15 for one instance, plus the
three terms of the additional time (with Strassen's exponent).  `a` and `b` stand for the constants
hidden in the two `O(·)`, and `κ` is the exponent in the bound on the weights, the paper's ν. 

### `Theorem19.total_corollary_26`

 **Theorem 19, second bound**, the costs added up: "so the time is O(n^{3−ε'} log n)",
`ε' = 0.00175`.  The letters are as in `Theorem19.total_theorem_5`, with Corollary 16 in place of
Corollary 15. 

 ### Remark 20 

### `remark_20_balance`

 **Remark 20**: "With g = D^η and a saving D^γ per instance, the instances cost n³
D^{η−γ} and the scans n³ D^{−η} [...].  They balance at η = γ/2": the larger of the two exponents
`η − γ` and `−η` is smallest, namely `−γ/2`, exactly at `η = γ/2`. 

### `remark_20_numbers`

 **Remark 20**: "that is, at η = 1/36 for the saving D^{1/18} of Theorem 5 and at η =
0.0315 for the saving D^{0.063} of Corollary 26 [...] the final exponent η/18". 

### `remark_20_brute_force`

 **Remark 20**: "With the straightforward algorithm (O(n²/g) per instance, since every
vertex of A has O(√D/g) neighbors in the middle part) the reduction recovers the brute-force bound
n³": `n²/√D` query pairs times `⌈s/g⌉` neighbors is at most `2n²/g`, and `4ng` instances at `2n²/g`
each come to `8n³`.  (That a vertex of `A` has at most `⌈s/g⌉` neighbors in the middle part is the
library's lemma `TriangleInstance.ncard_nbr_lopInstance_le`.)  The paper adds "up to a logarithmic
factor".  The cost of the instances has no such factor; the term ν n³ log n/g of Theorem 17, for the
scans, has one.  Only the cost of the instances is treated here. 
