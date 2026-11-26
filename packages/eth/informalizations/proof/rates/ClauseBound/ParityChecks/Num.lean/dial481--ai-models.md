---
{
  "module": "proof/rates/ClauseBound/ParityChecks/Num.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Num.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Num.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The truncated potential is num / den

A state of the choice of the checks is (Ls, cur, e): the complete checks, the part of the current
check chosen so far, the number e of clauses already decided for it. With j the number of
complete checks, k = r − 1 − j and p = 1/nb, the four terms of the truncated potential of that state
are
5^k·numP/(2·8^k·nb^i₀) (`Num.tUpar_eq`), numI/(8mr) (`Num.Uinc_eq`), numR/(8r(nb+1)^m)
(`Num.Urow_eq`) and numC/(8m(nb+1)^r) (`Num.Ucol_eq`),
and over the common denominator `den` their sum has the numerator `num` (`num_div_den`). The sums
over the checks 0, …, r − 1 are split into the complete checks, the current check and the
later, empty checks. The auxiliary statements are in the namespace `ClauseBound.ParityChecks.Num`. 

### `ChkOK`

 A list of clauses without repetition, all below e. 

 ### Lists and sums 

### `list_sum_range`

 The sum of a list of values at 0, …, n − 1. 

### `sum_getD`

 A sum over the first entries of a list of checks. 

### `sum_split`

 A sum over 0, …, r − 1, split at j. 

### `getD_mid`

 The current check. 

### `getD_late`

 The later checks are empty. 

### `countP_eq_sum`

 The number of lists that contain x, as a sum. 

### `card_filter_mem`

 The set of a list without repetition has as many elements as the list. 

### `card_Dset`

 m − e clauses are not yet decided. 

### `frac`

 2^a/(1 + p)^c over the denominator (nb + 1)^n, for c ≤ n. 

 ### The state 

### `card_lam`

 A check as a set has as many elements as its list. 

### `isState`

 The state (Ls, cur, e) is a state in the sense of `IsState`. 

### `den_pos`

 The common denominator is positive. 

 ### The four terms 

### `all_ok`

 All checks of the state are lists without repetition of clauses below m. 

### `undRow_early`

 For an earlier check all clauses are decided. 

### `undRow_mid`

 For the current check m − e clauses are not yet decided. 

### `undRow_late`

 For a later check no clause is decided. 

### `sum_card`

 The number of pairs (check, clause in it). 

### `sum_undRow`

 The number of undecided pairs. 

### `Uinc_eq`

 Υ_inc = numI/(8mr). 

### `sum_row`

 The numerators of the terms of Υ_row add up to numR. 

### `Urow_eq`

 Υ_row = numR/(8r(nb+1)^m). 

### `card_col`

 The number of checks that contain the clause x. 

### `sub_undCol`

 The number of checks for which the clause x is decided. 

### `sum_col`

 The numerators of the terms of Υ_col add up to numC. 

### `Ucol_eq`

 Υ_col = numC/(8m(nb+1)^r). 

### `numP_cast`

 numP = nb^i₀·(A + Σ_{i ≤ i₀} (−2p)^i·B_i). 

### `tUpar_eq`

 The truncated Υ_par = (5/8)^k·½·numP/nb^i₀. 

### `num_div_den`

 The truncated potential is num / den. 
