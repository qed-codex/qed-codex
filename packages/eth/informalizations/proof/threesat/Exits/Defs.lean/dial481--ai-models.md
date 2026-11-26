---
{
  "module": "proof/threesat/Exits/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A loop that can be left early (definitions and statements only)

The machines of this development leave a loop early in two places: lines 1 to 4 in their deciding
form (Suffices/Defs.lean), which return at the first formula Φ of Lemma 4 with Count(Φ) > 0, and
line 10, «try all groupings into K_ℓ groups until one is good».
The loop of the step machines of this development, `Groundwork.Stepped.foldWhile`
(proof/machines/StepMachines/Prog/Stepped.lean), cannot do this: its next point is a function of the
present point alone. So `firstRange` (Range.lean) runs through the whole range and keeps the first
hit, and `walk` (Walk.lean) tests every leaf.
`foldUntil` is `foldWhile` with one more argument, a test `stop` on the accumulator: after each
round the loop halts if the new accumulator passes the test. Its states are those of `foldWhile`.
The two uses:
* `firstUntil N M p`: the least y < N a such that p holds of M(a, y); the loop halts there;
* `walkUntil step root T`: does some leaf below root a pass the test T? The walk halts at the first
  leaf that passes.
What the statements say beyond those of `firstRange_runs` and `walk_runs`: the body need only halt
on the points up to the first hit (nothing is asked of it on later points), and the number of steps
is bounded by a sum over these points alone. This is how «the loop is left» shows in a statement.
This file has no proofs. 

### `foldUntil`

 The loop: run M at x = start a, fold its result into the accumulator by g; halt if the new
accumulator passes `stop`; else go on to nxt x; halt at none. 

### `firstUntil`

 The least y < N a such that p holds of M(a, y), if there is one; the loop halts at it. 

### `walkUntil`

 Does some leaf below root a pass the test T? The walk halts at the first leaf that passes. 

### `met`

 The points of the loop that are met: those of xs up to and including the first after which the
accumulator passes `stop`; all of xs if there is none. `f` is one round on the accumulator. 

### `StFoldUntil`

 **The loop.** Let xs be the orbit of nxt from start a, and let the body take t x steps on x and
return v x, FOR THE POINTS THAT ARE MET. Then the loop halts within Σ (t x + 1) steps, summed over
the points that are met, and returns the fold over them. (xs is a finite list; a loop whose orbit is
infinite and which ends only because of «stop» is not covered.) Sx, Sc, Sm bound the sizes of the
points, of the accumulator and inside the body. 

### `reach`

 How far the search goes: one past the first hit, or to the end of the range. 

### `StFirstUntil`

 **«try all … until one is good».** The body need only halt on y < reach, that is, up to the
first y with p (v y). Steps: at most Σ_{y < reach} (t y + 1). Result: the least y < N a such that p
holds of v y, as for `firstRange`. 

### `tested`

 The leaves that are tested: those up to and including the first that passes. 

### `StWalkUntil`

 **«for each … do if … then return».** The tree below root a has depth at most k. The test need
only halt on the leaves that are tested, that is, up to the first that passes. Steps: at most t + 2
for each leaf that is tested, and k more (for the nodes on the path to the last of them). Result:
whether some leaf passes, as for `walk`. 

### `StFoldUntilPoly`

 The loop has polynomial-time steps if its body has and `start`, `nxt`, `g`, `stop`, `c₀` are
polynomial-time. 

### `StFirstUntilOf`

 The two uses from the loop. 

### `StWalkUntilOf`

 See `StFirstUntilOf`. 
