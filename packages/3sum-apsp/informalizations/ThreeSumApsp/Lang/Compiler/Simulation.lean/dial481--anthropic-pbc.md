---
{
  "module": "ThreeSumApsp/Lang/Compiler/Simulation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Compiler/Simulation.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Compiler/Simulation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The compiler is correct on statements: the simulation theorem

A run of a statement of the light language in c steps is matched by a run of its code in at most
stepsPerStep · c steps of the machine (`sim`).

What never changes (the program, its code, the numbers of `Sizes`, and the facts that the code is in
place and that a frame is wide enough for the text) forms the structure `Setting`.  The situation
before the code of a statement runs is `Start`: the code is at pos, and the memory represents the
state in the frame q, with room on the stack for the calls still allowed.  The situation afterwards
is `Finished`: the machine has reached the position after the code, the memory represents the new
state in the same frame, and only cells that the statement may write have changed.  `Simulates` says
that `Start` leads to `Finished`.

The theorem is an induction on the run, with one lemma for each rule of the semantics: `sim_skip`,
`sim_set`, `sim_store`, `sim_seq`, `sim_iteTrue`, `sim_iteFalse`, `sim_whileFalse`,
`sim_whileTrue`, `sim_call`.  Each of them first takes the code of the statement apart (`codeAt_ite`
and its like say where the parts are) and then runs the parts in turn.  A call has four parts.
Enter (`steps_callEnter`): arguments, new frame, position to return to, jump.  The body: the
induction hypothesis.  Leave (`steps_callLeave`): return sequence and dispatcher.  Store the result
in the caller's variable (`steps_setVar`).

In the proofs S is the setting and B the situation at the start; the other letters are as in the
file on the cells.


 ## Where the parts of the code of a statement are 

### `codeAt_set`

 The code of e, and the two instructions that store T₀ in x. 

### `codeAt_seq`

 The code of s, and the code of t. 

### `codeAt_ite`

 The test, the first branch, the jump over the second branch, the second branch. 

### `codeAt_while`

 The test, the body, the jump back. 

### `codeAt_call`

 The arguments and the new frame, the jump to the procedure, and the two instructions that store
the result. 

 ## The setting 

### `Setting`

 What the simulation assumes once and for all: the numbers are large enough (`Sizes`), and the
program and its code fit them. 

### `Setting.P`

 The light program. 

### `Setting.code`

 The code of the whole program. 

### `Setting.bodyAt`

 Every procedure body is at its entry, followed by the return sequence, all before the
  dispatcher. 

### `Setting.dispatcherAt`

 The dispatcher serves the positions before it. 

### `Setting.width`

 Every body has width at most F. 

### `stepsPerStep`

 An upper bound for the number of machine steps that match one step of the light language, if the
code before the dispatcher has n instructions.  Each rule of the semantics counts at least one step
and, calls apart, runs a piece of code once, which takes at most n machine steps.  A call counts two
steps, so it has 2 stepsPerStep = 4 n: at most n for its own code, n for the return sequence, 2 n
for the dispatcher. 

### `le_stepsPerStep_mul`

 At most n machine steps are within the bound for c ≥ 1 steps of the language. 

### `add_le_stepsPerStep_mul`

 At most n machine steps, followed by b machine steps that are within the bound for k steps, are
within the bound for c + k steps if c ≥ 1. 

### `call_le_stepsPerStep_mul`

 The count for a call whose code is at pos and has size + 2 instructions: size steps to enter, b
for the body, r + 2 (pos + size + 1) to leave, where r is the length of the return sequence, and 2
to store the result.  The cost a of the arguments is not needed. 

### `Start`

 The situation before the code of the statement s runs, at nesting depth d of calls: the memory m
represents the state σ in the frame q, and the following holds. 

### `Start.codeAt`

 The code of s is at pos. 

### `Start.below`

 It ends at or before the dispatcher. 

### `Start.width`

 F local variables and 2 F + 1 temporaries are enough for s. 

### `Start.bounded`

 The state holds words. 

### `Start.room`

 The stack has room for this frame and for F + 1 cells for each further level of calls. 

### `Finished`

 The code of s, started as in `Start`, has matched a run of c steps that ends in σ': it has
taken n machine steps and left the memory m'. 

### `Finished.run`

 The machine has reached the position after the code. 

### `Finished.le`

 It took at most stepsPerStep machine steps for each step of the language. 

### `Finished.rel`

 The memory represents σ' in the same frame. 

### `Finished.agree`

 Only cells that a statement in the frame q may write have changed. 

### `Simulates`

 The code of s matches the run of s from σ to σ' in c steps. 

### `Start.sub`

 The situation before a part t of the statement runs, in the same frame. 

### `Start.room_succ`

 The room on the stack, seen from the frame of a procedure that is called. 

### `Start.test`

 The test of an if or a while that is at pos. 

 ## Statements without calls 

### `sim_skip`

 skip: no code, no step. 

### `sim_set`

 x := e: the code of e leaves the value in T₀, and two instructions store it in x. 

### `sim_store`

 The cell at a := e: the code of a and e leaves the values in T₀ and T₁, and one instruction
stores. 

### `sim_seq`

 s₁; s₂: the code of s₁, then the code of s₂. 

### `sim_iteTrue`

 if c then s₁ else s₂, when c holds: the test goes on to the code of s₁, and a jump leads over
the code of s₂. 

### `sim_iteFalse`

 if c then s₁ else s₂, when c fails: the test jumps to the code of s₂. 

### `sim_whileFalse`

 while c do s, when c fails: the test jumps to the position after the loop. 

### `sim_whileTrue`

 while c do s, when c holds: the test goes on to the code of s, a jump leads back to the test,
and the loop runs again. 

 ## Calls 

### `steps_callEnter`

 Entering a procedure: the arguments, the new frame with the position to return to, and the jump
to the entry e.  Afterwards the memory represents the state in which the procedure starts, in the
frame q + F + 1, and the stack cell before that frame holds the position after the jump.  Of the
stack, only cells from q + F on have changed. 

### `steps_callLeave`

 Leaving a procedure whose frame is q + F + 1, when the stack cell before that frame holds the
position ret: the return sequence and the dispatcher.  The machine arrives at ret; RET holds the
result (local variable 0), FP points to the frame q, and otherwise only scratch cells have
changed. 

### `sim_call`

 x := p(args): enter, the body, leave, store the result. 

 ## The theorem 

### `sim`

 **The simulation theorem.**  The code of a statement matches every run of the statement. 
