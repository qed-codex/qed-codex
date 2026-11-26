---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Encode/BandArrayFacts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Encode/BandArrayFacts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Encode/BandArrayFacts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The input array of a band: what the loops compute

The input array of a band (Sections 2.3.3 and 2.3.4) holds entries of the matrix at the codes of
certain strings and 0 elsewhere.  The table of subsets lists subsets of size m of the L levels:
`Spec.unrank L m s` is the mask of subset number s, and the block product (g, h) of a tile uses
subset number g K₀ + h.  No program text occurs here.  `BandArgs` collects the arguments of
bandArray: the number of a row, the address of a mask and the code of a string are functions of
them.

* The code of a left or right string is computed level by level: `codeUpTo` is the code of the first
  l levels.  One more level appends the next outer digit, or 3 plus the next inner digit
  (`codeUpTo_succ`), and after all levels the code is `Spec.gluedCode` (`codeUpTo_unrank`).
* The numbers that occur are small (`BandArgs.rowNo_lt`, `subsetIndex_lt`, `BandArgs.code_lt`).
* The array is filled in the order of the tuples (g, h, r, k), not of the codes.  `OverwrittenWith`
  says of two memories that cells of the array were overwritten only with the entries of the target
  list, so that a cell that is right stays right.


 ## The code of a string, level by level 

### `codeUpTo`

 The code of the first l levels: Horner's rule in base 7 on the outer digits o and 3 plus the
inner digits i, interleaved along the mask bs. 

### `codeUpTo_succ`

 One more level. 

### `codeUpTo_lt`

 The code of l levels is below 7^l. 

### `codeUpTo_unrank`

 On the mask of a subset of the table and the digits of a row and a column, the code of all
levels is `Spec.gluedCode`. 

 ## Sizes 

### `bandSize_le`

 A band has at most 7^L rows. 

### `BandArgs`

 The arguments of bandArray. 

### `BandArgs.p`

 The parameters L, m, N. 

### `BandArgs.β`

 The number of the band. 

### `BandArgs.side`

 0 for a row band of X, 1 for a column band of Y. 

### `BandArgs.aA`

 The address of the matrix. 

### `BandArgs.sI`

 The step from a row (of X, or column of Y) to the next. 

### `BandArgs.sK`

 The step from a column of X (or row of Y) to the next. 

### `BandArgs.mask`

 The address of the table of subsets. 

### `BandArgs.dig3`

 The address of the table of digits in base 3. 

### `BandArgs.dig4`

 The address of the table of digits in base 4. 

### `BandArgs.arr`

 The address of the array. 

### `blockNo`

 The number of the block of rows of the matrix `X` (`side = 0`), or of columns of the matrix `Y`
(any other side), for the block product `(g, h)`. 

### `rowNo`

 The number of the row of `X` (or column of `Y`) for the block product `(g, h)` and the row `r`
of the block. 

### `maskRow`

 The address of the mask of the subset of the block product `(g, h)`. 

### `code`

 The code of the string for the block product `(g, h)`, the row `r` and the column `k`. 

### `code_lt`

 A code is below `7^L`. 

### `rowNo_lt`

 The numbers of the rows, and of the blocks, of the padded matrix stay small. 

### `rowNo_mod`

 The offset of a row in its block. 

### `subsetIndex_lt`

 g K₀ + h is the number of a subset of the table. 

### `Par.sizes_le_S7`

 `binom(L, m)`, `K₀`, `N₀` and `L` are at most `7^L`. 

 ## Overwriting with the entries of a target list 

### `OverwrittenWith`

 The memory μ' agrees with μ outside the n cells from arr, and each of these cells holds what it
held in μ or the entry of the target T. 

### `OverwrittenWith.refl`

 Nothing has been written. 

### `OverwrittenWith.trans`

 First some writes, then more. 

### `OverwrittenWith.write`

 One write of an entry of the target. 

### `OverwrittenWith.keep`

 A cell that is right stays right. 
