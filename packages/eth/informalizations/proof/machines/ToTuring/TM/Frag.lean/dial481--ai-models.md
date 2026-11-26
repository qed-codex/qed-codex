---
{
  "module": "proof/machines/ToTuring/TM/Frag.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/TM/Frag.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/TM/Frag.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Fragments: programs of multi-stack machines over fixed stacks, alphabets and local state; they
differ in their labels only.
So gluing is a matter of labels: one after the other, a choice between two, a loop. 

### `Frag`

 A fragment: a finite set of labels, a first label, a program. 

### `Frag.Λ`

 the labels 

### `Frag.entry`

 the first label 

### `Frag.m`

 the program 

### `Frag.Runs`

 From its first label, with local state v and stacks S, the fragment halts after exactly n steps
with local state v and
stacks S'. 

### `Frag.seq`

 P, then Q. 

### `Frag.seq_runs`

 A run of P followed by a run of Q is a run of `P.seq Q`; the numbers of steps add up. 

### `run_head`

 One step of a larger machine at a label that holds a placed statement. 

### `Frag.ofStmt`

 One statement without jumps. 

### `Frag.ofStmt_runs`

 If the statement halts with the local state unchanged, the fragment runs in one step. 

### `Frag.branch`

 A head statement that ends in `goto true`, `goto false` or `halt`; then P, or Q, or nothing. 

### `Frag.branch_runs_true`

 If the head ends in `goto true`, the branch takes one step and then runs as P. 

### `Frag.branch_runs_false`

 If the head ends in `goto false`, the branch takes one step and then runs as Q. 

### `Frag.loop`

 A loop: the head statement ends in `halt` (leave the loop) or in `goto ()` (the body, then the
head again). 

### `Frag.loop_runs_exit`

 If the head halts, the loop ends after one step. 

### `Frag.loop_runs_iter`

 If the head ends in `goto ()`, the loop takes one step, runs the body, then runs as the loop
again. 

 ### Runs with an upper bound on the number of steps. The local state is an optional symbol, `none` before and after. 

### `Frag.Within`

 P leads from S to S' within t steps (local state none before and after). 
