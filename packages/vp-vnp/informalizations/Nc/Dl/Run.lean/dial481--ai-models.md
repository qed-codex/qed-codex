---
{
  "module": "Nc/Dl/Run.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Dl/Run.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Dl/Run.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The runs of the dealing program


### `digN`

 A number of units as a digit. 

### `digO`

 An outcome as a digit. 

### `flagT`

 The flags of a row. 

### `kRT`

 Keys of units written. 

### `kCT`

 Keys of units read. 

### `dgT`

 Instructions for the diagonal. 

### `chT`

 Keys of new units. 

### `S0`

 The state at the beginning. 

### `own1`

 Names of phase 1. 

### `v1`

 Values of phase 1. 

### `opts1`

 Options of phase 1. 

### `steps1`

 Phase 1: the states between the blocks. 

### `S1`

 The state after phase 1. 

### `own2`

 Names of phase 2. 

### `v2`

 Values of phase 2. 

### `steps2`

 Phase 2: row data. 

### `own3`

 Names of phase 3. 

### `v3`

 Values of phase 3. 

### `o3`

 Options of phase 3. 

### `steps3`

 Phase 3: numbers of units. 

### `own4`

 Names of phase 4. 

### `v4`

 Values of phase 4. 

### `steps4`

 Phase 4: outcomes. 

### `vr`

 The row data are valid after the given last party. 

### `rowStep`

 Check of a row. 

### `steps5`

 Phase 5: checks of the rows. 

### `coord`

 The name of an input of the straight-line program. 

### `slpStep`

 A step of the straight-line program. 

### `steps6`

 Phase 6: the straight-line program. 
