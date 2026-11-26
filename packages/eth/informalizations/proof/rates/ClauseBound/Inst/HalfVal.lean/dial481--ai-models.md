---
{
  "module": "proof/rates/ClauseBound/Inst/HalfVal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfVal.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfVal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The pieces with ρ = 1/√2 as programs: the values of the two functions of a factorization

`partH c₀ top` is the program for one of the two functions of a factorization. This file says what
it returns when the pad is long enough (`partH_eq`): the label θ, read as a number,
picks the pair (j, τ) with that number in the list `labs`, and the value is an entry of one of the
matrices `ClauseBound.Boson.topK`, `ClauseBound.Boson.botK` (`valK` of
proof/rates/ClauseBound/Inst/HalfIfc.lean), or 0 if the list has no such pair.
Two statements on the tables are taken as hypotheses: `StTopF` and `StBotF` say that `topF` and
`botF`, applied to the list of all partitions of 0, …, 4h, return the entries of `topK` and `botK`.
The strings enter through their partitions only, which have to be listed and of weight h; the
interface statement `StEnc` says that they are. The end of the file is `stVal`, which proves
the interface statement `StVal` from these three. 

### `StTopF`

 With a pad of length at least `padLen h`, `topF` on the list of all partitions of 0, …, 4h
returns the entries of `topK μ h i r`, for a listed μ of weight h and i ≤ 2h. 

### `StBotF`

 With a pad of length at least `padLen h`, `botF` on the list of all partitions of 0, …, 4h
returns the entries of `botK μ h r`, for a listed μ of weight h. 

### `mem_flatten_of_mem_getD`

 A member of an entry of a table is a member of the flattened table. 

### `mem_labs`

 A pair (j, τ) of the list of labels has j ≤ 2h and a listed τ. 

### `deltaF_eq`

 The number of all partitions of 0, …, 4h, as a sum. 

### `pad_allTab`

 A pad of length `padLen h` suffices for the table of all partitions of 0, …, 4h. 

### `partT_eq`

 What `partT` returns on the table of all partitions of 0, …, 4h, if the pad is long enough and
the partitions of the two strings are listed and have weight h. 

### `partH_eq`

 What `partH c₀ top` returns on two strings of λ bits and a label θ, with h = `hF c₀ λ`, s =
`sOf h i` and T the table of all partitions of 0, …, 4h: the value `valK` at the pair number θ
of the list of labels, or 0 if there is no such pair. The pad has length at least `padLen h`, and
the partitions of the two strings are listed and have weight h. 

### `stVal`

 The values of the two programs, as the interface states them: h is the least number ≥ 2 with
p(h) ≥ 2^λ, which the program finds if it is at most c₀·λ². 
