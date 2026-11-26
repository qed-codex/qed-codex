---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Host/Loop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/Loop.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/Loop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The host of Theorem 17: the loop over the instances

Proof of Theorem 17.  After the prime has been chosen and the query pairs have been sorted into
classes and cut into chunks, the host runs through all instances: instance number t belongs to the
piece number t / chunkCount of the third part of the vertices and to the chunk number t % chunkCount
of the table of chunks.  For each instance it writes the two biadjacency matrices, calls the solver
of Lop-AE-SparseTri on the chunk (a segment of the sorted arrays of query pairs, so nothing is
copied), and scans the piece for every accepted query pair, as long as no zero triangle has been
found.

The solver is arbitrary.  The facts about the data that the loop relies on are collected in the
structure `HostOk`.

* What the four calls assume is proved without any program: `HostSetting.writeX`,
  `HostSetting.writeY`, `HostSetting.solver`, `HostSetting.weights`, `HostSetting.answers`.
* The program has one lemma for each part of a round: `hostParams_spec` (the parameters of the
  instance), `hostCalls_spec` (the four calls) and `hostNext_spec` (the counters).
  `hostRound_spec` puts them together, and `hostLoop_spec` is the loop: hostLoop returns 1 if a scan
  has found a zero triangle (`X.found X.m`) and 0 if not, changes no cell below x, and takes at most
  `tHostLoop` steps, the sum over the instances of the times of the four calls.


 ## The procedure 

### `Size`

 The number n of vertices of a part. 

### `ParD`

 The inner dimension D. 

### `ThePrime`

 The prime p. 

### `PieceLen`

 The number q of vertices of a piece. 

### `NumChunks`

 The number chunkCount of chunks. 

### `NumInst`

 The number m of instances. 

### `AdrAB`

 The weights w(a,b). 

### `AdrBC`

 The weights w(b,c). 

### `AdrAC`

 The weights w(a,c). 

### `ResAC`

 The residues of the weights w(a,c). 

### `ResBC`

 The residues of the weights w(b,c). 

### `Rows`

 The rows of the sorted query pairs. 

### `Cols`

 The columns of the sorted query pairs. 

### `TabR`

 The classes of the chunks. 

### `TabL`

 The first places of the chunks. 

### `TabW`

 The numbers of query pairs of the chunks. 

### `MatX`

 The matrix X. 

### `MatY`

 The matrix Y. 

### `AdrOut`

 The answers of the solver. 

### `SolverFree`

 The free pointer. 

### `Inst`

 The number t of the instance. 

### `ChunkNo`

 The number ch of its chunk. 

### `PieceStart`

 The first vertex c0 of its piece. 

### `Found`

 1 if a zero triangle has been found. 

### `Len`

 The number len of vertices of the piece. 

### `Residue`

 The class rho of the chunk. 

### `Start`

 The first place lo of the chunk. 

### `NumPairs`

 The number w of query pairs of the chunk. 

### `Unused`

 Results that are not used. 

### `hostCalls`

 The four calls for one instance: the two matrices, the solver, the scans. 

### `hostNext`

 The numbers of the next instance, of its chunk, and the first vertex of its piece. 

### `hostParams`

 The parameters of the instance: the number of vertices of its piece, and the class, the first
place and the number of query pairs of its chunk. 

### `hostRound`

 One round of hostLoop. 

### `hostLoopBody`

 hostLoop(n, D, p, q, chunkCount, m, ab, bc, ac, rac, rbc, qi, qj, cr, cl, cw, x, y, out, fr). 

### `tWrites`

 The time for writing the two matrices of an instance whose piece has len vertices, with the
calls and the bookkeeping of a round. 

### `tHostLoop`

 The number of steps of hostLoop, if the solver takes Tn. 

 ## What the loop relies on 

### `HostOk`

 The facts about the data that the loop relies on; U is a bound on the weights. 

### `HostAddr`

 The addresses of the arrays. 

### `HostMem`

 What the memory holds: the weights, the residues of w(a,c) and w(b,c), the sorted query pairs,
and the three components of the table of chunks. 

### `HostLay`

 Where the arrays lie: everything that is read lies below x; then come the two matrices, the
answers, and the free pointer. 

### `HostLim`

 What the limits have to allow for; need is the need of the solver. 

### `HostCtx`

 The context of hostLoop: a solver of Lop-AE-SparseTri, and the procedures writeX, writeY,
scanPairs, scan in the program. 

### `hostLoopArgs`

 The arguments of hostLoop. 

 ## What the calls assume 

### `HostSetting`

 Everything that hostLoop assumes, and a memory μ' that agrees with the first memory μ below
x. 

### `absLe_one_of_zero_or_one`

 Entries 0 and 1 have absolute value at most 1. 

### `places`

 The order of the regions of the memory, the limits, and the sizes of instance t. 

### `next`

 A later memory that agrees with μ' below x. 

### `length_RAC`

 There are `n²` residues of the weights `w(a,c)`. 

### `length_RBC`

 There are `n²` residues of the weights `w(b,c)`. 

### `mem'`

 What the loop reads stands in μ' as it stood in μ. 

### `read_tab`

 Reading an entry of a component of the table of chunks. 

### `read_chunk`

 The three parameters of the chunk of instance t, in the memory. 

### `write`

 What writeX and writeY assume, for a matrix of size cells at dst and the residues of a list of
weights at r. 

### `writeX`

 The precondition of writeX holds. 

### `writeY`

 The precondition of writeY holds. 

### `inst`

 The instance number t, as the solver gets it. 

### `solver`

 The precondition of the solver holds, once the two matrices are written. 

### `weights`

 The weights are where the scans read them. 

### `answers`

 The answers of the solver and the query pairs of the chunk are where the scans read them. 

 ## The parts of a round 

### `hostState`

 The state of hostLoop: the arguments, the numbers t, ch and c0 of the instance, and what the
locals Found, Len, Residue, Start, NumPairs and Unused hold. 

### `hostParams_spec`

 **The parameters of instance t.** 

### `tCalls`

 The time of the four calls. 

### `HostCtx.writeX_meets`

 The call of writeX for instance t. 

### `HostCtx.writeY_meets`

 The call of writeY for instance t. 

### `HostCtx.solver_meets`

 The call of the solver for instance t, once the two matrices are written. 

### `HostCtx.scanPairs_meets`

 The call of scanPairs for instance t, once the solver has answered. 

### `hostCalls_spec`

 **The four calls for instance t.** 

### `hostNext_spec`

 **The counters**: from instance t to instance t + 1. 

 ## The loop 

### `HostInv`

 The invariant of the loop, before instance t. 

### `hostRound_spec`

 **One round of the loop.** 

### `hostLoop_spec`

 **hostLoop** returns 1 if a scan has found a zero triangle, and 0 if not, and changes no cell
below x. 
