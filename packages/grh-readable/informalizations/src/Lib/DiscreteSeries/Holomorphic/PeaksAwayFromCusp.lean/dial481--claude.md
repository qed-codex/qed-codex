---
{
  "module": "src/Lib/DiscreteSeries/Holomorphic/PeaksAwayFromCusp.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Holomorphic/PeaksAwayFromCusp.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Holomorphic/PeaksAwayFromCusp.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The peaks of a bounded holomorphic form lie away from the cusps

`(V.move g).firstMinimum` is the length of a shortest vector of the lattice at g, cut off at 1. It
is small deep in a cusp.

* `New.Rows.IsPeak`: a peak of a bounded function F is a point where |F| exceeds half of its
  supremum. At a peak x, |F| is at most 2|F(x)| everywhere and F(x) ≠ 0. A point where |F| is at
  least |F(x)| is again a peak.
* `New.Rows.exists_isPeak`: a bounded nonzero function has a peak.
* `New.Rows.IsPeak.le_firstMinimum`: let the order put the signs +1 first, and let F be a bounded
  form, holomorphic of a weight with gap 1 and entries in [-A, A] where A ≥ 2, and of a level
  p = -p̄ with im (Φ w p) in (0, A'] where A' ≥ 1. At every peak g of F the first minimum is at
  least (A A')^(-1/2).

A short lattice vector v is isotropic, and the transvection 1 - p v v^* J fixes F(g ·). Completing
squares writes the points n(z) = 1 - p z v v^* J of its one-parameter group, for im z > -1, as h b
with h real and b triangular (`New.Rows.exists_unitary_mul_triangular_of_pos`). The factor b^u is
bounded and tends to 0 as im z → ∞ (`New.Rows.exists_unitary_mul_triangular`). So z ↦ F(g n(z))
extends to a bounded holomorphic function of period 1 on im z > -1 that vanishes at i∞, and the
Schwarz lemma makes F(g) too small for a peak (`New.Rows.norm_le_of_transvection_invariant`). The
parameter is shifted by i, so that the half plane im z > -1 becomes the upper half plane and z = 0
becomes i.

Notions from other files:
* `New.IsPosFirstOrder`: The order o has distinct values and puts every index of sign +1 before
  every index of sign −1.
* `New.Rows.IsAdelicHol`: For every adelic g, some φ is analytic at all products h b (h preserving
  diag(s), b invertible and triangular for o, at each infinite place) and φ(h b) = b^u F(g·(h,1))
  (`New.IsHolOfWeight`).
* `New.HasHolGap`: The condition on signs ε, integer vector w and natural number γ that
  w_i + γ ≤ w_j whenever ε_i = +1 and ε_j = −1.
* `New.Space`: A hermitian space with a point: a matrix J over E and x in GL_n(𝔸) with xᴴJx equal to
  diag(s) at the infinite places and 1 at the finite places. `V.vecAtPoint y` is the adelic vector
  x⁻¹y, and `V.move g` is the space (J, xg).
* `New.Rows.rapidOfLevel`: The functions F that are continuous, left invariant under the rational
  points of V and right invariant under the principal level K(a), and that decay rapidly (members of
  `V.rapidFunctions`).

## Relation to the literature

Known result: Siegel's argument that a cusp form is large only away from the cusps. Here it is
proved for unitary groups over a CM field, for scalar functions of vector-valued weight and for
bounded forms, with half the supremum in place of an attained maximum. The distance from the cusp is
measured by the first minimum of the lattice, bounded below explicitly in weight and level. Source:
C. Poor, D. Yuen, Linear dependence among Siegel modular forms, Math. Ann. 318 (2000) 205-234, Thm
1.3; M. Eichler, Math. Ann. 213 (1975) 281-291; for the factorisation, Gill, Golub, Murray,
Saunders, Math. Comp. 28 (1974) 505-535.


### `New.Rows.exists_int_separating`

 An integer vector `u` with gap `1` for the signs `s` (`u i + 1 ≤ u j` whenever `s i = 1` and
`s j = -1`) is separated by an integer `A`: its entries at the signs `+1` are less than `A`, those
at the signs `-1` are at least `A`. 

### `New.Rows.sum_filter_lt_add_one`

 For an injective `o`, the sum of `x l` over `o l < o k + 1` is the sum over `o l < o k` plus
`x k`. 

### `New.Rows.transvection_gram`

 If `v` is isotropic for `J = diag s`, then `M = 1 - t v v^* J` has the Gram matrix
`Mᴴ J M = J - 2 re t J v v^* J`. 

### `New.Rows.exists_unitary_mul_triangular_of_pos`

 Completing squares. Let `o` be injective, `v` isotropic for `J = diag s`, put
`x k = s k |v k|²`, and suppose that the numbers `p a = 1 - 2 re t ∑ (x l, o l < a)` are positive.
Then `1 - t v v^* J = h b` with `h` in `USign s` (preserving `diag s`) and `b` invertible and
triangular for `o` (`IsBorelMatrix`), with diagonal entries `√(p (o k + 1) / p (o k))`. 

### `New.Rows.sum_mul_le_of_sign_mul_nonneg`

 If the real numbers `L k` sum to `0` and have the signs `s k`, and the integer vector `u` has
gap `1` for `s`, then `∑ L k * u k` is at most minus the sum of `L k` over the signs `+1`. 

### `New.Rows.sum_mul_le_of_sign_mul_nonpos`

 If the real numbers `L k` sum to `0` and have the signs `-s k`, and the entries of the integer
vector `u` have absolute value at most `B`, then `∑ L k * u k` is at most `-2 B` times the sum of
`L k` over the signs `+1`. 

### `New.Rows.one_sub_mul_sum_filter_pos`

 Let `o` put the signs `1` first and let `x` have total `0` and the signs `s`. If
`τ ∑ |x l| < 1`, then `1 - τ ∑ (x l, o l < a)` is positive for every `a`. 

### `New.Rows.sum_log_sub_log_eq`

 For an injective `o` and numbers `p a = 1 - τ ∑ (x l, o l < a)`, the sum of
`log (p (o k + 1)) - log (p (o k))` over an initial segment `T` of the order `o` is
`log (1 - τ ∑ (x k, k ∈ T))`. 

### `New.Rows.mul_log_sub_log_nonneg`

 If `c (b - a)` is nonnegative for positive `a` and `b`, then so is `c (log b - log a)`. 

### `New.Rows.exists_unitary_mul_triangular`

 Let `o` be injective and put the signs `1` of `J = diag s` first, let the weight `u` have gap
`1` (`u i + 1 ≤ u j` whenever `s i = 1` and `s j = -1`) and size at most `B ≥ 2`, and let `v` be
isotropic. If `y - η = 1 - re t |v|²` with `1 < y` and `0 < η ≤ 1 / 2`, then `1 - t v v^* J = h b`
with `h` in `USign s` (preserving `diag s`), `b` invertible and triangular for `o`
(`IsBorelMatrix`), and `|b ^ u| ≤ exp (2 B η) / √y` (here `b ^ u` is `diagChar u b`, the product of
the `b k k ^ u k`). 

### `New.Rows.transvection_mul`

 Two transvections `1 - a y y^* J`, `1 - c y y^* J` along one vector `y` isotropic for
`J = diag s` (`signMatrix s`) multiply by adding their parameters. 

### `New.Rows.exists_unitary_mul_triangular_upperHalfPlane`

 The factorisation `exists_unitary_mul_triangular` along the upper half plane. Let the signs `1`
of `J = diag s` come first in `o`, let the weight `u` have gap `1` and size at most `B ≥ 2` and let
`v` be isotropic. For purely imaginary `a` with `η = im a |v|²` in `(0, 1 / 2]`, the matrix
`1 - a (z - i) v v^* J` is `h b` (`h` preserves `J`, `b` is triangular for `o`) with
`|b ^ u| ≤ exp (2 B η) / √(1 + im z η)`. 

### `New.Rows.norm_I_le_of_periodic`

 The Schwarz lemma at the cusp: a holomorphic function on the upper half plane of period `1`
that vanishes at `i∞` and is bounded by `M` is at most `M exp (-2 π)` at `i`. 

### `New.Rows.IsPeak`

 A peak of a bounded function is a point where its modulus exceeds half of its supremum. 

### `New.Rows.IsPeak.bddAbove`

 The function is bounded. 

### `New.Rows.IsPeak.half_lt`

 The modulus at `x` exceeds half of the supremum. 

### `New.Rows.exists_isPeak`

 A nonzero bounded function has a peak. 

### `New.Rows.exists_isPeak_of_mem_rapidOfLevel`

 A nonzero member of `rapidOfLevel V a` (a rapidly decreasing form on the space `V` of level
`a`) has a peak. 

### `New.Rows.tendsto_prod_div_sqrt_atImInfty`

 For positive `η i`, the product of `c i / √(1 + im z * η i)` over a nonempty finite type tends
to `0` as `im z → ∞`. 

### `New.Rows.norm_le_of_transvection_invariant`

 The analytic part of `IsPeak.le_firstMinimum`. Let the order `o` put the signs `+1` first. Let
`F` on the real group `GInf E s` be holomorphic of a weight `u` for `o` (`IsHolOfWeight`: `F` times
the weight-`u` character of invertible `o`-triangular `b` extends analytically to products `h b`).
Let `u` have gap `1` (`u w i + 1 ≤ u w j` whenever `s i = 1`, `s j = -1`) and entries in `[-A, A]`,
`A ≥ 2`. Let `F` be bounded by `C > 0` and left invariant under `t`, which at each place is the
transvection `1 - a y y^* J` along an isotropic vector `y`, with `a` purely imaginary and
`J = diag s`. If the sizes `η w = im (a w) |y w|²` are positive and `A ∑ η ≤ 1`, then
`|F 1| ≤ C exp (2 - 2 π)`.

The bound is that of Schwarz's lemma for the extension of `F` along the complexified transvections
`1 - a (z - i) y y^* J`, `im z > 0`. As a function of `q = exp (2 π i z)` on the unit disc it is
bounded by `C exp 2`, vanishes at `0` and takes the value `F 1` at `q = exp (-2 π)`. 

### `New.Rows.ofMatrix_transvection_mem_Gamma`

 Let `m = 1 - p Y Y^* S`, with `Y` the adelic coordinates of a rational vector `y` and
`S = stdForm E s` the diagonal form of signs, preserve `S`. Then the element `ofMatrix m hm` of the
adelic unitary group is a rational point of the space `V` (a member of `V.Γ`). 

### `New.Rows.ofMatrix_transvection_snd_mem_principalLevel`

 Let `m = 1 - p Y Y^* S`, with `S = stdForm E s`, preserve `S`. If the finite components of `Y`
are integral (in `Ô E`), the finite part of `ofMatrix m hm` lies in the principal level `p`
(integral and congruent to `1` modulo `p`). 

### `New.Rows.IsPeak.le_firstMinimum`

 Peaks of a holomorphic form lie away from the cusp. The order `o` puts the signs `+1` first. Let
`F` on the adelic unitary group `G E s` be left invariant under the rational points `V.Γ` of the
space `V`. Let it be holomorphic at every translate (`IsAdelicHol`) of a weight `u` with gap `1`
(`u w i + 1 ≤ u w j` when `s i = 1`, `s j = -1`) and entries in `[-A, A]`, `A ≥ 2`. Let it be right
invariant under the principal level `p`, where `p = -p̄` and `im (Φ w p) ∈ (0, A']` for the
embedding `Φ w` at each infinite place `w`, `A' ≥ 1`. Then at a peak `g` of `F` (where `|F g|`
exceeds half the supremum of `|F|`), the first minimum of the moved space `V.move g` is at least
`(A A')^(-1/2)`. This first minimum is the length, in the norm of `archCoords`, of the shortest
nonzero vector of `baseLattice`, cut off at `1`. 
