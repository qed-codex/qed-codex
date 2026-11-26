---
{
  "module": "proof/consequences/WidthK/Top/Poly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/WidthK/Top/Poly.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/WidthK/Top/Poly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The machine `satMK` is `IsPolyT` (init, step and out are polynomial-time) if the decoder, the
sparsification step and the root function are
polynomial-time and the machine that counts the solutions of a sparse formula is `IsPolyT`.
A lemma used for it: reading the formula off the decoder's output is polynomial-time if the decoder
is (`decF_polyT`). 

### `decF_polyT`

 Reading the formula off the decoder's output is polynomial-time if the decoder is. 

### `isPolyT_satMK`

 `satMK dec step root M` is `IsPolyT` if `dec`, `step`, `root` are polynomial-time and `M` is
`IsPolyT`. 
