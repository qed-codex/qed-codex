---
{
  "module": "ThreeSumApsp/Lang/Compiler/Cells.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Compiler/Cells.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Compiler/Cells.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The cells of the compiled code, and the memories that represent a state

The memory of the machine is one array indexed by the integers, and the compiled code keeps its
registers, temporaries, pool, stack and the memory of the light language in different parts of it.
Every proof about compiled code has to know that a write to one cell leaves the others alone.  This
file settles that once.

* Sets of cells: `Temps k F` (what evaluating an expression into T_k may change), `Scratch F` (what
  any compiled code uses freely), `Constants N` (what no compiled statement changes), `Writable Z q`
  (what a statement that runs in the frame q may change), and two parts of the memory, `Stack q Q`
  and `Pool N`.  "The memories m and m' differ only inside s" is `AgreeOutside s m m'`.
* The tactic `cells` proves that two cells are different, that a cell is or is not in one of these
  sets, or that one of these sets lies in another.  The tactic `cell_read` reads a cell of a memory
  that is given by writes.
* `Sizes W` collects the numbers that never change, with the assumptions on them: the layout of the
  code, the limits, the number of stack cells, and a word size W that fits them (`Fits`).
* `Rel Z σ q m`: the memory m represents the state σ in the frame q.  The relation survives changes
  of scratch cells (`Rel.same`) and of the stack beyond the frame (`Rel.beyond`); a write to the
  cell of a local variable or to a memory cell is the same write in the state (`Rel.setLoc`,
  `Rel.setMem`).  All four come from `Rel.of_agreeOutside`.  `Framed` adds that the frame lies
  within the stack.
* Two pieces of code that occur everywhere: the jump (`steps_jump`) and the two instructions that
  store a cell in a local variable (`steps_setVar`).

**Letters**, in this file and in the files on expressions, tests, calls and the simulation.
Numbers: W is the word size, F the number of local variables of a frame, N the largest number in the
pool, Q the number of stack cells, q a frame, pos a position in the code.  The temporaries are
written T₀, T₁, …, T_j; there are 2 F + 1 of them.
Facts: m, m₁, m₂, … are memories in the order in which they arise.  Z is a `Sizes`.  R says that a
memory represents a state (`Rel`), I the same with the frame inside the stack (`Framed`).  A says
that two memories agree outside a set of cells (`AgreeOutside`); A₂ speaks of m₂.  run is a run of
the machine (`Steps`).  val, va, vb say which number a cell holds.  hcode and names that end in Code
say where a piece of code is (`CodeAt`).


 ## The numbers that never change 

### `Fits`

 The word size is large enough for the limits: words hold 2 · word + 2 (so the difference of two
values, and one less, is in range), all addresses of the memory, all addresses of a stack of Q
cells, and all numbers 0, …, N of the pool. 

### `Fits.inRange`

 A number within the limit on words is in the range of words. 

### `Sizes`

 The numbers on which the proofs about compiled code depend: the layout of the code, the limits
on the runs of the light program, and the number of stack cells.  The pool holds the numbers from 0
to the position of the dispatcher. 

### `Sizes.lim`

 The limits on the runs of the light program. 

### `Sizes.Q`

 The number of stack cells. 

### `Sizes.fits`

 The word size fits the limits, the pool and the stack. 

### `Sizes.offsets_le`

 The pool holds the numbers up to 2 (F + 1), which are the offsets in a frame. 

 ## Sets of cells 

### `Temps`

 What the evaluation of an expression into T_k may change: ADDR and the temporaries T_j with
k ≤ j ≤ 2 F. 

### `Stack`

 The stack cells j with q ≤ j < Q. 

### `MainFrame`

 The cells of the local variables of the outermost frame. 

### `Pool`

 The cells of the pool that hold the numbers 0, …, N. 

### `Constants`

 The cells that the start-up code fills and no compiled statement changes: the registers for 1,
0, -1 and the pool. 

### `Scratch`

 The cells that compiled code uses freely: the registers D, RET, RR, NFP, ADDR and the
temporaries. 

### `Writable`

 What the code of a statement that runs in the frame q may change: scratch cells, FP, the stack
cells from q on, and the memory cells within the limits. 

 The temporaries, the stack and the pool are arithmetic progressions of cells. 

### `cells`

 Proves that two cells of the compiled code are different, that a cell is or is not in one of the
sets above, or that one of these sets lies in another or in its complement.  A cell is given by its
name (cFP, cT j, cStack j, …) or is an integer that the context bounds.  The names and the sets are
replaced by their definitions; what remains are inequalities between integers, which follow from
those of the context, such as 1 ≤ q. 

### `cell_read`

 Reads a cell of a memory that is given by writes: it goes through the writes from the last to
the first, until it meets a write to the cell itself or no write is left. 

### `cell_read`

 Reads a cell of a memory that is given by writes to other cells of a memory in which, by h, the
cell holds the number in question. 

### `temps_subset_scratch`

 What an expression may change is scratch. 

### `scratch_subset_writable`

 A statement may change scratch cells. 

### `stack_subset_writable`

 A statement may change the stack from its frame on. 

### `writable_subset_writable`

 A statement in a later frame may change less. 

### `mem_writable_of_addr`

 A statement may change the memory cells within the limits. 

 ## Addresses, and numbers that fit in a word 

### `cStack_sub`

 The cell of the local variable x of the frame q, computed from FP and the pool. 

### `cStack_add`

 Back from the frame q + x to the frame q. 

### `cStack_succ_add`

 The stack cell before the cell q + 1. 

### `Sizes.inRange_stack`

 The addresses of the stack fit in a word. 

### `Sizes.inRange_addr`

 The addresses of the memory fit in a word. 

### `Sizes.inRange_neg_one`

 The number -1, on which every jump branches, fits in a word. 

 ## The relation between a state of the light language and a memory of the machine 

### `Rel`

 The memory m of the machine represents the state σ of a procedure whose frame is at q. 

### `Rel.of_agreeOutside`

 After a change that spares the numbers 1, 0, -1 and the pool, the new memory represents a state
as soon as FP, the local variables and the memory cells are right. 

### `Rel.same`

 A memory that differs only in scratch cells represents the same state. 

### `Rel.beyond`

 A memory that differs only in scratch cells and in the stack beyond the frame represents the
same state.  (Here and below 1 ≤ q is needed because stack cell 0 is memory cell 0.) 

### `Rel.setLoc`

 Writing a local variable. 

### `Rel.setMem`

 Writing a memory cell. 

### `Rel.read`

 Reading a memory cell. 

### `Rel.loc_zero`

 The cell to which FP points is local variable 0. 

### `Framed`

 The memory m represents the state σ in the frame q, and the frame lies within the stack: after
stack cell 0 and before stack cell Q. 

 ## Two pieces of code that occur everywhere 

### `Framed.same`

 A memory that differs only in scratch cells represents the same state in the same frame. 

### `steps_jump`

 An unconditional jump. 

### `steps_setVar`

 The two instructions that put the content v of the cell c into the local variable x. 
