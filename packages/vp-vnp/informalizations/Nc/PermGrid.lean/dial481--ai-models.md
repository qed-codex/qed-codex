---
{
  "module": "Nc/PermGrid.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/PermGrid.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/PermGrid.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Sums over two families of bits as permanents

`N` is a finite set of incidences with two permutations `σ`, `ρ`. A bit for every orbit of `σ` and a bit for
every orbit of `ρ` are summed over, and every incidence contributes a weight that depends on its two bits.
The sum is a permanent of size `3 * |N|`.


### `pick`

 The row that is chosen at `n`: `n` itself or its successor. 

### `slot`

 The columns used by the three rows of an incidence. 

### `ind`

 The indicator of a column. 

### `gridMatrix`

 The matrix. 

### `wt`

 The weight of a choice. 
