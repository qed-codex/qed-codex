---
{
  "module": "proof/rates/GeneralPieces/Half/Spec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Half/Spec.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Half/Spec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The pieces with ρ = 1/√2 as programs: their specification, from the statements about the ring

This file specifies the programs `halfF c₀ c`. That the pieces add up to h!·[x = v][y = u] and that
they are the sums of displays (54) and (55) is taken
from `AppHalfPieces.PieceFacts`, the steps of the proof of the theorem on pieces with ρ = 1/√2 as
statements about the ring ℚ[t₁, t₂, …] (a hypothesis of every theorem here). The bounds on the
pieces and on the values that the programs return are those of the
paragraph «Sizes and operations» of that proof (`Half/Size.lean`), and the two constants are chosen
from its paragraph «Numbers of bits», from log Δ = O(λ) and from the theorem on pieces with ρ = 1/√2
without the bound on operations of Definition 7(c)
(`thmHalfPiecesPure`). That the programs return the entries of the matrices, the list of the labels
and the encoding of the strings is taken from the lemmas about the programs (`stVal_all`, `stLabs`,
`stEnc`). 

### `halfA`

 The piece number i for strings of λ bits, as an integer function: A_s with s = i − 2h, h the
least number ≥ 2 with p(h) ≥ 2^λ, and μ(x) the partition with number x (lowest bit first) in the
programs' table of
the partitions of h, which is the lexicographic list of Appendix B (proved in `Half/Order.lean`). 

### `stFact`

 The two factorizations of the pieces by the two programs. The row half is display (54) on the
ring (`ApcL_row_eq`); the column half is display (55) in a form for the matrices
(`ClauseBound.Boson.ApcL_col_eq`);
display (55) on the ring is used where the function is identified with the A_s of Appendix B
(`ApcL_eq_piece`). 

### `half_realizes`

 The programs realize the functions `halfA`, at every length at which the constants are large
enough. 

### `stSpec`

 The specification of the pieces at every length at which the constants are large enough. 

### `exists_par_half2`

 For suitable constants the pieces with ρ = 1/√2, as programs, have the parameters (1/√2, c), and
the constants are large enough at every length. 
