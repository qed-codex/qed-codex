---
{
  "module": "Nc/Uni/SortU.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Uni/SortU.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Uni/SortU.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The sorting loop


### `lsT`

 The list tape, read. 

### `lsF`

 The list tape, written. 

### `rw'`

 A record on the list: flag, letters and mark, end. 

### `NB`

 Letters other than the end of a block. 

### `Dr`

 Rounds of the distribution: flag, first letter, the others. 

### `emDr`

 Emissions of a round of the distribution. 

### `barSet`

 The channels where a pass of the distribution ends a block. 

### `Ps`

 Runs of a pass. 

### `bsl`

 The letters of records, in some order. 

### `emCo`

 Emissions of the collection. 

### `emPs`

 Emissions of a pass. 

### `dimPs`

 Dimension of a pass. 

### `emFi`

 Emissions of the last reading: the marks are in front and are dropped. 
