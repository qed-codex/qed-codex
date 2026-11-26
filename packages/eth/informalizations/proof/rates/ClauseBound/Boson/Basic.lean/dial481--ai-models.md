---
{
  "module": "proof/rates/ClauseBound/Boson/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/Basic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The monomials of a given weight, the grading of the operators a[r], and rules for the normally ordered product

* `mem_P`, `mem_Pz`, `card_P`: the monomials of weight m are the multisets of positive integers with
  sum m, and there are p(m) of them.
* `op_grade`: a[r] raises the weight by r.
* `nop_eq_sum`: the index sets in the definition of the normally ordered product may be enlarged.

The auxiliary statements are in the namespace `ClauseBound.Boson.Basic`. 

### `nop_ne_zero`

 A nonzero entry of a normally ordered product comes from a nonzero entry of the family, after a
part of π or a part of σ has been removed. 

### `sum_erase_cast`

 The weight after a part has been removed. 

### `op_grade`

 a[r] raises the weight by r. 

### `nop_eq_sum`

 In `nop` the two index sets may be replaced by any larger finite sets. 
