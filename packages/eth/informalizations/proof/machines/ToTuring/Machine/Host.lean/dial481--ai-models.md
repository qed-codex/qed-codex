---
{
  "module": "proof/machines/ToTuring/Machine/Host.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Machine/Host.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Machine/Host.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The host: one of Mathlib's multi-stack machines that runs a stepped computation (`Stepped`)
whose init, step and out are
polynomial-time (`exists_tm`). Prologue: each bit of the input is popped off the stack of bits and
pushed on stack a, with a
closing bracket on the main stack; then ⟨⟩, the word of the empty list, is pushed on the main stack;
then the bits come back from
stack a, each followed by an opening bracket. The main stack now holds the word of the input list.
Then the fragment of init.
Then the word of the state is duplicated and the fragment of out runs on the copy. Then a loop,
whose head removes the word of
the output: at `none` it runs the fragment of step, duplicates the word of the new state, runs the
fragment of out on the copy
and starts again; at `some b` it pushes b on the stack of bits and leaves the loop. Finally the word
of the state is dropped.
Each time at the head of the loop the main stack holds the word of the output on the word of the
state, and all other stacks are
empty.

The prologue takes 4|x| + 3 steps (`prologue_within`). Each round of the loop takes one step for the
head, plus the steps of
step, plus 3·len + 3 for the copy, plus the steps of out (`mainLoop_within`). So the whole run takes
at most
c·(T + 1)·(|x| + 1)^c steps (`exists_tm`). 

 ### Fragments on the five stacks 

### `FrIO`

 Fragments of the final machine, over the four work stacks and the stack of bits. 

### `within_io`

 A fragment over the work stacks keeps its bound in the final machine. 

### `skip`

 The fragment that does nothing, in one step. 

 ### The prologue 

### `pourQ`

 Pop a bit off the stack of bits; push it on stack a, and a closing bracket on the main stack. 

### `pour`

 The first loop of the prologue. 

### `buildQ`

 Pop a symbol off stack a; push it, and then an opening bracket, on the main stack. 

### `build`

 The second loop of the prologue. 

### `prologue`

 The prologue: from the bits of the input to the word of the list of these bits. 

 ### The loop 

### `bitOf`

 The bit held in the local state, false if it holds none. Used on the second symbol of the word
of `some b`. 

### `chkQ`

 The head of the loop looks at the word of an optional bit on top of the main stack and removes
it. At `none` it goes on
with the body; at `some b` it pushes b on the stack of bits and leaves the loop. 

### `look`

 Duplicate the word of the state and turn the copy on top into the word of its output. 

### `body`

 The body of the loop: one step of the computation, then the output of the new state. 

### `mainLoop`

 The loop. At its head the word of the output of the state lies on the word of the state. 

### `mainLoop_within`

 The loop, from a state that reaches the result b within t steps: at most t rounds, and the last
state is left on the
main stack. 

 ### The machine 

### `prog`

 The whole program: prologue, init and the first output, the loop, and the last state dropped. 

### `tmOf`

 A fragment on the five stacks as one of Mathlib's bundled machines; input and output on the
stack of bits. 

### `outputs_of_within`

 A run of the fragment is a run of the bundled machine, in Mathlib's terms. 

### `exists_tm`

 A stepped computation on bit strings with polynomial-time init, step and out runs on one of
Mathlib's multi-stack
machines with finite alphabets. If it ends on x within T steps with states of size at most (|x| + 2)^d,
the machine takes
at most c · (T + 1) · (|x| + 1)^c steps, where c depends on the computation and d only. 
