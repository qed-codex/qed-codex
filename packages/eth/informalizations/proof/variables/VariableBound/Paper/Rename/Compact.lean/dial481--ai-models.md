---
{
  "module": "proof/variables/VariableBound/Paper/Rename/Compact.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Rename/Compact.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Rename/Compact.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The front end for the compact code

The compact code `MainTheoremForms.encC k φ` is `SatM.enc k φ` with 1ʷ in place of 1ᴺ, where w =
⌊log₂(2N)⌋ + 1 is the number of bits of a slot. `decC` reads the clauses from it: the width w is
read, not computed from N.
`rencC` is the front end: decode, rename the variables that occur, write the result in the code
`SatM.enc`.
* `rencC_encC`: for k ≥ 1 and φ with at most k literals in every clause, `rencC` maps the compact
  code of (k, φ) to `SatM.enc k (ren φ)`.
* `rencC_polyT`: it is polynomial-time. `lengthEncC`: the length of the compact code. 

### `clausesOf`

 The clauses written in the body b: one block of k slots of w bits per clause. 

### `decC`

 The clauses written in a compact code: after 1ᵏ 0 comes 1ʷ 0, then the body. 

### `rencC`

 The front end for the compact code: from the compact code of (k, φ) to the code of (k, φ with
the variables that occur renamed to 0, …, n − 1). 

### `bodyOf`

 The bits of the clauses of φ: k slots per clause, ⌊log₂(2N)⌋ + 1 bits per slot. 

### `takeWhile_ones`

 The leading 1s of 1ᵃ 0 v. 

### `dropWhile_ones`

 What follows 1ᵃ 0 in 1ᵃ 0 v. 

### `clausesOf_bodyOf`

 Reading the bits of the clauses with the width ⌊log₂(2N)⌋ + 1 gives the formula back, for k ≥ 1
and φ with at most k literals in every clause. 

### `decC_encC`

 Reading the compact code of (k, φ) gives the formula back, for k ≥ 1 and φ with at most k
literals in every clause. 

### `rencC_encC`

 The front end maps the compact code of (k, φ) to the code of (k, φ renamed), for k ≥ 1 and φ
with at most k literals in every clause. 

### `rencC_polyT`

 The front end for the compact code is polynomial-time. 

### `lengthEncC`

 The length of the compact code: k + w + 2 + m·k·w with w = ⌊log₂(2N)⌋ + 1. 
