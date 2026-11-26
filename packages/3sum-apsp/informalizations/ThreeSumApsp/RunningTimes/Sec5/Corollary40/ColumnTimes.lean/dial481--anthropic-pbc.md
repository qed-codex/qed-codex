---
{
  "module": "ThreeSumApsp/RunningTimes/Sec5/Corollary40/ColumnTimes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary40/ColumnTimes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary40/ColumnTimes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 40: what the running times of v-hinted Mv and Mv-hinted Mv have in common

In both problems Phase 2 preprocesses an n × t matrix X and a t × n matrix Y, with t = ⌊n^τ⌋, and
Phase 3 asks for the n entries of a column of XY.  The paper treats the second problem with the
words "The proof is the same, with X := N_{[n],I} and Y := V".  This file has what is the same.

* `ColumnRates τ a₂ a₃`: at these sizes the preprocessing of the data structure takes O(n^a₂) steps
  and n queries take O(n^a₃).  It holds with the exponents of Corollary 26 for τ < 1/18
  (`columnRates_of_lt_eighteenth`) and with those of Corollary 31 for general τ
  (`columnRates_of_genParams`); the latter is for given c, θ, ε and γ, so that one γ serves all
  problems (`exists_genParams` chooses them for a given τ).
* `KitRates.phaseRun_column`: a run of three phases in which Phase 2 takes the time of the
  preprocessing and w more steps, and Phase 3 the time of n queries and O(n) more steps, is a
  `PhaseRun` with the exponents 0, a₂, a₃, if w = O(n^a₂).


 ## The rates at the sizes n and t 

### `ColumnRates`

 The data structure with the parameters G takes, at the sizes N = n and D = t = ⌊n^τ⌋, at most
C n^a₂ steps for the preprocessing, at most C n^a₃ steps for n queries, and at most A n² cells. 

### `columnRates_of_le`

 Rates tp and tq with tp ≤ E n^a₂ and n tq ≤ E n^a₃ are rates for a column. 

### `columnRates_of_lt_eighteenth`

 **The rates of Corollary 26**, for 0 < τ < 1/18: "in O(n²/D^0.063) = O(n^{2−0.063τ}) time" and
"O(n D^0.437) = O(n^{1+0.437τ}) time". 

### `columnRates_of_genParams`

 **The rates of Corollary 31**, for parameters c, θ, ε, γ as in `GenParams` and 0 < τ < ε: "Phase
2 in O(n²/D^γ) = O(n^{2−γτ}) time and Phase 3 in O(n D^{1/2}) = O(n^{1+τ/2}) time". 

 ## The three phases 

### `columnSpace_le`

 The inputs, the output and what else lies before the data structure, at most 3 + 5 n² cells,
and a data structure of at most A n² cells take polynomially many cells. 

### `KitRates.phaseRun_column`

 **Three phases over a kit with given rates.**  The data structure lies at the address fr, with
n ≤ fr ≤ 3 + 5 n², and the memory ends after it.  If Phase 1 takes at most 4 steps, Phase 2 the
time of the preprocessing and w ≤ 100 (n^a₂ + 1) more steps, and Phase 3 the time of n queries and
30 n + 64 more steps, then the run is within limits that are polynomial in n, and the phases take
O(1), O(n^a₂) and O(n^a₃) steps. 
