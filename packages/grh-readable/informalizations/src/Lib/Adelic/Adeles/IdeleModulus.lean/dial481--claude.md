---
{
  "module": "src/Lib/Adelic/Adeles/IdeleModulus.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/IdeleModulus.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/IdeleModulus.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The module of an idele, Haar measure scaling and the norm map on finite adeles

This file studies the module of an idele of a number field `E`, its relation to Haar measure, and
its behaviour under norms. Here `New.𝔸 E` has one copy of `ℂ` for each infinite place. The module
`New.ideleAbs` is therefore the product of the squared norms at the infinite places and of the norms
at the finite places. The generalised index `New.genIndex a` of a finite idele, defined through the
scaling of Haar measure, is the inverse of its module; it is `[Ô : a Ô]` when `a` is integral. For
an extension `L / K` of number fields, the algebra norm `New.adeleNorm` on finite adeles preserves
the module.

## Main definitions and results

* `New.ideleAbs`: the module is multiplicative, and it is a continuous positive character
  (`New.continuous_ideleAbs`, `New.ideleAbs_pos`).
* `New.ideleAbs_toAdele`: the product formula for the diagonal embedding `New.toAdele`, for a
  totally complex `E`.
* `New.finIdeleAbs`: the module `∏ ‖x_w‖` of a finite idele; `New.finIdeleAbs_principalIdele` is the
  finite part of the product formula.
* `New.genIndex_eq_inv_finIdeleAbs`, `New.genIndex_eq_inv_norm`: for a finite idele, or an element
  of `E_wˣ`, the index `New.genIndex` is the inverse of its module.
* `New.map_mulVec_haar_finAdele`, `New.volume_map_mulVec_adele`, `New.volume_map_mul_mul_adele`:
  pushing Haar measure forward along `x ↦ a x` or `x ↦ a x b` divides it by the module of the
  determinant of that map.
* `New.finIdeleAbs_adeleNorm`: the norm keeps the module `New.finIdeleAbs` of a finite idele.

Notions from other files:
* `New.𝔸f E`, `New.Ô E`: the finite adeles of `E`, and the subring of those that are integral at
  every finite place.
* `New.FinPlace E`, `New.LocField w`: the finite places of `E` and the completion `E_w`; `w.q` is
  the order of the residue field at `w`, and `w.below K` is the place of a subfield `K` below `w`.
* `New.locIdele w x`: the finite idele with component `x` at `w` and `1` elsewhere.
* `New.idelesUnitOff S`: the finite ideles that are units at all places outside `S`.
* `New.genIndex a`: the inverse of the factor by which multiplication by a unit `a` scales Haar
  measure, and `0` for a non-unit.

## Relation to the literature

Known result: the module of an idele, the product formula and the scaling of Haar measure.

Part of a known result: functoriality of ideles under the norm map, restricted here to the module
and to supports.



## The module of an idele and the product formula

* `New.ideleAbs_star`, `New.ideleAbs_eq_one_of_mem_unitary`: for a CM field, the module is invariant
  under conjugation, and unitary ideles have module `1`.


### `ideleAbs`

 The module `|x|` of an element of `(𝔸 E)ˣ`, as a homomorphism to `ℝ`: the product of the
squared norms of the components at the infinite places (each a copy of `ℂ`) and of the norms at the
finite places. For a totally complex `E` this is the idelic module. 

### `ideleAbs_eq_prod_of_v_eq_one`

 If the idele `x` has valuation `1` at every finite place, then its module is the product of the
squared norms of its components at the infinite places. 

### `ideleAbs_finIdeleIncl_eq_one`

 A finite idele that is a unit at every finite place has module `1`. 

### `continuous_ideleAbs`

 The module `ideleAbs` is continuous on the idele group of `E`. 

### `finprod_norm_algebraMap_apply`

 For `x : E`, the product of the norms of the components of the principal finite adele `x` is the
product of `w x` over Mathlib's finite places `w` of `E`. 

### `ideleAbs_toAdele`

 The product formula: for a totally complex `E`, the principal idele of an element of `Eˣ` (its
image under the diagonal embedding `toAdele`) has module `1`. The class `PlaceEmbedding E` chooses
a complex embedding for each infinite place. 

### `ideleAbs_star`

 For a CM field `E`, the module of an idele `x` is invariant under complex conjugation. 

### `ideleAbs_eq_one_of_mem_unitary`

 For a CM field `E`, a unitary idele `x` (one with `star x * x = 1`) has module `1`. 


## Scaling of Haar measure by the module

The index `New.genIndex` is first compared with the module. Both are multiplicative, so at a single
place `w` it is enough, by `New.eq_norm_inv_of_uniformizer`, to treat uniformisers, whose index is
the order `w.q` of the residue field.

Conventions: `v` is the multiplicative valuation, `exp (-1)` on uniformisers.


 ### Valuations and absolute values at a finite place 

### `v_uniformizer_inv_mul_le_one_iff`

 An element `y` of `E_w` has valuation less than `1` if and only if its quotient by the chosen
uniformiser is integral. 

### `norm_locField_eq_q_zpow`

 The norm of a nonzero `x` in `E_w` is `w.q ^ k`, where `w.q` is the order of the residue field
and `v x = exp k`. 

### `eq_norm_inv_of_uniformizer`

 A homomorphism `χ : E_wˣ → ℝ` that takes the value `w.q`, the order of the residue field, on
every uniformiser is the inverse of the normalised absolute value. 

### `isValuationPair_Ô`

 For finite adeles `a`, `b` there is an idempotent `e` of `Ô`, the ring of integral finite
adeles, such that both lie in the `Ô`-module generated by the patch `a - e * (a - b)`
(`New.IsValuationPair`). 

 ### The module of a finite idele 

### `finIdeleAbs`

 The module `|x|` of a finite idele `x`: the module `New.ideleAbs` of the idele with finite part
`x` and component `1` at the infinite places. 

### `finIdeleAbs_principalIdele`

 The product formula, finite part: for `x` in `Eˣ`, with `principalIdele x` its diagonal image in
`(𝔸f E)ˣ`, the product of the normalised absolute values `|x|_w` over the finite places is
`|N_{E/ℚ}(x)|⁻¹`. 

 ### The generalised index as the inverse of the module 

### `reduceAt_surjective`

 Reduction modulo `w` maps the integral finite adeles onto the residue field at `w`. 

### `genIndex_locIdele_of_v_eq_exp_neg_one`

 For a uniformiser `x` at `w`, let `a` be the finite idele with component `x` at `w` and `1`
elsewhere. Its generalised index `[Ô : a Ô]` is the order `w.q` of the residue field. 

### `genIndex_eq_inv_finIdeleAbs`

 The generalised index `genIndex` of a finite idele, the inverse of the factor by which it scales
Haar measure, is the inverse of its module. 

### `genIndex_eq_inv_norm`

 The generalised index `genIndex` of an element of `E_wˣ`, the inverse of the factor by which it
scales Haar measure on `E_w`, is the inverse of its absolute value. 

 ### Linear maps and Haar measure 

### `map_mulVec_haar_finAdele`

 For a finite index type `n` and `a` in `GL_n` of the finite adeles, `x ↦ a x` pushes a Haar
measure `μ` on vectors forward to `μ` divided by the module `New.finIdeleAbs` of the finite idele
`det a`. 

### `volume_map_mulVec_adele`

 For `a` in `GL_n` of the adeles `𝔸 E`, with `n` a finite index type, the map `x ↦ a x` pushes
the Haar measure `volume` on adelic `n`-vectors forward to itself divided by the module
`New.ideleAbs` (the adelic absolute value) of `det a`. 

### `det_star`

 The determinant of the conjugate transpose of a matrix in GL_n of the adeles is the conjugate of
its determinant. 

### `volume_map_mul_mul_adele`

 For a finite index type n, a in GL_n(𝔸) and b in GL_1(𝔸), the map x ↦ axb on n×1 adelic matrices
pushes the standard measure forward to |det(b)^n det a|⁻¹ times itself, with |·| the module of an
idele. 


## The generalised index of a field element

* `New.genIndex_natCast`: for a natural number `k` and a CM field `E` it is `(k ^ r) ^ 2`, with
  `r` the number of infinite places of `E`.


### `New.genIndex_algebraMap`

 For a number field `E`, the generalised index `New.genIndex` of `x : E`, as a finite adele, is
the absolute value of the norm of `x` to `ℚ`. 

### `New.genIndex_natCast`

 For a natural number `k` the generalised index `New.genIndex` of `k` as a finite adele is
`(k ^ r) ^ 2`, with `r = Core.numInfPlaces E` the number of infinite places of the CM field `E`. The
reason is that the norm of `k` is `k ^ [E : ℚ]` and `[E : ℚ] = 2r`. 


## The norm map on finite adeles

For an extension `L / K` of number fields the finite adeles of `L` are a finite free module over
those of `K` (`New.adeleBasis`), so they have an algebra norm `New.adeleNorm`. It is continuous and
extends the field norm, so identities can be checked on the dense field.


### `adeleNorm`

 For an extension L/K of number fields, the algebra norm from the finite adeles of L to the
finite adeles of K, as a multiplicative map. 

### `continuous_adeleNorm`

 The norm map from the finite adeles of `L` to those of `K` is continuous. 

### `adeleNorm_algebraMap`

 The norm of an element `x` of `L`, regarded as a finite adele, is the field norm of `x`. 

### `adeleNorm_finAdeleIncl`

 For `a` a finite adele of `K`, the norm to `K` of its image in the adeles of `L` is
`a ^ [L : K]`. 

### `finAdeleIncl_adeleNorm`

 For Galois `L / K`, the norm of a finite adele `y` of `L`, included back in the adeles of `L`,
is the product of the images of `y` under the Galois group. 

### `localNorm`

 For an extension L/K, a finite place w of L and v = `FinPlace.below K w` the place of K below w,
the local norm L_w^× → K_v^×: the v-component of the adelic norm of the idele supported at w. 

### `adeleNorm_locIdele`

 For number fields L/K, a finite place w of L and y in L_w^×, the norm to K of the finite idele
`locIdele w y` (y at w and 1 elsewhere) has component `localNorm K w y` at the place below w and 1
at every other place. 

### `v_adeleNorm_eq_one`

 If every component of the finite idele `y` of `L` is a unit of the local integers, that is, `y`
is in `idelesUnitOff ∅`, then every component of its norm to `K` has valuation `1`. 

### `adeleNorm_star`

 For an extension `L / K` of CM fields, the norm `adeleNorm K L` of finite adeles commutes with
complex conjugation, written `star`. 

### `units_map_adeleNorm_star`

 For CM fields the norm of finite ideles commutes with conjugation. 


## Preservation of the module by the norm, and local norms

* `New.norm_localNorm`, `New.v_localNorm`: for an idele with one component `y` at `w`
  (`New.locIdele`), the norm at the place below has absolute value `‖y‖` and valuation `v y ^ f`,
  where `f` is the residue degree.

The local statements follow from the global one, which rests on the product formula and the
finiteness of the class group.


### `finIdeleAbs_adeleNorm`

 The norm from `L` to `K` keeps the module `New.finIdeleAbs`, the product of the normalised
absolute values of the components, of a finite idele. 

### `norm_localNorm`

 The local norm from `L_w` to the completion of `K` at the place below `w` keeps the normalised
absolute value. 

### `v_localNorm`

 Let `f` be the residue degree of `w` over `K`, that is, the residue field orders satisfy
`(w.below K).q ^ f = w.q`. The norm of the idele that is `y` at `w` and `1` elsewhere has
valuation `v y ^ f` at the place below `w` (valuations are written multiplicatively). 
