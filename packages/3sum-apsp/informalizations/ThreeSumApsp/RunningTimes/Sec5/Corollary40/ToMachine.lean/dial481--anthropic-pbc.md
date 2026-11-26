---
{
  "module": "ThreeSumApsp/RunningTimes/Sec5/Corollary40/ToMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary40/ToMachine.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary40/ToMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The three hinted problems: from a program that runs in phases to the word RAM

`AchievesVHinted`, `AchievesMvHinted` and `AchievesUMvHinted` (Section 5.4) ask for one program of
the word RAM for each phase, a slope, a constant, and an exponent for the polynomial time of
Phase 1.  The three theorems of this file produce them from one program of the small language with
one procedure for each phase.  What is left to show for a concrete program is, for every n ≥ 1 and
all inputs, a run in phases (`LightPhases`) within limits that are polynomial in n, and bounds
A (n^a + 1) on the numbers of steps: the structure `PhaseRun`.

The route is `PhaseRun.compile`.  The phases are compiled (`runsPhases_start`), and a compiled phase
takes a constant times as long as the phase (`within_ramSteps`).  This needs that every number of
the inputs fits in a word, which is shown for each problem (`absLe_rowMajor_toInt`,
`absLe_ofFn_fin`, `absLe_singleton_fin`).


 ## The numbers of the inputs fit in a word 

### `absLe_rowMajor_toInt`

 The numbers of a Boolean matrix are 0 and 1. 

### `absLe_singleton_fin`

 An index is below `n`. 

### `absLe_ofFn_fin`

 The entries of a vector of indices are below `n`. 

 ## The three problems 

### `achievesVHinted_of_light`

 **v-hinted Mv.**  If for every n ≥ 1 and all inputs the procedures p₁, p₂, p₃ of P run the three
phases within limits that are polynomial in n, in at most A (n^a₁ + 1), A (n^a₂ + 1) and A (n^a₃ +
1) steps, and leave column i of M V in the output cells, then the compiled procedures solve the
problem with Phase 2 in O(n^a₂) and Phase 3 in O(n^a₃) time. 

### `achievesMvHinted_of_light`

 **Mv-hinted Mv.**  If the procedures p₁, p₂, p₃ of P run the three phases of Mv-hinted Mv as in
`achievesVHinted_of_light` and leave column j of N_{[n],I} V in the output cells, then the compiled
procedures solve the problem with Phase 2 in O(n^a₂) and Phase 3 in O(n^a₃) time. 

### `achievesUMvHinted_of_light`

 **uMv-hinted uMv.**  If the procedures p₁, …, p₄ of P run the four phases of uMv-hinted uMv as
in `achievesVHinted_of_light` and leave the bit (U N_{I,J} V)_{i,j} in the first output cell, then
the compiled procedures solve the problem with Phases 2, 3, 4 in O(n^a₂), O(n^a₃), O(n^a₄) time. 
