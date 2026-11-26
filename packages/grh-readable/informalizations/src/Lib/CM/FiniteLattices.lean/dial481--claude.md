---
{
  "module": "src/Lib/CM/FiniteLattices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/FiniteLattices.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/FiniteLattices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finitely many CM lattices

* `New.CMLattice.finite_range_latticeModule`: for a prime `d ≡ 7 mod 8`, only finitely many lattices
  in `ℂ` underlie a CM lattice for `K = ℚ(√-d)`.
* `New.CMLattice.theta_eq_of_latticeModule_eq`: the theta function `θ` depends only on the lattice;
  in particular it does not depend on the representative `t` of the point of order two.
* `New.CMLattice.exists_norm_twistedTranslate_theta_le`: the values `(T_u θ)(0)` are bounded
  uniformly in the CM lattice and in `u`.

Each CM lattice is a multiple of one of finitely many ideals, and the scaling `℘''(t) = 2` fixes the
factor up to a fourth root of unity.

Notions from other files:
* `C : CMLattice d`: a lattice `C.Λ` in `ℂ` stable under `𝓞_K`, with a point `C.t` of order two
  modulo `C.Λ` such that neither `ω t` nor `ω̄ t` lies in `C.Λ` (`ω = quadGen d = (1 + √-d) / 2`),
  scaled so that `℘''(C.t) = 2`.
* `C.latticeModule`: the lattice `C.Λ` as an `𝓞_K`-submodule of `ℂ`.
* `QuadField.scaledIdeal d (u, 𝔞)`: the submodule `u 𝔞` of `ℂ`, for a fractional ideal `𝔞` of `K`.
* `C.twistedTranslate 1 u f`: the function `(T_u f)(z) = exp(-π (z ū + |u|² / 2) / C.area)
  f(z + u)`.
* `C.θ`: the translate `T_t σ` of the sigma function, normalised to `1` at `0`.

## Relation to the literature

Known result: lattices with complex multiplication by `𝓞_K` up to homothety correspond to the ideal
classes. Source: Silverman, Advanced topics in the arithmetic of elliptic curves, Chapter II.


### `sumInvPow_four_of_mul_mem_iff`

 The sum `L.sumInvPow y 4 = ∑ (l - y)⁻⁴` over the lattice of `L` is homogeneous of degree `-4`:
if `L' = c L` with `c ≠ 0` and `z ≡ c y` modulo `L'`, then the sum for `L'` at `z` is `c⁻⁴` times
the sum for `L` at `y`. 

### `six_mul_sumInvPow_t`

 The normalisation `℘''(t) = 2` of a CM lattice `C` at its point `t = C.t` of order two (a field
of `C` fixes `g₂` accordingly), written with the series `℘''(t) = 6 ∑ (l - t)⁻⁴`, where `l` runs
over the lattice. 

### `mul_t_sub_t_mem`

 Let `d` be a prime `≡ 7 mod 8` and let `C`, `D` be CM lattices for `ℚ(√-d)`. If multiplication
by `c` maps the lattice `C.Λ` onto `D.Λ`, then it takes the marked point `C.t` of order two to
`D.t` modulo `D.Λ`: the marked point is the only point of order two that neither
`ω = quadGen d = (1 + √-d) / 2` nor `ω̄` multiplies into the lattice. 

### `pow_four_eq_one_of_mul_mem_iff`

 Let `d` be a prime `≡ 7 mod 8`. If multiplication by `c ≠ 0` maps the lattice `C.Λ` of one CM
lattice onto the lattice `D.Λ` of another, then `c` is a fourth root of unity, as both are scaled
so that `℘''(t) = 2` at their marked points `t` of order two. 

### `IsInClass.exists_pow_four_eq_one_and_eq_scaledIdeal_mul`

 If `C` and `D` lie in the same ideal class `𝒞` (their lattices are complex multiples of ideals
in `𝒞`), then the lattice of `C` is `c` times that of `D` for a fourth root of unity `c`. 

### `finite_range_latticeModule`

 For a prime `d ≡ 7 mod 8`, only finitely many `𝓞_K`-submodules of `ℂ` are the lattice
`C.latticeModule` of a CM lattice `C` for `K = ℚ(√-d)`. 

### `area_eq_of_latticeModule_eq`

 Two CM lattices with the same underlying lattice have the same area of a period
parallelogram. 

### `theta_eq_of_latticeModule_eq`

 The theta function `θ` of a CM lattice depends only on the underlying lattice. 

### `exists_norm_twistedTranslate_theta_le`

 For a prime `d ≡ 7 mod 8`, the values `(T_u θ)(0) = exp(-π |u|² / (2 A)) θ(u)` are bounded
uniformly in the CM lattice `C` and in `u : ℂ`. Here `θ = C.θ` is the theta function of `C`,
`A = C.area`, and `T_u = C.twistedTranslate 1 u` is the twisted translation of degree one. 
