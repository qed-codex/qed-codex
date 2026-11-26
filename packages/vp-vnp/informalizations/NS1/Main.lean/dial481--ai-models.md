---
{
  "module": "NS1/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Accelerators and changes of the ring of constants


### `map`

 The images of the constants. 

### `consts`

 The constants. 

### `poly_lg`

 Powers of the logarithm are small. 

### `HasAcc`

 There is an accelerator of size `s` at the scale `V = v ^ H` over `R`: a trie of at most `s` nodes with constants
of `R`, and a program of size at most `s` that has the values of the universal plain sums of `V` steps on all
instances of size `V ^ (1 - 2 η)` in `V ^ (1 - η)` steps, `η = 16 / H`; names of constants and exponents are of
polylogarithmic length. 
