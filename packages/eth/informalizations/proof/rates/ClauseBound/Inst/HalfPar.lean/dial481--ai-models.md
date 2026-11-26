---
{
  "module": "proof/rates/ClauseBound/Inst/HalfPar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfPar.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfPar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # For large enough constants the pieces with ρ = 1/√2 as programs have the parameters (1/√2, c)

`Par.par_of_cst`: if c₀ and c are large enough at every length (`Cst c₀ c lam` for every λ ≥ 1),
then `halfF c₀ c` has the parameters (1/√2, c) in the sense of `ClauseBound.Gen.Par`. That the
programs
are pieces at every length λ ≥ 1 (`PiecesF.Spec`) enters as the hypothesis `StSpec`.
The main field is the one on the sum of the two numbers of bits of a piece (`Par.cap_add_cap_le`):
each number is a minimum, so it is at most ⌈log₂ R^row_s⌉ or
⌈log₂ R^col_s⌉ with s = i − 2h, |s| ≤ 2h, and the program's h, R^row and R^col are the numbers of
the mathematics. 

### `abs_sOf_le`

 |s| ≤ 2h for the number s of a piece. 

### `cap_add_cap_le`

 The two numbers of bits of a piece together are at most ⌈log₂ R^row_s⌉ + ⌈log₂ R^col_s⌉, s = i −
2h, h the least number ≥ 2 with p(h) ≥ 2^λ. 

### `par_of_cst`

 If c₀ and c are large enough at every length, then `halfF c₀ c` has the parameters (1/√2, c). 
