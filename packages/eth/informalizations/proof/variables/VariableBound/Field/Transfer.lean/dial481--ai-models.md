---
{
  "module": "proof/variables/VariableBound/Field/Transfer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Transfer.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Transfer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lists and finite sets

No arithmetic in the finite field of the proof of Lemma 13 is done here; only lists and finite sets.
`wordsL s` lists every word of s bits once; each Γ_u (`gamW`) is listed as an increasing list of
numbers below m; `famD m a` may filter first and map afterwards (`famD_eq`); and
`isFamily_list`: if a list L without repetitions enumerates, through an injective D, the index set Ω
of sets Γ with (a), (b), (c) of Lemma 13 (Family of checks), and G u lists the set Γ (D u),
then the places of the list `L.map G` index a family with (a), (b), (c). 

 ### The words 

### `mem_wordsL`

 The members of `wordsL s` are the words of s bits. 

### `nodup_wordsL`

 No word occurs twice in `wordsL s`. 

### `mem_quad`

 The members of the four-fold product are the quadruples of words of s bits. 

### `nodup_quad`

 No quadruple occurs twice in the four-fold product. 

 ### The members of the family 

### `gamW_sorted`

 Γ_u is listed in increasing order. 

### `gamW_nodup`

 Γ_u is listed without repetitions. 

### `gamW_lt`

 The numbers in the list of Γ_u are below m. 

### `card_setD`

 A list of numbers below m without repetitions has as many members as the set it lists. 

### `famD_eq`

 The list of the family: first leave out the u with 2^a·|Γ_u| > 16m, then list the sets. 

 ### From an index set to the places of a list 

### `isFamily_comap`

 (a), (b), (c) of Lemma 13 (Family of checks) pass along an injective map φ of index sets with Ω =
φ(Ω'). 

### `isFamily_list`

 Let the list L have no repetitions, let D be injective on its members with image Ω, and let G u
list the set Γ (D u) for every member u of L. If the sets Γ_w, w ∈ Ω, have (a), (b), (c) of
Lemma 13 (Family of checks) for v, then the list `L.map G` has |Ω| members, and they, indexed by
their places, have (a), (b), (c) for v. 

 ### The number of bits 

### `sD_le`

 16m ≤ 2^s. 

### `sD_lt`

 2^s < 32m, for m ≥ 1. 

### `one_le_sD`

 s ≥ 1, for m ≥ 1. 
