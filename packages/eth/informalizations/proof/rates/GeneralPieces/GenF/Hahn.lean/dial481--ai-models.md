---
{
  "module": "proof/rates/GeneralPieces/GenF/Hahn.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Hahn.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Hahn.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A derivation applied to every coefficient of a Hahn series

"e^{A⁻} is the ring homomorphism …, applied to the coefficient of each power of ω₂" (Appendix B): a
derivation d of a commutative ℚ-algebra A, applied to every coefficient of a series in the powers of
one more
variable with coefficients in A, is a derivation of the ring of these series (`hder`); and commuting
derivations give commuting derivations (`hder_comm`). 

### `hmap`

 d applied to every coefficient, as a linear map. 

### `hder`

 d applied to every coefficient, as a derivation. 

### `hder_comm`

 Commuting derivations give commuting derivations. 

### `hder_single`

 On a series with one term. 

### `hder_C`

 On a constant series. 
