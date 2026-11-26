---
{
  "module": "proof/rates/PaddedDescent/F/CertGrid.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/CertGrid.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/CertGrid.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Certificates for the loop over the patterns and for the bottom

Polynomial time (PolyT), with the side length g of the grid as DATA in unary, for: the number of
rectangles nRect g, the prices
priceRow and priceCol of a pattern, the context sideCtx of the cheaper side network and the list of
patterns. From these, the certificate of
one level (StCertExpand) follows from those of the rebalancing with a given label length
(StCertRebalG) and of the side network (StCertSide); the label
length lamNext K g n that one level hands to the rebalancing is given in unary when K, g and the
label length n are. The last theorem is the
certificate of brute force at the bottom (StCertBrute). The proofs of the prices follow useRow_polyT
(proof/machines/ToTuring/Poly/Grid.lean),
where g is a constant of the machine. 

 ### The number of rectangles 

### `nRect_eq_mul`

 The number of rectangles is the square of g(g−1)/2. 

### `nRect_le_mul`

 There are at most g⁴ rectangles. 

### `nRect_polyT`

 The number of rectangles is polynomial-time in g. 

### `nRect_unary`

 The number of rectangles is given in unary if g is. 

### `numPat_polyT`

 The number of patterns, (n+1)^(nRect g) for the label length n, is polynomial-time if g is given
in unary. 

 ### The prices 

### `priceRow_polyT`

 The price of a pattern with the rows merged is polynomial-time, for g and the label length in
unary. 

### `priceCol_polyT`

 The price of a pattern with the columns merged is polynomial-time, for g and the label length in
unary. 

 ### One level 

### `sideCtx_polyT`

 The context of the cheaper side network. 

### `patterns_polyT`

 The list of the patterns, cut off by the pad. 

### `capM_unary`

 The bound on the label bits that two nodes of a side network share is given in unary (`Unary`)
if g and the label length are. 

### `Ubar_unary`

 The bound on U of the cheaper side network is given in unary if g and the label length are. 

### `lamNext_unary_aux`

 The label length one level down, with any number D in place of Dcol, is given in unary if K, g
and the label length are. 

### `lamNext_unary`

 The label length one level down is given in unary if K, g and the label length are. 

### `childF_polyT`

 The child of one pattern. 

### `certExpand`

 One level is polynomial-time, given the certificates of the rebalancing with a given label
length and of the side network. 

 ### The bottom 

### `look_polyT`

 Looking up an entry of a table is polynomial-time. 

### `bruteF_polyT`

 Brute force on K nodes, K a constant. 

### `certBrute`

 Brute force on 256 nodes is polynomial-time: the statement `StCertBrute`. 
