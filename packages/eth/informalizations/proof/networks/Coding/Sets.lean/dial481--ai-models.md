---
{
  "module": "proof/networks/Coding/Sets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/Sets.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/Sets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Sets for lists

Section 6: «a clause is a nonempty set of literals, and a 3-CNF is a finite set of clauses with at
most 3 literals each». The end statement of this development, `Sat3.ThmEveryDelta`, has lists. Here:
every 3-CNF in the printed sense can be written as a list of lists; whatever writes it is an
instance in the sense of the end statement and is satisfiable exactly if the 3-CNF is (`stWrites`);
so 3-SAT is decided within c·2^{δn} steps for every δ > 0 also for 3-CNFs as sets, in whichever way
the set is written on the tape (`stSetFormOf`). And Section 3, Conventions: «a 3-CNF is a set of
clauses (Section 6), so m = O(n³)» (`stCubic`). 

### `stWrites`

 «a clause is a nonempty set of literals, and a 3-CNF is a finite set of clauses with at most 3
literals each» (Section 6): every such set can be written as a list of lists, and whatever writes it
is an instance of the end statement with as many clauses, without an empty clause, and satisfiable
exactly if the set is. 

### `stSetFormOf`

 **3-SAT in time c·2^{δn} for every δ > 0, for 3-CNFs as sets** (Section 6: «a 3-CNF is a finite
set of clauses with at most 3 literals each»), from the same for lists and from `StWrites` (lists
write sets). 

### `stCubic`

 «a 3-CNF is a set of clauses (Section 6), so m = O(n³)» (Section 3, Conventions): the clauses
are among the sets of 1, 2 or 3 of the 2n literals. 
