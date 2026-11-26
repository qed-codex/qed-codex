---
{
  "module": "src/New/OneLift/HeckeValues/TwistedRatio.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/TwistedRatio.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/TwistedRatio.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The algebraic part as a Hecke L-value, and products of L-values of twists

Let `p = (ν, z)` be a critical pair and `ϑ` a tame character of modulus `Q`. For the statements on
`algPart` and `integralAlgebraicPart` assume `z ≥ 2` and fix an index set with `2 z` elements
(`New.Data.CriticalPair.HasLiftRank`). The number `New.Data.CriticalPair.algPart` is the normalised
squared norm of the lift `New.Data.CriticalPair.trivialLift` of `ν ϑ`. It is positive and equals a
constant independent of `ϑ` times an `L`-value of `ν ϑ`, so the ratio of the absolute values of the
twisted and untwisted `L`-values, which is nonzero, is a ratio of values of `algPart`.

## Main definitions and results

* `New.Data.CriticalPair.algPart_pos`, `New.Data.CriticalPair.exists_ne_zero_algPart_eq_mul_L`: the
  number `New.Data.CriticalPair.algPart` is positive, and it is a nonzero constant independent of
  `ϑ` times an `L`-value of `ν ϑ`. `New.Data.CriticalPair.exists_algPart_eq_mul_L` states the value
  with the positivity.
* `New.Data.CriticalPair.ratio_eq_algPart_div`: the ratio `New.Data.CriticalPair.ratio` of the
  absolute values of twisted and untwisted `L`-values is a ratio of values of `algPart`.
* `New.Data.CriticalPair.exists_integralAlgebraicPart_eq_mul_L`,
  `New.Data.CriticalPair.ratio_eq_integralAlgebraicPart_div`: the same value and ratio for the
  multiple `New.Data.CriticalPair.integralAlgebraicPart`, with the `L`-value of `(ν ϑ)⁻¹`.
* `New.Data.CriticalPair.exists_ofAlgForm_trivialLift_eq_smul_lift`,
  `New.Data.CriticalPair.formAction_trivialLift`: the lift is a nonzero multiple of the theta lift
  of the constant function `1`, and the finite group of rank one at the chosen places fixes it.
* `New.Data.CriticalPair.lValueProd_eq_mul_prod_ratio_sq`: the product `New.Exchange.lValueProd` of
  squared L-values for the twist is the untwisted one times a power of the norm of `Q` and the
  squared ratios at `1, …, p.z`.

Notions from other files:
* `New.Data.CriticalPair`: a critical pair `p = (ν, z)`, of an integer `1 ≤ z ≤ D.t` and a character
  `ν` of U(1)(𝔸) of weight `-c` with `z ≤ c ≤ 4 D.b`, whose tame part is supported on the chosen
  places (`New.Data.IsChosen`).
* `New.Data.TameChar`: a character `ϑ` of U(1)(𝔸) of weight 0 with tame part supported on a finite
  set `Q` of places; `ϑ.normQ` is the product `N(Q)` of the norms of the places of `Q`.
* `New.AutChar.L`: `ν.L S` is the `L`-function of `x ↦ ν (x / x̄)` without the Euler factors at `S`
  and at the conjugates of the places of `S`, as an Euler product at real points `s > 1` and as
  its limit from the right at `s = 1`.
* `New.Data.CriticalPair.lValueData`: the data (`New.LValueData`) of the theta lift from U(1) to the
  definite `U(2 z)` for the character `ν ϑ`.
* `New.Data.CriticalPair.trivialLift`: the lift of `ν ϑ`, a nonzero multiple of the unscaled lift
  `New.LValueData.trivialLift`, which is the sum of the theta kernels over the classes of U(1).
* `New.Data.CriticalPair.algPart`: the number `‖φ‖ ^ 2 / N(Q) ^ (2 z - 1)`, where `φ` is the lift of
  `ν ϑ`; `integralAlgebraicPart` is a multiple of it by a natural number that does not depend on
  `ϑ`.

## Relation to the literature

Known; see `Lib.SiegelWeil.RallisInner.SharpData` for sources.



## The algebraic part as a multiple of a Hecke L-value

Fix an index set `n` with `2 z` elements, where `z ≥ 2` (`New.Data.CriticalPair.HasLiftRank`).
`TameChar.one` is the trivial character, with `Q = ∅`.


### `exists_norm_sq_trivialLift_eq_mul_L`

 The unscaled lift `(lValueData H ϑ).trivialLift` of a tame character `ϑ` is the algebraic form
on the definite unitary group `U(n)` obtained from `ν ϑ` on U(1) as the sum of the theta kernels
over the classes of U(1). There is a constant `C ≠ 0` such that, for every `ϑ` of modulus `Q`, the
square of the norm of this lift is `C` times the `L`-value of `(ν ϑ)⁻¹` at `z`, away from the chosen
places, `Q` and their conjugates, times `N(Q) ^ (card n - 1)`. 

### `cast_chosenGroupOrder_mul_denomBound_sq_ne_zero`

 The factor `D.chosenGroupOrder * p.denomBound ^ 2` by which `integralAlgebraicPart` is a
multiple of `algPart` is nonzero in `ℂ`. Here `D.chosenGroupOrder` is the product of the orders of
the groups `GL (r t)` over the residue fields at the chosen places, and `p.denomBound` is a
denominator for the values of the lift. 

### `vacuumScale_pow_mul_pow_rowLengthSum_ne_zero`

 The scalar `P.vacuumScale D.towerExp ^ k * (star D.piMBar * P.jetScale D.towerExp) ^
p.rowLengthSum` is nonzero. It is the scalar by which `trivialLift` is a multiple of the unscaled
lift, for an index set with `k` elements. 

### `L_inv_mul`

 Let `p = (ν, z)` be a pair and `ϑ` a tame character. Without the Euler factors at the chosen
places, the modulus `ϑ.Q` and their conjugates, the `L`-functions of `ν ϑ` and of its inverse
agree. 

### `neg_negWeight_ne_zero`

 The weight `-c` of the character `ν` of a pair `p = (ν, z)`, that is, the function
`v ↦ -(p.negWeight v)` on `D.Φ` with `c = p.negWeight`, is not zero, as `1 ≤ z ≤ c(v)` for every
`v`. 

### `L_mul_ne_zero`

 Let `p = (ν, z)` be a pair and `ϑ` a tame character. The `L`-function of `ν ϑ`, without the
Euler factors at the chosen places, the modulus `ϑ.Q` and their conjugates, is not zero at `z`. 

### `trivialLift_ne_zero`

 Let `p = (ν, z)` be a critical pair with `z ≥ 2` and `ϑ` a tame character. The lift
`trivialLift H ϑ` of the character `ν ϑ`, from U(1) to the definite `U(2 z)`, is nonzero. 

### `algPart_pos`

 Let `p = (ν, z)` be a critical pair and `H` the hypothesis that the index set `n` has `2 z`
elements, with `z ≥ 2`, and let `ϑ` be a tame character. The algebraic part `algPart H
ϑ = ‖trivialLift H ϑ‖ ^ 2 / N(Q) ^ (card n - 1)` is a positive real number. 

### `exists_ne_zero_algPart_eq_mul_L`

 Let `p = (ν, z)` be a critical pair and `H : p.HasLiftRank n` the hypothesis that the index set
`n` has `2 z` elements, with `z ≥ 2`. For a tame character `ϑ` of modulus `Q`, `algPart H ϑ` is the
algebraic part of the `L`-value of `ν ϑ` at `z`, defined as `‖φ‖ ^ 2 / N(Q) ^ (card n - 1)`. Here
`φ = trivialLift H ϑ` is the scaled lift of `ν ϑ` to `U(n)`, and `N(Q)` is the product of the norms
of the places of `Q`. There is a constant `A ≠ 0` such that, for every `ϑ`, this number is `A` times
the `L`-value of `ν ϑ` at `z`, without the Euler factors at the chosen places, the modulus `Q` and
their conjugates. 

### `exists_algPart_eq_mul_L`

 For every tame character `ϑ` of modulus `Q`, the algebraic part `algPart H ϑ = ‖trivialLift H ϑ‖
^ 2 / N(Q) ^ (card n - 1)`, the normalised squared norm of the lift of `ν ϑ`, is positive. It is the
`L`-value of `ν ϑ` at `z`, without the factors at the chosen places, the modulus and their
conjugates, times a number `A` that depends neither on `ϑ` nor on its modulus. 

### `ratio_eq_algPart_div`

 The sign in `p.ratio ϑ` is the default `1`, so this is the ratio of the absolute values of the
`L`-values at `z` of `(ν ϑ)⁻¹` and of `ν⁻¹`. It is equal to the algebraic part `algPart H
ϑ = ‖trivialLift H ϑ‖ ^ 2 / N(Q) ^ (card n - 1)`, the normalised squared norm of the lift of `ν ϑ`,
divided by the same number for the trivial character. 

### `integralAlgebraicPart_ne_zero`

 Let `p = (ν, z)` be a critical pair with `z ≥ 2` and `ϑ` a tame character. The number
`integralAlgebraicPart H ϑ`, a natural multiple of the normalised squared norm of the lift of `ν ϑ`,
is nonzero. 

### `exists_integralAlgebraicPart_eq_mul_L`

 There is a constant `A ≠ 0` such that, for every tame character `ϑ`, `integralAlgebraicPart H ϑ`
is `A` times the `L`-function of `(ν ϑ)⁻¹` at `z`, without the Euler factors at the chosen places
(`New.Data.IsChosen`), the places of the modulus `ϑ.Q` and their conjugates. 

### `ratio_eq_integralAlgebraicPart_div`

 Let `p = (ν, z)` be a critical pair, `H : p.HasLiftRank n` and `ϑ` a tame character. The ratio
`p.ratio ϑ` of the absolute values of the `L`-values at `z` of `(ν ϑ)⁻¹` and of `ν⁻¹` equals
`integralAlgebraicPart H ϑ / integralAlgebraicPart H TameChar.one`. 

### `ratio_ne_zero`

 For a pair `p = (ν, z)`, a tame character `ϑ` and a sign `s = ±1`, the ratio `p.ratio ϑ s` of
the absolute values of the `L`-values at `z` of `(ν ϑ ^ s)⁻¹` and of `ν⁻¹` is nonzero. 

### `star_ratio`

 For a pair `p`, a tame character `ϑ` and a sign `s = ±1`, the ratio `p.ratio ϑ s`, a quotient
of absolute values, is real: complex conjugation fixes it. 

### `ratio_ne_zero_and_real`

 For a pair `p = (ν, z)`, a tame character `ϑ` and a sign `s = ±1`, the ratio `p.ratio ϑ s` of
the absolute values of the `L`-values at `z` of `(ν ϑ ^ s)⁻¹` and of `ν⁻¹` is nonzero and real. 

### `LValueData.formAction_trivialLift`

 Let `X` be data for the lift from U(1) to the definite unitary group on `m`, with descent pair
`X.descentPair` (the line, the group on `m` and the character of `X`). The product `ChosenGL Unit`
of the groups `GL₁` over the residue fields at the chosen places, which acts on algebraic forms by
`formAction`, fixes `X.trivialLift`, a multiple of the theta lift of the constant function `1`. 

### `exists_ofAlgForm_trivialLift_eq_smul_lift`

 Let `p = (ν, z)` be a critical pair with `z ≥ 2` and `ϑ` a tame character. Let `O` be the
descent pair `(lValueData H ϑ).descentPair` of the lift from U(1) to `U(2 z)`, with weight
`O.columnCount`. The function on the adelic group `U(2 z)(𝔸)` attached by `ofAlgForm` to the
algebraic form `trivialLift H ϑ` (its matrix coefficient against the highest vector for the
parameter `O.paramV`, all signs being `1`) is a nonzero multiple of the theta lift, by the theta
kernel `O.pairThetaKernel`, of the constant function `1` on the adelic group `New.G` of U(1), taken
at the Schwartz function `O.fockDatum` made from that highest vector. 

### `formAction_trivialLift`

 Let `p = (ν, z)` be a critical pair, with `H` saying that `n` has `2 z` elements and `z ≥ 2`,
and let `ϑ` be a tame character. The product of the groups `GL₁` over the residue fields at the
chosen places of `lValueData H ϑ` acts by `formAction`, and it fixes the lift `trivialLift H ϑ` of
`ν ϑ`. 


## Products of squared L-values of a twist

The section opens with `New.Data.IsRegularFamily.heightLe_of_eq_zpow_mul`: for a family of twists
with `IsRegularFamily`, a bound on the height of a family of numbers survives multiplication by
powers of the norms of the moduli, such as the power in
`New.Data.CriticalPair.lValueProd_eq_mul_prod_ratio_sq`.


### `IsRegularFamily.heightLe_of_eq_zpow_mul`

 For each pair `ι` of a prime `ℓ` and an isomorphism `ℂ ≃ ℚ̄_ℓ` let `θ ι` be an `m`-fold twist
(`New.Data.MFoldTwist`: a twist whose tame part has nontrivial powers of exponent `1, …, m` at the
places of its modulus, for the number `m = D.m` fixed by the data `D`). Assume that the
family is regular (`New.Data.IsRegularFamily`: small ratios and bounded denominators), so that the
norm of the modulus of `θ ι` is prime to `ℓ`. Height at most `c` (`New.HeightLe`) means that there
are `H ≠ 0`, a real `α` and reals `h ℓ ≥ 0` with `‖σ H‖ ≤ exp α` for every automorphism `σ` of `ℂ`,
with `ℓ`-adic absolute value of `H * y ι` at most `ℓ ^ h ℓ` for every `ι`, and with
`α + ∑ ℓ ∈ T, h ℓ * log ℓ ≤ c` for every finite set `T` of primes. If the family `y` has height at
most `c ≤ c'`, and each `y' ι` is zero or is `y ι` times an integer power of that norm, then `y'`
has height at most `c'`. 

### `CriticalPair.lowerPoint`

 The pair with the same character as `p` and the point `max 1 (min z p.z)`; for `1 ≤ z ≤ p.z`
this is `z`. Clamping makes the definition total. 

### `TameChar.disjoint_isChosen_Q`

 No place of the modulus `Q` of a tame character `ϑ` is a chosen place. 

### `CriticalPair.ratio_lowerPoint`

 For `1 ≤ z ≤ p.z`, the ratio of the pair `p.lowerPoint z = (ν, z)` at a tame character `ϑ` and
a sign `s` is the quotient of the absolute values of the `L`-values at `z` of `(ν ϑ ^ s)⁻¹` and of
`ν⁻¹`. 

### `CriticalPair.lValueProd_eq_mul_prod_ratio_sq`

 Let `p` be a pair with character `ν`, let `ϑ` be a tame character of modulus `Q` and `s` a sign.
Recall `lValueProd S χ e = ∏_{w ∈ S} q_w ^ e ^ 2 * ∏_{1 ≤ z ≤ e} |L^S(z, χ)| ^ 2`. This product up
to `p.z` for `(ν ϑ ^ s)⁻¹`, away from the chosen places and `Q`, equals a product of three factors.
The first is `ϑ.normQ ^ p.z ^ 2`. The second is the product for `ν⁻¹`, away from the chosen places.
The third is the product of the squares of the ratios `|L(z, (ν ϑ ^ s)⁻¹)| / |L(z, ν⁻¹)|` of the
pairs `p.lowerPoint z = (ν, z)` for `1 ≤ z ≤ p.z`. 
