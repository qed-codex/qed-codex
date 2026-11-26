---
{
  "module": "proof/consequences/FromPrinted/Circuits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/Circuits.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/Circuits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Corollary 7 on the machines of its printed proof, and the circuit lower bound for E^NP (Section 7) on the procedure of Corollary 6, on the machines of proof/threesat/Printed/

`Consequences.tm_of_counts` and `Consequences.ofWord_binary_lt`
(proof/consequences/Consequences/Main.lean), which name no machine, are used as they stand.
* `tm_of_colorings`: the machine of `StColoringsCounted` is simulated by a Turing machine of
  Mathlib: the host theorem of proof/consequences/GraphProblems/, `GraphProblems.tm_of_stepped`.
* `graphsFrom`, `graphsByCounting`: Corollary 7, both sentences, from `StSetsCounted`,
  `StDominatingCounted`, `StColoringsCounted` as hypotheses, then on their proofs; «In particular,
  they decide …» by `GraphProblems.stDecide` and `GraphProblems.stDecideColor`.
* `circuitsFrom`, `circuits`: the circuit lower bound for E^NP (the paragraph «Circuit lower bounds»
  in Section 7) in its three Lean forms, from Corollary 6 for machines cut into steps
  (`Eight.ViaGrouping.EngineCounts`) for the family `FromPrinted.SplitCount.ENGINEsplit`, as a
  hypothesis, then on its proof; `stAlgoRuns` names the machine inside. 

### `tm_of_colorings`

 A Turing machine with finite alphabets that, started on the code of a graph G on n vertices,
halts with `post` of the number of proper colorings of G with k ≥ 3 colors within ⌊C·2^{δn}⌋ steps,
from the statement `StColoringsCounted` as a hypothesis: it simulates the machine of that statement
at δ/2. 

### `graphsFrom`

 **Corollary 7**, both sentences, in the wording of GraphProblemsStatement.lean
(`GraphsByCounting`): the five numbers are computed, and the five problems decided, in time
O(2^{δn}) on Turing machines. Here it is drawn from the three statements that name the machines, as
hypotheses: the Turing machines simulate the machines named in `StSetsCounted`,
`StDominatingCounted` and `StColoringsCounted`. 

### `graphsByCounting`

 **Corollary 7**, both sentences: `graphsFrom` on the proofs `stSetsCounted`,
`stDominatingCounted`, `stColoringsCounted`. 

### `stAlgoRuns`

 **The algorithm inside the circuit lower bound for E^NP (Section 7), with the procedure of
Corollary 6 named**: `Eight.ViaGrouping.ALGO_runs_of` at the family `ENGINEsplit`. For every δ > 0
there are ℓ, τ, c such that `ENGINEsplit 3 ℓ τ` has polynomial-time steps and
`CircuitLowerBound.Alg.algo (ENGINEsplit 3 ℓ τ) F fb` ends on every input x with the bit that says
whether the formula made from x is unsatisfiable within c·2^{δN} steps, N the number of variables of
that formula, for every F with `CircuitLowerBound.Alg.FormOK` and every fb. 

### `circuitsFrom`

 **The circuit lower bound for E^NP** (the paragraph «Circuit lower bounds» in Section 7) in its
three Lean forms (`ENP.CorCircuits`, `ENP.CorCircuits'`, `ENP.CorCircuitsInf`), from Corollary 6 for
machines cut into steps (`Eight.ViaGrouping.EngineCounts`) for the family
`FromPrinted.SplitCount.ENGINEsplit`, as a hypothesis. 

### `circuits`

 **The circuit lower bound for E^NP** (Section 7) in its three Lean forms: `circuitsFrom` on the
proof `FromPrinted.SplitCount.stEngineCounts`. 
