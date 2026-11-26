---
{
  "module": "src/New/OneLift/ComparisonOperator/ThreeExchanges.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/ThreeExchanges.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/ThreeExchanges.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Three exchanges: the carrier, the third exchange and its left side as a theta series

The exchange identity (`New.Rows.exists_mul_stdClassSum_eq_integral_modKernel`) is applied three
times, until only a number is left of the twist. The first two exchanges evaluate a class sum of
twisted square kernels on the space S of signature (2m, m) as a multiple of the carrier φ° =
`New.Rows.carrierForm`, the theta lift of the constant function 1 from the definite group U(0, m) to
U(S). The third exchange equates a multiple of a double class sum of kernels with 𝖥_i =
`New.Data.choiceFn j i`, the function on U(W_j) given by the integral of the carrier against a theta
kernel. The modulus of the product of the three constants is given by the product Γ_j of Hecke
values at three pairs (ν, z) of a character and an integer.

Letters: the twist is ϑ, υ = `upsilonU1` is the splitting character on U(1), and I_m = E^m is the
standard definite space of rank m.

## Main definitions and results

* `New.Data.exchangePair`: three pairs for each `1 ≤ j ≤ m`, indexed by `none` and the two signs.
* `New.Data.heckeValueProd`: the product `Γ_j` of the values `Exchange.lValueProd` at the inverses
  of the characters of these pairs, twisted by a tame character or its inverse. It is not divided by
  its value at the trivial twist.
* `New.Rows.exists_mul_stdClassSum_eq_carrierForm`, from the first two exchanges: for even `m` and a
  character c of weight 0 that is tame for (𝔪, χ), the carrier is a constant γ of known size times a
  class sum of `New.Rows.carrierCoeff` times a theta kernel twisted by χ∘det.
* `New.Rows.carrierForm_mem_rapidOfLevel_and_isAdelicHol`: for even `m`, if there is a tame
  character of weight 0, the carrier lies in `New.Rows.rapidOfLevel` for every level. So it has full
  level and is rapidly decreasing. It is also holomorphic.
* `New.Data.exists_mul_thirdExchangeLeftSide_eq_choiceFn`,
  `New.Data.thirdExchangeLeftSide_eq_kernelClassSum`: a number times a double class sum of kernels
  is 𝖥_i, and this double sum is a theta series on U(W_j).

Notions from other files:
* `New.Data.chiM`, `New.Data.chiMLocal`: a fixed character χ of U(1)(𝔸) of weight 0 and its tame
  part ω, which is trivial off the chosen places and has order greater than 8m at each of them.
* `New.Data.goodForms`: The good forms on V: the image of the idempotent e₀ of ℂ[𝖦] acting on forms
  of principal level at the chosen places above p₀ and p₁.
* `New.Data.signsW`: Signs ±1 on the indices i in `New.Data.RowIndex` for W_j: −1 when
  `New.Data.basisNumber`(i) ≥ `New.Data.posRank` j, and +1 otherwise.
* `New.Rows.IsAdelicHol`: For every adelic g, the function h ↦ F(g·(h,1)) on the archimedean group
  is holomorphic of the given weight for the given order (`New.IsHolOfWeight`).
* `New.Data.kernelWeight`: The weight `New.staircaseWeight` on W_j for the pair (W_j, V°).

## Relation to the literature

The twisted theta kernel of an indefinite and a definite unitary group of equal rank, summed against
an explicit form, is a non-zero multiple of one fixed non-zero holomorphic, rapidly decreasing form
of level one, for even m. The factor has modulus given by Hecke L-values, so the twist survives only
as a number. Non-vanishing and holomorphy of the stable-range theta lift of a character are known in
the literature. Related work: J.-S. Li, Non-vanishing theorems for the cohomology of certain
arithmetic quotients, 1992; Gan–Qiu–Takeda, The regularized Siegel–Weil formula, 2014; T. Yang,
Theta liftings and Hecke L-functions, 1997.

The theta kernel of two definite unitary groups of the same even rank 2e with determinant data,
summed over the classes of one group, is a non-zero constant whose modulus, up to a fixed factor and
conductor norms, is a product of Hecke L-values at 1,…,e. This is the first step in turning the
twist into a number. It is Rallis's formula at equal rank 2e for a character, whose central value
folds by the functional equation into Hecke L-values at 1,…,e and a conductor power, with the
ramified local data computed explicitly. Related work: Yamana, L-functions and theta correspondence
for classical groups, 2014; C. Li, Geometric and arithmetic theta correspondences (§2.4–2.5), 2024;
Yang, Theta liftings and Hecke L-functions, 1997.

See `New.OneLift.ComparisonOperator.FirstFactors` and `New.OneLift.ComparisonOperator.ProductsSpan`
for related work.



## Pairs (ν, z) of the three exchanges and the products Γ_j of Hecke values

A pair (`New.Data.CriticalPair`) consists of a character `ν` of `U(1)(𝔸)` of weight `-c` whose tame
part `ψ` is trivial off the chosen places, and an integer `1 ≤ z ≤ t`, with `z ≤ c v ≤ 4 b` at every
infinite place `v`.


### `signPoint`

 The point `z_±` of the pair of sign `s`: it is `m` for `s = 1` and `m / 2` for `s = -1`. 

### `mainPairPoint`

 The number `z_* = 7 (m / 2) + k / 2`, the point of the pair of the third exchange. Here
`k = r + 1 - m` is the rank of the source. 

### `k_add_six_le_t`

 The rank `k` of the source satisfies `k + 6 ≤ t`, for `t = 5 r`. 

### `mainPairPoint_mem_Icc`

 The point `z_* = D.mainPairPoint`, the point of the pair of the third exchange, lies in the
closed interval from `1` to `t = 5 r`. 

### `k_add_t_add_one_le_liftWeight`

 The weight `w j v = D.liftWeight j v` of the character of the `j`-th lift at an infinite
place `v` is at least `k + t + 1`, with `k` the rank of the source and `t = 5 r`. This holds for
every natural number `j`. 

### `liftWeight_le_four_mul_b`

 For a lift index `j`, that is `1 ≤ j ≤ m`, the weight `D.liftWeight j v` of the character of
the `j`-th lift at an infinite place `v` is at most `4 b`, where `b = D.b` is the real number
`exp D.logB` of the data. 

### `exponent_add_mainPairPoint_le_liftWeight`

 For a lift index `j`, let `n = j + (t - 11 m - 1) / 2`; this is the exponent of the splitting
character `υ` in the character `ν_j = μ_j⁰ υ ^ n` of `exchangePair`. At every infinite place `v`,
the weight `D.liftWeight j v` of the `j`-th lift is at least `n + D.mainPairPoint`. 

### `exchangePair`

 The pairs of the three exchanges, indexed by `Option ℤˣ`: the sign `-1` belongs to the first,
the sign `1` to the second and `none` to the third exchange. Here `j` is a lift index
(`1 ≤ j ≤ m`), `w j v = D.liftWeight j v` is the weight and `μ_j⁰ = D.untwistedLiftChar j` the
untwisted part of the character of the `j`-th lift, `υ = upsilonU1`, `t = 5 r`, and `ω` is the tame
part of `χ`. For `none`: `ν_j = μ_j⁰ υ ^ n` with `n = j + (t - 11 m - 1) / 2`, of weight
`-(w j v - n)` at `v` and tame part `ω ^ j`, at the point `z_* = D.mainPairPoint`.
For a sign `s = ±1`: `ν_± = υ ^ (-z_±) χ ^ (± j)`, of weight `-z_±` at every place and tame part
`ω ^ (± j)`, at the point `z_± = D.signPoint s`. 

### `heckeValueProd`

 The product of the Hecke values for the three pairs `(ν, z)` of `exchangePair j`,
twisted by `ϑ`. A twist consists of a character `ϑ.toAutChar` of U(1)(𝔸) with a tame part that is
non-trivial at every place of its finite set of places `ϑ.Q`. The factor of a pair is the real
number `Exchange.lValueProd` for the set of the chosen places and the places of `ϑ.Q`, the
character `(ν χ')⁻¹` and the integer `z`. Here `χ'` is `ϑ.toAutChar` for the pair `none` and
`ϑ.toAutChar ^ s` for the pair of sign `s`. 


## Equal-rank theta class sums and the twisted carrier identity

The first two exchanges, for characters that are tame for a modulus 𝔪 (`New.Exchange.IsTameFor`).
Here m is positive. The two exchange lemmas also assume that m is even; the lemma on conjugating a
constant class sum does not.

Notation: θ_{a,b}[Ψ,P] is the theta kernel with characters a, b, a function Ψ on matrices mod 𝔪 and
a polynomial P. I_m is the standard definite space, `New.stdClassSum` is the class sum on it, and
`stdLevel` is the integral level. υ is the splitting character restricted to U(1).


### `exists_mul_stdClassSum_modKernelStdSpace_eq_one`

 The first exchange. Let `E` be a CM field, `m = 2e > 0`, and fix exponents `k τ` at the infinite
places `τ`. There is a constant `C` such that each character `α` of `U(1)(𝔸)` of weight `-k` that is
tame for `(𝔪, χ)` has a `γ` with (a) `‖γ‖ ^ 2 = C / lValueProd 𝔪.places (α⁻¹ υ ^ e) e`, and (b) `γ
Σ_h θ_{α,α}[χ ∘ det, ∏_τ det (y_τ) ^ k τ](g, h) = 1` for all `g` in `G E 1`, the adelic unitary
group of the standard definite space `I_m = stdSpace E (Fin m)`. The kernel `θ = modKernelStdSpace`
is the theta kernel of `I_m` with itself, `y_τ` is the `m × m` matrix of variables at `τ`, and
`Σ_h = stdClassSum` is the sum, with weights `1 / #Aut`, over the double cosets of the rational
points and `stdLevel`, the stabilizer of the standard lattice. 

### `exists_stdClassSum_modKernelStdSpace_neg_eq_one`

 Let `E` be a CM field, `m > 0`, `I_m` the standard definite space of rank `m` and
`I_m⁻ = (stdSpace E (Fin m)).neg` the same space with its form negated. There is a number `n` of
norm 1 such that the following holds for every modulus `𝔪`, character `c` of `U(1)(𝔸)`, character
`χ` of the residue ring of `𝔪` and number `γ`. If `γ` times the class sum on `I_m`, at the integral
level `stdLevel`, of the theta kernel of `(I_m, I_m)` with characters `c⁻¹, c⁻¹` and function
`χ⁻¹ ∘ det` is the constant 1, then so is the conjugate of `γ` times `n / χ(η) ^ m` times the class
sum of the kernel of `(I_m⁻, I_m)` with characters `c υ ^ m, c υ ^ m` and function `χ ∘ det`. Here
`υ = upsilonU1` is the splitting character of `WeilData E` on the norm-one ideles, and
`η = 𝔪.normNegOne` is the unit mod 𝔪 that is the reduction of a chosen element of norm -1. 

### `exists_mul_stdClassSum_eq_carrierForm`

 Let `E` be a CM field and `m = 2e > 0`. There is a constant `C` such that each character `c` of
`U(1)(𝔸)` of weight 0 that is tame for `(𝔪, χ)` has a `γ` with (a) `‖γ‖ ^ 2 = C / (lValueProd (c⁻¹ υ
^ m, m) * lValueProd (c υ ^ e, e))`, and (b) `γ Σ_h carrierCoeff m c h · θ_{υ^m,c}[χ ∘ det, 1](x,
h) = φ°(x)` for all `x` in `G E (1 ⊕ᵥ -1)`, the adelic unitary group of the space `S` of signature
`(2m, m)`. The sum is the class sum on the finite adelic group `Gf` of the standard definite space
of rank `3m`, at the level `stdLevel`, and θ is the theta kernel of `S` and that space. 

 ## The carrier as a nonzero holomorphic rapidly decreasing form 

### `carrierForm_mem_rapidOfLevel_and_isAdelicHol`

 Let `E` be a CM field and `m` a nonzero even natural number, and let `E` have a character `c` of
`U(1)(𝔸)` of weight 0 that is tame for some `(𝔪, χ)`: its tame part is non-trivial exactly at the
places of `𝔪 ≠ 1` and induces `χ`. The carrier `carrierForm E m` is the theta lift of the constant 1
from `U(0, m)` to `U(S)`, with `S = signedSpace E (1 ⊕ᵥ -1)` of signature `(2m, m)`. (a) For every
integer `N` of `E` the carrier lies in `rapidOfLevel S N`: it is continuous, invariant under the
rational points of `U(S)` on the left and under the principal congruence subgroup `K(N)` on the
right, and rapidly decreasing. (b) There is an order `o`, an injective integer numbering of the
basis of `S` with the positive vectors before the negative ones (`IsPosFirstOrder`), for which the
carrier is holomorphic (`IsAdelicHol`): each left translate, restricted to the real group, extends
analytically to the products `h b` with `b` invertible and `o`-triangular. 

### `fockInner_realPairWeil_variableMinor_pow_eq_self`

 Let `E` be a CM field and `m > 0`. In the Fock space `PairFock` of the pair
`(U(0, m), U(2m, m))`, let `v` be the vector of the polynomial `∏_τ det (y⁻_τ) ^ (2m)`, where `τ`
runs over the infinite places and `y⁻_τ` is the `m × m` block of variables in the negative rows of
`U(2m, m)`. Then `⟨v, Ω(u, 1) v⟩ = ⟨v, v⟩` for every `u` in `GInf E (-1)`, the product over `τ` of
copies of the compact group `U(0, m)`.
Here `Ω = realPairWeil 0 0` is the real Weil representation of the pair with both weights `0`, and
`⟨·, ·⟩ = Fock.fockInner` is the sesquilinear form of the Fock space. 

### `carrierForm_ne_zero`

 Let `E` be a CM field. For every positive `m`, even or odd, the carrier `φ° = carrierForm E m`
is not zero. It is the theta lift of the constant 1 from the definite group U(0, m) to U(S), S of
signature (2m, m). 


## The third exchange

The exchange identity for the spaces `W = E^{3m} ⊕ W'`, `V″` and `S`, summed over the classes of
`E^{3m}`, equates a double class sum of kernels with the function `𝖥_i = choiceFn j i`, up to a
number whose modulus depends on the twist only through Hecke values and norms. Here `V″` is the
standard definite space on `FirstFactorIndex j`. The characters are `χ' = twistedChiMPow ϑ j`,
`ν″ = firstFactorChar ϑ j` and `ν♭ υ ^ m = carrierChar j`, where `ν♭ = ν″ / χ'` does not depend on
the twist.

The datum of the left side becomes a product at a smaller level. This is stated for rows `w` modulo
`ϖ²` of which the rows of `Λ` are combinations. For the rows of `Λ` stacked above `ϖ • 1`, the
level `rowFixingLevel` is `J_Λ` and `columnDatum` is the datum `Ψ_Λ` on `W_j`.


### `carrierChar_inv_div_twistedChiMPow_mul_upsilonU1_pow`

 The quotient `(carrierChar j)⁻¹ / χ'` times `υ ^ (3m + mainPairPoint)`, with `χ'` the character
`twistedChiMPow ϑ j`, is `ϑ⁻¹` divided by `μ_j⁰ υ ^ n`, the character of `exchangePair j none`. Here
`μ_j⁰ = D.untwistedLiftChar j` and `n = j + (t - 11 m - 1) / 2`. 

### `twistedChiMPow_inv_mul_upsilonU1_pow`

 The character `χ'⁻¹ υ ^ m`, with `χ' = twistedChiMPow ϑ j`, is `ϑ⁻¹` divided by
`υ ^ (-m) χ ^ j`, the character of `exchangePair j (some 1)`. 

### `twistedChiMPow_mul_upsilonU1_pow`

 The character `χ' υ ^ (m / 2)`, with `χ' = twistedChiMPow ϑ j`, is `ϑ` divided by
`υ ^ (-m / 2) χ ^ (-j)`, the character of `exchangePair j (some (-1))`. 

### `enlargedSpace`

 The space `W' = W_j ⊕ (E^j)⁻ ⊕ E^{3m-j} ⊕ W♭` of the third exchange, where `W♭` is the standard
definite space on the `6m + 1` indices `D.FlatIndex`. Its basis is indexed by `FirstFactorIndex j`,
like that of the definite space `V″`, and `padSigns j` gives the signs on the first three
summands. 

### `enlargedPoint`

 The point `(g, 1, 1, h♭)` of `U(W')`, with `h♭` the class of the index `i`. 

### `signOrder`

 The list of the positive, then the negative basis vectors of `W = E^{3m} ⊕ W'`. 

### `signs_eq_blockSigns_signOrder`

 The left side lists the signs of `W = E^{3m} ⊕ W'` with `W' = W_j ⊕ (E^j)⁻ ⊕ E^{3m-j} ⊕ W♭`:
sign `1` on the `3m` indices `D.CarrierIndex` of `E^{3m}`, the signs `padSigns j` on the first three
summands of `W'`, and sign `1` on the definite space `W♭` of rank `6m + 1`. The bijection
`signOrder j` lists the basis of `W` in two blocks, and `blockSigns` is `1` on the first block and
`-1` on the second, which has `m` vectors. So the first block holds the positive and the second the
negative basis vectors. 

### `invariantTraceChar`

 The invariant trace character `ψ^inv_Λ`: the sum over `γ` in `GL_{3m}` modulo `ϖ²` of the
additive character `traceChar Λ` at `x γ`, for `x` reduced modulo `ϖ²`. 

### `invariantTraceChar_mul`

 The invariant trace character `ψ^inv_Λ = invariantTraceChar ϑ j Λ` is invariant under right
multiplication of its argument `x` by an invertible matrix `γ` over the residue ring of
`D.twistModulus ϑ 2`. 

### `twistedChiMod`

 The character of the residue ring modulo `D.twistModulus ϑ 2 = ϖ² Q`, with `ϖ` the product of
the chosen places and `Q` the product of the places of `ϑ`, that comes from the tame part of
`twistedChiMPow ϑ j`, the product `χ' = χ^j ϑ` of the fixed character `D.chiM` and the twist. 

### `thirdExchangeKernel`

 The theta kernel of `(W, V″)` in the third exchange: `W = E^{3m} ⊕ W'`, and `V″` is the standard
definite space on `FirstFactorIndex j`. The characters are `twistedChiMPow ϑ j * carrierChar j` and
`ν″ = firstFactorChar ϑ j`, the character of the `j`-th lift times a power of υ; here
`carrierChar j` is `ν″ υ ^ m / twistedChiMPow ϑ j`, which is free of the twist. The datum is `Ψ`,
and the polynomial is `stackedDetProd` of the constant rows `constantRows` of `i`, read through the
bijection `posEquiv j` between its column indices and the positive part of the basis. It is taken at
the point `(h', g, 1, 1, h♭)` of `U(W)` and the point `h` of `U(V″)`. 

### `thirdExchangeLeftSide`

 The left side of the third exchange: the class sum over `U(V″)` of the kernel with the datum
`(x' x″) ↦ χ' (det x″) ψ^inv_Λ (x″⁻¹ x')`, summed over the classes `h'` of `E^{3m}` against the
coefficients `carrierCoeff` at `h'`. 

### `firstFactorChar_mul_upsilonU1_pow`

 The identity `ν″ υ ^ m = χ' (ν♭ υ ^ m)` of characters, with `ν″ = firstFactorChar ϑ j`,
`χ' = twistedChiMPow ϑ j` and `ν♭ υ ^ m = carrierChar j`, a character that does not depend on
`ϑ`. 

### `isTameFor_twistedChiMPow_mul_carrierChar`

 Let `D` be admissible data, `ϑ` a twist and `j` a lift index, `1 ≤ j ≤ m`. Let
`χ' = twistedChiMPow ϑ j = χ^j ϑ`. The character `carrierChar j` does not depend on `ϑ` and has
trivial tame part. The product of the two is tame for `D.twistModulus ϑ 2 = ϖ² Q`, with `ϖ` the
product of the chosen places and `Q` that of the places of `ϑ`: its tame part is non-trivial exactly
at the places of `ϖ² Q ≠ 1` and induces `twistedChiMod ϑ j`, the character of the residue ring given
by the tame part of `χ'`. Its weight at an infinite place `τ` is `m` minus the size of
`DetIndex j τ`, the index set of the determinants at `τ` in the polynomial of the third exchange. 

### `matchedPoly_constantRows`

 Let `D` be admissible data, `j` a lift index (`1 ≤ j ≤ m`) and `W = E^{3m} ⊕ W'`, where
`W' = W_j ⊕ (E^j)⁻ ⊕ E^{3m-j} ⊕ W♭`: the space `W_j = D.spaceW j`, its padding, and the definite
space `W♭` on the `6m + 1` indices `D.FlatIndex`. The variables at an infinite place `τ` form a
matrix with rows the basis of `W`, listed by sign through `signOrder j`, and `2m` positive and `m`
negative columns. For complex matrices `η_{τ k}` with `2m` rows, `matchedPoly` is the product of a
power of the determinant of the negative block and of the `det (η_{τ k} y_τ)`, with `y_τ` the
positive block. The choice `i` consists of a class of `U(W♭)` and lists `i.rows τ k` of `2m` row
indices, `k < D.reducedHalfGap`. The matrices `constantRows` have as rows either basis vectors of
`W_j` and the padding, or the rows `i.rows τ k` of `D.shortRows i`, an invertible matrix over `E`
with small rows in the lattice of the class, read at `τ` by the embedding `Φ τ`. For them
`matchedPoly` involves only the rows of `W'`: it is `paddedMinorProd j`, a product of minors in the
rows of `W_j` and the padding, times the determinants `pairedDetProd` in the rows of `W♭`. The maps
`renameRowsCols` place each factor in its block of rows. 

### `integral_carrierForm_mul_eq_card_mul_choiceFn`

 Let `D` be admissible data over the CM field `D.E`, `ϑ` a twist, `j` a lift index, `g` a point
of the adelic group `New.G D.E (D.signsW j)` of `W_j = D.spaceW j`, and `i : ChoiceIndex j` a
choice: a matrix `Λ = i.matrix` modulo `ϖ²` (`ϖ` the product of the chosen places), a class `h♭` of
the definite group `U(W♭)` and lists of rows. The left side integrates, over the unitary group of
the space `S = signedSpace` of signature `(2m, m)` modulo its rational points (`quotMeasure`), the
carrier `carrierForm`, the theta lift of 1 from `U(0, m)`, times the theta kernel `modKernel` of
`S` and `enlargedSpace j = W_j ⊕ (E^j)⁻ ⊕ E^{3m-j} ⊕ W♭` at `enlargedPoint j i g = (g, 1, 1, h♭)`.
Its characters are `υ ^ m`, with `υ = upsilonU1` the splitting character on the norm-one ideles,
and `carrierChar j`, which does not depend on `ϑ`. Its polynomial is the product of minors
`paddedMinorProd j` on the first three summands times the determinants on `W♭` formed with the rows
of `i`. Its finite datum, on matrices modulo `D.twistModulus ϑ 2 = ϖ² Q` (`Q` the product of the
places of `ϑ`), is `ψ^inv_Λ = invariantTraceChar ϑ j Λ`, the sum of the translates of the additive
character `ψ_Λ = traceChar Λ` under `GL_{3m}(𝒪/ϖ²)`. The function `choiceFn j i` is the same
integral with the datum `ψ_Λ` modulo `ϖ²`, and the left side is `#GL_{3m}(𝒪/ϖ²)` times it: the
carrier has full level, so every translate gives the same integral. 

### `exists_mul_thirdExchangeLeftSide_eq_choiceFn`

 The third exchange. There are a constant `C` and numbers `c ϑ`, one for each twist `ϑ`, with two
properties. First, `‖c ϑ‖ ^ 2` is `C` divided by `heckeValueProd j ϑ`, the product over the three
pairs `(ν, z)` of `exchangePair j` of the squared `L`-values at `1, …, z` of `(ν ϑ ^ (± 1))⁻¹`,
without the factors at the chosen places and `ϑ.Q`, and of powers of the norms of these places.
Second, for every choice `i : ChoiceIndex j` and every point `g` of the adelic unitary group of
`W_j = D.spaceW j`, the product of `c ϑ` and `thirdExchangeLeftSide ϑ j i g` is `choiceFn j i g`,
the integral of the carrier `carrierForm` against a theta kernel. 

### `productDatum`

 The product datum `Ψ^×` at `x = (x' x″)`, with `x″` square: the datum `columnDatum` of the rows
`w` on the columns of `x″` at `W_j`, times `ψ^inv_Λ (x')` if the other columns of `x″` are those of
`1` (`FixesColsOff`), and `0` otherwise. 

### `stdClassSum_thirdExchangeKernel_productDatum`

 Let `D` be admissible data, `ϑ` a twist, `j` a lift index, `W_j = D.spaceW j`, and `V″` the
standard definite space on `FirstFactorIndex j`, which contains the indices of `W_j` through
`.trans .inl .inl`. Let `w` be a finite family of rows modulo `ϖ²` (`ϖ` the product of the chosen
places) indexed by `FirstFactorIndex j`, and `i` a choice: a matrix `Λ = i.matrix` modulo `ϖ²`, a
class `h♭` and lists of rows. On the left, `thirdExchangeKernel` is the theta kernel of
`(W, V″)`, `W = E^{3m} ⊕ enlargedSpace j`, at `((h', g, 1, 1, h♭), h)`. Its datum `productDatum` at
`(x' x″)` is `columnDatum` of `w`, a function of the columns of `x″` at `W_j`, times
`invariantTraceChar ϑ j Λ x'` if the other columns of `x″` are those of `1`, and `0` otherwise.
It is summed over the classes `h'` of the finite adelic group `Gf` of `E^{3m}`, at the integral
level `stdLevel`, against `carrierCoeff`, a class sum of theta kernels of `(E^m, E^{3m})`. The
result is one theta kernel of `(W_j, V″)` at `(g, h)`. Its characters are `charW` of the descent
pair `D.descentPair ϑ j` (the data of the `j`-th lift) and `firstFactorChar ϑ j` (the character of
that lift times a power of the splitting character), its datum is `columnDatum` of `w`, and its
polynomial is `letterPoly` of the vector `leftSideSeries ϑ j i h` of the Weyl module with column
counts `colsPlus`. The coordinates of this vector are formed from the kernels at `h` of the summands
of `W` other than `W_j`. 

### `stdClassSum_thirdExchangeKernel_eq_productDatum`

 Let `D` be admissible data, `ϑ` a twist, `j` a lift index, `W_j = D.spaceW j`, and `V″` the
standard definite space on `FirstFactorIndex j`, which contains the indices of `W_j`. Let `i` be a
choice with matrix `Λ = i.matrix` modulo `ϖ²` (`ϖ` the product of the chosen places), and `w` rows
modulo `ϖ²` of which those of `Λ` are combinations: `u * w = Λ`. Both sides are class sums
`stdClassSum` over `U(V″)` of `thirdExchangeKernel`, the theta kernel of
`(E^{3m} ⊕ enlargedSpace j, V″)` at a point formed from `h'`, `g` and `i`. On the left the level is
the integral level `stdLevel` and the datum is `(x' x″) ↦ χ' (det x″) ψ^inv_Λ (x″⁻¹ x')`, where
`χ' = twistedChiMod ϑ j` is a character of the residue ring and `ψ^inv_Λ = invariantTraceChar ϑ j Λ`
is the sum of the translates of the additive character `traceChar Λ` under `GL_{3m}(𝒪/ϖ²)`. On the
right the level is `rowFixingLevel`, cut out by the matrices that are `1` in the columns outside
`W_j` and fix `w`, and the datum `productDatum` is `columnDatum` of `w` on the columns of `x″` at
`W_j` times `ψ^inv_Λ (x')` if the other columns of `x″` are those of `1`, and `0` otherwise. 

### `thirdExchangeLeftSide_eq_kernelClassSum`

 If `u * w` is the matrix `Λ` of `i`, the left side of the third exchange is the theta
series `kernelClassSum` on `U(W_j)`: the class sum, at the level cut out by the rows `w`, of kernels
with the vectors `leftSideSeries ϑ j i h`. 


## Level and holomorphy of 𝖥_i

Conventions: `New.Data.spaceW j` is the space W_j, `New.Data.orderW j` its order with positive
vectors first, `New.Data.conjHolomorphicWeight j` the weight of the parameter −`New.Data.paramW`,
and `New.Data.kernelWeight j` the weight of the complementary theta kernel.


### `goodForms_mem_rapidOfLevel`

 A good form `F` on `W_j`, as a function on `U(W_j)`, lies in `New.Rows.rapidOfLevel` for every
level `a` divisible by `New.Data.piM`: it is automorphic of level `a` and rapidly decreasing. 

### `polyVector_letterPoly_mem_holomorphicData`

 Let `D` be admissible data, `j` a lift index, `W_j = D.spaceW j` with signs `D.signsW j`, and
`V″` the standard definite space on `FirstFactorIndex j`. The data of the `j`-th lift at the trivial
twist, `untwistedDescentPair j`, number the basis of `W_j` (`numbering`) and give at each infinite
place `τ` a partition `μ⁺` with `colsPlus τ h` columns of height `h`. Let `ξ` be a vector of the
Weyl module of weight `μ⁺`, in the coordinates `WeylIndexFamily`. The polynomial `letterPoly … ξ` is
that of `ξ` with the variable `(τ, i, h)` replaced by the sum of the variables `(τ, i, a)` over the
basis vectors `a` of `W_j` of sign `+1` and number `h`. Its vector `v = Fock.polyVector` in the Fock
space of `(W_j, V″)`, whose coordinates have the product signs `realSigns (homSigns …)`, lies in
`holomorphicData`: every matrix coefficient `x ↦ ℓ (Ω (x, 1) v)` on the real group of `W_j` is
holomorphic for the order `orderW j` of the basis, of weight `u - u°`. Here
`u = conjHolomorphicWeight j` is the weight of the conjugates of good forms, `u° = kernelWeight j`
that of the complementary theta kernel, and `Ω = realPairWeil γ e` is the real Weil representation
of the pair with the weights `γ τ = negCount (D.signsW j)`, the number of negative signs of `W_j`,
and `e τ = firstFactorCharExp j - D.liftWeight j τ`, the weight of `firstFactorChar` at `τ`. 

### `exists_choiceFn_eq_mul_kernelClassSum`

 The function `𝖥_i = choiceFn j i` on `U(W_j)` is a multiple of the theta series
`kernelClassSum` for the trivial twist, at the level cut out by the rows of `Λ = i.matrix`. 

### `mul_choiceFn_mem_rapidOfLevel`

 For a good form `F` on `W_j`, the product of `F` with the function `choiceFn j i` on `U(W_j)`
is automorphic of level `D.piM ^ 2` and rapidly decreasing. 

### `isAdelicHol_choiceFn`

 The function `choiceFn j i` on `U(W_j)` is holomorphic for the order `orderW j`, of weight
`u″ = u - u°`. Here `u = conjHolomorphicWeight j` and `u° = kernelWeight j`. 
