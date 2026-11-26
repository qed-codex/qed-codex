---
{
  "module": "proof/threesat/Exits/Poly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/Poly.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/Poly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A loop that can be left early: polynomial-time steps

`IsPolyT` (every part of a stepped computation is polynomial-time) for the machine `foldUntil` of
proof/threesat/Exits/Defs.lean, the loop that can be left early, which stands for line 10 of
Algorithm 1, «try all groupings into K_ℓ groups until one is good», and for lines 2 and 3 read for
deciding (stop at the first Φ with Count(Φ) > 0).
The proof is that of `Groundwork.IsPolyT.foldWhile` (proof/machines/ToTuring/Poly/IsPoly.lean). The
one difference: after a round the next point is «none if the new accumulator passes `stop`, else nxt
x», which is polynomial-time because `stop` is.
The chain Lemma 1 → Proposition 3 → Theorem 2 of this folder needs only `stFoldUntilPoly` from this
file: the two uses of the loop (`search_isPolyT` in proof/threesat/Exits/Grouping.lean,
`Suffices.satLoop_polyTimeSteps_of` in proof/threesat/Suffices/Loop.lean) take the statement
`StFoldUntilPoly` as a hypothesis, and `stFoldUntilPoly` proves it. 

### `IsPolyT.foldUntil_step`

 One step of the loop that can be left is polynomial-time. 

### `IsPolyT.foldUntil`

 The loop `foldUntil` is `IsPolyT` if its body `M` is and `start`, `nxt`, `g`, `stop`, `c₀` are
polynomial-time. 

### `stFoldUntilPoly`

 **The loop that can be left has polynomial-time steps.** Behind «until one is good» (line 10 of
Algorithm 1) and the exit at the first Φ with Count(Φ) > 0 (lines 2 and 3 read for deciding). 

### `IsPolyT.firstUntil`

 «try all groupings into K_ℓ groups until one is good» (line 10 of Algorithm 1): the search that
halts at the first good number has polynomial-time steps if its body has and the bound `N` and the
test `p` are polynomial-time. 

### `IsPolyT.walkUntil`

 «for each … do» (line 2 of Algorithm 1), read for deciding: stop at the first Φ with Count(Φ) >
0: the walk that halts at the first leaf that passes has polynomial-time steps if `step`, `root` and
the steps of the test `T` are polynomial-time. 
