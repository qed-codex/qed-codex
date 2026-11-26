---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Contract.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Contract.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Contract.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The pruned recursion with its helpers

Let a program hold the bodies of fill, segBounds, union, pick and pruned as its procedures number
pFill, pSegBounds, pUnion, pPick and pPruned.  Then a call of pruned does what PrunedSpec says: it
writes the values of Pruned (Section 2.4.2) at the codes of its list to out, changes no cell but
these and its stack, and takes at most 5500 steps for each call of the recursion and for each code
passed to a call.  The proof puts the specifications of the four helpers into PrunedCtx.entry.


### `pruned_entry`

 **pruned** does what PrunedSpec says, in at most 5500 prunedWork steps.  Here
5500 = 50 · 70 + 2000, and 70 is the largest of the constants in the times of the four helpers. 
