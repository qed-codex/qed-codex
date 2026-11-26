---
{
  "module": "proof/rates/GeneralPieces/Half/Order.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Half/Order.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Half/Order.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The pieces with ρ = 1/√2 as programs: a string stands for the partition with its number in the lexicographic list

In the proof of the theorem on pieces with ρ = 1/√2, μ(x) is the partition of h with number x in the
lexicographic list of the partitions of h, written as nonincreasing sequences. The programs read the
string x as a number, first bit lowest, and take the entry with that number of the list
`ClauseBound.Part.partsOf h`. That list is strictly increasing in the lexicographic order
(`pairwise_partsLe`), so the
number of an entry is the number of partitions that come before it (`lexNum_partsOf`), and the
partitions of the programs are those of Appendix B (`isMu`). Also: the number h of Appendix B is
that of
the programs (`hOf_eq`). 

### `pairwise_partsLe`

 The list of the partitions of E into parts of size at most k is strictly increasing in the
lexicographic order. 

### `desc_ptn`

 A nonincreasing list of positive integers is its partition written as a nonincreasing sequence. 

### `ptn_desc`

 A partition is the partition of its nonincreasing sequence. 

### `desc_mem_partsOf`

 The nonincreasing sequence of a partition of h is in the list. 

### `lexNum_partsOf`

 The entry number k of the list of the partitions of h has the number k in the lexicographic
list. 

### `val_eq`

 A string read as an integer, first bit lowest, is the number that the programs read. 

### `isMu`

 The partition that the programs read from the string x is the partition of h with number x in
the lexicographic list. 

### `hOf_eq`

 The least h ≥ 2 with p(h) ≥ 2^λ: the number h of Appendix B is the number of the programs. 
