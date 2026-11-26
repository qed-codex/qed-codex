---
{
  "module": "proof/networks/Eight/App_Pieces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/App_Pieces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/App_Pieces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Arithmetic bounds on t = ⌈λ/3⌉, (2λ)^c and log₂(2λ)

In Appendix A the functions A_0, …, A_t of Definition 5 are pieces with parameters (11/12, c) for
every integer c ≥ 8, with I = {0, …, t} and d = 2^t; part (c) of Definition 7 asks that the numbers
involved be below 2^((2λ)^c).
The lemmas here are elementary bounds of that kind, for λ ≥ 1 and c ≥ 1: t ≤ λ, 2λ ≤ (2λ)^c, 2^t <
2^((2λ)^c) and log₂(2λ) ≥ 1.
They concern only sizes, not running times. 

### `tOf_le`

 t = ⌈λ/3⌉ ≤ λ for λ ≥ 1. 

### `two_mul_le_pow`

 2λ ≤ (2λ)^c for c ≥ 1. 

### `two_pow_tOf_lt`

 2^t < 2^((2λ)^c). 

### `one_le_logb`

 log₂(2λ) ≥ 1 for λ ≥ 1. 
