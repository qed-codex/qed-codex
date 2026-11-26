---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/ThinLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/ThinLayout.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/ThinLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The input of a thin matrix product in the memory

The trusted layout of the data structures of Section 4 is N, D, further parameters, X, Y, written
from cell 0 on. This file says where each part stands (`thinPair_cellN`, `thinPair_cellD`,
`thinPair_matAt_X`, `thinPair_matAt_Y`), how long the input is
(`length_thinPair_input`), and that all its numbers fit in a word if N, D, the parameters and the
bound on the entries do (`abs_thinPair_input_le`).

The offline problems have the layout N, D, |W|, further parameters, X, Y, the rows of the wanted
positions, their columns. The lemmas `thinInstance_…` say the same about it.


### `thinPair_matAt_X`

 X stands behind the parameters. 

### `thinPair_matAt_Y`

 Y stands behind X. 

### `abs_thinPair_input_le`

 All numbers of the input fit in a word. 

 ## The offline layout 

### `thinInstance_matAt_X`

 X stands behind the parameters. 

### `thinInstance_matAt_Y`

 Y stands behind X. 

### `thinInstance_seg_rows`

 The rows of the wanted positions stand behind Y. 

### `thinInstance_seg_cols`

 Their columns stand behind the rows. 

### `abs_thinInstance_input_le`

 All numbers of the input fit in a word. 
