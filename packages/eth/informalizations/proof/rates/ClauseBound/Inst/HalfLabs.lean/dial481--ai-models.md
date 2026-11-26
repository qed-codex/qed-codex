---
{
  "module": "proof/rates/ClauseBound/Inst/HalfLabs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfLabs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfLabs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The pieces with ρ = 1/√2 as programs: the labels of the factorizations

A label θ of a factorization is read as a number and stands for the pair (j, τ) with that number in
the list `labs T tr h s`. Here: a sum over all words θ of c bits of a product of two
functions of the entry number θ of a list is the sum over the list, if the list has at most 2^c
entries (`sum_words_getElem`); for the table T of all partitions of 0, …, 4h and |s| ≤ 2h, the list
of the
pairs has Σ_j p(s + j) entries row-wise and Σ_j p(2h − s − j) column-wise (`length_labs`); a sum
over it is the double sum over j ≤ 2h and over the partitions τ of the weight that belongs to j
(`sum_map_labs`); and the partitions in it are listed in the flattened table
(`mem_flatten_of_mem_labs`). The theorems `stWords` and `stLabs` put this in the form of the
interface lemmas `StWords` and `StLabs`. 

 ### Sums over lists 

### `sum_range_getElem`

 A sum over the positions of a list, continued by zeros. 

### `sum_words_getElem`

 A sum over all words θ of c bits of the product of two functions of the entry number θ of a list
with at most 2^c entries is the sum over the list. 

### `sum_map_range_int`

 The sum of the values F 0, …, F (n − 1), written with a list. 

### `sum_map_flatMap`

 The sum of z over w.flatMap e is the sum, over the members a of w, of the sums of z over e a. 

### `mem_flatten_of_mem_getD`

 A member of an entry of a table is a member of the flattened table. 

 ### The weights 

### `wOf_le`

 The weight of τ in a pair (j, τ) with j ≤ 2h is at most 4h if |s| ≤ 2h. 

 ### The list of the labels 

### `mem_labs`

 What it means to be in the list of the pairs (j, τ). 

### `mem_flatten_of_mem_labs`

 The partition of a label is listed in the flattened table, and its number j is at most 2h. 

### `length_labs`

 The number of labels is the number of terms of the expansion: Σ_j p(s + j) row-wise and Σ_j p(2h
− s − j) column-wise. 

### `sum_map_labs`

 A sum over the list of the labels is the double sum of the expansion. 

 ### The interface lemmas 

### `stWords`

 A sum over all words of c bits of a product of two functions of the entry of a list with at most
2^c entries is the sum over the list. 

### `stLabs`

 The list of the labels: its length, sums over it, its members. 
