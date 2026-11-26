---
{
  "module": "proof/consequences/CountKSat/Host.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/Host.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/Host.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The host machine for a stepped computation whose result is a word

`exists_tmW`: a stepped computation on bit strings whose result is a list of bits, and whose init,
step and out are polynomial-time, runs on one of
Mathlib's multi-stack machines, with one constant q: a run of T steps on the input x with all states
of size at most S costs the machine at most
q·(T+1)·(|x|+S+1)^q steps, and the machine halts with the result on its output stack, first bit on
top. The machine and q are chosen before x, T and S.

The machine is that of `Groundwork.exists_tm` (proof/machines/ToTuring/Machine/Host.lean), whose
result is one bit, except that the loop stops at a result `some w` (`chkW`) and an
epilogue moves w onto the output stack. On the main stack a value is written as a word of bits and
brackets (proof/machines/ToTuring/Enc.lean). The epilogue takes the word of w apart:
each bit goes to stack a (`unpack`), comes back from there and is pushed on the output stack
(`emit`); the brackets are removed on the way, the last three by `pop3`. The two passes leave
the first bit of w on top. This takes 4|w| + 3 steps (`epilogue_within`). `stHostW` restates
`exists_tmW` as the interface statement `StHostW` of
`proof/consequences/CountKSat/Interfaces.lean`.

The proofs of `mainLoop_within` and `exists_tmW` follow `mainLoop_within` and `exists_tm` of
proof/machines/ToTuring/Machine/Host.lean. The bound
q·(T+1)·(|x|+S+1)^q has the size S of the states as a free parameter, where `exists_tm` asks S ≤
(|x|+2)^d. 

 ### The head of the loop and the epilogue 

### `chkW`

 The head of the loop: at `none` remove its word and go on with the body; at `some w` remove the
opening bracket only and leave the loop. 

### `unpackQ`

 One round: take the first bit off the word of a list of bits and put it on stack a; its closing
bracket stays. At the empty list, remove its word and stop. 

### `unpack`

 The first loop of the epilogue. 

### `emitQ`

 One round: a bit comes back from stack a and is pushed on the stack of bits, and one closing
bracket is removed. When stack a is empty, stop. 

### `emit`

 The second loop of the epilogue. 

### `pop3`

 Remove the three symbols that are left of the word of `some w`. 

### `epilogue`

 The epilogue: the bits of w move from the main stack to the empty stack of bits, first bit on
top; the three symbols below them are removed. 

 ### The loop 

### `mainLoop`

 The loop. At its head the word of the output of the state lies on the word of the state. 

### `mainLoop_within`

 The loop, from a state that reaches the result w within t steps: at most t rounds. The last
state s' is left on the main stack, and on it what
the head leaves of the word of its output `some w`. 

 ### The machine 

### `prog`

 The whole program: prologue, init and the first output, the loop, the epilogue, and the last
state dropped. 

### `exists_tmW`

 A stepped computation `M` on bit strings whose result is a list of bits, with polynomial-time
init, step and out, runs on one of Mathlib's
multi-stack machines `N` with finite alphabets. There is one number `q` such that, whenever `M` ends
on `x` with the result `w` within `T` steps and with
all states of size at most `S`, the machine `N` started on `x` halts with output `w` within q · (T + 1)
· (|x| + S + 1)^q steps. 

### `stHostW`

 The host with a word as output: the interface statement `StHostW`. 
