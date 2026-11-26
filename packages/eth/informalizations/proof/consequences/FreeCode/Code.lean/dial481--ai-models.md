---
{
  "module": "proof/consequences/FreeCode/Code.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Code.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Code.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Definition 6 with the code that does not depend on k: one literal, and the length of the code

No sentence of the paper stands behind this file: the paper fixes no code.
* `slotDec_encLit`: the bits of a literal, read as a number (`ofWord`) and then as a literal
  (`Decode.slotDec`), give the literal back. The number of a literal is below 2^(⌊log₂ 2n⌋+1), so
  its bits determine it.
* `stLength` (= `FreeCode.StLength`): the code of a k-CNF on n variables has length below (2^k·(k+1) + 2)·(n+2)^(k+1).
  It uses that a k-CNF in which no clause is written twice has at most (2n+1)^k clauses
  (`DecodeK.IsKCNF.length_le`).
The first three lemmas repeat, for a literal rather than an optional literal, lemmas of
proof/machines/StepMachines/Prog/Decode.lean that are not visible outside that file; so do
`takeWhile_header` and `dropWhile_header` in Reader.lean. 

### `toWord_eq`

 The ℓ lowest binary digits of y, lowest first, are its bits number 0 to ℓ − 1. 

### `slot_lt`

 The number of a literal on n variables is below 2^(⌊log₂ 2n⌋+1). 

### `slotDec_slot`

 The number of a literal, read as a literal, gives the literal back, with its variable as a
number. 

### `encLit_eq`

 The bits of a literal are the ⌊log₂ 2n⌋ + 1 lowest binary digits of its number. 

### `length_encLit`

 A literal is written with ⌊log₂ 2n⌋ + 1 bits. 

### `slotDec_encLit`

 The bits of a literal, read as a number and then as a literal, give the literal back. 

### `length_encClause`

 A clause of s literals is written with 2 + s·(⌊log₂ 2n⌋ + 2) bits. 

### `length_clauses_le`

 The clauses of a formula with at most k literals per clause are written with at most m·(2 +
k·(⌊log₂ 2n⌋ + 2)) bits, m the number of clauses. 

### `length_enc_succ_le`

 The length of the code, plus one, of a k-CNF on n variables is at most (2^k·(k+1) + 2)·(n+2)^(k+1). 

### `stLength`

 The length of the code of a k-CNF on n variables is polynomial in n, for fixed k: the statement
`FreeCode.StLength`. 
