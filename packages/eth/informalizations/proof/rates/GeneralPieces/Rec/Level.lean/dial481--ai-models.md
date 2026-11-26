---
{
  "module": "proof/rates/GeneralPieces/Rec/Level.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Rec/Level.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Rec/Level.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One level, by case (ii) of Lemma 8

This follows the step from ℓ to ℓ+1 in the proof of part (b) of Theorem A (Appendix A), at the
sentence "Case (ii) of Lemma 8 applies to the network with the
smaller total". `cases_ii` checks the hypotheses of case (ii), `Lof_le_lamNext` compares the lemma's
L with the label length of the program, `child_spec2` calls
the lemma (`GeneralPieces.grouping_general`) for one term of the sum over ι, and `stExpandG2` is the
whole level. Differences from the paper: ζ is written 3/(2D) for a natural number D ≥ 2; one label
length serves all ι; the cost appears as lower bounds on the length of the pad, not as a number of
operations. The program also handles steps marked thin, where the column network is summed by
enumeration (`enum_spec2`); no step of the schedule (40) is thin. 

 ### Case (ii) of the lemma applies 

### `zetaOf_mem`

 0 < ζ ≤ 1 for ζ = 3/(2D), D ≥ 2. 

### `cases_ii`

 "Case (ii) of the lemma applies to the network with the smaller total": K divides g, c_{a,a'} ≤
g²λ = P/g, and 2ζ²g ≥ K·ln(2gK). Here the network has p nodes, each a merged row or column of d
nodes,
its parameter is P = m·p·d²·λ, and two nodes share at most d²·m·λ = P/p bits. 

### `Lof_le_lamNext`

 "The number L depends on ι; the bound holds for every ι": the lemma's L = ⌈(U + 2ζgP)/K²⌉ is at
most the label length `lamNextG` that the program uses for all ι, if U is at most the bound
`ubarG` for the smaller total. 

 ### A term that is rebalanced 

### `child_spec2`

 One term of the sum over ι (a pattern, numbered y) whose network, on g = p nodes that are merged
rows or columns of e = d nodes, is rebalanced, by case (ii) of Lemma 8: the new instance has the
value of the
network and is well formed. 

 ### A term that is evaluated at once 

### `enum_spec2`

 One term of the sum over ι (a pattern, numbered y) whose column network is evaluated by
enumeration: the result is the value of the network, and it is small. 

 ### The level 

### `stExpandG2`

 One level: the factor d^|R| times Z is the sum of the terms evaluated at once and of the values
of the new instances; these are well formed; there are few; the sum is small. 
