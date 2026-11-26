---
{
  "module": "proof/consequences/WidthK/Decode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/WidthK/Decode.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/WidthK/Decode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Reading the code of a k-SAT instance

`SatK.enc k φ` is `n` ones, a zero, then for every clause k slots of `width n` bits, each holding a
literal or nothing. This file defines the decoder
`decK k` and proves: `decK k (enc k φ) = (n, toN φ)` for k ≥ 1 when no clause has more than k
literals (`decK_enc`); and, for an instance of k-SAT,
the code has length less than (k·2^k + 1)·(n+2)^(k+1) (`length_enc_succ_le`).
With k = 0 a clause takes no bits, and the formulas [] and [[]] have the same code.

The file follows proof/machines/StepMachines/Math/Formula.lean and
proof/machines/StepMachines/Prog/Decode.lean line by line, with a parameter k for their width 3, and
uses their
lemmas that do not mention the width. Where they write out the slots 0, 1, 2, this file uses
`filterMap_range_getElem?`, proved by induction on k.
`toN`, `SatN` and `satN_toN` (φ is satisfiable iff `toN φ` is) are those of Prog/Decode.lean,
unchanged. 

### `clauseDec`

 The clause written in a block of k slots of `w` bits. 

### `decK`

 The number of variables and the clauses written in a bit string, k slots per clause. 

 ### The number of clauses 

### `eq_of_slots`

 A clause of at most k literals is determined by its entries at the places 0 to k − 1. 

### `IsKCNF.length_le`

 An instance on n variables has at most (2n+1)^k clauses, so its code is polynomially long. 

 ### Decoding 

### `filterMap_range_getElem`

 Reading the first k places of a list one by one gives its first k members. 

### `blk`

 The bits of clause `C` in the code. 

### `blk_eq`

 The bits of a clause are the words of its k slots, laid end to end. 

### `length_blk`

 Every clause takes k·(⌊log₂ (2n)⌋ + 1) bits. 

### `clauseDec_blk`

 Reading the bits of a clause of at most k literals gives the clause back, with its variables as
natural numbers. 

### `enc_eq`

 The code is the header 1ⁿ 0 followed by the bits of the clauses. 

### `length_body`

 The number of bits after the header. 

### `decK_enc`

 For k ≥ 1, decoding the code of a formula with at most k literals in every clause gives back `n`
and the formula, with
its variables as natural numbers. 

 ### The length of the code 

### `length_enc`

 The exact length of the code: the header, then k slots for every clause. 

### `length_enc_le`

 The code of an instance of k-SAT has at most n + 1 + k·(⌊log₂ (2n)⌋ + 1)·(2n+1)^k bits. 

### `length_enc_succ_le`

 The length of the code of an instance of k-SAT, plus one, is at most (k·2^k + 1)·(n+2)^(k+1):
polynomial in n for fixed k. 
