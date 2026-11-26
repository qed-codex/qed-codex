---
{
  "module": "ThreeSumApsp/Lang/Phases.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Phases.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Phases.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Programs that receive their input in phases

`RunsPhases` says what it means that programs of the word RAM, one for each phase, run one after the
other on a memory into which the inputs of the phases are written one after the other (Corollary
40).  Here is the corresponding notion for one light program with one procedure for each phase
(`LightPhases`), and the proof that the compiled programs run in phases on the word RAM
(`runsPhases_of_light`, and `runsPhases_start` from the empty memory at an admissible word size).

For the proof that a light program runs in phases there are two tools.  `InputsAt μ off ws` says
that the list `ws` of the inputs of the phases so far lies from cell 0 on and ends before cell
`off`; it holds again after the next input has been written (`InputsAt.next`).  A fact about the
body of a procedure, or a specification that the procedure meets, gives a run of a phase
(`phase_of_ends`, `phase_of_meets`).

The invariant between two phases is `Input lim μ 0 0 c`: the memory of the machine holds the memory
of the light program, and the cells of the two arguments hold 0.  Writing the input of a phase keeps
it (`input_withInput`), and so does a run of a compiled program (`input_run`), which may start on
whatever an earlier one has left, because its start-up code sets up all it needs.

What is left to show about a concrete program is collected in the structure `PhaseRun`: a run in
phases within limits that are polynomial in n, and bounds A (n^a + 1) on the numbers of steps.
`PhaseRun.compile` turns it into a run of the compiled phases, each a constant times as long
(`within_ramSteps`).


### `overwrite`

 The memory μ with the list ws written into the cells off, off + 1, …. 

### `overwrite_out`

 A cell outside the list that has been written keeps its content. 

### `overwrite_in`

 A cell of the list that has been written. 

### `seg_overwrite`

 After a list has been written, it is there. 

### `overwrite_single`

 Writing one number. 

 ## The inputs of the phases so far 

### `InputsAt`

 The list `ws`, which consists of the inputs of the phases so far, one after the other, lies from
cell 0 on, and `off` is the first cell after it. 

### `InputsAt.first`

 The input of the first phase is written from cell 0 on. 

### `InputsAt.next`

 The input of the next phase is written after the inputs so far. 

### `InputsAt.sameOutside`

 Writing the input of the next phase changes only the cells of this input. 

### `InputsAt.keep`

 A phase that changes no cell below `off` keeps the inputs. 

 ## From a procedure to a phase 

### `phase_of_ends`

 A phase: the outermost call of procedure p. 

### `phase_of_meets`

 A phase: the outermost call of a procedure that meets a specification. 

 ## Runs in phases 

### `LightPhases`

 The phases of the list are run one after the other, starting from the memory μ.  A phase is the
number of a procedure of P, its input, and its number of steps.  The last memory, with the address
of the first cell after the last input, satisfies good. 

### `input_withInput`

 Writing the input of a phase. 

### `input_run`

 One phase. 

### `runsPhases_of_light`

 **All phases.**  If the procedures of a light program run in phases, the compiled programs run
in phases on the word RAM, phase j within ramSteps P false cⱼ steps. 

### `runsPhases_start`

 **From the empty memory**, at every admissible word size. 

 ## Compiling the phases 

### `runsPhases_mono`

 `RunsPhases` still holds if the condition on the last memory is weakened. 

### `within_ramSteps`

 If a phase takes c ≤ A (n^a + 1) steps of the program, the compiled phase is `Within` the same
bound, with a constant that depends on the program and on A only. 

### `PhaseRun`

 What is left to show about a program that runs in phases, at the size `n` and for given inputs.
The list `l` has, for each phase, the number of its procedure, its input and its number of steps. 

### `PhaseRun.small`

 The limits are polynomial in `n`. 

### `PhaseRun.sizes_le`

 The sizes of the matrices fit in a word. 

### `PhaseRun.steps`

 The phase with the exponent `a` takes at most `A (n^a + 1)` steps. 

### `PhaseRun.run`

 The procedures run the phases within the limits, from the empty memory, and the memory is as
  it should be at the end. 

### `PhaseRun.compile`

 **The compiled phases.**  If every number of the inputs fits in a word, the compiled procedures
run the phases on the word RAM at every admissible word size, each a constant times as long as in
the program, and the output cells hold what the last memory of the program holds. 
