---
{
  "module": "proof/rates/GeneralPieces/DefGenPieces/Conv.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/DefGenPieces/Conv.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/DefGenPieces/Conv.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The definition of pieces with parameters (ρ, c), and the form in which the recursion uses it

`AppRunningTime.IsPieces` is the definition in Appendix A, clause by clause. The programs of the
recursion are analysed under `ClauseBound.Gen.Par P ρ c` and `P.Keeps`, which speak of every value
of the parameter h
and have three more fields: the exponent of the pad, a bound for the number of bits of the values,
and a constant m with all numbers of bits at most 2·m·λ. This file goes both ways.

* `of_par_realizes`: from `Par P ρ c` and `P.Keeps` to the definition, with max(c + 1, 2m) in place
  of c. The c + 1 turns «at most» into «below»; the 2m is the loop of `valF`, which adds up the
  value
  of a piece.
* `atZero_par`, `atZero_keeps`: from the definition to `Par` and `Keeps` for the programs read at h =
  0, given a bound 2·m·λ on all numbers of bits; `Par` then holds with every constant c' ≥ c, m.
  If all numbers of bits are at most 2λ then m = 1 and the constant c is the same (`to_par_one`).

The definitions `valOf` and `atZero` are in `DefGenPieces/Progs.lean`. 

 ### From the programs of the recursion to the definition 

### `abs_lt`

 «At most 2^b» with b ≤ (2λ)^c is «below 2^{(2λ)^{c'}}» for c' > c. 

### `logb_nonneg`

 log(2λ) ≥ 0. 

### `logb_le`

 log(2λ) ≤ λ. 

### `of_par_realizes`

 Programs with `Par P ρ c` and `P.Keeps` are pieces with parameters (ρ, max(c + 1, 2m)) in the
sense of the definition, with any functions A_i that they realize at h = 0. 

 ### From the definition to the programs of the recursion 

### `cnt_pos_of_isPieces`

 The index set is not empty, because the pieces add up to d ≥ 1 at x = v, y = u. 

### `atZero_spec`

 The programs read at h = 0 are pieces in the sense of the recursion, at every h. 

### `atZero_par`

 Pieces with parameters (ρ, c) all of whose numbers of bits are at most 2·m·λ give `Par` with
every constant c' ≥ c, m. 

### `atZero_keeps`

 The programs read at h = 0 are polynomial-time (`PiecesF.Keeps`), by the time clauses of the
definition. 

### `to_par_one`

 Pieces with parameters (ρ, c) and c^row, c^col ≤ 2λ: the recursion has them with m = 1 and with
the same constant c. 
