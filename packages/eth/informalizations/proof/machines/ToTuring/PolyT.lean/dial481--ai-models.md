---
{
  "module": "proof/machines/ToTuring/PolyT.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/PolyT.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/PolyT.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial time on Mathlib's multi-stack machines, defined here from Mathlib alone. `PolyT f`:
some fragment turns the word
of x, on top of the main stack, into the word of f x, within c·(len x + 1)^c steps, and leaves alone
whatever lies beneath it
and on the other three stacks. Because of this frame all fragments can share the same stacks, and
closure under composition,
pairing, case distinction and folds is proved by gluing fragments. `PolyT` is a proposition: the
fragment is hidden under an
existential quantifier, so the proposition `PolyT f` names no fragment; fragments are defined in TM/
and Closure/, glued
together in the proofs of the closure lemmas, and assembled into one machine by `exists_tm`.

What is not asked: nothing is ever decoded, the fragment must behave correctly only on words of
values, and the tree of a
value (`Enc`) need not determine the value. For the states of a computation, the encoding is chosen
by whoever proves
`IsPolyT`. None of this can weaken the end theorem, which does not mention `PolyT`: `Sat3.InTimeTM`
is about one of Mathlib's
machines, started on the bits of `Sat3.enc φ`. `exists_tm` (Machine/Host.lean) builds that machine
out of the fragments and
proves that it runs to the output bit within a polynomial times the number of steps of the stepped
computation, whatever
encoding was chosen: the machine itself writes the word of the input from the raw bits, it reads the
answer off the word of
an optional bit, which does determine the bit, and `Carried` ties the length of the words of the
states to the size in which
the files of proof/machines/StepMachines/ bound them. 

### `PolyT`

 f is computed in polynomial time on top of the main stack: for some constant c, one fragment
turns the word of x, with
any M beneath it on the main stack and any contents A, B, N of the other three stacks, into the word
of f x with the same M,
A, B, N, in at most c·(len x + 1)^c steps; and the word of f x has at most c·(len x + 1)^c symbols.
The definition says
nothing about words that are not words of values. 

### `PolyT.of`

 How to prove PolyT: a fragment, a polynomial bound on its steps, a polynomial bound on the
length of the result. 

### `PolyT.elim`

 How to use PolyT: one monotone polynomial bound for the steps and for the length of the result. 

### `PolyT.congr`

 PolyT passes to a function with the same values. 

### `PolyT.of_wd`

 Only words matter: if φ keeps the words of the inputs, and the words of g's values are those of
f ∘ φ, then g is
polynomial-time, computed by the same fragment as f. The types may differ. 

### `Unary`

 The number f x is computed in polynomial time in unary: as a list of that length. 

### `IsPolyT`

 Every part of the stepped computation M is polynomial-time, and the words of its states are at
most linear in their size. This
does not bound the number of steps that M takes; that bound comes from the files of
proof/machines/StepMachines/. The class holds
data, the encoding of the states; so theorems that assert it say `Nonempty (IsPolyT M)`. 
