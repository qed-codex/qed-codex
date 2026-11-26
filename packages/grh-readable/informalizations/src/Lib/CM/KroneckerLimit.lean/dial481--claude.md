---
{
  "module": "src/Lib/CM/KroneckerLimit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/KroneckerLimit.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/KroneckerLimit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Kronecker's first limit formula

`New.kronecker_limit` computes the first two terms at `s = 1` of the Epstein zeta function of a
lattice in `ℂ`, in terms of its area and of the discriminant `g₂³ - 27 g₃²`. The Epstein function is
not continued analytically: only real `s` with `1 < s < 2` occur, and a right derivative at `1`.

For the lattice `ℤ τ + ℤ`, each row `∑ n, |m τ + n|^(-2s)` with `m ≥ 1` is compared with the
integral `∫ |m τ + t|^(-2s) dt` (`New.hasSum_shiftedTerm`). The errors `New.meanError` sum to a
function continuous on `[1, 2]`, the integrals to a multiple of `ζ(2s - 1)`, which has a simple pole
at 1. At `s = 1` the cotangent series expresses the errors through `log |∏ (1 - q ^ n)|`
(`New.tsum_meanError_one`).

Notions from other files:
* `PeriodPair.area`: The area |Im(ω̄₁ω₂)| of the fundamental parallelogram spanned by the periods
  ω₁, ω₂ of a period pair.

## Relation to the literature

Known result: Kronecker's first limit formula. Here the real limit from the right is proved for any
lattice and stated with the discriminant. Rows are compared with integrals by the mean value
theorem. Source: C. L. Siegel, Lectures on Advanced Analytic Number Theory (1961), Chapter I,
Theorem 1; for a proof of this shape, F. Chamizo, A simple evaluation of a theta value, the
Kronecker limit formula and a formula of Ramanujan, Ramanujan J. (2022), Prop. 3.1.


### `New.hasSum_pnat_rpow_neg`

 The series `∑ m^(-s)` for real `s > 1`, in terms of the entire function `riemannZeta₀`, which is
`ζ(s) - 1 / (s - 1)` for `s ≠ 1`. 

### `New.norm_rpow_sub_rpow_le`

 For `a > 2`, `|a - b| ≤ 1` and `1 ≤ s ≤ 2`, the values of `t ↦ t^(-2s)` at `a` and `b` differ
by at most `4 (a / 2)^(-3)`, by the mean value theorem. 

### `New.betaFactor`

 The factor `√π Γ(s - 1/2) / Γ(s) * y^(1 - 2s)`. For `s > 1/2` it is the value of Euler's beta
integral `∫ |z + t|^(-2s) dt` over the real line when `im z = y > 0`. 

### `New.hasDerivAt_betaFactor`

 The derivative at `s = 1` of the value `√π Γ(s - 1/2) / Γ(s) * y^(1 - 2s)` of Euler's beta
integral; the Euler constants from `Γ'(1/2)` and `Γ'(1)` cancel. 

### `New.norm_eta_q_lt_one`

 The powers `q^(j+1)` of `q = exp (2 π i (x + i y))` have modulus less than one for `y > 0`. 

### `New.tprod_one_sub_eta_q`

 For `y > 0` and `q = exp (2 π i (x + i y))`, so that `eta_q m ⟨x, y⟩ = q^(m+1)`, the double
series `∑ q^((m+1)(j+1)) / (m+1)` converges absolutely, and it is minus a logarithm of
`∏ (1 - q^(j+1))`. 

### `New.summable_norm_mul_add_rpow`

 For `τ = x + i y` with `y > 0`, the series `∑ |m τ + n| ^ r` over `(m, n) ∈ ℤ²` converges for
`r < -2`; its term at `(0, 0)` is `0` in Lean. 

### `New.shiftedTerm`

 The term `|m τ + n + u|^(-2s)`, for `τ = x + i y`, `p = (m, n)` and a real shift `u`. 

### `New.meanError`

 The term `|m τ + n|^(-2s)` minus the mean of `|m τ + n + u|^(-2s)` over `u ∈ [0, 1]`, for
`τ = x + i y` and `p = (m, n)`. 

### `New.tendstoUniformlyOn_sum_meanError`

 The series of the errors `meanError x y p s` converges uniformly for `s ∈ [1, 2]`. 

### `New.integral_shiftedTerm`

 Euler's beta integral along the row `m`: `∫ |m τ + t|^(-2s) dt` over the real line, where
`τ = x + i y`; it equals `betaFactor y s * m ^ (1 - 2s)`. 

### `New.hasSum_shiftedTerm`

 The row `∑ n, |m τ + n|^(-2s)` (for `τ = x + i y`) is the sum of its errors
`meanError x y (m, n) s` plus the beta integral `betaFactor y s * m ^ (1 - 2s)`. 

### `New.tsum_meanError_row_one`

 Let `τ = x + i y` with `y > 0`, and fix the row `m + 1`. The errors `meanError x y (m + 1, n) 1`
are `|(m+1) τ + n|^(-2)` minus the mean of `|(m+1) τ + n + u|^(-2)` over `u ∈ [0, 1]`. Their sum
over `n : ℤ` is `2 π / y` times the real part of `∑ j, q^((m+1)(j+1)) / (m+1)`, where
`q = exp (2 π i τ)`, so that `eta_q m τ = q^(m+1)`. 

### `New.tsum_meanError_one`

 At `s = 1` the errors sum to `-2 π / y * log |∏ (1 - q^(j+1))|`, `q = exp (2 π i τ)`,
`τ = x + i y`; the errors are `meanError x y p 1` summed over `p : ℕ+ × ℤ`. 

### `New.regularPart`

 The part of `∑ |m τ + n|^(-2s)`, `τ = x + i y`, without a pole at `s = 1`. For `1 < s < 2` it
is the sum minus `betaFactor y s / (s - 1)` (`New.sub_one_mul_tsum_norm_mul_add_rpow`). 

### `New.continuousWithinAt_regularPart`

 The regular part of the sum is continuous from the right at `s = 1`. 

### `New.sub_one_mul_tsum_norm_mul_add_rpow`

 Let `τ = x + iy` with `y > 0`, and let `1 < s < 2`. The sum `∑ |m τ + n|^(-2s)` over `ℤ²` is
`regularPart x y s + betaFactor y s / (s - 1)`, where
`betaFactor y s = √π Γ(s - 1/2) / Γ(s) * y^(1 - 2s)` and `regularPart` is the part without a pole at
`s = 1`; the equation is stated multiplied by `s - 1`. 

### `New.kronecker_limit`

 **Kronecker's first limit formula.** Let `L` be a lattice of area `A` and discriminant
`Δ = g₂³ - 27 g₃²`, and let `k > 0`. There is a real function `F` with (a) `F 1 = π k`, (b) right
derivative `F 1 * (2 γ - log (A / (k π²)) - (log |Δ|) / 6)` at `1`, `γ` being Euler's constant, and
(c) `F s = (s - 1) ∑ (|l|² / (k A))^(-s)` for `1 < s < 2`. The sum is over all `l` in the lattice;
the term `l = 0` is `0`, since `0 ^ (-s) = 0` in Lean. For `k = 1` this is the expansion
`∑ (|l|² / A)^(-s) = π / (s - 1) + π (2 γ - log (A |Δ|^(1/6) / π²)) + o(1)` as `s` decreases to
`1`. 
