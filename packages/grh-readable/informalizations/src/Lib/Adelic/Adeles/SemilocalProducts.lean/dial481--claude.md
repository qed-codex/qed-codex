---
{
  "module": "src/Lib/Adelic/Adeles/SemilocalProducts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/SemilocalProducts.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/SemilocalProducts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Products of completions at finite sets of places and approximation of adeles by elements of E

Let `S` be a finite set of finite places of the number field `E`. The ring `New.LocProd S` is the
product of the completions `E_w` for `w ∈ S`, and `O` is the product of their rings of integers. The
file relates `New.LocProd S` to the finite adeles through the projection `New.evalPlaces S` and the
extension by zero `New.adeleOfLocal S`. It computes the projection of Haar measure and the
generalized index of an element of `New.LocProd S`, and it bounds the zeta function of `O`. For a CM
field `E` and `S` stable under conjugation it defines the involution of `New.LocProd S`.

## Main definitions and results

* `New.exists_principal_near_of_mem_differentIdeal`: approximation of an adele by an element of `E`.
* `New.integralOff`, `New.locProd_O_eq_map_evalPlaces`, `New.map_evalPlaces_restrict_volume`: the
  adeles integral off `S`, and the effect of the projection `New.evalPlaces S` on the integral
  adeles `New.Ô E` and on Haar measure.
* `New.idealZeta_locProd_le`, `New.genIndex_eq_inv_prod_norm`, `New.sqrt_genIndex_le_prod_norm`: the
  zeta function of `O` and the generalized index.

Notions from other files:
* `𝔸f E`, `New.Ô E`: the finite adeles of `E` and the subring of those integral at every place.
* `New.LocField w`, `New.LocInt w`: the completion `E_w` at the finite place `w` and its integers.
* `New.genIndex a`: the inverse of the factor by which the unit `a` scales Haar measure, and `0` if
  `a` is not a unit.
* `Φ w`: the chosen complex embedding of `E` at the infinite place `w`, given by
  `New.PlaceEmbedding E`, which is part of `New.CMType E`.
* `New.HasPrimitiveRoot5040 E`: the CM field `E` contains a primitive `5040`-th root of unity.

## Relation to the literature

Known; see `Lib.Adelic.Adeles.Basic` for sources.



## Effective approximation of adeles by elements of E

`New.exists_principal_near_of_mem_differentIdeal`: every adele of the CM field `E` differs from an
element of `E` by an adele that is integral at the finite places and of explicitly bounded size at
the infinite ones. The bound comes from the covering radius of the dual of the lattice `𝓞 E`.


### `New.exists_principal_near_of_mem_differentIdeal`

 Let `d ≠ 0` lie in the different of the CM field `E`, and let `f = Core.numInfPlaces E` be the
number of infinite places. For every adele `(z, y)` there is `a` in `E` such that `y - a` lies
in the ring `Ô E` of integral finite adeles and `‖z w - Φ w a‖ ≤ (2 * f) ^ 2 * ‖Φ w d‖` at all
infinite places `w`, where `Φ w` is the chosen complex embedding at `w`. 


## Projection to finitely many places and extension by zero

For a finite set `P` of finite places, `New.evalPlaces P` sends a finite adele to its components in
the product `New.LocProd P` of the completions at `P`, and `New.adeleOfLocal P` extends such
components by zero. Both are continuous, `evalPlaces P ∘ adeleOfLocal P` is the identity
(`New.evalPlaces_adeleOfLocal`), and `adeleOfLocal P ∘ evalPlaces P` is multiplication by the
idempotent `New.idem P` (`New.adeleOfLocal_evalPlaces`).


### `evalPlaces`

 The ring homomorphism sending a finite adele to its components at the places of the finite
set `P`. 

### `adeleOfLocal`

 Extension by zero: the additive and multiplicative map from the product of the completions
`E_w`, `w ∈ P`, to the finite adeles, with component `0` outside `P`. 

### `adeleOfLocal_evalPlaces`

 Projecting to the places in `P` and extending by zero is multiplication by `idem P`, the adele
with component `1` on `P` and `0` elsewhere. 


## Measure, zeta function and generalized index of the product of completions

Here `O` is the subring `New.SemilocalField.O` of `New.LocProd S`, the product of the rings of
integers; it is compact, open and of volume one. The units of `New.LocProd S` embed openly into
`New.LocProd S` (`IsOpenUnits`). For `S` stable under conjugation, `New.LocProd S` has a continuous
involution, and `O` satisfies `New.IsAdelic` under `New.HasPrimitiveRoot5040 E`: it is open,
compact, stable under `star` and a valuation pair, and it contains a skew unit and an element of
norm `-1`.


### `integralOff`

 The ring of finite adeles of `E` that are integral at every place outside `S`. 

### `ratToPlaces`

 The diagonal ring homomorphism from `E` to the product of the completions `E_w`, `w ∈ S`. 

### `Filling.ratIntegralOff`

 The ring of `S`-integers of `E`: the elements integral at every finite place outside `S`. 

### `mem_integralOff`

 A finite adele lies in `integralOff S` if and only if its components at the places outside `S`
have valuation at most `1`. 

### `adeleOfLocal_evalPlaces_mul`

 Extension by zero is linear over the finite adeles, which act on `LocProd S` through the
projection `evalPlaces S`. 

### `mem_Ô_iff`

 A finite adele is integral at all places if and only if its projection to the places in `S` lies
in the ring of integers `O` of `LocProd S` and it is integral outside `S`. 

### `locProd_O_eq_map_evalPlaces`

 The ring of integers `O` of `LocProd S` is the projection of the ring `Ô E` of integral finite
adeles. 

### `sub_adeleOfLocal_mem_iff`

 A finite adele with its components in `S` removed is integral at all places if and only if the
adele is integral outside `S`. 

 ### Zeta function and measure 

### `idealZeta_locProd_le`

 For a number field `E` and a finite set `S` of finite places of `E`, `LocProd S` is the product
of the completions `E_w` over the places `w` in `S`. The ideal zeta sum `∑ [R : I]⁻¹ ^ μ` (valued in
`[0, ∞]`) over the ideals `I` of finite index is at most as large for the ring of integers `R = O`
of `LocProd S` as for the integral finite adeles `R = Ô E`. 

### `map_evalPlaces_restrict_volume`

 The projection carries Haar measure on the adeles that are integral off `S` to `New.volÔ E`, the
mass of `New.Ô E`, times the Haar measure of `New.LocProd S` that gives `O` mass one. 

### `denomIndex_ne_zero`

 In the ring of integers `O` of `LocProd S`, the `r` with `a * r ∈ O` form a subgroup of finite
index: its index `denomIndex O a` is nonzero (an infinite index is `0`). 

### `volume_setOf_le_sqrt_inv_norm_sub_one_le`

 Let `a` in the completion at `w` have norm greater than `1`, and let `0 < t`. The level set of
the `x` with `√(‖x‖⁻¹ - 1) ≥ t`, that is with `0 < ‖x‖ ≤ (1 + t ^ 2)⁻¹`, has volume at most
`(1 + t ^ 2)⁻¹ * ‖a‖`. 

### `locallyIntegrable_one_add_sqrt_inv_norm_sub_one`

 The function `1 + √(‖x‖⁻¹ - 1)` is locally integrable on the completion at `w`; note that `√`
vanishes on negative numbers, so the root is zero for `‖x‖ ≥ 1`. 

 ### The generalized index and the product formula 

### `genIndex_eq_inv_prod_norm`

 The generalized index `genIndex x` of `x` in the product of the completions at `S` (the inverse
of the factor by which `x` scales Haar measure) is the inverse of the product of the local norms of
`x`. Both sides are `0` if a component of `x` is zero. 

### `sqrt_genIndex_le_prod_norm`

 Let `y ≠ 0` be an `S`-integer of the totally complex field `E`. By the product formula, the
square root of its generalized index in `LocProd S` is at most `∏ v, ‖Φ v y‖`, the product over
the infinite places. 

 ### The involution 

### `_root_.Finset.StarStable`

 The finite set `S` of finite places of `E` is stable under complex conjugation. 

### `instance : StarRing (LocProd S)`

 The involution of `LocProd S`: the component of `star x` at `w` is the conjugate of the
component of `x` at `star w`. 

### `adeleOfLocal_star`

 For `S` stable under complex conjugation, extension by zero commutes with conjugation. 
