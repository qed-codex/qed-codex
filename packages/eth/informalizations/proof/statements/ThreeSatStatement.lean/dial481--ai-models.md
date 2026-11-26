---
{
  "module": "proof/statements/ThreeSatStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/ThreeSatStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/ThreeSatStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # ETH for 3-SAT on Mathlib Turing machines (Definition 6): `s₃TM` > 0, the infimum of the δ for which some machine decides 3-SAT in time O(2^{δn})

The Exponential Time Hypothesis for 3-SAT, on Mathlib's own Turing machines (`Turing.FinTM2`:
finitely many stacks).
`Sat3.ETH_TM` says: `s₃TM` > 0, where `s₃TM` is the infimum of the δ for which 3-SAT on n variables
is in time O(2^{δn}).
The end theorem, `MainResults.ethIsFalse` in Solution.lean, is `¬ Sat3.ETH_TM`. This file has
definitions only and imports Mathlib only. 

 ### 3-SAT and how an instance is written on the tape 

### `Lit`

 A literal on x₀ … xₙ₋₁: a variable, and the value of it that makes the literal true. 

### `CNF`

 A clause is the OR of a list of literals; a formula is the AND of a list of clauses. 

### `Satisfiable`

 Some assignment makes a literal of every clause true. 

### `Is3CNF`

 An instance of 3-SAT: at most 3 literals per clause, and no clause written twice, so that its
length is bounded in terms of n.
(A Mathlib machine must halt with only its output on its stacks, so it has to pop all of its input,
except perhaps the last
symbol. If clauses could be repeated, no time bound in n alone could hold, and the hypothesis below
would be trivially true.) 

### `slot`

 A slot of a clause as a number: 0 = no literal, 2i+1 = ¬xᵢ, 2i+2 = xᵢ. 

### `enc`

 As a bit string: 1ⁿ 0, then 3 slots per clause, ⌊log₂ (2n)⌋ + 1 bits per slot, low bit first. 

 ### Time on a Turing machine 

### `DecidesTM`

 `M`, started on an instance's code, halts within `t n` steps with the bit «satisfiable» as
output. One step (`TM2.step`) runs
the statement (`TM2.Stmt`) at the current label as far as a `goto` or `halt`: perhaps several pushes
and pops, but a bounded
number for a fixed machine, which has finitely many labels. 

### `InTimeTM`

 «3-SAT is in time O(2^{δn})» on Turing machines: one machine, finite alphabets, one constant. 

### `s₃TM`

 The infimum of the δ for which 3-SAT is in time O(2^{δn}) on Turing machines (∞ if there is no
such δ). 

### `ETH_TM`

 The Exponential Time Hypothesis (item 3 of Theorem 1 of Impagliazzo, Paturi, JCSS 62 (2001)), on
Turing machines. 
