---
{
  "module": "ThreeSumApsp/Lang/Logic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Logic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Logic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Proof rules for the light language

Ends lim P d s σ T Q says: the statement s, started in σ, ends within T steps in a state that
satisfies Q.  There is one rule for each construct; a rule turns a goal about a statement into goals
about its parts, so a proof follows the text of the program from top to bottom.  Recursion needs no
rule: a statement about a recursive procedure is proved by induction (in Lean) on a measure, and the
rule for calls unfolds the body.

There are three rules for loops: with an invariant indexed by the number of the round and a cost for
each round (Ends.while), the same with one cost for all rounds (Ends.whileConst), and, for a loop
whose number of rounds depends on the data, with a quantity that every round decreases
(Ends.whileVariant).

The file also has the basic facts about runs (a run stays a run when procedures are appended to the
program), notation for writing programs, the simplification set
`light_norm`, and the standing assumptions `Std` about the limits.


 ## Runs 

### `getElem`

 A procedure of a program is a procedure, with the same number, of the program with more
procedures appended. 

### `getElem`

 Procedure number i of a list that is appended to the program P₀ has the number |P₀| + i,
whatever is appended after the list. 

### `getElem`

 Procedure number i of a list that is appended to the program P₀ has the number |P₀| + i. 

### `Exec.append`

 A run stays a run when procedures are appended to the program. 

 ## The rules 

### `Ends`

 The statement s, started in σ, ends within T steps in a state that satisfies Q. 

### `Ends.mono`

 More time and a weaker conclusion. 

### `Ends.append`

 What is proved about a program holds for the program with more procedures appended. 

### `Ends.whileStep`

 A loop whose test holds: one round, then the loop again. 

### `Ends.whileDone`

 A loop whose test fails. 

### `Ends.while`

 Loops.  I i is the invariant before round number i (counted from 0) of n rounds, and b i bounds
the cost of that round. 

### `Ends.whileConst`

 Loops in which every round costs at most b. 

### `Ends.whileVariant`

 Loops whose number of rounds depends on the data.  I is the invariant, m a quantity that every
round decreases, and b bounds the cost of a round. 

### `Ends.call`

 Calls: verify the body from the frame made of the arguments. 

 ## Notation for writing programs

Not trusted: a theorem about a program does not depend on how the program was typed in. 

### `v`

 Local variable number x. 

### `k`

 The constant n. 

### `M`

 The memory cell at address a. 

### `+'`

 The sum of two expressions. 

### `-'`

 The difference of two expressions. 

### `*'`

 The product of two expressions. 

### `Cond.le`

 The test a ≤ b, written as a < b + 1. 

### `Stmt.iteNe`

 Branching on a ≠ b: the branches of the test a = b, swapped. 

### `Cond.holds_le`

 The test a ≤ b holds if and only if a ≤ b. 

 ## Simplification 

### `light_norm`

 `light_norm [h₁, h₂]` unfolds values, costs and safety conditions of expressions and tests, and
reads of updated variables and cells, and rewrites with the facts `h₁`, `h₂` about the variables. 

### `light_norm`

 Unfolds values, costs and safety conditions of expressions and tests, and reads of updated
variables and cells. 

### `toNat_natCast_add_natCast`

 The natural number behind an address that is a sum of two natural numbers. 

 ## The limits 

### `Std`

 The standing assumptions about the limits: an address fits in a word, and so do the constants
of the programs. 

### `Limits.Addr.abs_le`

 An address fits in a word if the memory is not larger than the largest word. 

### `Limits.addr_of_lt`

 A natural number below the size of the memory is an address, and fits in a word. 

### `Limits.abs_le_of_le`

 A natural number at most the size of the memory fits in a word. 
