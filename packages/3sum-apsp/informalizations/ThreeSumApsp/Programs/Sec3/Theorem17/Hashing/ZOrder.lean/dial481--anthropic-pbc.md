---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/ZOrder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/ZOrder.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/ZOrder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Matrices over ℤ[x]/(x^p - 1) in Z-order: the table of places, and P and Q of Theorem 17's proof

spreadTable(dst, N2) writes the table of `spread`: the number with the binary digits of i, read in
base 4.  There is no division: a pointer j = ⌊i/2⌋ and the parity of i are carried along, and
dst[i] = 4 dst[j] + parity (`spreadStep_spec`, `spreadTable_spec`).

buildZ(dst, r, mort, n, N2, p, mx, my), with N2 = 2^K, writes an N2 × N2 matrix of vectors of length
p in Z-order, 4^K p cells in all, whose entry for the pair (x, y), x, y < n, is the unit vector with
its 1 at place r[x n + y], and whose other entries are zero vectors.  Here mort is the address of
the table that spreadTable has written, so that mort[x] = spread x.  The place of the pair (x, y) is
mx · spread x + my · spread y.  With (mx, my) = (2, 1) the pair is (row, column), which gives
"P[a,c] := x^{w(a,c) mod p}"; with (1, 2) it is (column, row), which gives
"Q[c,b] := x^{w(b,c) mod p}" from the residues of w(b,c) stored at b n + c.  (Inside the two quoted
formulas x is the paper's indeterminate, and P and Q are the paper's matrices; in the code `P` is
the program.)  The routine clears the matrix (`buildZClear_spec`) and marks one cell for each pair
(`buildZMark_spec`); `markList_eq_zList` identifies the marked list with the matrix.


 ## The table of places 

### `Dst`

 The local variables of spreadTable.  The arguments: Dst = dst, Rows = N2.  Then Idx = i;
Half = j = ⌊i/2⌋; Parity, the parity of i. 

### `spreadStep`

 dst[i] := 4 dst[j] + parity; then i, j and the parity go on to i + 1. 

### `spreadTableBody`

 spreadTable(dst, N2). 

### `spreadStep_spec`

 **One entry of the table.** 

### `spreadTable_spec`

 **spreadTable**: at most 30 N2 + 17 steps. 

### `spreadTable_meets`

 **spreadTable** as a procedure. 

 ## The matrices 

### `Dst`

 The local variables of buildZ.  The arguments: Dst = dst, Residues = r, Places = mort, Num = n,
Rows = N2, Prime = p, MulX = mx, MulY = my.  Then Ptr, the first cell that is still to be cleared;
Stop, the end of the matrix; Square = n²; Idx = t = x n + y, the number of the pair; Row = x;
Col = y. 

### `buildZClear`

 The N2 N2 p cells of the matrix are cleared. 

### `buildZMark`

 The pair (x, y) marks its cell: dst[(mx mort[x] + my mort[y]) p + r[t]] := 1. 

### `buildZBody`

 buildZ(dst, r, mort, n, N2, p, mx, my). 

### `buildZTime`

 An upper bound on the number of steps of buildZ. 

### `BuildZPre`

 What buildZ needs: where the arrays lie, and what they hold.  The matrix has N2 = 2^K rows and
columns, so 4^K entries of p cells each, and R is the list of the n² residues that stand at r. 

 ### The pure side: a list of zeros in which places are marked one after the other 

### `markList`

 The list of `len` zeros in which the places `idx 0, …, idx (t - 1)` have been set to 1. 

### `getD_markList`

 An entry of the list is 1 if its place has been marked, and 0 if not. 

### `length_unitOrZero`

 A unit vector and the zero vector have p entries. 

### `markList_eq_zList`

 **A matrix of unit vectors, by marking.**  The pairs are numbered by `t < m`; pair number `t`
stands in row `ρ t` and column `κ t`, and `τ` gives the number of the pair in a row and a column. 

### `markList_eq_matPList`

 The first matrix of the proof of Theorem 17, P, by marking. 

### `markList_eq_matQList`

 The second matrix of the proof of Theorem 17, Q, by marking. 

 ### The program 

### `readR`

 The residues lie outside the matrix, so they can be read at any time. 

### `readM`

 The table of places lies outside the matrix, so it can be read at any time. 

### `buildZClear_spec`

 **The matrix is cleared.** 

### `buildZMark_spec`

 **The pair number t marks its cell.** 

### `buildZ_spec`

 **buildZ**, for any two multipliers that keep the places inside the matrix. 

### `buildZ_P_spec`

 **buildZ with (mx, my) = (2, 1)**: the matrix P of the proof of Theorem 17 (not the program
`P`). 

### `buildZ_Q_spec`

 **buildZ with (mx, my) = (1, 2)**: the matrix Q of the proof of Theorem 17. 

### `buildZ_P_meets`

 **buildZ** as a procedure, for the matrix P. 

### `buildZ_Q_meets`

 **buildZ** as a procedure, for the matrix Q. 

 ## The matrices P and Q as lists 

### `length_matPList`

 The matrix P has 4^K vectors of p numbers. 

### `length_matQList`

 The matrix Q has 4^K vectors of p numbers. 

### `absLe_unitOrZero`

 The entries of a unit vector and of the zero vector are 0 or 1. 

### `absLe_zList_unit`

 The entries of a matrix of unit vectors and zero vectors are 0 or 1. 

### `absLe_matPList`

 The entries of P are 0 or 1. 

### `absLe_matQList`

 The entries of Q are 0 or 1. 
