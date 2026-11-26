---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/Memory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Memory.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Memory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 30 in the light language: the memory map and the invariant of the data structure

The data structure occupies one block of the memory, from a base address b0 on. First comes the
shared block of Section 2 (directory, tables, the encodings of all bands), and behind it the areas
of Section 4:

    WD (L) | CUR (L) | BOX (L) | SS (m) | FP (1) | ROOTS (nB²) | TR (cap)

WD holds the digits of the output string of a query; CUR, BOX and SS are scratch strings; FP holds
the length of the trie array; ROOTS holds the roots of the tries, that of tile (β, β') in the cell
β nB + β'; TR is the trie area. Cell 31 of the directory holds t. `Areas` says where the tables that
the routines of Section 4 read and the areas of Section 4 lie, and `areas` proves it.

Two routines know this map: preCore(L, m, t, N, D, aX, aY, b0) builds the block from the matrices at
aX and aY, which lie below b0, and queryAt(I, J, b0) answers a query from it. They are relocatable,
so that Theorem 30, its offline form and Corollary 26 use the same two routines. The main procedures
of Theorem 30's programs only read the sizes from the input and compute the addresses. For Corollary
26 a routine of its own stands in between: it finds m and, from the threshold of the proof on, L and
t, writes padded copies of the matrices, and runs `preCore` on them.

Section 4.3: "Our data structure consists of three components: the list of the K₀² subsets Q
assigned to the block products of a tile […], the encodings of all row bands and all column bands,
and for every tile, the values of all its boxes". In the invariant DSReady the field shared holds
the first two, and the fields roots and trie hold the third: "for each tile we store its boxes, with
their values, in a standard trie on their strings of L symbols". The tries of all tiles lie in one
array (trie), and the table roots has the root of the trie of each tile. The invariant depends only
on the cells from b0 on, without the scratch strings (`DSReady.congr`).


 ## The map 

### `aWD`

 The digits of the output string of a query: L cells. 

### `aCUR`

 Scratch of the preprocessing, the current leaf: L cells. 

### `aBOX`

 Scratch, the current box: L cells. 

### `aSS`

 Scratch of a query, the current string on the levels of Q: m cells. 

### `aFP`

 The cell that holds the length of the trie array. 

### `aROOTS`

 The roots of the tries: one cell for each tile. 

### `aTR`

 The trie area. 

### `trieCap`

 The capacity of the trie area (`Spec.length_allTries_le`). 

### `top`

 The first address behind the block (one cell is left unused, so that every address of the block
is strictly below it). 

 ## Where the areas lie 

### `Areas`

 What the routines of Section 4 need of the map: the tables that they read lie one behind the
other between the directory and WD, and the areas of Section 4 behind WD. 

### `areas`

 The tables and the areas lie as Areas says. 

### `wd_ge`

 The directory lies before the areas of Section 4. 

### `base_le_sharedEnd`

 The shared block ends behind its base address. 

### `base_add_lt_top`

 The block holds more than its directory. 

### `base_lt_top`

 The block is not empty. 

### `base_le_top`

 The block ends behind its base address. 

### `scratch_in_block`

 The scratch strings of a query lie in the block. 

 ## The directory 

### `levels`

 The cells of the directory, the first 32 cells of the block, that the routines of Section 4 use.
They hold L, m, L - m, K₀, nB, 10^L, the addresses of the tables MASK, BAND, BLOCK, DIG3 and of the
encodings ENCA, ENCB, the end of the shared block (which is the address of WD), and t. All but the
last are written by the shared stage. 

 ## The invariant 

### `encRow`

 The encoding of the row band β. 

### `encCol`

 The encoding of the column band β. 

### `dsTries`

 The tries of all tiles, and their roots. 

### `DSReady`

 **The block from b0 on holds the data structure for X and Y.** The preprocessing establishes
this, and every query needs it and keeps it. 

### `DSReady.congr`

 The invariant depends only on the cells from b0 on, without the scratch strings WD, CUR, BOX,
SS. 

### `DSReady.of_same`

 A memory that differs from one that holds the data structure only on the scratch strings WD,
CUR, BOX, SS holds it too. 

### `dsReady_congr`

 The invariant of the data structure only depends on the cells from b0 on. 

### `Lim30`

 The limits that the two routines need: U bounds the entries of X and Y. 

### `Lim30.value`

 Every value and every partial sum fits in a word. 

### `Lim30.enc`

 The shared stage can compute the encodings. 

### `Lim30.pow`

 The shared stage can compute the table of the powers of 10. 

 ## The two routines that know the map 

### `Proc.preCore`

 The numbers of the two routines. 

### `tQueryAt`

 The time of `queryAt`. 

### `tPreCore`

 The time of `preCore`; c is the constant of the shared stage (`Sec2.SharedSpec`). 

### `QueryAtSpec`

 queryAt(I, J, b0) returns (XY)[I, J] from the block at b0, of which it changes only cells of the
scratch strings WD to SS. 

### `PreCoreSpec`

 preCore(L, m, t, N, D, aX, aY, b0) builds the data structure for the matrices at aX and aY in
the block from b0 on. Nothing is assumed about the content of the block. 
