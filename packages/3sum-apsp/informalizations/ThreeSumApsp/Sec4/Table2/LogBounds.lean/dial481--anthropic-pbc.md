---
{
  "module": "ThreeSumApsp/Sec4/Table2/LogBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Table2/LogBounds.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Table2/LogBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The numerical toolkit for Table 2

Table 2 and the proof of Corollary 26 evaluate the exponents `q(θ)` and `γ = θ ln(1/ρ_c)/ln 4` of
Corollary 31 and the bound `R_c(γ)` of (11) at rational points. All three are built from logarithms
of rational numbers. This file turns each such claim into inequalities between rational numbers,
which the tactic `numerics` checks by evaluating both sides.

* `log_mem` encloses `log θ`: write `θ = 2^k (1 + x)/(1 - x)` with `2^k` near `θ`, and sum `n` terms
  of `log ((1 + x)/(1 - x)) = 2 (x + x³/3 + x⁵/5 + ⋯)`.
* `qOf_le` and `le_qOf` bound `q(θ)` at a rational `θ`.
* `gammaOf_one_mem`, `lnΛ_zero_mem`, `lt_Rc_of_lnΛ_zero_mem` and `Rc_lt_of_lnΛ_zero_mem` treat the
  two numbers on which a row of the table depends: `ln(1/ρ_c)/ln 4` and the denominator of (11) at
  `γ = 0`.
* `Table2Query.intro`, `Table2Ninth.intro` and `Table2Density.intro` give an entry of the table from
  two rational numbers that enclose its `θ`; the `θ` itself comes from the intermediate value
  theorem.


 ## Logarithms of rational numbers 

### `logTwoLo`

 Mathlib's lower bound on `ln 2 = 0.693147180559…`. 

### `logTwoHi`

 Mathlib's upper bound on `ln 2 = 0.693147180559…`. 

### `logThreeLo`

 A lower bound on `ln 3 = 1.098612288668…`. 

### `logThreeHi`

 An upper bound on `ln 3 = 1.098612288668…`. 

### `logTenLo`

 A lower bound on `ln 10 = 2.302585092994…`. 

### `logTenHi`

 An upper bound on `ln 10 = 2.302585092994…`. 

### `seriesArg`

 The `x` with `θ = 2^k (1 + x)/(1 - x)`. It is small when `2^k` is near `θ`. 

### `logApprox`

 The approximation `k ln 2 + 2 (x + x³/3 + ⋯)` of `log θ`, with `n` terms of the series at
`x = seriesArg k θ`, and with the midpoint of the two bounds in place of `ln 2`. 

### `logErr`

 A bound on the error of `logApprox`: `|k|` times half the distance of the two bounds on `ln 2`,
and the remainder of the series. 

### `numerics`

 Proves an equation or inequality between explicit rational numbers by evaluating both sides,
after unfolding the approximations of logarithms. 

### `log_mem`

 The enclosure of `log θ`, between two rational numbers if `θ` is rational. It holds for every
`k` and `n`; they decide only how tight it is. 

 ## The exponent `q` of the query time (Corollary 31) 

### `qOf_eq_div`

 `q(θ)` written out in terms of `log 2` and `log 3`. 

### `qOf_le`

 An upper bound on `q(θ)` at a rational `θ`. The hypothesis `h` is `H(θ) + θ ln 9 ≤ r ln 4` with
every logarithm replaced by the bound that makes the inequality harder. Here `2^k` is the power of
two nearest to `θ`; four terms of the series for `log θ` and for `log (1 - θ)` are enough for every
entry of Table 2. 

### `le_qOf`

 A lower bound on `q(θ)` at a rational `θ`, computed as in `qOf_le`. 

 ## The exponent `γ` (Corollary 31) 

### `gammaOf_one_mem`

 Bounds on `γ` at `θ = 1`, that is on `ln(1/ρ_c)/ln 4`, from bounds on `ln(1/ρ_c)`. 

### `gammaOf_mem`

 `γ` at a `θ` between `θlo` and `θhi`, from bounds on `γ` at `θ = 1`. 

 ## The bound `R_c(γ)` (equation (11)) 

### `lnΛ_zero_mem`

 Bounds on the denominator of (11) at `γ = 0` from bounds on `log (1/c)` and `log (1 - 1/c)`. 

### `lt_Rc_of_lnΛ_zero_mem`

 `ε < R_c(γ)` for all `0 ≤ γ ≤ Γ`, from an upper bound on the denominator of (11) at `γ = 0`. 

### `Rc_lt_of_lnΛ_zero_mem`

 `R_c(γ) < r` for all `γ ≥ γlo ≥ 0`, from a lower bound on the denominator of (11) at `γ = 0`. 

 ## Entries of Table 2

An entry needs two facts on its row, `hg` (an enclosure of `ln(1/ρ_c)/ln 4`) and `hR` (the `ε` of
the row is below `R_c(γ)` up to the largest `γ` of the row), and two rational numbers `θlo ≤ θhi`
that enclose its `θ`. 

### `entry_of_mem`

 What all entries have in common: if `θ` lies between `θlo` and `θhi` then the printed `γ₀` is
`γ` rounded down to four decimals, and `ε < R_c(γ)`. 

### `exists_qOf_eq`

 If `q(θlo) ≤ q ≤ q(θhi)` then `q(θ) = q` for some `θ` between `θlo` and `θhi`. 

### `Table2Query.intro`

 An entry of the left half of Table 2, from an enclosure of the `θ` of its column. 

### `Table2Ninth.intro`

 An entry of the column `q = 0.43` of Table 2, which uses `θ = 1/9`. 

### `Table2Density.intro`

 An entry of the right half of Table 2: `γ + q` is at most `κ` at `θlo` (`hqlo`) and at least `κ`
at `θhi` (`hqhi`), so it equals `κ` in between. 

### `exists_Rc_lt`

 At the `θ` of a column of the left half, `R_c(γ) < r`. With `r = ε + 0.001` this shows that the
`ε` of a row is the smallest `R_c(γ)` of the row rounded down to three decimals (Section 4.4). 
