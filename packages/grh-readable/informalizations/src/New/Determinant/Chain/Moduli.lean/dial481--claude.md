---
{
  "module": "src/New/Determinant/Chain/Moduli.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/Moduli.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/Moduli.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Ratios of Hecke values and heights of functions of the twist

This file treats functions of an `m`-fold twist `ϑ` with modulus Q. Here `ϖ` generates the product
of the chosen places, and `D.twistModulus ϑ e` is the modulus `ϖ ^ e Q`, with exponent e at the
chosen places and 1 at the places of Q. It defines the ratios of Hecke values and the absolute
value of a function of the twist up to a constant and a power of the norm of Q. Heights are
stated with `New.HeightLe c y`: the family y, indexed by the ι : ℂ ≅ ℚ̄_l, has height at most c.

## Main definitions and results

* `New.Data.lRatioProd`, `New.Data.HasAbsUpToNormPower`: ratios of Hecke values, and the absolute
  value of a function of the twist up to a constant and a power of the norm of Q.
* `New.Data.CriticalPair.isTameFor_mul_and_lValueProd_eq`: for a ramified pair with character ν and
  a twist ξ, the character νξ and its inverse are tame, and their products of `L`-values are
  expressed by the ratios of Hecke values.

Notions from other files:
* `New.Data.MFoldTwist`: a twist ϑ whose tame part has ψ_wⁿ non-trivial for all w in Q and
  1 ≤ n ≤ m.
* `New.Data.CriticalPair`: an integer 1 ≤ z ≤ t and a character ν of weight −c, z ≤ c ≤ 4b, with
  tame part supported on the chosen places.


### `card_residueRing_twistModulus`

 The residue ring of the modulus ϖ^e·Q attached to ϑ, with (ϖ) the product of the chosen places,
has order (∏ N w)^e · ∏_{w ∈ Q} N w, the first product running over the chosen places w. 

### `lRatioProd`

 The product over `1 ≤ z ≤ s` of the ratios `|L^{MQ}(z, (ν ϑ)⁻¹) / L^M(z, ν⁻¹)|` of Hecke values,
where `L^M` omits the chosen places and their conjugates, and `L^{MQ}` also the places of the
modulus `Q` of `ϑ` and their conjugates. 

### `CriticalPair.L_inv`

 The character `ν` of a pair and its inverse have the same `L`-function away from the chosen
places and their conjugates. 

### `CriticalPair.L_mul_inv`

 For the character `ν` of a critical pair and a tame character `ϑ` of modulus `Q`, the character
`ν ϑ` and its inverse have the same `L`-function away from the chosen places, the places of `Q` and
their conjugates. 

### `CriticalPair.ofReal_lRatioProd`

 For a pair `p = (ν, z)`, the number `lRatioProd` is the product over `1 ≤ i ≤ z` of the ratios
`CriticalPair.ratio` `= |L(i, (ν ϑ)⁻¹)| / |L(i, ν⁻¹)|` of the pairs `p.lowerPoint i = (ν, i)`; the
sign argument of `CriticalPair.ratio` has its default value `1`. 

### `CriticalPair.lRatioProd_eq_prod_norm_div`

 For the character `ν` of a critical pair and a tame character `ϑ` of modulus `Q`, the product
`lRatioProd` of the ratios of Hecke values can be written without inverses, as the product over
`1 ≤ i ≤ s` of `|L^{MQ}(i, ν ϑ) / L^M(i, ν)|`. 

### `CriticalPair.lValueProd_mul_inv_eq`

 For a critical pair `p` (a character `ν = p.character` and an integer `z = p.z`) and a tame
character `ϑ` with places `ϑ.Q`, the number `lValueProd` up to `z` for `(ν ϑ)⁻¹` and the chosen
places together with `ϑ.Q` is a product of three factors. They are `lValueProd` for `ν` and the
chosen places, `ϑ.normQ ^ z ^ 2`, and `D.lRatioProd ν z ϑ ^ 2`, the square of the product of ratios
of Hecke L-values. 

### `CriticalPair.lRatioProd_one_pow`

 At the powers of the trivial twist the product of the ratios of Hecke values is `1`. 

### `HasAbsUpToNormPower`

 `c` has absolute value `f` up to a norm power: `‖c ϑ‖² = C (Nm Q)ᵏ (f ϑ)²` for all `m`-fold
twists `ϑ`, with `Q` the modulus of `ϑ` and with a real `C` and an integer `k` that do not depend on
`ϑ`. The case `C = 0`, where `c` vanishes for all twists, is allowed. 

### `HasAbsUpToNormPower.mul`

 If `c` has absolute value `f` up to a norm power and `c'` has absolute value `f'` up to a norm
power, then `c * c'` has absolute value `f * f'` up to a norm power. 

### `HasAbsUpToNormPower.of_norm_sq_eq_mul_card_zpow`

 A function of the twist whose squared norm is a constant times a power of the norm of `𝔪 = ϖᵉ Q`
has absolute value `1` up to a norm power. 

### `HasAbsUpToNormPower.prod`

 If each `γ a` has absolute value `F a` up to a norm power, then the product of the `γ a` has as
absolute value up to a norm power the product of the `F a`. 

### `HasAbsUpToNormPower.exists_norm_div_eq`

 Let `c` and `f` be a complex and a real function of the `m`-fold twist `ϑ`, and write
`N(Q) = ϑ.normQ` for the norm of the modulus `Q` of `ϑ`. Suppose `c` has absolute value `f` up to a
norm power, that is `‖c ϑ‖² = C N(Q)ᵏ (f ϑ)²` with `C` and `k` independent of `ϑ`, and that `f ≥ 0`,
`f 1 = 1` and `c 1 ≠ 0` at the trivial twist `1`. Then there is an integer `e` with
`‖c ϑ / c 1‖ = N(Q) ^ (e / 2) * f ϑ` for all `ϑ`. 

### `CriticalPair.hasAbsUpToNormPower_of_norm_sq_eq_lValueProd`

 Let `p = (ν, z)` be a critical pair, `e ≠ 0`, and `c` a complex function of the `m`-fold twist
`ϑ`. Write `Q` for the modulus of `ϑ` and `𝔪 = ϖᵉ Q`, with `(ϖ)` the product of the chosen places.
Suppose `‖c ϑ‖²` is a constant `C` times `lValueProd` up to `z` for `(ν ϑⁿ)⁻¹` and the places of
`𝔪`. Then `‖c ϑ‖² = C' N(Q)ᵏ (f ϑ)²` with `C'` and `k` independent of `ϑ`, where `f ϑ` is the
product `lRatioProd` of the ratios of Hecke values at `ϑⁿ`. 

### `IsRamifiedRatio`

 `F` is the product of the ratios of Hecke values of a ramified pair at the `n`-th powers of the
twists, for some `1 ≤ n ≤ m`. 

### `HasSmallRatios.heightLe_inv_rpow_mul_prod`

 Let `θ ι` be twists with small ratios: their moduli have norm `N ι = (θ ι).normQ` prime to `ℓ`,
and the inverse ratios of L-values of ramified pairs at their powers have height at most the cut-off
`D.x₁`. For `a` in a finite set `s`, let `F a` be a ramified ratio: `F a ϑ` is the product
`lRatioProd` of the ratios of Hecke values of a ramified pair at `ϑⁿ`, for a fixed `1 ≤ n ≤ m`. Then
the family `((N ι) ^ (e / 2) ∏_{a ∈ s} F a (θ ι))⁻¹` has height at most `#s · t · x₁`. 

### `IsRamifiedRatio.nonneg`

 A function `G` of the twist that is a ramified ratio (`IsRamifiedRatio`) is nonnegative at every
`m`-fold twist `ϑ`. 

### `quotientPair`

 The pair of the character `ν = (υ ^ (-Δ) χ) ^ n` and the integer `t`. Here
`υ = WeilData.upsilonU1` is the splitting character on the norm-one ideles, `Δ = D.gap`, and
`χ = D.chiM` has weight `0` and tame part `D.chiMLocal`, so `ν` has weight `-n Δ` and tame part
`D.chiMLocal ^ n`. As `D.untwistedLiftChar j = D.chiZero * (υ ^ (-Δ) χ) ^ j`, one has
`ν = D.untwistedLiftChar (i + n) / D.untwistedLiftChar i` for every `i`. 

### `isRamified_quotientPair`

 The tame part of `quotientPair n` is nontrivial exactly at the chosen places, since
`1 ≤ n ≤ m`. 

### `quotientRatio`

 The product of the ratios of Hecke values of the character
`D.untwistedLiftChar j / D.untwistedLiftChar i` at the twist `ϑ ^ (j - i)` (truncated subtraction),
over the points `1 ≤ z ≤ t`. The characters `D.untwistedLiftChar j = D.chiZero * (υ ^ (-D.gap) *
D.chiM) ^ j` of U(1)(𝔸), with `υ = WeilData.upsilonU1`, form a geometric progression. 

### `isRamifiedRatio_quotientRatio`

 For `i < j ≤ m`, `D.quotientRatio i j` is a ramified ratio (`IsRamifiedRatio`), with
`n = j − i`. It is the product of the ratios of Hecke values of
`D.untwistedLiftChar j / D.untwistedLiftChar i` at the powers ϑ^(j − i). 

### `isPrimitiveMulChar_of_isTameFor`

 Let ν be tame for the squarefree modulus 𝔪₀ = ϖQ with weight γ and character χ of O_E/𝔪₀: ν has
weight γ and a tame part (ψ_w) that is non-trivial exactly at the w ∣ 𝔪₀, and χ = ∏_{w ∣ 𝔪₀} ψ_w.
Then χ is primitive: for each a ≠ 0 in O_E/𝔪₀ some χ(1 + ca) is neither 0 nor 1. 

### `CriticalPair.isTameFor_mul`

 For a ramified critical pair with character `ν` of weight `-negWeight`, a twist `ξ` of modulus
`Q` and `e ≠ 0`, the character `ν ξ` is tame for `𝔪 = ϖᵉ Q` with weight `-negWeight`: its tame part
`ψ = p.tamePart * ξ.tamePart` is non-trivial exactly at the places of `𝔪`, and its character on
`O_E / 𝔪` is `charOfTamePart 𝔪 ψ = ∏_{w ∣ 𝔪} ψ_w`. 

### `CriticalPair.isTameFor_mul_inv`

 For a ramified critical pair with character `ν` of weight `-negWeight`, a twist `ξ` of modulus
`Q` and `e ≠ 0`, the character `(ν ξ)⁻¹` is tame for `𝔪 = ϖᵉ Q` with weight `negWeight`. 

### `CriticalPair.lValueProd_mul_zpow_eq`

 For a critical pair `(ν, z)`, a twist `ξ` of modulus `Q`, `e ≠ 0` and a sign, the number
`lValueProd` up to `z` for `(ν ξ) ^ sign` and the places of `𝔪 = ϖᵉ Q` equals the number for `ν` and
the chosen places, times `N(Q) ^ z ^ 2` and the square of the product of the ratios of Hecke
values. 

### `CriticalPair.isTameFor_mul_and_lValueProd_eq`

 Let `p = (ν, z)` be a ramified critical pair of `D` of weight `-negWeight`, so the tame part of
`ν` is non-trivial exactly at the chosen places. Let `ξ` be a twist, a tame character whose tame
part is non-trivial at each place of its modulus `Q`. Let `𝔪 = ϖᵉ Q` with `e ≠ 0`, where `ϖ` is the
product of the chosen places. Then `ν ξ` and its inverse are tame for `𝔪`: they have weights
`-negWeight` and `negWeight`, tame part non-trivial exactly at the places of `𝔪`, and character
`charOfTamePart` (or its inverse). For both of them, `lValueProd` equals that for `ν` and the chosen
places, times `ξ.normQ ^ z ^ 2` and the square of `lRatioProd`, the product of the ratios of Hecke
values. 

### `CriticalPair.isTameFor_inv_mul_pow`

 For a ramified critical pair `(ν, z)`, `1 ≤ n ≤ m` and `e ≠ 0`, the character `(ν ϑⁿ)⁻¹` is tame
for the modulus `twistModulus ϑ e = ϖᵉ Q` ((ϖ) the product of the chosen places, Q the modulus of
ϑ), with weight `negWeight`. 
