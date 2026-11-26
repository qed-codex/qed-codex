---
{
  "module": "src/New/Congruences/FirstOrder/DenominatorBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/DenominatorBound.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/DenominatorBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The bound for denominators

The bound that Ribet's method gives for the denominator of the orthogonal projection to `Z`: an
operator on `Z`, with eigenvalues of bounded valuation, takes the projection of every integral form
orthogonal to the false lifts to an integral form. `O` is a descent pair of hermitian spaces of
ranks `r < n` (`New.DescentPair`). `Z` is a subspace of its forms spanned by vectors in the ranges
of the idempotents `New.Selmer.typeProjection O c` of types `c` in lift setting.

The *chain* at a place of norm `q` is `∏ (X - q ^ i)`, `i < t'`, with `t' = O.rankDiff`.

* `New.Selmer.typeProjection_sub_starProjection_mem_of_isOrthogonalToFalseLifts`: a form orthogonal
  to the false lifts differs from its projection to `Z`, in each type, only outside the weak lifts.
* `New.Selmer.exists_operator_ellVal_le_liftValuationBound`: the bound for denominators. An operator
  on `Z` preserves the Hecke eigenspaces, has eigenvalues of valuation at most
  `New.Selmer.liftValuationBound` and takes projections of integral forms orthogonal to the false
  lifts to integral forms.
* `New.Selmer.denominatorLe_clearingBound`: if `Z` is spanned by lifts whose twisted main summands
  have small Selmer groups with divisible coefficients (`New.Selmer.IsLiftGenerator`), then
  `New.Selmer.DenominatorLe` holds with exponent `β log ℓ`, where
  `β = New.Selmer.clearingBound D ℓ`. Its operator is `D.chosenGroupOrder` times that of
  `exists_operator_ellVal_le_liftValuationBound` (`New.Selmer.exists_operator_det_clearingBound`).

Notions from other files:
* `New.Selmer.AbsGal`: the absolute Galois group of the CM field `D.E` of the data `D`.
* `New.Data.chosenGroupOrder`: the product, over the chosen places above `D.levelPrime 0` and
  `D.levelPrime 1`, of the orders of the groups `GL (D.r * D.t)` over the residue fields.
* `New.Patching.Isotypic`: a system, that is the space of forms with given Hecke eigenvalues at
  almost all places. `B.Eigensystem L` is the set of systems that contain a nonzero form of level
  `L` over the base data `B`; the base level is `L = ![]`.
* `New.Selmer.normalisedRep`: the twist of a Galois representation by the character
  `normalizingAvatar O`.
* `New.Selmer.IsAuxTwist`: the character is anticyclotomic, its modulus avoids the given places and
  its ramification has bounded valuation.

## Relation to the literature

For a twist with short Selmer groups, an operator of bounded ℓ-adic valuation clears the denominator
of the projection to theta lifts on integral forms orthogonal to the false lifts. The bound counts
local losses, class number, level, odd classes and congruences between the characters; the orders of
the even classes, where Vandiver's conjecture lives, do not enter. Ribet-type bounds, Taylor–Wiles
primes in the residually reducible case and the mass formula case are treated in the following
works. Related work: Dasgupta–Kakde–Silliman–Wang, The residually indistinguishable case of Ribet's
method for GL2, 2023; Dotto–Thorne, Modularity of residually reducible representations of rank 2,
2026; Martin–Wakatsuki, Mass formulas and Eisenstein congruences in higher rank, 2024.


### `exists_isUnit_cyclotomicChar_pow_sub_one`

 Let the prime `ℓ` exceed the square of `D.halfGap = D.r ^ 8`. Then some element `γ` of the
absolute Galois group of `D.E` has an `ℓ`-adic cyclotomic character `u` with `u ^ a - 1` a unit of
`ℤ_ℓ` for `0 < a < D.t`, where `D.t = 5 * D.r`. 

### `exists_cyclotomicChar_pow_sub_one_dvd_pow_padicValNat`

 Some element `φ` of the absolute Galois group of `D.E` has an `ℓ`-adic cyclotomic character `u`
such that for `0 < a < D.t` the number `u ^ a - 1` divides, in `ℤ_ℓ`, the `ℓ`-part of
`D.chosenGroupOrder`, the product of the orders of `GL (D.r * D.t)` over the residue fields of the
chosen places. 

### `exists_cyclotomicChar_pow_sub_one_dvd`

 There are `h`, at most the `ℓ`-adic valuation of `D.chosenGroupOrder` and zero unless
`ℓ ≤ D.halfGap ^ 2`, and a topological generator `γ` of the Galois group of `D.E` modulo the kernel
of the cyclotomic character such that `u ^ a - 1` divides `ℓ ^ h` in `ℤ_ℓ` for `0 < a < D.t`, where
`u` is the cyclotomic character of `γ`. 

### `IsWeakLift`

 The system `x` (an isotypic space of forms for the descent pair `O`) is a weak lift: at every
Galois element the characteristic polynomial of its normalised representation has the root `1`. 

### `IsNonzeroIn`

 The form `v` of the descent pair `O` is a nonzero form of the isotypic space `x`. 

### `IsNonzeroIn.mem`

 The algebraic form `v.toSmoothForm` of `v` lies in `x`. 

### `IsNonzeroIn.ne_zero`

 The algebraic form `v.toSmoothForm` of `v` is not zero. 

### `IsLiftWithTwistedLattice`

 The system `x` lifts a row `R` (`IsMainSummandLike`: a representation of rank `r` with the
properties of a main summand): the trace of its normalised representation is that of `R` twisted
by `ϑ.invAvatar` plus the powers `e < O.rankDiff` of the inverse cyclotomic character. The twist
has a lattice on which some `γ` acts by a scalar `y` and, if `x = x₀`, its Selmer group with
divisible coefficients has length at most `sel`. 

### `liftValuationBound`

 The bound `sel + 2 t′ ram + r′ loc + err` for the valuations of the eigenvalues of the operator
that clears denominators. Here `r′ = card r`, `t′ = O.rankDiff`, `loc = localDefectBound D ℓ` and
`err = denominatorError D ℓ`; `ram` bounds the ramification of the twist and `sel` the lengths of
the Selmer groups. 

### `invAvatar_eq_one_of_mem_inertiaAbove`

 Let `ϑ` be an auxiliary twist of the data `D`, with ramification at most `ram` (`IsAuxTwist`):
the places of `ϑ.Q` and their conjugates avoid `badPlaces D ℓ`, and `ϑ.invAvatar`, the `ℓ`-adic
Galois character of `ϑ⁻¹`, is anticyclotomic with modulus `ϑ.Q`. Then `ϑ.invAvatar` kills the
inertia groups at the places in `placesAboveM D`, those above the two primes `D.levelPrime i`. 

### `exists_eventually_hasRootChain_mostFrobeniiAt`

 Let `ϑ` be an auxiliary twist of ramification at most `ram` and `B` base data whose systems, the
Hecke eigenspaces of level `![]`, have normalised Galois representations with integral
characteristic polynomials. Let `R` be a row of weights `wt` (`IsMainSummandLike`). For every `ν`
and `g` there is `δ` with trivial cyclotomic character such that, along the filter `mostFrobeniiAt`
at `δ ^ ℓ ^ ν * g`, a place `y.place` with Frobenius `y.frob` satisfies: (a) the place avoids
`badPlaces D ℓ` and is off the base level; (b) if the system `x` is a weak lift and its polynomial
at the Frobenius is congruent to `∏ (X - cyclotomicInv φ ^ i)`, `φ = y.frob`, `i < O.rankDiff`,
times some `S` with `1 ≤ ‖S 1‖`, then its Hecke polynomial at the place, with the variable rescaled
by `normalizingAvatar O φ` read in `ℂ` by the fixed isomorphism `ιℓ`, is the chain `∏ (X - q ^ i)`,
`q` the norm of the place, times a divisor of an integral `e` with `e 1 = 1`; (c) the characteristic
polynomial of the twist of `R` by `ϑ.invAvatar` at the Frobenius has a value of norm at least `1` at
`1`. 

### `exists_taylorWilesPlaces_hasRootChain`

 The auxiliary places of the Taylor–Wiles method. Let the types `c` form a lift setting for the
pair of hermitian spaces `O` and the auxiliary twist `ϑ` of ramification at most `ram`, and let the
systems of the base data `B` have integral characteristic polynomials. Let `x₀` lift the row `R` of
weights `wt`: the trace of its normalised representation is that of the twist of `R` plus the powers
`cyclotomicInv ^ e`, `e < O.rankDiff` (`HasLiftTrace`). Let `g₁` generate the Galois group of `D.E`
topologically modulo the kernel of the cyclotomic character, let `u ^ a - 1` divide `ℓ ^ h` in `ℤ_ℓ`
for `0 < a < D.t = 5 * D.r`, where `u` is the cyclotomic character of `g₁`, and let
`ℓ ≤ D.halfGap ^ 2` (`D.halfGap = D.r ^ 8`) or `h = 0`. Then there are a finite linear order `J` and
a monotone map `exponent` to the exponents `0 < e < O.rankDiff` such that for each `ν > 0` some
places `Q` of norm `1` modulo `ℓ ^ ν`, indexed by `J`, satisfy: (a) they form a triangle for the
generator `g₁⁻¹` (`IsPrimeTriangle`): the Frobenius elements of exponent `e` and finitely many test
points detect the Galois cohomology classes of twist `-e` unramified off `ℓ`, the powers `u ^ e`
being separated up to `ℓ ^ (D.halfGap * h)`, with total loss `D.halfGap ^ 22 * h`; (b) they avoid
`badPlaces D ℓ` and are off the base level, so are unramified for the forms of `B`; (c) for every
weak lift `x` of base level congruent to `x₀`, the Hecke polynomial at the place of index `j` and
norm `q`, with the variable rescaled by the normalising character, is the chain `∏ (X - q ^ i)`,
`i < O.rankDiff`, times a divisor of an integral `e j` that has value `1` at `1` and does not depend
on `x`. 

### `norm_charpoly_coeff_le_one_of_continuous`

 A continuous representation of a compact group over `ℚ̄_ℓ` keeps a lattice, so its
characteristic polynomials have integral coefficients. 

### `exists_det_one_sub_ne_zero`

 Let `u x g` be matrices over `ℚ̄_ℓ` with integral characteristic polynomials, and suppose that
for each `x` some `u x g` does not have the eigenvalue `1`. Then for each `x` there is `elt x` such
that `det (1 - u x (elt x))` is a nonzero element `value x` of the valuation ring of `ℚ̄_ℓ`. 

### `exists_prod_sub_det_one_sub_eq_zero`

 Let `u x g` be matrices over `ℚ̄_ℓ` with integral characteristic polynomials, `x` in a finite
type. There are finitely many elements `elt k` and nonzero elements `value k` of the valuation ring
of `ℚ̄_ℓ` such that the product of the `value k - det (1 - u x (elt k))` vanishes at every `x` for
which some `u x g` does not have the eigenvalue `1`. 

### `exists_dvd_prime_pow_succ`

 A nonzero `ℓ`-adic integer divides a positive power of `ℓ`. 

### `normalizingAvatar_tameGenerator`

 The character `normalizingAvatar O` is unramified away from `ℓ`, so it is trivial at the tame
generator of a place `A` over `w ∤ ℓ`. 

### `exists_isCommonRibetElement_ellVal_le`

 There is a common Ribet element for a finite family `sys` of systems, with normalised Galois
representations `N x`. Assume the following. The types `c` form a lift setting for `O` and the twist
`ϑ`, whose ramification is at most `ram`. The places `w j`, with tame generators `tame j` and
Frobenius elements `φ j`, form a triangle (`IsPrimeTriangle`) with bounds `D.halfGap * h` and
`D.halfGap ^ 22 * h`, where `h` is at most the valuation of `D.chosenGroupOrder`, the product of the
orders of general linear groups over the chosen residue fields. Each `N x` has the weights `wt` and
the type made from `c` and `O.rankDiff` eigenvalues `1` (`IsRepOfType`), and
`(N x g - ϑ.invAvatar g) (N x g - 1) = 0` on inertia above `ϑ.Q` and its conjugate. Each system in
`𝓧` lifts a row with a twisted lattice, and for `sys x₀` the Selmer length of the twisted row is at
most the finite `sel` (`IsLiftWithTwistedLattice`). The module `𝒥` holds `ℓ ^ ν` times all traces of
the `N x`, and the traces of the relations, with polynomials `e j` of value `1` at `1`, that tie
`tame j` to `φ j` (`IsTraceIdeal`). Then one family `f` of polynomials in the `X j` multiplies every
family `x ↦ det (1 - N x g)` into `𝒥`, has on `𝓧` no monomial properly dividing `∏ X j`, and has at
`x₀` a coefficient `d` of `∏ X j` with `D.chosenGroupOrder ^ 2 * d` of valuation at most
`liftValuationBound ℓ O ram sel`. 

### `exists_ellVal_le_and_diagOp_mem_ellIntegralForms`

 The operator at a base system `x₀ ∈ 𝓧`. Let the types `c` form a lift setting for the pair `O`
and the twist `ϑ`, of ramification at most `ram`. Let each system in `𝓧` lift a row with a twisted
lattice, the Selmer length for `x₀` being at most the finite `sel`. Let `B` be base data. At every
level made of places outside `badPlaces D ℓ`, let each system of `B` have as normalised
representation `N x` one of the weights `wt` and the type made from `c` (`IsRepOfType`), with
`(N x g - ϑ.invAvatar g) (N x g - 1)` zero on inertia above `ϑ.Q` and its conjugate. Then at some
level `L` there are eigenvalues `s` such that: (a) `D.chosenGroupOrder ^ 2 * s x₀` has valuation at
most `liftValuationBound ℓ O ram sel = sel + 2 * O.rankDiff * ram + card r * localDefectBound D
ℓ + denominatorError D ℓ`; (b) if `l` and `y` are forms of base level, `D.chosenGroupOrder • l` is
integral, `y` is supported on `𝓧` and `l`, `y` have the same components outside the base systems
that are not weak lifts (weak lift: all characteristic polynomials have the root `1`), then
`D.chosenGroupOrder • D.chosenGroupOrder • B.diagOp s y` is integral. Here `B.diagOp s` scales each
system `x` by `s x`, and `D.chosenGroupOrder` is the product of the orders of general linear groups
over the chosen residue fields. 

### `exists_heckePolyOnForms_eq_zero`

 There is a split place `w`, off the places of `O` and their conjugates, at which the Hecke
polynomial operator, evaluated at the number `O.liftHeckeRoot w` (the inverse of the largest root
`υ q ^ (O.rankDiff - 1)` of the chain that a theta lift has in its Hecke polynomial, with `q` the
norm of `w` and `υ` the Frobenius value of `O.charW`), kills every nonzero form `v` of base level
that lies in a system `x` which is a weak lift: at every Galois element the characteristic
polynomial of the normalised representation of `x` has the root `1`. 

### `typeProjection_sub_starProjection_mem`

 Let `typeProjection O c` be the action on forms of the idempotent of the tuple of types `c`,
with range in the image of the element `E` of the group algebra. Let `Z` be stable under it and
under the Hecke polynomial operators `O.heckePolyOnForms`, and let `y` be orthogonal to the false
lifts: the forms in `Zᗮ` and the image of `E` that, at some split place, the Hecke polynomial
operator at its lift Hecke root `O.liftHeckeRoot`, the value expected of a lift, kills. If at one
split place `w` this operator kills the nonzero isotypic forms in the range of `typeProjection O c`
that lie outside `M`, then `typeProjection O c` takes the component of `y` orthogonal to `Z` into
`M`. 

### `IsLiftGenerator`

 A lift generator of `Z`: a form in `Z`, in the range of an apt projection inside the image of
`E`, that lifts a system with a main summand whose twist by `ϑ.invAvatar` has a Selmer group with
divisible coefficients of length at most `sel` (`HasDivisibleSelmerLengthLe`). 

### `IsLiftGenerator.mem`

 The form lies in `Z`. 

### `IsLiftGenerator.exists_type`

 The form is in the range of `typeProjection O c` for a type `c` in lift setting, inside the
  image of `E`. 

### `IsLiftGenerator.exists_hasLiftHeckePolynomial`

 The form lifts a system with a main summand `R` for a pair `V` with
  `O.u1Char = V.u1Char * ϑ.toAutChar`, and the Selmer group with divisible coefficients of the
  twisted main summand has length at most `sel`. 

### `IsLiftGenerator.mono`

 A lift generator for the bound `sel` on the length of its Selmer group is one for every larger
bound. 

### `span_mem_invtSubmodule_heckePolyOnForms`

 A lift (`O.HasLiftHeckePolynomial`: a form whose Hecke polynomials are those of the lift of some
eigenvalues `z`) is an eigenvector of every Hecke polynomial operator, so the span of a set of lifts
is stable under these operators. 

### `IsLiftGenerator.typeProjection_eq_zero_or_mem_range`

 Let `v` be a lift generator (`IsLiftGenerator`) for the pair of hermitian spaces `O`: a form in
`Z`, in the range of `typeProjection O c'` for some tuple of types `c'` compatible with the twist
`ϑ` (a lift setting) and with this range in the image of `E`, that lifts Hecke eigenvalues of a
rank-`r` main summand whose twisted Selmer group has length at most `sel`. Then for every `c`,
either `typeProjection O c` kills `v`, or `v` lies in its range and is a nonzero form of some system
`x`, a space of forms with given Hecke eigenvalues. 

### `IsLiftGenerator.exists_isMainSummandLike`

 Let `v` be a lift generator (`IsLiftGenerator`): a form in `Z`, of a type forming a lift setting
for `ϑ` whose forms all lie in the image of `E`, that lifts Hecke eigenvalues with a main summand
whose twist has a Selmer group of length at most `sel`. Let `v` be a nonzero form of the system `x`.
Then `x` lifts an `r`-dimensional Galois representation `R` with the properties of a main summand
for weights `wt` (`IsMainSummandLike`): the trace of the normalised representation of `x` is that of
`R` twisted by `ϑ.invAvatar`, the avatar of `ϑ⁻¹`, plus the first `O.rankDiff` powers of the inverse
cyclotomic character (`HasLiftTrace`). For some Galois element `γ` that acts on a lattice in the
twist by the scalar `y`, the Selmer group with divisible coefficients of the twist, with auxiliary
places `ϑ.Q`, has length at most `sel`. 

### `span_isLiftGenerator_mem_invtSubmodule_heckePolyOnForms`

 Let `w` be a split place such that neither `w` nor its conjugate lies in `O.places`, the places
of the level of the pair `O`, and let `ξ` be any complex number. The Hecke polynomial operator at
`w`, evaluated at `ξ`, preserves the span of the lift generators (`IsLiftGenerator`): the forms in
`Z`, of a type compatible with the twist `ϑ` (a lift setting) whose forms all lie in the image of
`E`, that lift Hecke eigenvalues of a rank-`r` main summand whose twist has a Selmer group of length
at most `sel`. 

### `span_isLiftGenerator_mem_invtSubmodule_typeProjection`

 For every tuple `c` of types, the action `typeProjection O c` on forms of the idempotent of `c`
preserves the span of the lift generators (`IsLiftGenerator`): the forms in `Z`, of a type
compatible with the twist `ϑ` (a lift setting) whose forms all lie in the image of `E`, that lift
Hecke eigenvalues of a rank-`r` main summand whose twist has a Selmer group of length at most
`sel`. 

### `span_isLiftGenerator_mem_invtSubmodule`

 Consider the span of the lift generators (`IsLiftGenerator`): the forms in `Z`, of a type
compatible with the twist `ϑ` (a lift setting) whose forms all lie in the image of `E`, that lift
Hecke eigenvalues of a rank-`r` main summand whose twist has a Selmer group of length at most
`sel`. It is stable under the Hecke polynomial operators `O.heckePolyOnForms`, at every value `ξ`
and every split place `w` (`star w ≠ w`) such that neither `w` nor its conjugate lies in
`O.places`, the places of the level. It is also stable under `typeProjection O c`, the action on
forms of the idempotent of the tuple of types `c`. 

### `typeProjection_sub_starProjection_mem_of_isOrthogonalToFalseLifts`

 Let the types `c` form a lift setting for the pair `O` and the twist `ϑ`, auxiliary for the bad
places with ramification at most `ram`. Let `Z` be stable under the Hecke polynomials and under
`typeProjection O c`, whose range lies in the image of `E`, and let `y` be orthogonal to the false
lifts: the forms in `Zᗮ` and the image of `E` that a Hecke polynomial at its lift Hecke root kills.
If every nonzero isotypic form in the range of `typeProjection O c` outside `M` belongs to a weak
lift, then `typeProjection O c (y - Z.starProjection y)` lies in `M`. 

### `mem_integralForms_ofIso_iff`

 A form is integral at the place of `ℂ_ℓ` given by `ιℓ` (gauge at most `1` everywhere) if and
only if its algebraic form has `ℓ`-integral coordinates at the points integral above `ℓ`. 

### `IsLiftGenerator.exists_isMainSummandLike_hasTwistedLattice`

 Let `v₀` be a lift generator for the bound `sel` on the Selmer length, and a nonzero form
(`IsNonzeroIn`) of the system `x₀`. Every system `x` that contains a nonzero lift generator, with no
bound on the Selmer length, lifts a row `R` (`IsMainSummandLike`) with a twisted lattice
(`HasTwistedLattice`): the trace of the normalised representation of `x` is that of `R` twisted by
`ϑ.invAvatar`, the avatar of `ϑ⁻¹`, plus the powers `e < O.rankDiff` of the inverse cyclotomic
character, some Galois element acts on a lattice in this twist by a scalar, and for `x = x₀` the
Selmer group with divisible coefficients of the twist can be taken of length at most `sel`. 

### `diagOp_toSmoothForm_typeProjection`

 At each system `x`, `B.diagOp s' ∘ toSmoothForm ∘ typeProjection O c` multiplies a form of `x`
in the range of `typeProjection O c` by `ιℓ.symm (s' x)`. 

### `diagOp_typeProjection_eq_zero_of_mem_span`

 Let `L` be a family of places and `s` a function on `B.Eigensystem L`, the systems that contain
a nonzero form of level `L` over the base data `B`; the operator `B.diagOp s` scales each such
system `x` by `ιℓ.symm (s x)`. Let the forms of type `c`, the range of `typeProjection O c`, have
base level, and let `s` vanish at every system that contains a nonzero lift generator of `Z` for the
twist `ϑ`. Then `B.diagOp s` kills the component `typeProjection O c z` of type `c` of every form
`z` in the span of these lift generators. 

### `exists_linearMap_eq_smul_mem_integralForms`

 An operator for one lift generator. Let `ϑ` have ramification at most `ram` (`IsAuxTwist`), let
`Z` be spanned by lift generators for the bound `⊤`, and let `v₀ ≠ 0` be one for the finite `sel`.
Then a linear map `G` from the forms `O.FormV` to their algebraic forms has every lift generator as
an eigenvector, with an eigenvalue at `v₀` of `ℓ`-adic valuation at most
`liftValuationBound ℓ O ram sel`, which is `sel + 2 * O.rankDiff * ram + card r * localDefectBound D
ℓ + denominatorError D ℓ`. Let `y` be integral at `ιℓ` and orthogonal to the false lifts: the forms
in `Zᗮ` and the image of `E` that, at some split place, the Hecke polynomial at `O.liftHeckeRoot`
kills. Then every form whose algebraic form is `G` of the projection of `y` to `Z` is integral at
`ιℓ`. 

### `PreservesHeckeEigenspaces`

 The operator `Λ` on `Z` preserves every eigenspace in `Z` of every Hecke polynomial at a split
place off the places of `O` and their conjugates. 

### `preservesHeckeEigenspaces_toLin_diagonal`

 An operator on `Z` that is diagonal in a basis of lifts (`O.HasLiftHeckePolynomial`: Hecke
eigenforms that lift some system `z`) preserves the eigenspaces of the Hecke polynomials. 

### `exists_operator_ellVal_le_liftValuationBound`

 Bound for denominators. Let the twist `ϑ` have ramification at most `ram` (`IsAuxTwist`), let
`sel` be finite, and let `Z` be spanned by lift generators: forms in `Z`, of a type compatible with
`ϑ` (a lift setting) inside the image of the group-algebra element `E`, that lift Hecke eigenvalues
with main summands whose twisted Selmer groups with divisible coefficients have length at most
`sel`. Then an operator `Λ` on `Z` preserves the eigenspaces of the Hecke polynomials at the split
places off `O.places.conjClosure`, has eigenvalues of valuation at most
`liftValuationBound ℓ O ram sel`, which is `sel + 2 * O.rankDiff * ram + card r * localDefectBound D
ℓ + denominatorError D ℓ`, and takes to forms integral at `ιℓ` the projections to `Z` of forms
integral at `ιℓ` and orthogonal to the false lifts, which are the forms in `Zᗮ` and the image of `E`
that, at some split place, the Hecke polynomial at `O.liftHeckeRoot`, the value expected of a lift,
kills. Here `ιℓ` is the fixed isomorphism from `ℂ` to the algebraic closure of `ℚ_ℓ`. 

### `exp_le_norm_det_smul_of_ellVal_le`

 If `N * ιℓ μ` has `ℓ`-adic valuation at most `B` for every eigenvalue `μ` of `Λ`, then the
determinant of `N • Λ` has `ℓ`-adic norm at least `exp (-(finrank ℂ Z * (B * log ℓ)))`. 

### `exists_operator_det_clearingBound`

 The operator form of the bound for denominators with the clearing bound. Let the twist `ϑ` have
ramification at most `twistError ℓ D`, the small number `(4 f + 3) r v_ℓ(N) + 2 ^ (-ℓ)` with
`N = D.chosenGroupOrder`, with respect to the places above `ℓ` and the level (`badPlaces D ℓ`), and
let `Z` be spanned by lift generators (`IsLiftGenerator`): forms in `Z` of suitable type that lift
Hecke eigenvalues with main summands whose twisted Selmer groups have length at most
`twistError ℓ D`. Then some operator `Λ` on `Z` has a determinant of `ℓ`-adic norm at least
`exp (-(finrank ℂ Z * (card r * (β * log ℓ))))`, where `β = clearingBound D ℓ` adds the local
losses, error terms and `v_ℓ(N)`. It takes the projection to `Z` of every form `y'` integral at `ιℓ`
and orthogonal to the false lifts to a form integral at `ιℓ`, whose pairings with the forms integral
at all places above `ℓ` are integral. 

### `denominatorLe_clearingBound`

 Denominators for a good twist. Let `ι.ιℓ` be the isomorphism from `ℂ` to the algebraic closure
of `ℚ_ℓ` that `ι` chooses, and `ψ = ϑ.invAvatar` the `ℓ`-adic avatar of `ϑ⁻¹` for it. Let
`β = clearingBound D ℓ`, the sum of the local losses, the error terms and the valuation of
`D.chosenGroupOrder`; the small number `twistError ℓ D` is one of these terms. Assume: (i) the set
`ϑ.Q` is auxiliary for `ψ` and the places above `ℓ` and the level (`badPlaces D ℓ`), with
ramification at most `twistError ℓ D` (`IsAuxTwist`); (ii) `Z` is spanned by lift generators
(`IsLiftGenerator`): vectors of `Z` of a type `c` that forms a lift setting inside the image of `E`,
each lifting Hecke eigenvalues `z` with a main summand `R` for some pair `V` with
`O.u1Char = V.u1Char * ϑ.toAutChar`, where the Selmer group of `ψ R` with divisible coefficients has
length at most `twistError ℓ D`. Then `DenominatorLe` holds for `E` and `Z` with exponent `β log ℓ`:
some operator on `Z` with determinant of `ℓ`-adic norm at least
`exp (-(finrank ℂ Z * (card r * (β * log ℓ))))` takes the projection to `Z` of each form integral at
`ι.ιℓ` and orthogonal to the false lifts to a form that is integral at `ι.ιℓ` and has integral
pairings with the forms integral at all places above `ℓ`. 
