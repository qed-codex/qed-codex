---
{
  "module": "ThreeSumApsp/RunningTimes/Sec1/Theorems1_4.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec1/Theorems1_4.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec1/Theorems1_4.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorems 1 to 4 on the word RAM

The theorems of the introduction restate later items.

* Theorem 1: the last sentence of Corollary 26 with `|W| ≤ N²/√D` (`corollary_26_W`), and Theorem
  25 without its logarithms (`dataStructureBelow_wantedBelow_epsStar`), for `ε < 0.1204 < ε*`.
* Theorem 2, the deterministic sentence: the last bound of Theorem 19 and the bounds of Theorem 22
  using Corollary 26, where `2.9995` is above `2.99942` (`SolvedInTime.mono_exponent`).  Its first
  line is printed for `n`-vertex graphs: "an instance on an arbitrary `n`-vertex graph reduces to
  this form by taking three copies of the vertex set" (Section 3.2), which is one more program
  (`Light.Sec3.Theorem2.graphs_of`).
* Theorem 3: Corollary 26, and Theorem 24 without its logarithms (the same lemma), for
  `ε < 0.1204 < ε*`.
* Theorem 4: Corollary 40.


### `wordRam_theorem_1`

 **Theorem 1**, on the word RAM. 

### `wordRam_theorem_2`

 **Theorem 2**, the four deterministic lines, on the word RAM. 

### `wordRam_theorem_2_graphs`

 **Theorem 2**, first line for `n`-vertex graphs, on the word RAM. 

### `wordRam_theorem_3`

 **Theorem 3**, on the word RAM. 

### `wordRam_theorem_4`

 **Theorem 4**, on the word RAM. 
