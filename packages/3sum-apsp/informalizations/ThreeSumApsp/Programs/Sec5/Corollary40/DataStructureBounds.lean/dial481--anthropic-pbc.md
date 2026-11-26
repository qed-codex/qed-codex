---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary40/DataStructureBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/DataStructureBounds.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/DataStructureBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Time, space and limits of the relocatable data structure

The programs for Corollary 40 call the preprocessing and the query routine of a data structure for
the entries of a thin matrix product, placed at an address fr of their choice.  `KitRates` collects
what they use about it: bounds on the two running times and on the number of cells, and limits
within which the routines run for matrices of zeros and ones.  The limits are a function of the
number sp of memory cells and serve every structure that lies within the memory, so that several
structures can lie side by side.  `kit31_rates` proves this for all parameters and all bounds that
dominate the two costs of Theorem 30; `kitRates_corollary26` (Corollary 26) and
`kitRates_corollary31` (Corollary 31) are its instances.


 ## The bounds on the two running times 

### `preBound26_le_sq`

 The bound on the preprocessing of Corollary 26 is at most `N²`. 

### `exists_preBound31_le_sq`

 `(log D + 1)²/D^γ` is bounded, so the bound on the preprocessing is `O(N²)`. 

### `one_le_rpow_mul_preBound31`

 For D ≤ F the bound on the preprocessing is at least 1/F^γ. 

### `one_le_queryBound31`

 The bound on a query is at least 1. 

 ## The limits 

### `kitInputEnd`

 The first cell after an input with no wanted positions: three sizes and the two matrices. 

### `baseLim`

 The limits of Section 4 for a structure that lies directly after such an input, for matrices of
zeros and ones. 

### `limKit31`

 Limits for the routines with general parameters on matrices of zeros and ones, with `sp` cells
of memory.  Only the number of cells depends on the place of a structure.  So the bound on the words
and the depth are those of `baseLim`, with `sp` more for the addresses and 20 more levels of calls
for the procedures that call the routines. 

### `limKit31_ok`

 **One set of limits for all places**: the limits serve every structure that ends within the
memory. 

### `small_limKit31`

 The limits are polynomial in `n` if the memory is, for `D₀ ≤ N ≤ n`. 

 ## What the programs use about a kit 

### `KitRates`

 **What the programs of Corollary 40 use about a kit** at the sizes N and D: the preprocessing
takes at most C tp steps and a query at most C tq; a structure has at most A N² cells; the limits
limK sp, for a memory of sp cells, serve every place within the memory, allow 22 levels of calls
more than the preprocessing needs, and are polynomial in n ≥ N if sp is. 

### `KitRates.small`

 The degree 40 is twice the degree 20 of the limits of Section 4, which are polynomial in N and
  D (`polyBound_pair_le`). 

### `KitRates.mono`

 Two bounds can be replaced by bounds that are at least 1/E times as large; the factor E goes
into the constant. 

### `KitRates.mul_tPre_le`

 x preprocessings take at most C E X steps if x tp ≤ E X. 

### `KitRates.mul_tQ_le`

 x queries take at most C E X steps if x tq ≤ E X. 

### `KitRates.lim_at`

 The limits for a memory that ends after one structure at fr: they serve this structure, every
address fits in a word, and 22 levels of calls are left. 

 ## The data structure of Section 4 as a kit 

### `kit31_rates`

 **The rates of the data structure with the parameters G**, for all bounds tp, tq ≥ 1 that
dominate the two costs of Theorem 30 from the threshold on, with tp = O(N²). 

### `kitRates_corollary26`

 **Corollary 26's data structure as a kit**: for N ≥ D^18 the preprocessing takes O(N²/D^{0.063})
steps and a query O(D^{0.437}). 

### `kitRates_corollary31`

 **The data structure with general parameters as a kit** (Corollary 31), for admissible c, θ, ε,
with γ = γ(c, θ) and q = q(θ): for 1 ≤ D ≤ N^ε the preprocessing takes O(N² (log D + 1)²/D^γ) steps
and a query O(D^q (log D + 1)).  The threshold m₀ ≥ M is as large as one likes, and D ≤ N^ε is asked
only above the threshold: below it D ≤ 4^{m₀}, and the constant takes care of it. 
