---
{
  "module": "proof/consequences/CircuitLowerBound/Cert/TabF.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Cert/TabF.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Cert/TabF.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): the formulas are written out in polynomial time

`stCertTabF`: the formula of a table is written out in time polynomial in the table, L in unary, P
and a list that is at least as long as the formula has clauses. The two numbers of a table are
data in binary and occur in exponents, so the program cuts them off at L; where there is room
(`Fits`) this changes nothing.

`stFlip`: write a = `nu m` and L = 2^a. When `pos m` equals `top a`, which is 2^2^L, the formula of
the table `codeOf a`, cut off at L, has variables below 2^L, so all its 2^2^L assignments are tried
in time polynomial in m. 

 ### The table with its two numbers cut off 

### `clipE`

 The table with its two numbers cut off at L. 

### `clipE_eq`

 Where there is room, the cut-off changes nothing. 

### `clipE_polyT`

 The table, cut off, is polynomial-time. 

### `kb_clipE_unary`

 The first number of a table that is cut off at a number in unary is given in unary. 

### `lam_clipE_unary`

 The same for the second number. 

 ### One clause, for a table whose two numbers are given in unary 

### `size_le_self`

 A number has at most as many binary digits as its value. 

### `rb_unary`

 The number of bits for the place of a clause in the table is given in unary. 

### `tval_polyT`

 The time of a literal. 

### `qval_polyT`

 The position of a literal. 

### `bq_unary`

 The number of bits of a position is given in unary. 

### `nb_unary`

 The number of bits of the number of a clause is given in unary. 

### `litAt_polyT`

 A literal of the formula. 

### `clauseAt_polyT`

 A clause of the formula. 

 ### The formula 

### `G`

 The formula of a table, cut off by a pad, with the two numbers of the table cut off at L. 

### `G_polyT`

 The program is polynomial-time. 

### `G_eq`

 Where there is room and the pad is long enough, the program writes the formula of the table. 

 ### All assignments of a formula with few variables 

### `sat_iff_testBit`

 A formula with variables below M is satisfiable if and only if the binary digits of some number
below 2^M satisfy it. 

### `tryAll`

 «Some number below N satisfies φ», as a program. 

### `tryAll_iff`

 What the program decides. 

### `tryAll_polyT`

 Trying all numbers below a number in unary is polynomial-time. 

 ### Sizes when `pos m` equals `top (nu m)` 

### `two_pow_size_le`

 2 to the number of binary digits of n is at most 2n + 1. 

### `length_rest_le`

 The rest of a word is no longer than the word. 

### `length_tab_codeOf_le`

 The table with the number a has at most a clauses. 

### `two_pow_nb_le`

 Where there is room, the formula of a table has at most (2·(number of clauses of the table) + 1)·2^L
clauses. 

 ### The flip 

### `fb`

 The answer for m, given in unary: the table `codeOf (nu m)` fits, and some number below `pos m`
satisfies its formula, cut off at L. 

### `fb_polyT`

 The answer is computed in polynomial time. 

### `fb_iff`

 When `pos m` equals `top (nu m)`, the answer is right, given that the variables of the formula
of a table have L bits. 

### `stCertTabF`

 The formula of a table is written out in polynomial time. 

### `stFlip_of`

 When `pos m` equals `top (nu m)`, whether the table `codeOf (nu m)` fits and its formula, with L =
2^(nu m), is satisfiable is decided in time polynomial in m, given that the variables of a formula
of a table have L bits. 

### `stFlip`

 When `pos m` equals `top (nu m)`, whether the table `codeOf (nu m)` fits and its formula, with L =
2^(nu m), is satisfiable is decided in time polynomial in m. 
