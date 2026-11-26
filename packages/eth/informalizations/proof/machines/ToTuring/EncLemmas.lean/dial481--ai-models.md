---
{
  "module": "proof/machines/ToTuring/EncLemmas.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/EncLemmas.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/EncLemmas.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The words of the constructors, their lengths, and `Carried` for every type former: the word of a
value is linear in its
size. 

### `wd_int`

 An integer is written as the pair of its sign (`true` if negative) and its absolute value. 

### `len_none`

 The word of `none` is a pair of brackets. 

### `len_some`

 The word of `some a` adds four brackets to the word of `a`. 

### `len_inl`

 The word of a left injection adds a tag bit and two brackets. 

### `len_inr`

 The word of a right injection adds a tag bit and two brackets. 

### `len_list`

 The word of a list has the words of its entries, two brackets for each entry and two more at the
end. 

### `len_append`

 The words of `l` and `l'` together have two symbols more than the word of `l ++ l'`. 

### `length_le_len`

 A list has at most as many entries as its word has symbols. 

### `len_le_of_mem`

 The word of an entry is no longer than the word of the list. 

### `two_le_len_list`

 The word of a list has at least its two brackets. 

### `len_bool`

 A truth value is one symbol. 

### `len_unit`

 The one value of `Unit` is a pair of brackets. 

### `len_bools`

 A list of truth values takes three symbols for each entry and two more at the end. 

### `len_units`

 A list over `Unit` takes four symbols for each entry and two more at the end. 

### `len_nat`

 A natural number takes three symbols for each binary digit and two more at the end. 

### `len_int`

 An integer takes the word of its absolute value, a sign bit and two brackets. 

### `len_nat_mono`

 A larger natural number has a word at least as long. 
