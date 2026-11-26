---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21b/Apsp/Passes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/Apsp/Passes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/Apsp/Passes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# APSP by repeated squaring: the three passes over the matrix

For Theorem 21(b).  The host for APSP keeps the current matrix as a list of
`n²` integers, in which a large number `INF` stands for `+∞`.  This file has its three simple
passes, each with its specification (`clip_meets`, `apInit_meets`, `apOut_meets`).

* clip(len, thr, INF, src, dst) copies `len` cells from `src` to `dst` and replaces every number
  above `thr` by `INF`.
* apInit(n, INF, adj, w, A) writes the weight matrix of the graph to `A`: 0 on the diagonal, the
  weight where there is an edge, `INF` elsewhere.
* apOut(len, INF, A, out) writes two cells for each cell of `A`: (0, 0) for `INF`, and (1, x) for
  any other number `x`.

In each proof the memory after j rounds is written down (`wrote`, `zeroedDiag`), one lemma says what
a round does to the state, and the loop rule does the rest.


 ## clip 

### `Len`

 The number of cells. 

### `Thresh`

 The threshold. 

### `Big`

 The number that stands for +∞. 

### `Src`

 The address of the source. 

### `Dst`

 The address of the destination. 

### `Idx`

 The counter q. 

### `clipBody`

 clip(len, thr, INF, src, dst): for q < len, dst[q] := INF if src[q] > thr, and src[q]
otherwise. 

### `clip_meets`

 **clip** writes the clipped list to dst, changes nothing else, and takes at most 23 len + 6
steps. 

 ## apInit 

### `Verts`

 The number n of vertices. 

### `Big`

 The number that stands for +∞. 

### `AdjAt`

 The address of the adjacency matrix. 

### `WtsAt`

 The address of the weights. 

### `Mat`

 The address of A. 

### `Idx`

 The counter of both passes. 

### `Cells`

 n², in the first pass. 

### `Diag`

 The address of the diagonal cell, in the second pass. 

### `apInitFill`

 The round of the first pass: A[q] := w[q] if adj[q] = 1, and INF otherwise. 

### `apInitDiag`

 The round of the second pass: the diagonal cell becomes 0; the next one is n + 1 cells on. 

### `apInitBody`

 apInit(n, INF, adj, w, A): the first pass fills the n² cells of A, the second pass puts 0 on the
diagonal. 

### `apInitCell`

 The entry number q of the weight matrix, the diagonal apart. 

### `zeroedDiag`

 The memory μ after the first j diagonal cells of the matrix at A have become 0. 

### `zeroedDiag_succ`

 What round j of the second pass writes. 

### `seg_zeroedDiag_wrote`

 After both passes the weight matrix stands at A. 

### `sameOutside_zeroedDiag`

 Both passes change the n² cells of A only. 

### `ApInitInv`

 The invariant of the second pass of apInit before round j; μ is the memory after the first
pass. 

### `apInitFill_spec`

 **One round of the first pass of apInit**, for the cells adj[j] = x and w[j] = y: the weight y
where there is an edge, and INF where there is none. 

### `apInitDiag_spec`

 **One round of the second pass of apInit**, for the address o of the diagonal cell.  The next
address o + n + 1 is computed also in the last round, so it has to fit. 

### `apInit_meets`

 **apInit** writes the weight matrix to A, changes nothing else, and takes at most
23 n² + 17 n + 18 steps.  Only n² cells are written; the space 2 n² is asked for because after the
last round of the second pass the local Diag holds A + n (n + 1), which has to fit. 

 ## apOut 

### `Len`

 The number of cells of A. 

### `Big`

 The number that stands for +∞. 

### `Mat`

 The address of A. 

### `Out`

 The address of the output. 

### `Idx`

 The counter q. 

### `Pos`

 The address out + 2q. 

### `apOutWrite`

 The two cells of the output for the cell A[q]. 

### `apOutRound`

 The round of apOut for the cell A[q]. 

### `apOutBody`

 apOut(len, INF, A, out): for q < len, the cells out[2q], out[2q + 1] become 0, 0 if A[q] = INF,
and 1, A[q] otherwise. 

### `apOutCell`

 Cell number c of the output: cells 2q and 2q + 1 are 0, 0 if L[q] = INF, and 1, L[q]
otherwise. 

### `wrote_apOutCell_succ`

 What round q writes. 

### `ApOutInv`

 The invariant of the loop of apOut before round j. 

### `apOutWrite_spec`

 **The two stores of a round of apOut**, for the cell A[j] = x and the address o of the output.


### `apOutRound_spec`

 **One round of apOut** writes the pair for the cell A[j] and moves Pos on by two. 

### `PairsAt`

 What apOut leaves from the address `out` on: for each number of the list `L` a pair of cells.
Its first cell holds 0 if the number is `INF`; otherwise the pair holds 1 and the number. 

### `apOut_meets`

 **apOut** writes the pairs to out, changes nothing else, and takes at most 30 len + 8 steps. 
