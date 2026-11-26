---
{
  "module": "proof/rates/PaddedDescent/Choice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Choice.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Choice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The parameters chosen from one integer s

For precision s the algorithm uses the threshold τ = 2^(4s+17), the code parameter β = (s+7)² and
the depth t = ⌊19s/3⌋ + 700, whatever the width k of the clauses. The
thresholds of the sparsification for clauses of width k are those of `WidthK.Defs`: there a path of
the tree has at most bsum τ k · n steps and a leaf has at most
leafC τ k · n clauses. Both numbers are at most a power of τ whose exponent depends on k only, so
that they are below 2^β as soon as s ≥ `s0K k` = 2^(k+4). This file
proves that; the inequality (k/τ)·log₂(e·τ·bsum τ k) ≤ 1/2^s for such s, from which
`WidthK.stLeafCount` bounds the number of leaves by 2^(n/2^s); that t levels with
contraction 8963/10000 make up for the factor 2^10·(s + 8)⁶·2^s; and that K_t is at least 2^(4β +
10s + 1000). 

 ### The threshold of the sparsification 

### `two_pow_le_tauOf`

 2^17 ≤ τ. 

### `four_le_tauOf`

 4 ≤ τ. 

### `two_le_tauOf`

 2 ≤ τ. 

### `one_le_tauOf`

 1 ≤ τ. 

### `tauOf_pow`

 τ^e = 2^((4s+17)·e). 

### `bsum_tauOf_le`

 bsum τ k ≤ 2^((4s+17)·2^(k+1)). 

### `theta_tauOf_le`

 θ_j ≤ 2^((4s+17)·2^k) for j < k. 

### `leafC_tauOf_le`

 leafC τ k ≤ 2k·2^((4s+17)·2^k). 

 ### From s0K k on, the parameters are large enough for width k 

### `two_pow_s0K_le`

 2^(s0K k) ≤ C0K k: the pad suffices for exhaustive search while s < s0K k. 

### `le_of_s0K_le`

 k ≤ s for s ≥ s0K k. 

### `exponent_le_betaOf`

 The inequality between exponents behind the three lemmas that follow: (4s+17)·(2^(k+1) + 1) + k +
3 ≤ (s+7)² for s ≥ 2^(k+4). 

### `three_mul_tauOf_mul_bsum_le`

 3·τ·bsum τ k ≤ 2^β for s ≥ s0K k. 

### `bsum_le_two_pow_betaOf`

 bsum τ k ≤ 2^β for s ≥ s0K k. 

### `leafC_add_two_le`

 leafC τ k + 2 ≤ 2^β for s ≥ s0K k: in a leaf of the tree for width k every variable occurs in at
most 2^β − 2 clauses. 

### `add_seven_le`

 s + 7 ≤ 7·2^s. 

### `betaOf_le`

 β ≤ 49·4^s. 

### `tauOf_works`

 (k/τ)·log₂(e·τ·bsum τ k) ≤ 1/2^s for τ = 2^(4s+17) and s ≥ s0K k: this is the hypothesis of
`WidthK.StLeafCount` with ε = 1/2^s.
Indeed e·τ·bsum τ k ≤ 3·τ·bsum τ k ≤ 2^β, and k·β ≤ 2^s·49·4^s ≤ 2^(3s+17). 

 ### The decay over the levels 

### `lt_two_pow_mul_div_add_one`

 n < 2^s·(⌊n/2^s⌋ + 1). 

### `decay_step`

 Three more units of s: 19 more levels, each of which multiplies by 8963/10000, make up for the
factor 8 that 2^s gains and for the growth of
(s + 2^15)⁶. The margin is small: (8963/10000)^19·8 = 0.99936…. This is why 2^15 stands here in
place of 8: it makes the growth of the sixth power small enough. 

### `decay_aux_step`

 From s to s + 3 in `decay_aux`. 

### `decay_aux`

 8963^(⌊19s/3⌋+700)·2^10·(s + 2^15)⁶·2^s ≤ 10000^(⌊19s/3⌋+700): by induction in steps of 3, from
s = 0, 1, 2. 

### `decay`

 t levels, each of which multiplies by 8963/10000, make up for the factor C·(s + 8)⁶·2^s, for
every C ≤ 2^10. 

 ### K_t is large compared with 2^β 

### `two_pow_betaOf_le_Ktop`

 2^(4β + 10s + 1000) ≤ K_t. 
