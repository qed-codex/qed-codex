---
{
  "module": "proof/variables/VariableBound/Paper/Rename/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Rename/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Rename/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Renaming the variables that occur: the program

The n variables that occur are renamed to x₁, …, xₙ, the paper's convention. Here the new names are
0, …, n − 1. This file has the program that does it, as a function from bit strings to bit strings.
Definitions only.
The input is `SatM.enc k φ` for a formula φ over x₀ … x_(N−1). It is decoded (`kOf`, `fmlOf` of
proof/rates/ClauseBound/Alg/Top.lean) to k in unary and the list of clauses with natural numbers as
variables.
`occL` lists the variables that occur, each once, in the order of their last occurrence; `renF`
replaces every variable by its position in that list; `encN` writes the result as a bit string
again, by the formula
of `SatM.enc`. The number N is not used. 

### `occL`

 The variables that occur in ψ, each once, in the order of their last occurrence. 

### `renL`

 ψ with every variable replaced by its position in the list L. 

### `renF`

 The renamed formula: the number of variables that occur, in unary, and ψ with every variable
replaced by its position in `occL ψ`. 

### `slotN`

 A slot of a clause as a number, as `Sat3.slot`: 0 = no literal, 2i+1 = ¬xᵢ, 2i+2 = xᵢ. 

### `encN`

 The code of (k, n, ψ), with k and n in unary, by the formula of `SatM.enc`: 1ᵏ 0, then 1ⁿ 0,
then k slots per clause, ⌊log₂ (2n)⌋ + 1 bits per slot, low bit first. 

### `renc`

 The front end: from the code of (k, φ) to the code of (k, φ with the variables that occur
renamed to 0, …, n − 1). 
