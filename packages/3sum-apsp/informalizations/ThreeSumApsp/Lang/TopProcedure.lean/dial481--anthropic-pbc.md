---
{
  "module": "ThreeSumApsp/Lang/TopProcedure.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/TopProcedure.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/TopProcedure.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# From a solver of a task to a program for the layout of the end statement

A solver gets its size, the bound on the numbers and its addresses as arguments.  A problem of the
end statement has a fixed layout: cell 0 holds the size n, then comes the input, then the output;
the bound U = n^κ is not in the memory.  For every κ one more procedure, `topBody`, is appended to
the program of the solver.  It reads n.  At size 0 it answers at once.  Otherwise it forms U = n^κ
by κ multiplications and n², computes the addresses, calls the solver, and returns the result of
the solver (for a decision problem) or 1.

`Wrap` collects what has to be said about a problem and a task for this to work.  `Wrap.body_ends`
and `Wrap.body_ends_zero` follow the procedure through its text, `Wrap.small` bounds the word size,
the memory and the depth that the run needs by a polynomial in n, and `Wrap.realized` is the
conclusion: if the task is solved in time T, then the problem is solved on the word RAM within a
constant times T.


### `powStmt`

 Local 2 is multiplied κ times by local 1. 

### `topBody`

 The outermost procedure.  Local 1 is n, the content of cell 0.  At size 0 the result is 0 for a
decision problem and 1 for a problem with an output.  Otherwise local 2 is U = n^κ, local 3 is n²,
and the arguments of the solver are expressions in these three; for a problem with an output the
result of the solver is replaced by 1. 

### `pow_spec`

 The loop that is written out κ times turns U = 1 into U = n^κ. 

### `safe_fourAddresses`

 The arguments n, U and four addresses 1, 1 + n², 1 + 2n², 1 + c n² are safe. 

### `verdictOf_flag`

 The verdict that belongs to the result of a decision procedure. 

 ## The problems of `EndStatement` 

### `ofEnd_cell0`

 Cell 0 holds the size. 

### `ofEnd_input_le`

 All cells of the input are within the size and the bound. 

### `safe_cell0`

 Cell 0 may be read. 

 ## Polynomials in the size 

### `polyBound_pow_le`

 A polynomial in `n` and `U = n^κ` is a polynomial in `n`. 

### `Wrap`

 What connects a problem in the layout of the end statement with a task. 

### `Wrap.cst`

 The input and the output take at most cst (n² + 1) cells. 

### `Wrap.args`

 The arguments of the solver, the free pointer last, as expressions in the locals 1 (n), 2 (U)
  and 3 (n²). 

### `Wrap.inst`

 The instance of the task. 

### `Wrap.fr`

 The free pointer: the first cell after the output. 

### `Wrap.vals`

 The expressions have the values that the solver expects. 

### `Wrap.safe`

 They may be evaluated as soon as the addresses of the input and the output fit in a word. 

### `Wrap.zero`

 At size 0 it is right to reject, for a decision problem, and to accept, whatever the output
  cells hold, for a problem with an output. 

### `Wrap.pre`

 The input meets the precondition of the task. 

### `Wrap.post`

 What the task promises is a right answer. 

### `bodySteps`

 The steps of the outermost procedure, beside those of the solver. 

### `extra`

 The steps of the outermost procedure and of its call, beside those of the solver. 

### `limits`

 The limits of the run on an instance. 

### `Room`

 What the run asks of the limits. 

### `Room.cells`

 The addresses of the input and the output fit in a word. 

### `Room.bound`

 The bound on the numbers, and 1, fit in a word. 

### `Room.solver`

 The solver, called at depth 2 with the free pointer behind the output, has what it needs. 

### `room`

 The limits of the run leave that room. 

### `Answered`

 The final state holds a right answer to the instance. 

### `body_ends`

 The run of the outermost procedure on an instance of size at least 1. 

### `body_ends_zero`

 The run of the outermost procedure on an instance of size 0. 

### `ends_of_body`

 The outermost call, from the run of its procedure. 

### `small`

 The limits are polynomial in the size. 

### `topSolves`

 The compiled program is run within these limits: what the interface to the machine asks for. 

### `realized`

 **If the task is solved in time T, the problem is solved on the word RAM within a constant times
T.** 
