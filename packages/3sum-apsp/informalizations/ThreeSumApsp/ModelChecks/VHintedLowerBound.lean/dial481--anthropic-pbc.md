---
{
  "module": "ThreeSumApsp/ModelChecks/VHintedLowerBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/ModelChecks/VHintedLowerBound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/ModelChecks/VHintedLowerBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Phase 3 of v-hinted Mv needs linear time on the word RAM

A check of the definition of a problem that is solved in phases (Section 5.4): it cannot be met for
free. The `n` output cells depend on the index that arrives in Phase 3, and a step writes one cell
(`WordRam.changed_cells`).  Take all entries of `M` equal to 1, column 0 of `V` all 1 and its
other columns all 0.  For the indices 0 and 1 the first two phases are the same runs, and the
outputs differ in all `n` cells; but two runs of Phase 3 that together take fewer than `n` steps
leave one output cell as it was.


### `one_le_hintSize`

 The hint dimension is at least 1. 

### `output_zero`

 All entries of `M` are 1 and column 0 of `V` is all 1: the output for the index 0 is all 1. 

### `output_one`

 The other columns of `V` are all 0: the output for the index 1 is all 0. 

### `not_achievesVHinted`

 Whatever is prepared in Phases 1 and 2, Phase 3 of v-hinted Mv takes linear time. 
