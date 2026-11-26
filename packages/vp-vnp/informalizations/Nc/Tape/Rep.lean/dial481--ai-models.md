---
{
  "module": "Nc/Tape/Rep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tape/Rep.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tape/Rep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Linear representations of series on words

A series is a function `List Ω → F`. A linear representation of dimension `n` gives the value of the series
at a word as (row vector) · (product of matrices, one for each letter) · (column vector). Sums, products and
stars (over non-empty factors) of represented series are represented, and dimensions add up.


### `Series`

 A series on words. 

### `mul`

 The Cauchy product. 

### `one`

 The unit: 1 at the empty word. 

### `kstar`

 The star over non-empty factors: the sum over all ways to cut the word into non-empty factors. 

### `Rep`

 A linear representation with state space `Q`. 

### `Rep.lam`

 initial weights 

### `Rep.mu`

 transition weights 

### `Rep.gam`

 final weights 

### `tail`

 The weights from a state to acceptance along a word. 

### `series`

 The series of a representation. 

### `add`

 Sum of two series. 

### `mul`

 Product of two series. 

### `star`

 Star of a series (over non-empty factors). 
