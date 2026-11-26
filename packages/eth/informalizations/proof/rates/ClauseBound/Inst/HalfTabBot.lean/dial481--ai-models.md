---
{
  "module": "proof/rates/ClauseBound/Inst/HalfTabBot.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfTabBot.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfTabBot.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The second factor of a term of a piece, from the table of ν[·]

`zzF` computes z_ν, and `botF` computes the entries of (h!/z_ν)·ν[r], if the list of monomials is in
order, all parts of ν are at most W and the pad is long enough. 

### `prod_toFinset_coe`

 A product over the distinct members of a list. 

### `zzF_eq`

 `zzF` computes z_ν. 

### `botF_eq`

 `botF` computes the entries of (h!/z_μ)·μ[r]. 
