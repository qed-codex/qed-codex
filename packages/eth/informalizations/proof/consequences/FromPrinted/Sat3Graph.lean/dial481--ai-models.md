---
{
  "module": "proof/consequences/FromPrinted/Sat3Graph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/Sat3Graph.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/Sat3Graph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, Corollary 7 for the decision problems, from 3-SAT, on the machine `Printed.SAT`, which decides with Algorithm 1, as a machine of proof/threesat/Printed/

Proofs of `StWithThreeSatMachine` and `StTiedTM` of proof/consequences/FromPrinted/SatDefs.lean, and
the end theorem with the statement `GraphProblems.CorGraphsDecide`, in two pieces (`endFrom`,
`decideFromThreeSat`). What proof/consequences/Sat3Graph/ proves for every procedure D
(`Sat3Graph.stSets`, `stDominating`, `stColoring`, `stCert`, and the hosts of Host.lean) is used as
it stands.
The procedure for 3-SAT is the machine of Theorem 2 in its decision form without its reader
(`FromPrinted.SplitSat.core3 ℓ τ`, `FromPrinted.SplitSat.stCore3`). Given δ and k: take w so large
that the tree for Dominating Set has at most 2^{δn/2} leaves (`GraphProblems.stShortens`); all five
3-CNFs then have at most Q·(n+1) variables for Q = a + 1 + 3·(w − 3) + 2k, and the exponent δ₃ =
δ/(2Q) is small enough for all five.
On Turing machines: the five deciders are taken with δ/2 and hosted with polynomial overhead
(proof/consequences/Sat3Graph/Host.lean). 

### `stWithThreeSatMachine`

 **`StWithThreeSatMachine`.** For every family of circuits that tests the size and is computed in
polynomial time, every δ > 0 and k ≥ 3 there are ℓ, τ, w, c such that the five deciders with D =
`core3 ℓ τ` have polynomial-time steps and decide the five problems within c·2^{δn} steps. 

### `stTiedTM`

 **`StTiedTM`.** For every δ > 0 and k ≥ 3 there are a family of circuits that tests the size and
is computed in polynomial time (`sizeGates`), and ℓ, τ, w, c such that each of the five deciders
with D = `core3 ℓ τ` itself has polynomial-time steps and decides its problem within c·2^{δn} steps,
and is simulated with polynomial overhead by a Turing machine with finite alphabets that decides the
problem within ⌊C·2^{δn}⌋ steps. 

### `endFrom`

 **The end theorem, first piece**: from the tied statement `StTiedTM`, taken as a hypothesis, the
statement `GraphProblems.CorGraphsDecide`: for every δ > 0, Independent Set, Clique, Vertex Cover,
Dominating Set and, for every k ≥ 3, k-Coloring are decided by Turing machines in time O(2^{δn}).
The Turing machines are those that the hypothesis gives (for the four problems on sets, those at k = 3);
nothing else about a machine is used. 

### `decideFromThreeSat`

 **The end theorem**, with the statement `GraphProblems.CorGraphsDecide`: `endFrom` applied to
`stTiedTM`. Each of the five deciders asks the machine of Theorem 2 in its decision form
(`FromPrinted.SplitSat.core3`) whether a 3-CNF is satisfiable; apart from procedure Count inside
that machine, nothing counts satisfying assignments. 
