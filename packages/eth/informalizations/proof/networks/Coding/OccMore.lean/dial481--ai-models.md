---
{
  "module": "proof/networks/Coding/OccMore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/OccMore.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/OccMore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The printed network of Φ: Definition 2, small values, the count

For `Coding.occNet g Φ`, the network of Section 6, with one bit per occurrence:
* `stOccNetIs`: «The network of Φ is the following network on [g] with P = 6m̄ and B = 1 …
  Definition 2 holds: Σ_{b ≠ a} c_{a,b} ≤ 2·3m̄ = P», except condition (iii) of Definition 2, which
  `Net.Is` does not contain. The bound on the row sums is taken from the padded network `wordNet`,
  which has the same numbers c_{a,b} (`capF_eq`).
* `stOccNetSmall`: «Their length is at most 3m̄ ≤ P», «all values are 0 or 1».
* `stOccNetCountsOf`, `stOccNetCounts`: «Hence Z is the number of assignments of the variables
  occurring in Φ that satisfy Φ», so Φ is satisfiable if and only if Z > 0, carried over from the
  padded network of Φ, whose value `Eight.network_value_eq` gives, since padding does not change the
  value.
* `stRowSumReached`: the footnote «P is taken as large as 6m̄ because Σ_{b ≠ a} c_{a,b} can reach
  6m̄». `import all StepMachines.Prog.CountNet` gives access to `boole_congr`, which is not public. 

### `length_occIn_le`

 There are at most 3 occurrences for each clause. 

### `boole_zero_or_one`

 [p] is 0 or 1. 

### `abs_boole_lt`

 |[p]| < 2^B with B = 1, as condition (ii) of Definition 2 asks. 

### `stOccNetSmall`

 «Their length is at most 3m̄ ≤ P» and «all values are 0 or 1» (Section 6). 

### `stOccNetIs`

 «The network of Φ is the following network on [g] with P = 6m̄ and B = 1 … Definition 2 holds:
Σ_{b ≠ a} c_{a,b} ≤ 2·3m̄ = P» (Section 6): the printed network satisfies Definition 2 except
condition (iii), with P = 6m̄ and B = 1, for m ≥ 1. 

### `stOccNetCountsOf`

 **«Hence Z is the number of assignments of the variables occurring in Φ that satisfy Φ», so Φ is
satisfiable if and only if Z > 0** (Section 6), for the printed network, from its two hypotheses:
the padded network of Φ is the printed one with padding (`StOccNet`), and padding does not change
the value (`StPaddingValue`). 

### `stOccNetCounts`

 **«Hence Z is the number of assignments of the variables occurring in Φ that satisfy Φ», so Φ is
satisfiable if and only if Z > 0** (Section 6), for the printed network. 

### `stRowSumReached`

 «P is taken as large as 6m̄ because Σ_{b ≠ a} c_{a,b} can reach 6m̄» (Section 6, footnote):
three clauses on three variables, one clause in each cluster; the middle cluster has three tests to
each of the other two. 
