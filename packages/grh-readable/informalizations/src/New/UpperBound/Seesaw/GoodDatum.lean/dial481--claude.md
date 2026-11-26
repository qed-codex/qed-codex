---
{
  "module": "src/New/UpperBound/Seesaw/GoodDatum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/GoodDatum.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/GoodDatum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Evaluated data as admissible combinations of glued translates of the vacuum

The data `pointDatumY ϑ k` of the chain of spaces `D.spaceY k`, moved by elements that are integral
away from the level of the twist, are admissible combinations of translates of the vacuum. The
tensor of their evaluations is an admissible combination of the glued translates
`New.Data.gluedVacuum` (`New.Data.exists_isAdmissibleCombination_gluedVacuum`).

Notions from other files:

* `V.finHeisenbergOp x V.vacElem`: the translate of the vacuum of the space `V` by the finite adelic
  vector `x`, in the space `𝒮 V` of the Weil representation `V.ω`.
* `translations ι q d`, `weightedTranslations q d`: the finite adelic vectors `x` such that `d x`
  (respectively each `d i * x i`) is integral at the places not dividing `q`.
* `IsAdmissibleCombination v A q d p B z`: `z` is a finite combination of the `v x` with `x ∈ A`,
  whose coefficients times `d` are integral away from `q` and, if `p` holds, have absolute sum at
  most `B` under every automorphism of `ℂ`.
* `localLevel n S`: the elements of the finite adelic unitary group `Gf E n` that are integral at
  the places of `S`.
* `D.piM`: the integer `π̄₀ π̄₁` of `E`, whose prime divisors are the chosen places.
* An edge of the chain is an arrow `D.spaceY k → D.spaceY (k + 1)`; the pair of edges number `i`
  consists of the arrows from `2 i` to `2 i + 1` and from `2 i + 1` to `2 i + 2`.

## Relation to the literature

See `New.UpperBound.Seesaw.SeesawIdentity` for related work.


 ## Scaling factors and the evaluation of a pair of edges 

### `chosenRatio`

 The quotient `c / c̄` of the finite idele `c = D.chosenIdele`, which generates the ideal of
`D.piM`, by its conjugate. 

### `chosenRatio_mul_star`

 The adele `D.chosenRatio = c / c̄` has norm one. 

### `chosenRatio_apply_of_N_mem`

 The adele `D.chosenRatio = c / c̄` has component `1` at every place above the prime `D.N`. 

### `v_piM_eq_one_of_N_mem`

 The integer `D.piM`, whose prime divisors are the chosen places, is a unit at the places
above the prime `D.N`. 

### `v_star_piM_mul_chosenRatio`

 For `β = D.piM` and `δ = D.chosenRatio`, the adeles `β̄ δ` and `β` have the same valuation
at every finite place: `δ = c / c̄` for an idele `c` with the valuations of `β`. 

### `flipScale_mul_divStar_ideleA`

 Let `η = normNegOne` be the chosen unit of norm `-1`, `α` the idele of the Weil data and
`c = D.chosenIdele`. The idele `flipScale = η̄ ᾱ / α` times `a / ā`, for `a = D.ideleA = α / c̄`,
is `η̄` times `D.chosenRatio = c / c̄`. 

### `isScalingAtM_of_eq_one_or_eq`

 Let `β = D.piM` and `δ = D.chosenRatio`, and let `κ` be factors on the rows
`PairIndex X X''`, each equal to `1` or `δ` and equal to `1` on the first block. Then `κ` is a
scaling (`IsScalingAtM`): `δ` has norm one and is `1` above `D.N`, where `β` is a unit, and the
factors become integral after multiplication by `β̄`, those of the first block also by `β`. 

### `isScalingAtM_one`

 The scaling of a pair of edges other than the last: the factors `1` on all rows
`PairIndex X X''` form a scaling for `β = D.piM` and `δ = D.chosenRatio`
(see `isScalingAtM_of_eq_one_or_eq`). 

### `isScalingAtM_lastScaling`

 The scaling of the last pair of edges: the factors `lastScaling`, equal to `δ` at the last row
and to `1` elsewhere, form a scaling for `β = D.piM` and `δ = D.chosenRatio`. 

### `latticeScale_two_mul`

 The norm-one adele `D.latticeScale j = (a / ā) ^ ⌈(m - j) / 2⌉`, where `a = D.ideleA` and
`m = 2 ϱ + 2` is the length of the chain, gains one factor `a / ā` from `j = 2 i + 2` to `j = 2 i`
when `i ≤ ϱ`. 

### `isAdmissibleEval_doubleLiftEvalY`

 The chain of hermitian spaces `Y j = D.spaceY j` ends at `j = D.m = 2 ϱ + 2`, where `ϱ = D.ϱ`.
For `i ≤ ϱ`, `D.doubleLiftEvalY i` is the map, attached to the arrows
`Y (2 i) → Y (2 i + 1) → Y (2 i + 2)`, from data on `Hom(Y (2 i + 1), (Y (2 i))⁻ ⊕ Y (2 i + 2))` to
tensors of finite data on `Hom(X (2 i), X (2 i + 1))` and `Hom(X (2 i + 1), X (2 i + 2))`, for the
standard definite spaces with basis `X j = D.X j`. Let `β = D.piM`. There is a constant `C` such
that, for every `n` prime to the prime `D.N`, this map sends the translate of the vacuum by a matrix
that is integral away from `n` after multiplication by `β` on the rows of `Y (2 i)` and by `β̄` on
those of `Y (2 i + 2)` to a finite combination of the vectors
`C • gluedTranslate D.N D.piNPlaces (t₁, t₂)` with `β̄ t₁`, `β̄ t₂` integral away from `n`. The
coefficients are integral away from `n` after multiplication by the number of integral matrices
modulo `β` of shape `(X (2 i) ⊕ X (2 i + 2)) × X (2 i + 1)`, and the absolute sum of their images
under any automorphism of `ℂ` is at most `1`. Here `gluedTranslate` is the sum, over vectors with
simple poles at the places `D.piNPlaces` dividing `π = D.piN` (where `π π̄ = D.N`), of translates of
the tensor of the two vacua moved by `t₁` and `t₂`. 

 ## The Weil action and products of translates of the vacuum 

### `mulVec_mem_translations`

 An element `g` of the finite adelic unitary group that is integral away from `q` preserves the
group of vectors `x` with `d x` integral away from `q`. 

### `mem_translations_of_mem_stdLattice`

 If `d` is an integral adele and `x` lies in the standard lattice of integral vectors, then
`d x` is integral away from `q`. 

### `isAdmissibleCombination_weil_of_mem_localLevel`

 Let `g` in the finite adelic unitary group `Gf E n` be integral away from `q`, let `d` be an
integral adele, and let `d x` be integral away from `q`. Then `V.ω (1, g)`, with archimedean
component `1`, takes the translate of the vacuum by `x` to a finite combination of translates by
vectors `y` with `d y` integral away from `q`. The coefficients are integral away from `q`. If `p`
holds, which forces `q = 1`, the absolute sum of their images under any automorphism of `ℂ` is at
most `1`. 

### `exists_arrowProduct_eq_smul_finHeisenbergOp`

 The product `arrowProduct` of the translates by `t₁` and `t₂` of the vacua of
`Hom(V, V')` and `Hom(V', V'')` is a root of unity times a translate of the vacuum of
`Hom(V', V⁻ ⊕ V'')`, where `V⁻ ⊕ V''` is `flipSum V V''`. If `star β` times each of the two
translations is integral away from `q`, then the joined translation `z` becomes integral away from
`q` after multiplication by `β` on the block of `V⁻` and by `star β` on the block of `V''`
(`selfOrConj β`). 

### `piM_mul_normQ_mem_ideal`

 Let `ϑ` be a tame character of `U(1)(𝔸)`, with tame part supported on the finite set of places
`ϑ.Q`. The modulus `D.twistModulus ϑ 1`, the product of the chosen places and of the places of
`ϑ.Q`, divides `D.piM` times the product `ϑ.normQ` of the norms of the places of `ϑ.Q`. 

### `isAdmissibleCombination_pointDatumY`

 Let `ϑ` be a tame character of `U(1)(𝔸)`, with tame part supported on the finite set of places
`ϑ.Q`, and let `q = ϑ.normQ` be the product of the norms of these places. Let `Y k = D.spaceY k` be
the hermitian spaces of the chain, with bases `D.Y k ⊆ D.Y (k + 1)`. The datum `pointDatumY ϑ k` on
`Hom(Y k, Y (k + 1))` is the indicator of the matrix of this inclusion modulo the product of the
prime divisors of `D.piM` and the places of `ϑ.Q`, and the vacuum at the other finite places. It is
a finite combination of Heisenberg translates of the vacuum by adelic matrices `x` with
`star D.piM * x` integral away from `q`. The coefficients become integral away from `q` after
multiplication by the number of matrices modulo `D.piM`, and the absolute sum of their images under
any automorphism of `ℂ` is at most `1`, so this bound holds whatever the proposition `p` under which
it is asked for. 

### `isAdmissibleCombination_translatedPointDatumY`

 Let `ϑ` be a tame character of `U(1)(𝔸)`, with tame part supported on the finite set of places
`ϑ.Q`, and let `q = ϑ.normQ` be the product of the norms of these places. Let every finite adelic
point `y k` of the unitary group of `Y k = D.spaceY k` be integral away from `q`. The datum
`pointDatumY ϑ k` on `Hom(Y k, Y (k + 1))`, moved by `(y k, y (k + 1))` under the Weil
representation, is a finite combination of Heisenberg translates of the vacuum by matrices `x` with
`star D.piM * x` integral away from `q`. The coefficients become integral away from `q` after
multiplication by the number of matrices modulo `D.piM`, and if `ϑ.Q` is empty the absolute sum of
their images under any automorphism of `ℂ` is at most `1`. 

### `absNorm_pow_mul_card_dvd_residueMatrixCount_pow`

 Let `Y j = D.Y j` and `X j = D.X j` be the basis index sets of the spaces `D.spaceY j` and of
the standard definite spaces of rank `D.n j`, for `j ≤ D.m = 2 D.ϱ + 2`, and let `i ≤ D.ϱ`. The
numbers of matrices modulo `D.piM` of the three shapes `Y (2 i + 1) × Y (2 i)`,
`Y (2 i + 2) × Y (2 i + 1)` and `(X (2 i) ⊕ X (2 i + 2)) × X (2 i + 1)` multiply to a divisor of
`D.residueMatrixCount ^ 4`, where `D.residueMatrixCount` is the norm of `D.piM` to the power
`D.n D.m ^ 2`. 

### `isAdmissibleCombination_arrowProduct_translatedPointDatumY`

 Let `ϑ` be a tame character of `U(1)(𝔸)`, with tame part supported on the finite set of places
`ϑ.Q`, and let `q = ϑ.normQ` be the product of the norms of these places. Let every point `y k` of
the unitary group of `Y k = D.spaceY k` be integral away from `q`. The product `arrowProduct` of the
data `translatedPointDatumY ϑ y k` on `Hom(Y k, Y (k + 1))` and `translatedPointDatumY ϑ y (k + 1)`
on `Hom(Y (k + 1), Y (k + 2))` lies on `Hom(Y (k + 1), (Y k)⁻ ⊕ Y (k + 2))`. It is a finite
combination of translates of the vacuum by matrices that become integral away from `q` after
multiplication by `D.piM` on the rows of `Y k` and by its conjugate on those of `Y (k + 2)`. The
coefficients become integral away from `q` after multiplication by the numbers of matrices modulo
`D.piM` of the two shapes, and if `ϑ.Q` is empty the absolute sum of their images under any
automorphism of `ℂ` is at most `1`. 

### `exists_isAdmissibleCombination_evaluatedDatum`

 Let `i ≤ D.ϱ`, where the chain of spaces `Y j = D.spaceY j` ends at `j = 2 D.ϱ + 2`. There is a
constant `C` with the following property. Let `ϑ` be a tame character of `U(1)(𝔸)`, with tame part
supported on the finite set of places `ϑ.Q`, let `q = ϑ.normQ` be the product of their norms, and
let the points `y k` of the unitary groups of the `Y k` be integral away from `q`. Then
`evaluatedDatum ϑ y i`, the image under `D.doubleLiftEvalY i` of the product of the moved data on
`Hom(Y (2 i), Y (2 i + 1))` and `Hom(Y (2 i + 1), Y (2 i + 2))`, is a finite combination of the
vectors `C • gluedTranslate D.N D.piNPlaces (t₁, t₂)`. The matrices `t₁`, `t₂` are indexed by the
bases `D.X j` of the standard definite spaces and have denominator `star D.piM` away from `q`.
Here `gluedTranslate` is the sum over simple poles at the places `D.piNPlaces` above the prime `D.N`
(`doubleLiftGluing`) applied to the tensor of the two vacua translated by `t₁` and `t₂`. The
coefficients times `D.residueMatrixCount ^ 4`, a power of the norm of `D.piM`, are integral away
from `q`, and if `ϑ.Q` is empty the absolute sum of their images under any automorphism of `ℂ` is at
most `1`. 

### `exists_isAdmissibleCombination_gluedVacuum`

 The chain of spaces `Y j = D.spaceY j` ends at `j = D.m = 2 D.ϱ + 2`. There is a constant `C`
with the following property. Let `ϑ` be a tame character of `U(1)(𝔸)`, with tame part supported on
the finite set of places `ϑ.Q`, let `q = ϑ.normQ` be the product of their norms, and let the points
`y k` of the unitary groups of the `Y k` be integral away from `q`. Then the pure tensor of the
vectors `evaluatedDatum ϑ y i` for `i ≤ D.ϱ` is a finite combination of the vectors
`C • D.gluedVacuum t`, where `t` is a tuple of matrices with denominator `star D.piM` away from `q`.
The coefficients times `D.residueMatrixCount ^ (2 * D.m)`, a power of the norm of `D.piM`, are
integral away from `q`, and if `ϑ.Q` is empty the absolute sum of their images under any
automorphism of `ℂ` is at most `1`. 
