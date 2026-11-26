---
{
  "module": "ThreeSumApsp/Sec4/Corollary31/RationalParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Corollary31/RationalParameters.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Corollary31/RationalParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Rational parameters for Corollary 31

Corollary 31 has real parameters `c > 10` and `0 < θ < 0.9`, and a real `ε < R_c(γ)` with
`γ = θ ln(1/ρ_c)/ln 4`. A program can only contain rational numbers. This file shows that the
parameters can be replaced by rational ones without loss (`exists_rat_params`): first a rational
`c' > c` so close to `c` that `ε` is still below `R_{c'}(γ)`, by continuity (`continuousAt_Rc`);
then a rational `θ' < θ` so close to `θ` that the exponent `γ` of `c'` and `θ'` is still at least
that of `c` and `θ`. A smaller `θ` makes `q` smaller and `R_{c'}(γ)` larger. The file also writes
the numbers `⌈c m⌉` and `⌈θ m⌉` for rational parameters in integer arithmetic (`levelsOf_div`,
`switchOf_div`).


### `exists_nat_div_btwn`

 Between two real numbers, the smaller of which is not negative, lies a quotient of two natural
numbers. 

### `continuousAt_Rc`

 With `θ` fixed, `R_c(γ)` is continuous in `c`. 

### `RatApprox`

 The rational numbers `a/b` and `p/q` can take the place of the parameters `c` and `θ` of
Corollary 31, for the same `ε`. 

### `RatApprox.ratio_gt`

 `a/b > 10`, in the natural numbers. 

### `RatApprox.p_pos`

 `p/q > 0`, in the natural numbers. 

### `RatApprox.switch_lt`

 `p/q < 0.9`, in the natural numbers. 

### `RatApprox.admissible`

 The hypotheses of Corollary 31 hold for `a/b`, `p/q` and `ε`. 

### `RatApprox.gamma_le`

 The exponent `γ` does not get smaller. 

### `RatApprox.qOf_le`

 The exponent `q` does not get larger. 

### `exists_rat_ratio`

 A rational `c' = a/b` above `c` for which `ε` is still below `R_{c'}(γ)`, at the same `θ`. 

### `exists_rat_params`

 **Rational parameters suffice.** For `c`, `θ`, `ε` as in Corollary 31 there are rational numbers
`c' = a/b > c` and `θ' = p/q < θ` that satisfy the hypotheses of the corollary with the same `ε`,
and whose exponents are no worse: `γ(c', θ') ≥ γ(c, θ)` and `q(θ') ≤ q(θ)`. 

### `levelsOf_div`

 `L = ⌈c m⌉` for a rational `c = a/b`. 

### `switchOf_div`

 `t = ⌈θ m⌉` for a rational `θ = p/q`. 
