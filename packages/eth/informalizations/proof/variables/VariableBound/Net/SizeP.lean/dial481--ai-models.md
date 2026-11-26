---
{
  "module": "proof/variables/VariableBound/Net/SizeP.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/SizeP.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/SizeP.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 3, «The parameters»

«At most Δ⌈n/g⌉ clauses have a variable at a; each gives z_a one mark of kind 0 and load(E) ≤ t̄ + 2
marks of kind 1; the checks with home a give at most ⌈r̄/g⌉·s̄ more. So z_a has at most P₀ bits.
An object has at most two tests at a, and ⌈log C(t, μ)⌉ ≤ t, so condition (i) of the definition of a
network holds with P = ⌈2P₀⌉.» One theorem for each of these sentences, then the network of a
profile
has size P (`sized_netDN`, `sized_PD`), and with the bound on |W_a| of
proof/variables/VariableBound/Net/SizeB.lean the statement `StSized`. Display (69) is proved in
SizeB.lean, the case m ≤ n̄ in SizeSmall.lean. Some counting lemmas come from
proof/rates/PaddedDescent/F/MarkDeg.lean. 

 ### The number of objects that touch a node 

### `countP_block_le`

 A clause with a variable among a·q, …, a·q + q − 1 is counted at one of these variables (0 < q). 

### `card_clauses_at_le`

 Step 3, «The parameters»: «at most Δ⌈n/g⌉ clauses have a variable at a», if 0 < g, the data are
well-formed (`WfD`) and every variable occurs in at most Δ clauses. 

### `colD_eq`

 load(E) as the number of the checks j < r that contain the clause number e. 

### `card_objs_of_clause_le`

 Step 3, «The parameters»: a clause E «gives one mark of kind 0 and load(E) marks of kind 1»: at
most 1 + load(E) objects have the clause number e (for well-formed data, `WfD`). 

### `card_var_at_le`

 The objects whose clause has a variable at a: at most Δ⌈n/g⌉·(1 + c), if 0 < g, the data are
well-formed (`WfD`), every variable occurs in at most Δ clauses and load(E) ≤ c for every clause. 

### `card_home_at_le`

 The incidences of the checks with home a: at most the sum of the sizes of these checks (for
well-formed data, `WfD`). 

### `length_tch_le`

 The number of objects that touch a: at most Δ⌈n/g⌉·(1 + c) plus the sizes of the checks with
home a, if 0 < g, the data are well-formed (`WfD`), every variable occurs in at most Δ clauses and
load(E) ≤ c for every clause. 

### `le_qv_mul`

 r ≤ ⌈r/g⌉·g for 0 < g. 

### `card_home_le`

 At most ⌈r/g⌉ of the checks j < r have the home a (0 < g). 

### `qv_mono`

 ⌈r/g⌉ grows with r. 

 ### The size of the network of a profile 

### `cw_le`

 Step 3, «The parameters»: ⌈log C(t, μ)⌉ ≤ t. 

### `sum_capD_le`

 The capacities at a node a < g sum to at most twice the number of objects that touch a: «an
object has at most two tests at a, and ⌈log C(t, μ)⌉ ≤ t». 

### `abs_boole_le`

 A number that is 0 or 1 is at most 1 in absolute value. 

### `one_le_two_pow`

 1 ≤ 2^B in the integers. 

### `sized_netDN`

 The network of the profile y has size P with values bounded by 2^B, if at every node a < g the
number ⌈n/g⌉ + (number of objects that touch a) of bits of a setting is at most P, twice the number
of
objects that touch a is at most P, and |W_a| ≤ 2^B. 

 ### P₀ and P 

### `sum_home_le`

 Step 3, «The parameters»: «the checks with home a give at most ⌈r̄/g⌉·s̄ more», if 0 < g, 0 ≤
s̄, r ≤ r̄ and |Λ_j| ≤ s̄ for all j. 

### `bits_le_P0`

 Step 3, «The parameters»: «so z_a has at most P₀ bits», if 0 < g, 0 ≤ s̄, the data are
well-formed (`WfD`), every variable occurs in at most Δ clauses, r ≤ r̄, |Λ_j| ≤ s̄ for all j and
load(E) ≤ t̄ + 2 for
every clause. 

### `le_PD`

 A natural number that is at most 2P₀ is at most P = ⌈2P₀⌉. 

### `sized_PD`

 Step 3, «The parameters»: the network of a profile has size P = ⌈2P₀⌉ with values bounded by
2^B, if |W_a| ≤ 2^B at every node a < g, and 0 < g, 0 ≤ s̄, the data are well-formed (`WfD`), every
variable
occurs in at most Δ clauses, r ≤ r̄, |Λ_j| ≤ s̄ for all j and load(E) ≤ t̄ + 2 for every clause. 

### `stSized`

 Step 3, «The parameters»: for a list with display (67), the network of an admissible profile
satisfies conditions (i) and (ii) of the definition of a network with P = ⌈2P₀⌉ and B = (k + 1)M + 1.
Hypotheses: 0 < g, 0 ≤ s̄, the data are well-formed (`WfD`), every variable occurs in at most Δ
clauses, r ≤ r̄, |Λ_j| ≤ s̄ for all j, load(E) ≤ t̄ + 2 for every clause, and the profile is
admissible. 
