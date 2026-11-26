---
{
  "module": "ThreeSumApsp/Programs/Sec4/Corollary26/AllInstances.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Corollary26/AllInstances.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Corollary26/AllInstances.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 26, the offline form, on all instances

Corollary 26 is about matrices with N ≥ D^18. A solver that other procedures call has to be right on
every instance. allInstances26(N, D, w, U, x, y, wi, wj, out, fr) tests whether D^18 ≤ N, calls the
offline routine offline32 if so and the brute force if not. The texts are `allInstances26Body` and
`regimeTest26Body`.

* *The routine.* It solves the task `thinTask` on every instance, within the time
  `allInstancesTime26` and the need `allInstancesNeed26` (`allInstances26_solves`). It tests whether
  D^18 ≤ N (`regimeTest26_meets`). In that regime it calls the offline routine of Corollary 26,
  whose demands on the limits are covered by the need (`lim31_of_need`, `offline32_meets_thinTask`);
  outside it calls the brute force.
* *The time in the regime.* For N ≥ D^18 the time is O(w D^{0.437} + N²/D^{0.063}), the bound of
  Corollary 26: the time of the offline routine is at most a constant times tp + w tq for all bounds
  that dominate the two costs of Theorem 30 (`exists_tOffline32_le`), and in the regime the two
  bounds of Corollary 26 do (`regime26`).
* *The need is polynomial in the parameters.* Every summand of the need is a numeral times a product
  of at most 20 factors N + 1, D and U. With Q = (N + 1) (D + 1) (w + 1) (U + 1) each factor is at
  most Q, so each product is at most Q^20 (`le_pow_twenty`). So the largest number, the cells and
  the levels of calls are at most 2^11 Q^20 (`word_le`, `cells_le`, `depth_le`).


 ## Time and need 

### `allInstancesTime26`

 The time of allInstances26, for the parameters N, D, w, U; c is the constant of the shared
stage. 

### `allInstancesNeed26`

 What allInstances26 needs, for the parameters N, D, w, U: the largest number formed, the cells
from the free pointer on, the levels of calls. With B = (N + 1)^5, which bounds 10^L in the regime
(`below`). 

 ## The test 

### `regimeTest26_ends`

 regimeTest26(N, D) returns 1 if D^18 ≤ N and 0 if not, and changes no cell. 

### `regimeTest26_meets`

 The procedure regimeTest26 returns 1 if D^18 ≤ N and 0 if not, and changes no cell. 

 ## The limits 

### `fits_of_need`

 A number that is at most the first part of the need fits in a word. 

### `top_le_of_need`

 The block of Theorem 30, behind the two padded matrices, ends within the cells of the need. 

### `lim30_of_below`

 If B bounds 10^L, 7^L and 10^m, the three numbers in the limits of Theorem 30 are at most B³ U²,
7 B U and 10 B. 

### `lim31_of_need`

 In the regime, the need of allInstances26 covers what offline32 asks of the limits. 

 ## The matrices of an instance 

### `thinMX`

 The first matrix of an instance. 

### `thinMY`

 The second matrix of an instance. 

### `entryN_thin`

 The entry of the product of the two matrices is the entry that the task asks for. 

 ## The routine 

### `map_entryN_thin`

 The answers of the offline routine are those that the task asks for. 

### `offline32_meets_thinTask`

 **In the regime** the offline routine solves the task. 

### `allInstances26_solves`

 **allInstances26 solves the task on all instances**, in every program that holds allInstances26,
regimeTest26 and the brute force at their numbers and in which offline32 satisfies `OfflineSpec32`
at the parameters of Corollary 26, also after more procedures are appended. 

 ## The time in the regime 

### `allInstancesTime26_le`

 **The time of allInstances26 in the regime is within the bound of Corollary 26.** 

 ## The need is polynomial in the parameters 

### `word_le`

 The largest number that allInstances26 forms. 

### `cells_le`

 The cells that allInstances26 uses. 

### `depth_le`

 The levels of calls that allInstances26 needs. 

### `le_prod_four`

 Three of four positive factors are at most the product. 

### `allInstancesNeed26_poly`

 The need is polynomial in the parameters. 
