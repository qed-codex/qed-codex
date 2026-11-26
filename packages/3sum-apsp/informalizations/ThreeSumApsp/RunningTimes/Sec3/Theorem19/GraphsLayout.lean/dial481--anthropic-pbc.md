---
{
  "module": "ThreeSumApsp/RunningTimes/Sec3/Theorem19/GraphsLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem19/GraphsLayout.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem19/GraphsLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Exact Triangle on n-vertex graphs on the word RAM

Theorem 2, first line: "Exact Triangle on n-vertex graphs in O(n^{2.9983}) time".

The input is n in cell 0, the adjacency matrix from cell 1 and the weights from cell 1 + n²; the
free pointer is 1 + 2n² (`graphInst`).  The input meets the precondition of the task `graphEtTask`
(`pre_graph`), so a solver of the task gives a program for the layout of the end statement
(`wrapGraph`).

The task is solved by the host that turns a graph into a tripartite instance (`isHost_graphEt`): the
weights grow from U to 3U + 1, and the host writes n² cells.  So its time is `graphTime T`, if T is
the time for the tripartite form (`solvedIn_graphEtTask`).  For U = n^κ and n ≥ 2 the new bound is
at most n^(κ + 2), so a bound O(n^a) with a ≥ 2 for the tripartite form, for every exponent, gives
the same bound for n-vertex graphs (`solvedInTime_graphs`).


 ## The layout of the end statement 

### `weight_mem_input`

 The weight of an edge is one of the numbers of the input. 

### `graphInst`

 The instance of the task: where the two matrices stand. 

### `pre_graph`

 The input of the end statement meets the precondition of the task. 

### `wrapGraph`

 What connects Exact Triangle on n-vertex graphs in the layout of the end statement with the
task. 

 ## The running time 

### `graphTime`

 The time for n-vertex graphs, if T is the time for the tripartite form: the host writes n²
cells, and the bound on the weights grows from u to 3u + 1, which is at most u n² for n ≥ 2. 

### `solvedIn_graphEtTask`

 The task for n-vertex graphs is solved in time `graphTime T`. 

### `solvedInTime_graphs`

 A bound O(n^a), a ≥ 2, for the tripartite form of Exact Triangle gives the same bound for
n-vertex graphs on the word RAM. 

### `Theorem2.graphs_of`

 **Theorem 2**, first line, as printed: "Exact Triangle on n-vertex graphs in
O(n^{2.9983}) time", from the bound for the tripartite form. 
