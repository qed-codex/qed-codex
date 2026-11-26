---
{
  "module": "proof/rates/PaddedDescent/F/CertMark.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/CertMark.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/CertMark.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial-time certificates (`PolyT`) for the network of marks of
proof/rates/PaddedDescent/F/MarkNet.lean, one lemma for each of its functions, with the numbers g,
n, β, b in unary
and the layers and the profile as data. Every certificate is stated for arguments that depend on a
context x. The last two theorems, `certMark` and `certAdm`, prove the interface statements
`StCertMark` and `StCertAdm` of proof/rates/PaddedDescent/F/Interfaces.lean. The proofs use the
closure
lemmas of proof/machines/ToTuring/Lib and proof/machines/ToTuring/Poly/Digits.lean and those of
proof/rates/PaddedDescent/F/FuelCert.lean. The weight `mW` is cut into its four tests and its sign,
which are
certified one by one. 

### `qv_polyT`

 The number of variables per node is polynomial-time in g and n. 

### `cls_polyT`

 The list of all clauses with the index of their layer. 

### `clAt_polyT`

 Clause number e with the index of its layer. 

### `tchB_polyT`

 The test «clause e touches node a». 

### `tch_polyT`

 The list of the clauses that touch a node. 

### `linkB_polyT`

 The test «a and b are neighbours in the chain of clause e»; g is in unary because the test runs
through all nodes. 

### `ownB_polyT`

 The test «a is the least node that clause e touches». 

### `tst_polyT`

 The list of the clauses of a layer whose marks two nodes compare. 

### `mark_polyT`

 The mark that a state word gives to a clause. 

### `str_polyT`

 The string of the marks that two nodes compare in a layer. 

### `enc_polyT`

 The block code is polynomial-time, with β and the block length b in unary. 

### `mu_polyT`

 A number prescribed by the profile: one digit of y. 

### `mu_le`

 A number prescribed by the profile is at most the number of clauses. 

### `mu_unary`

 A number prescribed by the profile is given in unary, since it is at most the number of clauses. 

### `mcap_unary`

 The length of the label between two nodes is given in unary. 

### `mlab_polyT`

 The label that a state word sends to another node. 

### `neg_one_pow_eq`

 (−1)^k by the parity of k. 

### `sign_polyT`

 The sign (−1)^k is polynomial-time in k. 

### `qv_unary`

 The number of variables per node is given in unary if g and n are. 

### `mW1`

 The first test of `mW`: the bits of absent variables are false. 

### `mW2l`

 One literal in the second test of `mW`. 

### `mW2`

 The second test of `mW`: a marked clause has all its literals at a false. 

### `mW3`

 The third test of `mW`: the numbers of owned marked clauses are those of the profile. 

### `mW4`

 The fourth test of `mW`: the weights of the strings are those of the profile. 

### `mWs`

 The exponent of the sign in `mW`. 

### `mW_eq`

 `mW` written with the four tests and the exponent named above. 

### `mW1_polyT`

 The first test of `mW` is polynomial-time. 

### `mW2l_polyT`

 The test of one literal is polynomial-time. 

### `mW2_polyT`

 The second test of `mW` is polynomial-time. 

### `mW3_polyT`

 The third test of `mW` is polynomial-time. 

### `mW4_polyT`

 The fourth test of `mW` is polynomial-time. 

### `mWs_polyT`

 The exponent of the sign in `mW` is polynomial-time. 

### `mW_polyT`

 The weight of a state word at a node is polynomial-time, with g and n in unary. 

### `markF_keeps`

 The lengths of the network of marks are given in unary, and its two functions are
polynomial-time. 

### `sum_range_eq`

 In a double sum over a' < a < g the inner range can be cut out of the outer one. 

### `adm_polyT`

 The test «the profile y is admissible» is polynomial-time, with g in unary, for every width k of
the clauses. 

### `certMark`

 The network of marks has lengths in unary and polynomial-time functions. 

### `certAdm`

 The test for admissible profiles is polynomial-time in (g, n, w in unary), the layers and the
profile. 
