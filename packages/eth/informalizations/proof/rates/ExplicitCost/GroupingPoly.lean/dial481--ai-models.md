---
{
  "module": "proof/rates/ExplicitCost/GroupingPoly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/GroupingPoly.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/GroupingPoly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The procedure of Lemma 8 (Appendix A, the grouping with explicit cost) has polynomial-time steps

One certificate for all K, g and ζ: these are read from the input. The certificates of the
constructions are those of proof/machines/QueryMachines/Poly.lean and
proof/threesat/Exits/Poly.lean; those of the plain functions, jointly in K, g and the input, are
those of proof/rates/PaddedDescent/F/CertNet.lean; that of an entry is `entryDataCert`. Proved here:

* `inK_unary`, `inG_unary`, `inP_unary`, `inB_unary`, `inU_unary`: K, g, P, B stand in the input in
  unary, and U is a sum of numbers that do;
* `label_le`, `labelLength_polyT`, `labelLength_unary`: L is at most U + 2gP + 1 on EVERY input
  (this is what min(a, b) in its definition is for), so it can be written in unary;
* `bitsOut_unary`: B' in unary; `good_joint`, `goodData_polyT`: the test of a grouping;
  `toLists_joint`, `entryInput_polyT`: cutting a setting into its strings, with K and L computed
  from the input; `callOf_polyT`: the call;
* `groupingPoly`: the search, the call, and the two substitutions. 

 ## The numbers 

### `inK_unary`

 K is given in unary. 

### `inG_unary`

 g is given in unary. 

### `inP_unary`

 P is given in unary. 

### `inB_unary`

 B is given in unary. 

### `inU_unary`

 U is a sum of g² numbers that are given in unary. 

### `label_le`

 ⌈(bU + 2·min(a, b)·gP)/(bK²)⌉ ≤ U + 2gP + 1, for all natural numbers. 

### `label_joint`

 The formula for L, jointly in all its numbers. 

### `labelLength_polyT`

 L is computed in polynomial time. 

### `labelLength_unary`

 L can be written in unary in polynomial time. 

### `bits_joint`

 The formula for B', jointly in all its numbers. 

### `bitsOut_unary`

 B' can be written in unary in polynomial time. 

 ## The test, the queries, the call 

### `good_joint`

 The test of a grouping, jointly in K, g, L, the number of the grouping and the input. 

### `goodData_polyT`

 The test of the procedure is computed in polynomial time. 

### `toLists_joint`

 Cutting a setting z_w into its K − 1 strings of λ bits, jointly in K, λ and the query. 

### `entryInput_polyT`

 How a query to the tables becomes an input of `entryData`. 

### `callOf_polyT`

 The call is computed in polynomial time. 

 ## The machines 

### `groupingCall_poly`

 The procedure up to the call has polynomial-time steps. 

### `groupingPoly`

 The procedure has polynomial-time steps, up to the call and as a whole if E has and `arg` is
polynomial-time. 
