---
{
  "module": "ThreeSumApsp/RunningTimes/Sec4/Corollary31_32.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec4/Corollary31_32.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec4/Corollary31_32.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollaries 31 and 32 on the word RAM

The route.  For rational `c` and `θ` the data structure of Theorem 30 with `L = ⌈cm⌉` levels and
switching order `t = ⌈θm⌉` is one program (`Light.Sec4.program31`), which computes `m`, `L` and `t`
itself.  The parameters include a threshold `m₀`: for `m < m₀` the preprocessing finds `m` and `4^m`
and stores the flag 0, and a query computes an inner product (the paper: "for smaller m the
corollary again holds trivially").  Real `c` and `θ` are replaced by rational ones nearby, for which
`ε` is still admissible, `γ` is no smaller and `q` no larger; at these the two costs of Theorem 30
obey the bounds of the corollaries on the inputs with `D ≤ N^ε` and `m ≥ m₀`
(`Light.Sec4.exists_ratParams`).  The two lemmas about this program, compiled
(`Light.Sec4.isDataStructure_of_costsWithin` for the data structure,
`Light.Sec4.solves_of_costsWithin` for the wanted entries), then give both corollaries in a form
that includes `D = 1` (`Corollary31.from_one`, `Corollary32.from_one`).  The corollaries as
printed, and the bounds without logarithmic factors for every `ε < ε*`
(`dataStructureBelow_wantedBelow_epsStar`), follow by arithmetic alone: the same programs, a smaller
domain, and a bound that dominates the proved one (`exists_isDataStructure_of_dominated`,
`exists_solves_of_dominated`).


 ## The form that includes `D = 1`

NOTE.  This form is not in the paper.  The last sentences of Theorems 1 and 3 have no lower bound
on `D`, while Theorems 24 and 25 and Corollaries 31 and 32 assume `D ≥ 2`; Section 4.1 adds that
"for D = 1 the bounds are trivial".  In a statement about programs, one program has to serve all
`D`, so the case `D = 1` cannot be added by arithmetic to a statement about `D ≥ 2`.  Here
`log D + 1` stands in place of `log D`, which is 0 at `D = 1`. 

### `Corollary31.from_one`

 Corollary 31, on the word RAM, with `D = 1` included: preprocessing in
`O(N² (log D + 1)² / D^γ)` time and space, and a query in `O(D^q (log D + 1))` time. 

### `Corollary32.from_one`

 Preprocess `X` and `Y` by Corollary 31 and "ask one query for each position of W" (proof of
Theorem 25; "With Corollary 31 in place of Theorem 24, the same argument gives explicit exponents"),
on the word RAM, with `D = 1` included: the entries at every set `W` of positions in
`O(|W| D^q (log D + 1) + N² (log D + 1)² / D^γ)` time. 

 ## The corollaries as printed 

### `wordRam_corollary_31`

 **Corollary 31**, on the word RAM. 

### `wordRam_corollary_32`

 **Corollary 32**, on the word RAM. 

 ## Without the logarithmic factors, for every `ε < ε*` 

### `dataStructureBelow_wantedBelow_epsStar`

 The last sentences of Theorems 3 and 1, on the word RAM, for every `ε < ε*` (the theorems have
`ε < 0.1204`): choose `c` and `θ` as in the proof of Theorem 24 (`exists_admissible`), for the
wanted entries with `q := κ/2` and `γ' := min{γ, κ/2}` as in the proof of Theorem 25, and give away
half of the exponent to absorb the logarithmic factors. 
