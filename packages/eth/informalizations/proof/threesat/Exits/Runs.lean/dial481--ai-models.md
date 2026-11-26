---
{
  "module": "proof/threesat/Exits/Runs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/Runs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/Runs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A loop that can be left early: steps, sizes, result

Proofs of the statements of proof/threesat/Exits/Defs.lean about steps, sizes and results of the
machines `foldUntil`, `firstUntil` and `walkUntil` (all but `StFoldUntilPoly`, which is proved in
Poly.lean).
* `stFoldUntil`: the loop. The proof is that of `Groundwork.Stepped.foldWhile_runs`
  (proof/machines/StepMachines/Prog/Stepped.lean), an induction along the orbit, with one more case:
  after a round whose accumulator passes `stop` the machine is in a halting state.
* `stFirstUntilOf`, `stFirstUntil`: line 10 of Algorithm 1, «try all groupings into K_ℓ groups until
  one is good».
* `stWalkUntilOf`, `stWalkUntil`: line 2 of Algorithm 1, «for each … do», run so that it stops at
  the first Φ with Count(Φ) > 0 (the deciding form; the printed algorithm sums the counts). The
  further ingredient here is the count of the stacks that are met, `length_tested_visits`.
Neither use goes through `firstRange` or `walk`.
The imports `import all StepMachines.Prog.Range` and `import all StepMachines.Prog.Walk` give access
to lemmas of those files that are not public: `orbit_range`, `sum_map_range` and `foldl_first`
(Range.lean) and `sum_sel` (Walk.lean). 

 ### The loop 

### `foldUntil_body`

 The body, run inside the loop; when it has halted, the loop goes to the next point, or halts if
the new accumulator passes `stop`. 

### `foldUntil_reaches`

 The loop from any point of the orbit and any accumulator. 

### `stFoldUntil`

 **The loop that can be left.** Steps: Σ (steps of the body + 1) over the points that are met;
result: the fold over them. Behind «until one is good» (line 10 of Algorithm 1) and the stop at the
first Φ with Count(Φ) > 0 in the deciding form of lines 2 and 3. 

 ### «try all … until one is good» 

### `stFirstUntilOf`

 «try all groupings into K_ℓ groups until one is good» (line 10 of Algorithm 1), from the loop:
the points met are (a, y) for y below `reach`. 

### `stFirstUntil`

 «try all groupings into K_ℓ groups until one is good» (line 10 of Algorithm 1): the search halts
at the first good number, within the steps of the numbers up to it. 

 ### «for each … do», stopped at the first leaf that passes 

### `length_tested_visits`

 **How many stacks are met.** While the tree below s, of depth at most k, is walked up to the
first leaf that passes, at most 2·(number of leaves tested) + k − 1 stacks are met: an inner node
that is met either has all the leaves of its left half tested, or lies on the path to the last leaf
tested. 

### `stWalkUntilOf`

 «for each … do» (line 2 of Algorithm 1), run so that it stops at the first Φ with Count(Φ) > 0
(the deciding form), from the loop: the stacks met are those up to the first whose top is a leaf
that passes. 

### `stWalkUntil`

 «for each … do» (line 2 of Algorithm 1), run so that it stops at the first Φ with Count(Φ) > 0
(the deciding form): the walk halts at the first leaf that passes, within t + 2 steps for each leaf
tested and k more. 
