---
{
  "module": "ThreeSumApsp/Programs/Sec4/Corollary26/Regime.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Corollary26/Regime.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Corollary26/Regime.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 26: the parameters 21, 1/9 and 60, and the regime N ≥ D^18

Corollary 26 is the case c = 21, θ = 1/9 of the programs with rational parameters, with the
threshold 60 (`ratParams26`): the preprocessing calls that of Theorem 30 with L = 21 m and t = ⌈m/9⌉
if m = ⌈log₄ D⌉ ≥ 60. On the inputs with N ≥ D^18, and for m ≥ 60, the hypotheses of Theorem 30 hold
at these L and t (`hyp30_26`), and its two cost expressions are O(N²/D^{0.063}) and O(D^{0.437})
(`costs26`); both come from `Corollary26.costs`. Then the bound N²/D^{0.063} (`preBound26`) and what
is used about it. `regime26` puts this in the form in which the statements about the programs with
rational parameters ask for it (`CostsWithin`).


 ## The parameters 

### `ratParams26`

 The parameters of Corollary 26 in the program text: "L := 21m and t := ⌈m/9⌉", and the 60 of
"for all m ≥ 60". 

### `ratParams26_L`

 L = 21 m. 

### `ratParams26_t`

 t = ⌈m/9⌉. 

### `ratParams26_m₀`

 The 60 of "for all m ≥ 60": below it the program computes inner products. 

### `par26`

 The parameters of Theorem 30: L = 21 m. 

### `switch26`

 t = ⌈m/9⌉. 

### `parOf_ratParams26`

 At the parameters of Corollary 26, Theorem 30 is used with L = 21 m. 

### `switchOf31_ratParams26`

 At the parameters of Corollary 26, Theorem 30 is used with t = ⌈m/9⌉. 

### `switchOf_ninth`

 The ceiling ⌈m/9⌉ in natural numbers. 

 ## The two cost expressions 

### `preBound26`

 The bound of the preprocessing of Corollary 26. 

### `costs26`

 **The costs of Theorem 30 at the parameters of Corollary 26**, for m ≥ 60. 

### `hyp30_26`

 Proof of Corollary 26: "For m ≥ 60, Theorem 30 thus applies". 

 ## The overheads 

### `N_mul_D_le_preBound26`

 `N D₀ ≤ N²/D₀^{0.063}`, because `D₀^{1.063} ≤ D₀^{18} ≤ N`. 

### `one_le_of_pow_eighteen_le`

 N ≥ 1, because N ≥ D^18. 

### `le_of_pow_eighteen_le`

 N ≥ D, because N ≥ D^18. 

### `one_le_preBound26`

 The bound of the preprocessing is at least 1. 

 ## The regime 

### `regime26`

 **The regime N ≥ D^18.** There is a constant with which, on these inputs, the two bounds of
Corollary 26 dominate the two costs of Theorem 30 at L = 21 m and t = ⌈m/9⌉ for m ≥ 60. 
