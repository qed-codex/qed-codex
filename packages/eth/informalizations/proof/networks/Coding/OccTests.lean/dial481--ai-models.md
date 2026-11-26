---
{
  "module": "proof/networks/Coding/OccTests.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/OccTests.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/OccTests.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «An occurrence lies in at most two tests …»

Section 6: «An occurrence lies in at most two tests. The total number of tests is the number of
occurrences minus the number of variables that occur, hence at most 3m − 1.» This development proves
these sentences for tests as pairs of places (`Eight.card_tests_at_le_two`,
`Eight.card_testsOf_add`, proof/networks/Eight/SecProof_Network.lean).
Here they are carried over to `Coding.tests`, the list of pairs of occurrences, along the map that
sends a place with a literal to its occurrence; all of Φ is taken as one cluster. The map is one to
one, goes onto the occurrences, and carries Lean's links to the tests (`mem_tests_iff`,
`linkB_iff`). `import all StepMachines.Prog.CountNet` gives access to `linkB_iff` and `litAt_idx`,
which are not public. 

### `occOfSlot`

 The pair (clause, position) of a place, all of Φ being one cluster. 

### `place_occOfSlot`

 The place of the pair of a slot is the index that Lean's network gives the slot. 

### `occOfSlot_injective`

 Different slots have different pairs. 

### `exists_occOfSlot`

 Every occurrence is the pair of some slot. 

### `mem_occurrencesOf_iff`

 A place holds a literal exactly if its pair is an occurrence. 

### `mem_tests_iff_link`

 A pair of places is a link exactly if the pair of their occurrences is a test. 

### `nodup_tests`

 No test is listed twice. 

### `toFinset_tests`

 The tests are the pairs of the links of Lean's network, taken slot by slot. 

### `toFinset_occAll`

 The occurrences are the pairs of the slots that hold a literal. 

### `getD_eq_getElem'`

 Inside the list, getD reads the entry. 

### `toFinset_vars`

 The variables at the occurrences are the variables that occur. 

### `stTests`

 «An occurrence lies in at most two tests. The total number of tests is the number of occurrences
minus the number of variables that occur, hence at most 3m − 1» (Section 6). 
