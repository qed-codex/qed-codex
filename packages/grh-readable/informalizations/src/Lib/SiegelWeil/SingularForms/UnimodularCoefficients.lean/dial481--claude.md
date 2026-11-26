---
{
  "module": "src/Lib/SiegelWeil/SingularForms/UnimodularCoefficients.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/SingularForms/UnimodularCoefficients.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/SingularForms/UnimodularCoefficients.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Singular forms governed by unimodular coefficients

The file first computes how conjugation scales Haar measure on the hermitian `1 × 1` matrices, which
parametrise the centre of the unipotent radical of the stabiliser of an isotropic line. Its main
result, after Freitag, concerns an automorphic function `f` that is right invariant under the
integral points supported on `S ∪ S̄` and whose partial means along extra isotropic lines are
invariant under shears; `S` is a set of finite places away from the level of `f`. Suppose the
Fourier coefficient of `f` at an invertible `T` vanishes at the points that act on the frame by a
matrix `γ` on `S ∪ S̄` and by `1` elsewhere, where the normalised index `δ⁻¹ γᴴ T γ` is unimodular
on `S ∪ S̄` and `δ = ȷκκ̄`. Then this coefficient vanishes at all points that fix the frame off
`S ∪ S̄`. Lattices on `S ∪ S̄` are given by matrices `γ` whose columns span them.

## Main definitions and results

* `New.Exchange.closurePart`: the endomorphism that keeps the components on `S ∪ S̄` and replaces
  all others by 1.
* `New.Exchange.StraightPoint`, `New.Exchange.exists_straightPoint`: points whose lattice splits
  along the two isotropic lines, and the straightening of a point by singularity.
* `New.Exchange.centreCoeff_eq_zero_of_unimodular`: the vanishing theorem.

Notions from other files:
* `New.Space.Splitting`: a decomposition of a hermitian space into two dual isotropic frames k, l
  and an orthogonal complement with inclusion ι and form ε₀; `A.symm` exchanges k and l, and
  `A.comp B` has the frame (k_A, ι_A k_B).
* `New.Space.Splitting.radicalElement`: For adelic c (n₀×p, where n₀ indexes the complement) and b
  (p×p), the element of G with k ↦ k, ι ↦ ι + kc*ε₀, l ↦ l − ιc − k(½ȷ⁻¹(b + b*) + ½c*ε₀c).
* `New.Space.Splitting.lineShift`: n₊(a) = `A.lineShift B a` shifts the isotropic vector u of A to
  u − ι k_B aᴴ; n₋(b) = `A.symm.lineShift B b` shifts that of `A.symm`.
* `IsBaseAdapted`: the frames of a splitting are orthonormal at the infinite places and integral at
  the finite ones. `stdLevel E n` consists of the points that are integral at the finite places.
* `New.Space.Splitting.partialMean`, `New.Space.Splitting.shiftedMean`: f⁺(g) is the mean over b of
  the coefficient of f along D at T at n₋(b) g, and φ⁺_g(a) = f⁺(n₊(a) g); f⁻ and φ⁻ are those for
  `A.symm`.
* `New.Space.Splitting.frameStabilizer`: the points that fix a given multiple of the frame of D.
* `New.WeilData`: Weil data on a stably unramified E. They consist of ȷ in E with ȷ = −ȷ̄, Im τȷ > 0
  for every τ in the CM type and (1 − ȷ⁻¹)/2 integral; a finite idele α for which the completed
  integers Ô are self-dual under (z, u) ↦ ψ_f(ȷαᾱzu); and a splitting character υ equal to −1 at
  uniformisers of the places w with w = w̄.

## Relation to the literature

Known result: Singular forms are governed by their coefficients at unimodular indices. Here the
setting is adelic, unitary and not holomorphic, and singularity comes from invariance under shears
at a nonempty set of places. The result here is the vanishing criterion
`centreCoeff_eq_zero_of_unimodular`, proved by choosing a point at which the denominator of the
inverse determinant of the index is least. Source: E. Freitag, Singular Modular Forms and Theta
Relations, Lecture Notes in Math. 1487, Springer 1991; see also J.-S. Li, Automorphic forms with
degenerate Fourier coefficients, Amer. J. Math. 119 (1997).

The tower property for the constant term of a theta lift along an isotropic line is in
`Lib.SiegelWeil.Tower.LargeSideConstantTerm`.


 ## Haar measure on the centre of the radical of an isotropic line 

### `map_conjugate_selfAdjoint`

 Let `μ` be a Haar measure on the hermitian `1 × 1` matrices over the adeles, and let `a` be
invertible. The push-forward of `μ` under `x ↦ a x a*` is `μ` scaled by the inverse of the idelic
absolute value of `det a`. 


## Singular forms and unimodular coefficients

The proof takes a point with the least value of a subgroup index that measures how far the
determinant of the normalised index is from a unit.


### `closureIntegers`

 The ring of adeles that are integral at the places of S ∪ S̄. 

### `closurePart`

 The endomorphism of the adelic unitary group that keeps the components on S ∪ S̄ and
replaces all others by 1. 

### `snd_idemAdele_conjClosure_mul_mul`

 Taking the part on S ∪ S̄ of an adele, as a finite adele, is multiplicative. 

### `adeleMatrix_closurePart`

 The matrix of `closurePart S g` is that of `g` on S ∪ S̄ and the identity elsewhere. 

### `invDifferentIdele`

 The idele ȷκκ̄, with κ = `New.WeilData.scaleIdele`; its finite part is ȷαᾱ. 

### `siegelBracket`

 Siegel's T[γ] = γᴴTγ for a matrix T over E, read in the adeles, and an adelic matrix γ, divided
by the idele δ = ȷκκ̄ (`New.Exchange.invDifferentIdele`). 

### `closurePart_radicalElement`

 The part `closurePart S` on S ∪ S̄ of an element of the unipotent radical is the element whose
parameters are multiplied by the adele that is 1 on S ∪ S̄ and 0 elsewhere. 

### `closurePart_radicalCentre`

 The part `closurePart S` on S ∪ S̄ of an element `D.radicalCentre M` (matrix
`1 + D.kAdelic * (M - Mᴴ) * D.lCoord`, so only `M - Mᴴ` matters) of the centre of the unipotent
radical is the element whose parameter is multiplied by the adele that is 1 on S ∪ S̄ and 0
elsewhere. 

 ### Fourier coefficients 

### `stdAddChar_idemAdele_mul`

 On the adeles supported on S ∪ S̄, the standard character at δx is the character
`selfDualAddChar E : z ↦ ψ_f(ȷαᾱz)` of the finite adeles at x, for the idele δ = ȷκκ̄. 

### `centreCoeff_mul_radicalCentre`

 Let `f` be an automorphic function, let `X` agree on `S ∪ S̄` with a point `g` that acts on the
isotropic frame of `D` by `c`, and let `D.radicalCentre M`, whose matrix is
`1 + D.kAdelic * (M - Mᴴ) * D.lCoord`, be an element of the centre of the unipotent radical. Right
translation of `X` by the part on `S ∪ S̄` of this element divides the Fourier coefficient at `T` by
the value of the character `selfDualAddChar E : z ↦ ψ_f(ȷαᾱz)` of the finite adeles at the part on
`S ∪ S̄` of `tr (M * siegelBracket T c)`. Here `siegelBracket T c = δ⁻¹ cᴴ T c`. 

 ### The index of a lattice in its dual 

### `denomIndex_lt_of_mul_mem_of_mul_notMem`

 The denominator of a finite adele `a` (the index in `Ô` of the group of the `x` with `a x ∈ Ô`)
is smaller than that of `b`, if `a = u b` with `u ∈ Ô` and some `y ∈ Ô` has `a y ∈ Ô`, `b y ∉ Ô`. 

### `dualIndex`

 The denominator (`denomIndex`, an index of subgroups of `Ô`) of the part on `S ∪ S̄` of the
determinant of the inverse of `siegelBracket T γ = δ⁻¹ γᴴ T γ`. If `siegelBracket T γ` is
invertible and integral on `S ∪ S̄`, this is the index there of the lattice spanned by `γ` in its
dual. 

### `dualIndex_lt_dualIndex_mul_of_det_inv_notMem`

 Let `siegelBracket T γ` (the matrix `γᴴ T γ` divided by the idele `invDifferentIdele E`) and `r`
be integral on `S ∪ S̄`, let `siegelBracket T (γ * r)` be invertible, and let the inverse of `det r`
not be integral on `S ∪ S̄`. Then passing from `γ` to `γ * r` raises `dualIndex`, the denominator of
the part on `S ∪ S̄` of `(siegelBracket T γ)⁻¹.det`. 

 ### Points that agree on `S ∪ S̄` 

### `AgreesOnClosure`

 The point `X` agrees with `g` on `S ∪ S̄` and fixes the isotropic frame of `D` elsewhere. 

### `AgreesOnClosure.closurePart_eq`

 `X` and `g` have the same components on `S ∪ S̄`. 

### `AgreesOnClosure.mem_frameStabilizer`

 `X` fixes the frame of `D` off `S ∪ S̄`. 

### `AgreesOnClosure.closurePart_self`

 The part of `g` on `S ∪ S̄` agrees with `g` on `S ∪ S̄` and fixes the frame of `D` elsewhere. 

### `mem_frameStabilizer_of_mem_supportedOn`

 A point supported on `S ∪ S̄` fixes the frame of `D` off `S ∪ S̄`. 

### `AgreesOnClosure.mul`

 If `X`, `Y` agree with `g`, `k` on `S ∪ S̄` and fix the frame of `D` elsewhere, then `X * Y`
does so with respect to `g * k`. 

### `AgreesOnClosure.lineShift_mul`

 Let the frame of `D` be that of `B` inside the complement of the plane split off by `A`. If `X`
agrees with `g` on `S ∪ S̄` and fixes the frame of `D` elsewhere, then so does n₊(a) X with respect
to n₊(a) g, for the shift n₊(a) = `A.lineShift B a`. 

### `AgreesOnClosure.actsOnFrame`

 If `X` agrees on `S ∪ S̄` with a point `g` that acts on the frame `k` of `D` by `γ` (that is,
`g k = k γ`), and fixes the frame elsewhere, then `X` acts on the frame by `γ` on `S ∪ S̄` and by
`1` elsewhere. 

 ### Integrality 

### `isUnit_det_siegelBracket`

 If `T` and `γ` are invertible, then so is `siegelBracket T γ = δ⁻¹ γᴴ T γ`. 

### `invDifferentIdele_mul_siegelBracket_apply`

 For invertible `γ`, a column `x`, a row `b` and a scalar `t`, the pairing `tr (T (γ x tᴴ) b)` is
δ times the value of the form `siegelBracket T γ = δ⁻¹ γᴴ T γ` at the columns `γ⁻¹ bᴴ t` and `x`. 

### `centreCoeff_mul_closurePart`

 Let `f` be right invariant under the integral points supported on `S ∪ S̄`, and let `k` be
integral at the finite places. Right translation by the part of `k` on `S ∪ S̄` does not change the
Fourier coefficients of `f` along `D`. 

### `isIntMatrix_siegelBracket`

 Let `f` be automorphic and right invariant under the integral points supported on `S ∪ S̄`. Let
the splittings `A`, `B` be adapted to the integral structure, and let the frame of `D` be that of
`B` inside the complement of the plane split off by `A`. Let `X` have the same components on
`S ∪ S̄` as a point `u` that acts on the frame of `D` by `γ`. If the Fourier coefficient of `f`
along `D` at `T` is not zero at `X`, then Siegel's bracket `siegelBracket T γ = δ⁻¹ γᴴ T γ` has
entries integral at the places of `S ∪ S̄`, where δ = ȷκκ̄ is the idele `invDifferentIdele`; that
is, the lattice spanned by the columns of `γ` lies in its dual for the form δ⁻¹ T. 

### `isIntMatrix_closureIntegers_of_actsOnFrame`

 If a point `k` that is integral at the finite places acts by `a` on the frame of a splitting `D`
adapted to the integral structure, then `a` is integral on `S ∪ S̄`. 

 ### Iwasawa blocks 

### `exists_mem_stdLevel_actsOnFrame_fromBlocks`

 Iwasawa decomposition for the flag of `A.comp B`: every `g` has a right translate `g * κ`, with
`κ` integral at the finite places, that acts on the frame by a block upper triangular matrix. 

### `exists_eq_radicalElement_mul_actsOnFrame`

 Let `g` act on the frame of `A.comp B` by a block upper triangular matrix with last block `γ`.
Up to the unipotent radical of `A`, `g` is an element `u` that acts on the frames of `A.comp B` and
`A.symm.comp B` by block diagonal matrices `t ⊕ γ` and `t' ⊕ γ` with `t'ᴴ t = 1`. 

### `dualIndex_lt_of_actsOnFrame`

 Let the splittings `A`, `B` be adapted to the integral structure, let `h` act on the frame of
`A.comp B` with upper right block `0` and lower blocks `x`, `γ`, and let `h * κ`, with `κ` integral
at the finite places, act by a block upper triangular matrix with last block `γ'`. If
`siegelBracket T γ'` is integral on `S ∪ S̄`, `γ` and `siegelBracket T γ` are invertible and
`γ⁻¹ * x` is not integral on `S ∪ S̄`, then `dualIndex` (the denominator on `S ∪ S̄` of the
determinant of the inverse of `siegelBracket T γ`) is smaller for `γ'` than for `γ`. 

 ### Straight points 

### `StraightPoint`

 A straight point for the plane split off by `A`: a point that fixes the frame of `D` off
`S ∪ S̄` and agrees on `S ∪ S̄` with a point `u` = `blockPoint` that scales the two isotropic
vectors of `A` by `t` = `lineScalar` and `t'` = `dualScalar` and acts on the image of the frame of
`B` by `γ`. If `A` and `B` are adapted to the integral structure, then on `S ∪ S̄` the lattice of
the point is the direct sum of its parts in the two isotropic lines and in their orthogonal
complement, and the columns of `γ` span its part in the span of the frame of `B`. 

### `StraightPoint.point`

 The point. 

### `StraightPoint.blockPoint`

 A point with the same components on `S ∪ S̄` that acts by block diagonal matrices. 

### `StraightPoint.lineScalar`

 The scalar by which `u` acts on the isotropic vector of `A`. 

### `StraightPoint.dualScalar`

 The scalar by which `u` acts on the isotropic vector of `A.symm`. 

### `StraightPoint.γ`

 The matrix by which `u` acts on the image of the frame of `B`. 

### `StraightPoint.agrees`

 The point agrees with `u` on `S ∪ S̄` and fixes the frame of `D` elsewhere. 

### `StraightPoint.actsOnFrame_comp`

 `u` acts on the frame of `A.comp B` by `t ⊕ γ`. 

### `StraightPoint.actsOnFrame_symm_comp`

 `u` acts on the frame of `A.symm.comp B` by `t' ⊕ γ`. 

### `StraightPoint.conjTranspose_mul`

 The two scalars are dual to each other. 

### `symm`

 The same point, with the two isotropic lines exchanged. 

### `actsOnFrame`

 If the frame of `D` is the image of the frame of `B`, then `blockPoint` acts on it by `γ`. 

### `exists_centreCoeff_ne_zero`

 Let the frame of `D` be that of `B` inside the complement of the plane split off by `A`. If the
function φ⁺ (`shiftedMean`) of a straight point is not zero, then the coefficient of `f` along `D`
at `T` is not zero at some point that agrees on `S ∪ S̄` with one acting on the frame of `D` by `γ`
and fixes this frame elsewhere. 

### `isIntMatrix_siegelBracket`

 Let `f` be automorphic and right invariant under the integral points supported on `S ∪ S̄`, let
`A`, `B` be adapted to the integral structure, and let the frame of `D` be that of `B` inside the
complement of the plane split off by `A`. If the function φ⁺ (`shiftedMean`) of a straight point is
not zero, then `siegelBracket T γ = δ⁻¹ γᴴ T γ` is integral on `S ∪ S̄`. 

### `exists_straightPoint`

 Straightening. Let `f` be automorphic and right invariant under the integral points supported on
`S ∪ S̄`, let the frame of `D` be that of `B` inside the complement of the plane split off by `A`,
and let the partial mean f⁺ be invariant under the shears for a nonempty set `U` of finite places at
the points that fix the frame of `D` off `S ∪ S̄`. Let `X` be such a point, which agrees with `g` on
`S ∪ S̄`, and let `g * κ`, with `κ` integral at the finite places, act on the frame of `A.comp B` by
a block upper triangular matrix with last block `γ`. If f⁺ is not zero at `X`, then the function φ⁺
(`shiftedMean`) is not zero for some straight point with matrix `γ`. For adapted `A`, `B` the
columns of `γ` span the projection, along the line of `A`, of the part of the lattice of `g` in the
span of the frame of `A.comp B`. 

### `isIntMatrix_of_shiftedMean_ne_zero`

 Supports. Let `f` be automorphic and right invariant under the integral points supported on
`S ∪ S̄`, let `A`, `B` be adapted to the integral structure, let the frame of `D` be that of `B`
inside the complement of the plane split off by `A`, let `det T ≠ 0`, and let the partial mean f⁺ be
invariant under the shears for a nonempty set `U` of finite places at the points that fix the frame
of `D` off `S ∪ S̄`. Let no straight point whose function φ⁺ (`shiftedMean`) is not zero have a
smaller `dualIndex` (the denominator on `S ∪ S̄` of `det (siegelBracket T γ)⁻¹`) than `P`. If the
function φ⁺ of `P` is not zero at `a`, then `γ⁻¹ aᴴ t`, with `t = P.lineScalar`, is integral on
`S ∪ S̄`: the vector `aᴴ t` lies in the lattice spanned by `γ`. 

### `shiftedMean_add_of_isIntMatrix`

 Periods. Let `A` split a hyperbolic plane off the hermitian space `W`, let `B` split the
complement `W₀` along an isotropic frame, and let the isotropic frame of `D` be the image in `W` of
that of `B` (`hD`). Let `f` be continuous and left invariant under the rational points of the
unitary group of `W` (`hf`), and let `det T ≠ 0`.

Let `S` be a set of finite places, `S̄` its conjugate, and `P` a straight point. On `S ∪ S̄` the
point `g = P.point` acts on the frame of `D` by `γ = P.γ` and scales the isotropic vector of
`A.symm` by `t' = P.dualScalar`; elsewhere it fixes the frame of `D`. The function
φ⁺ = `A.shiftedMean B D T f g` sends an adelic row `a` to f⁺(n₊(a) g), where n₊(a) is the shift
`A.lineShift B a` and f⁺(g) is the mean over rows `b` of the Fourier coefficient of `f` along `D`
at `T` at the point `A.symm.lineShift B b * g`. The function φ⁻ is the same for `A.symm`.

Suppose that `γ⁻¹ bᴴ t'` has entries integral on `S ∪ S̄` whenever φ⁻(b) ≠ 0 (`h_supp`), and that
`x` is a column with `siegelBracket T γ * x = δ⁻¹ γᴴ T γ x` integral on `S ∪ S̄` (`hx`), where δ is
the idele `invDifferentIdele E`. Then the row that is `(γ x t'ᴴ)ᴴ` on `S ∪ S̄` and zero elsewhere
is a period of φ⁺; `idemAdele S.conjClosure` is the adele that is 1 on `S ∪ S̄` and 0 elsewhere. 

### `isIntMatrix_inv_siegelBracket`

 Let `f` be automorphic, let the frame of `D` be that of `B` inside the complement of the plane
split off by `A`, and let `det T ≠ 0`. Let the function φ⁺ (`shiftedMean`) of the straight point `P`
be nonzero. Suppose that `γ⁻¹ aᴴ t`, with `t = P.lineScalar`, is integral on `S ∪ S̄` at each `a` in
the support of φ⁺, and `γ⁻¹ bᴴ t'`, with `t' = P.dualScalar`, at each `b` in the support of φ⁻. Then
the inverse of `siegelBracket T γ = δ⁻¹ γᴴ T γ` is integral on `S ∪ S̄`: the lattice spanned by `γ`
contains its dual. 

### `centreCoeff_eq_zero_of_unimodular`

 After Freitag: a singular form is governed by its unimodular coefficients.

Let `f` be an automorphic function that is right invariant under the integral points supported on
`S ∪ S̄` (`hK`, `hf`), and let the splittings `A`, `B` be adapted to the integral structure. Let the
frame of `D` be that of `B` inside the complement of the plane split off by `A` (`hD`), let
`det T ≠ 0`, and let `U` be a nonempty set of finite places. Suppose that the partial means f⁺ and
f⁻ are invariant under the shears for `U` (`ShearInvariant … (idemAdele U)`; in the proof this lets
f⁺ drop a left factor `A.radicalElement c z` taken on `S ∪ S̄`) at the points that fix the frame of
`D` off `S ∪ S̄` (`h_shear`, `h_shear_symm`). Suppose that the Fourier coefficient of `f` along `D`
at `T` vanishes at the points that act on the frame by `γ` on `S ∪ S̄` and trivially elsewhere,
whenever `siegelBracket T γ = δ⁻¹ γᴴ T γ` and a left inverse of it are integral on `S ∪ S̄`
(`h_unimodular`). Then the coefficient vanishes at all points that fix the frame of `D` off
`S ∪ S̄`. 
