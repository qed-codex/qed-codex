---
{
  "module": "proof/threesat/Given/Level.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Given/Level.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Given/Level.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Proposition 3, «Cost», through `IsGivenNetwork`

The proof of `Printed.stLevelTied_of` (proof/threesat/Printed/LevelCost.lean), carried out with
«Both networks satisfy Definition 2» in the form `stGridGiven` and Lemma 1 applied in the form
`stOnGiven`. The arithmetic (`Printed.level_time_printed`, `Printed.level_size_printed`,
`Printed.size_units`) and the other facts of this development are used as they stand; Lemma 1 for
the algorithm of its proof is `Printed.stGroupingTied`. 

 ## One ι 

### `level_one`

 «Apply Lemma 1 to the network with the smaller total»: the run for one ι. The bound of Lemma 1
on the row network or the column network, each a network in the sense of `IsGivenNetwork`
(`stOnGiven`, read by `onClosed`), and the display on the smaller total (`stMin`). The text is that
of `Printed.level_one_of` but for these two places. 

 ## The loop over ι and the division 

### `level_runs`

 The paragraph «Cost» for the step machine that `levelMachine` becomes when the tables are built
in: value, number of steps, sizes. c holds λ and B in unary. The text is that of
`Printed.level_runs_of`, with `stGridGiven` in the place of `Printed.grid_isNetwork_of`. 

 ## Proposition 3, first sentence, for the algorithm of its proof 

### `levelMachine_achieves`

 «Cost» for `levelMachine`: if the machine of Lemma 1 does what Lemma 1 says on networks on [g],
then `levelMachine K g M` does what `Printed.AchievedBy` asks for (g², (ρ + 2/K)e + 2/K). 

### `stLevelTied`

 **Proposition 3, first sentence, for the algorithm of its proof**, from any machine that does
what `Printed.AchievedBy` asks (Definition 4 in the paper's unit of cost, a table query costs one
operation, with a bound on memory added). The statement is `Printed.StLevelTied`; the proof runs
through `stGridGiven` and `stOnGiven`. 

 ## Polynomial-time steps 

### `networkOn_steps`

 A machine for networks with polynomial-time steps, on procedures with polynomial-time steps: the
second conjunct of `IsGivenNetwork` is all that is used. (`stOnGiven` says the same of a network;
here no network is at hand, since g, K and M are arbitrary.) 

### `stLevelPoly`

 The machine of Proposition 3 has polynomial-time steps if M has. The statement is
`Printed.StLevelPoly`; the text is that of `Printed.levelLoop_poly` and `Printed.stLevelPoly_of`,
with `gridProcs_poly`, the second conjunct of `stGridGiven`, for the two networks. 
