---
{
  "module": "Nc/Sort/Radix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Sort/Radix.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Sort/Radix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Radix sort and the check of neighbours

Records are pairs of a flag (false: entry of the table, true: lookup) and a key of n letters. After one pass
for every letter, records with equal keys are neighbours, in the original order. So every lookup has the key of
an entry of the table before it if and only if, after sorting, every lookup has the same key as the record
before it.


### `Rc`

 A record: a flag and a key. 

### `pass`

 One pass: distribute by letter j, collect. 

### `srt`

 The list after the first j passes. 

### `keys`

 The keys of length j, in the order of the sort. 

### `chk`

 The check of neighbours. 

### `headOk`

 The first record of the list is an entry of the table. 

### `chk_table`

 First the table, then the lookups: the check succeeds if and only if every lookup is in the table. 
