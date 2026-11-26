---
{
  "module": "src/New/Congruences/GaloisRepresentations/SelmerHypotheses.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/SelmerHypotheses.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/SelmerHypotheses.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bad places, ℓ-adic avatars and hypotheses on conjugate self-dual representations

Fix data `D`, a prime `ℓ` and a descent pair `O` (`New.DescentPair`) with chosen places
`O.chosenPlace`. This file introduces the bad places and the `ℓ`-adic avatars of characters of
`U(1)`. It states the hypotheses on conjugate self-dual `ℓ`-adic representations `R` of the
absolute Galois group of the CM field `D.E` under which Selmer groups are bounded: conjugate
self-dual representations of given level, main summands and representations of a type. It also
defines lift settings and the idempotents of tuples of types acting on forms. The two primes
`p₀`, `p₁` of the data are `D.levelPrime 0` and `D.levelPrime 1`.

## Main definitions and results

* `New.Selmer.IsConjSelfDual`: `R` is continuous, has a non-degenerate trace form on the span of its
  image, and is conjugate self-dual up to a twist.
* `New.Selmer.IsConjSelfDualOfLevel`: moreover `R` has given jumps and is of finite type at the
  places off a set `S` and at those above `ℓ p₀ p₁`, and has good reduction at those of them prime
  to `p₀ p₁`.
* `New.Selmer.IsMainSummandLike`: the case `S = ∅`, with conditions on the jumps, the ramification
  above `p₀ p₁` and the size of the image.
* `New.Selmer.IsLiftSetting`, `New.Selmer.typeProjection`: descent pairs with type polynomials
  suited to a twist, and the idempotents of tuples of types acting on forms.

Notions from other files:
* `New.DescentPair`: A descent pair: places M and Q, a space W of rank r with numbered basis
  vectors, an embedding of its r indices into a set of n > r indices, weights k⁺ and k⁻, and a
  character μ whose tame part is trivial off these places.
* `New.DescentPair.FormV`: the algebraic forms on the definite space `V = I_n` with the weight and
  level of `O`; the product of the groups `GL_r(k_w)` at the chosen places acts on them.
* `New.conjGal`: The map `g ↦ g^c = c g c`, with `c` complex conjugation.

## Relation to the literature

See `Lib.ClassField.Avatar.LocalGlobalCompatibility` for sources.



## Bad places and ℓ-adic avatars of characters of U(1)

For the data `D`, an embedding of `D.E` in `ℚ̄` (`New.Ω`) is fixed.

* `New.Selmer.avatar_conjGal_mul_avatar`: `μ(g^c) μ(g) = cyc(g)^{2j - k}`.


### `noncomputable instance : CMFieldWithRoot5040 D.E`

 `D.E` is a `New.CMFieldWithRoot5040`. Its embedding in `Ω` factors through the cyclotomic field
of conductor `D.cyclotomicConductor`. 

 ### The Galois group and the bad places 

### `AbsGal`

 The absolute Galois group of the field E of the data D: automorphisms of an algebraic
closure of E fixing E. 

### `placesAboveM`

 The set of finite places of E above one of the two primes p₀, p₁ of the data. 

### `badPlaces`

 The finite set of places of E dividing `ℓ p₀ p₁ N`, with `N` the level of the data; these are
the bad places. 

### `placesDividing_union_subset_badPlaces`

 The places dividing `ℓ` and the places above `p₀` or `p₁` are bad places. 

### `_root_.New.Data.IsChosen.mem_placesAboveM`

 A chosen place (`New.Data.IsChosen`) lies above `p₀` or `p₁`. 

### `norm_natCast_le_norm_sub_of_pow_eq_one`

 Two distinct `N`-th roots of unity in `ℚ̄_ℓ` have distance at least `‖N‖`. 

### `cyclotomicInv_frob`

 For a Frobenius datum `x` whose place `x.place` does not divide `ℓ`, the inverse cyclotomic
character `cyclotomicInv ℓ D.E (PadicAlgCl ℓ)` takes the value `x.place.q`, the norm of `x.place`,
at `x.frob`, a geometric Frobenius at `x.place`. 

 ### Avatars and the cyclotomic character 

### `_root_.New.Data.TameChar.invAvatar`

 The ℓ-adic avatar, through ι, of the base change to E of ϑ⁻¹: a character of the absolute
Galois group of E with values in ℚ̄_ℓ. Here ι is the isomorphism of ℂ with ℚ̄_ℓ that the instance
`New.PadicIso ℓ` fixes. 

### `avatar_conjGal_mul_frob`

 Let `x` be a Frobenius datum whose place does not divide `ℓ`, with the tame part `ψ` of `a`
trivial at the place and at its conjugate, and let `μ` be the avatar of the algebraic Hecke
character `y ↦ a(y / ȳ) υ(y)^{-k} |y|^{j - k/2}`, with `υ` the fixed splitting character. At the
element `g` of the datum, `μ(g^c) μ(g) = cyc(g)^{2j - k}`. 

### `avatar_conjGal_mul_avatar`

 The ℓ-adic avatar μ of the algebraic Hecke character `a(x / x̄) υ(x)^{-k} |x|^{j - k/2}`
satisfies `μ(g^c) μ(g) = cyc(g)^{2j - k}` for all g. Here `a` is a character of `U(1)` of weight
`e` and tame part `ψ`, `υ` is the fixed splitting character, `cyc` is the cyclotomic character and
`g^c` is `New.conjGal g`. 

### `isLabelledAt_avatar`

 Let `w` be a split place, `A` a place of `Ω`, and `a` a character of `U(1)` whose tame part `ψ`
is trivial at `w̄`. Let `μ` be the avatar of `y ↦ a(y / ȳ) υ(y)^{-k} |y|^{j - k/2}`, with `υ` the
fixed splitting character. Then inertia at `A` acts on `μ` through the label of `ψ w`, the element
of the residue field that names this character (`New.charName`) through
`T = faithfulChar (ResField w)`: an element with tame exponent `i` of level `f` at `A` over `w` is
killed by `X - ι (T^i label)`. 


## The chosen places of the level places

For the level places L = `D.levelPlaces ϑ`, the chosen places of L are chosen in the sense of
`New.Data.IsChosen`, lie above p₀ or p₁ and are outside the modulus of ϑ.


### `New.Data.TameChar.tamePart_eq_one_of_isChosen`

 The tame part of a tame character `ϑ` is trivial at every chosen place
(`New.Data.IsChosen`). 

### `New.Data.isChosen_levelPlaces_chosenPlace`

 Each chosen place of the level places `D.levelPlaces ϑ` is chosen in the sense of
`New.Data.IsChosen`. 

### `New.Selmer.isChosen_chosenPlace`

 Each chosen place of the level places `D.levelPlaces ϑ` is chosen in the sense of
`New.Data.IsChosen`, the tame part of `ϑ` is trivial there, and it lies above `p₀` or `p₁`. 


## Hypotheses on conjugate self-dual representations for Selmer bounds

* `New.Selmer.twistError`: the number `e'_ℓ` of the twisting theorem.

`New.CoeffRing ℓ` are the rings of integers of finite Galois extensions of `ℚ_ℓ`, and
`∀ᶠ O in .atTop` means for all large ones; `New.ellVal` and `New.CoeffRing.normLength` are
normalised so that `ℓ` counts one.


### `IsConjSelfDual`

 `R` is continuous, has non-degenerate trace form, and is conjugate self-dual up to twist,
`R^c ≅ R^∨(1 − t)`. Self-duality is stated on traces: `tr R(g^c) = cyc(g)^{1−t} tr R(g⁻¹)` for all
`g`, where `t = 0` is read as `t = 1`. 

### `IsConjSelfDual.continuous`

 `R` is continuous. 

### `IsConjSelfDual.nondeg`

 The trace form on the span of the image of `R` is non-degenerate. 

### `IsConjSelfDual.trace_conj`

 Conjugate self-duality on traces: `tr R(g^c) = cyc(g)^{1 - t} tr R(g⁻¹)`, where
  `cyclotomicInv` is the inverse of the cyclotomic character `cyc`; `t = 0` is read as `t = 1`. 

### `twistError`

 The negligible number `e'_ℓ = (4 f + 3) r v_ℓ(D.chosenGroupOrder) + 2 ^ (-ℓ)` that bounds the
Selmer groups, the ramification and the valuations of the `L`-values of a good twist. The integer
`New.Data.chosenGroupOrder` is the order of the product of `GL (D.r * D.t)` over the residue fields
at the chosen places. 

### `selmerCocycles`

 The Selmer group of a lattice `ρ` modulo `ℓ ^ m`: the continuous cocycles that are unramified
off `ℓ p₀ p₁`, `Q` and `Q̄`, lie in `H¹_f` above `ℓ` and vanish at the given element `γ`. The last
condition singles out one cocycle in each class when `ρ γ - 1` is invertible. 

### `IsTwistedLattice`

 `u`, `ψ'` and `ζ'` are models over `O` of `R`, `ψ` and `ζ`, and on the twisted lattice `ψ' u`
the element `γ` is the scalar `ζ'`. 

### `IsTwistedLattice.scalar_eq`

 `ζ'` is `ζ`. 

### `IsTwistedLattice.isLatticeIn`

 `u` is a lattice in `R`. 

### `IsTwistedLattice.twist_eq`

 `ψ'` is `ψ`. 

### `IsTwistedLattice.apply_eq_smul`

 `γ` acts on the twisted lattice by the scalar `ζ'`. 

### `IsTwistedLattice.isUnit_sub_one`

 `ζ' - 1` is a unit. 

### `IsTwistedLattice.mem_inertiaAbove`

 `γ` lies in an inertia group above a place that does not divide `ℓ`. 

### `IsTwistedLattice.cyclotomicChar_eq_one`

 The cyclotomic character is `1` at `γ`, which lies in inertia at a place not above `ℓ`. 

### `HasTwistedLattice`

 Over all large coefficient rings, `R`, `ψ` and `ζ` have models `u`, `ψ'`, `ζ'` on whose twisted
lattice `γ` acts by the scalar `ζ'` (`IsTwistedLattice`). 

### `crystallineSelmerLength`

 The length of the Selmer group of a lattice `ρ` with coefficients in `Frac(O) / O`: the
continuous cocycles that are unramified off `ℓ p₀ p₁`, `Q` and `Q̄`, lie in `H¹_f` above `ℓ` and
vanish at `γ`. 

### `HasDivisibleSelmerLengthLe`

 Over all large coefficient rings `O` there are models `u`, `ψ'` and `ζ'` of `R`, `ψ` and `ζ`
such that `γ` acts on the twisted lattice `ψ' u` by the scalar `ζ'` (see `IsTwistedLattice`) and the
Selmer group of `ψ' u` with coefficients in `Frac(O) / O` has length at most `sel`, normalised by
`len O / ℓ = 1`. 

### `length_selmerCocycles_le_crystallineSelmerLength`

 Let `ρ` be a matrix representation over `O` of the absolute Galois group of `E = D.E`, `Q` a
finite set of places of `E` and `γ` an element of the Galois group. Consider the locally constant
cocycles for `ρ` that are unramified at the places prime to `ℓ p₀ p₁` and outside `Q` and `Q̄`, obey
the relations of the crystalline cocycles above `ℓ` (`crysRelations ρ`) and vanish at `γ`. The
module of those with coefficients in `O / ℓ ^ M` (`selmerCocycles`) is at most as long as the module
of those with coefficients in `Frac(O) / O`, whose length is `crystallineSelmerLength`. 

### `HasDivisibleSelmerLengthLe.hasTwistedLattice`

 A bound for the Selmer group with divisible coefficients comes with a twisted lattice. 

### `HasDivisibleSelmerLengthLe.mono`

 A bound for the Selmer group with divisible coefficients holds for every larger bound. 

### `IsConjSelfDualOfLevel`

 A conjugate self-dual representation of level `S`: `R` satisfies `IsConjSelfDual`, and three
local conditions hold at every place `v` that is outside `S` or divides `ℓ p₀ p₁`. 

### `IsConjSelfDualOfLevel.local_conditions`

 At every place `v` off `S` or above `ℓ p₀ p₁`, and every `A` over `v`: `R` is trivial on
  inertia near `1` (potentially crystalline above `ℓ`), has jumps `J` (`HasJumpsAt R A J`, read
  through the isomorphism fixed by the instance `New.PadicIso ℓ`), and is unramified (crystalline
  above `ℓ`) if `v` is prime to `p₀ p₁`. 

### `IsMainSummandLike`

 A main summand: a conjugate self-dual representation of empty level whose jumps satisfy
`IsMainSummandWeights`, with four more conditions. At the places above `p₀ p₁` prime to `ℓ`, a power
prime to the place kills the image of inertia and two determinants have bounded valuation. The image
of a lattice spans all matrices, and it contains a scalar with prescribed cyclotomic character. Some
inertia element acts by a scalar of large order modulo the maximal ideal. 

### `IsMainSummandLike.inertia_above_M`

 At every `A` over a place `v ∣ p₀ p₁` prime to `ℓ`, there are an inertia element `γ` and an
  integer `N` prime to `v` such that `R` is trivial on the `N`-th powers of inertia, and
  `det (R γ - 1)` and `det (R (γ^c)⁻¹ - 1)` have valuation at most `card n` times that of
  `D.chosenGroupOrder`. If `v` is a chosen place, `γ` is the tame generator `hA.tameGenerator`. 

### `IsMainSummandLike.span_eq_top`

 For all large coefficient rings `O`, the image of every lattice `u` in `R` spans all matrices
  over `O`. 

### `IsMainSummandLike.exists_scalar_cyclotomicChar`

 For all large coefficient rings `O` and every lattice `u` in `R` over `O`, some `g` with
  cyclotomic character `p₀ ^ card n` or `p₁ ^ card n` acts on `u` by a scalar. 

### `IsMainSummandLike.exists_scalar_inertia`

 Some inertia element at a place above `p₀` or `p₁` and prime to `ℓ` acts by a scalar `y` such
  that `y ^ (ℓ ^ a * j) - 1` is a unit for all `a` and `1 ≤ j ≤ 4 * card n + 2`. 

### `IsMainSummandLike.eventually_span_eq_top_and_exists_eq_smul_one`

 Let `R` be a main summand (`IsMainSummandLike`) of rank `card n`. For all large coefficient
rings `O`, the image of every lattice `u` in `R` spans all matrices over `O`, and some `g` with
cyclotomic character `p₀ ^ card n` or `p₁ ^ card n` acts on `u` by a scalar. 

### `IsMainSummandLike.eventually_eq_bot_or_eq_top`

 A main summand `R` (`IsMainSummandLike`) is residually absolutely irreducible: for all large
coefficient rings `O`, every lattice `u` in `R` and every ring map `f` from `O` to a field `k`, the
only subspaces of `kⁿ` stable under all `f (u g)` are `0` and `kⁿ`. 

### `IsMainSummandLike.eventually_lattice_unique`

 Let `R` be a main summand: an `ℓ`-adic representation of the Galois group of `D.E` with
`R^c ≅ R^∨(1 - t)` on traces and Hodge–Tate jumps `J`, such that, among other conditions, the image
of each lattice over a large coefficient ring `O` spans all matrices. Then the stable lattice is
unique up to scalars, for all large `O`: if `R` has matrices `u g` over `O` in the basis `Q` and
`u' g` over `O` in the basis `Q'`, then `Q' = α Q k` with a scalar `α` and `k` in `GL_n(O)`. 


## The normalising character, lift settings, main summands and representations of a type

Conventions: a label is a polynomial over the residue field at a place of `O.chosenPlace`.

* `New.Selmer.normalizingAvatar`, `New.Selmer.normalizingAvatar_eq_of_isFrob_inv`,
  `New.Selmer.normalisedRep`: the normalising character, its Frobenius values, and the twist of a
  representation by it.


 ### The normalising character 

### `normalizingAvatar`

 The ℓ-adic avatar of the algebraic Hecke character built from the inverse of the character
`O.charW`, with weight `-card r`. Here `card r` is the dimension of the space `W` of `O`. It
normalises the representations attached to forms on `V`, which has dimension `card n`. 

### `normalizingAvatar_eq_of_isFrob_inv`

 The value of the normalising character `New.Selmer.normalizingAvatar O` at `s` when `s⁻¹` fixes
a place `A` over `w ∤ ℓ` and acts there as the `d`-th power of Frobenius: it is the `d`-th power of
the image under the fixed isomorphism `ιℓ` of the inverse of `O.charW.frobValue r w`, the value at a
uniformiser at `w` of the Hecke character of `W` made from `O.charW`, times `q_w ^ (card r / 2)`. 

### `normalisedRep`

 The normalised representation: R twisted by the character `New.Selmer.normalizingAvatar`. 

 ### Scaled type polynomials 

### `scaledTypePoly`

 The label c_i with its roots multiplied by the element of the residue field that names
(`New.charName`) the character `(O.tamePart w)⁻¹`, where `w = O.chosenPlace i`. 

### `IsLiftSetting`

 The descent pair `O` with the labels `c` is a lift setting for the twist `ϑ`. Conditions on the
pair: its places are `D.levelPlaces ϑ`. Its character `O.tamePart` is `D.chiMLocal ^ j * ϑ.tamePart`
with `1 ≤ j ≤ D.m`. The numbers `card r` and `O.rankDiff` are odd, with `card r ≤ D.r` and
`O.rankDiff ≤ D.t`. Conditions on the labels: each `c i` is a label of degree `card r`. Its scaled
type polynomial (`New.Selmer.scaledTypePoly`) does not have `1` as a root. Over each prime
`D.levelPrime k`, one of the labels is primitive with `card r = D.r`, or is `X - 1` with
`card r = 1`. 

### `IsLiftSetting.toLevelPlaces_eq`

 The places of `O` are those of `D.levelPlaces ϑ`. 

### `IsLiftSetting.exists_tamePart_eq_chiMLocal_zpow_mul`

 The character `O.tamePart` is `D.chiMLocal ^ j * ϑ.tamePart` for some `1 ≤ j ≤ D.m`. 

### `IsLiftSetting.odd`

 The rank `card r` and the number `O.rankDiff` are odd. 

### `IsLiftSetting.rank_le`

 `card r ≤ D.r` and `O.rankDiff ≤ D.t`. 

### `IsLiftSetting.isLabel`

 Each `c i` is a label of degree `card r`. 

### `IsLiftSetting.exists_primitive_or_one`

 Over each prime `D.levelPrime k` there is a place `O.chosenPlace i` where either
  `card r = D.r` and `c i` is a primitive polynomial (`IsPrimitivePolynomial`), or `card r = 1` and
  `c i = X - 1`. 

### `IsLiftSetting.not_isRoot_scaledTypePoly`

 The scaled type polynomial `New.Selmer.scaledTypePoly O c i` does not have `1` as a root. 

### `typeProjection`

 The endomorphism of the space of forms given by the action of the group-algebra idempotent
attached to the tuple of labels c. 

### `HasLiftTrace`

 The trace of `u` is `ψ · tr R + ∑_{e < t} cyc⁻¹ ^ e`: on traces, `u` is the sum of the twist
`ψ R` and the first `t` powers of the inverse cyclotomic character. 

### `IsMainSummand`

 `R` is a main summand (`IsMainSummandLike`), and it serves all twists of `O`: if the character
of a descent pair `V` is `O.u1Char` twisted by `ϑ` and the eigenform `y` for `V` lifts the system of
Hecke eigenvalues `z`, then on traces the normalised representation attached to `y` is the sum of
`ψ R` and the first `V.rankDiff` powers of the inverse cyclotomic character (`HasLiftTrace`), with
`ψ` the avatar of `ϑ⁻¹`. 

### `IsRepOfType`

 A representation of a type: `R` is conjugate self-dual of twist `1 - k`, jumps `J` and level `S`
(`New.Selmer.IsConjSelfDualOfLevel`), and inertia at the place `O.chosenPlace i` acts through the
roots of the label `c i`, a polynomial over the residue field. 

### `IsRepOfType.labelled`

 At each place `A`, an element of inertia over `O.chosenPlace i` is killed by the polynomial
  that `IsLabelledAt` makes from the label `c i` and the tame exponent at level `(card r)!`. 


## Lift settings, label idempotents, and split places off the level

Small facts used with a descent pair `O` (`New.DescentPair`) and a tuple `c` of polynomials over the
residue fields at the places `O.chosenPlace i`. Only `New.Selmer.IsLiftSetting.card_le` and
`New.Selmer.IsLiftSetting.isChosen_chosenPlace` assume that the tuple is a lift setting for a twist
(`New.Selmer.IsLiftSetting`). The other facts hold for any tuple `c`.

* `New.Selmer.IsLiftSetting.isSymmetric_typeProjection`,
  `New.Selmer.IsLiftSetting.typeProjection_eq_self_of_mem_range`,
  `New.Selmer.IsLiftSetting.range_typeProjection_mem_invtSubmodule`: the idempotent
  `typeProjection O c` is self-adjoint and fixes its range. Its range is stable under the Hecke
  polynomials `O.heckePolyOnForms` off the level.


### `IsLiftSetting.card_le`

 If the labels `c` form a lift setting for the twist `ϑ` (`New.Selmer.IsLiftSetting`), the
dimension `card n` of the space `V` of the descent pair is at most twice the rank
`D.n D.m = D.k + D.m * (D.t + 1)`. 

### `IsLiftSetting.isChosen_chosenPlace`

 If the labels `c` form a lift setting for the twist `ϑ` (`New.Selmer.IsLiftSetting`), every
place `O.chosenPlace i` of the descent pair is chosen in the sense of `New.Data.IsChosen`. 

### `IsLiftSetting.isSymmetric_typeProjection`

 The idempotent `typeProjection O c`, by which the tuple of labels `c` acts on the forms on the
space `V` of the descent pair `O`, is self-adjoint. 

### `IsLiftSetting.typeProjection_eq_self_of_mem_range`

 The idempotent `typeProjection O c` fixes every form `y` in its range. 

### `IsLiftSetting.range_typeProjection_mem_invtSubmodule`

 Let `c` be a tuple of polynomials over the residue fields at the chosen places of the descent
pair `O`, and `typeProjection O c` the idempotent by which the tensor product of their label
idempotents (`New.tupleIdem`) acts on the forms on `V`. Let `w` be a split place such that neither
`w` nor its conjugate is among the places of `O`. For every complex number `x`, the range of
`typeProjection O c` is stable under the Hecke polynomial at `w` evaluated at `x`, the operator
`∑_{i ≤ card n} (-x) ^ i q ^ (i (i - 1) / 2) T_{w,i}`, with `q` the norm of `w` and `T_{w,i}` the
Hecke operators at `w`. 

### `frequently_isSplit_notMem_places`

 Infinitely many places of `E` are split and are, with their conjugates, outside the places of
the descent pair `O`. 
