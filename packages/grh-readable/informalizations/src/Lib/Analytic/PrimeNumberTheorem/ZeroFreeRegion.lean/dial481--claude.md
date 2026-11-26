---
{
  "module": "src/Lib/Analytic/PrimeNumberTheorem/ZeroFreeRegion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/ZeroFreeRegion.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/ZeroFreeRegion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A zero-free region for Dirichlet L-functions

For a Dirichlet character `χ` and large `l`, the function `L(s, χ)` has no zero with
`re s ≥ 1 - l⁻²⁵` and `|s| ≤ e^l`, and its logarithmic derivative, with the pole removed, is at most
`2 l²⁵` there. The inequality `|L(σ, 1)³ L(σ + i t, χ)⁴ L(σ + 2 i t, χ²)| ≥ 1` bounds `L` from below
to the right of `re s = 1`, and the bound for the derivative carries this across the line. If `χ²`
is principal, the points near `1` are treated by `𝖿_χ(1) ≠ 0` and continuity; so how large `l` must
be depends on `χ`.

Notions from other files:
* `entireL χ`: the entire function `L(s, χ)`, or `(s - 1) L(s, χ)` if `χ` is principal;
* `regularL χ`, written `𝖿_χ` in comments: `entireL χ`, divided by `s` if `χ` is principal.

## Relation to the literature

Known result: the classical zero-free region, in the crude form with a power of the logarithm that
the 3-4-1 inequality gives directly. Source: Montgomery and Vaughan, Multiplicative Number Theory I,
2007, ch. 11.


### `eventually_le_norm_regularL`

 For all sufficiently small real `r`, the regularized L-function `regularL χ` (`L(s, χ)`, times
`(s - 1) / s` if `χ` is principal) has absolute value at least `r` within distance `r` of `1`. 

### `pow_three_le_mul_norm_regularL_pow`

 A lower bound from the 3-4-1 inequality. Let `l ≥ 10¹⁰`, `N ≤ e^l` and `0 < η ≤ 1`, and write
`𝖿_χ` for `regularL χ`, that is `L(s, χ)`, times `(s - 1) / s` if `χ` is principal. Then
`η³ ≤ 256 l⁷ |𝖿_χ(s)|⁴` for `re s ≥ 1 + η` and `|s| ≤ 3 e^l / 2`, if `χ²` is not principal or
`|s - 1| ≥ 1 / l`. 

### `div_pow_le_norm_regularL`

 Let `l ≥ 10¹⁰` and `N ≤ e^l`; if `χ²` is principal, let `|𝖿_χ| ≥ 1 / l` within `1 / l` of `1`,
where `𝖿_χ = regularL χ` is `L(s, χ)`, times `(s - 1) / s` if `χ` is principal.
Then `|𝖿_χ(s)| ≥ 12 / l²²` for `re s ≥ 1 + l⁻²⁵` and `|s| ≤ 3 e^l / 2`. 

### `norm_logDeriv_regularL_le`

 Let `l ≥ 10¹⁰` and `N ≤ e^l`; if `χ²` is principal, let `|𝖿_χ| ≥ 1 / l` within `1 / l` of `1`,
where `𝖿_χ = regularL χ` is `L(s, χ)`, times `(s - 1) / s` if `χ` is principal.
Then `𝖿_χ(s) ≠ 0` and `|𝖿_χ'(s) / 𝖿_χ(s)| ≤ l²⁵` for `re s ≥ 1 - l⁻²⁵` and `|s| ≤ e^l`. 

### `norm_logDeriv_entireL_le`

 Let `χ` be a Dirichlet character mod `N ≥ 1`, `l ≥ 10¹⁰` and `N ≤ e^l`. If `χ²` is principal,
assume `|regularL χ z| ≥ 1 / l` whenever `|z - 1| ≤ 1 / l`, where `regularL χ` is `L(s, χ)` times
`(s - 1) / s` if `χ` is principal and `L(s, χ)` otherwise. Then for `re s ≥ 1 - l⁻²⁵` and
`|s| ≤ e^l`, the entire function `entireL χ` (equal to `L(s, χ)`, or to the continuation of
`(s - 1) L(s, χ)` if `χ` is principal) does not vanish at `s`, and its logarithmic derivative there
has norm at most `2 l²⁵`. 

### `eventually_norm_logDeriv_entireL_le`

 **Zero-free region** for a fixed character: for all large `l`, on `re s ≥ 1 - l⁻²⁵`,
`|s| ≤ e^l` the function `entireL χ` (`L(s, χ)` with the pole removed) does not vanish and its
logarithmic derivative is at most `2 l²⁵`. 
