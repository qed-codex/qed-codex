---
{
  "module": "src/New/Determinant/Exchange/NegativeIndices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/NegativeIndices.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/NegativeIndices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Theta coefficients vanish off negative forms

This file finds a unit vector, supported on the negative signs, that kills the columns of a
frame. The rotations of its line lie in the maximal compact subgroup of `U (signMatrix s)`. It
shows that a polynomial whose Fock vector is fixed by the compact stabiliser of the frame is zero.
It proves that right translation by an element of a compact subgroup preserves the left Haar
measure. Here `New.Exchange.negCount s` is the number of signs `-1`.

## Main definitions and results

* `New.Exchange.centreCoeff_eq_zero_of_not_representedBy`: a Fourier coefficient of the theta
  integral `New.Exchange.thetaIntegral` vanishes, under conditions on weights, signs and
  integrability, at an invertible form that fails to be negative definite at some real place. After
  unfolding, the coefficient is an integral modulo the stabiliser of a frame, and the mean of the
  integrand over a compact subgroup is an invariant functional on Fock space, which is zero.
* `New.Exchange.apply_eq_zero_of_forall_fixed_eq_zero`: let a compact group act by bounded operators
  `ρ g` on a Banach space, and let `W` be a stable subspace of finite dimension in which only `0` is
  fixed. Then an invariant bounded functional `l` vanishes at every vector of `W` with continuous
  orbit: the mean of the orbit is a fixed vector of `W`.

Notions from other files:
* `thetaIntegral S T α β f`: the integral over `[U(T)]` of the theta kernel of the datum `f`.
* `PairFock E s t`, `realPairWeil`: the Fock space of the pair and its real Weil representation.

## Relation to the literature

See `New.Determinant.Exchange.TheoremForPartners` for related work.


### `New.Exchange.exists_unitary_mulVec_eq_single`

 Let `s` be a vector of signs and `U (signMatrix s)` the unitary group of the diagonal Hermitian
form with entries `s` (`u.val.val` is the matrix of `u`). If the Gram matrix of the columns of `x`
for this form is not of the form `-cᴴ * c` for any `c`, then some element of the group carries a
vector in the span of the columns to the positive basis vector `i`. 

### `New.Exchange.exists_unit_dotProduct_col_eq_zero`

 Let `s` have `card b` more negative signs than `t`, and let the positive basis vector `i` be in
the span of the columns of `x`. There is a unit vector `r`, supported on the negative signs of `s`,
that kills the columns of `x` and the columns `j` of `y` with `t j = -1`. 

### `New.Exchange.exists_mem_maxCompactU_eq_rotation`

 Let `s` be a vector of signs and `U (signMatrix s)` the unitary group of the diagonal Hermitian
form with entries `s`; its maximal compact subgroup `maxCompactU s` consists of its elements that
are also unitary for the standard form. Let `r` be a unit vector supported on the negative signs,
and `|η| = 1`. The rotation by `conj η` of the line of `star r` lies in `maxCompactU s`. 

### `New.Exchange.mulSingle_mem_blockDiagAlg`

 An element of the maximal compact subgroup, placed at `τ`, is block diagonal at every place. 

### `New.Exchange.realPairWeil_rotation_polyVector`

 Let `c` be the rotation by `conj η`, `|η| = 1`, of the line of `star r`, for a unit vector `r`
supported on the negative signs of `s`. Placed at `τ`, it acts on the vector of `P` by a
substitution times `η ^ N`, where `N` is the number of positive signs of `t` minus `μ τ`. For each
`j` the substitution multiplies `∑ i, conj (r i) • X (τ, i, j)` by `conj η` if `t j = -1`, and
`∑ i, r i • X (τ, i, j)` by `η` if `t j = 1`. It fixes the combinations of the `X (τ, i, j)`
orthogonal to these, and all variables at other places. 

### `New.Exchange.eval_eq_zero_of_rotation_fixed`

 Let `μ τ` be less than the number `negCount (-t)` of positive signs of `t`, and let `r` be a
unit vector supported on the negative signs of `s`. If the elements `1 + δ • star r rᵀ` of the
maximal compact subgroup `maxCompactU s`, placed at `τ` (`mulSingle`) and `1` elsewhere, fix the
vector of `P`, then `P` vanishes at every point `z` at which the variables
`∑ k, conj (r k) • X (τ, k, j)` with `t j = -1` vanish. 

### `New.Exchange.apply_eq_zero_of_forall_fixed_eq_zero`

 Let a compact group act by bounded operators `ρ g` on a Banach space, and let `W` be a stable
subspace of finite dimension in which only `0` is fixed. Then an invariant bounded functional `l`
vanishes at every vector of `W` with continuous orbit: the mean of the orbit is a fixed vector of
`W`. 

### `New.Exchange.eq_zero_of_stabilizer_fixes_polyVector`

 Let the weight `μ τ` be less than the number `negCount (-t)` of positive signs of `t`. Let `s`
have `card b` more negative signs than `t`, and let the positive basis vector `i` be in the span of
the columns of `x`. Suppose every `c` in `maxCompactU s` with `c * x = x`, placed at `τ` and acting
by `realPairWeil μ 0`, fixes the Fock vector `polyVector` of a polynomial `P`. Then `P = 0`. 

### `New.Exchange.realPairWeil_mulSingle_mem_map_homogeneousSubmodule`

 An element `c` of the maximal compact subgroup, placed at `τ`, maps the Fock vector of a
homogeneous polynomial of degree `d` to the Fock vector of another such polynomial. 

### `New.Exchange.exists_isometry_fock_functional_eq_zero`

 Let the weight `μ τ` be less than the number `negCount (-t)` of positive signs of `t`. Let `s`
have a positive sign, and `card b` more negative signs than `t`. Let the Gram matrix of the columns
of `x` not be of the form `-cᴴ * c`. For some isometry `u` at the place `τ`, a functional on Fock
space that is invariant under the compact stabiliser of `u * x`, acting by the real Weil
representation of weight `μ` (`realPairWeil`), is zero. 

### `New.Exchange.haar_map_mul_right_of_isCompact`

 Right translation by an element of a compact subgroup preserves the left Haar measure of a
locally compact group: the modular function is `1` on compact subgroups. 

### `New.Exchange.integral_theta_pairWeil_stabilizer_eq_zero`

 Let `C` be the elements of the stabiliser of an adelic frame `x'` that lie in the conjugate of
`maxCompact E s` by `u⁻¹` at the real place `τ`, with an invariant probability measure `κ`. Suppose
that only the zero functional on Fock space is invariant, for the weight `μ` of `ν`, under the
compact stabiliser of `u x'` at `τ`. Then the theta functional `θ` of the Weil representation with
characters `ν`, `δ` has mean zero over `k C u⁻¹`. 

### `New.Exchange.homSlice_pairWeil_stabilizer_mul`

 Let the splitting `D` write `X` as the sum of two dual isotropic subspaces of rank `#b` and of
`Z`, orthogonal to both. The slice at `x'` (`D.homSlice`) is the map from data on `Hom(X, Y)` to
data on `Hom(Z, Y)` that takes the value `x'` on one of the two subspaces. An element `k` of the
stabiliser of `x'` in `U(Y)` commutes with it: on the slice it acts by the Weil representation of
the smaller pair `(Z, Y)`, with the character `ν` if `δ = ν υ ^ #b`, for `υ` the character
`upsilonU1` of the Weil data. 

### `New.Exchange.centreCoeff_eq_zero_of_not_representedBy`

 The spaces `X`, `Y`, `Z` are Hermitian over `E` with Weil data `H`: a splitting Hecke character
`υ`, whose restriction to the norm-one ideles is `H.upsilonU1`, and a scalar `H.j` of `E` with
`conj j = -j`. Let the splitting `D` write `X` as the sum of two dual isotropic subspaces of rank
`#b` and of `Z`, orthogonal to both. (a) The weights `μ τ` are less than the number of positive
signs of `Z`; `Y` has a positive sign, and `#b` more negative signs than `Z`. (b) `ν` has weight
`μ`, with any tame part `ψ`, and `δ = ν H.upsilonU1 ^ #b`. (c) `T` is invertible and, at some real
place, not of the form `-cᴴ c` (`RepresentedBy` fails). (d) The sum over the rational frames of the
absolute values of the terms of the unfolded theta integral is integrable (`HasIntegrableTerms`).
The theta integral `thetaIntegral X Y δ δ f` integrates the kernel of `f` over `[U(Y)]`, in the Weil
representation of `(X, Y)` in which `δ` is the character of `U(1)` for both spaces: the first fixes
the action of `U(Y)`, the second that of `U(X)`. Then `centreCoeff` at `H.j • T` of this function on
`U(X)`, its Fourier coefficient along the centre of the unipotent radical of `D`, vanishes at `g`.

