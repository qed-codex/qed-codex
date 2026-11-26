---
{
  "module": "src/New/Congruences/FitTwistsExist.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FitTwistsExist.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FitTwistsExist.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# All data have regular families of m-fold twists

This file states the conclusion of the Selmer group argument.

* `New.exists_isRegularFamily`: for all data `D` there is a family of `m`-fold twists, one for each
  prime `ℓ` and isomorphism `ι : ℂ ≃ ℚ̄_ℓ`, that is regular (`New.Data.IsRegularFamily`): for the
  first `m` powers of its members the inverse ratios of `L`-values have height at most `D.x₁`, and
  the logarithms of the denominators of the projections to lifts sum over the primes to at most
  `D.denominatorBudget`.
* `New.Selmer.exists_mFoldTwist_hasDenominatorsLe`: the twist for one prime and one isomorphism.
* `New.Selmer.range_goodLift_le_span_hasLiftHeckePolynomial`: the lifts are spanned by forms that
  lift one of finitely many eigensystems, which do not depend on the twist.

Notions from other files:
* `New.Data.MFoldTwist`: a twist ϑ whose tame part ψ has ψ_wⁿ non-trivial for all places w in its
  set Q and 1 ≤ n ≤ m.
* `New.Data.IsNegligible`: nonnegative reals `e l` with `∑ e l log l ≤ x ^ C` over every finite set
  of primes, where `x = D.x` is the length of the prime sum, the smallest scale of the data.
* `New.Selmer.IsMainSummand`: an `ℓ`-adic Galois representation satisfies the local and global
  conditions `IsMainSummandLike` and, up to a twist and a string of characters, gives the traces of
  the representations attached to the lifts of a Hecke eigensystem, for all twists of a descent
  pair.
* `New.Selmer.DenominatorLe`: an operator `Λ` on a space `Z` of forms, with determinant of norm at
  least `exp (-(dim Z · r · β))` at `ι`, clears the denominators of the orthogonal projection to
  `Z`. Here `r` is the rank of the source of the lift.

## Relation to the literature

For each prime ℓ and each identification of the complex numbers with the algebraic closure of the
ℓ-adic numbers, there is a twist whose first m powers have few congruences. For these twists, the
denominators of projections to theta lifts and the divisibility of ratios of Hecke values sum over
all ℓ to a total that the heights afford. It is known that denominators of projections to lifts give
Selmer classes and that twisting lowers Selmer ranks. Related work: Prasanna, Integrality of a ratio
of Petersson norms, 2006 (after Ribet, 1976; Wiles); Klosin, Congruences among modular forms on
U(2,2) and the Bloch–Kato conjecture, 2009; Mazur–Rubin, Ranks of twists of elliptic curves, 2010.


### `New.Selmer.DenominatorLe.clearsProjection`

 Let the projection to the space `Z` of lifts have denominator at most `exp β` per dimension of
`Z` and per unit of the rank `r` of the source (`DenominatorLe`). If `β ≤ β'`, then some operator
with determinant of norm at least `exp (-(dim Z · r · β'))` clears this denominator
(`New.Data.ClearsProjection`). 

### `New.Selmer.sum_padicValNat_mul_log_le`

 Summed over a finite set `T` of primes `l` with weights `log l`, the `l`-adic valuations of a
natural number `a` are at most `log b` for every natural number `b ≥ a`. 

### `New.Selmer.prod_Ioc_natB_le_pow`

 Let `natB` be the weight `b` of the data `D` as a natural number, and `halfGap = r ^ 8`. The
product of the natural numbers `k` with `natB - 30 halfGap³ < k ≤ natB + 30 halfGap³` (truncated
subtraction), which enters the crystalline loss `crystallineLoss`, is at most
`(natB + 30 halfGap³) ^ (60 halfGap³)`. 

### `New.Selmer.sum_defectBound_mul_log_le`

 Let `m` be the number of lifts, `r` the rank of the target, `k = r + 1 - m` the rank of the
source, `b = D.natB` the weight as a natural number, `h = D.halfGap = r ^ 8`, and `M = D.M` the
product of the two level primes. The local loss `defectBound D l` is
`10⁶ (m / k) (b v_l(M) + v_l((2 b)! Π ^ h³))`, where `v_l` is the `l`-adic valuation and `Π` is the
product of the positive integers in `(b - 30 h³, b + 30 h³]`. Summed over any finite set `T` of
primes `l` with weights `log l`, these losses are at most
`10⁶ (m / k) (b log M + log ((2 b)! (b + 30 h³) ^ (60 h⁶)))`. 

### `New.Selmer.sum_localDefectBound_mul_log_le`

 **Bound for the local loss.** The numbers `localDefectBound D l = 4 f · defectBound D l` have
`∑ localDefectBound D l · log l ≤ 4 · 10⁶ e¹⁸⁰ f (m / k) b log b` over every finite set `T` of
primes. Here `f` is the number of infinite places of `D.E`, `m` the number of lifts, `k = r + 1 - m`
the rank of the source, `b = exp D.logB` the weight, and `defectBound D l` is `10⁶ (m / k)` times a
sum of `l`-adic valuations of integers attached to `D`. 

### `New.Selmer.isNegligible_padicValNat_oddClassBound`

 **The odd classes are few.** The integer `oddClassBound D` is at most `2 ^ (4 (N + t + 3) ^ 27)`
times the class number of `D.E`, for the cyclotomic conductor `N`. Its `l`-adic valuation bounds the
lengths of the groups of odd classes (`shaOdd`), Galois cohomology classes of `D.E` with
coefficients in Tate twists of `O/l^ν`. These valuations are negligible with the exponent `2000`:
with weights `log l` they sum to at most `D.x ^ 2000` over every finite set of primes. 

### `New.Selmer.isNegligible_twistError`

 The numbers `twistError l D = (4 f + 3) r v_l(D.chosenGroupOrder) + 2⁻ˡ` are negligible with
the exponent `999`: with weights `log l` they sum to at most `D.x ^ 999` over every finite set of
primes. 

### `New.Selmer.isNegligible_denominatorError`

 The error term `denominatorError D l` of the bound for the denominators of projections to lifts
is finite: it is an explicit combination of the `l`-adic valuations of `oddClassBound D`, the bound
for odd Galois cohomology classes, and `D.chosenGroupOrder`, the order of a product of general
linear groups over residue fields. These terms are negligible with the exponent `4000`: with weights
`log l` they sum to at most `D.x ^ 4000` over every finite set of primes. 

### `New.Selmer.isNegligible_padicValNat_card_stdClasses`

 The `l`-adic valuations of the class number of `U(1)` at the level `D.chosenLevel` (the number
of double cosets `StdClasses`) are negligible with the exponent `30`: with weights `log l` they sum
to at most `D.x ^ 30` over every finite set of primes. 

### `New.Selmer.sum_clearingBound_add_padicValNat_le`

 The number `clearingBound D l` is the bound for the exponent of `l` in the denominator of a
projection to lifts, per dimension and per unit of rank of the source: a sum of the local loss
`localDefectBound D l`, multiples of the twist and error terms, and the valuation of
`D.chosenGroupOrder`. The number of `StdClasses` at the level `D.chosenLevel` is the class number of
`U(1)` there. Summed over a finite set `T` of primes `l` with weights `log l`, the clearing bounds
and the `l`-adic valuations of this class number are at most
`D.denominatorBudget = D.errorUnit / (m k)`, for `m` the number of lifts and `k = r + 1 - m`. 

### `New.Selmer.isRepOfType_one`

 A descent pair `O` consists of the data of a theta lift from a hermitian space `W` to one of
rank `#n`: a finite set of level places, a character of `U(1)` with its weight and tame part, and
the weight of the forms. Here `W` has rank one (index type `Unit`), and `O.ChosenIndex` indexes the
chosen places of `O`. The label of each chosen place, a polynomial over its residue field, is taken
to be `X - 1`. Then the trivial `ℓ`-adic representation of rank one satisfies `IsRepOfType`: it is
conjugate self-dual with the parameter `1`, meets the local conditions of `IsConjSelfDualOfLevel` at
all finite places (the level is `∅`) with the single jump `0` at each embedding of `D.E` in `ℂ`, and
inertia at each chosen place acts through the root of the label. 

### `New.Selmer.exists_isMainSummand_mainPair`

 A critical pair `(ν, z)` is a main pair for an index `1 ≤ j ≤ m` if `m < z ≤ r`, the tame part
of `ν` is `D.chiMLocal ^ j`, and the weight `-c` of `ν` has `w + r - t ≤ c ≤ w` at each infinite
place, for `w = D.liftWeight j`. Here `m` is the number of lifts, `r = D.r`, `t = D.t`, and
`D.chiMLocal` is the fixed family of residue characters that is trivial off the chosen places. The
data `lValueData` describe the theta lift of `ν`, untwisted, from `U(1)` to `U(2 z)`. Then there is
an `ℓ`-adic representation `T` of rank one that is a main summand (`IsMainSummand`) for this lift
and the constant system `1` of Hecke eigenvalues: `T` satisfies `IsMainSummandLike`, and for every
twist of the lift the Galois representations attached to lifted eigenforms have, up to
normalisation, the trace of the twisted `T` plus a string of characters. 

### `New.Selmer.range_goodLift_le_span_hasLiftHeckePolynomial`

 **Splitting, pairs of rank `r`.** Let `ϑ` be a twist and `1 ≤ j ≤ m`. The map `D.goodLift ϑ j`
is the theta lift, for the data `D.descentPair ϑ j`, of the good forms on the rank `r` space
`W_j = D.spaceW j`; good forms have principal level at the chosen places and lie in the image of the
idempotent `D.e₀`. Its range, the space of lifts, is spanned by its forms `y` with two properties.
* There is a tuple `c` of labels, one polynomial over the residue field at each chosen place, that
  satisfies `IsLiftSetting`: each label has degree `r`, some label over each level prime is
  primitive, and no twisted label has the root `1`. The form `y` lies in the image of the idempotent
  of `c` (`typeProjection`), which is contained in that of `D.e₀`.
* There is a system `q (w, i)` of Hecke eigenvalues, one for each finite place `w` and number `i` of
  the Hecke operator, that occurs in a good form on `W_m`, such that at the split places outside the
  level the Hecke polynomial of `y` is that of a lift of `q`. 

### `New.Selmer.exists_mFoldTwist_selmerLengthLe_inv_ratio_le`

 **The twisting theorem for two families of main summands.** Let `ℓ` be a prime,
`ι : ℂ ≃ ℚ̄_ℓ`, and `e = twistError ℓ D = (4 f + 3) r v_ℓ(D.chosenGroupOrder) + 2 ^ (-ℓ)`, where
`f` is the number of infinite places of `D.E` and `D.chosenGroupOrder` the order of a product of
general linear groups over residue fields. Let `R a` and `R₁ b` be finitely many Galois
representations of rank `r` and one, each satisfying the conditions `IsMainSummandLike` on main
summands for some self-duality parameter `t` and some multisets `J` of Hodge–Tate jumps. There is a
twist `τ`, whose tame part has nontrivial powers up to `m` at each place of its modulus
(`MFoldTwist`), such that each power `ϑ = τ ^ j`, `1 ≤ j ≤ m`, has the following properties, where
`ψ = ϑ.invAvatar` is the `ℓ`-adic Galois character of `ϑ⁻¹`.
* The modulus `ϑ.Q` is auxiliary for the places dividing `ℓ p₀ p₁ N`, for the two level primes
  `p₀, p₁` and the level `N` (`badPlaces`): its places have prime norm, avoid these places and
  their conjugates, and no two are conjugate. The character `ψ` comes from the norm-one torus, and
  the valuations of `ψ σ - 1`, for tame generators `σ` at the places of `ϑ.Q`, sum to at most `e`
  (`IsAuxTwist`).
* For each given representation, some Galois element `γ` acts on a lattice in its twist by `ψ` as a
  scalar `ζ`, and the crystalline Selmer group of that lattice with coefficients in `Frac O / O`
  has length at most `e`, normalised so that `O / ℓ` has length one, for all large coefficient
  rings `O` (`HasDivisibleSelmerLengthLe`).
* For each pair `p = (ν, z)` ramified exactly at the chosen places and each sign `s`, the inverse of
  `p.ratio ϑ s = |L(z, (ν ϑ ^ s)⁻¹)| / |L(z, ν⁻¹)|`, a ratio of partial `L`-values, has norm at most
  `ℓ ^ e` at `ι`. 

### `New.Selmer.denominatorLe_range_goodLift`

 **Denominator for the space of lifts.** Let the modulus of the twist `ϑ` be auxiliary and its
ramification at most `twistError ℓ D` (`IsAuxTwist`). Suppose that every Hecke eigensystem `q` of
good forms on `W_m = D.spaceW D.m` has a main summand for the `j`-th descent pair of the trivial
twist `TameChar.one`. That is, there is a Galois representation `R` giving the traces attached to
all twisted lifts of `q` (`IsMainSummand`), and the twist of `R` by `ϑ⁻¹` has a short Selmer group
with divisible coefficients. Let `Z = (D.goodLift ϑ j).range` be the space of lifts for `ϑ` and `j`,
and let `r` be the size of `D.RowIndex`, the rank of `W_m`. Then some operator with determinant of
norm at least `ℓ ^ (-(dim Z · r · clearingBound D ℓ))` clears the denominators of the projection to
`Z` on integral forms orthogonal to the false lifts for the idempotent `D.e₀` of the good forms
(`DenominatorLe`). 

### `New.Selmer.denominatorLe_span_trivialLift`

 **Denominator for the line of a main pair.** Let the modulus of the twist `ϑ` be auxiliary and
its ramification at most `twistError ℓ D` (`IsAuxTwist`). Let `p = (ν, z)` be a main pair for `j`
(`IsMainPair`), with `lValueData` the data of the theta lift of `ν ϑ` from `U(1)` to `U(2 z)` and
`trivialLift` the lifted form. Let `R` be a main summand for the untwisted lift and the trivial
eigensystem whose twist by `ϑ⁻¹` has a short Selmer group with divisible coefficients. Then an
operator with determinant of norm at least `ℓ ^ (-clearingBound D ℓ)` clears the denominators of the
projection to the line of `trivialLift` on integral forms orthogonal to the false lifts for the
idempotent of the labels `X - 1` at the chosen places (`DenominatorLe`). 

### `New.Selmer.exists_mFoldTwist_hasDenominatorsLe`

 **A twist with few congruences at one prime.** For a prime `ℓ` and `ι : ℂ ≃ ℚ̄_ℓ` there is an
`m`-fold twist `τ` (`D.MFoldTwist`) with three properties, where `ϑ = τ ^ j` (`τ.powTwist j`) and
`j : D.LiftIndex`, so `1 ≤ j ≤ m`. The product `τ.normQ` of the norms of the places in the set `Q`
of `τ` is prime to `ℓ`. Take each ramified pair `p = (ν, z)` (`p.IsRamified`: the tame part of `ν`
is nontrivial exactly at the places dividing `D.piM`, of norm `p₀ p₁`) and each sign `s`. The
inverse of `p.ratio ϑ s = |L(z, (ν ϑ ^ s)⁻¹)| / |L(z, ν⁻¹)|` (partial `L`-values) has norm at most
`ℓ ^ e` under `ι.ιℓ`, where `e = twistError ℓ D = (4 f + 3) r v_ℓ(D.chosenGroupOrder) + 2 ^ (-ℓ)`.
For each `j`, `D.HasDenominatorsLe ι.ιℓ ϑ j β` holds, with `exp β` equal to `ℓ ^ clearingBound D ℓ`
times the `ℓ`-part of the number of classes `StdClasses` of `U(1)` at level `D.chosenLevel`. 

### `New.exists_isRegularFamily`

 **Twists with few congruences.** All data `D` have a regular family of `m`-fold twists `θ κ`,
one for each pair `κ` of a prime `ℓ` and an isomorphism `ℂ ≃ ℚ̄_ℓ`. The modulus of `θ κ` is prime to
`ℓ`. 
