---
{
  "module": "proof/consequences/Complement/Readers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Complement/Readers.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Complement/Readers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 7: cliques and vertex covers are counted with the ONE formula for independent sets

«Add the clause {¬x_u, ¬x_v} for each edge uv; Corollary 6 then counts the independent sets of size
s. The cliques of size s are the independent sets of size s of the complement graph, and the vertex
covers of size s are the complements of the independent sets of size n − s.» (proof of Corollary 7)
* `stIndepAlone`: the formula for independent sets is computed in polynomial time, has width 2,
  variables below n and at most n² clauses. It is proved from the lemmas of
  proof/consequences/GraphProblems/ on formulas with one clause per chosen pair
  (`GraphProblems.Sets.shaped_pairs`, `GraphProblems.pairs_polyT`), not from the bundled statements
  that also speak of the formulas for cliques and vertex covers.
* `stComplCert`, `stReadersCert`: the matrix of the complement graph and the two readers are
  computed in polynomial time.
* `stReaders`: what the readers return on `codeWith G s`, and what it counts.
* `stCounts`: every machine that counts with a prescribed number of true variables, put after the
  readers, counts cliques and vertex covers, within the same number of steps.
* `stFromSized`, `stFromGamma_of`: the same with the machine of `GraphProblems.StSized`, and with «Γ
  beside the formula, then E». 

### `stIndepAlone`

 The formula for independent sets alone: it is computed in polynomial time from (n in unary,
matrix); it has at most 2 literals per clause, variables below n, and at most n² clauses. 

### `stComplCert`

 The matrix of the complement graph is computed in polynomial time from (n in unary, matrix). 

### `readers_aux`

 The two readers are polynomial-time, with any polynomial-time function r in the place of
`read2`. 

### `stReadersCert`

 The two readers are polynomial-time. 

### `stReaders`

 What the two readers hand over counts cliques and vertex covers: on `codeWith G s`, s ≤ n,
`readClique` returns (n in unary, s, the formula for independent sets of the complement graph),
whose satisfying assignments with s true variables are as many as the cliques of size s; `readCover`
returns (n in unary, n − s, the formula for independent sets of G), whose satisfying assignments
with n − s true variables are as many as the vertex covers of size s. 

### `stCounts`

 **For every machine Z that counts with a prescribed number of true variables**, at width 2 with
the exponent δ: Z after `readClique` returns the number of cliques of size s, and Z after
`readCover` the number of vertex covers of size s, within the same number of steps. 

### `stFromSized`

 **With the machines named.** From the interface `GraphProblems.StSized`: for every δ > 0 one
machine Z, put after the two readers, has polynomial-time steps and counts the cliques and the
vertex covers of size s ≤ n within c·2^{δn} steps. 

### `stFromGamma_of`

 **The route from end to end, counted in steps**, from the statement `SizeCircuit.StSizedBy` on
the machine «Γ beside the formula, then E», taken at width 2: that machine, put after the reader of
the formula for independent sets, after `readClique` and after `readCover`, returns the numbers of
independent sets, cliques and vertex covers of size s ≤ n within c'·2^{δn} steps. 
