---
{
  "module": "proof/machines/StepMachines/Math/GridArith.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/GridArith.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/GridArith.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Arithmetic for one level of the recursion (Section 5), in a form with other names than the
paper's: here ρ is the constant with 4ρ = log₂ 12 = 2 + log₂ 3, not the ρ = 11/12 of Lemma 2.
A name is the bit string that labels the bond of a rectangle between two merged nodes; it is written
in n + size(3^c) bits.
The file bounds the number of bits of 3^c, shows that the two names of a term, one for merged rows
and one for merged columns, have at most 4ρλ + 2 bits together,
and bounds the number C(g,2)² of rectangles by g⁴/4. 

### `size_three_pow_le`

 The number 3^c has at most c·log₂3 + 1 bits. 

### `four_rho`

 4ρ = log₂ 12 = 2 + log₂ 3. 

### `cap_pair_le`

 The two names of a term, with n = λ and d = i: the name for rows has n + size(3^(n−d)) bits, the
name for columns n + size(3^d) bits; together they have at most 4ρλ + 2 bits. 

### `four_mul_choose_sq_le`

 4·C(g,2)² ≤ g⁴. 
