---
{
  "module": "proof/rates/ClauseBound/Inst/CertHalf.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/CertHalf.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/CertHalf.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Certificates for the pieces with ρ = 1/√2: the two functions of a factorization

The programs of proof/rates/ClauseBound/Inst/Half.lean are polynomial-time (PolyT): the number s of
a piece, the weights, the list `labs` of the pairs (j, τ) that the labels stand for, the code `encF`
of a
string, and the two functions of a factorization, first with all their arguments apart (`partT`),
then as functions of one query (`partH`). The number h is given in unary.

The entries of the matrices, `topF` and `botF`, enter through their certificates, in the form of the
statements `StTopF` and `StBotF`. The first of them asks for the number j of a pair in
unary. A member (j, τ) of `labs` has j ≤ 2h, so that j can be replaced by min j (2h) without
changing a value (`partT_eq`); this number is given in unary. The two statements are proved below
(`stTopF`, `stBotF`) from the certificates `topF_polyT` and `botF_polyT` of the imported files. With
them and the five certificates of proof/rates/ClauseBound/Inst/CertHalfSmall.lean, the end is
`halfF_keeps`: for all values of its two parameters the family `halfF`
has the certificates `PiecesF.Keeps` that the algorithm asks of a family of pieces. 

### `StTopF`

 The entries `topF` are polynomial-time, for W, h and the number i in unary. 

### `StBotF`

 The entries `botF` are polynomial-time, for W and h in unary. 

 ### The labels and the code 

### `sOf_polyT`

 The number s of a piece is polynomial-time. 

### `wOf_polyT`

 The weight of τ in a pair (j, τ) is polynomial-time. 

### `labs_polyT`

 The list of the pairs (j, τ) is polynomial-time, for h in unary. 

### `encF_polyT`

 The partition that a string stands for is polynomial-time. 

### `fst_le_of_mem_labs`

 A member (j, τ) of the list of the pairs has j ≤ 2h. 

 ### The two functions of a factorization 

### `bodyT`

 The value of one of the two functions at the pair (j, τ). 

### `partT_eq`

 The number j of a pair may be cut off at 2h. 

### `bodyT_polyT`

 The value at a pair (j, τ) is polynomial-time, for h and j in unary. 

### `partT_polyT`

 One of the two functions of a factorization, with its arguments apart, is polynomial-time, for h
in unary. 

### `partH_polyT_of`

 The two functions of a factorization are polynomial-time in the query, given the certificates of
the entries of the matrices. 

 ### The family 

### `stTopF`

 The certificate of `topF`, in the form in which it is used here. 

### `stBotF`

 The certificate of `botF`, in the form in which it is used here. 

### `partH_polyT`

 The two functions of a factorization are polynomial-time in the query. 

### `halfF_keeps`

 The pieces with ρ = 1/√2 keep polynomial time, for all values of the two parameters. 
