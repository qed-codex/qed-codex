---
{
  "module": "proof/networks/Eight/Cor/ENP.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Cor/ENP.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Cor/ENP.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, the circuit lower bound for E^NP: E^NP does not have circuits of linear size; the algorithm for satisfiability as a parameter

The proof of proof/consequences/CircuitLowerBound/ uses the algorithm for satisfiability at one
place, the interface statement `CircuitLowerBound.StAlg`: a machine that, given 1^m 0 y, reads y as
a circuit and tests by the procedure for #3-SAT whether the assignment that the circuit computes
violates some clause of the formula `Phi m`. The machine cut into steps is
`CircuitLowerBound.Alg.algo E F fb`, with the procedure E as a parameter. In this development E is
the machine of the proof of Corollary 6 at width 3, which runs CLIQUE(ℓ) of Algorithm 1; here E is
left open, and
`StAlg` is proved from a procedure that is a parameter (`stAlg_of`). Everything else of
proof/consequences/CircuitLowerBound/ (the language, the tables, the chains, the circuits, the two
forms of E^NP) is used as it
is and does not use Algorithm 1 or Lemma 2.

Different from the paper: the paragraph «Circuit lower bounds» in Section 7 derives the statement
from «ETH is false» by citing a theorem of Williams (see also Jahanjou, Miles and Viola). In
proof/consequences/CircuitLowerBound/ the implication is proved, for the algorithm of this
development, not for an arbitrary algorithm for 3-SAT. 

### `stAlg_of`

 The interface statement `CircuitLowerBound.StAlg`, from a procedure for #3-SAT that is a
parameter and the statements on the formula, on circuits as data, on the schedule and on the last
place of a chain. 
