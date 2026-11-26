---
{
  "module": "ThreeSumApsp/Sec4/Corollary31/Limit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Corollary31/Limit.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Corollary31/Limit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 31: the limit `ε*`; the choice of `c` and `θ` in the proof of Theorem 24

The bound `R_c(γ) = ln 4/ln Λ` of equation (11) increases to `ε* = ln 4/(5 ln 10) = 0.1204…` as `c`
decreases to 10 and `γ` to 0.

* The limit. The paper's "direct calculation" is done here with the derivative of `ln Λ` with
  respect to `c`, which is positive (`hasDerivAt_lnΛ`, `deriv_lnΛ_pos`), so `R_c(γ)` decreases in
  `c` (`sec4_Rc_strictAntiOn`); at `c = 10`, `γ = 0` the identity `H(1/10) + (9/10) ln 9 = ln 10`
  gives `ln Λ = 5 ln 10` (`lnΛ_ten_zero`, `tendsto_lnΛ`). Hence `sec4_Rc_zero_tendsto`,
  `sec4_Rc_lt_epsStar`, and the value `sec4_epsStar_numeric`.
* The proof of Theorem 24. Given `ε < ε*` and `q > 0`, first `c` and then `θ` are chosen by
  continuity (`exists_admissible`).


 ### The limit `ε*` 

### `entropy_sub_mul_deriv`

 `H(x) - x H'(x) = -ln(1-x)` for `0 < x < 1`, with `H'(x) = ln((1-x)/x)` (see
`hasDerivAt_entropy`). 

### `hasDerivAt_mul_entropy_inv`

 The derivative of `c H(1/c)` with respect to `c` is `H(1/c) - (1/c) H'(1/c) = ln(c/(c-1))`. 

### `hasDerivAt_lnΛ`

 The derivative of `ln Λ` with respect to `c` is `ln(10/3) - (1/2) ln(c/(c-1))`, for `c > 1` and
every `γ`. 

### `deriv_lnΛ_pos`

 The derivative of `ln Λ` with respect to `c` is positive for `c ≥ 10`, because
`c/(c-1) ≤ 10/9 < (10/3)²`. 

### `entropy_one_tenth`

 Proof of Corollary 31: "the identity H(1/10) + (9/10) ln 9 = ln 10". 

### `lnΛ_ten_zero`

 At `c = 10` and `γ = 0`, `ln Λ = 10 ln 10 - 5 H(1/10) - 9 ln 3 = 5 ln 10`. 

### `lnΛ_strictMonoOn`

 Proof of Corollary 31: "ln Λ increases with c", on `[10, ∞)` and for every `γ`, since its
derivative is positive. 

### `log_ten_pos`

 `ln 10 > 0`. 

### `lnΛ_ge`

 For `c ≥ 10`, `ln Λ ≥ 5 ln 10 + γ ln 4`, its value at `c = 10`. 

### `sec4_Rc_strictAntiOn`

 Corollary 31: "R_c(0) increases [...] as c decreases to 10": the monotonicity.  It holds for
every fixed `γ ≥ 0`; the paper says it for `γ = 0` ("for γ = 0, ln Λ increases with c", proof of
Corollary 31). 

### `tendsto_lnΛ`

 Proof of Corollary 31: "for γ = 0, ln Λ [...] tends to 5 ln 10 as c decreases to 10, by the
identity H(1/10) + (9/10) ln 9 = ln 10". The limit is the value at `c = 10` (`lnΛ_ten_zero`). 

### `sec4_Rc_zero_tendsto`

 Corollary 31: "Moreover, R_c(0) increases to ε* = ln 4/(5 ln 10) = 0.1204… as c decreases to
10": the limit. (The monotonicity is `sec4_Rc_strictAntiOn` at `γ = 0`.) 

### `sec4_epsStar_numeric`

 Section 4.1: "Let ε* := ln 4/(5 ln 10) = 0.1204…". 

### `sec4_Rc_lt_epsStar`

 Table 1, row `ε`: "R_c(γ) < 0.1204…", that is `R_c(γ) < ε*`, for `c > 10` and
`γ ≥ 0`. 

 ### The choice of `c` and `θ` in the proof of Theorem 24 

### `tendsto_qOf_zero`

 Proof of Theorem 24: "as θ → 0, the first expression tends to 0". The first expression is
`q = (H(θ) + θ ln 9)/ln 4`. 

### `tendsto_gammaOf_zero`

 As `θ → 0`, `γ = θ ln(1/ρ_c)/ln 4` tends to 0. 

### `exists_admissible`

 The choice of c and θ in the proof of Theorem 24. The paper: "Let ε < ε* and q > 0. Choose c >
10 with R_c(0) > ε (Corollary 31), and then θ ∈ (0, 0.9) small enough that (H(θ) + θ ln 9)/ln 4 < q
and R_c(θ ln(1/ρ_c)/ln 4) > ε." 
