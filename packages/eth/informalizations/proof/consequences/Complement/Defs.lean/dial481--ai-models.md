---
{
  "module": "proof/consequences/Complement/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Complement/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Complement/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 7: «The cliques of size s are the independent sets of size s of the complement graph, and the vertex covers of size s are the complements of the independent sets of size n − s.» (definitions and statements only)

proof/consequences/GraphProblems/ gives cliques and vertex covers formulas of their own (`cliqueF`,
`coverF`). Here both numbers are obtained, as in the paper, from the ONE formula for independent
sets (`indepF`): for cliques on the matrix of the complement graph, for vertex covers with n − s in
the place of s.
This file has no theorem. 

### `StCliques`

 «The cliques of size s are the independent sets of size s of the complement graph». 

### `StCovers`

 «the vertex covers of size s are the complements of the independent sets of size n − s», for s ≤
n. 

### `complMatrix`

 The adjacency matrix of the complement graph, from that of the graph: the entry (u, v) is 1
exactly if u ≠ v and the old entry is 0. 

### `StComplMatrix`

 It is the matrix of the complement graph. 

### `StComplCert`

 It is computed in polynomial time from (n in unary, matrix). 

### `readClique`

 The reader for cliques: `codeWith G s` as (n in unary, s, formula for independent sets of the
complement graph). 

### `readCover`

 The reader for vertex covers: `codeWith G s` as (n in unary, n − s, formula for independent sets
of the graph). 

### `StReaders`

 What the two readers hand over counts cliques and vertex covers. 

### `StReadersCert`

 The two readers are polynomial-time. 

### `StCounts`

 **For EVERY machine Z that counts with a prescribed number of true variables** (the body of
`GraphProblems.StSized` at width 2 with the exponent δ): Z after `readClique` returns the number of
cliques of size s, and Z after `readCover` the number of vertex covers of size s, within the same
number of steps. 

### `StIndepAlone`

 The formula for independent sets alone: its certificate and its shape. (In
proof/consequences/GraphProblems/ these facts are bundled with those for `cliqueF` and `coverF`;
they are stated apart here, so that the route here does not depend on the two formulas.) 

### `StFromSized`

 **With the machines named.** From the interface `GraphProblems.StSized`: for every δ > 0 ONE
machine Z, put after the two readers, counts the cliques and the vertex covers of size s ≤ n within
c·2^{δn} steps, with polynomial-time steps. 

### `StFromGamma`

 **The route from end to end, counted in steps.** «Add the clause {¬x_u, ¬x_v} for each edge uv;
Corollary 6 then counts the independent sets of size s. The cliques … the vertex covers …» For every
family of circuits that tests the size, every δ > 0 and EVERY procedure E for #3-SAT whose exponent
δ_E is small enough for the O(n) variables of Γ: the machine that puts Γ beside the formula and then
runs E (`SizeCircuit.sizedBy gates E`),
put after the reader of the formula for independent sets (`GraphProblems.readF indepF`), after
`readClique` and after `readCover`, returns the numbers of independent sets, cliques and vertex
covers of size s ≤ n within c'·2^{δn} steps. 

### `StOnTuringMachines`

 The two clauses of `GraphProblems.CorGraphsCount` and the two of `GraphProblems.CorGraphsDecide`
on cliques and vertex covers, on Mathlib's Turing machines. The counting machines are Z of
`StFromSized` after `readClique` and `readCover`, with the number written by `Nat.bits`; the
deciding machines are the same with «the number is not 0» as the output, which decides by
`GraphProblems.StDecide` («subsets of … cliques, and supersets of vertex covers …, are again such
sets»).
By its statement this shows nothing beyond proof/consequences/GraphProblems/ (which proves it with
formulas of their own); `StCounts`, `StFromSized` and `StFromGamma` name the route by counting. The
route goes from `StFromSized` and `GraphProblems.StDecide` through the host theorem of
proof/consequences/GraphProblems/ (`GraphProblems.tm_of_stepped`), and it uses `StCliques`,
`StCovers`, `StCounts` and `StFromSized`
(proved as `Complement.stCliques`, `stCovers`, `stCounts`, `stFromSized`), not the formulas
`GraphProblems.cliqueF` and `GraphProblems.coverF` of proof/consequences/GraphProblems/. It is the
proof of Corollary 7 by counting (both halves), not the proof of `GraphProblems.CorGraphsDecide`
from 3-SAT in proof/consequences/Sat3Graph/, which uses no counting machine.
(For cliques the formula of proof/consequences/GraphProblems/ and the one here are the same list;
for vertex covers they differ.) 
