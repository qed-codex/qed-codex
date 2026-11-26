---
{
  "module": "NS1/ApproxAdd.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/ApproxAdd.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/ApproxAdd.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The counter of exponents

A program that adds two numbers of the same number of binary digits, modulo that power of 2, and is plain.


### `maj`

 Two of three bits are 1. 

### `addc`

 The digits of a sum, with a carry; the last carry is dropped. 

### `val_addc`

 **Paper: proof of Proposition prop:approx-acc, the counter adds.** The program's sum is the sum modulo 2 ^ length. 

### `addBr`

 Write a digit and go on with a carry. 

### `AD`

 Add; the argument is (this program, (carry, (number, number))). 
