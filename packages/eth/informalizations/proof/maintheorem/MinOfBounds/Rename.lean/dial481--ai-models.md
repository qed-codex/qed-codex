---
{
  "module": "proof/maintheorem/MinOfBounds/Rename.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MinOfBounds/Rename.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MinOfBounds/Rename.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Corollary 11 from Theorem A (c) and Theorem D (b): the renaming

This file proves the renaming to the paper's convention: the variables that occur are renamed to
x_1, …, x_n, in time polynomial in the length of the formula.

* `renamedCode_eq`: the bit string `MinOfBounds.renamedCode k φ` is `SatM.enc k (ren φ)`, where
  `VariableBound.Rename.ren φ` is the formula φ with every variable replaced by its position in the
  list of the variables that occur.
* `renamedCodeIsTheCodeOfARenaming`: the properties of `ren φ` that the proof uses; each of them is
  a theorem of proof/variables/VariableBound/Paper/Rename/Math.lean.
* `renamingFrontEndExists`: the polynomial-time function is `VariableBound.Rename.rencC` of
  proof/variables/VariableBound/Paper/Rename/Compact.lean.
* `numOcc_le_mul`: n ≤ m·k, because every variable that occurs stands in one of the m clauses, which
  have at most k literals each.
* `renamedCodeIsPolynomial`: the code of the renamed formula is at most twice as long as the compact
  code. It has k + n + 2 + m·k·(⌊log₂(2n)⌋ + 1) bits and the compact code has k + w + 2 + m·k·w bits
  with w = ⌊log₂(2V)⌋ + 1; here n ≤ V and n ≤ m·k. 

### `renamedCode_eq`

 The code of the renamed formula is `SatM.enc k (ren φ)`. No hypothesis on k or φ. 

### `renamedCodeIsTheCodeOfARenaming`

 The formula φ' is `VariableBound.Rename.ren φ`. 

### `rencC_renames`

 The function `VariableBound.Rename.rencC` is polynomial-time and renames the variables that
occur. 

### `renamingFrontEndExists`

 There is a polynomial-time function that renames the variables that occur:
`VariableBound.Rename.rencC`. 

### `length_literals_le`

 A list of m clauses with at most k literals each has at most m·k literals. 

### `numOcc_le_mul`

 n ≤ m·k: in a formula with m clauses of at most k literals each, at most m·k variables occur. 

### `length_renamedCode_le`

 The code of the renamed formula is at most twice as long as the compact code, for a formula with
at most k literals in every clause. 

### `renamedCodeIsPolynomial`

 The number a is 2. 
