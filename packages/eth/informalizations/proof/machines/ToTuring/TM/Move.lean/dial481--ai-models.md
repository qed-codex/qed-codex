---
{
  "module": "proof/machines/ToTuring/TM/Move.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/TM/Move.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/TM/Move.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The one loop that handles data: pop one item (the code of a tree) off a stack, symbol by symbol,
and push its mirror
image on no, one or two other stacks. Open brackets are counted in unary on the counter stack (one
`R` for each open bracket)
above a sentinel `L`, so that nothing beneath the item, nor beneath the sentinel, is ever looked at.
The loop is written once,
for four stacks (source, two targets, counter) with two flags that say which targets are used; `mv`,
`mv2` and `drp` are that
loop on renamed stacks (TM/Rename.lean). 

### `S4`

 Source, two targets, counter. 

### `MvL`

 The labels of the loop. 

### `St4`

 Statements of the loop. 

### `pushIf`

 Push on k if p. 

### `mvChk`

 Is the count back at the sentinel? Then remove it and halt; else go on. 

### `mvM`

 The program: a sentinel on the counter; then pop a symbol, push its mirror image (on t1 if p₁,
on t2 if p₂), count. 

### `mvB`

 The loop as a fragment on four stacks. 

### `toStk`

 The four stacks of the loop as work stacks. 

### `other`

 A work stack other than i, j and the counter; it fills a target slot of the loop that is not
used. 

### `mv`

 Move one item from stack i to stack j, mirrored. 

### `mv2`

 Move one item from stack i to the stacks j and k, mirrored. 

### `drp`

 Pop one item off stack i. 

 ### The loop on its four stacks 

### `st4`

 The contents of the four stacks. 

### `putIf`

 The word w on top of B if p, else B. 

### `run_inside`

 Inside at least one open bracket, an item is moved and the loop goes on, the count as before. 

### `mvB_runs`

 The loop on its four stacks: one item leaves the source and its mirror image arrives on the
chosen targets, in
|code| + 1 steps; what lies beneath is not touched. 

 ### The loop on the work stacks 

### `mvB_ren_runs`

 The loop on the work stacks: source i, targets j and k, all different, and the counter. 

### `mv_runs`

 `mv i j` takes the item x off stack i and puts its mirror image on stack j, in |code x| + 1
steps; nothing else
changes. 

### `mv_runs'`

 The way back: a mirrored item becomes the item. 

### `mv2_runs`

 `mv2 i j k` takes the item x off stack i and puts its mirror image on both stacks j and k, in |code
x| + 1 steps. 

### `drp_runs`

 `drp i` removes the item x from stack i in |code x| + 1 steps; nothing else changes. 
