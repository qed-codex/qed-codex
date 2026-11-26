---
{
  "module": "proof/rates/GeneralPieces/Ring/Lex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Lex.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Lex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The number h and the lexicographic list of the partitions of h

The first sentence of the proof of the theorem on the pieces with ρ = 1/√2 in Appendix B: "Given λ ≥
1, let h ≥ 2 be the least integer with p(h) ≥ 2^λ, and let μ(x) be the partition of h with
number x ∈ {0,1}^λ (read as an integer, counting from 0) in the lexicographic list of the partitions
of h, written as nonincreasing sequences."
Proved here: such an h exists (`hOfSpec`), and it equals the h defined by `ClauseBound.Part.hOf`
(`hOf_eq`); different partitions of h have different numbers in the list, and every j < p(h)
is the number of a partition of h (`lexNum_injOn`, `exists_lexNum_eq`); a string read as an integer
is below 2^λ, and different strings give different integers (`val_lt`, `val_injective`); so for 2^λ
≤ p(h) there
is exactly one function μ as in that sentence, and it is injective (`existsUnique_isMu`,
`IsMu.injective`). 

 ### The number h 

### `hOf_eq`

 The h of the appendix equals the h defined by `ClauseBound.Part.hOf`. 

 ### The number of an element in a sorted list 

### `rank_lt`

 If f(a) < f(b) and a is in the list, fewer elements come before a than before b. 

### `rank_lt_card`

 The number of an element of the list is below the length of the list. 

### `rank_injOn`

 Different elements of the list have different numbers. 

### `exists_rank_eq`

 Every number below the length of the list is the number of an element. 

 ### The lexicographic list of the partitions of h 

### `desc_injective`

 A partition is determined by its nonincreasing sequence. 

### `lexNum_injOn`

 Different partitions of h have different numbers. 

### `exists_lexNum_eq`

 Every j < p(h) is the number of a partition of h. 

 ### A string read as an integer 

### `val_eq`

 A string read as an integer is the sum of the 2^i over the positions i of its ones. 

### `val_lt`

 A string of λ bits, read as an integer, is below 2^λ. 

### `val_injective`

 Different strings are different integers. 

 ### The function μ 

### `IsMu.injective`

 μ is injective. 

### `IsMu.wt`

 μ(x) is a partition of h. 

### `existsUnique_isMu`

 If 2^λ ≤ p(h), there is exactly one function μ such that μ(x) is the partition of h with number
x in the lexicographic list. 

### `hOfSpec`

 There is an h ≥ 2 with p(h) ≥ 2^λ, so "the least integer h ≥ 2 with p(h) ≥ 2^λ" is defined. 
