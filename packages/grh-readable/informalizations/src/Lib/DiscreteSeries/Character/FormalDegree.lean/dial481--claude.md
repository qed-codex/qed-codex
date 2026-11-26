---
{
  "module": "src/Lib/DiscreteSeries/Character/FormalDegree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Character/FormalDegree.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Character/FormalDegree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Harish-Chandra's formula for formal degrees and stable orbital integrals

`New.Orbital.formalDegree_eq_weylDimensionPoly` is Harish-Chandra's formula for the formal degree of
a discrete series of `G = U(diag ε)`, and `New.Orbital.neg_one_pow_mul_sum_integral_dsKernel` gives
the stable sum of the orbital integrals of `New.HCParam.dsKernel` over the compact torus, both for a
parameter `l = 2λ` of gap `500 n³ + 10 n⁵`; `New.Orbital.harish_chandra_degree_and_orbital` states
the two together. By `New.Orbital.exists_laurent_orbital_integral` the orbital integral times a
product of roots is a Laurent polynomial; it is identified by comparing monomials of low level
(`New.Orbital.orbital_eq_char_sub_offOrbitIntegral`, `New.Orbital.coeff_eq_zero_of_low_level`).
The formal degree, with its constant, is read off from one coefficient in this comparison. The
orbital integrals converge absolutely by `New.Orbital.integrable_dsCoeff_conj`.

Conventions: `New.HCParam.rootProd l r` is the product of `x_a - x_b` over the pairs with
`r (ε a) (ε b)` and `l b < l a`, and `New.HCParam.lowerCount l r a` counts these `b`;
`New.Orbital.alternant ε κ` is the alternant over the permutations that preserve the signs `ε`;
`New.Orbital.torusEval x` evaluates a Laurent polynomial at a point `x` of the torus.

Notions from other files:
* `New.Orbital.oppositePairs`: The finite set of pairs of indices (a,b) with ε_a = +1 and ε_b = −1.
* `New.weylDimensionPoly`: The product of `λ i - λ j` over the pairs with `λ j < λ i`, divided by
  `∏_{i < card n} i!`, for `l = 2λ`.
* `New.HCParam.formalDegree`: For signs ε and l=2λ, the reciprocal of the integral over U(diag ε) of
  the squared modulus of the matrix coefficient `l.dsCoeff`, for the compact dual measure.
* `New.HCParam.kTypeChar`: `l.compactForm.lowestKType.kTypeChar` is the character of U(n) of
  highest weight λ − ρ.
* `New.HCParam.HasGap`, `New.HCParam.HasLargeGap`: l=2λ has distinct entries ≡ n−1 mod 2, and
  |λ_i−λ_j| ≥ h whenever ε_i ≠ ε_j; `HasLargeGap A` is the gap h = 500n³+A.

## Relation to the literature

Known result: Discrete series character on the compact Cartan via orbital integrals, and formal
degree. This is done only for U(p,q), for parameters of gap 500n³+10n⁵ and for the explicit
coefficient of the lowest K-type. It gives the formal degree, and the stable sum of elliptic orbital
integrals as a multiple of the conjugate of Weyl's character of the compact form, both exact in the
compact dual measure. Source:
Harish-Chandra, Discrete series for semisimple Lie groups II: explicit determination of the
characters, Acta Math. 116 (1966), Thm 16 (with part I, Acta Math. 113 (1965), Thm 3); Knapp,
Representation Theory of Semisimple Groups (1986), Thm 12.7.


### `dotProduct_add_gain_le_comp_perm`

 Rearrangement with a gain: if `o` strictly reverses the order of `b`, then permuting `b` by `w`
raises `o ⬝ᵥ b` by at least `|b i - b (w i)|`, for every `i`. 

### `sum_sign_mul_eval_alternant`

 Antisymmetrising the alternant over the Weyl group of `K` (the permutations that fix the signs
`ε`) gives the alternant over all permutations, as many times as that group has elements. 

### `lowerCount_dotProduct_lt_of_coeff_ne_zero`

 Here the level of an exponent is its dot product with `o = (-l).compactForm.lowerCount Eq`, the
vector that counts the larger entries of `l`. `l.rootProd r` is the Laurent polynomial ∏ (x_a − x_b)
over the pairs with `r (ε a) (ε b)` and `l b < l a`, and `(-l).lowerCount r a` counts the `b` with
`r (ε a) (ε b)` and `l a < l b`; `compactForm` is `l` with all signs set to 1, so there the
condition is `r 1 1`. For `N = 4 n²` and an exponent `γ` of
`l.compactForm.rootProd r * l.rootProd Ne ^ N`, the level of `(-l).compactForm.lowerCount r + N •
(-l).lowerCount Ne` is less than that of `γ` plus `500 n³ + 10 n⁵`. 

### `coeff_top_of_isConeSeriesMultiple`

 Let `o` strictly reverse and `b` strictly keep the order of the injective parameter `l`. Let
`P = D ^ k · t` with `D = (-l).rootProd Ne`, where `t` is a formal series with `t a = 1` and each
exponent of `t` occurs in `alternant ε μ` for some `μ` with `μ - a` in the positive root cone of `l`
(`IsConeSeriesMultiple`). Let `δ = (-l).lowerCount Ne` be the exponent of the highest-level term of
`D` and suppose `a + k • δ = b`; then `P` has coefficient `1` at `b`, and for every exponent `γ` of
`P` some permutation `w` with `ε ∘ w = ε` gives `o ⬝ᵥ γ ∘ w ≤ o ⬝ᵥ b`. 

### `prod_compact_mul_prod_noncompact`

 The product of the compact roots that are positive for `l` times that of the noncompact ones is
the product of all positive roots, which is the Weyl denominator of the compact form. 

### `prod_noncompact_neg`

 If `l` has a gap (so that its entries are distinct), then reversing the order of `l` multiplies
the product of the noncompact positive roots by `-1` to the power `#(oppositePairs ε)`, which is
their number. 

### `lowestKType_add_lowerCount_eq`

 The exponent `lowestKType + lowerCount Eq` in Weyl's formula for the lowest `K`-type, for any
signs `ε'` (`toHCParam ε' l` is `l` regarded for these signs), is
`paramAddRho l + (toHCParam 1 (-l)).lowerCount Eq`, a vector independent of the signs
(`paramAddRho l` is `λ + ρ`), minus the count of the negative noncompact roots. 

### `add_smul_lowerCount_lt`

 Let `l` have gap `500 n³ + 10 n⁵`, let `2 κ = l + n - 1` and let `N = 4 n²`. Then
`κ + N • (-l).lowerCount Ne` keeps the order of `l`. 

### `coeff_mul_alternant_of_level_le`

 Let `o` strictly reverse the order of `κ`, let entries of `κ` at indices of different sign `ε`
be at least `h` apart, and let `m < o ⬝ᵥ κ + o ⬝ᵥ β + h` for every exponent `β` of `Q`. Then the
products of `Q` with the alternants of `κ` over all permutations and over those that fix the signs
`ε` have the same coefficients up to level `m`. 

### `eq_smul_of_coeff_eq_of_level_le`

 Let `P` and `Q` be antisymmetric under the Weyl group of `K`, and let each of their exponents
have a Weyl conjugate of level at most `m`. If `P` and `c • Q` agree up to level `m`, they are
equal. 

### `lowerCount_neg_compactForm_lt`

 The number of entries of `l` above `l i` strictly reverses the order of `l`. 

### `numeratorExponent`

 The exponent `κ` of the numerator in Weyl's character formula for the compact form of `l`. It
is `paramAddRho l` plus the vector that counts, at `i`, the entries of `l` above `l i`. 

### `two_mul_numeratorExponent`

 The exponent of Weyl's numerator is `(l + n - 1) / 2`. 

### `torusEval_rootProd_mul_kTypeChar`

 Weyl's character formula for the compact form of `l`: the Weyl denominator times the character
of the lowest `K`-type is the full alternant of `numeratorExponent l`. 

### `level_add_lt_of_coeff_ne_zero`

 The bound of `lowerCount_dotProduct_lt_of_coeff_ne_zero` for the product `(-l).rootProd Ne` of
the negative noncompact roots in place of `l.rootProd Ne`, with both sides shifted by the level of
`a`. 

### `coeff_pow_mul_alternant_one_of_level_le`

 Let `l` have gap `500 n³ + 10 n⁵`, let `D = (-l).rootProd Ne`, `N = 4 n²` and
`κ = numeratorExponent l`, and let the level of `γ` be `(-l).compactForm.lowerCount Eq ⬝ᵥ γ`. At
exponents of level at most that of `κ + N • (-l).lowerCount Ne`, the products of `D ^ N` with the
alternants of `κ` over all permutations and over the Weyl group of `K` have equal coefficients. 

### `isWeylAntisymm_pow_mul_alternant`

 For injective `l`, a power of the product of the negative noncompact roots times the alternant
of `κ` is antisymmetric under the permutations that fix the signs `ε`. 

### `isConeSeriesMultiple_pow_mul_alternant`

 For injective `κ`, a power of the product of the negative noncompact roots times the alternant
of `κ` is that power times a series `t` with `t κ = 1` whose exponents each occur in some
`alternant ε μ` with `μ - κ` in the positive root cone of `l` (`IsConeSeriesMultiple`): the series
is the alternant. 

### `formalDegree_mul_kTypeNormSq_and_isOrbitalLaurent`

 Let the Harish-Chandra parameter `l` for the signs `ε` have gap `500 n³ + 10 n⁵`
(`HasLargeGap (10 * n ^ 5)`), let `D = (-l).rootProd Ne` be the product of the negative noncompact
roots, and let `N = 4 n²`. Then `l.formalDegree` times the squared norm `kTypeNormSq` of the lowest
`K`-type of the compact form equals `1`. Moreover `Vc · D ^ (N + 1) · Θ = D ^ N · alternant ε
(numeratorExponent l)` (`IsOrbitalLaurent`), where `Θ x` is `l.formalDegree` times
`∫ g : USign ε, l.dsCoeff (g⁻¹ * diagTorus ε x * g)`, the normalised orbital integral of `l.dsCoeff`
on the diagonal torus, `Vc` is the Weyl denominator of `K`, the alternant is summed over the Weyl
group of `K`, and `numeratorExponent l` is the numerator exponent in Weyl's character formula for
the compact form.

The second part is Harish-Chandra's character formula on the compact torus, for the normalised
orbital integral of `l.dsCoeff`, with denominators cleared and only for parameters of this gap. 

### `formalDegree_eq_weylDimensionPoly`

 **Harish-Chandra's formal degree formula**, for a parameter `l` of gap `500 n³ + 10 n⁵`: the
formal degree of the discrete series, for the compact dual measure, is the value
`weylDimensionPoly l` of Weyl's dimension polynomial. 

### `integrable_dsCoeff_conj`

 Absolute convergence of the orbital integrals: for a parameter `l` of gap `500 n³ + 10 n⁵` and a
regular point `x` of the compact torus, `g ↦ l.dsCoeff (g⁻¹ x g)` is integrable on `U(diag ε)`.

This is Harish-Chandra's convergence theorem for regular orbital integrals of Schwartz functions,
restricted to one discrete series coefficient (a Schwartz function by Harish-Chandra) of
`U(diag ε)`, the compact torus and parameters of large gap. 

### `neg_one_pow_mul_sum_integral_dsKernel`

 Let the Harish-Chandra parameter `l = 2λ` have gap `500 n³ + 10 n⁵`, and let `l.dsKernel g` be
`l.formalDegree` (`deg_λ`) times the conjugate of the discrete series coefficient `l.dsCoeff g`
(`c_λ(g)`). At a regular point `x` of the compact torus, the stable sum of the orbital integrals of
`l.dsKernel` is, up to the sign `(-1) ^ #(oppositePairs ε)`, the order of the Weyl group of `K`
times the conjugate of Weyl's character of `U(n)` of highest weight `l.compactForm.lowestKType`.
Here `oppositePairs ε` is the set of pairs `(a, b)` with `ε a = 1` and `ε b = -1`.

This is a consequence of Harish-Chandra's elliptic orbital integral formula for discrete series
coefficients. It gives only the sum over all permutations, and the integrals converge absolutely by
`integrable_dsCoeff_conj`. 

### `harish_chandra_degree_and_orbital`

 Let `l = 2λ` be a Harish-Chandra parameter for the signs `ε`, with `n` nonempty and gap
`500 n³ + 10 n⁵`. Then (a) the formal degree, the reciprocal of `∫ |c_λ|²` over `USign ε`, equals
`weylDimensionPoly l`; (b) at every regular point `x` of the compact torus (`x` injective), the sum
over all permutations `σ` of the orbital integrals `∫ l.dsKernel (g⁻¹ diag(x ∘ σ) g) dg`, which
converge absolutely by `integrable_dsCoeff_conj`, times `(-1)` to the number of pairs `(a, b)` with
`ε a = 1` and `ε b = -1`, equals `#{σ | ε ∘ σ = ε}` (the order of the Weyl group of `K`) times the
conjugate of Weyl's character `l.compactForm.lowestKType.kTypeChar` of the compact form at
`diag(x)`. Here `c_λ` is `l.dsCoeff`, `deg_λ` is `l.formalDegree`, and `l.dsKernel` is `deg_λ` times
the complex conjugate of `c_λ`.

These are Harish-Chandra's formal degree formula and the stable form, summed over all permutations,
of his formula for elliptic orbital integrals of discrete series coefficients, for U(p, q),
parameters with large gap and one coefficient. 
