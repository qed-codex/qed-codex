---
{
  "module": "src/New/Spanning/Unfolding/FillingAdmissible.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Filling data for admissible data: fit to Y₀, Bessel bounds, standing hypotheses

For admissible data `D`, the file shows that the filling data `New.Data.filling` fit the space `Y₀`.
It also shows that they satisfy the standing hypotheses `New.Filling.IsAdmissible`, so that the
general filling theorem applies.

## Main definitions and results

* `New.Data.filling_fits`: the filling data `New.Data.filling` fit the space `Y₀`
  (`New.Filling.Fits`).
* `New.Data.sourceFormCoords`: source forms in coordinates, indexed by pairs (class, Bessel
  coordinate).
* `New.Data.goodProjTranslate`: the map from forms of level `M` on `Y₀` to the image of the good
  idempotent `New.Data.e₀`. It is a translation followed by this idempotent, scaled by the order of
  the finite group `𝖦`.
* `New.Data.card_besselSystem_le_pow`, `New.Data.card_besselCoord_le_pow`: the Bessel system at one
  place has at most `b ^ (2 k)` coordinates, and their tensor product at most `b ^ (2 k f)`.
* `New.Data.log_filling_besselDegree_mem_Icc`: two-sided bounds for the logarithm of the degree of
  the Bessel systems.
* `New.Data.card_mul_card_classes_mul_prod_le`, `New.Data.card_sq_mul_mass_mul_prod_le`: two
  products built from group orders, class number, masses, dimensions and degrees are at most
  `(1 + b⁻⁹)` times `New.Filling.mainSecondMoment`. `New.Data.card_mul_prod_frameMass_le` states
  both.

Notions from other files:
* `New.Data.spaceY`: for an index `j`, the hermitian space `Y_j` with its adelic frame, hence its
  lattice `𝖬_j`, chosen as in `New.Data.exists_space_isStd_of_le_and_gram_eq_of_lt`. Only `j = 0`
  occurs in this file.
* `New.Data.chosenGL`: The finite group 𝖦 = ∏ GL_r(𝔽_w), over the chosen places w above p₀ and p₁.
* `New.Data.targetParameter`: The entry i (from 0) of the target parameter at v: k/2 − 1 − i for
  i < k − 1, and Δ/2 − w_{i+2−k}(v) otherwise, where Δ/2 = `D.halfGap` and
  w_j(v) = `D.liftWeight j v`.
* `New.Filling.besselDegree`: The product over infinite places of the degrees of the Bessel systems.
* `New.Data.logLevelTarget`: a number `λ`, built from the mean of the `log (D.weight v)`, from
  `log (M rootDisc / 2π)` and from `log b`, with `λ ≤ log N ≤ λ + √(log b)`.


 ## Fit to Y₀, source forms in coordinates and the projection to target forms 

### `filling_fits`

 The filling data of D fit the hermitian space Y₀ = `D.spaceY 0` in the sense of
`New.Filling.Fits`. 

### `inclXFin_zero_mem_stdLevel_iff`

 A finite adelic point of U(X₀) preserves the lattice of Y₀ if and only if it is integral and
its last row is that of 1 modulo π. In the coordinates of the filling data this is
`New.Filling.inclHFin_mem_latticeStabilizer_iff`. 

### `comap_inclXFin_zero_chosenLevel`

 The finite adelic points of U(X₀) that lie in the principal level of Y₀ at the chosen places
form the level `New.Data.levelX` of X₀. In the coordinates of the filling data this is
`New.Data.levelX_zero_eq_comap`. 

### `sourceFormCoords`

 The isomorphism that applies the central translation by `D.latticeScale 0` to a source form on
X₀ and takes its values at the class representatives, in the coordinates of the Bessel systems. 

### `goodProjTranslate`

 For s in 𝖦, the linear map from forms of parameter ς and level M on Y₀ to the image of the good
idempotent e₀. It is the translation by s, followed by |𝖦| times the action of e₀. 


## Bessel systems: number of coordinates, target parameter and degree

`New.Data.targetParameter v i` is numbered from 0, and `f` is the number of infinite places.


### `card_besselSystem_le_add_pow`

 At each infinite place `v`, the Bessel system of `D` has at most `(k + a) ^ k` coordinates, `k`
the rank of `X₀`. Their number is the dimension of the representation of `U(X₀)` at `v`, which is
that of a symmetric power of degree at most `a = D.a` of a space of dimension `k`. 

### `card_besselSystem_le_pow`

 At each infinite place `v`, the number of coordinates of the Bessel system of `D`, that is the
dimension of the representation of `U(X₀)` at `v`, is at most `b ^ (2 k)`, `k` the rank of `X₀`. 

### `card_besselCoord_le_pow`

 The tensor product of the Bessel systems of `D` over the `f` infinite places has at most
`b ^ (2 k f)` coordinates, `k` the rank of `X₀`. 

### `card_besselCoord_mul_factorial_le`

 For admissible data `D`, let `d` be the number of coordinates of the tensor product of the
Bessel systems, `k` the rank of `X₀`, `f` the number of infinite places and `b = D.b` the weight at
the `b`-places. Then `d ((k - 1)!)^f ≤ (b^{5/4})^{k f}`, where `b^{5/4}` is written `(√√b)^5`. 

### `targetParameter_sub_mem_Icc`

 For `i < l` and an infinite place `v`, the difference
`D.targetParameter v i - D.targetParameter v l` of entries of the target parameter lies between `1`
and the lift weight `D.liftWeight (l + 2 - D.k) v`. Here `k = D.k` is the rank of the source, and
`l + 2 - D.k` is truncated subtraction of natural numbers. 

### `filling_besselDegree_eq_exp_sum`

 The degree `D.filling.besselDegree` of the Bessel systems of `D` is the exponential of the sum,
over the infinite places `v` and over `k - 1 ≤ l < r`, of `∑_{i<l} log (ς_i - ς_l) - log l!`. Here
`ς = D.targetParameter v` is the sequence of `r = D.r` entries from which the Harish-Chandra
parameters at `v` are read off, and `k = D.k`. 

### `log_filling_besselDegree_mem_Icc`

 The logarithm of the degree of the Bessel systems of `D`, plus `f` times the sum of `log l!`
over `k − 1 ≤ l < r`, lies between `∑_v m (k − 1) log W_v` and `∑_v m r (log W_v + 1/x)`. Here `v`
runs over the `f` infinite places, `k` is the rank of `X₀`, `r` is the number of entries of the
target parameter, `m = r - k + 1`, `x` is the parameter `D.x` of the data and `W_v` is
`D.weight v`. 


## Number of classes, mean values and the standing hypotheses

The ratio of the main second moment to the second moment of the Bessel group is computed exactly
(`New.Data.mainSecondMoment_div_identitySecondMoment_eq`). The sizes of the degree, of the ratio of
the masses and of `N` then give the range of this ratio
(`New.Data.mainSecondMoment_div_identitySecondMoment_mem_Icc`).


### `relIndex_latticeStabilizer`

 The finite points of `U(X₀)` that `New.Filling.inclHFin` sends into the integral group
`New.Filling.latticeStabilizer` have index `(N^k - 1)^f` in the group `New.stdLevel` of integral
points, `N` being the prime level, `k` the rank of `X₀` and `f` the number of infinite places. 

### `card_classes_eq_card_mul_pow_mul_mass`

 The number of classes of level `New.Data.levelX 0` on `U(X₀)` is `|H̄| (N^k - 1)^f` times
the mass `New.mass` in rank `k`, where `H̄` is the image (`New.Filling.reducedImage`) under
reduction of the integral points of `H = besselH`, the copy of `U(X₀)` in the unitary group, `N` is
the prime level and `f` is the number of infinite places. 

### `prod_frameMass_mul_div_eq`

 With `fr_v` the frame mass, and `d_v`, `deg_v` the dimension and the degree of the Bessel system
at `v`, the product of the `fr_v d_v ^ 2 / deg_v` is `(∏ fr_v) d ^ 2 / deg`, where `d` and `deg` are
the dimension and the degree of the tensor product of the Bessel systems. 

### `prod_unitSphereMass_mul_div_eq`

 At an infinite place `v`, let `fr_v` be the frame mass, `sph_k` the mass of the unit sphere in
the rank `k` of `X₀`, `d_v` and `deg_v` the number of coordinates and the degree of the Bessel
system, and `c_v = fr_v N ^ k d_v ^ 2 / (sph_k deg_v)`, with `N` the prime level. The product of
the `sph_k c_v` over the `f` infinite places is `N ^ (k f) (∏ fr_v) d ^ 2 / deg`, where
`d = ∏ d_v` and `deg = ∏ deg_v`: the masses `sph_k` cancel. 

### `filling_mainSecondMoment_eq`

 The main second moment of the filling data is
`(|H̄| (N ^ k - 1) ^ f mass_k d) ^ 2 / (deg mass_r)`, where `H̄` is the reduced image of `besselH`,
`mass_l` is `New.mass` in rank `l`, and `d`, `deg` are the dimension and the degree of the tensor
product of the Bessel systems. 

### `pow_sub_one_pos`

 Since the prime level `N` is at least `2`, the number `N ^ k - 1` is positive. 

### `card_sq_mul_mass_mul_prod_le`

 For the filling data of admissible data `D`, let `H̄` be the reduced image of `besselH`, `d_v`
and `deg_v` the dimension and the degree of the Bessel system at `v`, `fr_v` the frame mass, `sph_k`
the mass of the sphere in rank `k`, `mass_l` the mass `New.mass` in rank `l` and
`c_v = fr_v N ^ k d_v ^ 2 / (sph_k deg_v)`. Then `|H̄| ^ 2 mass_k ∏ sph_k c_v` is at most
`(1 + b⁻⁹)` times the main second moment `(n_X ∏ d_v) ^ 2 / (mass_r ∏ deg_v)`. Here `n_X` is the
number of classes, `k`, `r` are the ranks of `X₀`, `Y₀`, and `b = D.b` is the weight at the
`b`-places. 

### `card_mul_card_classes_mul_prod_le`

 For the filling data of admissible data `D`, let `H̄` be the reduced image of `besselH`, `n_X`
the number of classes, `d_v` and `deg_v` the dimension and the degree of the Bessel system at `v`
and `fr_v` the frame mass. Then `|H̄| n_X ∏ fr_v d_v ^ 2 / deg_v` is at most `(1 + b⁻⁹)` times the
main second moment `(n_X ∏ d_v) ^ 2 / (mass_r ∏ deg_v)`. Here `mass_r` is the mass `New.mass` in the
rank `r` of `Y₀`, and `b = D.b` is the weight at the `b`-places. 

### `card_mul_prod_frameMass_le`

 **Mean values.** For the filling data of admissible data `D`, let `H̄` be the reduced image of
`besselH`, `n_X` the number of classes, `d_v` and `deg_v` the dimension and the degree of the Bessel
system at `v`, `fr_v` the frame mass, `sph_k` the mass of the unit sphere in rank `k`, `mass_l` the
mass `New.mass` in rank `l` and `c_v = fr_v N ^ k d_v ^ 2 / (sph_k deg_v)`. The numbers
`|H̄| n_X ∏ fr_v d_v ^ 2 / deg_v` and `|H̄| ^ 2 mass_k ∏ sph_k c_v`, which bound mean values, are at
most `(1 + b⁻⁹)` times the main second moment `(n_X ∏ d_v) ^ 2 / (mass_r ∏ deg_v)`. Here `N` is the
prime level, `k`, `r` are the ranks of `X₀`, `Y₀`, and `b = D.b` is the weight at the `b`-places. 

### `scaledSiegelConst_le`

 For the filling data of admissible data `D`, the scaled Siegel constant `|S̄| |Ū| n_X c_S` is at
most `(1 + b⁻⁹)` times the main second moment `(n_X d)² / (deg mass_r)` times
`deg c^f / vol^n (cov Λ / d)²`. Here `S̄` is the reduced image of the Bessel subgroup `besselS`,
`|Ū| = unipotentOrder`, `n_X` is the number of classes, `c_S = siegelConst`, `b = D.b` is the weight
at the `b`-places, `d` and `deg` are the number of coordinates and the degree of the tensor product
of the Bessel systems, and `mass_r` is the mass in the rank `r` of `Y₀`. Further
`c = openCellConst`, `f` is the number of infinite places, `vol` the volume of the integral finite
adeles, `n` the number of frame vectors, `cov = unipotentCovolume` and `Λ = frameScaleProd`. 

### `filling_reduction_surjective`

 Reduction at the chosen places maps the integral group `New.Filling.latticeStabilizer` of the
filling data onto the finite group `New.Filling.ResidueGL`. 

### `mainSecondMoment_div_identitySecondMoment_eq`

 The main second moment of the filling data, divided by their identity second moment, is
`d (N ^ k - 1) ^ f mass_k / (deg mass_r |Ū|)`. Here `d` and `deg` are the number of coordinates and
the degree of the tensor product of the Bessel systems, `mass_l` is the mass in rank `l`, and `|Ū|`
is the order `unipotentOrder` of the reduced unipotent group; `N` is the prime level, `k` and `r`
are the ranks of `X₀` and `Y₀`, and `f` is the number of infinite places. 

### `abs_log_mainSecondMoment_div_identitySecondMoment_sub_le`

 Up to a factor `b ^ (± k f / 4)`, the ratio of the main second moment to the identity second
moment is `(M b ^ (-15 / 2)) ^ (k f) d ((k - 1)!) ^ f`. Here `b` is the weight at the `b`-places of
the admissible data `D`, `M = p₀ p₁` is the principal level, `d` is the number of coordinates of the
tensor product of the Bessel systems, `k` is the rank of `X₀` and `f` is the number of infinite
places. The statement is for the logarithms, with `D.logB = log b`. 

### `mainSecondMoment_div_identitySecondMoment_mem_Icc`

 For admissible data `D`, the ratio of the main second moment to the identity second moment lies
between `b ^ (11 k f)` and `(M / b ^ 6) ^ (k f)`. Here `b = D.b` is the weight at the `b`-places,
`M = p₀ p₁` is the principal level, `k` the rank of `X₀` and `f` the number of infinite places. 

### `N_le_pow`

 The prime level `N` is at most `b ^ (60 n)`, where `n` is `D.shape.n`. 

### `pow_div_le_pow_sub_one`

 Replacing `N ^ k` by `N ^ k - 1` loses at most the factor `b`, as both `b` and `N ^ k` are at
least `2`. 

### `instance : D.filling.IsAdmissible`

 The filling data of `D` satisfy the standing hypotheses `New.Filling.IsAdmissible`: the level
is the preimage of the principal level, reduction is onto, and the size inequalities hold. 
