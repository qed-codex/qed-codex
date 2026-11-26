---
{
  "module": "proof/machines/StepMachines/Math/Code.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/Code.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/Code.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Codes: finite sets named by words of a given length, and the first ways to make one (all words,
another way to write the set
or the length, a bijection, the empty set, pairs). 

### `Code`

 A code of the finite set S by words of length n: the words of D name the elements of S, one
each, through dec. 

### `Full`

 Every word of length n is a name. 

### `sum_dec`

 A sum over S is the sum over the names. 

### `sum_words`

 The same, over all words of length n. 

### `word`

 The words of length n name themselves. 

### `cast`

 The same names for another set and length, equal to the given ones. 

### `map`

 Names carried along a bijection φ of S with S'. 

### `empty`

 No element. 

### `prod`

 Pairs: the two names one after the other. 
