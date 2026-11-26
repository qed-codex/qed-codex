---
{
  "module": "ThreeSumApsp/Lang/Syntax.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Syntax.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Syntax.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The light language

A small imperative language with procedures and recursion, in which the paper's procedures can be
written almost as printed.  It is a proof device: a program of this language is compiled
(`compileProgram`) to the word RAM of the end statement, and the compiler is proved to keep results
and, up to a constant factor that depends on the program text only, step counts.

* A program is a finite piece of data: a list of procedure bodies.  It contains no Lean functions.
* The memory is an array of integers addressed by natural numbers.  Each running procedure has local
  variables 0, 1, 2, ….
* Arithmetic: +, −, ×.  There is no division.  Comparisons (<, =) occur as the tests of if and
  while.
* Every executed operation costs one step: each constant, variable, operation and load of an
  expression, each comparison, assignment, store, branch, call and return.
* A run is subject to limits: it forms no value of absolute value above `word`, touches no cell at
  an address ≥ `space`, and nests calls at most `depth` deep.  A run that would break a limit does
  not exist.


### `Op`

 The operations on two words. 

### `Op.eval`

 The result of an operation. 

### `Expr`

 Expressions: constants, local variables, operations, and the content of the memory cell at an
address. 

### `Cond`

 Tests. 

### `Stmt`

 Statements.  `call p args x` runs procedure number p on the values of args and puts its result
into x. 

### `Program`

 A program: the bodies of its procedures, numbered from 0. 

### `State`

 What a running procedure sees: its local variables and the memory. 

### `Limits`

 The limits on a run: largest absolute value of a word, number of memory cells, nesting depth of
calls. 

### `Expr.val`

 The value of an expression. 

### `Expr.cost`

 The number of steps that evaluating an expression takes: one for each of its constants,
variables, operations, loads. 

### `Limits.Addr`

 An address within the limits. 

### `Expr.Safe`

 The evaluation of an expression stays within the limits: every value that is formed fits in a
word, and every address that is read is within the memory. 

### `Cond.Holds`

 Whether a test holds. 

### `Cond.cost`

 The number of steps of a test: its two sides and the comparison. 

### `Cond.Safe`

 The evaluation of a test stays within the limits. 

### `frame`

 The local variables of a procedure that has just been called: the arguments in 0, 1, …, and 0 in
all others. 

### `memOf`

 The memory that holds the list ws in the cells 0, 1, 2, … and 0 elsewhere. 

### `Exec`

 `Exec lim P d s σ σ' c`: within the limits lim, and at nesting depth d of calls, the statement
s of the program P, started in the state σ, ends in the state σ' after exactly c steps. 

### `State.Bounded`

 Everything held in a variable or in a cell fits in a word. 
