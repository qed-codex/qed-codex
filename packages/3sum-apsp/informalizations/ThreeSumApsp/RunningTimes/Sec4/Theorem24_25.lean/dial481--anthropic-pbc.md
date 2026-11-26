---
{
  "module": "ThreeSumApsp/RunningTimes/Sec4/Theorem24_25.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec4/Theorem24_25.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec4/Theorem24_25.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorems 24 and 25 on the word RAM

Theorem 24, as in the paper: for `ε < ε*` and `q > 0` choose `c` and `θ` with `ε < R_c(γ)` and with
the `q` of Corollary 31 below the given one (`exists_admissible`), and apply Corollary 31.
Theorem 25, as in the paper: "Apply Theorem 24 with q := κ/2, and ask one query for each position of
W."  A statement "there are programs" gives no program that another one could call, so the lemma
`Theorem24.with_queries` says two things of one `γ`: there is the data structure of Theorem 24, and
there is a program that computes the entries at every set `W` of positions in
`O(N² log² D/D^γ + |W| D^q log D)` time.  In its proof both come from one choice of `c` and `θ`, and
the program is the one of `Corollary32.from_one`, which preprocesses and asks one query for each
position of `W`.  Theorem 24 is the first half of the lemma.  Theorem 25 is its second half at
`q := κ/2`, with `γ' := min{γ, κ/2}` and the sum of the two times from `Theorem25.time`.
The programs are those of Corollaries 31 and 32; only the bounds are rewritten
(`exists_isDataStructure_of_dominated`, `exists_solves_of_dominated`).


### `Theorem24.with_queries`

 Theorem 24, and what the proof of Theorem 25 does with it: "ask one query for each position of
W".  For `ε < ε*` and `q > 0` there is a `γ > 0` with the data structure of Theorem 24 and with a
program that computes the entries at every set `W` of positions in
`O(N² log² D/D^γ + |W| D^q log D)` time. 

### `wordRam_theorem_24`

 **Theorem 24**, on the word RAM. 

### `wordRam_theorem_25`

 **Theorem 25**, on the word RAM. 
