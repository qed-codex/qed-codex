---
{
  "module": "ThreeSumApsp/Lang/ToMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/ToMachine.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/ToMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# From runs of light programs to the running-time notions of the word RAM

`Solves` says what it means that a program of the word RAM solves a problem within a time bound, and
`IsDataStructure` that two programs form a data structure.  This file gives the corresponding
notions for light programs (`ProgramSolves`, `ProgramIsDataStructure`; what they ask on one instance
are the structures `ProgramSolvesAt` and `ProgramIsDataStructureAt`), which speak only about `Exec`,
and proves that the compiled programs satisfy the notions of the word RAM with time C · T + C, where
C depends on the compiled program only (`solves_of_programSolves`, `isDataStructure_of_program`).

1. **Word size.**  The limits of the run are polynomial in the parameters of the instance (`Small`),
   so they fit every admissible word size of slope `slopeOf` (`fits_of_small`).
2. **Time and space.**  c steps become at most C · c + C steps (`ramSteps_le`); calls nested d deep
   reach at most C · d + C cells below 0 (`lowCell_le`).
3. **Runs.**  Each run is one use of `compileProgram_correct`.  A solver is one run from the initial
   memory (`input_loadWords`).  A data structure is one such run for the preprocessing and then an
   induction on the list of queries, each of them one run (`serves_of_program`).
4. **From specifications.**  The runs that the two notions ask for come from specifications of the
   procedures (`Meets.main`, `AnswersQueries.of_meets`).
5. **The additive constant.**  If T ≥ 1, the bound C · (A · T) + C is at most C (A + 1) · T
   (`solves_of_programSolves_scaled`, `isDataStructure_of_program_scaled`).


 ## The notion for light programs 

### `Small`

 The limits are at most 2^s ((p₁ + 1) (p₂ + 1) ⋯)^k in the parameters of the instance. 

### `ProgramSolvesAt`

 What is asked of the run of procedure p0 on the instance x: within the limits lim it ends in the
state σ' after c steps. 

### `ProgramSolvesAt.run`

 The run starts on the memory that holds the input of the problem. 

### `ProgramSolvesAt.time`

 It ends within the time bound. 

### `ProgramSolvesAt.input_fits`

 The numbers of the input fit in a word. 

### `ProgramSolvesAt.small`

 The limits are polynomial in the parameters of the instance. 

### `ProgramSolvesAt.answer`

 The result gives the verdict, and the cells after the input hold the output. 

### `ProgramSolves`

 **A light program solves a problem.**  Procedure p0 of P, called on the memory that holds the
input of the problem, ends within T x steps and within limits that are polynomial in the
parameters; its result gives the verdict (if dec: accept exactly if the result is positive;
otherwise accept), and the cells after the input hold the output. 

### `Meets.main`

 **The outermost statement calls a procedure that meets a specification.**  The call costs four
steps, and B is any real bound for the time. 

 ## The word size 

### `textBound`

 A number that depends on the compiled program only: times the polynomial bound on the limits,
it exceeds all four numbers that have to fit in a word (`Fits`). 

### `textBoundBits`

 The number of binary digits of that number. 

### `slopeOf`

 The slope of the word size for a compiled program: the exponents s and k of the bound
2^s ((p₁ + 1) ⋯ (p_r + 1))^k on the limits, and the bits for the numbers that the compiled code
itself forms (offsets in a frame, positions in the code). 

### `fits_of_lt`

 The word size fits the limits if the limits, the largest number N of the pool and the number Q
of cells of the stack, with the factors of `Fits`, are below a number B ≤ 2^W. 

### `fits_of_small`

 Limits that are polynomial in the parameters fit every admissible word size. 

 ## Time and space 

### `timeConst`

 The constant of the time and space bounds of a compiled program: the two constants of the time,
and the extent of the negative cells that are in use before any call. 

### `ramSteps_le`

 The time of a compiled program. 

### `lowCell_le`

 The space of a compiled program below the cell 0. 

### `far_of_space`

 A cell that lies more than C · S + C cells before or after the input is out of the reach of a
run whose limits on addresses and on the nesting of calls are given by S. 

 ## Runs from the initial memory 

### `input_loadWords`

 The initial memory holds the input, and zeros in the cells of the two arguments. 

### `Compiler.Holds.output`

 Reading the output: a cell of a memory that holds μ, as a signed word. 

 ## Solvers 

### `solves_of_programSolves`

 **The compiled program solves the problem on the word RAM**, within C · T + C steps, C depending
on the compiled program only. 

 ## The two-stage data structure 

### `AnswersQueries`

 From every memory with the property DS, procedure pQ, called on I and J, returns the entry
(I, J) of the product within T steps and leaves a memory with the property DS. 

### `AnswersQueries.of_meets`

 Queries are answered if the procedure meets the corresponding specification. 

### `ProgramIsDataStructureAt`

 What is asked of the two procedures on the instance x, with the limits lim and the property DS
of memories, "holds the data structure for X and Y". 

### `ProgramIsDataStructureAt.small`

 The limits are polynomial in N and D. 

### `ProgramIsDataStructureAt.index_fits`

 The indices of rows and columns fit in a word. 

### `ProgramIsDataStructureAt.input_fits`

 The numbers of the input fit in a word. 

### `ProgramIsDataStructureAt.space`

 The space bounds the addresses after the input. 

### `ProgramIsDataStructureAt.depth`

 The space bounds the nesting of calls. 

### `ProgramIsDataStructureAt.pre`

 The preprocessing, on the memory that holds the input, establishes DS. 

### `ProgramIsDataStructureAt.query`

 Every query needs and keeps DS. 

### `ProgramIsDataStructure`

 **A light program is a data structure for the entries of a thin matrix product.**  Procedure
pPre of P is the preprocessing, procedure pQ the query, with arguments I and J and the entry as its
result. 

### `Compiler.Holds.withQuery`

 Writing a query into the cells of the two arguments does not touch the cells 0, 1, 2, …. 

### `serves_of_program`

 **The queries.**  From a memory that holds the data structure, the compiled query procedure
serves every list of queries: each query is one run, and leaves a memory that holds the data
structure. 

### `isDataStructure_of_program`

 **The two compiled programs are a data structure on the word RAM**: queries are put into the
cells -1 and -2 (`cARG1`, `cARG2`) and answered in the cell -3 (`cRESULT`). 

 ## Absorbing the additive constant 

### `scaled_le`

 C · (A · T) + C ≤ C (A + 1) · T if T ≥ 1. 

### `solves_of_programSolves_scaled`

 The form in which the running-time theorems need it: if the light program takes at most A · T
steps and T ≥ 1 on the domain, the compiled program takes at most C · T steps, where
C = timeConst · (A + 1). 

### `isDataStructure_of_program_scaled`

 If preprocessing, space and queries of the light program are at most A times bounds that are at
least 1 on the domain, those of the compiled programs are at most C times these bounds, where
C = timeConst · (A + 1). 
