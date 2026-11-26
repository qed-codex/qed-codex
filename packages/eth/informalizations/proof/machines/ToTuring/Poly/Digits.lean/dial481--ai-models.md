---
{
  "module": "proof/machines/ToTuring/Poly/Digits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Digits.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Digits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial time for the patterns ι of one level of the recursion (ι(q) is the digit number q of
a number in base λ+1) and for
the lengths of the bit strings that encode the labels of the grouping step (`tb`, `capW`); and
`sum_range_eq_list`, which turns a sum
over `Finset.range` into the sum of a list. 

### `sum_range_eq_list`

 A sum over `Finset.range` as the sum of a list, the form in which it is polynomial-time. 

### `digit_polyT`

 The digit number q of y in base n + 1. 

### `capW_polyT`

 The length of the bit string of a label when the bound c on the number of symbols is a number in
binary that is at most
the length n, which is given in unary. 
