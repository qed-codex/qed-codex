---
{
  "module": "Nc/Acc/Prog.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Acc/Prog.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Acc/Prog.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The program of an accelerator


### `pairB`

 Pair the neighbours of a list. The argument is (this program, list). 

### `pairsF`

 Pair the neighbours several times. 

### `lt0`

 The letter of the empty tree. 

### `lt1`

 The letter of a node. 

### `lt2`

 The letter at the end. 

### `treeF`

 The tree of pairs of the letters of the word of the argument. 

### `accF`

 The program. 

### `pairTree`

 The tree of pairs. 

### `tbits`

 The brackets of a tree, in preorder: 0 = empty, 1 = a node. 

### `ltr`

 The letter as a tree. 

### `look_pairTree`

 The letter at a place of the tree of pairs. 

### `decL`

 The letter with a given code. 

### `codeB`

 The one-hot code of a word, with one letter `none` at the end. 

### `lamK`

 The weight of a letter at a place. 

### `accK`

 The constants of an accelerator. 

### `accF_kv`

 **The program computes the part of degree at most `d` of a polynomial with a small circuit.** 
