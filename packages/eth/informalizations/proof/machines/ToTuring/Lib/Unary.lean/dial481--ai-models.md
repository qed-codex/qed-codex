---
{
  "module": "proof/machines/ToTuring/Lib/Unary.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/Unary.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/Unary.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Numbers given in unary, as lists of that length: `Unary f` says that the list of `f x` copies of
`()` is `PolyT` in `x`.
This file relates `Unary` to `PolyT` and closes it under constants, composition, sums, products and
smaller functions. 

### `poly`

 A function that is polynomial-time in unary is polynomial-time as a number: take the length of
the list. 

### `of_length`

 The length of a polynomial-time list is polynomial-time in unary. 

### `of_le`

 A polynomial-time number bounded by a unary one is itself unary: cut the list of length `g c`
down to length `f c`. 
