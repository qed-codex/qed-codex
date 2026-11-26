---
{
  "module": "src/New/Spanning/MainTerm/EnergyEstimate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/EnergyEstimate.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/EnergyEstimate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Main-term bound for the second moment over open reductions fixing given vectors

This file proves the main-term estimate of the filling theorem. The subgroup
`New.Filling.fixer Sg D` consists of the reductions s that fix the given vectors `D w` modulo w or
its conjugate, at the chosen places `w ∈ Sg` above the first prime. It shows that every term over an
open reduction lies in the big cell. It then proves Siegel's step and uses it to bound the sum over
the open reductions that fix the vectors at `Sg`.

## Main definitions and results

* `New.Filling.IsFillingData.mul_sum_norm_sum_cosetAmplitude_sq_le`: Siegel's step, which bounds the
  squared norms of finitely many class sums by densities at finite places weighted by the local
  bounds.
* `New.Filling.sum_norm_sum_cosetAmplitude_sq_le`: the estimate for finitely many distinct classes
  whose reductions fix the vectors at `Sg`. The bound is (1 + b⁻⁴) b^(−6 𝔰.k |Sg|) times the main
  second moment times `unipotentCovolume`².
* `New.Filling.linkSecondMoment_isOpenElement_le`: the squared norms of the class sums of the cut
  function add up to at most the same bound. The sum runs over all links, pairs of classes and
  reductions s that are open and fix the vectors at `Sg`; only terms with `termDisc γ ≠ 0` enter.

Notions from other files:
* `New.Filling.IsAdmissible`: The standing hypotheses: `sourceLevel` is the preimage of K(M),
  `reduction` is onto, and size inequalities hold between b, M and ϖ, κ_v, N, the constant
  `scaledSiegelConst`, the second moments, the number of Bessel coordinates and an index.
* `New.Filling.mainSecondMoment`: The real number `sourceDim`² / (`besselDegree` · mass), with the
  mass `New.mass` of the genus of the standard lattice of rank dim V.
* `New.Filling.termsOver` c s c': The terms over (c, s, c'): rational γ such that h_c⁻¹ γ h_c' lies
  in the stabiliser K of the lattice and has reduction s.

## Relation to the literature

In the unfolded second moment of the Poincaré series, the summed main terms are dominated by the
quadratic form of a positive kernel of local Bessel (orbital) integrals at a finite set of primes,
with a constant close to one. With the sieve this bounds the main term above. Kloosterman sums as
local orbital integrals, normal forms for Bessel double cosets and Siegel's formula are known in the
literature. Related work: Jacquet–Ye, Germs of Kloosterman integrals for GL(3), 1999; Y. Liu,
Relative trace formulae toward Bessel and Fourier–Jacobi periods, 2014; Siegel, Über die analytische
Theorie der quadratischen Formen, 1935.


### `leadingMinor_frameGram_map`

 The leading minors of the frame products (the products of the frame of the middle form over
the lattice with its image under `X`) commute with ring maps. 

### `exists_leadingMinor_reduceAt_eq`

 If `γ ∈ S.termsOver c s c'`, that is, `h_c⁻¹ γ h_c'` lies in K and has reduction `s`, then for
each `l` the leading minor of order `l` of `S.frameProducts γ` is integral. At every place `w` in
`S.chosenPlaces i` its reduction `reduceAt w` equals the same minor of
`(S.latticeMiddle (ResField w)).frameGram (s i w)`. 

### `IsOpenElement.leadingMinor_ne_zero`

 If `s` is open, that is, at some chosen place above the first prime none of its proper leading
minors of frame products vanishes, then for every term `γ` over a block `(c, s, c')` no proper
leading minor of the frame products of `γ` vanishes: `γ` lies in the big cell. 

### `one_add_inv_pow_ten_pow_le`

 With `f` the number of infinite places, the factor `(1 + S.b⁻¹ ^ 10) ^ f` of the sieve is at
most `1 + S.b⁻¹ ^ 9`, because `f ≤ S.b / 1000` by the hypothesis `S.IsAdmissible`. 

### `one_add_pow_six_mul_add_pow_ten_le_one_add_pow_four`

 For `0 ≤ u ≤ 1 / 1000` one has `(1 + u⁶) ((1 + u⁹)² (1 + u⁶) + u¹⁰) ≤ 1 + u⁴`. With `u = b⁻¹`
this collects the error factors in `sieve_constant_le`. 

### `normalizingConst`

 The normalising constant `r` of the main term, used with `k = 𝔰.k - 1`: the product over the
infinite places of √`openCellConst` and powers of the squared scales `frameScaleSq` of the frame
vectors, divided by the number of Bessel coordinates. 

### `prod_poissonConst_eq`

 Assume `S.IsAdmissible` and `𝔰.k = kPred + 1`. The product of the Poisson summation constants
`S.poissonConst i` over `i < 𝔰.n` is `S.normalizingConst kPred ^ 2` times
`volÔ E ^ 𝔰.n (dim / Λ) ^ 2 / c_G ^ f`, where `dim = Fintype.card S.BesselCoord` is the number of
Bessel coordinates, `Λ = S.frameScaleProd`, `c_G = 𝔰.openCellConst` and `f` is the number of
infinite places. 

### `scaledSiegelConst_mul_decayConst_le`

 The error is measured against the identity second moment. Let `f` be the number of infinite
places, `n = 𝔰.n = ϱ + 1` the number of frame vectors, `k = 𝔰.k` and `dim` the number of Bessel
coordinates. The left side has three factors: the constant `scaledSiegelConst` of Siegel's step; the
quotient `vol(Ô) ^ n (dim / Λ)² / c_G ^ f` of the constants of Poisson summation by the squared
normalising constant, where `Λ = frameScaleProd` is a product of powers of the squared scales of the
frame vectors and `c_G = openCellConst = vol U(k)² / (vol U(k + 2ϱ + 1) vol U(k - 1))`; and
`decayConst`, the product over the infinite places `v` of a volume ratio of the shape times
`(|κ_v| ^ (2ϱ + 1) / (M N)) ^ (k - n⁷)` with `κ_v = S.realM v`. It is at most `b ^ (n⁹ f)` times
`dim * identitySecondMoment * unipotentCovolume²`. Here `identitySecondMoment` is the order of the
reduction of the Bessel subgroup times the number of classes times `dim`. 

### `sieve_constant_le`

 Let `S` be admissible with size parameter `b`, `kPred = 𝔰.k - 1`, and let the number `numSieved`
of places at which vectors are fixed be at most `f`, the number of infinite places. The theorem
`sieve` bounds a sum of last entry densities over pairs of heads by `(∏ i, poissonConst i) * ((∏ v,
(1 + b⁻¹⁰) / deg v) * m + ε)`. Here `poissonConst i`, the constant of Poisson summation in entry
`i`, is vol(Ô) over the Jacobian of the scaling at the infinite places; `deg v` is the degree of the
Bessel system at `v`; `m` bounds the mass at the finite places; and
`ε = b^(2403 𝔰.n⁹ f) * decayConst` is the error, `decayConst` being the product of the constants in
the decay at the infinite places. For `m = (1 + b⁻⁶) / b^(6 𝔰.k numSieved)`, this bound times the
constant `(1 + b⁻⁶) * scaledSiegelConst` of Siegel's step is at most `r² (1 + b⁻⁴) b^(-6 𝔰.k
numSieved) * mainSecondMoment * unipotentCovolume²`, where `r = S.normalizingConst kPred` and
`mainSecondMoment = sourceDim² / ((∏ v, deg v) * mass)`, with the mass of the genus of the standard
Hermitian lattice of rank `𝔰.r`. 

### `normalizingConst_sq_pos`

 The square of the normalising constant is positive. 

### `gramScalar_mul_headDensity`

 Let `P` be a structure of finite place on the product of the completions at `T`, and `G` a
filling datum for it. Let the head have ϱ first entries `p`, units off `T`, and last entry `t` with
‖t‖² > N² at every infinite place; `x v a` is its entry of index `a` under `Φ v` times
`S.frameScaleSq v a = κ_v^(2(ϱ - a)) / N`, the squared scale of the frame vector `a`
(`κ_v = S.realM v`). The first factor on the left is the product over `v` of the scalars of
`normalizedOrbitalIntegral` at `x v`; in it `openCellConst` is a ratio of volumes of compact unitary
groups and `(S.besselSystem v).Index` indexes a basis of the value space of the Bessel functions at
`v`. The second factor `G.headDensity` is a product of powers of the moduli of `p` for `P`. Their
product is `S.normalizingConst kPred`, with `kPred = 𝔰.k - 1`, times the square root of (∏ (‖t‖² -
N²))^(𝔰.k - 1). By the product formula the powers of `p` cancel; the constant collects
√`openCellConst`, the powers of the squared scales and the numbers of indices. 

### `prod_bandLimit_eq_gram`

 Let `S` be an admissible filling, and `σ` a rational element of the floor group (it fixes the
hyperbolic basis vectors `e_a`, `e*_a` for `a < ϱ`) with last frame product `t`. A head is a tuple
`p` of ϱ entries from a finite set `T₀` of units of `E`, followed by `t`; `x v p a` is its entry of
index `a` under the embedding `Φ v`, times the squared scale `S.frameScaleSq v a` of the frame
vector `a` at `v`. The Weyl element `w_p` of the head sends `e_a` to `p_a e*_a` and `e*_a` to
`e_a / p̄_a` for `a < ϱ`. Let `W = S.besselFn .cut` be the product over the infinite places of the
cut Bessel functions W♭, which have bounded support modulo the Bessel subgroup, and let
`besselOrbitalIntegral volume W γ` be the tensor ∫ W(g) ⊗ W(γ⁻¹ g)^* dg. Let `R p q` be the product
over `v` of `bandLimit 𝔰.n`, the top one of the forms on pairs of heads that the Bessel system at
`v` provides for the sieve. Then `R` is the Gram matrix of the orbital integrals at `γ = w_p σ`,
each weighted by the product over `v` of the scalar of `normalizedOrbitalIntegral`, √c_G · (|x_ϱ|² -
1)^((k - 1)/2) · |I|⁻¹ · ∏_{a<ϱ} |x_a|^(k + 1 + 2(ϱ - a - 1)), where `x = x v p`, `k = 𝔰.k`,
`c_G = 𝔰.openCellConst` and `I` is the index set of the Bessel system at `v`. 

### `IsFillingData.mul_sum_norm_sum_cosetAmplitude_sq_le`

 Siegel's step. Let `S` be an admissible filling of shape `𝔰` over a CM field `E` with Weil data,
and let `kPred = 𝔰.k - 1`. Let `1 / M`, `1 / N`, the lattice basis and its inverse be integral off
the finite set of places `T`. Let `P` be a structure of finite place on the product of the
completions at `T`, `G` a filling datum for it, and `Y` a group between the congruence group of `G`
and the integral points. Take finitely many distinct classes `(c i, S.reduction (n i), c' i, σ i)`,
with `σ i` in the floor group, last entry `t i` with ‖t i‖² > N² at every infinite place, position
integral off `T` and lift `n i` in `Y` at `T`.

On the left, `S.cosetAmplitude .cut c s c' γ` is the sum of the amplitudes of the cut function at
`u γ u'⁻¹` over the rational unipotent `u`, `u'` for which this element lies over `(c, s, c')`. It
is summed over `γ = w_p σ`, for the Weyl elements `w_p` of the heads with first entries `p` in a
finite set `T₀` of units off `T`. The squared norms of these class sums, times `r²` for the
normalising constant `r`, add up to at most `(1 + b⁻⁶) * S.scaledSiegelConst` times the real part of
a sum over the last entries and the pairs of heads. The summand is the product of the top forms
`bandLimit 𝔰.n` of the Bessel systems at the infinite places with the density `G.lastEntryDensity`
at `T`, divided by `Y.massRatio = vol(Y) vol(K) / fl²`, where `K` is the congruence group of `G` and
`fl = G.unipotentMass`. 

### `sum_norm_sum_cosetAmplitude_sq_le`

 Let `S` be an admissible filling of shape `𝔰` over a CM field `E` with Weil data, with size
parameter `b = S.b`, and `Sg` a set of chosen places above the first level prime p₀
(`S.chosenPlaces 0`). Take finitely many distinct classes `(c i, S.reduction (n i), c' i, σ i)`
whose last entries `t i` lie in a finite set `T₀` of units off `T`, whose positions are integral off
`T` and whose reductions are in `S.fixer Sg D`. Here `σ i` is in the floor group, its last frame
product is `t i`, and ‖t i‖² > N² at every infinite place; `1 / M`, `1 / N`, the lattice basis and
its inverse are integral off `T`. The double coset sum `S.cosetAmplitude .cut c s c' γ` adds the
amplitudes of the cut Bessel function at `u γ u'⁻¹` over the rational unipotent `u`, `u'` for which
this element lies over `(c, s, c')`. These sums, added over the heads with entries in `T₀`, have
total square norm at most `(1 + b⁻⁴) b^(-6 𝔰.k |Sg|)` times
`mainSecondMoment = sourceDim² / (besselDegree * mass)` times `unipotentCovolume²`. 

### `linkSecondMoment_isOpenElement_le`

 Let `S` be an admissible filling of shape `𝔰` over a CM field `E` with Weil data, `Sg` a set of
chosen places above the first level prime p₀, and `D w` a nonzero vector of the span of the frame
modulo `w` or modulo its conjugate. On the left, `linkSecondMoment` sums the squared norms of the
class sums of the cut function over all links, pairs of classes, and reductions `s` that are open
and fix `D w` for `w ∈ Sg`. With `X` the isotropic span of `e₁, …, e_ϱ`, the link of a term `γ` is
the module of pairs of classes in `X^⊥/X` of `t` and `γ⁻¹ t`, for `t` orthogonal to `X` and `γ X`;
each class sum runs over the terms of one link. Only terms `γ` with
`termDisc γ = |Δ|² - N² |Δ'|² ≠ 0` enter, where `Δ` is the determinant and `Δ'` the leading minor of
size ϱ of the frame products of `γ`. The bound is `(1 + b⁻⁴) b^(-6 𝔰.k |Sg|)` times
`mainSecondMoment = sourceDim² / (besselDegree * mass)` times `unipotentCovolume²`. Here `b` is the
size parameter of `S`, `𝔰.k` is the rank of X₀, `mass` is the mass of the genus of the standard
Hermitian lattice of rank `𝔰.r`, and `unipotentCovolume` is an explicit number which, if `E`
contains a primitive 5040th root of unity, is the integral of the cutoff `S.classCutoff c` over the
real unipotent group, for every class `c` (`lintegral_classCutoff_eq_unipotentCovolume`). 
