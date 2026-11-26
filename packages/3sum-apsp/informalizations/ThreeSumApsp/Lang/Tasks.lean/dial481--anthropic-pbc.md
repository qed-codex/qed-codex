---
{
  "module": "ThreeSumApsp/Lang/Tasks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Tasks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Tasks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Problems, solvers, and the interpretation of "is solved in time T" in the light language

A *task* is a problem together with a calling convention: which arguments a procedure gets, what the
memory holds when it is called, and what the result and the memory have to be when it returns.
`Solves task P p T need` says that procedure number `p` of the program `P` solves the task within
`T` steps, if the limits of the run allow for `need`.  A reduction of the paper is a *host*: a
procedure that calls an arbitrary solver of another task.

Conventions.

* A solver gets sizes, a bound `U` on the absolute values of the numbers, the addresses of its
  arrays, and as last argument the free pointer `fr`.  All inputs and outputs lie below `fr`.  The
  solver may write its output segments and any cell from `fr` on, and no other cell.  Nothing is
  assumed about the cells from `fr` on, so a solver can be called again and again.
* A solver has to be correct for every valid bound `U` that it is given.
* A solver is a pair of a program and a procedure number.  What is proved about it holds for every
  program that begins with this program, so a host appends its own procedures.

A `Task` is a problem whose time and need depend on a size and a bound.  `TaskN` and `SolvesN` are
the same notions with a list of parameters.


 ## Limits 

### `Need`

 What a run needs: the largest absolute value it forms, the number of cells it uses from the free
pointer on, and the number of levels of calls below the procedure. 

### `Need.Ok`

 The limits allow for the need of a procedure that is called at depth `d` with the free pointer
`fr`.  An address always fits in a word. 

### `Need.Ok.mono`

 A smaller need is allowed for if a larger one is, also with a larger free pointer and at a
larger depth if the sums are not larger. 

### `PolyNeed`

 A need that depends on a size and a bound is polynomially bounded in the two: by
`2^s ((n + 1) (U + 1))^k`. 

 ## Specifications of single routines 

### `Seg.of_kept`

 A list below fr stays where it is if nothing below fr changes. 

 ## Tasks and solvers 

### `Task`

 A problem with a calling convention. 

### `Task.Inst`

 The instances, as they lie in the memory: sizes, bound, addresses, contents. 

### `Task.size`

 The size of an instance. 

### `Task.bound`

 The bound on the absolute values of its numbers that is handed to the solver. 

### `Task.args`

 The arguments of the call, without the free pointer, which comes last. 

### `Task.Pre`

 The instance is valid, and it lies in the memory below the free pointer. 

### `Task.Post`

 The result and the final memory are right.  (That the cells below the free pointer are
  otherwise unchanged is part of this.) 

### `Solves`

 **Procedure `p` of the program `P` solves the task** within `T (size) (bound)` steps, whenever
the limits allow for `need (size) (bound)`; and so it does in every program that begins with `P`. 

### `Solves.append`

 A solver stays a solver when procedures are appended to its program. 

### `Solves.meets`

 **A solver meets the specification that its task prescribes**, in every program that begins with
its program. 

### `SolvedIn`

 "The task is solved in time `T`", for a real-valued `T` whose second argument is an upper bound
on the numbers: some solver with a polynomially bounded need takes at most `T n u` steps on every
instance of size `n ≥ 1` with a bound `1 ≤ U ≤ u`. 

### `SolvedIn.mono`

 A larger bound on the running time is still a bound on the running time. 

### `timeUpTo`

 The largest time `Tn n U` for a bound `U ≤ u`.  A program has a natural number as the bound on
its numbers, and a claim on running times a real number. 

### `timeUpTo_le`

 What bounds the time for every natural number `U ≤ u` bounds `timeUpTo`.  For a negative `u`
there is still `U = 0`. 

### `Solves.solvedIn`

 A solver with a polynomially bounded need solves its task in its own time. 

 ## Hosts 

### `IsHost`

 A host from the task `lower` to the task `upper`: from every solver of `lower` it makes a solver
of `upper`, by appending procedures, whose time and need are given functions of those of the solver,
and whose need stays polynomially bounded. 

### `IsHost.solvedIn`

 From a host to a transfer of running times.  What remains is arithmetic: a bound for the host's
time function, given a bound for the solver's. 

 ## Tasks with a list of parameters 

### `TaskN`

 A problem with a calling convention and a list of parameters. 

### `TaskN.Inst`

 The instances, as they lie in the memory. 

### `TaskN.pars`

 The parameters on which time and need depend. 

### `TaskN.args`

 The arguments of the call, without the free pointer, which comes last. 

### `TaskN.Pre`

 The instance is valid, and it lies in the memory below the free pointer. 

### `TaskN.Post`

 The result and the final memory are right. 

### `SolvesN`

 Procedure `p` of the program `P` solves the task within `T pars` steps, whenever the limits
allow for `need pars`; and so it does in every program that begins with `P`. 

### `SolvesN.append`

 A solver stays a solver when procedures are appended to its program. 

### `SolvesN.meets`

 A solver meets the specification of its task, at the depth d at which it runs. 

### `PolyNeedN`

 A need that is polynomially bounded in the parameters. 
