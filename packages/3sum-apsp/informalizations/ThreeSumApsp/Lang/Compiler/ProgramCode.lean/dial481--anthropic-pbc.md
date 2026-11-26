---
{
  "module": "ThreeSumApsp/Lang/Compiler/ProgramCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Compiler/ProgramCode.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Compiler/ProgramCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The code of a whole program

`compileProgram P p0 dec` is the program of the word RAM that runs procedure p0 of the light
program P.  With dec = false it accepts at the end of the run; with dec = true it accepts if the
result of the procedure is positive and rejects if not.  It has five parts:

| position | part |
|---|---|
| 0 | `headCode`: the numbers 1, 0, -1, and a jump to the start-up code |
| `mainPos` | `mainCode`: the outermost statement `mainStmt p0`, then the verdict (`tailCode`) |
| `firstBody` | `bodiesCode`: the bodies of the procedures, each with its return sequence |
| `dispPos` | the dispatcher for the positions below `dispPos` |
| `3 * dispPos` | `startCode`: the pool, the outermost frame, and a jump back to `mainPos` |

The start-up code comes last so that no position in the rest of the code depends on its length.

The number `frameSize` of local variables of every frame is read off the text of P: it is the width
of the text.  The pool holds the numbers up to `dispPos`: every position to return to, and with them
the smaller numbers that the code needs (`two_mul_frameSize_add_le_dispPos`).

The facts proved here are about positions only: each part is where the table says
(`codeAt_headCode`, …, `codeAt_startCode`), and every body is at its entry (`codeAt_bodies`).


 ## The number read off the text 

### `frameSize`

 The number of local variables of every frame: the width of the text, and at least 3 for the
outermost frame. 

### `three_le_frameSize`

 The outermost frame has room for the result and the two arguments. 

### `width_le_frameSize`

 Every body fits into a frame. 

 ## The parts of the code 

### `_root_.Light.mainStmt`

 The outermost statement: procedure p0 is called on the local variables 1 and 2 of the outermost
frame, and its result goes to local variable 0. 

### `tailCode`

 What follows the outermost statement, from position pos on: the result, which is local
variable 0 of the outermost frame, goes to the cell `cRESULT`; then the machine accepts, or, if dec
is set, it accepts if the result is positive and rejects if not. 

### `mainPos`

 The position of the outermost statement: after the four instructions of `headCode`. 

### `tailPos`

 The position of the code that follows the outermost statement. 

### `firstBody`

 The position of the first body: after the outermost statement and what follows it. 

### `entries`

 The positions of the bodies, the first of them at pos.  A body is followed by the return
sequence. 

### `endPos`

 The position after the bodies, the first of them at pos. 

### `dispPos`

 The position after the last body, which is the position of the dispatcher.  It is also the
largest number in the pool. 

### `codeLayout`

 What the code of the statements of P needs to know about the whole code. 

### `bodiesCode`

 The bodies with their return sequences, the first of them at pos. 

### `headStraight`

 The first three instructions: the numbers 1, 0, -1. 

### `poolCode`

 The code that fills the pool with the numbers 0, …, N. 

### `zeroCode`

 The code that puts zeros into the local variables of the outermost frame. 

### `frameCode`

 The code that sets up the outermost frame: FP, zeros in its local variables, and then the two
arguments in its local variables 1 and 2. 

### `startStraight`

 The start-up code without its last jump. 

### `headCode`

 The first part: the numbers 1, 0, -1, and the jump to the start-up code. 

### `mainCode`

 The second part: the outermost statement and the verdict. 

### `startCode`

 The last part: the start-up code and the jump back to the outermost statement. 

### `_root_.Light.compileProgram`

 **The code of a program.**  With dec = false the machine accepts at the end of the run; with
dec = true it accepts if the result of procedure p0 is positive and rejects if not. 

 ## Lengths and positions 

### `size_mainStmt`

 The length of the outermost statement. 

### `width_mainStmt`

 The outermost statement uses the local variables 0, 1, 2. 

### `two_mul_frameSize_add_le_dispPos`

 The dispatcher comes after four instructions, the 2 F + 11 instructions of the outermost
statement and at least two for the verdict.  So the pool also holds the distance 2 (F + 1) between
two frames and the number 2 · `mainFrame` from which the start-up code forms the first frame
pointer, and it reaches further down than the 2 F + 1 temporaries. 

### `codeAt_headCode`

 The first part is at position 0. 

### `codeAt_mainStmt`

 The outermost statement is at `mainPos`. 

### `codeAt_tailCode`

 The code for the verdict follows the outermost statement. 

### `codeAt_bodiesCode`

 The bodies begin at `firstBody`. 

### `codeAt_dispatcher_dispPos`

 The dispatcher is at `dispPos`. 

### `codeAt_startCode`

 The start-up code follows the dispatcher. 

### `codeAt_bodies`

 Every body is at its entry, followed by the return sequence, and ends at or before the position
after the bodies. 
