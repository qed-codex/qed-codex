---
{
  "module": "ThreeSumApsp/Lang/Rules.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Rules.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Rules.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Derived rules: time that is not typed, blocks, counting loops

The rules of this file spare the typing of step counts.  Ends.next gives the first statement its
time and the rest of the program what is left; Ends.setThen, Ends.storeThen and Ends.iteThen do the
same for one assignment, store or branch, and Ends.setLast, Ends.storeLast and Ends.iteLast treat
the last statement of a program.  `Ends.pieceThen` and `Ends.pieceLast` are the two forms for a
piece of the program that has a lemma of its own.  In every rule the main premises come first, then
the side conditions, and last the comparison of times.  The comparison has the default proof
`light_time`, safety conditions have the default proof `light_side`.

A block is a statement without loops and calls.  s.Runs lim σ R says that the block s runs safely
from σ and ends in a state that satisfies R; Ends.block turns this into a fact about time, with the
cost computed. Ends.whileBlock is the rule for a loop whose body is a block.

Stmt.for i hi body is the loop "for i = 0, …, hi - 1 do body".  The rule Ends.for owns the counter:
the safety of the test and of the increment and the number of steps of the loop are settled here,
once. Ends.forMem is the common case in which the body changes no local variable, so that the
invariant speaks about the memory only.  The three parts of every loop rule are called start, round
and done.  A loop rule is told a bound b on the steps of a round; for a round that is a block with
a name, say xRound, this is xRound.blockCost.


 ## Blocks 

### `Stmt.after`

 The state after a block (σ itself for a loop or a call, which are not blocks). 

### `Stmt.blockCost`

 A bound on the number of steps of a block: the longer side of each branch counts (0 for a loop
or a call). 

### `Stmt.BlockSafe`

 The statement is a block, and its run from σ stays within the limits. 

### `Stmt.Runs`

 The block s, started in σ, stays within the limits and ends in a state that satisfies R. 

 ## The default proofs 

### `light_time`

 `light_time [t₁, t₂]` compares two numbers of steps, after computing the costs of the
expressions, tests, blocks and argument lists that occur and unfolding the running times `t₁`,
`t₂`. 

### `light_time`

 Compares two numbers of steps, after computing the costs of the expressions, tests, blocks and
argument lists that occur. 

### `light_side`

 `light_side [h₁, h₂]` proves that an expression or a test stays within the limits, has a given
value, or holds, after putting in the values of the variables.  The facts `h₁`, `h₂` say what the
cells hold that are read, or are definitions to be unfolded; everything else is linear arithmetic
over the hypotheses in the context, to which the two fields of a hypothesis `Std lim` are added. 

### `light_side`

 Proves that an expression or a test stays within the limits, has a given value, or holds, after
putting in the values of the variables, by linear arithmetic over the hypotheses in the context. 

### `light_arith`

 Proves an inequality between addresses, sizes and bounds by linear arithmetic over the
hypotheses in the context.  A field of a record that is written out, such as
`{ dst := a, len := n }.len`, is computed first. 

 ## Rules for blocks 

### `Stmt.Runs.mono`

 A weaker conclusion. 

### `Stmt.Runs.seq`

 Two blocks, one after the other. 

### `Stmt.Runs.ite_pos`

 A branch whose test holds. 

### `Stmt.Runs.ite_neg`

 A branch whose test fails. 

### `Ends.block`

 **Blocks.**  A block that runs safely from σ ends within any T ≥ s.blockCost, in the state
s.after σ. 

 ## Sequencing: what is left of the time goes to the rest of the program 

### `Ends.next`

 The first statement gets T₁ steps, the rest of the program what is left of T. 

### `Ends.seqAssoc`

 Brackets do not matter: a piece of several statements, followed by the rest of the program, is
run statement by statement. 

### `Ends.skipThen`

 A `skip` before the rest of the program takes no step. 

### `Ends.skipLast`

 A `skip` may be put behind a statement. 

### `Ends.seqSelf`

 A program that is defined as a sequence may be treated as the sequence. 

### `Ends.pieceThen`

 A piece of the program about which `h` is known, followed by the rest of the program, which gets
the steps that are left. 

### `Ends.pieceLast`

 A piece of the program about which `h` is known, at the end of the program. 

### `Ends.setLast`

 An assignment at the end of the program. 

### `Ends.setThen`

 An assignment, followed by the rest of the program. 

### `Ends.storeLast`

 A store at the end of the program. 

### `Ends.storeThen`

 A store, followed by the rest of the program. 

### `Ends.iteLast`

 A branch at the end of the program: both sides get the steps that the test leaves. 

### `Ends.iteThen`

 A branch, followed by the rest of the program: each side, with the rest of the program behind
it, gets the steps that the test leaves. 

### `Ends.iteIffThen`

 A branch, followed by the rest of the program, where the test says `p`: the first side is run
under the hypothesis `p`, the second under `¬ p`. 

 ## Loops whose body is a block 

### `Ends.whileBlock`

 **Loops whose body is a block.**  I j is the invariant before round j of n rounds.  The time is
computed from body.blockCost. 

 ## Counting loops 

### `Stmt.for`

 for i = 0, …, hi - 1 do body. 

### `Ends.for`

 **Counting loops.**  I j is the invariant before round j.  The bound hi has the value n
throughout, n fits in a word, and the body keeps the counter and takes at most b steps.  The rule
supplies σ.loc i = j; I 0 is asked of σ with 0 in the counter, and I (j + 1) of the state after the
increment. 

### `Ends.forMem`

 **Counting loops whose body changes no local variable.**  Before round j the local variables are
the given ones with j in the counter, and I j holds of the memory.  The bound hi has the value n
throughout, n fits in a word, and the body takes at most b steps. 
