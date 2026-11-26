---
{
  "module": "ThreeSumApsp/Sec4/Table2/Captions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Table2/Captions.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Table2/Captions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The captions of Tables 1 and 2

* "the θ at which γ = κ - q" (Section 4.4), which the right half of Table 2 uses: `γ` and `q`
  increase with `θ` (`gammaOf_strictMono`, `qOf_strictMonoOn`), so `γ + q` takes the value `κ`
  exactly once, and there the exponent `min{γ, κ - q}` of Corollary 32 is largest
  (`exists_gammaOf_eq_sub_qOf`). Nothing else rests on this lemma.
* For every entry, Corollary 31 or 32 gives what the caption of Table 2 claims:
  `table_2_query_valid`, `table_2_ninth_valid`, `table_2_density_valid`.
* "A larger c gives a larger γ but a smaller ε" (`table_2_larger_c`), and the parameters of Section
  2 are the entry `c = 19`, `q = 0.43` (`table_1_section_2_column`).

The rows themselves are `table_2_c40` to `table_2_c10_5`.


 ## The `θ` at which `γ = κ - q` 

### `exists_gammaOf_add_qOf_eq`

 The balance point exists: `γ + q` is continuous, it is 0 at `θ = 0`, and at `θ = 0.9` it exceeds
`log_4 10 ≥ κ`. 

### `exists_gammaOf_eq_sub_qOf`

 Section 4.4 speaks of "the θ at which γ = κ - q": there is exactly one such `θ` in `(0, 0.9)`
when `c > 10` and `0 < κ ≤ log_4 10`, and the exponent `min{γ, κ - q}` of Corollary 32 is largest
there. At this `θ` the two terms of Corollary 32 are equal; Section 4.1: "Setting the parameters to
balance the preprocessing time and the total time for all the queries". 

 ## What the caption of Table 2 claims for an entry 

### `table_2_query_valid`

 Caption of Table 2, left half: "the numerical entry is a value γ for which Theorem 24 holds,
meaning that after O(N² log² D/D^γ) preprocessing, a query takes O(D^q log D) time", "whenever
D ≤ N^ε". For an entry computed as Section 4.4 prescribes (`Table2Query`), Corollary 31 gives these
bounds (`ValidQueryEntry`). 

### `table_2_ninth_valid`

 Caption of Table 2: "the column q = 0.43 uses the switching order t = m/9 of Section 2 (more
precisely, q = 0.4277…)". For an entry of this column, computed at `θ = 1/9` (`Table2Ninth`),
Corollary 31 gives the bounds of the caption with `q = 0.43`. 

### `table_2_density_valid`

 Caption of Table 2, right half: "the numerical entry is a value γ for which Theorem 25 holds,
meaning that any |W| ≤ N²/D^κ wanted entries take O(N² log² D/D^γ) time". For an entry computed as
Section 4.4 prescribes (`Table2Density`), Corollary 32 gives this bound (`ValidDensityEntry`). 

 ## The captions 

### `table_2_larger_c`

 Caption of Table 2: "A larger c gives a larger γ but a smaller ε" (at a fixed `θ > 0`). A fixed
`θ` is a fixed column of the left half of the table: there `γ` increases with `c` and `R_c(γ)`
decreases. In the right half `θ` changes with `c`; for it the sentence is not stated. Nor is it
stated for the `ε` of a row, which is the smallest `R_c(γ)` over all entries of the row. 

### `table_1_section_2_column`

 Table 1 (column "in Section 2"), Table 2's caption and Section 4.1: at `L = 19m` one has
"ρ < 1/2"; the bold entry `c = 19`, `θ = 1/9` is Theorem 5, "where γ = 1/18 = 0.0555…"; Theorem 5's
`ε = 1/18` is below `R_19(1/18)`; and "Theorem 5 is the entry c = 19, q = 0.43, applied to a set W
of N²/√D wanted entries (that is, κ = 1/2)", where the exponent `min{γ, κ - q}` of Corollary 32 is
still `1/18`. 
