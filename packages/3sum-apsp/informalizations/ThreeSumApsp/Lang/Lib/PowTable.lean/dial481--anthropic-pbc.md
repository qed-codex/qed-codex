---
{
  "module": "ThreeSumApsp/Lang/Lib/PowTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/PowTable.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/PowTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Tables of powers

powTable(dst, L, b) writes 1, b, b², …, b^(L-1) into the L cells from dst and changes nothing else,
within `powTableTime L` steps (`powTable_meets`).  The list of these powers is `powList b L`.


### `powList`

 The pure model: the powers 1, b, …, b^(L-1). 

### `Dest`

 The local variables of powTable: the arguments dst, L and b, the exponent j, and the power b^j.


### `powTableRound`

 One round: dst[j] := p; p := p * b. 

### `powTableBody`

 powTable(dst, L, b): p := 1; for j < L: dst[j] := p; p := p * b. 

### `powTableTime`

 The time of powTable. 

### `PowTable.Filled`

 The state before round j: p = b^j, the first j cells hold the powers up to b^(j-1), and no cell
outside the L cells from dst has changed.  The list t holds the local variables after the five of
powTable. 

### `powTable_ends`

 The body of powTable writes the powers of b and changes nothing else, whatever its local
variables hold apart from the three arguments. 

### `powTable_meets`

 **powTable(dst, L, b)** writes the powers 1, b, …, b^(L-1) into the L cells from dst and changes
nothing else. 
