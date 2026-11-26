---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Host/PrimeStage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/PrimeStage.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/PrimeStage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The host of Theorem 17: the prime, the sizes, the addresses

This file proves the specification of the second part of the host procedure `et17` (Exact Triangle
by Theorem 17), which chooses the prime and computes the sizes and the addresses of the arrays:
five calls (`et17Sizes_spec`) and then seventeen assignments (`et17Addr_spec`).


### `et17Addr_spec`

 **The sizes and the addresses.**  Of the locals that are set before, only Size, Free, ParD,
ThePrime, Cap and Bits are read. 

### `SizesReady`

 What the second part uses: the parameters are not small, and the limits allow for one more
level of calls, for the arrays and for the numbers that the four small procedures form. 

### `sizesReady_of`

 The need of the host provides what the second part uses. 

### `et17Sizes_spec`

 **The second part of et17**: the prime, the sizes and the addresses are in the locals; only
cells from the free pointer on have changed. 
