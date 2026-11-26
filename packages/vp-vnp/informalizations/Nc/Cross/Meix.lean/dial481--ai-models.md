---
{
  "module": "Nc/Cross/Meix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cross/Meix.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cross/Meix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Two families of polynomials

`mB y r n = [tⁿ] (1+t)^r/(1+yt)^(r+1)`, `mC y r n = [tⁿ] (1+yt)^r/(1+t)^(r+1)`.
That these are the coefficients, the relation between the two families and the orthogonality relation are
Paper.meixner_B, meixner_C, meixner_reciprocal and eq_orth (Paper/Identity.lean).


### `mB`

 `[tⁿ] (1+t)^r/(1+yt)^(r+1)`. 

### `mC`

 `[tⁿ] (1+yt)^r/(1+t)^(r+1)`. 
