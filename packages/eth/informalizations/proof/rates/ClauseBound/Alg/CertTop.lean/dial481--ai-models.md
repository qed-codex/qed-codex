---
{
  "module": "proof/rates/ClauseBound/Alg/CertTop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/CertTop.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/CertTop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The top level in m is polynomial-time

Polynomial-time certificates (`PolyT`) for the function `AM` of (input, pad) and for the exponent
function `eM` of the input (`stCertM`), and for the network `satFk` of a k-CNF in which
both the number g of groups and the width k are part of the data, in unary (`stCertSatK`). The
certificates of proof/machines/ToTuring/Poly/Count.lean have g and k as constants;
proof/rates/ClauseBound/Alg/CertCount.lean has those that do not depend on k, with g as data; this
file gives the others, with g as data and k a
function of the input. 

 ### The network of a k-CNF, with g and k as data 

### `litAt_polyT3`

 The literal at a slot, jointly in k, the formula and the slot. 

### `varAt_polyT3`

 The variable at a slot, jointly in k, the formula and the slot. 

### `slotsOf_polyT3`

 The list of the slots of a formula, jointly in k, in unary, and the formula. 

### `linkB_polyT3`

 The test «slot i' is the next occurrence of the variable at slot i», jointly in k, in unary, the
formula and the two slots. 

### `locals_polyT3`

 The list of the slots of a group, jointly in g, k in unary and the formula. 

### `links_polyT3`

 The list of the links between two groups, jointly in g, k in unary, the formula and the two
groups. 

### `wF_polyT3`

 The weight of a group of clauses at a state word, jointly in g, k in unary, the formula and the
query. 

### `fF_polyT3`

 The factor of two groups of clauses at a state word and a label word, jointly in g, k in unary,
the formula and the query. 

### `capF_unary3`

 The number of label bits of two groups is given in unary, jointly in g, k in unary, the formula
and the two groups. 

### `stCertSatK`

 The four functions of the network of a k-CNF are polynomial-time, with the number of groups and
the width, both in unary, as data. 

 ### Numbers in unary 

### `unary_max`

 The larger of two numbers given in unary is given in unary. 

### `unary_size`

 The number of binary digits of a number given in unary is given in unary. 

### `root9_polyT`

 ⌊m^{1/9}⌋ is polynomial-time in m, when m is given in unary. 

### `PtopK_unary`

 The bound P of the network of a k-CNF is given in unary if g, k and m are. 

### `lamTopK_unary`

 The label length of the top instance is given in unary if K, g, k and m are. 

### `entry_unary`

 The bound on the size of the entries of the top instance is given in unary if K and P are. 

### `maxFour_polyT`

 The largest of the four exponents of the top level is polynomial-time in the numbers K, P, λ and
the exponent v of the solver. 

 ### The function and its exponent 

### `countG_polyT`

 The value of the network of a formula is polynomial-time jointly in the pad, the index, k in
unary and the formula. 

### `needTopC_polyT`

 The exponent of a pad that suffices at an index, computed under a bound, is polynomial-time
jointly in the bound, the index, k and m in unary. 

### `planM_polyT`

 The choice between the clique algorithm and exhaustive counting is polynomial-time in the input. 

### `stCertM`

 The function of (input, pad) and the exponent function of the input are polynomial-time. 
