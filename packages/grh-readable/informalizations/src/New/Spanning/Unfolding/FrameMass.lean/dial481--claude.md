---
{
  "module": "src/New/Spanning/Unfolding/FrameMass.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FrameMass.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FrameMass.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Masses of spheres and of frames

For the data `D` and an infinite place `v`, the file defines the mass `sph_l` of the unit sphere of
`ℂ ^ l` and the product `fr_v = N ^ k sph_{k+1} ⋯ sph_r`. By the approximate formula for the ratio
of masses in consecutive ranks, the product of the `fr_v` over the infinite places is at most
`N ^ (k f) mass_k / mass_r` up to a factor close to one, where `f` is the number of infinite places
and `mass_l` is the mass `New.mass` in rank `l`.

## Main definitions and results

* `New.Data.unitSphereMass`, `New.Data.frameMass`: the numbers `sph_l` and `fr_v`.
* `New.Data.prod_frameMass_mul_le`: the upper bound for the product of the `fr_v`.
* `New.Data.prod_frameMass_mul_openCellConst_eq`: the product of the `fr_v` in terms of the
  constants `New.Filling.siegelConst` and `New.Shape.openCellConst`.

Notions from other files:
* `New.Data`: the data: a CM field `E` with `f` infinite places (the type `D.Φ`) and root
  discriminant `rd = D.rootDisc`, a generator `P.deltaE D.towerExp` of its different, a prime level
  `N`, a weight `b`, the length `x` of the prime sum, and ranks `r = k + 2 ϱ + 1`.
* `New.Data.shape`: the shape of the hermitian space `Y₀` of rank `r`, which is the sum of `ϱ`
  hyperbolic planes, a space `X₀` of rank `k` and a line.
* `New.mass E l`: the mass of the genus of the standard hermitian lattice `O_E ^ l`.
* `New.Filling.siegelConst`: `c_S = (π ^ k / ((k - 1)! N ^ k)) ^ f |disc E| ^ (1/4) vol(Ô) ^ k`.
* `New.Shape.openCellConst`: `c_G = vol U(k) (2 π ^ k / (k - 1)!) / vol U(r)`.
* `New.volÔ E`: the volume `vol(Ô) = (2 / rd) ^ f` of the integral finite adeles.


### `log_pow_div_pow_sub_one_le`

 For the prime level `N` and the rank `k ≥ 1` of the data, the logarithm of `N ^ k / (N ^ k - 1)`
is at most `2 / N`. 

### `sum_two_div_two_pow_le_log_sub`

 The `r - k` errors `2 / 2 ^ ϱ` of the mass formula in the ranks between `k` and `r` add up to at
most `log (1 + b⁻⁹) - 2 f · 2/N`. 

### `abs_sum_log_mass_ratio_sub_le`

 The main term of `log (mass_{i+1} / mass_i)`, with `mass_l` the mass of the genus of `O_E ^ l`,
is `f ((i + 1/2) log rd + log i! - (i + 1) log 2π)`, with `rd` the root discriminant and `f` the
number of infinite places of `E`. The sum over `k ≤ i < r` of the differences between logarithm and
main term has absolute value at most `log (1 + b⁻⁹) - 2 f · 2/N`. 

### `apply_deltaE_mem_Icc`

 At every infinite place `v`, the generator `ϖ` of the different of `E` has `2 ≤ |ϖ|_v ≤ b`,
where `b` is the weight of the data. 

### `two_div_and_inv_sqrt_deltaE_mem_Icc`

 At the infinite place `v`, let `ϖ = P.deltaE D.towerExp`. Write `|ϖ|_v = v ϖ` and let `b = D.b`
be the scale of the data. Then the numbers `2 / |ϖ|_v` and `|ϖ|_v ^ (-1 / 2)` lie between `b⁻¹` and
`1`. 

### `unitSphereMass`

 The number `sph_l = (2π) ^ l / (|ϖ|_v ^ (l - 1 / 2) (l - 1)!)` at the infinite place `v`, where
`ϖ` generates the different of `E`. For `l ≥ 1` it is the mass of the unit sphere of `ℂ ^ l` for
the fibre measure `dy / d⟨y, y⟩`, when `ℂ` carries `2 / |ϖ|_v` and `ℝ` carries `|ϖ|_v ^ (-1 / 2)`
times Lebesgue measure. 

### `frameMass`

 The number `fr_v = N ^ k sph_{k+1} ⋯ sph_r` at the infinite place `v`, where `N` is the level,
`k ≤ r` are the ranks of the data and `sph_l` is `New.Data.unitSphereMass`. 

### `one_le_inv_unitSphereMass`

 The mass `sph_l` of the unit sphere of `ℂ ^ l` is at most one for `l ≥ 1`, at every infinite
place `v`. This is a corollary of the size of the different. 

### `inv_unitSphereMass_le_pow`

 For `l ≤ r` and every infinite place `v`, the number `sph_l` satisfies `sph_l⁻¹ ≤ x ^ (18 l)`.
For `l ≥ 1` it is the mass of the unit sphere of `ℂ ^ l`; for `l = 0` the formula that defines it
gives `|ϖ|_v ^ (1 / 2)`, with `ϖ` the generator of the different. 

### `r_eq_k_add_two_mul_varrho_add_one`

 The rank `r` of the data equals `k + (2 ϱ + 1)`, where `k` is the smaller rank of the data and
`ϱ` the number of hyperbolic planes. 

### `cast_card_Ico_k_r`

 For the ranks `k ≤ r` of the data there are `2 ϱ + 1` integers `i` with `k ≤ i < r`, where `ϱ`
is the number of hyperbolic planes. 

### `inv_pow_le_frameMass`

 The number `fr_v = N ^ k sph_{k+1} ⋯ sph_r` is at least `b ^ (-(ϱ + 1) r)` at every infinite
place `v`. 

### `log_prod_unitSphereMass`

 The logarithm of the product of the sphere masses `sph_{i+1}` over the `f` infinite places is
`-f ((i + 1/2) log rd + log i! - (i + 1) log 2π)`, with `rd` the root discriminant of `E`. 

### `abs_log_prod_unitSphereMass_sub_le`

 The product of the sphere masses `sph_{i+1}` over the infinite places is `mass_i / mass_{i+1}`
up to a factor close to one: the logarithms differ by at most `2 / 2 ^ ϱ` for `i ≥ k`. 

### `prod_prod_unitSphereMass_pos`

 The product of the sphere masses `sph_{k+1}, …, sph_r` over all infinite places is positive. 

### `prod_frameMass_eq_mul_prod`

 The product of `fr_v = D.frameMass v = N ^ k sph_{k+1} ⋯ sph_r` over the `f = D.f` infinite
places `v` in `D.Φ` equals `(N ^ k) ^ f` times the product, over `k ≤ i < r`, of the products of
`sph_{i+1}` over the infinite places. 

### `prod_frameMass_mul_le`

 The product of the `fr_v = N ^ k sph_{k+1} ⋯ sph_r` over the `f` infinite places is at most
`(1 + b⁻⁹) (1 - N ^ (-k)) ^ (2 f) N ^ (k f) mass_k / mass_r`. The statement has `mass_r` and the
factor `(1 - N ^ (-k)) ^ (2 f)` moved to the left side. 

### `sum_Ico_k_r_cast`

 For the ranks `k` and `r = k + 2 ϱ + 1` of the data, the sum of the integers `i` with
`k ≤ i < r` is `(2 ϱ + 1) (k + ϱ)`, where `ϱ` is the number of hyperbolic planes. 

### `log_prod_frameMass`

 The logarithm of the product of the `fr_v = N ^ k sph_{k+1} ⋯ sph_r` over the `f` infinite
places, as a linear form in the logarithms of `N`, `2`, `π`, the root discriminant and the `i!`. 

### `log_openCellConst`

 The logarithm of `c_G = vol U(k) (2 π ^ k / (k - 1)!) / vol U(r)`, the constant of the open
cell, as a linear form in the logarithms of `2`, `π` and the factorials. Here `vol U(j)` is the
volume of the compact unitary group. The shape `D.shape` records the number `ϱ` of hyperbolic planes
and an index set with `k` elements. 

### `prod_frameMass_mul_openCellConst_eq`

 The product of the `fr_v = N ^ k sph_{k+1} ⋯ sph_r` over the `f` infinite places `v` of `E`
satisfies `(∏ fr_v) c_G ^ f |disc E| ^ (ϱ / 2) = c_S N ^ (2 k f) vol(Ô) ^ (ϱ + 1 + 2 ϱ (ϱ + k))`. 
