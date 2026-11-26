---
{
  "module": "proof/rates/PaddedDescent/F/SideF.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/SideF.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/SideF.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The network of one term of one level of the recursion (Section 5), read off an explicit table (cutF = cutW, itemF = sideItem, StS, StChild)

`sideF` presents `Grid.sideN`; with `StRG` this gives the step for one term y, where the number y
names one choice of a piece for every rectangle (the ι in the proof of Proposition 3): the child has
Z = `sideZ` of y, and the
bounds `lamNext`, `bNext` hold for it. 

### `cutF_eq`

 `cutF` is `cutW`, if the pad has at least 2^|x| units. 

### `itemF_eq`

 `itemF` is `sideItem`, if the pad has at least 2^n units. 

### `stS`

 `StS`: `sideF` presents the network `Grid.sideN` of one term, if the pad is long enough. 

 ### The arithmetic of one level 

### `Pn_mono`

 `Pn g` is monotone in the label length. 

### `Ubar_mono`

 `Ubar g` is monotone in the label length. 

### `capM_mono`

 `capM g` is monotone in the label length. 

### `lamNext_mono`

 `lamNext K g` is monotone in the label length. 

### `bNext_mono`

 `bNext K g` is monotone in the label length. 

### `le_mul_div_succ`

 x ≤ y·(x / y + 1) for y > 0. 

### `stChild`

 One term: the core of `StE`. (The hypothesis y < (ℓ+1)^R of the statement is not used.) 
