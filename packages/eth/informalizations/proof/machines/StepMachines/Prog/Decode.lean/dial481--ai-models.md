---
{
  "module": "proof/machines/StepMachines/Prog/Decode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Decode.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Decode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Reading the input: `dec` recovers the number of variables and the clauses from the bit string
`Sat3.enc φ`.
The string is `n` ones, a zero, then for every clause three slots of `width n` bits, each holding a
literal or nothing.
Variables are natural numbers on the decoded side. 

### `NCNF`

 A formula with natural numbers as variables. 

### `width`

 The number of bits of a slot: ⌊log₂ (2n)⌋ + 1. 

### `slotDec`

 A slot's number as a literal: 0 = none, 2i+1 = ¬xᵢ, 2i+2 = xᵢ. 

### `clauseDec`

 The clause written in a block of three slots of `w` bits. 

### `dec`

 The number of variables and the clauses written in a bit string. 

### `toN`

 The formula with its variables read as natural numbers. 

### `SatN`

 Satisfiability of a formula with natural numbers as variables. 

### `block_flatten`

 Blocks of one length, laid end to end, are read back by offset. 

### `blk`

 The bits of clause `C` in the code. 

### `dec_enc`

 Decoding the code of a formula with at most three literals in every clause gives back `n` and
the formula. 

### `length_enc`

 The length of the code. 

### `length_enc_succ_le`

 The code is polynomially long. 

### `satN_toN`

 Satisfiability does not depend on how variables are named. 

### `nil_mem_toN`

 The empty clause is seen on the decoded side. 

### `mem_toN`

 Clauses keep their lengths, and the variables are below `n`. 
