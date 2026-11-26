---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/Routines.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Routines.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Routines.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The routines of Section 4, assembled

The fourteen routines with the numbers 40 to 53, as a list (procs40), and the theorem that every
program that holds them at these numbers (Has40) meets all their specifications (specs40). Each
routine is proved under the specifications of the routines that it calls; here these assumptions are
discharged, in the order in which the routines call each other. For the programs of Theorem 30, its
offline form and Corollary 26, which hold the fourteen routines behind forty others
(has40_of_append), this gives the specifications of the two routines that know the memory map:
preCoreSpec_of and preCoreSpec_all for the preprocessing, queryAtSpec_all for a query.


### `procs40`

 The bodies of the procedures number 40, 41, …, 53. 

### `Has40`

 The program P holds the routines of Section 4 at their numbers. 

### `Specs40`

 The specifications of all the routines of Section 4. 

### `specs40`

 **Every program that holds the routines of Section 4 at their numbers meets all their
specifications.** 

### `preCoreSpec_of`

 The preprocessing at a given place of the memory, for a program that also holds its body and
meets the specification of the shared stage. 

### `preCoreSpec_all`

 The same for all limits: the specification assumes Lim30, which contains the standing
assumptions. 

### `queryAtSpec_all`

 A query at a given place of the memory, for all limits. 

### `has40_of_append`

 A list that has forty procedures, then the routines of Section 4, then anything, holds them at
their numbers. 
