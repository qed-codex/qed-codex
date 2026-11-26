---
{
  "module": "proof/rates/ClauseBound/Inst/HalfPart.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfPart.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfPart.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The numbers of partitions and the table of all partitions, as programs

Without a pad: `pTab W` is the list p(0), …, p(W), computed one entry at a time by the recurrence
E·p(E) = Σ_{v ≥ 1} Σ_{k ≥ 1, kv ≤ E} v·p(E − kv) (`pTab_getD`). From it: `hF c₀ lam`, the first
E in 2 … c₀·lam² with p(E) ≥ 2^lam, which is `ClauseBound.Part.hOf lam` if that number is at most
c₀·lam² (`hF_eq`), and the sums `RrowF`, `RcolF` (`RrowF_eq`, `RcolF_eq`).
The table of all partitions of 0, …, W: `allTab W` is a list whose entry number E is the list of the
partitions of E as nonincreasing lists of positive integers (`allTab_getD`). It is built in
rounds k = 1, …, W; round k runs through E = 0, …, W and appends to entry E the lists k :: L for L
in the new entry E − k. `allTabF pad W` does the same with every state cut off by the pad; it is
equal to `allTab W` if the pad has length at least (7W + 10)·Σ_{E ≤ W} p(E) (`allTabF_eq`). 

 ### Definitions 

### `nextP`

 From the list T = p(0), …, p(N − 1) of length N: the number (Σ_{v=1}^{N} Σ_{k=1}^{N/v} v·T[N −
kv]) / N, which is p(N). 

### `pTab`

 The list p(0), …, p(W). 

### `pzF`

 The entry number E of a table of numbers, for an integer E; 0 for E < 0. 

### `hF`

 The first E in 2 … c₀·lam² with p(E) ≥ 2^lam; 2 if there is none. 

### `RrowF`

 Σ_{i=0}^{2h} p(s + i), from the table p(0), …, p(4h). 

### `RcolF`

 Σ_{i=0}^{2h} p(2h − s − i), from the table p(0), …, p(4h). 

### `PT`

 A table of partitions: entry number E is a list of partitions of E, each a list of its parts. 

### `initT`

 The table before the first round: the empty partition of 0. 

### `stepE`

 One step of round k: the new entry number E, appended to the new entries 0, …, E − 1. 

### `roundT`

 Round k: from the partitions into parts < k to those into parts ≤ k. 

### `allTab`

 The table of the partitions of 0, …, W. 

### `roundF`

 Round k with every state cut off by the pad. 

### `allTabF`

 The table of the partitions of 0, …, W with every state cut off by the pad. 

### `tabK`

 The table after round k. 

 ### Lists over a range 

### `sum_map_range`

 The sum of a list f 0, …, f (n − 1) as a sum over a range. 

### `sum_Icc_one`

 A sum over 1, …, n as a sum over a range. 

### `getD_map_range`

 The entry number i of the list f 0, …, f (n − 1). 

 ### The table of the numbers of partitions 

### `nextP_map`

 The recurrence computes p(N) from p(0), …, p(N − 1), for N ≥ 1. 

### `pTab_succ`

 One more entry. 

### `pTab_eq`

 The table is the list p(0), …, p(W). 

### `length_pTab`

 The table has W + 1 entries. 

### `pTab_getD`

 The entry number i ≤ W of the table is p(i). 

### `pzF_pTab`

 The entry number E ≤ W, for an integer E. 

### `hF_eq`

 `hF` finds `hOf lam` if that number is at most c₀·lam². 

### `hF_le`

 `hF` is at most c₀·lam² + 2. 

### `two_le_hF`

 `hF` is at least 2. 

### `RrowF_eq`

 The number Σ_{i=0}^{2h} p(s + i) of terms of the row-wise factorization of a piece, read from
the table, for s ≤ 2h. 

### `RcolF_eq`

 The number Σ_{i=0}^{2h} p(2h − s − i) of terms of the column-wise factorization of a piece, read
from the table, for s ≥ −2h. 

 ### The table of all partitions 

### `initT_eq`

 Before the first round. 

### `foldl_stepE`

 The first j steps of round k + 1. 

### `roundT_tabK`

 Round k + 1. 

### `foldl_roundT`

 The first j rounds. 

### `allTab_getD`

 The entry number E ≤ W of the table is the list of the partitions of E. 

### `mem_allTab_getD`

 Its members are the nonincreasing lists of positive integers with sum E. 

### `length_allTab_getD`

 There are p(E) partitions of E. 

### `nodup_map_coe_allTab_getD`

 As multisets they are different from each other. 

### `toFinset_map_coe_allTab_getD`

 As multisets they are the monomials of weight E. 

### `mem_flatten_allTab`

 The members of the flattened table are the nonincreasing lists of positive integers with sum at
most W. 

 ### The lengths of the words, and the pad 

### `len_le_of_forall`

 A list of n members with words of length at most c has a word of length at most n·(c + 2) + 2. 

### `len_parts_le`

 The word of a list of positive integers with sum E has length at most 7E + 2. 

### `len_partsLe_le`

 The word of the list of the partitions of E into parts ≤ k. 

### `len_map_partsLe_le`

 The word of the first j entries of the table after round k. 

### `len_state_le`

 All states of the computation of the table have words of length at most (7W + 10)·Σ_{E ≤ W}
p(E). 

### `foldl_stepE_cap`

 The first j steps of round k + 1 with the pad. 

### `allTabF_eq`

 With a pad of length at least (7W + 10)·Σ_{E ≤ W} p(E) no cut-off is active. 
