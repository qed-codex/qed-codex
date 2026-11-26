---
{
  "module": "src/New/Spanning/Bessel/FillingData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/FillingData.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/FillingData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Filling data from admissible data, with Bessel systems at the real places

The filling theorem is stated for abstract data (`New.Filling`). This file builds such data from
admissible data D (`New.Data`). At each real place it constructs a Bessel system of the type fixed
by D. It then assembles these systems, the relevant primes and places, and the level `D.levelX 0`
into the filling data. It identifies that level with the preimage of the level K(M) of
`New.Filling.principalLevel`: here M = p₀ p₁, and K(M) includes a congruence modulo π.

## Main definitions and results

* `New.Data.exists_besselSystem`: the Bessel function at a real place, with its normalisation,
  Schur's bound, decay, cut and local bounds. That its coordinates are orthonormal is
  `New.BesselSystem.orthonormal`, in `New.Spanning.Bessel.Orthonormality`.
* `New.Data.filling`: the prime `New.Data.N`, the primes p₀, p₁ (field `levelPrime`) with their
  chosen places, the level `D.levelX 0` and a Bessel system at each infinite place.
* `New.Data.levelX_zero_eq_comap`: the level `D.levelX 0` is the preimage of the principal
  congruence subgroup K(M), that is `New.Filling.principalLevel`.

Notions from other files:
* `New.Data.piNIdele`: the principal finite idele of `π`, where `N = π π̄`; `New.Data.piNPlaces` is
  the set of places dividing `π`.
* `New.Data.piM`: the conjugate of the integer `D.piMBar` of norm `p₀ p₁`; the chosen places are its
  prime divisors.

## Relation to the literature

At a real place, integrals of a Bessel function on an indefinite unitary group against its
translates have Fourier transforms decaying beyond a band; the bounds themselves are proved in the
imported files. These integrals replace Petersson's J-Bessel kernel in showing that few translates
almost span the target forms. Rank one is classical, and Bessel kernels are studied for GL(n) and
GSp(4).

Related work: Petersson, Über die Entwicklungskoeffizienten der automorphen Formen, 1932; NIST DLMF
§10.22; Baruch, Bessel distributions on the open cell, 2001–2004; Comtat et al., Effective Kuznetsov
trace formula for GSp(4), 2025.



## Bessel systems at the real places

The Bessel function at each real place is built at a stationary point given by
`New.DiscreteSeries.IsSteep.exists_stationary_point`.


### `unitarySignFrameY`

 An orthonormal frame with the signs of `Y₀`. 

### `exists_unitary_schur_rep`

 The Schur matrices of weight `w`, written in an orthonormal basis for their Gram form, give a
continuous unitary representation of U(n), with n = `𝔰.κ`, which is conjugate to the transposed
Schur matrices of transposes and is irreducible: only scalars commute with it. If `u` is the
Harish-Chandra parameter of the weight `w`, then `dsCoeff`, the coefficient attached to `u`, is a
diagonal matrix coefficient of it, seen as operators by `besselValueRep`. 

### `weylDimensionPoly_paramW_le`

 If the parameter `D.paramW v` of the discrete series at the place `v` has entries of size at
most `3 a`, then Weyl's dimension polynomial at it is at most `b ^ (2 r ^ 2)`, where `a` and `b` are
the size parameters of D and `r` is the number of its row indices. 

### `volU_div_volU_le`

 The quotient of the volumes of U(k) and U(r) is at most `(b ^ r) ^ r`, where `k` and `r` are the
rank of X₀ and the number of row indices of D, and `b` is its size parameter. 

### `scaledVolumeRatio_le`

 The constant `scaledVolumeRatio` of the local bounds for the shape of D is at most
`b ^ (2 r ^ 2)`, where `b` is the size parameter of D and `r` the number of its row indices. 

### `weylDimensionPoly_mul_scaledVolumeRatio_le`

 If every entry `D.paramW v i` has absolute value at most `3 * D.a`, then Weyl's dimension
polynomial at `D.paramW v`, times the constant `D.shape.scaledVolumeRatio` of the local bounds, is
at most `D.b ^ (4 r ^ 2)`, where `r = D.shape.r` is the rank of G₁. 

### `abs_paramW_le`

 The entries of `D.paramW v`, twice the Harish-Chandra parameter at the place `v` of the discrete
series on G₁, have absolute value at most `3 a`, where `a = D.a` is a size parameter of D. 

### `exists_lowestKType_eq_ite`

 Let `u ()`, indexed by the basis `D.shape.κ` of X₀, list twice the Harish-Chandra parameter of
the weight on the compact group U(X₀) that has `D.columnCount v h` columns of height `h` for each
`h` below the rank. Then the highest weight `lowestKType` attached to `u ()` is `D.columnCount v 1`
at one index `i` and `0` at the others, and the entries of `u ()` have absolute value at most
`3 * D.a`. Here the natural number `D.a` is a size parameter of the data D, the product
`D.natX * D.natB`. 

### `realPlaceSizes`

 The size inequalities `Floors.RealPlaceSizes`, under which cut Bessel functions have local
bounds, hold for `D.shape` with box radius `b ^ (6 n + 2)`, exponent `k - (3 n + 6)` and base
`b = D.b`. Here `D.shape` describes the hermitian space Y₀, the sum of some hyperbolic planes, a
space X₀ and a line; `n = D.shape.n` is the number of planes plus one and `k = D.shape.k` is the
rank of X₀. 

### `exponent_add_le_mul_sq_r`

 An inequality of exponents of `b = D.b`, where `r` and `k` are the ranks of G₁ and U(X₀): the
loss `3 * (20 * (r + k) ^ 2)` in the lower bound for the period and the further `99 r ^ 2` allowed
for cutting the Bessel function add up to at most `400 r ^ 2`. 

### `liftWeight_add_columnCount_le`

 At an infinite place `v`, three times `D.liftWeight 0 v`, which is the weight of the character
of the lift of index `0` (the first one), plus the number `D.columnCount v 1` of columns of height 1
in the weight on X₀ is at most `b ^ 2`, where `b = D.b` is the size parameter of D. 

### `rank_add_le_cube`

 The ranks `r` of G₁ and `k` of U(X₀) and the bound `3 a` on the entries of the parameters
`D.paramW v` add up to at most `b ^ 3`, where `a` and `b` are the size parameters of D. 

### `rank_sq_mul_log_le`

 For the ranks `r` of G₁ and `k` of U(X₀) and the size parameter `b` of D, the number `r ^ 7`,
which bounds from below the gaps of the Harish-Chandra parameters at the real places, is at least
`10 ^ 30` times the cube of `(r + k) ^ 2 log (b ^ 3)`. 

### `_root_.New.IsBesselFunction.integral_dsKernel_mul_eq_of_convolve_eq`

 Let `l` be a parameter of large gap, with coefficient `c_l` on G₁ and formal degree `deg`. If a
Bessel function `F` is fixed by convolution with `deg * c_l`, then each coordinate of `F` is fixed
by right convolution with the kernel `l.dsKernel`, carried over from `USign ε` by the frame. 

### `exists_besselSystem`

 **Bessel functions at a real place**: for each infinite place `v : D.Φ` of the field of `D`
there is a Bessel system `B : BesselSystem D.shape D.b D.f`. Such a system is a full Bessel function
on the group G₁, the unitary group of the hermitian form of the shape `D.shape`, together with a cut
version of bounded support, and the two satisfy the bounds listed in `BesselSystem`. It is built for
the shape `D.shape` of the hermitian space Y₀ of `D`, with size parameter `D.b`, and the number
`D.f` of infinite places sets the rate of decay. Its type (`IsDiscreteSeriesBessel`) is
`(D.paramW v, D.columnCount v)`: the doubled parameter of the discrete series whose Bessel function
is the full function, and the numbers of columns of each height in the weight of the representation
on the values. 

### `natCast_levelPrime_dvd_iff`

 The prime `D.levelPrime i` divides an integral finite adele `r` (an element of `Ô D.E`) iff the
component of `r` has valuation less than 1 at each chosen place `w` above that prime (the type
`D.ChosenPlace i`) and at the conjugate place `star w`. 

### `filling`

 The filling data `New.Filling` attached to the admissible data D. They record the prime N, the
idele of π (in the field `piN`), the primes p₀, p₁ with chosen places, `deltaE`, and Bessel systems
chosen from `New.Data.exists_besselSystem`. The type of the chosen systems is stated in
`New.Data.isDiscreteSeriesBessel_filling_besselSystem`. 

### `isDiscreteSeriesBessel_filling_besselSystem`

 The Bessel system of `D.filling` at the infinite place `v` has type
`(D.paramW v, D.columnCount v)`: its full function is the Bessel function of the discrete series of
parameter `D.paramW v`, with values in the representation of U(X₀) of weight `D.columnCount v`. 

### `levelX_zero_eq_comap`

 The level of index `0`, `D.levelX 0`, is a level on the first hermitian space X₀ of the sequence
X_j of D. It is the preimage, under the embedding `inclHFin` of the finite adelic points of U(X₀) in
those of U(Y₀), of `New.Filling.principalLevel`, the level K(M) of the elements that satisfy the
congruence modulo π and reduce to 1 at the chosen places. 
