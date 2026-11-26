---
{
  "module": "src/Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Growth of Dirichlet L-functions near the line `re s = 1`

Let `χ` be a character modulo `N`, and let `𝖿_χ(s)` (`regularL χ s`) be `L(s, χ)`, times
`(s - 1) / s` if `χ` is principal. Partial summation gives `|𝖿_χ(s)| ≤ 1 + 4 N |s|` in
`re s ≥ 1 / 2`, and the three-lines theorem improves this to `|𝖿_χ(s)| ≤ l²` for `re s ≥ 1 - 1 / l`
and `|s| ≤ 3 e^l`, whenever `l ≥ 10¹⁰` and `N ≤ e^l`.

Notions from other files:
* `entireL χ`: the entire function equal to `L(s, χ)` if `χ` is not principal, and to the
  continuation of `(s - 1) L(s, χ)` if it is.

## Relation to the literature

Known result: the bound `L(s, χ) ≪ log (N |s|)` near `re s = 1` and away from the pole. It is proved
here for `𝖿_χ` and with a square in place of the first power. Source: Montgomery and Vaughan,
Multiplicative Number Theory I, 2007, Lemma 10.15.


### `norm_mul_cpow_neg_add_one_le`

 If `|r| ≤ C` on `(1, ∞)`, then the integrand of `∫₁^∞ r(t) t ^ (-s - 1) dt` is dominated by
`C t ^ (-re s - 1)`. 

### `integrableOn_mul_cpow_of_bounded`

 For a bounded measurable `r`, the integral `∫₁^∞ r(t) t ^ (-s - 1) dt` converges in
`re s > 0`. 

### `norm_integral_mul_cpow_le`

 If `|r| ≤ C` on `(1, ∞)`, then `|∫₁^∞ r(t) t ^ (-s - 1) dt| ≤ C / re s` for `re s > 0`. 

### `differentiableAt_integral_mul_cpow`

 For a bounded measurable `r`, the integral `∫₁^∞ r(t) t ^ (-s - 1) dt` is holomorphic in
`re s > 0`. 

### `charMean`

 The mean value of a Dirichlet character over the classes modulo `N`. 

### `norm_charMean_le_one`

 The mean value of a Dirichlet character has absolute value at most `1`. 

### `charMean_eq_zero`

 The mean value of a nonprincipal Dirichlet character is `0`. 

### `sum_range_char_add`

 A sum of `χ` over `N` consecutive integers is `N` times the mean value `charMean χ` of `χ`,
that is, the sum over all classes modulo `N`. 

### `norm_sum_char_sub_le`

 The sum of the values of `χ` up to `x` differs from `x` times the mean value `charMean χ` by at
most `2 N`. 

### `norm_LSeries_char_le`

 If `re s ≥ 1 + 1 / A` with `A > 0`, then `|L(s, χ)| ≤ 1 + A`, since the Dirichlet series of
`χ` is dominated by `ζ(re s)`. 

### `regularL`

 `𝖿_χ(s)` is `L(s, χ)`, times `(s - 1) / s` if `χ` is principal. The entire function `entireL χ`
has the factor `s - 1` in that case; dividing by `s` keeps the size of `L(s, χ)` for large `|s|`. 

### `differentiableAt_regularL`

 `𝖿_χ` (`regularL χ`: `L(s, χ)`, times `(s - 1) / s` if `χ` is principal) is holomorphic in
`re s > 0`. 

### `regularL_eq`

 In `re s > 1` the regularised function `𝖿_χ` (`regularL χ`) is `L(s, χ) (s - δ) / s`, with
`δ = 1` if `χ` is principal and `δ = 0` otherwise. 

### `norm_sub_ite_le`

 `|s - δ| ≤ |s|` in `re s ≥ 1 / 2`, where `δ` is `1` or `0` as the proposition `p` holds or
not (in the uses, `p` says that a character is principal). 

### `norm_regularL_le_linear`

 Partial summation: `|𝖿_χ(s)| ≤ 1 + 4 N |s|` in `re s ≥ 1 / 2`, where `𝖿_χ` (`regularL χ`) is
`L(s, χ)`, times `(s - 1) / s` if `χ` is principal, and `N` is the modulus of `χ`. 

### `norm_LSeries_le_mul_norm_regularL`

 For `l ≥ 1` and `re s > 1`, at distance at least `1 / l` from `1` if `χ` is principal, we have
`|L(s, χ)| ≤ 2 l |𝖿_χ(s)|`, where `𝖿_χ` (`regularL χ`) is `L(s, χ)`, times `(s - 1) / s` if `χ` is
principal. 

### `norm_regularL_le_sq`

 If `l ≥ 10¹⁰` and the modulus `N` is at most `e^l`, then `|𝖿_χ(s)| ≤ l²` for
`re s ≥ 1 - 1 / l` and `|s| ≤ 3 e^l`. Here `𝖿_χ` (`regularL χ`) is `L(s, χ)`, times
`(s - 1) / s` if `χ` is principal. 

### `norm_deriv_regularL_le`

 Cauchy's estimate: if `l ≥ 10¹⁰` and the modulus `N` is at most `e^l`, then `|𝖿_χ'(s)| ≤ 2 l³`
for `re s ≥ 1 - 1 / (2 l)` and `|s| ≤ 2 e^l`. Here `𝖿_χ` (`regularL χ`) is `L(s, χ)`, times
`(s - 1) / s` if `χ` is principal. 
