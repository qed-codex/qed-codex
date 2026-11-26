---
{
  "module": "src/New/Derivatives/FormalGroup/Resolution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/Resolution.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/Resolution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Resolutions of the identity and power series in the compositions `y(μ_i z)`

This file is about families of vectors `u j` in `Eⁿ`, taken `m j` times, with
`z = ∑ m j (u j† z) u j` for all complex vectors `z` indexed by `InfinitePlace E × n`, where `u j`
is read as such a vector through the CM type, and about power series composed with linear forms
`μ_i z`: products of the series `θ(μ_i z)`, for the theta function `θ` of a lattice `C`, and
integral series in the `y(μ_i z)`, for the parameter `y` of the elliptic curve of `C`.

The following imported notions occur in the statements.

* `Φ w` is the complex embedding of the CM type at the infinite place `w` of `E`.
* `ιₚ` is a fixed embedding of `ℂ` into `ℂ_p`, and `valRingCp p` is the closed unit ball of `ℂ_p`.
* `C.multiSeriesRing μ` is the ring of power series with integral coefficients in the series
  `y(μ_i z)`, where `y` is the Taylor series of the parameter `C.translatedY` of the curve.

## Main definitions and results

* `New.dagger`: the coefficients of the linear form `y† z` of a vector `y` in `Eⁿ`;
  `New.daggerForms`: the same for a family of vectors, read in `ℂ_p`.
* `New.IsResolution`: families of vectors `u j`, taken `m j` times, with
  `z = ∑ m j (u j† z) u j` (Parseval frames).
* `New.IsIntegralAbove`: elements of `E` that are integral at all places above `p`; they are
  quotients of elements of `𝓞 E` by natural numbers prime to `p`
  (`New.IsIntegralAbove.exists_mul_eq`).
* `New.CMLattice.thetaProd`: the product of copies of `θ` along linear forms.
* `New.CMLattice.rescale_thetaProd`, `New.CMLattice.rescale_mem_multiSeriesRing`: scaling the
  variables scales the linear forms in a product of copies of `θ` and in an integral series in
  copies of the parameter.
* `New.CMLattice.pderiv_mem_multiSeriesRing`: for integral linear forms, partial derivatives
  preserve the ring of such series.

## Relation to the literature

A resolution of the identity is a Parseval frame.


 ## Resolutions of the identity, integrality above a prime, and products of theta series 

### `dagger`

 The coefficient at the coordinate `x = (w, c)` of the linear form
`y† z = ∑ conj (Φ w (y c)) z (w, c)`, where `Φ w` is the embedding of the CM type at the infinite
place `w` and the sum is over all pairs `(w, c)`. 

### `IsResolution`

 The vectors `u j` of `Eⁿ`, taken `m j` times, are a resolution of the identity:
`z = ∑ m j (u j† z) u j` for all complex vectors `z` indexed by the pairs `(w, c)`, written in
coordinates. Here `u j` is read as the vector with coordinates `Φ w (u j c)`, where `Φ w` is the
embedding of the CM type at the infinite place `w`, and `dagger (u j)` gives the coefficients of
the linear form `u j† z`. 

### `IsResolution.sum_conj_mul`

 Parseval's identity. If `∑ m_j u_j u_j† = 1` (`IsResolution u m`), then
`∑ m_j conj (u_j† z') (u_j† z) = ∑ conj z'_x z_x` for all complex vectors `z` and `z'`. 

### `IsIntegralAbove`

 The element `y` of the number field `E` is integral at all places above `p`. A finite place
`w : FinPlace E` is a nonzero prime of `𝓞 E` (a point of `HeightOneSpectrum (𝓞 E)`), `w.asIdeal` is
its underlying ideal and `w.valuation E` is its adic valuation on `E`. 

### `IsIntegralAbove.exists_mul_eq`

 Let `E` be a CM number field with a CM type (`CMType E`) and `p` a prime number. An element `y`
of `E` that is integral at all primes of `𝓞 E` above `p` is the quotient of an integer `α` of `E`
by a natural number `N` prime to `p`. 

### `IsIntegralAbove.norm_le_one`

 An element integral above `p` is integral under every embedding into `ℂ_p`. 

### `IsIntegralAbove.norm_conj_le_one`

 If `y` is integral above `p`, then the complex conjugate of its image under any complex
embedding `τ` has norm at most one in `ℂ_p`, read there by `ιₚ`. 

### `daggerForms`

 The coefficients of the linear forms `u_j† z` of a family of vectors, read in `ℂ_p` by `ιₚ`. 

### `IsResolution.sum_smul_linearSeries`

 Let `∑ m_j u_j u_j† = 1` (`IsResolution u m`), where `u j` in `Eⁿ` is read as the complex vector
with coordinates `Φ w (u j c)`, and fix `x = (w, c)`. Suppose the integral elements `ν j` of `ℂ_p`
are the images of `Φ w (u j c)` under the embedding `ιₚ` of `ℂ`, and the integral vectors `μ j` are
the coefficients `daggerForms u j` of the forms `u_j† z`, read in `ℂ_p` by `ιₚ`. Then
`∑ m_j ν_j (μ_j z) = z_x` as power series over the valuation ring `valRingCp p` of `ℂ_p`. 

### `CMLattice.thetaProd`

 The product `∏ θ(μ_j z) ^ m j` of copies of the theta function `C.θ` along linear forms `μ_j`,
as a power series with coefficients in `ℂ_p`. Here `C` is a lattice in `ℂ` with a point `t` of
order two, stable under the ring of integers of `ℚ(√-d)` if `d ≠ 0`; `C.θ` is the twisted
translate by `t` of its sigma function, normalized by `θ(0) = 1`; `taylorVia ιₚ f` is the Taylor
series of `f` at `0`, its coefficients read in `ℂ_p` by the embedding `ιₚ` of `ℂ`; and
`linearSeries (μ j)` is the linear form `μ_j z = ∑ μ j x * z x`. 

 ## Scaling and derivatives of series composed with linear forms 

### `rescale_subst_linearSeries_eq_subst_smul`

 Scaling every variable by `a` in the power series `g.subst (linearSeries c)`, i.e. `g` evaluated
at the linear form `∑ c_i z_i`, gives `g.subst (linearSeries (a • c))`. 

### `map_rescale`

 Applying a ring homomorphism `φ` to the coefficients turns a scaling of the variables by `a`
into a scaling by `φ a`. 

### `Space.jetSeries_mul_eq_rescale`

 Multiplying the scale `b` of the series `V.jetSeries b f` by `a` scales its variables by `a`.
The coefficient of `z ^ α` in `V.jetSeries b f` is `b ^ |α| / α!` times the theta functional of
`v ⊗ f`, where `v` is the Fock vector of `z ^ α`. 

### `rescale_thetaProd`

 Scaling all variables of the product by `a` multiplies each linear form `μ_i` by `a`. 

### `rescale_mem_multiSeriesRing`

 Let `d` be any natural number and `C` a lattice in `ℂ` that is stable under the ring of integers
of `ℚ(√-d)`, with a point `t` of order two. Let `y` be the Taylor series at `0`, read in `ℂ_p`, of
the function `C.translatedY z = (℘'(z + t) - a₁ (℘(z + t) - ℘(t))) / 2`, where `a₁ ^ 2 = 12 ℘(t)`,
so that `C.multiSeriesRing μ` is the ring of power series with integral coefficients in the
`y(μ_i z)`. If `H(z)` is such a series in the `y(μ_i z)`, then `H(a z)` is such a series in the
`y((a μ_i) z)`. 

### `pderiv_mem_multiSeriesRing`

 For linear forms `μ_i` with coefficients of norm at most one, partial derivatives preserve the
ring `C.multiSeriesRing μ` of power series with integral coefficients in the `y(μ_i z)`. Here `d`
is a prime congruent to `7` modulo `8`, the lattice `C` is stable under the ring of integers of
`ℚ(√-d)`, and `y` is the Taylor series of the parameter `C.translatedY` of its elliptic curve. 
