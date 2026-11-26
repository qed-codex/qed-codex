---
{
  "module": "src/New/Determinant/Exchange/ConeImage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/ConeImage.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/ConeImage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The image of the cone integral

Let `W' = W ⊕ H` and `V' = V ⊕ H`, with adapted splittings and isotropic lines `A` and `B` in the
hyperbolic planes, and let the rank of `W` be even. For `0 < z`, every Schwartz vector `v` for
`(W, V)` has a Schwartz vector `v'` for `(W', V')` such that the cone integral of `v'` and `v` have
the same theta integrals on standard data (`exists_thetaLarge_cone_eq`). Up to a positive factor
that is analytic in `z`, one `v'` serves for all `z > 0` (`exists_thetaLarge_cone_eq_mul`). The
slices of this `v'` along `A` (its values in the mixed model attached to `A`, as a function of a
vector of `V'` at the infinite places) are `β x • k x v^B`, where `v` is the zero term of `v^B`
along `Hom(W, B)`, `β` is a bump function near the vector `x_B` that spans `B`, and the smooth
family `k x` carries `x_B` to `x` for isotropic `x` in the support of `β`.

In the code `A` and `X` are the splittings of `W'` and `V'` that define the two lines, the adelic
vector `x_B` that spans `B` is `X.kAdelic`, and `lineVector X w` is its component at the infinite
place `w`. The word real refers to the components at the infinite places of `E`.

* `PairFock E s t` is the Fock space of the pair with signs `s` and `t`; a vector is Schwartz
  (`IsSchwartzVector`) if all its weighted norms are finite.
* `realPairWeil γ γ'` is the Weil representation of the real points `GInf` of the two unitary groups
  on this space, with `(x, y)` twisted by `det y ^ γ * det x ^ (-γ')`.
* A splitting is adapted (`IsBaseAdapted`) if its adelic frames are orthonormal at the infinite
  places and integral at the finite places.
* `cone A X μ z v'` is the integral of `coneIntegrand A X μ true z v'` over the pairs `(κ, a)` of a
  point of the maximal compact subgroup `maxCompact E t'` of `U(V')` and a family of non-zero
  complex numbers indexed by the infinite places.
* `thetaLarge W V 𝔠 v Φ` is the theta integral over `[U(V)]` of the datum with real part `v` and
  component `Φ` at the ramified places of `𝔠`, as a function on `U(W)`.
* A `SplitTameChar E μ` is a tamely ramified character of weight `μ`, all `μ w > 0`, of the norm-one
  adeles, with a non-empty set of ramified places that contains no conjugate of one of its places;
  so the ramified places are split over the totally real subfield.

## Relation to the literature

See `New.Determinant.Exchange.TheoremForPartners` for related work.


### `lineVector_ne_zero`

 The component `lineVector X w` at an infinite place `w` of the vector `x_B` that spans the
isotropic line of the splitting `X` is non-zero. 

### `lineVector_isotropic`

 Let `X.kAdelic` be the adelic vector `x_B` that spans the isotropic line of the splitting `X`,
and `lineVector X w` its component at the infinite place `w`. This component is isotropic for the
Hermitian form with signs `t'`. 

### `maxCompactInf`

 The component at the infinite places of a point `κ` of the maximal compact subgroup of the
adelic unitary group for the signs `t'`. 

### `conePoint`

 The isotropic vector `κ⁻¹ x_B a` of `p = (κ, a)`, where `x_B` is the vector that spans the
isotropic line of `X`, with components `lineVector X w` at the infinite places `w`. It is written in
the coordinates of the slices along a line of the source: its entry at `(w, i, ())` is the `i`-th
entry at the infinite place `w`. 

### `conePoint_apply`

 Let `lineVector X w` be the component at the infinite place `w` of the vector `x_B` that spans
the isotropic line of `X`. The coordinates of `conePoint X (κ, a)` at `w` are those of
`κ⁻¹ x_B a`, that is of `a w • lineVector X w` multiplied by the inverse of `κ` at `w`. 

### `maxCompact_fst_mem_maxCompactU`

 A point of the adelic maximal compact subgroup is a unitary matrix at each infinite place. 

### `sum_norm_sq_conePoint`

 Let `x_B` be the vector that spans the isotropic line of the splitting `X` of `V'`, with
components `lineVector X w`, so that `conePoint X (κ, a)` is `κ⁻¹ x_B a`. A point `κ` of the
maximal compact subgroup of `U(V')` keeps lengths: at each infinite place `w`, the squared length
of `κ⁻¹ x_B a` is `‖a w‖ ^ 2` times that of `x_B`. 

### `realSlice_eq_slice_conePoint`

 Let `A` be an adapted splitting and `x_B = X.kAdelic` the adelic vector that spans the isotropic
line of `X`, with components `lineVector X w` at the infinite places. Here `realSlice A V'` sends a
vector for `(W', V')` to its value, a vector for `(W, V')`, at a given adelic vector of `V'` in the
mixed model attached to `A`. For `κ⁻¹ x_B a`, with `κ` replaced by its infinite component and `a`
extended by `0` at the finite places, this is the slice of that mixed model at the point
`conePoint X (κ, a)`, the coordinates of `κ⁻¹ x_B a` at the infinite places. 

### `hasCompactSupport_of_norm_sq_mem_Icc`

 A function `ρ` of `(κ, a)`, with `κ` in `maxCompact E t'`, that vanishes unless
`1 / 2 ≤ ‖a w‖ ^ 2 ≤ 2` at every infinite place `w`, has compact support. 

### `HasPosMellinTransform`

 A real function `ρ` of the pairs `p = (κ, a)` has a positive Mellin transform if for all real
`z` the integral of `ρ (κ, a) |a| ^ z` converges and is positive. Here `|a|` is the module of the
idele that is `a` at the infinite places and `1` elsewhere. 

### `HasPosMellinTransform.integrable`

 The integral of `ρ (κ, a) |a| ^ z` converges. 

### `HasPosMellinTransform.integral_pos`

 The integral of `ρ (κ, a) |a| ^ z` is positive. 

### `HasPosMellinTransform.mul_sqrt_pow`

 Let `ρ` have a positive Mellin transform: for all real `z` the integral of `ρ (κ, a) |a| ^ z`
converges and is positive. Then `(κ, a) ↦ ρ (κ, a) |a| ^ (m / 2)` has one too: the factor shifts the
exponent by `m / 2`. 

### `hasPosMellinTransform_comp_conePoint`

 Let `x_B` be the vector that spans the isotropic line of the splitting `X`, with components
`lineVector X w`, so that `conePoint X (κ, a)` is `κ⁻¹ x_B a` for `κ` in the maximal compact
subgroup `maxCompact E t'` of `U(V')`. Let `β ≥ 0` be continuous, non-zero at `x_B`, and zero unless
the squared length at each infinite place is within a factor `2` of that of `x_B`. Then for all real
`z` the integral of `β (κ⁻¹ x_B a) |a| ^ z` over the pairs `(κ, a)` converges and is positive. 

### `exists_hasPosMellinTransform_mulVec_eq_smul`

 Let the splitting `X` of `V'` define the isotropic line spanned by `x_B`, with components
`lineVector X w`, and write `conePoint X (κ, a) = κ⁻¹ x_B a` for `κ` in the maximal compact subgroup
of the unitary group `U(V')`. There are a smooth compactly supported function `β` and a smooth
family `k x` of real points of `U(V')` such that `ρ (κ, a) = β (κ⁻¹ x_B a)` has a positive Mellin
transform and, for `x = κ⁻¹ x_B a` with `β x ≠ 0`, the point `κ * k x` multiplies `x_B` by `a` at
each infinite place. 

### `exists_slice_eq_smul_realPairWeil`

 Slices along an adapted splitting `A` can be prescribed: for `β` smooth of compact support, a
smooth family `k x` of real points of `U(V')` and a Schwartz vector `v` for `(W, V')`, some Schwartz
vector `v'` for `(W', V')` has the slice `β x • k x v` at every `x`. 

### `exists_coneIntegrand_eq_smul`

 Let the splittings `A` and `X` be adapted and the rank of `W` even. There is a function `ρ` of
`(κ, a)` such that `ρ (κ, a) |a| ^ z` has a positive integral for all real `z`, with the following
property. Each Schwartz vector `v` for `(W, V)` has a Schwartz vector `v'` for `(W', V')` such that
the integrand `coneIntegrand A X μ true z v'` of the cone integral of `v'`, with weight `μ` and
exponent `z`, is at each `(κ, a)` the multiple `ρ (κ, a) |a| ^ z` of a translate of `v` by a real
point `h` of `U(V)`. 

### `thetaLarge_realPairWeil`

 The theta integral `thetaLarge W V 𝔠 v Φ`, a function of a point `g` of `U(W)`, is the integral
over `[U(V)]` for the datum with real part `v` and component `Φ` at the ramified places of `𝔠`. It
does not change when a real point `h` of `U(V)` acts on `v` by the Weil representation twisted by
`det ^ targetWeight n μ`, where `targetWeight n μ w = ⌊#n / 2⌋ - μ w`. Here `𝔠` is a split tame
character: a tamely ramified character of weight `μ`, with all `μ w > 0`, of the norm-one adeles,
whose non-empty set `𝔠.ramifiedPlaces` of ramified places contains no conjugate of one of its
places, so that these places are split. `Φ` is a function on the matrices over the product of the
completions at these places. 

### `exists_thetaLarge_cone_eq_mul`

 Let `A` and `X` be adapted splittings `W' = W ⊕ H` and `V' = V ⊕ H` with `H` a hyperbolic plane,
let the rank of `W` be even, and let `σ` identify `b ⊕ r` with the index set of `W`. There is a
positive analytic function `B` on the real line such that each Schwartz vector `v` for `(W, V)` has
a Schwartz vector `v'` for `(W', V')` with this property: for all `z > 0`, the theta integrals over
`[U(V)]` of `cone A X μ z v'` are `B z` times those of `v`. This holds at every adelic point `g` of
`U(W)`, for every character `𝔠` of weight `μ` (all `μ w > 0`) of the norm-one adeles that is tamely
ramified exactly at a non-empty set of split places, containing no place together with its
conjugate, and for every standard datum `stdRowDatum σ 𝔠.semilocalChar y` at these places. 

### `exists_thetaLarge_cone_eq`

 Let the splittings `A` and `X` be adapted, the rank of `W` even and `0 < z`, and let `σ`
identify `b ⊕ r` with the index set of `W`. Each Schwartz vector `v` for `(W, V)` has a Schwartz
vector `v'` for `(W', V')` such that the cone integral `cone A X μ z v'` and `v` have the same theta
integrals over `[U(V)]`, at every adelic point `g` of `U(W)`. This holds for every split tame
character `𝔠` of weight `μ`, that is a character of the norm-one adeles, tamely ramified exactly at
a non-empty set of split places that contains no place together with its conjugate, and for every
standard datum `stdRowDatum σ 𝔠.semilocalChar y` at these places: the function that sends `x` to
`𝔠.semilocalChar⁻¹` of the determinant of the matrix with rows `y` and `x`, ordered by `σ`, if that
matrix is integrally invertible, and to zero otherwise. 
