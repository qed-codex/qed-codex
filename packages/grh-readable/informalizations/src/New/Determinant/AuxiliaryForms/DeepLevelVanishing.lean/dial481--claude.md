---
{
  "module": "src/New/Determinant/AuxiliaryForms/DeepLevelVanishing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/DeepLevelVanishing.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/DeepLevelVanishing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Vanishing of forms on Y₀ orthogonal to the deep level on Ỹ^0_0

A form `y` of level `J_M = D.chosenLevel` on a hermitian space `V` is zero if it is orthogonal to
the restrictions of all forms of the deep level `J(𝔟)` on `V ⊕ ⟨1⟩`, translated by a suitable real
point `ω`. This requires size conditions on the level and a lower bound for the pairing of the
matrix coefficients for the parameter `l` of `V` and the parameter `l'` of `V ⊕ ⟨1⟩`.

Every bound `S` of `‖y‖` is halved. The smoothing of `y` is its convolution with the translated
coefficient for `l'`; the point `ω` with the lower bound for the pairing comes from steepness, in
the proof of `New.Data.exists_eq_zero_of_orthogonal_gridLevelForms`.

1. Decay: `New.Exchange.integral_typeKernelMajorant_le`.
2. The cusp: `New.Exchange.norm_le_half_of_firstMinimum_lt`.
3. A Poincaré series is a form, so its period is zero:
   `New.Exchange.poincare_period_translatedCoeff_eq_zero`.
4. Unfolding shows that the smoothing of `y` is small: `New.Exchange.norm_poincare_period_sub_le`
   and `New.Exchange.norm_realConv_translatedCoeff_le`.
5. Undoing the smoothing: `New.Exchange.norm_le_half_of_le_firstMinimum`.

## Main definitions and results

* `New.Exchange.HasDeepLevelSizes`: the size conditions. The real number `m` in them is at least a
  power of `β` that absorbs all constants in the estimates.
* `New.Exchange.eq_zero_of_petersson_translate_eq_zero`: the criterion at a given real point;
  `New.Exchange.exists_forall_eq_zero_of_petersson_restrict_eq_zero` chooses the point place by
  place.
* `New.Data.exists_eq_zero_of_orthogonal_gridLevelForms`: the forms of level `J(𝔟)` on `Ỹ^0_0`,
  restricted to `U(Y₀)` after translation by one real point, detect every nonzero form of level
  `J_M` on `Y₀`.

Notions from other files:
* `New.typeKernel`: `typeKernel l s` is the product over the infinite places `w` of the formal
  degree times the conjugate matrix coefficient `(l w).dsCoeff` of the parameter `l w`.
* `New.Space.IsForm`: `V.IsForm e F` says that `F` is automorphic, bounded, and fixed by the right
  convolution `New.realConv` with `e` over the real points (if `e` is integrable).
* `New.Space.firstMinimum`: the least norm of a nonzero vector of the lattice of a space, cut off at
  `1`; `V.move x` is the space `V` with its adelic frame multiplied by `x`.
* `New.Data.principalForms`, `New.Data.gridLevelForms`: the forms fixed by `D.chosenLevel`, and the
  forms on `Ỹ^i_0` fixed by the deep level, that is, the principal level of
  `D.gridLevelGen = D.piM ^ D.natB`, where `D.piM * star D.piM = D.M` is `M`.
* `New.Data.spaceY`: the hermitian space `Y_j` with its adelic frame, chosen as in
  `New.Data.exists_space_isStd_of_le_and_gram_eq_of_lt`.
* `(l w).HasLargeGap B`: the entries of `l w = 2λ` are distinct, of the parity of `card n - 1`, and
  entries of `λ` with different signs are at least `500 n³ + B` apart; `dsCoeff` is the matrix
  coefficient of the parameter and `dsKernel` its conjugate times the formal degree.

## Relation to the literature

Nonvanishing periods via Poincaré series of deep level and restriction results of Burger–Sarnak type
are known in the literature. Related work: Prasad–Schulze-Pillot, Generalised form of a conjecture
of Jacquet, 2008; Harris, Testing rationality of coherent cohomology of Shimura varieties, 2014;
Muić, Fourier coefficients of automorphic forms and integrable discrete series, 2015.



## A vanishing criterion through restrictions of deep level forms

The parameter `l` of the forms on `V` has large gaps for `4 A`, and the parameter `l'` of the forms
on `V ⊕ ⟨1⟩` has large gaps for `2 A`, with `8 (card n + 1)² < A`.


### `New.Exchange.norm_prod_conj_dsCoeff_inv_mul_sub_le`

 A Lipschitz bound under left translation for the product over the infinite places `w` of the
conjugate matrix coefficients `(l w).dsCoeff`. The parameters `l w` are integer vectors with entries
bounded by `L` and large gaps: entries of `l w / 2` with different signs differ by at least
`500 n³ + 4 A`. If `β` bounds `2000 (card n + L + 1)⁶` and the number `D.f` of infinite places and
`u` is a real point within `δ` of `1`, the values at `u⁻¹ * z` and `z` differ by at most `β² δ`. 

### `New.Exchange.HasDeepLevelSizes`

 The size conditions of the vanishing criterion for a space of rank `card n` over the field `D.E`
of the data `D`. The exponent `A` dominates the rank, the exponent `N` of a lower bound
`v * β ^ (-N)`, with `v` a volume, for local pairings of matrix coefficients, and the real
dimension; `β` dominates the constants, among them the cusp constant
`cuspConst D.E n D.cyclotomicConductor` and the bound `L` of the parameters; `m` is at least a large
power of `β`; and the generator of the deep level is large against `m` at every infinite place `w`,
with embedding `Φ w`. The radius `m` is a real number, not the number `D.m` of lifts. 

### `New.Exchange.HasDeepLevelSizes.rank_sq_lt`

 `A` is large against the square of the rank. 

### `New.Exchange.HasDeepLevelSizes.exponent_lt`

 `A` exceeds the exponent `N` of the lower bound for the local pairings. 

### `New.Exchange.HasDeepLevelSizes.dim_le`

 `A` exceeds by `2` or more the real dimension of a space of rank `card n + 1` over `E ⊗ ℝ`. 

### `New.Exchange.HasDeepLevelSizes.cuspConst_sq_le`

 `β` bounds the constant of the cusp estimate: `D.M` is the level and `cuspConst` depends on
  the rank and on the number `D.cyclotomicConductor` in the different of `D.E`. 

### `New.Exchange.HasDeepLevelSizes.rank_pow_le`

 `β` bounds a polynomial in the rank and the bound `L` of the parameters. 

### `New.Exchange.HasDeepLevelSizes.places_le`

 `β` bounds the number of infinite places. 

### `New.Exchange.HasDeepLevelSizes.pow_le`

 `m` is at least a large power of `β`. 

### `New.Exchange.HasDeepLevelSizes.pow_le_norm_gridLevelGen`

 The level is deep: its generator is large at every infinite place. 

### `New.Exchange.HasDeepLevelSizes.beta_le_m`

 The size conditions for the deep level force the constant `β` to be at most the radius `m`,
which is at least a power of `β`. 

### `New.Exchange.HasDeepLevelSizes.pow_places_le_div`

 The comparison of constants behind `integral_typeKernelMajorant_le`. Of the size conditions for
the deep level it uses `8 (card n + 1)² < A`, `N < A`, `2000 (card n + L + 1)⁶ ≤ β` and
`β ^ (20 A (D.f + 1)) ≤ m`. The left side is the `D.f`-th power of the bound for the local
integrals; it is small against `m`. 

### `New.Exchange.HasDeepLevelSizes.sq_le_pow_mul_firstMinimum`

 Under the size conditions `HasDeepLevelSizes`, `D.M * κ²` is at most `β ≤ m`. Here
`κ = cuspConst D.E n D.cyclotomicConductor` is the constant of the cusp estimate
`IsForm.norm_le_of_firstMinimum_lt`. So where `V.firstMinimum` is at least the threshold
`(m⁻² / (D.M κ²)) ^ card n` of that estimate, `m² ≤ m ^ (3 card n + 2) * V.firstMinimum`. 

### `New.Exchange.typeKernelMajorant`

 The function `u ↦ ∏_w deg(l w) (2 / ‖u w‖) ^ (2 A)` on the real points, with `deg` the formal
degree. It is a majorant of `‖typeKernel l s‖` that keeps half of its decay when the parameters
`l w` have large gaps for `4 A`. 

### `New.Exchange.integral_typeKernelMajorant_le`

 Let the parameters `l w` have large gaps for `4 A` and entries bounded by `L`. Then
`typeKernelMajorant l A`, the product over the infinite places `w` of the formal degree of `l w`
times `(2 / ‖u w‖) ^ (2 A)`, is integrable over the real points `u`. Under the size conditions for
the deep level, where `β` dominates the constants, `β ^ N` is the loss in the local pairings and
`m` is at least a large power of `β`, its integral is at most
`m / (16 β) / (β ^ N (2 β) ^ (3 A)) ^ D.f`, with `D.f` the number of infinite places. 

### `New.Exchange.norm_typeKernel_inv_mul_sub_le`

 The kernel `typeKernel l s` varies slowly. Let the parameters `l w` have large gaps for `4 A`
and entries bounded by `L`, and assume the size conditions `HasDeepLevelSizes D n A L N β m`: `β`
dominates the constants and `m` is at least a large power of `β`. For a real point `u` within
`m⁻¹ ^ 2` of `1`, the values of the kernel at `u⁻¹ * z` and `z` differ by at most `β / m` times the
sum of the values at these points of `typeKernelMajorant l A`, the function
`u ↦ ∏ w, deg(l w) (2 / ‖u w‖) ^ (2 A)` with `deg` the formal degree. 

### `New.Exchange.norm_le_half_of_firstMinimum_lt`

 High in a cusp a form is at most half of its bound. Assume the size conditions
`HasDeepLevelSizes D n A L N β m`, and let the parameters `l w` have large gaps for `4 A` and
entries bounded by `L`. Let `y` be a form on `V` of type `l`, right invariant under the principal
congruence subgroup of level `D.M` (`HasLevel`) and bounded by `S`. Where the first minimum of the
lattice of `V.move x` is below the threshold of the cusp estimate, whose constant is
`cuspConst D.E n D.cyclotomicConductor`, we have `‖y x‖ ≤ S / 2`. 

### `New.Exchange.poincare_period_translatedCoeff_eq_zero`

 Let `y` be a function on the group of `V` whose Petersson product with `x ↦ φ ((x ⊕ 1) ω)` is
zero for all forms `φ` on `Z = V ⊕ ⟨1⟩` of type `l'` and level `K`, where the parameters `l' w` have
large gaps for `2 A` and `8 (card n + 1)² < A`. Fix a real point `α` and put `c g = ∏ w, conj ((l'
w).dsCoeff ((α w)⁻¹ * g w * ω w))`, the translated coefficient for `l'`. Then the Poincaré series
over the rational points `γ` of `Z` of `c` times the indicator of `K` at the finite part
(`poincareKernel`), centred at `x ⊕ 1`, has zero period against `y` over the quotient of the group
of `V` by its rational points (`quotMeasure`). 

### `New.Exchange.norm_realConv_translatedCoeff_le`

 Assume the size conditions `HasDeepLevelSizes D n A L N β m` and large gaps for `2 A` of the
parameters `l' w`. Let `y` be automorphic on `V`, of the deep level
`principalLevel n D.gridLevelGen`, and bounded by `S`. Let it also be orthogonal to
`x ↦ φ ((x ⊕ 1) ω)` for all forms `φ` on `V ⊕ ⟨1⟩` of type `l'` and deep level. For a real point
`α`, the translated coefficient `translatedCoeff l' α ω g` is
`∏ w, conj ((l' w).dsCoeff ((α w)⁻¹ * g w * ω w))`. Where
`m² ≤ m ^ (3 card n + 2) * (V.move x).firstMinimum`, its restriction along the block embedding
`inl s 1` is integrable. The convolution of this restriction with `y` at `x` is then at most
`10 S / m` times `sliceConst A α ω = ∏ w, (2 (‖α w‖ ‖ω w‖)²) ^ A * 16 ^ A * v`, with `v` the volume
of the unit ball around `1` in `U(s)`. 

### `New.Exchange.norm_dsKernel_mul_pow_le`

 Let the parameter `l` have large gaps for `4 * A` (`HasLargeGap`), let `16 ≤ β` and
`‖ω‖ ^ 2 ≤ β`. Then the norm of the kernel `dsKernel l r`, times
`(2 (‖inl s 1 r * ω‖ ‖ω‖)²) ^ A * 16 ^ A`, is at most
`l.formalDegree * (2 / ‖r‖) ^ (2 A) * (2 β) ^ (3 A)`. Here `inl s 1 r = diag(r, 1)`. 

### `New.Exchange.integral_translatedCoeff_mul_eq_prod`

 Let the parameters `l w` have large gaps for `4 A`, so that their formal degrees are positive,
and let `ω` be a real point, with a component `ω w` in `U(s ⊕ᵥ 1)` at each infinite place `w`. Pair
the conjugate of the kernel `typeKernel l s`, divided by the value of the kernel at `1`, with the
restriction along `inl s 1 : r ↦ r ⊕ 1` of
`translatedCoeff l' ω ω g = ∏ w, conj ((l' w).dsCoeff ((ω w)⁻¹ * g w * ω w))`. This integral over
the real points is the product over `w` of the local pairings of the matrix coefficients. 

### `New.Exchange.realConv_translatedCoeff_mul`

 Right translation of the point by the real point `u` moves `u ⊕ 1` into the left argument of
the translated coefficient. 

### `New.Exchange.norm_le_half_of_le_firstMinimum`

 Let `y` be a form on `V` of type `l` and of the deep level `D.gridLevelGen`, bounded by `S` and
orthogonal to `x ↦ φ ((x ⊕ 1) ω)` for all forms `φ` on `V ⊕ ⟨1⟩` of type `l'` and deep level. Assume
the size conditions for the deep level, large gaps of the parameters, bounded entries of `l`, that
`ω` is not large (`hω`) and that the local pairings of the coefficients for `l` and `l'` are bounded
from below (`h_pair`). Where the first minimum of `V.move x` is at least the threshold of the cusp
estimate, whose constant `cuspConst D.E n D.cyclotomicConductor` depends on the rank and on a number
in the different of `D.E`, we have `‖y x‖ ≤ S / 2`. 

### `New.Exchange.eq_zero_of_petersson_translate_eq_zero`

 The vanishing criterion at a real point `ω` of `GInf D.E (s ⊕ᵥ 1)`. Assume the following. First,
the size conditions `HasDeepLevelSizes D n A L N β m`. Second, large gaps of the parameters: entries
of `l w / 2` with different signs differ by at least `500 n³ + 4 A`, and likewise for `l'` with
`n + 1` and `2 A`. Third, entries of `l` bounded by `L`. Fourth, `ω` is not large (`hω`). Fifth, at
each infinite place the coefficient for `l` pairs nontrivially with the restriction of the
coefficient for `l'` conjugated by `ω`, with the explicit lower bound `h_pair`. Then a form `y` on
`V` of type `l` and level `D.chosenLevel` vanishes if it is orthogonal to `x ↦ φ ((x ⊕ 1) ω)` for
every form `φ` on `V ⊕ ⟨1⟩` of type `l'` and of the deep level
`principalLevel (n ⊕ Unit) D.gridLevelGen`. 

### `New.Exchange.exists_forall_eq_zero_of_petersson_restrict_eq_zero`

 Let `l` be the parameters of the forms on `V` and `l'` those of the forms on `V ⊕ ⟨1⟩`, whose
signs `t` are `s ⊕ᵥ 1`. Assume large gaps for `4 A` of `l w` and for `2 A` of `l' w`, `|l w i| ≤ L`,
the size conditions of `HasDeepLevelSizes`, and that at each infinite place some point `ω` with
`‖ω‖ ^ 2 ≤ β` makes the pairing for `l` and `l'` not small (`h_place`). Then there is a real point
`g` such that a form `y` on `V` of type `l` and level `D.chosenLevel` vanishes if it is orthogonal
to `x ↦ φ ((x ⊕ 1) g)` for all forms `φ` on `V ⊕ ⟨1⟩` of type `l'` and of the deep level
`D.gridLevelGen`. 

 ## Forms of level `J_M` on Y₀ 

### `New.Data.norm_gridLevelGen`

 At every infinite place the generator `D.gridLevelGen = D.piM ^ D.natB` of the deep level
has modulus `√D.M ^ D.natB`. 

### `New.Data.exists_eq_zero_of_orthogonal_gridLevelForms`

 There is a real point `g` of `GInf D.E (D.gridSigns true 0 0 0)`, the archimedean unitary group
on the index type `D.Y 0 ⊕ Unit`, the index type of `Ỹ^0_0 = Y₀ ⊕ ⟨1⟩`, with the following property.
Let `y` lie in `D.principalForms`, so it is a form on `Y₀ = D.spaceY 0` of type `D.paramW` and level
`J_M = D.chosenLevel`. Then `y` vanishes if it is Petersson orthogonal to `x ↦ φ ((x ⊕ 1) g)` for
all `φ` in `D.gridLevelForms 0`, the forms on `Ỹ^0_0` of type `D.gridKernel true 0 0 true` and of
the principal level of `D.gridLevelGen`. 
