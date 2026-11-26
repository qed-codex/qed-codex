---
{
  "module": "Zeta23/WeilEF/GoodHeights.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/GoodHeights.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/GoodHeights.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/WeilEF/GoodHeights.lean — good horizontal heights for the EF contour: for every j ≥ 7 a height
R ∈ [j, j+1] avoiding the ordinates of all ζ-zeros near heights ±j by ≥ 1/(2(n+1)) (n ≪ log j of them;
pigeonhole over n+1 cell midpoints), whence on Im s = ±R, 1/2 ≤ Re s ≤ 2:  ζ(s) ≠ 0 and
‖ζ'/ζ(s)‖ ≤ C log²(j+3), by the partial fraction Zeta23.WeilEF.zeta_logDeriv_partial_fraction (with its
multiplicity-sum conjunct) and the proved local zero count Zeta23.RvM.zetaZeroConfig_local_count
(via Zeta23.Tail.LocalCount).  Statement shape (consumed by Contour.lean horizontal_vanish):
j ≥ 7, σ ∈ [1/2, 2], bound in log((j:ℝ)+3).
-/
```

 ### Gap / pigeonhole lemma 

### `exists_far_point`

 For a finite set S of reals and any a, some R ∈ [a, a+1] stays at distance ≥ 1/(2(|S|+1)) from S:
among the |S|+1 equally spaced cell midpoints of [a,a+1], each point of S is δ-close to at most one. 

 ### Elementary facts used below 

### `isNontrivialZero_of_mem_closedBall`

 a zero of ζ in the closed ball of radius r₀ < 2 about 2 + t i is a nontrivial zero. 

### `sum_mult_six_windows`

 a finite set of nontrivial zeros with ordinates in (a, a+6] has total multiplicity
≤ 6 A₀ log(|a|+9) (six unit windows of the local count). 

### `card_le_sum_mult`

 card ≤ total multiplicity (each nontrivial zero has multiplicity ≥ 1). 

 ### good heights 

### `good_heights_at`

 **Good heights**: for every j ≥ 7 there is R ∈ [j, j+1] such that on both horizontal segments
Im s = ±R, 1/2 ≤ Re s ≤ 2, ζ(s) ≠ 0 and ‖ζ'/ζ(s)‖ ≤ C log²(j+3)  (R avoids the ordinates of all
zeros with |Im ρ ∓ R| < 2 by at least 1/(2(n+1)), n ≪ log j their number; then the partial
fraction ζ'/ζ(s) = Σ_{|ρ−(2±iR)| ≤ 1.6} m_ρ/(s−ρ) + O(log) with Σ m_ρ ≪ log). 

### `good_heights`

 **Good heights**, in the consumed shape: a height function `R_j ∈ [j+7, j+8]` (all `j : ℕ`) with
ζ ≠ 0 and `‖ζ'/ζ‖ ≤ C_g log²(j+10)` on both horizontal lines `im = ±R_j`, `1/2 ≤ re ≤ 2`
(`good_heights_at` re-indexed by `j ↦ j + 7` and a choice function). 
