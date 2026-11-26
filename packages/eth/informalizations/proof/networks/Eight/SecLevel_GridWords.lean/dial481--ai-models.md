---
{
  "module": "proof/networks/Eight/SecLevel_GridWords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecLevel_GridWords.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecLevel_GridWords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 5 «One level of the recursion»: sentences of the proof of Proposition 3 for the networks that Algorithm 1 runs

Procedure CLIQUE of Algorithm 1 (`Eight.Level.levelAlg`) works with tables that take bit strings
written as lists, writes a function ι : ℛ → {0, …, t} as a number y < (t+1)^{|ℛ|}, whose digits in
base t + 1 are the values ι(q), and runs
the network `Eight.Level.netOfι g tr lam y Rm` (tr = false: rows, tr = true: columns), whose
settings and indices are words.

`netOfι_row` and `netOfι_col` say what this network is: the row network, or the column network, of
proof/networks/Eight/SecLevel_Grid.lean, for the tables carried to the grid and the function ι
written by y, with every setting and every index θ written
as a word (`Network.pull`). From this and the theorems of that file, several sentences of the proof
get a statement about the network that the algorithm runs:
display (34): `eqExpansion_words`; the settings: `netOfι_S`; «the value is Z_ι»: `value_netOfι`;
Definition 2 with P = g³λ and all values at most 2^{gB + g²t}: `netOfι_sized_t`; the totals:
`U_netOfι`; display (36): `eqMinTotal_words` (and `stMin` in proof/networks/Eight/Level/Min.lean). 

 ## A function ι written as a number 

### `card_rectangles_eq`

 The number of rectangles: |ℛ| is `nRect g`, the number that the algorithm uses. 

### `sum_patOf`

 The numbers y < (t+1)^{|ℛ|} write every function ι of display (34) exactly once: a sum over
these numbers is the sum over the functions. 

### `Zι_digOf`

 Z_ι depends only on the values of ι on ℛ. 

 ## Display (34) 

### `eqExpansion_words`

 **Display (34)** for the clique that the algorithm is given: 2^{t|ℛ|} · Z = ∑_ι Z_ι.
`Inst.ZW lam [] Rm` is the value of the (g², λ)-clique whose tables Rm take strings written as
lists; the sum is over the numbers y that write the functions ι.
From `Eight.eqExpansion`. 

 ## What the networks of the algorithm are 

### `netOfι_row`

 **The row network that the algorithm runs** is the row network of the proof of Proposition 3
(`Eight.rowNetwork`), for the tables carried to the grid and the function ι written by y, with
settings and indices written as words: a setting of a row
in g · g² · λ bits (`stC`), an index θ of two rows in c_{a,a'} bits (`gridCl`). 

### `netOfι_col`

 **The column network that the algorithm runs** is the column network of the proof of Proposition
3 (`Eight.colNetwork`), with settings and indices written as words. 

### `netOfι_S`

 «S_a is the set of these tuples, encoded by concatenation in g(g² − 1)λ ≤ P bits, where P =
g³λ.» Different from the paper: the settings are all words of exactly g³λ bits, because a setting of
a grid point has a dummy string for the grid point
itself (see `Eight.eqExpansion`). 

 ## «Each factor in (34) is used exactly once, so the value is Z_ι» 

### `value_netOfι`

 Both networks that the algorithm runs have the value Z_ι of display (34). From
`Eight.value_rowNetwork` and `Eight.value_colNetwork`: writing the settings as words does not change
the value, because every word of the right length writes a setting. 

 ## Definition 2 with P = g³λ and B₁ 

### `netOfι_sized_t`

 Both networks that the algorithm runs satisfy conditions (i) and (ii) of Definition 2 with P =
g³λ and all values at most 2^{gB + g²t}; this is the form that the proof of the cost of a level
uses. From `Eight.rowNetwork_sized_t` and
`Eight.colNetwork_sized_t`. `BoundedInst lam B Rm`: the tables are at most 2^B in absolute value at
the queries that are asked. 

 ## The smaller total (36) 

### `U_netOfι`

 The number that the algorithm computes for a network (`totalG`) is its total U. 

### `eqMinTotal_words`

 **Display (36)** for the two networks that the algorithm runs: min(U_row, U_col) ≤ N(ρ + 1/g) +
2g⁴, N = g⁴λ, ρ = 11/12. From `Eight.eqMinTotal`. 
