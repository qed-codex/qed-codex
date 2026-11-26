---
{
  "module": "NS1/Compose.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Compose.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Compose.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Cuts one after the other


### `pvs`

 The product of the plain sums of a list of instances. 

### `CutD`

 A program `G` that cuts plain sums of `τ` steps on instances of size `s` into at most `P` pieces of `τ'` steps on
instances of size `s'`, in `t` steps. 

### `CutD.cutProg`

 A cut gives the program of the cut hypothesis. 

### `stepC`

 One more cut for every element: the argument is (element, list of pieces so far). 

### `compC`

 First `G`, then `G'` on every piece. 

### `_root_.Paper.thm_cut_compose`

 **Paper: Theorem thm:cut, composition of cuts.** "Composing the programs: the next one is run on every piece in
the list ... The sum formulas compose." 
