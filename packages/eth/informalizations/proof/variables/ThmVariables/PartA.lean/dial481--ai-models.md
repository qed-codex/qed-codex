---
{
  "module": "proof/variables/ThmVariables/PartA.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/ThmVariables/PartA.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/ThmVariables/PartA.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (a) with the printed hypothesis, from the form with the padding string

Let K, e, C₀, `kf`, `num`, E be as in the printed hypothesis. The step from counted operations to
the padding string (`SolverFromMachine`, a hypothesis here) gives a polynomial-time solver S with a
sequence Q of levels for the same K_ℓ and for e′_ℓ = `CliqueLevels.cutNumber K num ℓ`, the number in
[e_ℓ, 2e_ℓ] cut at 1.
* The clause of the hypothesis that a number in [e′_ℓ, 2e′_ℓ] can be computed holds for the sequence
  e′, because e′_ℓ itself is computed: it is the fraction min(a, b)/b for the fraction a/b that
  `num` returns (`QueryMachines.Bridge.cutFraction`; `cut_eq`, `numberBetween_cut`).
* Theorem D (a) with the padding string (`RecursionToBound.ThmVariablesAWithNumberBetween`, a
  hypothesis here) gives a machine M with the bound at e′_ℓ.
* The levels of n are the same, because K at the ℓ-th index is K_ℓ.
* e_ℓ ≤ e′_ℓ ≤ 2e_ℓ and e′_ℓ ≤ 1, so the bound at e′_ℓ is the bound at e_ℓ with twice the constant
  (`boundAtANumberBetween`). The last two points are `conclusion_of_cut`. 

### `cut_eq`

 min(a, b)/b = min(a/b, 1), for all natural numbers a and b (both sides are 0 if b = 0). 

### `cutNumber_nonneg`

 e′_ℓ = `cutNumber K num ℓ` is not negative, for all K, `num` and ℓ. 

### `numberBetween_cut`

 A number in [e′_ℓ, 2e′_ℓ] can be computed from ℓ in time polynomial in K_ℓ, for e′_ℓ the number
that `num` returns, cut at 1: it is e′_ℓ itself. Hypotheses: Q is a sequence of levels of a solver S
for the numbers e′_ℓ, `num` is polynomial-time, and S has K_ℓ at the ℓ-th index of Q. 

### `conclusion_of_cut`

 A machine with the bound of Theorem D (a) for a solver whose levels are K_ℓ and e′_ℓ, the number
in [e_ℓ, 2e_ℓ] cut at 1, has the bound for K_ℓ and e_ℓ with twice the constant. Hypotheses: K, e, C₀
satisfy the printed inequalities (`CliqueLevels.Levels`), `num` returns a number in [e_ℓ, 2e_ℓ]
(`CliqueLevels.NumberBetween`), Q is a sequence of levels of the solver S for the numbers e′_ℓ, and
S has K_ℓ at the ℓ-th index of Q. 

### `partAFromThePaddingString`

 Theorem D (a) with the printed hypothesis follows from Theorem D (a) with the padding string and
the step from a machine to a solver. 
