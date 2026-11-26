---
{
  "module": "NS1/Deal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Deal.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/Deal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Steps and templates

A state is a trie. Steps: choose an option (a list of assignments) from a table, look up an operation, guess a bit
list, check. Templates: trees with holes that are filled from the state.


### `RepW`

 The trie `W` has the values `σ`. 

### `assignT`

 Assign: the elements of the list are pairs (path, value). 

### `assignS`

 Assign, for values. 

### `assignF`

 Assign; `o` gives the list, `w` the trie. 

### `allBits`

 All bit lists of a given length. 

### `bitsB`

 Guess a bit list. The argument is (this program, (length in binary, bits so far)). 

### `bitsF`

 Guess a bit list whose length is a fixed binary number. 
