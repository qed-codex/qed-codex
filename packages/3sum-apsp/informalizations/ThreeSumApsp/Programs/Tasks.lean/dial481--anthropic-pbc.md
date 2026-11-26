---
{
  "module": "ThreeSumApsp/Programs/Tasks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Tasks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Tasks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The problems of the paper as tasks

* The problems for Section 3.4 have a size and a bound (`Task`).
* The problems of Theorem 5 and of Section 3.1 have the parameters `N`, `D`, `w` and `U` (`TaskN`).
  The calling convention is the same: sizes, the bound, the addresses of the arrays, the address of
  the output, and the free pointer last.  The three tasks: the wanted entries of a thin matrix
  product (`thinTask`; Theorem 5 and Corollary 26), #Lop-AE-SparseTri (`lopCountTask`;
  Definition 14) and Lop-AE-SparseTri (`lopDetectTask`; Definition 13).  All three have the same
  instances (`ThinInst`).
* What "solved in time `T`" means for them: `ThinSolvedIn`, `LopSolvedIn`.


 ## The problems for Section 3.4 

### `TriInst`

 Three `n × n` matrices of weights in the memory. 

### `TriInst.Pre`

 The three matrices lie below the free pointer, and their entries are bounded by `U`. 

### `TriInst.Pre.keep`

 An instance stays where it is if no cell below the free pointer changes. 

### `TriInst.Pre.mono`

 The free pointer may grow. 

### `triPre_of_arrays`

 Three matrices one after the other, with the free pointer behind them, are an instance. 

### `etTask`

 **Exact Triangle**: et(n, U, ab, bc, ac, fr) returns 1 if there is a zero triangle and 0 if not.


### `ntTask`

 **Negative Triangle**: nt(n, U, ab, bc, ac, fr) returns 1 if there is a negative triangle and 0
if not. 

### `VecInst`

 A list of `N` numbers in the memory. 

### `VecInst.Pre`

 The list lies below the free pointer, and its entries are bounded by `U`. 

### `c3Task`

 **Convolution-3SUM**: c3(N, U, x, fr) returns 1 if `x_i + x_j = x_{i+j}` for some `i`, `j`, and
0 if not. 

### `s3Task`

 **3SUM**: s3(n, U, x, fr) returns 1 if three of the numbers, at different positions, sum to 0,
and 0 if not. 

### `MatInst`

 Two `n × n` matrices in the memory, and the place for a third. 

### `MatInst.Pre`

 The two matrices and the place for the product lie below the free pointer; the place for the
product does not meet the two matrices. 

### `mpTask`

 **The (min,+)-product**: mp(n, U, a, b, c, fr) writes the product of the matrices at `a` and `b`
to `c`. 

### `GraphInst`

 A directed graph in the memory: adjacency matrix and weights, and the place for the `2n²` cells
of the answer. 

### `GraphInst.Pre`

 The graph and the place for the answer lie below the free pointer; the graph has no negative
cycle. 

### `apTask`

 **APSP**: ap(n, U, adj, w, out, fr) writes two cells for each pair `(i, j)`, at
`out + 2 (i n + j)`: 1 and the distance from `i` to `j` if `j` can be reached from `i`, and 0 in the
first cell if not. 

 ## The thin matrix product and the lopsided triangle problems 

### `ThinInst`

 Matrices `X` (`N × D`) and `Y` (`D × N`), row by row, `w` wanted positions (rows in `WI`,
columns in `WJ`), and the place for `w` answers. 

### `ThinInst.N`

 The number of rows of `X` and of columns of `Y`. 

### `ThinInst.D`

 The number of columns of `X` and of rows of `Y`. 

### `ThinInst.w`

 The number of wanted positions. 

### `ThinInst.U`

 The bound on the absolute values of the entries. 

### `ThinInst.x`

 The address of `X`. 

### `ThinInst.y`

 The address of `Y`. 

### `ThinInst.wi`

 The address of `WI`. 

### `ThinInst.wj`

 The address of `WJ`. 

### `ThinInst.out`

 The address of the answers. 

### `ThinInst.X`

 The first matrix, row by row. 

### `ThinInst.Y`

 The second matrix, row by row. 

### `ThinInst.WI`

 The rows of the wanted positions. 

### `ThinInst.WJ`

 The columns of the wanted positions. 

### `ThinInst.Pre`

 Everything lies below the free pointer, the entries are bounded by `U`, the positions are
distinct positions of an `N × N` matrix, and the place for the answers meets none of the inputs. 

 The ten arguments of a procedure for one of these tasks, as local variables. 

### `Rows`

 N. 

### `Cols`

 D. 

### `Wanted`

 The number w of wanted positions. 

### `Bound`

 The bound U on the entries. 

### `AdrX`

 The address of X. 

### `AdrY`

 The address of Y. 

### `AdrWI`

 The address of the rows of the wanted positions. 

### `AdrWJ`

 The address of their columns. 

### `AdrOut`

 The address of the output. 

### `Free`

 The free pointer. 

### `ThinInst.ZeroOne`

 The entries of both matrices are 0 or 1. 

### `thinEntry`

 The entry `(XY)[I, J]`. 

### `thinOut`

 The wanted entries, in the order of the positions. 

### `thinTask`

 **The wanted entries of a thin matrix product** (Theorem 5, Corollary 26):
`thin(N, D, w, U, x, y, wi, wj, out, fr)`. 

### `lopCountTask`

 **#Lop-AE-SparseTri** (Definition 14), the graph given by its two biadjacency matrices: the same
call with `U = 1` on matrices of zeros and ones; the answers are the numbers of common
neighbours. 

### `lopDetectTask`

 **Lop-AE-SparseTri** (Definition 13): the answer is 1 if the pair has a common neighbour and 0
if not. 

### `ThinSolvedIn`

 "The thin matrix product is solved in time `T N D w' u`", where `w'` is an upper bound on the
number `w` of wanted positions and `u` one on the bound `U`. 

### `LopSolvedIn`

 "The task (one of the two lopsided triangle problems) is solved in time `T n D w'`", where `w'`
is an upper bound on the number `w` of query pairs. 
