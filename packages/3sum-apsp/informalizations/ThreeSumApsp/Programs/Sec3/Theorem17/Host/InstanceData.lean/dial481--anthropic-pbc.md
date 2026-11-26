---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Host/InstanceData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/InstanceData.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/InstanceData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The host of Theorem 17: the list of its instances, as pure data

Proof of Theorem 17, "For each chunk 𝒬 ⊆ W_ϱ and each piece C_k form the instance".  After the prime
has been chosen, the host runs one loop over all instances: instance number `t` belongs to the piece
number `t / chunkCount` of `C` and to the chunk number `t % chunkCount` of the table of chunks.
This file defines what the host writes (`matX`, `matY`, `WI`, `WJ`), what the solver answers
(`ans`), which query pairs are accepted and which scans succeed (`acc`, `hit`), and whether a zero
triangle has been found before instance `t` (`found`).  The class of a residue `ϱ < p` is the
paper's `W_ϱ`: the pairs `(a, b)` whose weight is congruent to `ϱ` modulo `p`.  The pairs are listed
class after class, in the order of the residues, and a chunk is a segment of a class.


### `BigCase`

 The hypotheses of Theorem 17 on its parameters, in natural numbers: "Let 16 ≤ D ≤ n, and let
1 ≤ g ≤ √D be an integer." 

### `HostData`

 The data on which the loop over the instances depends. 

### `HostData.n`

 The number of vertices of each part. 

### `HostData.D`

 The bound on the number of middle vertices of an instance of Lop-AE-SparseTri, that is, the
  inner dimension of its matrices `X` and `Y`. 

### `HostData.p`

 The prime. 

### `HostData.q`

 The number of vertices of a piece of `C`. 

### `HostData.cap`

 The largest number of query pairs of an instance. 

### `HostData.AB`

 The weights of the edges `(a, b)`, row by row. 

### `HostData.BC`

 The weights of the edges `(b, c)`, row by row. 

### `HostData.AC`

 The weights of the edges `(a, c)`, row by row. 

### `RAB`

 The residues modulo `p` of the weights of the edges `(a, b)`. 

### `RBC`

 The residues modulo `p` of the weights of the edges `(b, c)`. 

### `RAC`

 The residues modulo `p` of the weights of the edges `(a, c)`. 

### `QI`

 The rows `a` of all pairs `(a, b)`, class after class. 

### `QJ`

 The columns `b` of all pairs `(a, b)`, class after class. 

### `CT`

 The table of the chunks. 

### `chunkCount`

 The number of chunks. 

### `h`

 The number of pieces. 

### `m`

 The number of instances. 

### `c0`

 The first vertex of the piece of instance t. 

### `len`

 The number of vertices of the piece of instance t. 

### `chunk`

 The chunk of instance t. 

### `rho`

 The residue `ϱ` of the chunk of instance t. 

### `lo`

 The first place of the chunk of instance t in the list of all pairs. 

### `w`

 The number of query pairs of instance t. 

### `matX`

 The matrix `X` of instance t. 

### `matY`

 The matrix `Y` of instance t. 

### `WI`

 The rows of the query pairs of instance t. 

### `WJ`

 The columns of the query pairs of instance t. 

### `ans`

 The answers of a solver of Lop-AE-SparseTri to instance t. 

### `acc`

 The query pair number i of instance t is accepted. 

### `hit`

 The scan for the query pair number i of instance t succeeds. 

### `found`

 A zero triangle has been found before instance t. 

### `execs`

 The number of scans made for instance t. 

### `fails`

 The number of accepted query pairs of instance t whose scan fails or would fail. 
