---
{
  "module": "proof/rates/GeneralPieces/Trim/Cert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Trim/Cert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Trim/Cert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The values of the pieces are computed in polynomial time

If the programs of P are polynomial-time in the pad and their arguments, so is the program `valF P`
for the values of the pieces (`valF_polyT`). This is
the requirement that one algorithm computes each of them, in the definition of pieces with
parameters (ρ, c) in Appendix A, for the values of the pieces; the loop of `valF` is cut off by the
pad, so
no condition on the pad is needed here. 

### `unary_min'`

 The smaller of two numbers, the second of which is given in unary, is given in unary. 

### `cap_unary`

 The number of bits of a factorization of P, with h and λ in unary and the number of the piece in
binary. 

### `valF_polyT`

 The value of a piece is polynomial-time in the pad, h in unary, the number of the piece in
binary and the four strings. 
