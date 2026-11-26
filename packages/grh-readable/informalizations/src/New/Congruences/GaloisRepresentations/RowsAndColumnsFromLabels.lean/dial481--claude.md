---
{
  "module": "src/New/Congruences/GaloisRepresentations/RowsAndColumnsFromLabels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/RowsAndColumnsFromLabels.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/RowsAndColumnsFromLabels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Main summands and conjugate self-dual representations from type polynomials

Let `O` be a descent pair (`New.DescentPair`) with type polynomials `c` in a lift setting
(`New.Selmer.IsLiftSetting`). This file describes inertia on representations of a type for `O` and
on representations attached to its eigenforms.

* `New.Selmer.exists_inertiaGroup_isInertiaSpectrum`: inertia elements above the primes
  `D.levelPrime 0` and `D.levelPrime 1` are killed by polynomials whose roots are roots of unity of
  controlled order (`New.Selmer.IsInertiaSpectrum`).
* `New.Selmer.IsRepOfType.isMainSummandLike`: a representation of a type of rank `card r` and empty
  level, with jumps as in `New.Selmer.IsMainSummandWeights`, is a main summand
  (`New.Selmer.IsMainSummandLike`).
* `New.Selmer.isFiniteTypeAt_and_polyKillsAt_of_mem_conjClosure`: a representation attached to an
  eigenform of parahoric type at the auxiliary places (`New.Selmer.HasTwistParahoricType`) has no
  monodromy above `ϑ.Q` and its conjugates, and a quadratic polynomial kills inertia there.
* `New.Selmer.normalisedRep_quadratic_on_inertia`: its normalised representation satisfies the same
  quadratic relation on inertia above `ϑ.Q` and its conjugates.

Notions from other files:
* `New.Selmer.IsLiftSetting O c ϑ`: the places of `O` are the chosen places above `D.levelPrime 0`,
  `D.levelPrime 1` and those of `ϑ.Q`, its character is a power of `D.chiMLocal` times `ϑ.tamePart`,
  and `c` are type polynomials of degree `card r`.
* `New.Selmer.IsRepOfType O k J c S R`: `R` is a conjugate self-dual representation of given level
  (`New.Selmer.IsConjSelfDualOfLevel`: on traces `R^c ≅ R^∨(1 - k)`, with Hodge–Tate jumps `J` and
  local conditions off the level `S` and above `ℓ M`), and inertia at the chosen places acts through
  the roots of the type polynomials `c` over the residue fields.
* `New.ClosurePlace`: a place of the algebraic closure `Ω` of `ℚ`, that is, a valuation subring;
  `conjPlace A` is the complex conjugate place, and `AbsGal D` is `Gal(Ω/D.E)`.
* `New.Data.IsChosen`: a place of `D.E` is chosen if it divides `D.piM`, an integer whose product
  with its conjugate is `M = D.levelPrime 0 * D.levelPrime 1`.
* `New.GaloisRep.PolyKillsAt R A s P`: `P` kills `s` at the place `A`, that is, `P (R s) = 0` off
  `ℓ`, and an analogue for Weil pairs (`New.Period.IsKilledBy`) above `ℓ`.
* `New.Selmer.scaledTypePoly`: the scaled type polynomial, `c i` with its roots multiplied by the
  element of the residue field that names the character `(O.tamePart w)⁻¹`, `w = O.chosenPlace i`.
* `New.ellVal`: the `ℓ`-adic valuation with values in `[0, ∞]`.
* `New.Data.Twist`: a tame character (`New.Data.TameChar`) whose tame part is non-trivial at every
  place of its set `Q`.

## Relation to the literature

See `New.Congruences.GaloisRepresentations.RowsFromEigensystems` for related work.


### `norm_pow_sub_pow_eq_one`

 Let `x` be a root of unity in `ℚ̄_ℓ`. If `(x ^ a) ^ ℓ ^ u ≠ (x ^ b) ^ ℓ ^ u` for all `u`, then
`x ^ a - x ^ b` has norm `1`. 

### `ellVal_det_sub_one_le_card_mul`

 Let the matrix `Z` be killed by the polynomial with roots `μ`, where each member `y` of `μ` is
different from `1` and satisfies `y ^ (D.levelPrime i ^ d - 1) = 1` for some `1 ≤ d ≤ D.r`. Then the
`ℓ`-adic valuation of `det (Z - 1)` is at most `card r` times that of `D.chosenGroupOrder`. 

### `not_q₂_dvd_mul_pow_mul`

 Let `D` be the data of the construction with parameters `P`, so that `D.m` is the number of
lifts and `D.r` the rank of the target, and let `1 ≤ j ≤ D.m`, `1 ≤ t ≤ 4 * D.r + 2`. Let
`s = D.towerExp`
be the exponent with `2 ^ s = D.m ^ 22`. The number `P.q₂ s` is a multiple of `P.q₀ ^ s` and is the
order of the fixed residue field characters `D.chiMLocal` at the chosen places of `D.E` above the
level. It does not divide `j * t` times a power of `ℓ`. 

### `IsInertiaSpectrum`

 A multiset `μ` of possible eigenvalues of `s` at the place `A` of `Ω = ℚ̄`, common to all
representations `R` of a type of rank `card m` whose type polynomials are the scaled type
polynomials `scaledTypePoly O c i` times `(X - 1) ^ t`; the duality twist `k`, the jumps `J` and the
level `S` of `R` are arbitrary. It consists of `card r + t` roots of unity whose orders are bounded
through `p = D.levelPrime l`. On every such representation the polynomial with roots `μ` kills `s`
at `A`, and kills `conjGal s⁻¹` at the complex conjugate place `conjPlace A`. Here `conjGal` is
conjugation by complex conjugation, and off `ℓ` "`Q` kills `s`" (`PolyKillsAt`) means
`Q (R s) = 0`. 

### `IsInertiaSpectrum.card_eq`

 `μ` has `card r + t` members. 

### `IsInertiaSpectrum.pow_factorial_eq_one`

 Each member of `μ` has order dividing `p ^ (card r)! - 1`, `p = D.levelPrime l`. 

### `IsInertiaSpectrum.exists_pow_eq_one`

 Each member of `μ` has order dividing `p ^ d - 1` for some `1 ≤ d ≤ D.r`. 

### `IsInertiaSpectrum.polyKillsAt`

 On every such representation, the polynomial with roots `μ` kills `s` at `A`. 

### `IsInertiaSpectrum.polyKillsAt_conjPlace`

 On every such representation, the polynomial with roots `μ` kills `conjGal s⁻¹` at the
  conjugate place. 

### `IsInertiaSpectrum.of_conjPlace`

 If `μ` is an inertia spectrum (`IsInertiaSpectrum`: a multiset of possible eigenvalues) of
`conjGal s⁻¹` at the conjugate place `conjPlace A`, then `μ` is also an inertia spectrum of `s` at
`A`. 

### `exists_isInertiaSpectrum_chosenPlace`

 The eigenvalues of inertia at a chosen place. Let `O.chosenPlace i` divide `p = D.levelPrime l`,
and let `A` be a place of `Ω = ℚ̄` over it. Each `s` in inertia at `A` has a multiset `μ` of
`card r + t` roots of unity (`IsInertiaSpectrum`), each of order dividing `p ^ (card r)! - 1` and
some `p ^ d - 1`, `1 ≤ d ≤ D.r`, such that the polynomial with roots `μ` kills `s` at `A` and
`conjGal s⁻¹` at the conjugate place in every rank `card m` representation with type polynomials
`scaledTypePoly O c i * (X - 1) ^ t`. Moreover `1 ∉ μ` if `t = 0` and `s` is `hA.tameGenerator`, the
fixed generator of tame inertia at `A`. 

### `exists_inertiaGroup_isInertiaSpectrum`

 The eigenvalues of inertia above the two primes `D.levelPrime l` of the level. Let `v` be a
place of `D.E` dividing `p = D.levelPrime l` and `A` a place of `Ω = ℚ̄` over `v`. There is `γ` in
inertia at `A`, the fixed generator `hA.tameGenerator` of tame inertia if `v` is chosen, such that
each `s` in inertia has a multiset `μ` of `card r + t` possible eigenvalues (`IsInertiaSpectrum`),
with `1 ∉ μ` if `t = 0` and `s = γ`. These are roots of unity of order dividing `p ^ (card r)! - 1`
and some `p ^ d - 1`, `1 ≤ d ≤ D.r`, and the polynomial with roots `μ` kills `s` at `A`, and
`conjGal s⁻¹` at the conjugate place, in every rank `card m` representation whose type polynomials
are the `scaledTypePoly O c i` times `(X - 1) ^ t`. 

### `IsRepOfType.exists_map_pow_eq_one_and_ellVal_det_le`

 Ramification of a representation of a type above `M = D.levelPrime 0 * D.levelPrime 1`. Let `R`
be a rank `card r` representation of a type (`IsRepOfType`) and empty level: conjugate self-dual of
weight `k` with Hodge–Tate jumps `J`, unramified off `ℓ M`, inertia at each `O.chosenPlace i` acting
through the roots of `scaledTypePoly O c i`. Let `A` lie over a place `v` that divides `M`
(`placesAboveM`) but not `ℓ`. Then `R` is trivial on the `N`-th powers of the inertia group of `A`
in `AbsGal D = Gal(Ω/D.E)` for some `N` that is a unit at `A`. For some `γ` in inertia, the fixed
tame generator if `v` is chosen, the `ℓ`-adic valuations of the determinants of `R γ - 1` and
`R (conjGal γ)⁻¹ - 1` are at most `card r` times that of `D.chosenGroupOrder`, the product of the
orders of `GL (D.r * D.t)` over the residue fields at the chosen places. Here `conjGal γ` is the
conjugate of `γ` by the chosen complex conjugation `cmConj` of `Ω`. 

### `IsCommonRootPower`

 The roots of the scaled type polynomial `scaledTypePoly O c i`, taken in an algebraic closure of
the residue field of `O.chosenPlace i`, have the common `e`-th power `y`, of large order relative to
`j`. With `q` the order of the residue field, each root is fixed by the `q ^ card r`-th power, and
its Frobenius conjugates stay distinct after raising to powers of `ℓ`. 

### `IsCommonRootPower.pow_eq`

 Each root `ξ` has `ξ ^ e = y`. 

### `IsCommonRootPower.pow_q_pow_card_eq`

 Each root is fixed by the `q ^ card r`-th power. 

### `IsCommonRootPower.injOn_pow`

 For each root `ξ` and each `u`, the powers `(ξ ^ q ^ a) ^ ℓ ^ u`, `a < card r`, are
  distinct. 

### `IsCommonRootPower.dvd_of_pow_eq_one`

 If `y ^ x = 1` then `P.q₂ D.towerExp`, the order of `D.chiMLocal` at the chosen places,
  divides `j * x`. 

### `IsLiftSetting.exists_isCommonRootPower_of_isPrimitivePolynomial`

 Let `c` be a lift setting for the descent pair `O` and the twist `ϑ`, so that `c i` is a type
polynomial over the residue field, of order `q`, of the place `O.chosenPlace i` above the level, and
let `O.tamePart = D.chiMLocal ^ j * ϑ.tamePart`, where `D.chiMLocal` has order `N = P.q₂ D.towerExp`
at the chosen places (`P`: the parameters of the data `D`). Let `card r = D.r` and let `c i` be a
primitive polynomial: monic irreducible of degree `card r` with a root of order `q ^ card r - 1`.
Then the roots `ξ` of the scaled type polynomial `scaledTypePoly O c i` have a common `e`-th power
`y` such that, for every `x : ℕ`, `y ^ x = 1` forces `N ∣ j * x`; moreover (`IsCommonRootPower`)
`ξ ^ q ^ card r = ξ`, and for each `u` the powers `(ξ ^ q ^ a) ^ ℓ ^ u`, `a < card r`, are
distinct. 

### `IsLiftSetting.exists_isCommonRootPower_of_eq_X_sub_one`

 Let `c` be a lift setting for the descent pair `O` and the twist `ϑ`, so that `c i` is a type
polynomial over the residue field, of order `q`, of the place `O.chosenPlace i` above the level, and
let `O.tamePart = D.chiMLocal ^ j * ϑ.tamePart`, where `D.chiMLocal` has order
`N = P.q₂ D.towerExp` at the chosen places (`P`: the parameters of the data `D`). Let `card r = 1`
and `c i = X - 1`, so that `scaledTypePoly O c i` has as only root `ξ` the element naming
`O.tamePart⁻¹`. Then some power `y = ξ ^ e` has the property that, for every `x : ℕ`, `y ^ x = 1`
forces `N ∣ j * x`; moreover (`IsCommonRootPower`) `ξ ^ q = ξ`, the remaining condition being
empty in rank `1`. 

### `IsLiftSetting.exists_isCommonRootPower`

 Let `c` be a lift setting for the descent pair `O` and the twist `ϑ`, so that `c i` is a type
polynomial over the residue field, of order `q`, of the place `O.chosenPlace i` above the level, and
let `O.tamePart = D.chiMLocal ^ j * ϑ.tamePart`, where `D.chiMLocal` has order `N = P.q₂ D.towerExp`
at the chosen places (`P`: the parameters of the data `D`). Let `c i` be primitive with
`card r = D.r`, or `X - 1` with `card r = 1`. Then the roots `ξ` of `scaledTypePoly O c i` have a
common `e`-th power `y` such that, for every `x : ℕ`, `y ^ x = 1` forces `N ∣ j * x`; moreover
`ξ ^ q ^ card r = ξ`, and for each `u` the powers `(ξ ^ q ^ a) ^ ℓ ^ u`, `a < card r`, are
distinct. 

### `IsRepOfType.exists_inertia_isRoot_charpoly`

 Let `c` be a lift setting for the descent pair `O` and the twist `ϑ`. Let `R` be a rank `card r`
representation of `AbsGal D = Gal(Ω/D.E)` over `ℚ̄_ℓ` of empty level whose inertia at each chosen
place acts through the roots of `scaledTypePoly O c i` (`IsRepOfType`), these being the roots of
`c i` times the element naming `O.tamePart⁻¹`. Let the place `A` of `Ω = ℚ̄` lie over
`O.chosenPlace i` and not over `ℓ`. There are `s` in inertia at `A` and an injective multiplicative
map `τ` from the algebraic closure of the residue field to `ℚ̄_ℓ` such that `R s` is killed by every
polynomial that vanishes on the images of the roots of the scaled type polynomial, and one image
`τ ξ`, a root of unity, is an eigenvalue of `R s`. 

### `eventually_span_eq_top_and_exists_scalar_of_tame_pair`

 Let `A` be a place of `Ω = ℚ̄`, not over `ℓ`, over the place `w` dividing `D.levelPrime l`, with
residue field of order `q`. Let the representation `R` of rank `card r` have finite type at `A` and
be trivial on the `N`-th powers of inertia, `N` a unit at `A`. Let `s` in inertia have
`R (s ^ q ^ card r) = R s` and an eigenvalue `ζ`, a root of unity, whose conjugates `ζ ^ q ^ a`,
`a < card r`, are pairwise incongruent. Then over all large coefficient rings the image of a lattice
in `R` spans all matrices and has a scalar matrix at an element of cyclotomic character
`D.levelPrime m ^ card r` for some `m`. 

### `IsRepOfType.isMainSummandLike`

 Let `c` be a lift setting for the descent pair `O` and the twist `ϑ`, and let
`M = D.levelPrime 0 * D.levelPrime 1`. Let `R` be a representation of a type of rank `card r` and
empty level: in particular `R^c ≅ R^∨(1 - k)` on traces, `R` has Hodge–Tate jumps `J` and is
unramified off `ℓ M`, and inertia at `O.chosenPlace i` acts through the roots of
`scaledTypePoly O c i`. Let `k` and `J` satisfy `IsMainSummandWeights`: `k ≤ D.t`; for one
`j ≤ D.m` each jump `u` has `D.gap / 4 ≤ |u| ≤ 2 D.m D.gap` or is within `D.t` of `-D.liftWeight j`
(of `D.liftWeight j` at embeddings outside the CM type); at most `card r * D.m / D.k` jumps at an
embedding have `|u| ≤ 2 D.halfGap ^ 2`, and at most `card r` at a conjugate pair are negative. Then
`R` is like a main summand (`IsMainSummandLike`): above `M` and off `ℓ`, inertia is killed by a
power prime to the place and, for some inertia element `γ`, `det (R γ - 1)` and
`det (R (conjGal γ)⁻¹ - 1)` have valuation at most `card r` times that of `D.chosenGroupOrder`; over
all large coefficient rings the image of a lattice spans all matrices and has a scalar at an element
of cyclotomic character `D.levelPrime m ^ card r`; and an inertia element above `M` acts by a scalar
`y` with `y ^ (ℓ ^ a * t) - 1` a unit for all `a` and `1 ≤ t ≤ 4 * card r + 2`. 

### `invAvatar_eq_of_isTameExponent`

 Let `ϑ` be a twist, that is, a tame Hecke character with tame part `ϑ.tamePart` non-trivial on
its set of places `ϑ.Q`, and let `ϑ.invAvatar` be the `ℓ`-adic avatar of `ϑ⁻¹`, the Galois character
with values in `ℚ̄_ℓ` obtained through the fixed isomorphism `ιℓ : ℂ ≅ ℚ̄_ℓ`. Let `A` be a place of
`Ω = ℚ̄` not over `ℓ`, let `w` be a place in `ϑ.Q` different from its conjugate `star w`, with
residue field `k` of order `q`, and let `T = faithfulChar k` be the fixed injective character of the
algebraic closure of `k`. Let `s` have tame exponent `a` of level `f` at `A` over `w`: `s` is in
inertia, and `T` sends the residue of `s z / z` to `exp (2πi / (q ^ f - 1)) ^ a` for a
`(q ^ f - 1)`-th root `z` of a uniformiser. Then `ϑ.invAvatar` sends `s` to `ιℓ ((T ^ a) x⁻¹)`,
where `x` is the unit of `k` that corresponds to the character `ϑ.tamePart w` under the isomorphism
`charName T`. 

### `isSplit_twistPlace`

 Each place `O.twistPlace i` of the twist of the pair `O` differs from its conjugate. 

### `HasTwistParahoricType`

 The function `f` on the finite adelic unitary group `Gf D.E n`, with values in the coordinates
`WeylIndex n O.columnCount → ℂ` of the Weyl module of weight `O.columnCount`, has the parahoric type
(`New.HasParahoricType`) of the pair `O` at `w = O.twistPlace i`, a place of the twist of `O`.
Block `0` is empty; block `1` is the complement of the range of the embedding `O.incl : r ↪ n`, with
the trivial character; block `2` is that range, with the character `(O.tamePart w)⁻¹`. So an
integral matrix at `w` whose reduction is block triangular multiplies `f` by `(O.tamePart w)⁻¹` of
the determinant of block `2` of the reduction. 

### `natCast_notMem_of_mem_conjClosure`

 If `ϑ.Q` is auxiliary (`IsAuxiliary`) for the places dividing `ℓ p₀ p₁ N` (`badPlaces D ℓ`),
then no place `w` of `ϑ.Q` or of its conjugate divides `ℓ`, that is, `ℓ ∉ w.asIdeal`. 

### `isFiniteTypeAt_and_polyKillsAt_of_mem_conjClosure`

 Let `c` be a lift setting (`IsLiftSetting`) for the descent pair `O` and `ϑ`: the places
`O.twistPlace i` are those of `ϑ.Q`, and `O.tamePart` agrees with `ϑ.tamePart` there. Let `ϑ.Q` be
auxiliary for the places dividing `ℓ * D.levelPrime 0 * D.levelPrime 1 * D.N` (`badPlaces D ℓ`): its
places have prime norm, and neither they nor their conjugates are bad. Let `R` be attached
(`Attached`) to the Hecke polynomials `H` of an eigenform `f`. Suppose that at each `O.twistPlace i`
the form `f` has the parahoric type of `O`: block triangular integral matrices act through
`O.tamePart⁻¹` of the determinant of the block indexed by `r`. Let `A` lie over a place `w` in
`Set.conjClosure ϑ.Q`. Then `R` has finite type at `A`. Also `(X - a s) (X - 1)` kills each `s` in
the inertia group of `A`, where `a = ϑ.invAvatar` is the `ℓ`-adic avatar of `ϑ⁻¹`. 

### `normalisedRep_quadratic_on_inertia`

 Let `c` be a lift setting (`IsLiftSetting`) for the descent pair `O` and the twist `ϑ`: the
places `O.twistPlace i` are those of `ϑ.Q`. Let `ϑ.Q` be auxiliary for the set `badPlaces D ℓ` of
places dividing `ℓ * D.M * D.N`: its places have prime norm, and they and their conjugates are not
bad. Let `f ≠ 0` have Hecke polynomial `H w` at almost all places `w` of prime norm (`IsEigenform`),
and the parahoric type of `O` at each `O.twistPlace i`: block triangular integral matrices act
through `O.tamePart⁻¹` of the determinant of the block indexed by `r`. Let `R` be attached to `H`:
for each `η > 0` and most Frobenius elements, the coefficients of the characteristic polynomial are
within `η` of those of `ιℓ (H w)`. Let `u = normalisedRep O R` be the twist of `R` by
`normalizingAvatar O`, the avatar of a Hecke character made from the inverse of the character
`O.charW` of the hermitian space of `O`. Then `(u g - a g) (u g - 1) = 0` for `g` in inertia above
`ϑ.Q` and its conjugates, where `a = ϑ.invAvatar` is the `ℓ`-adic avatar of `ϑ⁻¹`. 
