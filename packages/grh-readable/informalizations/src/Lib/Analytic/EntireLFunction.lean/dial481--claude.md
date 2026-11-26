---
{
  "module": "src/Lib/Analytic/EntireLFunction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/EntireLFunction.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/EntireLFunction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Quadratic twists, polar functions and logarithmic derivatives of Dirichlet L-functions

This part shows that the twist of a Dirichlet character by the Legendre symbol of an odd prime not
dividing the modulus is not principal. It defines `New.IsPolar`, the condition that a Laplace-type
transform of an error term continues meromorphically with at most simple poles in the right
half-plane. It also expresses `∑ χ(n) Λ(n) n^{-s}` through the logarithmic derivative of
`New.entireL χ` and identifies the residues of that logarithmic derivative with the orders of the
zeros of `New.entireL χ`.

## Main definitions and results

* `New.quadTwist_ne_one`: the twist of a character modulo `N` by the Legendre symbol `(·/d)`, for an
  odd prime `d` prime to `N`, is not principal.
* `New.IsPolar`: `E` is measurable, `|E v| ≤ C e^v` for `v ≥ 0`, and `∫₀^∞ E(v) e^{(1-s)v} dv`
  continues to a meromorphic function of `s` with at most simple poles of residue `r ρ` in
  `re ρ > 0`.
* `New.LSeriesHasSum_mul_vonMangoldt`: `∑ χ(n) Λ(n) n^{-s}` in terms of the logarithmic derivative
  of `New.entireL χ`.
* `New.tendsto_sub_mul_logDeriv_entireL_analyticOrderNatAt`: the residues of that logarithmic
  derivative are the orders of the zeros of `New.entireL χ`.

Notions from other files:
* `New.entireL`: The entire function equal to L(s, χ) if χ is not principal, and to the continuation
  of (s − 1)L(s, χ) if χ is principal.

## Relation to the literature

Known; see `Lib.Analytic.Landau` for sources.


 ### The quadratic twist of a character 

### `quadTwist_apply`

 The twist of `χ` by the Legendre symbol takes the value `χ(n) (n/d)` at an integer `n`. 

### `quadTwist_ne_one`

 For a Dirichlet character `χ` mod `N` and an odd prime `d` coprime to `N`, the twist of `χ` by
the Legendre symbol `(·/d)`, a character mod `N * d`, is not principal. 

 ### Polar functions and Laplace integrals 

### `IsPolar`

 `E` is measurable, `|E v| ≤ C e^v` for all `v ≥ 0`, and its transform
`∫₀^∞ E(v) e^{(1-s)v} dv` continues from `re s > 2` to a meromorphic function on `ℂ` whose poles in
`re s > 0` are at most simple; for `re ρ > 0`, `r ρ` is the residue at `ρ`, and `0` where there is
no pole. For `E(v) = R(e^v)` the transform is `∫₁^∞ R(y) y^{-s} dy`. 

### `integrableOn_laplace_of_abs_le`

 If `E` is measurable and `|E v| ≤ C e^v` for `v ≥ 0`, the transform
`∫₀^∞ E(v) e^{(1-s)v} dv` converges for `re s > 2`. 

### `laplace_pow`

 For `re s > 0`, the Laplace transform of `t ^ k` at `s` is `k! / s ^ (k + 1)`. 

 ### The logarithmic derivative of a Dirichlet L-function 

### `entireL_ne_zero`

 `entireL χ` has no zero in `re s ≥ 1`. 

### `LSeriesHasSum_mul_vonMangoldt`

 For `re s > 1`, the series `∑ χ(n) Λ(n) n^{-s}` has the sum `-L'/L(s, χ)`, written through
`entireL χ`, which is `L(s, χ)`, or `(s - 1) L(s, χ)` for principal `χ`. The term `1 / (s - 1)` is
present only for `χ = 1`. 

### `tendsto_sub_mul_of_continuousAt`

 A function continuous at `s` has residue zero there. 

### `tendsto_sub_mul_logDeriv_entireL_analyticOrderNatAt`

 The logarithmic derivative of `entireL χ`, which is `L(s, χ)`, or `(s - 1) L(s, χ)` for
principal `χ`, has at most a simple pole at `s`. Its residue is the order of vanishing of
`entireL χ` at `s`. 
