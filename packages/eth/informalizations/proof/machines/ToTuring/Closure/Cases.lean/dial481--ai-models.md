---
{
  "module": "proof/machines/ToTuring/Closure/Cases.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Closure/Cases.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Closure/Cases.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Closure of polynomial time under case distinctions on Bool, Option, sums and lists; the branches
may use the context x.
Two fragments do all the work: one takes a sum apart and goes on according to its tag, the other
puts a tag on a list that
tells whether it is empty. All else follows by composition, because a fragment sees the tree of a
value and not its type. 

 ### A choice between two fragments 

### `within_branch`

 The head statement leads to the label b; then the fragment for b runs. 

### `tagHead`

 Pop the bit on top of the main stack and go to the label of that name. 

### `sumCore`

 Case distinction on a sum, without context. 

 ### Is the list empty? 

### `nilHead`

 Look at the second symbol of the item on top of the main stack: a closing bracket means that the
item is ⟨⟩ (label false),
anything else that it is a pair (label true). The stack is left as it was (the first symbol, an
opening bracket, is popped
and pushed back). 

### `tagF`

 Put the tag b on the item on top of the main stack. 

### `listSplit`

 A list is empty, or it has a first element and a rest. 

 ### The case distinctions 

### `cond'`

 Case distinction on a Boolean c x; both branches see the context x. 

### `ite'`

 The same for `if … then … else` on a decidable proposition c x. 

### `sumElim`

 Case distinction on a sum s x; each branch sees the context x and what lies under the tag. 

### `listCases`

 Case distinction on a list l x: it is empty, or it has a first element and a rest; both branches
see the context x. 

### `optionElim`

 Case distinction on an option o x; both branches see the context x. 
