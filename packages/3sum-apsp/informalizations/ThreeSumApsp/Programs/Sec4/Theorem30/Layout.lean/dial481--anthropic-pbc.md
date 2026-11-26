---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/Layout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Layout.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Layout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 30 on the word RAM: the two main procedures for the trusted layout

The trusted layout of the input, the one in the statement of the theorem (`ThinPair.input`), is N,
D, m, L, t, X, Y (`Layout`, `layout_input`). The main procedure of the preprocessing reads the sizes
and calls preCore with the block of the data structure right behind the input (`preMain_meets`); the
main procedure of a query reads N and D, computes the address of the block and calls queryAt
(`queryMain_meets`); between them the memory satisfies `DS`. `Meets.main` and
`AnswersQueries.of_meets` pass from the procedures to the outermost statement.

Time, space and the nesting of calls are within a constant times the expressions of the theorem
(`exists_bounds30`, from `exists_tPreCore_le`, `exists_tQueryAt_le`, `exists_top_sub_le`), the
limits `lim30` suffice and are polynomial in N (`lim30_ok`, `small_lim30`), and the numbers of the
input fit in a word (`abs_input_le`). This makes the light program a data structure (`top30`). The
compiler (`isDataStructure_of_program_scaled`) then gives Items.Theorem_30 for every program that
holds the two main procedures at their numbers and meets the specifications of preCore and queryAt
(`theorem_30_of`).


### `Ans`

 The locals of the two main procedures: the answer, which in a query is at first the row I, and
the column J; then N, D, the product N D, and in preMain the address of Y.  The last local is the
address of the block. 

### `preMainBody`

 preMain (its two arguments are not used): read the sizes, compute the two addresses, call
preCore. 

### `queryMainBody`

 queryMain(I, J): read the sizes, compute the address of the block, call queryAt. 

### `blockBase`

 The base address of the block of the data structure: the length of the input. 

### `Layout`

 The memory holds the input of the preprocessing, with D = 4^m, from cell 0 on. 

### `DS`

 **The memory holds the data structure for X and Y**: the two sizes that a query reads, and the
block behind the input. 

### `preMain_meets`

 **The main procedure of the preprocessing** builds the data structure behind the input. 

### `queryMain_meets`

 **The main procedure of a query** returns the entry and keeps the data structure. 

### `layout_input`

 The trusted input of the preprocessing, with D = 4^m, is laid out as preMain expects. 

### `abs_input_le`

 **The numbers of the input fit in a word** of the limits of Theorem 30, if the block starts
behind them. 

### `b0_le`

 **The block** starts at an address that is polynomial in N. 

### `Bounds30`

 The time of the two main procedures, the length of the block and the nesting of calls are at
most C times the expressions of Theorem 30. 

### `exists_bounds30`

 **Time and space** are within a constant times the expressions of Theorem 30. 

### `top30`

 **Theorem 30 as a light program.** c0 is the constant of the shared stage, c the exponent of the
bound N^c on the entries. 

### `theorem_30_of`

 **Theorem 30 on the word RAM**, for any program that holds the routines. 
