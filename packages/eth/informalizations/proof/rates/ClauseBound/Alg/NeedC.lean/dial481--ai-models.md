---
{
  "module": "proof/rates/ClauseBound/Alg/NeedC.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/NeedC.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/NeedC.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The exponent of the pad, computed under a bound (`StNeedC`)

`needC P b Kup lam B sched` goes through the schedule with a state that holds the current label
length, entry size, length of the work list, size of the sum, number of nodes, and the largest
exponent so far. After every step the state is thrown away if its word is longer than 100·(b + 2).
Here: if the computation gives a number, that number is `needG`; and if `needG` is at most
b, the computation gives it.

* Without cut-offs the computation gives `needG` (`needFin_foldl`).
* A state that was thrown away stays away (`foldl_none`), so a result comes from the computation
  without cut-offs (`eq_of_foldl_eq_some`).
* The word of a state has 4·lam + 3·(the binary digits of B, cnt, z, the number of nodes and the
  largest exponent so far) + 26 symbols, and each of these six numbers is at most the largest
  exponent
  so far or `needG` of the rest of the schedule (`len_some_le`); that maximum is the same at every
  step (`tot_cons`). 

### `tot`

 The larger of the largest exponent so far and `needG` of the rest of the schedule. 

### `tot_cons`

 A step does not change `tot`. 

### `needFin_foldl`

 Without cut-offs the computation gives the larger of the largest exponent at the start and
`needG`. 

### `first_le_needG`

 The bounds of the first step (the binary digits of the first sum, lam, and the binary digits of
B and of Kup) are at most `needG`. 

### `size_le_self`

 A number has at most as many binary digits as its value. 

### `len_some_le`

 The word of a state is short. 

### `foldl_none`

 A state that was thrown away stays away. 

### `eq_of_foldl_eq_some`

 A result of the computation with cut-offs is the result of the computation without. 

### `foldl_eq_some`

 If the bound b is at least the largest exponent at the start and `needG`, no cut-off at 100·(b + 2)
is active. 

### `stNeedC`

 `StNeedC`: the computation under the bound b gives nothing but `needG`, and it gives `needG` if
that is at most b. 
