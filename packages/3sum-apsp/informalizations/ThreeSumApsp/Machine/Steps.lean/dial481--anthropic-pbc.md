---
{
  "module": "ThreeSumApsp/Machine/Steps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Machine/Steps.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Machine/Steps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Running the word RAM: words, steps, pieces of code, straight-line code, branches

What the proofs about compiled code need to know about the word RAM in which the paper's claims are
stated.

* **Words.**  `wd W v` is the word of the integer v.  If v is in the range of signed words
  (`InRange`), the word gives back v (`toInt_wd`).
* **Steps.**  The end statement defines only whole runs (`exec`).  A configuration (`Cfg`) and a
  single step (`step`) are defined here; `exec_succ_of_step` and `exec_succ_of_verdict` say that
  `exec` takes one step at a time.
* **Runs.**  `Steps P n c c'`: exactly n steps lead from c to c', none of them a verdict.
  Runs are composed by `Steps.trans`; a run that ends before a verdict gives the value of `exec`
  (`exec_of_steps`), and more time does not change that value (`exec_mono`).
* **Code.**  `CodeAt P pos l`: the program P has the instructions of the list l from position pos
  on.
* **Straight-line code.**  Six instructions only change the memory (`Straight`, `effect`); a list
  of them runs through in its length (`steps_straight`).
* **Known numbers.**  On cells that hold the words of known numbers, an instruction writes the word
  of a known number: `effect_add`, …, `effect_store` for the memory; `steps_add`, `steps_sub`,
  `steps_load`, `steps_store` for the step.
* **Branches and verdicts.**  A branch on a cell that holds a known number is `steps_bltz`;
  `Steps.branch` turns its two outcomes into the two outcomes of a test.  The verdicts are
  `step_accept` and `step_reject`.
* **Framing.**  `AgreeOutside s m m'`: the memories m and m' are equal outside the set s of cells.
  For code without stores such a set can be read off the text (`WritesIn`, `agreeOutside_effects`).


 ## Words 

### `InRange`

 The integer v is the signed value of a W-bit word. 

### `wd`

 The word of an integer. 

### `toInt_wd`

 The word of a number in the range of words, read as a signed number, is that number. 

### `wd_toInt`

 Every word is the word of its signed value. 

### `inRange_of_abs_le`

 Numbers of absolute value at most B are in the range of words if 2 B < 2^W. 

### `loadWords_mem_nat`

 The initial memory holds the input in the cells 0, 1, 2, …, followed by zeros. 

### `loadWords_mem_neg`

 The negative cells of the initial memory hold zeros. 

 ## Configurations and single steps 

### `Cfg`

 A configuration of the machine: the position of the next instruction and the memory. 

### `step`

 One step: the next configuration, or the verdict. 

 ## Runs 

### `Steps`

 n steps of the machine, none of which gives a verdict, lead from c to c'. 

### `Steps.trans`

 One run after the other. 

### `Steps.cast_pos`

 A run, with its last position written differently. 

### `Steps.cast_count`

 A run, with its number of steps written differently. 

### `exec_zero`

 Within no steps there is no verdict. 

### `exec_succ_of_verdict`

 A step that gives a verdict ends the run. 

### `exec_succ_of_step`

 After a step that gives no verdict the run goes on, with one step less. 

### `exec_of_steps`

 A run that reaches a verdict. 

### `exec_mono`

 More time does not change the outcome of a run. 

 ## Pieces of code 

### `CodeAt`

 The program P has the instructions of the list l from position pos on. 

### `codeAt_self`

 The whole program, from position 0 on. 

### `CodeAt.left`

 The first part of a piece of code. 

### `CodeAt.right`

 The second part of a piece of code follows the first. 

### `CodeAt.head`

 The first instruction of a piece of code is the one that the machine finds at its position. 

### `CodeAt.tail`

 A piece of code without its first instruction. 

### `CodeAt.cast_pos`

 A piece of code, with its position written differently. 

 ## Straight-line code 

### `Straight`

 The instructions that only change the memory and go on to the next position. 

### `effect`

 What an instruction that only changes the memory does to it. 

### `effects`

 What a list of instructions that only change the memory does to it. 

### `steps_instr`

 One instruction that only changes the memory. 

### `steps_straight`

 A list of instructions that only change the memory. 

 ## Single instructions on cells that hold known numbers 

### `effect_one`

 The only constant. 

### `effect_add`

 The sum of two known numbers. 

### `effect_sub`

 The difference of two known numbers. 

### `effect_mul`

 The product of two known numbers. 

### `effect_load`

 Loading from the address a that the cell j holds. 

### `effect_store`

 Storing at the address a that the cell i holds. 

 ## Branches and verdicts 

### `steps_bltz`

 A branch on a cell that holds the number v: to l if v is negative, else to the next position. 

### `Steps.branch`

 A run that ends with a branch on the sign of v, where v is negative if and only if p fails. 

 ## Framing 

### `AgreeOutside`

 The memory m' differs from m only in cells of the set s. 

### `AgreeOutside.trans_union`

 A change inside s, then a change inside t. 

### `AgreeOutside.cell`

 A cell outside s is unchanged. 

### `AgreeOutside.read`

 A cell outside s still holds v. 

### `AgreeOutside.update`

 Writing a cell of s. 

### `WritesIn`

 The instruction writes no cell outside s, whatever the memory holds. 

### `agreeOutside_effects`

 Code without stores changes only the cells that its instructions name as their targets. 
