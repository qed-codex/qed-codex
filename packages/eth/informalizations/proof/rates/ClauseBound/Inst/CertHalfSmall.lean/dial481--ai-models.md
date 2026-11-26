---
{
  "module": "proof/rates/ClauseBound/Inst/CertHalfSmall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/CertHalfSmall.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/CertHalfSmall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The pieces with ρ = 1/√2 as programs: the certificates of the five numbers

For all values of the two parameters c₀ and c of `halfF`: the number of pieces, the number of bits
of a factorization, the exponent of the pad and the bound for the bits of the values are given in
unary (`cnt`, `cap`, `need`, `bits`), and the factor d = h! is polynomial-time (`d`), all as
functions of λ in unary. These are five of the seven fields of `(halfF c₀ c).Keeps`. 

### `sOf_polyT`

 s = i − 2h, with i cut off at 4h, is polynomial-time in h and i. 

### `clog_polyT`

 The least k with n ≤ 2^k is polynomial-time in n. 

### `cnt`

 The number 4h + 1 of pieces is given in unary. 

### `d`

 The factor h! is polynomial-time. 

### `cap`

 The number of bits of a factorization is given in unary; the number i of the piece is in binary. 

### `need`

 The exponent c·λ of the pad is given in unary. 

### `bits`

 The bound (2λ)^c for the number of bits of the values is given in unary. 
