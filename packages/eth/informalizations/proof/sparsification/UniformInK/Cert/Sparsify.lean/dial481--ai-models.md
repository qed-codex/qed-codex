---
{
  "module": "proof/sparsification/UniformInK/Cert/Sparsify.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Cert/Sparsify.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Cert/Sparsify.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The choice of the heart at one step of the sparsification is polynomial-time jointly in the width k

The twin of proof/sparsification/SparsifyWidthK/Poly/Sparsify.lean and of the first half of
proof/rates/PaddedDescent/F/CertSparsify.lean. There the width k is a constant of every certificate,
and so are the lists that depend
on k alone: the 2^k masks, and the pairs (j, h) with their thresholds. Here k is a function of the
context x, and the two lists are computed. This takes polynomial time if k and 2^k are given in
unary: `masks k` is the list of the words of k bits of the numbers below 2^k, lowest bit first
(`masks_eq`), and each threshold in the list is 4 times a power of τ with an exponent below 2k.
The functions `heartsL`, `tryL`, `pickL` are `heartsP`, `tryT`, `pickK` with the two lists as
arguments. 

 ### The masks 

### `range_two_mul`

 The numbers below 2N are 0, 1, then 2, 3, and so on up to 2N-2, 2N-1. 

### `masks_eq`

 The list `masks k` consists of the words of k bits of the numbers 0, 1, …, 2^k - 1, lowest bit
first. 

### `masks_polyT`

 The list of all masks of length k is polynomial-time if k and 2^k are given in unary. 

 ### The pairs (j, h) and their thresholds 

### `pairsK_polyT`

 The list of the pairs (j, h) with 1 ≤ h < j ≤ k is polynomial-time if k is given in unary. 

### `le_of_mem_pairsK`

 In a pair (j, h) of the list, j is at most k. 

### `thetaU_eq`

 `thetaU τ i` as one expression: 1 if i = 0, otherwise 4·τ^(2i−1). 

### `thetaU_polyT`

 The threshold θ i is polynomial-time jointly in τ and i, if i is given in unary. 

### `thrList_polyT`

 The list of the pairs (j, h), each with its threshold θ (j - h), is polynomial-time jointly in τ
and k, if k is given in unary. 

 ### The rule with the two lists as arguments 

### `heartsL`

 `heartsP` with the list M in place of `masks k`. 

### `tryL`

 `tryT` with the list M in place of `masks k`. 

### `pickL`

 `pickK` with the list M in place of `masks k` and the list L in place of the pairs (j, h) with
their thresholds. 

### `pickK_eq_pickL`

 `pickK` is `pickL` at the two lists that belong to θ and k. 

### `polyT_heartsL`

 Listing the candidate hearts is polynomial-time jointly in the list of masks, the formula and
the sizes j and h. 

### `polyT_tryL`

 The search for a heart of a given size that reaches a given threshold is polynomial-time jointly
in the list of masks. 

### `polyT_pickL`

 The choice of the heart and its petals is polynomial-time jointly in the two lists. 

### `polyT_pickKU`

 The choice of the heart and its petals at a node is polynomial-time jointly in k, τ and the
formula, if k and 2^k are given in unary. 
