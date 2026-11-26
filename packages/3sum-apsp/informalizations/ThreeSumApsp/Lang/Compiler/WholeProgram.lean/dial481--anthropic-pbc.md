---
{
  "module": "ThreeSumApsp/Lang/Compiler/WholeProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Compiler/WholeProgram.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Compiler/WholeProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The compiler is correct on whole programs

`compileProgram_correct`: if the call of procedure p0 of the light program P ends after c
steps, the compiled program gives its verdict within `ramSteps P dec c` = c₀ + K c steps, where c₀
and K depend on the text of P (and on dec) only.  If the memory of the machine held the memory of
the light program and the two arguments before (`Input`), it holds the final memory afterwards, with
the result in the cell -3 (`Outcome`).

The run of the machine has three parts.

1. The start-up code (`steps_start`) leads to a memory that represents the first state
   (`rel_startMem`).
2. The outermost statement is the call of p0.  The compiled program satisfies what the simulation
   theorem assumes (`setting`, `start_mainStmt`), so `sim` gives a run of at most K c steps to a
   memory that represents the last state.
3. The code that follows copies the result to the cell -3 and gives the verdict (`steps_tail`).

Each part comes with the set of cells that it may change.  The cells below `-lowCell` and the cells
from `lim.space` on are in none of the three sets (`not_mem_of_far`), and neither are the cells -1
and -2.

The notions of the compiler and of its proof are in the namespace `Light.Compiler`.  The statements
about programs name four of them, which are in `Light`: `compileProgram`, `mainStmt`, `verdictOf`,
`ramSteps`.  The passage to the notions of the word RAM also uses `compileProgram_correct` with
`Fits`, `Holds`, `Input` and `Outcome`, the cells `cARG1`, `cARG2`, `cRESULT`, and the numbers
`startCost`, `stepsPerStep`, `dispPos`, `frameSize`, `stackCells`, `lowCell`.


 ## The verdict 

### `_root_.Light.verdictOf`

 The verdict: accept, or, if dec is set, accept exactly if the result is positive. 

### `Verdict`

 What the code that follows the outermost statement leaves, if it starts in the memory m and the
result is r: the machine is about to give the verdict, the cell `cRESULT` holds the result, and only
that cell and the register D have changed. 

### `steps_tail`

 The code that follows the outermost statement gets there in at most three steps. 

 ## Time and space of the compiled program 

### `startCost`

 A bound for the number of steps of the compiled program outside the outermost statement:
`dispPos` + `frameSize` + 9 before it (`steps_start`), at most three after it (`steps_tail`), and
the verdict. 

### `_root_.Light.ramSteps`

 A bound for the number of steps of the compiled program, for c steps of the light program. 

### `stackCells`

 The number of cells of the stack that a run within the limits needs. 

### `lowCell`

 A bound for the extent of the negative cells that the compiled program uses: the stack ends
before the cell -2 · stackCells, and the pool, which reaches further down than the temporaries, ends
at the cell -(25 + 4 · dispPos). 

 ## The setting of the simulation theorem 

### `setting`

 The compiled program, with its numbers, satisfies what the simulation theorem assumes once and
for all. 

### `start_mainStmt`

 The outermost statement is at `mainPos` and runs in the frame `mainFrame`. 

### `not_mem_of_far`

 The cells below `-lowCell` and the cells from `lim.space` on are not among those that the
start-up code, the outermost statement or the code for the verdict may change. 

 ## The theorem 

### `Holds`

 The cells 0, 1, 2, … of the memory m of the machine hold the memory μ of the light language,
and μ holds words. 

### `Input`

 What a run of a compiled program needs in the memory m: the memory μ of the light language, and
the arguments i and j, which are words, in their two cells. 

### `Outcome`

 What a run of a compiled program from the memory m leaves in the memory m', if the light run
ends in σ'. 

### `Outcome.holds`

 The cells 0, 1, 2, … hold the final memory. 

### `Outcome.result`

 The cell for the result holds the result. 

### `Outcome.arg1`

 The first argument is still there. 

### `Outcome.arg2`

 The second argument is still there. 

### `Outcome.far`

 The cells far below 0 and the cells from lim.space on are unchanged. 

### `compileProgram_correct`

 **The compiler is correct.**  Let the call of procedure p0 of the program P on the arguments i,
j and the memory μ end after c steps within the limits, and let the word size fit the limits.  Then
the compiled program, started on any memory whose cells `a ≥ 0` hold the words of μ and whose
cells -1 and -2 hold i and j, gives its verdict within `startCost + stepsPerStep · c` steps.  Then
the cell -3 holds the result of the procedure and the cells `a ≥ 0` hold the final memory.  The
cells -1 and -2, the cells below `-lowCell` and the cells from `lim.space` on are unchanged.  The
two constants of the time depend on the text of P and on dec only. 
