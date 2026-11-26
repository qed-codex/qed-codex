---
{
  "module": "ThreeSumApsp/Lang/Compiler/StatementCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Compiler/StatementCode.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Compiler/StatementCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The compiler from the light language to the word RAM: cells, and the code of statements

This file holds the definitions: the cells, the code of expressions, tests, statements, calls and
returns, the length of each piece of code, and the one condition on the text of a program (its
width).  The code of a whole program, `compileProgram`, puts these pieces together.

**Cells.**  A memory cell a of the light language is the cell a ≥ 0 of the machine.  Everything else
lives in negative cells.  A whole program takes two arguments from the cells -1 and -2 (`cARG1`,
`cARG2`) and puts its result into the cell -3 (`cRESULT`); the cell -4 is not used.  Odd cells from
-5 down hold the registers of the compiled code, the temporaries T₀, T₁, … for the evaluation of
expressions, and a pool of numbers: the cell `cPool n` holds the number n, for all n up to the
largest position to return to.  Even cells hold the call stack: stack cell j is the cell -2 j
(`cStack`).  The outermost frame of a whole program begins at stack cell `mainFrame` = 4, so the
code of its statements writes no stack cell before the cell -8 and leaves the cells -1, …, -4
alone.  The lemmas about pieces of code ask less: only that a frame begins after stack cell 0.

**Numbers.**  The constants of the program text are built from their binary digits where they are
needed.  The numbers that the compiled code itself needs, offsets in a frame and positions to return
to, come from the pool: the length of the code that builds a number from its digits depends on the
number, and a position to return to depends on the lengths.

**Frames.**  With F local variables per procedure, the frame of a running procedure is given by a
number q: local variable x is the cell -2 (q + x), the position to return to is in the
cell -2 (q - 1), and the register FP holds -2 q.  A call moves q to q + F + 1.

**Jumps.**  The machine only has "branch if negative" to a fixed position.  An unconditional jump
tests a register that holds -1.  A return loads the position r to return to into the register RR and
jumps to the dispatcher, the code "RR := RR - 1; if RR < 0 go to j" for j = 0, 1, 2, …, which
arrives at position r after 2 (r + 1) steps: a constant for a fixed program.

**Calls.**  The caller evaluates the arguments into temporaries, computes the address of the new
frame, fills its local variables (arguments first, then zeros), stores the position to return to,
moves FP and jumps to the procedure.  The procedure ends with its return sequence: result into RET,
position into RR, FP back to the caller's frame, jump to the dispatcher.  Back in the caller, RET is
stored into the variable that receives the result.

**Lengths.**  A jump forward needs the length of code that is not yet written, so the lengths are
defined on the text (`Expr.size`, `Cond.size`, `Stmt.size`) and then shown to be the lengths of the
code (`length_compileExpr`, `length_compileCond`, `length_compileStmt`).


 ## Cells

The names of the registers are written in capitals, as in the comments on the code. 

### `cARG1`

 The cell from which a whole program takes its first argument. 

### `cARG2`

 The cell from which a whole program takes its second argument. 

### `cRESULT`

 The cell into which a whole program puts its result. 

### `cONE`

 The register that holds 1. 

### `cZERO`

 The register that holds 0. 

### `cNEG`

 The register that holds -1; an unconditional jump branches on it. 

### `cFP`

 The frame pointer FP: the address of local variable 0 of the running procedure. 

### `cADDR`

 The register ADDR: the address for the next load or store of a local variable. 

### `cRET`

 The register RET: the result of the procedure that has just returned. 

### `cRR`

 The register RR: the position to return to, counted down by the dispatcher. 

### `cNFP`

 The register NFP: the frame pointer of the procedure that is about to be called. 

### `cD`

 The register D: the difference that a test branches on. 

### `cT`

 The temporaries. 

### `cPool`

 The pool of numbers. 

### `cStack`

 The cell number j of the stack. 

### `mainFrame`

 The frame of the outermost statement of a whole program: the first whose cells lie beyond the
cells of the arguments and the result. 

 ## Expressions and tests 

### `_root_.Light.Op.instr`

 The instruction of the machine for an operation. 

### `digitsCode`

 Code that builds in the cell c the number with the given binary digits, least significant digit
first: the number of the higher digits, doubled, plus the lowest digit. 

### `digitsLen`

 The length of `digitsCode c L`. 

### `compileExpr`

 Code that leaves the value of the expression in the temporary T_k, using only T_k, T_{k+1}, …
and ADDR.  A constant is built from its binary digits, in at most 2 log₂ n + 3 instructions. 

### `_root_.Light.Expr.size`

 The length of the code of an expression. 

### `compileCond`

 Code that goes on to the next position if the test holds and jumps to the position l if it does
not.  Both tests evaluate a into T₀ and b into T₁.  For a < b the code forms D = b - a - 1 and
leaves if D < 0.  For a = b it forms D = a - b and leaves if D < 0, then forms -D and leaves if that
is negative. 

### `_root_.Light.Cond.size`

 The length of the code of a test. 

 ## Statements 

### `CodeLayout`

 What the code of a statement needs to know about the whole program. 

### `CodeLayout.F`

 The number of local variables of every frame. 

### `CodeLayout.entry`

 The positions of the procedures. 

### `CodeLayout.disp`

 The position of the dispatcher. 

### `argsCode`

 The arguments of a call, evaluated into T_k, T_{k+1}, …. 

### `argsSize`

 The length of the code for the arguments of a call. 

### `frameInit`

 The local variables of the new frame: the first n from the temporaries, the others 0. 

### `newFrame`

 The code of a call between the arguments and the jump to the procedure: the address of the new
frame into NFP, its local variables, the position ret to return to, and FP := NFP. 

### `callCode`

 A call up to and including the jump to the procedure; ret is the position after the jump. 

### `callSize`

 The length of a call up to and including the jump. 

### `_root_.Light.Stmt.size`

 The length of the code of a statement. 

### `compileStmt`

 The code of a statement, for the position pos. 

### `epilogue`

 The return sequence of a procedure: the result (local variable 0) into RET, the position to
return to into RR, the frame of the caller, and the jump to the dispatcher. 

### `epilogueSize`

 The length of the return sequence. 

### `dispatcher`

 The dispatcher for the positions below n. 

 ## Lengths 

### `length_compileExpr`

 The code of an expression has the length defined on the text. 

### `length_compileCond`

 The code of a test has the length defined on the text. 

### `length_argsCode`

 The code for the arguments of a call has the length defined on the text. 

### `length_frameInit`

 Two instructions for each local variable of the new frame. 

### `length_newFrame`

 The code between the arguments and the jump has 2 F + 4 instructions. 

### `length_callCode`

 A call up to its jump has the length defined on the text. 

### `length_compileStmt`

 The code of a statement has the length defined on the text. 

 ## The width of a text

The compiled code gives every frame the same number F of local variables.  That is enough if F is at
least the width of every body: a number that bounds the variables, the arguments of each call, and
the temporaries that each expression needs.  Then 2 F + 1 temporaries are enough too: up to F
arguments of a call wait in temporaries while the last one is evaluated in up to F more.  "The width
is at most F" is taken apart by one lemma for each construct. 

### `Expr.vars`

 One more than the largest variable of an expression. 

### `Expr.height`

 The number of temporaries that the code of an expression uses. 

### `Expr.width`

 The width of an expression: at least its variables and its temporaries. 

### `Cond.width`

 The width of a test: that of its two sides. 

### `maxOf`

 The largest value of f on a list. 

### `Stmt.width`

 The width of a statement: at least the width of its expressions, one more than each variable
that it writes, and the number of arguments of each of its calls. 
