---
{
  "module": "src/New/Congruences/Selmer/ClassSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/ClassSums.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/ClassSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# L-values of a pair as integral measures, and avatars of tame characters

For a pair `p` (`New.Data.CriticalPair`: a character `ν` of U(1) and a point `z`) ramified at the
chosen places, ratios of the values `L(z, (ν ϑ)⁻¹)`, as `ϑ` runs over tame characters
(`New.Data.TameChar`), are interpolated over `ℂ` by integral measures. The `ℓ`-adic form is in
`New.Congruences.Selmer.LValueSystems`.

* `New.Data.CriticalPair.exists_isTwistMeasure`: a function `F` of `ϑ` that is an integral measure
  at every modulus (`New.Data.TameChar.IsIntegralMeasure`) and gives a power of the ratio of
  `L`-values `New.Data.CriticalPair.ratio` on twists (`New.Data.CriticalPair.IsTwistMeasure`); the
  cases `z ≥ 2` and `z = 1` are `New.Data.CriticalPair.isTwistMeasure_integralAlgebraicPart` and
  `New.Data.CriticalPair.exists_isTwistMeasure_of_z_eq_one`.
* `New.Selmer.exists_tameChar_invAvatar_eq`: an anticyclotomic Galois character of auxiliary
  modulus that is trivial above `ℓ` is the `ℓ`-adic avatar of the inverse of a tame character
  (`New.Data.TameChar.invAvatar`).

Notions from other files:
* `New.IsAuxiliary S I`: The places of `I` have prime norm, neither they nor their conjugates lie in
  the set `S` of places, and their conjugates lie outside `I`.
* `New.Data.CriticalPair`: A character `p.character` of U(1) of weight `-p.negWeight` with tame part
  `p.tamePart`, and an integer `p.z` with `1 ≤ z ≤ c` at every infinite place.
* `New.Data.TameChar`: A character of U(1) of weight 0, with modulus a finite set `Q` of places and
  tame part `ψ` supported on `Q`; `New.Data.Twist` is the type of those that are twists of `D`.
* `New.Data.IsChosen`: The places dividing a fixed element `D.piM` of `E`; they carry the
  tame part of a pair.
* `New.Data.CriticalPair.ratio`: The absolute value of `L(z, (ν ϑ)⁻¹) / L(z, ν⁻¹)`, without the
  Euler factors at the chosen places, in the numerator also at the modulus of `ϑ`, and their
  conjugates.
* `New.Data.CriticalPair.IsRamified`: The tame part of the pair is nontrivial exactly at the chosen
  places.

## Relation to the literature
Known result: Integral group-ring elements interpolating twisted Hecke L-values, with norm
relations. The form proved here concerns tame anticyclotomic twists of a fixed modulus, and the
elements are integral at every prime away from it at once. At integers from 2 on, the element is the
squared norm of a theta lift from U(1); at 1 it is a theta period on U(2) times its conjugate and
gives the squared value. Adding a place multiplies the element by Euler factors. Source: N. Katz,
p-adic L-functions for CM fields, Invent. Math. 49 (1978); construction as theta elements:
Bertolini, Darmon, Invent. Math. 126 (1996), adelic form Chida, Hsieh, J. reine angew. Math. 741
(2018); Euler factor: Tamagawa, Ann. of Math. 77 (1963).


### `IsTwistMeasure`

 The properties of a family `F` of values, one for each tame character, by which it interpolates
ratios of twisted and untwisted `L`-values (`p.ratio`). The set `I` holds the exponents of the
inverse Euler factors that a new place in the modulus contributes. At a twist the ratio occurs to
the power `m + 1`, times the `m`-th power of the norm of the modulus. 

### `IsTwistMeasure.apply_one_ne_zero`

 The value at the trivial character is not zero. 

### `IsTwistMeasure.isIntegralMeasure`

 At each modulus, `F` is evaluation on one combination of points whose coefficients are
  integral at every prime that does not divide the norm of the modulus. 

### `IsTwistMeasure.apply_insert`

 Adding a place `v` to the modulus multiplies `F` by the inverse Euler factors at `v` with
  the exponents in `I`. 

### `IsTwistMeasure.apply_twist`

 At a twist, `F` is its value at the trivial character times the `m`-th power of the norm of
  the modulus and the `(m + 1)`-th power of the ratio. 

### `tamePart_mul_tamePart_apply_eq_one_of_notMem`

 For a critical pair `p` and a tame character `ϑ`, the product of their tame parts is trivial at
every place off the modulus `D.twistModulus ϑ 2`, whose places are the chosen places (the places
dividing `D.piM`) and those of `ϑ.Q`. 

### `integralAlgebraicPart_insert`

 For a critical pair `p = (ν, z)`, with `ν = p.character`, let `H` say that `n` has `2 z`
elements and `z ≥ 2`. Let `ϑ` and `ϑ'` be the same tame character, with moduli `Q` and `Q ∪ {v}`.
Then `integralAlgebraicPart H`, a fixed multiple of `L(z, (ν ϑ)⁻¹)` without the chosen places, the
modulus and their conjugates, is multiplied by `(1 - a / q ^ z) * (1 - a⁻¹ / q ^ z)`, with `q` the
norm of `v` and `a` the value of the base change `x ↦ (ν ϑ)(x / x̄)` at a uniformizer at `v`. 

### `isTwistMeasure_integralAlgebraicPart`

 For a critical pair `p = (ν, z)`, let `H` say that `n` has `2 z` elements and `z ≥ 2`. Then
`integralAlgebraicPart H`, an integral multiple of the algebraic part of the twisted `L`-value at
`z`, has the properties of `IsTwistMeasure {z} 0`: it is nonzero at the trivial character; at each
modulus it is evaluation on finitely many points with coefficients integral away from that modulus
(an integral measure); it is multiplied by the inverse Euler factors with exponent `z` when a place
is added; and at a twist it is its value at the trivial character times `p.ratio`, the absolute
value of the ratio of the twisted to the untwisted `L`-value. 

### `hasWeight_mul_upsilonU1`

 For `p = (ν, z)` a critical pair with `ν = p.character` of weight `-c`, where `c = p.negWeight`,
and `ϑ` a tame character, `ν ϑ υ` has weight `-(c - 1)` and the product of the tame parts of `ν`
and `ϑ` as tame part. Here `υ = upsilonU1` is the restriction to the norm-one ideles of the fixed
splitting Hecke character of `E`. 

### `exists_mul_norm_sq_detPeriod_eq`

 Let `p = (ν, z)` be a critical pair with `ν = p.character` of weight `-c`, whose tame part is
nontrivial exactly at the chosen places, those dividing `D.piM` (`IsRamified`). For a twist `ϑ`, a
tame character whose tame part is nontrivial at each place of its modulus `Q`, let `Λ` be the period
(`detPeriod`) on the rank-two unitary group of the character `ν ϑ υ`, in weight `c - 1`, with the
modulus `D.twistModulus ϑ 2` and the product of the tame parts of `ν` and `ϑ`. Here `υ = upsilonU1`
is the restriction to the norm-one ideles of the fixed splitting Hecke character. Then there is a
constant `C`, independent of `ϑ`, such that `Λ ≠ 0`, `C ≠ 0` and `C * ‖Λ‖ ^ 2` is
`Exchange.lValueProd`: the norms of the places in `S = {w | D.IsChosen w} ∪ Q` multiplied together,
times `|L(1, (ν ϑ)⁻¹)| ^ 2` without the Euler factors at `S` and its conjugate. 

### `detPeriod_mul_upsilonU1_insert`

 Let `p = (ν, z)` be a critical pair with `ν = p.character` of weight `-c`. Let `ϑ'` be the tame
character `ϑ` (same `toAutChar` and `tamePart`) with modulus `Q ∪ {v}` instead of `Q`, where
`v ∉ Q`. Let `υ = upsilonU1` be the restriction to the norm-one ideles of the fixed splitting Hecke
character. Replacing `ϑ` by `ϑ'` multiplies by `(1 - X) * (1 - q * X)` the period `detPeriod` of
`ν ϑ υ` on the rank-two unitary group, in weight `c - 1`, with the tame part of `ν` times that of
`ϑ`, at the modulus `D.twistModulus ϑ 2` (the chosen places to the exponent `2`, times `Q`). Here
`q` is the norm of `v`, and `X⁻¹` is `AutChar.frobValue` in rank two:
`q * (ν ϑ υ)(ϖ / ϖ̄) / υ(ϖ) ^ 2` for a uniformizer `ϖ` at `v`, where `υ(ϖ)` is the value of the
Hecke character itself. 

### `exists_isIntegralMeasure_norm_sq_detPeriod`

 For a critical pair `p = (ν, z)` with `ν = p.character` of weight `-c` and `υ = upsilonU1`,
there is `N ≠ 0` such that `F ϑ' = ‖D.chosenGroupOrder * N * Λ ϑ'‖ ^ 2` is an integral measure at
the modulus of every tame character `ϑ`: on the characters `ϑ'` with `ϑ'.Q = ϑ.Q` it is a sum
`∑ a, c_a * ϑ'(u_a)`, with fixed norm-one ideles `u_a` and coefficients `c_a` integral at every
prime not dividing the norm of `ϑ.Q`. Here `Λ ϑ'` is the period `detPeriod` of `ν ϑ' υ` on the
rank-two unitary group, a sum over classes at the standard level, in weight `c - 1`, with tame part
that of `ν ϑ'` and modulus `D.twistModulus ϑ' 2`, the chosen places to the exponent `2` times
`ϑ'.Q`. 

### `exists_isTwistMeasure_of_z_eq_one`

 Let `p = (ν, 1)` be a critical pair, that is, a character `ν` of U(1) with the point `1`, whose
tame part is nontrivial exactly at the chosen places, those dividing `D.piM` (`IsRamified`). There
is a function `F` of tame characters with the properties of `IsTwistMeasure {0, 1} 1`: it is nonzero
at the trivial character; at each modulus it is evaluation on finitely many points with coefficients
integral away from that modulus (an integral measure); adding a place of norm `q` multiplies it by
the inverse Euler factors with denominators `q ^ 0` and `q ^ 1`; and at a twist `ϑ` it is
`F 1 * normQ ϑ * r ^ 2`, where `r = p.ratio ϑ` is the ratio of the absolute values of the twisted
and untwisted `L`-values at `1`. 

### `exists_isTwistMeasure`

 Let `p = (ν, z)` be a critical pair, that is, a character `ν` of U(1) with an integer
`1 ≤ z ≤ c`, `-c` its weight, whose tame part is nontrivial exactly at the chosen places, those
dividing `D.piM` (`IsRamified`). Some function `F` of tame characters has the properties of
`IsTwistMeasure I m`: it is nonzero at the trivial character; at each modulus it is evaluation on
finitely many points with coefficients integral away from that modulus (an integral measure); adding
a place of norm `q` multiplies it by the inverse Euler factors with denominators `q ^ l`, `l ∈ I`;
and at a twist `ϑ` it is `F 1 * normQ ϑ ^ m * r ^ (m + 1)`, where `r = p.ratio ϑ` is the ratio of
twisted and untwisted `L`-values at `z` in absolute value. For `z ≥ 2`, which is what
`HasLiftRank` asks besides `2 z` indices, `I = {z}`, `m = 0` and `F` is `integralAlgebraicPart`, an
integral multiple of the algebraic part of the `L`-value. For `z = 1`, `I = {0, 1}` and `m = 1`, so
that the square of the ratio occurs. 

### `coprime_prod_q_of_isAuxiliary`

 If `I` is an auxiliary set of places avoiding `badPlaces D ℓ`, the places dividing `ℓ M N` (with
`M = D.M` and `N = D.N` the level), then the product of the norms of the places of `I` is prime to
`ℓ` and to `M N`. 

### `tameCharOfAuxiliary`

 The tame character of modulus `I` given by a member `χ = (μ, ψ)` of `tameChars I`, that is, a
character `μ` of U(1)(𝔸) of weight `0` whose tame part `ψ` is trivial outside `I`; here `I` is an
auxiliary set avoiding `badPlaces D ℓ`, the places dividing `ℓ`, `D.M` or `D.N`. 

### `invAvatar_eq_of_artinMap_eq`

 If a finite idele `x` of `E` has the Artin symbol `g` in the absolute Galois group `AbsGal D`,
then `τ.invAvatar`, the `ℓ`-adic avatar of the inverse of a tame character `τ`, takes at `g` the
value `ιℓ (b⁻¹)`, with `b` the value at `x` of the base change of `τ` and `ιℓ` the fixed
isomorphism of `ℂ` with the algebraic closure of the `ℓ`-adic numbers. 

### `exists_tameChar_invAvatar_eq`

 Let `ℓ` be the fixed prime, `E = D.E` the CM field of the data `D`, `Ω` the algebraic closure of
`ℚ`, and `I` a finite set of places of `E` that is auxiliary for `badPlaces D ℓ`, the places
dividing `ℓ * D.M * D.N`: the places of `I` have prime norm, their conjugates are outside `I`, and
neither they nor their conjugates are bad. Let `ψ : Gal(Ω/E) → ℚ̄_ℓ` be a locally constant character
with `ψ(Art x) = η(x / x̄)` for an idele class character `η` of modulus `I` that is trivial on the
local components at the places over `ℓ` (`IsFromU1`). Then `ψ = τ.invAvatar` for some `τ` with
modulus `I` in `D.TameChar`, the weight-zero tamely ramified characters of U(1)(𝔸) of `E`. 
