---
{
  "module": "proof/rates/PaddedDescent/Params.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Params.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Params.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The parameters of this folder's algorithm for 3-SAT (definitions only)

This file defines the numbers that the single algorithm for 3-SAT computes from the number of
variables `n`. It proves nothing beyond the two
defining equations of `kseq`. In the recursion of this folder one level takes K_j nodes to
(K_j·L_j)² nodes with a small factor L_j, where the paper's
recursion of Section 5 takes K nodes to g² = 9K¹⁶ nodes with g = 3K⁸. These numbers are also not
those of Theorem A in Appendix A. 

### `Dcol`

 The colouring of a network on g nodes with K colours is allowed the relative error 1/Dcol. 

### `kseq`

 The logarithm of the number of nodes at level `j`: k₀ = 8 and k_{j+1} = 2·(k_j + 47 + j). 

### `kseq_zero`

 k₀ = 8. 

### `kseq_succ`

 k_{j+1} = 2·(k_j + 47 + j). 

### `Kseq`

 The number of nodes at level `j`: K_j = 2^(k_j), so K₀ = 256. 

### `Lseq`

 The factor between the number of colours and the side of the grid at level `j`: L_j = 2^(47+j). 

### `gseq`

 The side of the grid at level `j`: g_j = K_j·L_j, so that K_{j+1} = g_j². 

### `sOf`

 The precision that the algorithm picks from the number of variables `n`: the exponent of the
time will be about n / 2^(sOf n).
(Subtraction of natural numbers stops at 0; the product with 3 is taken first, and then the division
by 19 rounds down.) 

### `tauOf`

 The threshold of the sparsification for precision `s`. It does not depend on the width k of the
clauses: for every k it is large enough as soon as s is
large enough (`s0K k` below). 

### `betaOf`

 The marks of the clauses are coded in blocks of 2^(betaOf s) bits. The number 2^(betaOf s) is at
least the number of clauses per variable of a
sparsified formula of width k, as soon as s ≥ `s0K k`: that number is a power of τ whose exponent
depends on k only, and betaOf grows faster than any multiple of s. 

### `layersOf`

 The number of times that the set of clauses of a sparsified formula is divided into a layer and
a rest. 

### `capOf`

 The cap of the cut-off sums: an assignment that satisfies the later layers violates fewer than
capOf n clauses of a layer. 

### `depthOf`

 The number of levels for precision `s`: 19/3 levels for each unit of s (the division rounds
down), and 700 more. 

### `s0K`

 For clauses of width k the parameters above are large enough as soon as the precision s is at
least s0K k. For smaller s the machine uses exhaustive search. 

### `C0K`

 The constant in the exponent of the length of the pad, 2^(C0K k·(⌊n/2^s⌋ + 1)), for width k. It
is so large that the pad suffices for exhaustive search while s < s0K k. 

### `Ktop`

 The number of nodes at the top level for precision `s`. 

### `gtop`

 The number of nodes of the network of a formula, which is rebalanced to K_t nodes at the top:
3·K_t⁸. 

### `Ytop`

 Y = gtop². The overheads for precision `s` are bounded in terms of it
(`PaddedDescent.Threshold`). 
