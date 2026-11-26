---
{
  "module": "proof/maintheorem/NamesInOrder/General.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/NamesInOrder/General.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/NamesInOrder/General.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The general case: a formula with any names
`generalFormFollows`: let N have the bound of the Main Theorem with nothing added, and let N′ run N
behind a front end that renames the variables that occur. The renamed formula has the same k and m,
its n variables all occur, and it has as many satisfying assignments as φ has on the variables that
occur (`MinOfBounds.renamedCodeIsTheCodeOfARenaming`). So N′ runs within q·(bound + L + 1)^q steps,
L the length
of the compact code, which `MinOfBounds.overheadGoesIntoC` turns into the bound for any names plus a
polynomial in L. `generalFormFollowsAsPropositions` uses `MinOfBounds.renamingFrontEndExists` and
`Wrap.everyMachineCanBeWrapped`. 

### `timeMin_le`

 2^{C·min{a, b}}, rounded down, is at most each of 2^{C·a} and 2^{C·b}, rounded down. 

### `generalFormFollows`

 The general case, first half, for every machine. 

### `generalFormFollowsAsPropositions`

 So the Main Theorem with nothing added to the bound, for formulas whose variables all occur,
gives the Main Theorem for formulas with any names, with a polynomial in the length of the code
added. 
