---
{
  "module": "proof/threesat/Printed/LevelCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/LevelCost.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/LevelCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Proposition 3, «Cost», with a table query at the cost of one operation

The counterpart of `Eight.ViaGrouping.stLevelP_of` (proof/networks/Eight/ViaGrouping/Level.lean) for
the machine `levelMachine`. With the tables built in, that machine is the step machine of
proof/networks/Eight/ with `networkOnSteps` in the place of the algorithm for networks
(`levelMachine_close`). The bound of Lemma 1 enters through `StOnProcedures`, applied to the row
network or the column network of ι,
a network in the sense of Definition 2 with the printed B₁ given (`grid_isNetwork_of`). The other
facts are those of proof/networks/Eight/: the expansion Σ_ι Z_ι = 2^{t|ℛ|}·Z (`eqExpansion_words`),
the bound on the values (`netOfι_sized_t`), the smaller total (`stMin`), and the arithmetic
(`Eight.Level.level_time`, `level_size`).
At the end `QueryMachines.stClose` reads the number of steps as own steps plus queries. 

 ## Arithmetic 

### `size_units`

 A list of units of length n has size 2n + 1. 

### `level_time_printed`

 «Cost», the number of steps, with the printed B₁ = gB + g²λ + 1 and the factor 3 of
`StOnProcedures`: from `Eight.Level.level_time` at B + gλ + 1 in the place of B. 

### `level_size_printed`

 «Cost», the sizes: from `Eight.Level.level_size`; sc is the size of the pair (λ, B) in unary.
Not in the paper, which counts operations only. 

 ## One ι 

### `level_one_of`

 «Apply Lemma 1 to the network with the smaller total»: the run for one ι. The bound of Lemma 1
(`StOnProcedures`) on the row network or the column network, and the display on the smaller total
(`stMin`). 

 ## The loop over ι and the division 

### `level_runs_of`

 The paragraph «Cost» for the step machine that `levelMachine` becomes when the tables are built
in: value, number of steps, sizes. c holds λ and B in unary. 

 ## Proposition 3, first sentence, for the algorithm of its proof 

### `levelMachine_achieves_of`

 «Cost» for `levelMachine`: if the machine of Lemma 1 does what Lemma 1 says on networks on [g],
then `levelMachine K g M` does what Definition 4 asks for (g², (ρ + 2/K)e + 2/K). 

### `stLevelTied_of`

 **Proposition 3, first sentence, for the algorithm of its proof, from any machine that does what
Definition 4 asks.** The hypotheses: two statements on the coding of the tables (`StAskServes`,
`StCliqueValue`), Lemma 1 for the algorithm of its proof, and Lemma 1 for networks given by
procedures. 
