---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Tables/BandCounters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Tables/BandCounters.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Tables/BandCounters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Band and block of every row, by counting (Section 2.3.4)

Section 2.3.4 cuts the N rows of X into bands of K₀ blocks of N₀ rows.  counters(N, K0, N0, dst)
writes, for every row I < N, its band I / (K0 N0) to the cell dst + I and its block I / N0 % K0 to
the cell dst + N + I.  There is no division: three counters (band, block, offset) are stepped from
each row to the next, as `Spec.stepCtr` says, and `Spec.ctrAt_succ` says that they are the
quotients and remainders.

A round writes two cells (`Counted.step`) and steps the counters (`countersRound_spec`);
`counters_spec` runs through the rows, and `counters_entry` is the specification that the callers of
the procedure assume.


### `Total`

 The local variables of counters: Total = N, Blocks = K0, Width = N0, Dest = dst (the arguments);
Row is the current row, and Band, Block, Offset are its band, its block and its offset. 

### `countersRound`

 One round: the band and the block of the current row are written, and the counters move on to
the next row. 

### `countersBody`

 counters(N, K0, N0, dst).  The row and the three counters are not set at the beginning: local
variables that are not arguments start at 0. 

### `Counted`

 The memory before round i: band and block of the rows below i are written, and no cell outside
the 2 N cells from dst has changed. 

### `Counted.step`

 The two cells that round i writes. 

### `Inv`

 The state before round i: the counters are those of row i. 

### `countersRound_spec`

 **One round** writes the band and the block of row `i` and steps the counters to those of row
`i + 1`. 

### `counters_spec`

 **counters** writes the band and the block of every row and changes nothing else. 

### `counters_entry`

 **The specification that the callers of counters assume.** 
