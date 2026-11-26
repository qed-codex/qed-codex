---
{
  "module": "proof/networks/Eight/ViaGrouping/LevelCert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/LevelCert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/LevelCert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The algorithm of one level, on an algorithm for networks in the printed form, has polynomial-time steps

A step of a step machine in this development may be any polynomial-time function. Here: if the
pieces of Lemma 2, «computable in time poly(λ)», are computed in polynomial time (`Eight.StKeeps`)
and the function for Ψ is (`StPsiPoly`), then the row network and the column
network of ι, given as Definition 2(iii) asks (`levelProcs`), have P, P_a and c_{a,b} in unary and
four procedures with polynomial-time steps (`levelProcs_keepsP`); and the algorithm of one level
(`levelAlgP`) has polynomial-time steps if the algorithm for
networks that it calls has (`stLevelKeepsP_of`). The certificates of the loop, of the choice of the
network and of the division are those of proof/networks/Eight/Level/Cert.lean. 

### `levelProcs_keepsP`

 The row network and the column network of ι, given as Definition 2(iii) asks, have P = g³λ, P_a
and c_{a,b} in unary and four procedures with polynomial-time steps, for λ in unary. The test for
membership says yes without looking at the query. 

### `stLevelKeepsP_of`

 The algorithm of one level has polynomial-time steps if the algorithm for networks has, and if
the pieces and the two functions for Ψ are computed in polynomial time. 
