---
{
  "module": "proof/consequences/FromPrinted/GraphDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/GraphDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/GraphDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7: Corollary 7 (counting in graphs) and the circuit lower bound for E^NP on the machines of proof/threesat/Printed/ (definitions and statements only)

This file puts Corollary 7 and the circuit lower bound for E^NP (Section 7) on the procedure
`FromPrinted.SplitCount.ENGINEsplit`, which is `SplitCount.ENGINEsplit` with `Printed.COUNT ℓ` at
the leaves in the place of `Eight.ViaGrouping.COUNTp ℓ`; its definitions `SIZED`, `DOMcount`,
`StSetsCounted`, `StDominatingCounted`, `StColoringsCounted`, `StAlgoRuns` name this procedure.
`Consequences.CountsGraph` (proof/consequences/Consequences/Defs.lean), which names no machine, is
used as it stands.
This file has no theorem. 

### `SIZED`

 The machine that counts the satisfying assignments with exactly s true variables: Γ from the
circuit `sizeGates` beside the formula, then the procedure of the printed proof of Corollary 6 at
width max(w, 3), level ℓ, threshold parameter τ. 

### `StSetsCounted`

 **Independent sets, cliques, vertex covers of size s, with the machines named.** For every δ > 0
there are ℓ, τ, c such that `SIZED 2 ℓ τ`, put after the reader of the formula for independent sets,
after `readClique` and after `readCover`, has polynomial-time steps and returns the three numbers
within c·2^{δn} steps, on states of size at most c·(n+2)^c. 

### `DOMcount`

 The machine for dominating sets: read the input, walk the tree that shortens the clauses to w
literals, count at each leaf by `SIZED w ℓ τ`, add up. 

### `StDominatingCounted`

 **Dominating sets of size s, with the machine named.** «Choose w so large that the number of
leaves is at most 2^{δn/2}, apply Corollary 6 to each leaf, and add up.» For every δ > 0 there are
w, ℓ, τ, c such that the tree that shortens the clauses to w literals has at most 2^{(δ/2)n} leaves
(`ShortensD w (δ / 2)`), and `DOMcount w ℓ τ` has polynomial-time steps and returns, on the code of
(G, s), s ≤ n, the number of dominating sets of size s within c·2^{δn} steps, on states of size at
most c·(n+2)^c. 

### `StColoringsCounted`

 **Proper colorings with k colors, with the machine named**: the k-CNF on kn variables, then the
procedure of the printed proof of Corollary 6; the number in kn + 1 bits. 

### `StAlgoRuns`

 **The algorithm inside the circuit lower bound for E^NP (Section 7), with the procedure of
Corollary 6 named.** For every δ > 0 there are ℓ, τ, c such that `ENGINEsplit 3 ℓ τ` has
polynomial-time steps and `CircuitLowerBound.Alg.algo (ENGINEsplit 3 ℓ τ) F fb` ends on every input
x with the bit «the formula made from x is unsatisfiable» within c·2^{δN} steps, on states of size
at most c·(N + 2)^c, N the number of variables of that formula, for every F with
`CircuitLowerBound.Alg.FormOK` and every fb.
Only the steps of the procedure are counted: the formula `CircuitLowerBound.Alg.pre F fb x` is made
when the input is handed over. It is `Eight.ViaGrouping.ALGO_runs_of` at the family `ENGINEsplit`.
It stands beside the proof of the circuit lower bound (see `Circuits`). 

 ### The end theorems

Each is proved in two pieces: a theorem `…From` that has the statements named as HYPOTHESES, and a
one-line instance on their proofs. The theorems of this development (everything outside Lean's core,
Std, Batteries and Mathlib) that the proof of `…From` reaches say nothing about a particular machine
for k-SAT or #k-SAT
(the host theorem and the facts on graphs and formulas; for the circuit lower bound the theorems of
proof/consequences/CircuitLowerBound/ and `Eight.ViaGrouping.corCircuits_of`, `corCircuits'_of`,
`corCircuitsInf_of`, `stAlg_from`, `stEngine_of` and `Eight.stAlg_of`; all of these take the
procedure or the machine as a hypothesis; one exception, which is no fast machine: under
`circuitsFrom` lies proof/consequences/CircuitLowerBound/'s own exhaustive search
`CircuitLowerBound.TabF.tryAll` with `fb`, which answers the question at the last place of a chain
by trying all assignments; it belongs to the construction of the language). 

### `GraphsByCounting`

 Corollary 7, by counting.
`FromPrinted.Consequences.graphsFrom : StSetsCounted → StDominatingCounted → StColoringsCounted → GraphsByCounting`:
the Turing machines simulate the five named machines (host theorem of
proof/consequences/GraphProblems/, `GraphProblems.tm_of_stepped`); «In particular, they decide …» by
`GraphProblems.stDecide`, `stDecideColor`, with the output that the number is not 0. 

### `Circuits`

 The circuit lower bound for E^NP (the paragraph «Circuit lower bounds» in Section 7), in its
three Lean forms. `FromPrinted.Consequences.circuitsFrom : EngineCounts ENGINEsplit → Circuits`,
from `Eight.ViaGrouping.corCircuits_of`, `corCircuits'_of`, `corCircuitsInf_of` applied to
`Eight.ViaGrouping.stEngine_of`.
(`StAlgoRuns` names the machine inside; it stands beside the path, since `corCircuits_of` takes the
procedure with the machine left open.) 
