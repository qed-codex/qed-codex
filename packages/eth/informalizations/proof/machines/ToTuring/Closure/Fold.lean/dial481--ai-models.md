---
{
  "module": "proof/machines/ToTuring/Closure/Fold.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Closure/Fold.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Closure/Fold.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Closure of polynomial time under folds over lists; a fold is the only form of loop that the
certificates of polynomial time provide. The function folded may use the context x.
The lengths of all intermediate values must be bounded by a polynomial in the length of x. 

 ### The loop 

### `foldHead`

 The head of the loop. On the main stack lies the word of a list, then the word of the state. If
the list is empty its word
is removed and the loop is left; else its opening bracket is removed and the body is entered. 

### `foldBody`

 The body: park the first element on a and the rest of the list on b, remove the closing bracket,
fetch the element, pair it
with the state, apply P, fetch the rest of the list. 

### `foldLoop`

 The loop: the head, then the body, again and again until the list is empty. 

### `roundT`

 The steps of one round: Lb bounds the length of the word of the list, Bd that of the states, t
the steps of P. 

### `foldLoop_within`

 The loop computes the fold. 

### `foldl_ctx`

 The fold keeps the context in the first component of its state. 

### `foldl`

 The fold: if l, a and g are polynomial-time and a polynomial in len x bounds the lengths of all
intermediate values,
then x ↦ (l x).foldl (g x) (a x) is polynomial-time. 

### `foldl_add`

 The fold when every step adds at most b(len x) to the length, b a polynomial bound. 
