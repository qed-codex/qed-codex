---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/OfflineStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/OfflineStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/OfflineStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 30, the offline form (9), on the word RAM

From the specifications of preCore and queryAt to Items.Theorem_30_wanted, for any program that
holds wantedCore and wantedMain at their numbers (`theorem_30_wanted_of`). The light program solves
the problem (`wanted_topSolves`) for four reasons, one lemma each: the trusted input is laid out as
wantedMain expects (`wantedLayout_input`), the time is `O((9))` (`exists_tWantedCore_le`), the block
starts at an address that is polynomial in N (`wantedB0_le`), and the numbers of the input fit in a
word (`abs_wanted_input_le`).


### `length_le_sq`

 A list of positions without repetitions has at most N² members. 

### `exists_tWantedCore_le`

 **The time** of the main procedure is `O((9))`: the preprocessing is within (8), and each of the
w rounds is within the cost of a query. 

### `wantedLayout_input`

 The trusted input of the offline form, with D = 4^m, is laid out as wantedMain expects. 

### `wantedB0_le`

 **The block** starts at an address that is polynomial in N. 

### `abs_wanted_input_le`

 **The numbers of the input fit in a word** of the limits of Theorem 30, if the block starts
behind them. 

### `wanted_topSolves`

 **The offline form of Theorem 30 as a light program.** 

### `theorem_30_wanted_of`

 **Theorem 30, the offline form, on the word RAM**, for any program that holds the routines. 
