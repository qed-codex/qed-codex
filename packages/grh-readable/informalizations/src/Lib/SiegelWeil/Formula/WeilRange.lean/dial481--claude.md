---
{
  "module": "src/Lib/SiegelWeil/Formula/WeilRange.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Formula/WeilRange.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Formula/WeilRange.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Siegel sets and the Siegel–Weil formula in Weil's range

This file develops reduction theory for a hermitian space `S` split into `p` hyperbolic planes
(`P : New.SiegelWeil.CompleteSplitting S p`). It proves the Siegel–Weil formula for a space `T` of
rank greater than `2 p`. Write `a_x` for the Levi element `P.levi (Core.dyadicDiag x, 1)`, where
`New.Core.dyadicDiag x` is diagonal with entries `2 ^ x i` at the infinite places and `1` at the
finite places. Write `n(ν)` for `P.radicalElement 0 ν`. Siegel sets give the bound in the cusp used
in the proof of the formula.

## Main definitions and results

* `New.SiegelWeil.exists_compact_parabolic_normal_form`: a normal form `δ⁻¹ g = n(ν) a_x⁻¹ κ`
  adapted to a given rational Lagrangian.
* `New.SiegelWeil.exists_siegel_set`: every adelic point is `γ a_x κ` with `γ` rational, `x ≥ 0`,
  `κ` in a compact set.
* `New.SiegelWeil.exists_summable_zeroTerm_bound`: in Weil's range the zero terms
  `New.SiegelWeil.Lagrangian.zeroTerm`, composed with the normalised torus action
  `New.SiegelWeil.normalisedTorus` (`splitWeil S T`, the Weil representation on `𝒮 (S.hom T)`, of
  `a_x` scaled by `2 ^ (-d * card m * ∑ i, x i)`, with `d` the number of infinite places), are
  bounded by one summable function of the Lagrangian.
* `New.SiegelWeil.siegel_weil`: the mean of theta over `[U(T)]` is the sum of the zero terms.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to diag(s) at the infinite places and 1 at the finite places.
* `New.SiegelWeil.CompleteSplitting`: The splittings S = lE^p ⊕ kE^p into two isotropic frames l and
  k, which pair to p hyperbolic planes; `P.k` is the isotropic frame k and `P.kAdelic` is x⁻¹k, the
  same frame in standard coordinates.
* `New.Space.Splitting.levi`: The homomorphism GL_p(𝔸) × G(V₀) → G(V) sending (m, g₀) to the element
  with k ↦ km, ι ↦ ιg₀, l ↦ l m*⁻¹.
* `New.Space.Splitting.radicalElement`: `P.radicalElement 0 b`, written `n(b)`, is the unipotent
  element with k ↦ k and l ↦ l − k(½ȷ⁻¹(b + b*)), where ȷ is the purely imaginary element of
  `WeilData E`.
* `New.SiegelWeil.Lagrangian.zeroTerm`: The zero term along a Lagrangian L, which is the value at 0
  (`New.SiegelWeil.mixedValue`) in the Schrödinger model of a chosen complete splitting with
  kE^p = L.

## Relation to the literature

Siegel–Weil formula in the convergent range. Here a split space of rank 2p is paired
with a hermitian space of rank above 2p, both unimodular at every finite place, over a CM field `E`
with `WeilData E` (so it contains the 5040th roots of unity and E/E⁺ is unramified at the finite
places), and the Eisenstein series is written as a sum over Lagrangians. Source: A. Weil, Sur la
formule de Siegel dans la théorie des groupes classiques, Acta Math. 113 (1965), n° 52 Thm 5; the
method of proof follows Andrianov (1979), Harris (1981), and P. Garrett, The Siegel-Weil formula in
the convergent range (notes, 2005).

Reduction theory, namely the existence of Siegel sets. The compactness criterion of Mahler that it
uses is from `Lib.Adelic.Reduction.FiniteVolume`.


 ## Siegel sets and uniform summability of the zero terms 

### `radicalElement_eq_conj_levi`

 Conjugation by the Levi element of the invertible adelic matrix `a` sends the element
`n(b) = P.radicalElement 0 b` of the unipotent radical to `n(a b a*)`. 

### `exists_compact_parabolic_normal_form`

 Normal form for the complete splitting `P` of `S` into `p` hyperbolic planes, with isotropic
frame `k`. There is a compact set `Ω` such that for every adelic `g` and rational `γ` there
are a rational `δ`, integers `x`, a rational invertible `y` and a matrix `ν` with (a)
`δ⁻¹ g = n(ν) a_x⁻¹ κ` and `(ν, κ) ∈ Ω`, where `n(ν) = P.radicalElement 0 ν` is unipotent and
`a_x = P.levi (Core.dyadicDiag x, 1)` is the Levi element of the diagonal matrix with entries
`2 ^ x i` at the infinite places, and (b) `δ⁻¹ γ` acting on the isotropic frame `k` by
`k ↦ k y` (`P.ActsOnFrame`); so `δ k` and `γ k` span the same Lagrangian. 

### `exists_siegel_set`

 Siegel sets for a hermitian space `S` with complete splitting `P`: there is a compact `Ω` such
that every adelic point `g` of the unitary group is a rational point (embedded by `S.ratEmbed`)
times the Levi element of `dyadicDiag x`, the diagonal matrix with entries `2 ^ x i` at infinity and
`1` at the finite places, `x i ≥ 0`, times an element of `Ω`. 

### `tsum_div_two_pow_lt_top`

 Let `exps : ι → p → ℕ` give a vector of exponents for each index, let `d ≠ 0` and `C ≠ ∞`, and
suppose that, for every vector `x`, at most `C * (2 ^ d) ^ (∑ i, ∑ j, (x i + x j)) * N` indices have
exponents `x`. Then the sum over the indices `L` of `A / ((2 ^ d) ^ ∑ i, exps L i) ^ k` is finite
if `2 * card p < k`. 

### `exists_mul_k_apply_ne_zero`

 Let `δ` be a rational point of the unitary group of `S`. No column of `δ k` vanishes, where `k`
is the isotropic frame of the complete splitting `P`. 

### `lagrangian_isometrySplitting_comp_eq`

 Let `γ k` be orthogonal to the Lagrangian `L` of `S`, where `k` is the isotropic frame of the
complete splitting `P` (`h_orth` tests this on the frame of the chosen splitting of `L`), and let
`δ` be a rational isometry with `γ k = δ k y` for an invertible `y`. Then `L` is the Lagrangian
spanned by the columns of `δ k`: that is the Lagrangian of `(isometrySplitting δ).comp P`, the
splitting `P` moved by `δ`. 

### `exists_summable_zeroTerm_bound`

 Let `P` be a complete splitting of `S` into `p` hyperbolic planes and let `T` have rank greater
than `2 p`. There is a summable function `c` on the Lagrangians `L` of `S` such that, for every
`x : p → ℕ`, the operator norm of `Lagrangian.zeroTerm T L` composed with `normalisedTorus T P x` is
at most `c L`. Here the zero term along `L` sends `f` to its value at `0` in the Schrödinger model
of a splitting whose frame `k` spans `L`, and `normalisedTorus T P x` is `splitWeil S T` of the Levi
element `diag (2 ^ x i)` (entries `1` at the finite places) scaled by
`2 ^ (-d * rank T * ∑ i, x i)`, with `d` the number of infinite places. At `x = 0` this is the
convergence of the Eisenstein series in the Siegel–Weil formula. 


## The Siegel–Weil formula in Weil's range

`New.SiegelWeil.normalisedTorus T P x`, for `x : p → ℕ`, is the normalised action of the torus
element `diag (2 ^ x i)` (at the infinite places) of the Levi subgroup of `P`. Let `ℓ` be the
difference of the two sides of `New.SiegelWeil.siegel_weil`. Splitting off one isotropic line and
using induction on the rank of `S`, `ℓ ∘ normalisedTorus T P x` tends to `0` as any `x ι → ∞`.
Siegel sets turn this into a bound in the cusp, from which
`New.SiegelWeil.eq_zero_of_le_tsum_zeroTerm` gives `ℓ = 0`.


### `New.SiegelWeil.lCoord_mul_levi_dyadicDiag`

 Let `P` be a complete splitting of `S` with frame `k` and let `D₁` split off the line spanned by
the column `ι` of `k`. The Levi element of `diag (2 ^ x i)` scales the row `D₁.lCoord` by the
conjugate of `2 ^ (-x ι)` (at the infinite places; `twoAtInfinity E` is `2` there and `1` at the
finite places; `adeleMatrix` is the matrix of a group element in standard coordinates). The row
`D₁.lCoord` gives the `l`-coordinate of an adelic vector in `D₁`. 

### `New.SiegelWeil.tendsto_integral_theta_zeroTerm_sub`

 Let `P` be a complete splitting of `S` into `p` planes, let the rank of `T` exceed `2 p`, and
let `D₁` split off the isotropic line spanned by the column `ι` of `P.k`, with complement `S₁`. As
`x ι → ∞`, uniformly for `f` in a compact set `C`, the integral over `[U(T)]` of the difference
between the theta function of the zero term of `normalisedTorus T P x f` along the line and that of
`normalisedTorus T P x f` tends to `0`. Here `splitWeil` is the Weil representation of the pair of
unitary groups, `D₁.homSource T` is the splitting that `D₁` gives of the space on which it acts, and
`T.quotMeasure` is the measure of `[U(T)]`. 

### `New.SiegelWeil.tendsto_zeroTerm_of_notMem`

 Let `T` have nonzero rank, and let the Lagrangian `L` of `S` not contain the column `ι` of
`P.k`, where `P` is a complete splitting `S = l E ^ p ⊕ k E ^ p` with isotropic frame `P.k`. Then
the zero term along `L` of `normalisedTorus T P x f` tends to `0` as `x ι → ∞`, uniformly for `f` in
a set `C` of norm at most `R`. Here `normalisedTorus T P x` is the normalised action of the torus
element `diag (2 ^ x i)`, and the zero term along `L` sends `f` to the mean of `θ (ϱ z f)` over the
maps `z : S → T` vanishing on `L`, adelic modulo rational. 

### `New.SiegelWeil.bddAbove_norm_sub_tsum_norm_zeroTerm`

 Let `ℓ` be a continuous linear functional on `𝒮 (S.hom T)` that is invariant under the rational
points of `S`. Suppose that `ℓ (normalisedTorus T P x f)` tends to `0` as any `x ι → ∞`, uniformly
for `f` in compact sets, and that the zero terms are absolutely summable over the Lagrangians of
`S`. Then for each `f`, `‖ℓ (ω(g) f)‖` exceeds `∑' L, ‖zeroTerm L (ω(g) vacElem)‖` by at most a
constant independent of `g`. Here `ω(g)` is `splitWeil S T (g, 1)`, `vacElem` is the vacuum vector
of `𝒮`, `normalisedTorus T P x` is the normalised action of the torus element `diag (2 ^ x i)`, and
the zero term along a Lagrangian `L` sends `f` to the mean of `θ (ϱ z f)` over the maps `z : S → T`
vanishing on `L`, adelic modulo rational. 

### `New.SiegelWeil.exists_lagrangian_equiv_col_mem`

 Let `D₁` split off the isotropic line spanned by the column `ι` of `P.k`. The Lagrangians of the
complement `S₁` correspond to the Lagrangians of `S` through that line, and the zero term along the
image of `L` is the zero term along `L` taken after the zero term along the line. 

### `New.SiegelWeil.tendsto_tsum_zeroTerm_sub_integral_theta`

 The induction step of the Siegel–Weil formula. In Weil's range, let `D₁` split off the line
spanned by the column `ι` of `P.k`, let the zero terms of `S` be summable and theta integrable, and
let the formula hold for the complement `S₁`. Then the difference of the two sides of the formula
for `S` at `normalisedTorus T P x f` tends to `0` as `x ι → ∞`, uniformly for `f` in a compact
set. Here Weil's range means `2 * card p < card m`, `θ` is the theta functional on the test
functions and `splitWeil` is the Weil representation of the pair of unitary groups. 

### `New.SiegelWeil.integrable_theta_splitWeil`

 If `T` has rank greater than `2 p`, the theta function `h ↦ θ (ω(1, h) f)` is integrable over
the quotient `[U(T)]` for every test function `f`, where `ω` is `splitWeil S T`. 

### `New.SiegelWeil.siegel_weil`

 The Siegel–Weil formula in Weil's range. Let `S` be split into `p` hyperbolic planes and let `T`
have rank greater than `2 p`. Then the operator norms of the zero terms along the Lagrangians `L` of
`S` are summable. Moreover, for every `f` the function `h ↦ θ (ω(1, h) f)` is integrable for the
measure `T.quotMeasure` of the quotient `[U(T)]`, and its mean (integral divided by total mass)
equals the sum of the zero terms of `f`, that is, the Eisenstein series at `f`. Here `ω` is the Weil
representation `splitWeil S T`, `𝒮 (S.hom T)` is the space of test functions on which it acts, and
the zero term of `f` along `L` is the value of `f` at `0` in the Schrödinger model of a splitting
whose isotropic frame spans `L`. An integrable majorant of theta that is uniform in `f` is given by
`New.SiegelWeil.theta_normalisedTorus_le`.

The pairs are unimodular over a CM field with `WeilData`, and the test functions are taken in `𝒮`
rather than among Schwartz–Bruhat functions. 
