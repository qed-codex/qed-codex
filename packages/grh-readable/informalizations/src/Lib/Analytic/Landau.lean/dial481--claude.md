---
{
  "module": "src/Lib/Analytic/Landau.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Landau.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Landau.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Landau's lemma

This part proves Landau's lemma: the moment generating function of a measure is not analytic at
its abscissa of convergence. It applies the lemma to transforms satisfying `New.IsPolar`. Assume
a one-sided bound on the error term `E`, and assume that the residues `r x` at real `x > β` have
non-negative real part. Then the part concludes that there is no pole to the right of `β`.
Together with `Lib.Analytic.EntireLFunction`, these are the analytic tools for passing from a
one-sided bound on an error term to the absence of zeros of L-functions.

## Main definitions and results

* `New.exists_Ioi_subset_integrableExpSet_of_analyticAt`: Landau's lemma; the Laplace transform of
  a measure is not analytic at its abscissa of convergence.
* `New.IsPolar.landau`: let `β > 0`. If `E v ≤ e^{(β-1)v}` for all large `v` and `re (r x) ≥ 0`
  for real `x > β`, then `r ρ = 0` for `re ρ > β`.

Notions from other files:
* `New.IsPolar` (from `Lib.Analytic.EntireLFunction`): `E` is measurable, `|E v| ≤ C e^v` for
  `v ≥ 0`, and `∫₀^∞ E(v) e^{(1-s)v} dv` continues meromorphically with at most simple poles of
  residue `r ρ` in `re ρ > 0`.

## Relation to the literature

Known result: Landau's lemma on Dirichlet integrals of one sign. It is applied to transforms with
simple poles whose residues at real points have non-negative real part: no pole lies to the right
of the abscissa given by the one-sided bound. Source: Montgomery and Vaughan, Multiplicative
Number Theory I, 2007, Lemma 15.1 (Widder, The Laplace Transform, 1941, II Thm 5b).


 ### Landau's lemma 

### `mem_integrableExpSet_of_summable_taylor`

 Let `X ≤ 0` be measurable and let `g` be equal near a real `z` to the moment generating function
`s ↦ ∫ exp (s X) ∂μ`, which converges near `z`. If the Taylor series of `g` at `z` converges at a
real `σ ≤ z`, then the moment generating function converges at `σ`. 

### `exists_mul_exp_le`

 Let `E` satisfy `|E v| ≤ C e^v` for `v ≥ 0`, and let `β > 0`. If `E v ≤ e^{(β-1)v}` for large
`v`, then `E(v) e^v ≤ K e^{βv}` for some `K` and all `v > 0`. 

### `exists_measure_laplace_eq`

 Let `E` be measurable with `|E v| ≤ C e^v` for `v ≥ 0`, and let `β > 0`. If `E v ≤ e^{(β-1)v}`
for large `v`, then there are a measure `μ` and a real `K` such that, for `re s > β + 2`, the
integral `∫ e^{-s|v|} ∂μ` converges to `K / (s - β) - ∫₀^∞ E(v) e^{(1-s)v} dv`. 

### `eventuallyEq_of_eq_far_right`

 Identity theorem: two functions meromorphic on `re z > a` that agree far to the right agree
on a punctured neighbourhood of every point of the half-plane. 

### `exists_Ioi_subset_integrableExpSet_of_analyticAt`

 **Landau's lemma.** Let `X ≤ 0` be measurable and let the moment generating function
`s ↦ ∫ exp (s X) ∂μ` converge to the right of `a`. If it agrees near the real points `x > a` close
to `a` with a function `g` that is analytic at `a`, then it converges on a larger half-line. So it
is not analytic at its abscissa of convergence. 

### `exists_Ioi_subset_integrableExpSet`

 Let `X ≤ 0` be measurable and let the moment generating function `s ↦ ∫ exp (s X) ∂μ` converge
to the right of `a`. Let `Ψ` be meromorphic at `a`, equal to it on a punctured neighbourhood of
every real `x > a`, and with at most a simple pole at `a`: `(z - a) Ψ z → c` with `re c ≤ 0`. Then
the moment generating function converges on a larger half-line. 

### `IsPolar.landau`

 **No pole to the right of `β`**, by Landau's lemma and the sign of the residues at real points.
Suppose `IsPolar E r`: `|E v| ≤ C e^v` for `v ≥ 0` and the transform
`∫₀^∞ E(v) e^{(1-s)v} dv` has a meromorphic continuation with at most simple poles of residue `r ρ`
in `re ρ > 0`. Let `β > 0`. If `E(v) ≤ e^{(β-1)v}` for all large `v` and the residues at real points
right of `β` have real part `≥ 0`, then there is no pole in `re s > β`, that is, `r ρ = 0`. 
