---
{
  "module": "proof/rates/ClauseBound/Alg/Decode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Decode.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Decode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Reading the input 1ᵏ 0 code(φ)

The input of the machine that counts for all k at once is `SatM.enc k φ`: k ones, a zero, then the
code `SatK.enc k φ` of φ as an instance of k-SAT.
`kOf` returns k in unary and `fmlOf` returns n in unary and the formula with natural numbers as
variables (`stDecM`), both in polynomial time (`stCertDecM`).
Here k is part of the input, in unary. The certificates of
proof/consequences/WidthK/Poly/Decode.lean have k as a constant; this file proves its three lemmas
with k a function of the input. 

 ### What is read 

### `kOf_ones`

 `kOf` reads k from 1ᵏ 0 w. 

### `restOf_ones`

 `restOf` reads w from 1ᵏ 0 w. 

### `stDecM`

 For k ≥ 1, reading the code of (k, φ), where φ has at most k literals in every clause, gives
back k in unary, n in unary and the formula with natural numbers as variables. 

 ### Polynomial time, with k as data in unary 

### `clauseDec_polyT`

 Reading one clause from a block of k slots of w bits is polynomial-time, k in unary. 

### `clauses_polyT`

 Reading the list of clauses from the body b, one block of k·w bits per clause, is
polynomial-time, k in unary. 

### `decK_polyT`

 The decoder `decK` is polynomial-time jointly in k, in unary, and the word. 

### `decU_polyT`

 The reader `decU` is polynomial-time jointly in k, in unary, and the word. 

### `kOf_polyT`

 `kOf` is polynomial-time. 

### `restOf_polyT`

 `restOf` is polynomial-time. 

### `stCertDecM`

 `kOf` and `fmlOf` are polynomial-time. 
