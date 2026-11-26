---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem19/Graphs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem19/Graphs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem19/Graphs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Exact Triangle on n-vertex graphs, from the tripartite form

Section 3.2: "an instance on an arbitrary n-vertex graph reduces to this form
by taking three copies of the vertex set and giving every missing edge the weight 3n^ν + 1, which
lies in no zero triangle". The host writes one n × n array, with the weight of an edge where there
is an edge and 3U + 1 where there is none, at the free pointer, and calls a solver of Exact Triangle
with this array as each of the three matrices of weights.

The route: how a cell of the new array is computed (`GrInst.getD_Z`); three copies of the array are
the tripartite instance of Section 3.2 (`GrInst.triOf_Z`, `GrInst.tri_pre`); one round of the loop
(`graphEtFill_spec`); the host (`graphEt_spec`); the result (`isHost_graphEt`).  The prefix graphEt
stands for Exact Triangle on graphs.


 ## The task 

### `GrInst`

 A graph on n vertices with weights on its edges, and the addresses of its adjacency matrix and
of the matrix of the weights. 

### `GrInst.ADJ`

 The adjacency matrix, row by row: 1 for an edge, 0 for none. 

### `GrInst.W`

 The weights, row by row: 0 where there is no edge. 

### `GrInst.Pre`

 The two matrices lie below the free pointer, and the weights of the edges are bounded by U. 

### `graphEtTask`

 **Exact Triangle on n-vertex graphs**: get(n, U, adj, w, fr) returns 1 if three pairwise
adjacent vertices have edge weights that sum to zero, and 0 if not. 

 ## The pure side 

### `exists_fin_index`

 Every index below n · m is the index of a pair. 

### `GrInst.Z`

 The weights of the tripartite instance, row by row. 

### `GrInst.getD_Z`

 How a cell of the new array is computed from the cells of the two given ones. 

### `GrInst.triOf_Z`

 The instance that is read from three copies of the new array is the tripartite instance of
Section 3.2. 

 ## The host 

### `Verts`

 The number n of vertices. 

### `Bound`

 The bound U on the weights. 

### `AdjAt`

 The address of the adjacency matrix. 

### `WtsAt`

 The address of the weights. 

### `Free`

 The free pointer, where the new array is written. 

### `Cells`

 n². 

### `Big`

 The weight 3U + 1 of a missing edge. 

### `Idx`

 The counter q. 

### `graphEtFill`

 The round for the cell number q: the weight of the edge, or 3U + 1 if there is none. 

### `graphEtBody`

 get(n, U, adj, w, fr), Exact Triangle on a graph: the array of the weights of the tripartite
instance is written at the free pointer, and the solver is called with it as each of the three
matrices. 

### `graphEtTime`

 The time of the host: n² cells are written, and the solver runs with the bound 3U + 1. 

### `graphEtNeed`

 The need of the host: n² cells more than the solver, one level of calls more. 

### `GrInst.tri`

 The tripartite instance, with the new array as each of its three matrices. 

### `GrInst.tri_pre`

 The tripartite instance is as the task Exact Triangle prescribes. 

### `graphEtFill_spec`

 **One round of the loop of get**, for the cells adj[j] = a and w[j] = b. 

### `FillInv`

 The invariant of the loop of get: the first j cells at the free pointer hold the weights of the
tripartite instance, and no other cell has changed. 

### `graphEt_spec`

 **The host is correct.** 

### `polyNeed_graphEtNeed`

 The need of the host is polynomially bounded if the need of the solver is. 

### `isHost_graphEt`

 **Exact Triangle on n-vertex graphs from the tripartite form**: the host makes a solver for
graphs from every solver of Exact Triangle. 
