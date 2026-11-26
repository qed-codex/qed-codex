---
{
  "module": "proof/rates/CountedToPadded/Tables.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/Tables.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/Tables.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Tables that are written out

Proof of `BitsOfTablesFacts` (Defs.lean); the size of tables is at most the length of their word;
`entry` is polynomial-time; the number of bits of the entries and the length of the word of the
tables are computed in unary. 

 ### The largest number of a list, at least 1 

### `one_le_foldr_max`

 The largest number of a list, at least 1, is at least 1. 

### `le_foldr_max`

 It is at least every number of the list. 

### `foldr_max_le`

 It is at most every c ≥ 1 that bounds the list. 

 ### The entries 

### `getD_eq_or_mem`

 An entry of a list with a value to fall back on is that value or stands in the list. 

### `entry_eq_or_mem`

 An entry is 0 or stands in the tables. 

 ### Size and word 

### `size_le_len_list`

 If every entry of a list has size at most the length of its word, so has the list. 

### `size_le_len_tab`

 The size of tables is at most the length of their word. (`Carried` is the inequality in the
other direction.) 

### `size_entry_le`

 An entry is no larger than the tables. 

 ### Certificates 

### `entry_poly`

 `entry` is polynomial-time. 

### `lookupIsPoly`

 The certificate of `lookup`. 

### `bitsOfTables_eq`

 The largest number with the start value 1 is the largest number, with the start value 0, of the
list with 1 put behind it. 

### `bitsOfTables_poly`

 The number of bits of the entries is polynomial-time. 

### `len_tab_eq`

 The length of the word of the tables, written out. 

### `len_tab_unary`

 The length of the word of the tables, in unary. 

### `bitsOfTables_le_len`

 The number of bits of the entries is at most the length of the word of the tables. 

### `bitsOfTables_unary`

 The number of bits of the entries, in unary. 

### `bitsOfTablesFacts`

 B′ is at least 1 and bounds every entry; under `WFe` it is at most B + 1. 
