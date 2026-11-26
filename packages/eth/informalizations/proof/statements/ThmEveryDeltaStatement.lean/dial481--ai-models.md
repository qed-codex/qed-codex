---
{
  "module": "proof/statements/ThmEveryDeltaStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/ThmEveryDeltaStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/ThmEveryDeltaStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem 2 in its decision form: for every constant δ > 0, 3-SAT on n variables can be decided in time O(2^{δn})

This file only *states* the theorem: it has definitions and no proofs, and it imports only
`ThreeSatStatement.lean` (definitions only; that file imports Mathlib only).
The statement is `Sat3.ThmEveryDelta`, at the end.

"Algorithm" means a deterministic Turing machine with finitely many stacks, as defined in Mathlib
(`Turing.FinTM2`);
"time" is its number of steps. 

 The definitions of 3-SAT and of the input string of an instance (`Lit`, `CNF`, `Satisfiable`,
`Is3CNF`, `slot`, `enc`) are those of `ThreeSatStatement.lean`. 

 ### Time 

### `HaltsWith`

 The machine `M`, started with the input string of φ on its input stack and all other stacks
empty, halts after at most `t`
steps, with the single bit `b` on its output stack, all other stacks empty, and its internal state
back at its initial value.
(One step, `Turing.TM2.step`, runs the instructions at the current label as far as the next `goto`
or `halt`: a number of pushes and
pops that is bounded for a fixed machine.) 

### `DecidedInTime`

 "3-SAT can be decided in time O(2^{δn})": there are one machine `M` and one constant `c` such
that, for every n, on every
instance φ of 3-SAT on n variables, `M` halts after at most c · 2^{δn} steps and outputs whether φ
is satisfiable.
(Mathlib makes the sets of stacks, labels and internal states of a machine finite, and the alphabet
of the input stack; the
condition `Finite (M.tm.Γ k)` makes the alphabet of every stack finite. A machine can push only
finitely many different symbols
in any case, since its instructions compute them from the internal state; the condition makes the
finiteness explicit.) 

### `ThmEveryDelta`

 **Theorem 2 in its decision form.** For every constant δ > 0, 3-SAT on n variables can be
decided in time O(2^{δn}). 
