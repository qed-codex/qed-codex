---
{
  "module": "proof/networks/Eight/ViaGrouping/CorENP.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/CorENP.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/CorENP.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, the circuit lower bound for E^NP, from a procedure for #3-SAT that is a parameter

The proof of proof/consequences/CircuitLowerBound/ uses the algorithm for satisfiability at one
place, the interface statement `CircuitLowerBound.StAlg`; `Eight.stAlg_of`
(proof/networks/Eight/Cor/ENP.lean) proves it from a procedure for #3-SAT that is left open
(`Eight.StEngine`). This file draws the circuit lower bound for E^NP (Section 7) from that
hypothesis (`corCircuits_of`, `corCircuits'_of`, `corCircuitsInf_of`), and states the run of the
machine inside that lower bound with the procedure named, for a family of machines En k ℓ τ with
`EngineCounts En` (`ALGO_runs_of`).
The proofs in this file name no algorithm for cliques or for networks.

Different from the paper: the paragraph «Circuit lower bounds» in Section 7 draws this lower bound
from «ETH is false» by citing a theorem of Williams (see also Jahanjou, Miles and Viola). In
proof/consequences/CircuitLowerBound/ the implication is proved, for a procedure for #3-SAT cut into
steps, not for an arbitrary algorithm for 3-SAT. 

### `ALGO_runs_of`

 **The algorithm inside the circuit lower bound for E^NP (Section 7), with the procedure named.**
For every δ > 0 there are a level ℓ and a threshold parameter τ such that `En 3 ℓ τ` has
polynomial-time steps and the machine `CircuitLowerBound.Alg.algo (En 3 ℓ τ) F fb` ends on every
input x with the bit
«the formula made from x is unsatisfiable», within c·2^{δN} steps, N the number of variables of that
formula. F and fb stand for the functions that make the formula; the statement holds for every F
with `Alg.FormOK` and every fb. Only the steps of the procedure are counted: the formula
`Alg.pre F fb x` is made in the hand-over. The proof of the lower bound uses F and fb that are
computable in polynomial time (`CircuitLowerBound.StForm`, `CircuitLowerBound.StFlip`). 

### `stAlg_from`

 The interface statement `CircuitLowerBound.StAlg`, from Corollary 6 for machines cut into steps. 

### `corCircuits_of`

 **The circuit lower bound for E^NP (the paragraph «Circuit lower bounds» in Section 7)**: some
language in E^NP is not decided by (non-uniform) Boolean circuits of size O(n). The statement is
`ENP.CorCircuits` of `CircuitLowerBoundStatement.lean` (oracle machines with an oracle for SAT); the
hypothesis is Corollary 6 for machines cut into steps. 

### `corCircuits'_of`

 The circuit lower bound for E^NP with the second form of E^NP (an ordinary machine that is
started again after every answer). 

### `corCircuitsInf_of`

 The lower bound for E^NP infinitely often (not stated in the paper; it looks stronger but is
equivalent to that lower bound, because finitely many lengths can be paid for by a larger c:
`ENP.infinitely_often`): for every c the language has no circuits with c·(n+1) gates at infinitely
many lengths n. 
