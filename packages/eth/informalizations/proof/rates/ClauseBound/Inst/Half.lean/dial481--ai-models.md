---
{
  "module": "proof/rates/ClauseBound/Inst/Half.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/Half.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/Half.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The pieces with ρ = 1/√2 as programs: definitions

For strings of λ bits let h be the least number ≥ 2 with p(h) ≥ 2^λ. A string x stands for the
partition number x in the list of the partitions of h. The pieces are numbered
0, …, 4h; the piece number i is A_s with s = i − 2h. A label θ of a factorization is read as a
number and stands for the pair (j, τ) with that number in the list of all pairs with
0 ≤ j ≤ 2h and τ a partition of s + j (row-wise) or of 2h − s − j (column-wise). The two functions
of a factorization are entries of the matrices of the operators, read off tables
that are rebuilt at every call. Two constants have no explicit value and are parameters: c₀ (h is
searched for up to c₀·λ²) and c (no piece needs more than 2cλ bits, a pad of length 2^{cλ} suffices,
and all
values have at most (2λ)^c bits). Definitions only. 

### `sOf`

 s = i − 2h; the number i of the piece is cut off at 4h. 

### `wOf`

 The weight of τ in the pair (j, τ). 

### `labs`

 The list of the pairs (j, τ). 

### `encF`

 The partition of h that the string x stands for. 

### `partT`

 One of the two functions of a factorization, given h, s and the table T of the partitions of 0,
…, 4h. On top the strings are (x, y) row-wise and (x, u) column-wise;
below they are (u, v) row-wise and (y, v) column-wise. 

### `partH`

 One of the two functions of a factorization, as a function of (pad, direction), (unused
parameter, number of the piece), (two strings, label). 

### `deltaF`

 The number of all partitions of 0, …, 4h. 

### `padLen`

 A length of the pad that suffices for all tables. 

### `halfF`

 The pieces with ρ = 1/√2. 
