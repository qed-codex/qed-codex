---
{
  "module": "proof/rates/GeneralPieces/Rec/PartB.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Rec/PartB.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Rec/PartB.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Part (b) of Theorem A, as one statement

"One deterministic algorithm, given ℓ ≥ 0, λ, B ≥ 1 and query access to tables with |W_w| < 2^B,
outputs the value of the (K_ℓ, λ)-clique within 2^{e_ℓK_ℓ²λ}(K_ℓ(λ + B))^{C₀K_ℓ²} operations."

The algorithm is `solveG` on the schedule (40). For ℓ ≥ 1 the schedule of level ℓ has at least
g_{ℓ−1} = √K_ℓ symbols, far more than ℓ, so a program that is polynomial-time on all inputs cannot
write it down from ℓ alone.
It reads K_ℓ off the instance, whose tables are written out (the number of rows is K_ℓ), and builds
the schedule of the largest level whose number of nodes is at most that; on a (K_ℓ, λ)-clique this
is level ℓ.
So the ℓ in the input is not read. The statement is `GeneralPieces.Tied.PartB`, which names the
program (`Tied.runB`), the schedule and the hypotheses of case (ii); `AppRunningTime.PartB` follows
from it (`partB_of_tied`). The clauses: polynomial time (the certificates of the programs), the
value (all levels under the hypotheses of case (ii) of Lemma 8,
at every step of the schedule), and the bound on the exponent of the pad, a string of ones whose
length bounds the number of operations (`stRate2`). 

### `K_strictMono`

 K_ℓ is strictly increasing in ℓ. 

### `pick_rows`

 On a (K_ℓ, λ)-clique the program picks level ℓ. 

### `runB_polyT`

 The named program is polynomial-time in (pad, ℓ, instance), if the descent through all levels
is. 

### `partB_tied_of`

 Part (b) for the named program, from the interface statements; C₀ depends on c only. 

### `partB_of_tied`

 The form with "there is a program" follows; it does not name the recursion. 

### `solveG2`

 All levels give the value of the clique, under the hypotheses of case (ii) at every step. 

### `certSolveG`

 The descent through all levels is polynomial-time in (pad, K₀, schedule, instance), if the
programs of the pieces are. 

### `partB_tied`

 Part (b) of Theorem A for the named program, for pieces given as polynomial-time programs whose
numbers of bits are at most 2λ; C₀ depends on c only. 
