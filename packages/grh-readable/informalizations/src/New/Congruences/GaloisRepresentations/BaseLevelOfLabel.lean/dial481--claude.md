---
{
  "module": "src/New/Congruences/GaloisRepresentations/BaseLevelOfLabel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/BaseLevelOfLabel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/BaseLevelOfLabel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Base data whose forms contain those with given labels in a lift setting

Let `O` be a descent pair (`New.DescentPair`): hermitian spaces `W` and `V` with bases `r` and `n`,
with chosen places, twist places, weights and a character. Let `c` be a tuple of labels
(polynomials over the residue fields) at the chosen places, forming a lift setting with a twist `ϑ`
(`New.Selmer.IsLiftSetting`); `typeProjection O c` is the idempotent on forms that cuts out the
labels `c`.

* `New.Selmer.IsFormOfType`, `New.Selmer.IsFormOfType.isRepOfType_normalisedRep`: the eigenforms
  of type `c` with the level and character of `O` off a set of places, and their normalised
  representations as representations of a type.
* `New.Selmer.exists_baseLevel`: base data (`New.Patching.BaseLevel`) whose forms contain the image
  of the idempotent and whose eigensystems have normalised representations that are representations
  of a type with a quadratic relation on inertia, when the modulus of `ϑ` is auxiliary; also,
  `New.Data.chosenGroupOrder` times the idempotent keeps integral forms.
* `New.Selmer.normalisedJumps_eq_range_add_map`: the Hodge–Tate jumps of the normalised
  representations are, when the rank of the larger space is even, `0, …, t - 1` and the
  `(t - 1) / 2 ∓ (λ_c + κ')`, where `t` is the difference of the ranks, `λ` the parameter on the
  smaller space and `-κ'` the weight of the character.

Notions from other files:
* `New.levelSpace`: the vectors `v` of a representation `π` with `π k v = χ k • v` for all `k` in
  the subgroup `K`.
* `New.Gf.componentOn`: keeps the components of an element at the places of `S` and their
  conjugates, and replaces the others by 1.
* `New.DescentPair.columnCount`: the weight datum `(τ, i) ↦ k⁺(τ, i) + k⁻(τ, n − i)` of forms on the
  definite space of rank `n`, with `k⁺`, `k⁻` the two weights of the pair.
* `New.DescentPair.FormV`: the algebraic forms on the definite space of rank `n` with the weight
  `(O.columnCount, O.detExp)`, the level group and the level character `O.levelChar` of the pair
  `O`.
* `New.DescentPair.chosenGLRep`: the action of `∏ GL_r(k_w)`, over the chosen places `w`, on the
  vectors of `π` with the level and character of `O`, twisted by `∏ ψ_w (det g_w)`, where `ψ_w` is
  the character `O.tamePart w` of the residue field `k_w`.
* `New.levelOf`, `New.descentResidueLevel`, `New.DescentPair.levelChar`: the level of `O` is the
  group of integral elements whose reductions at its places lie in `descentResidueLevel`;
  `levelChar` is its character.
* `New.Data.chosenGroupOrder`: the order of a product of groups `GL` over the residue fields of the
  chosen places of `D`; `New.Patching.BaseLevel.ellIntegralForms`: the forms whose values at the
  points integral above `ℓ` are sent to `ℓ`-adic integers by `ιℓ : ℂ ≃ ℚ̄_ℓ`.
* `New.HasProductLabel`: a label of a form at a place, made from a polynomial and characters of
  blocks of given sizes; `New.faithfulChar`: the faithful character by which it is formed.
* `New.Selmer.IsRepOfType`: a conjugate self-dual representation of given jumps and level on which
  inertia at the chosen places acts through the roots of the labels; `New.Selmer.normalisedRep`: the
  twist of a representation by `normalizingAvatar O`; `ϑ.invAvatar`: the `ℓ`-adic avatar of `ϑ⁻¹`
  over `D.E`.


### `hasParahoricType_chosenGLRep`

 Let `w = O.chosenPlace i` be a chosen place of the pair `O`, assumed split (`hw`), and write
`ψ_w` for the character `O.tamePart w` of its residue field `k_w`. The map `ofSplitPlace hw` places
`GL_n(E_w)` in the finite adelic group. Let `π` be a representation of that group on a space `S` of
functions, and `u` a vector of the level and character of `O`. Suppose that `π k u` is the right
translate of `f` by `k` for all `k` in `GL_n(E_w)`. Then `f` has a parahoric type at `w`: an
integral `k` whose reduction keeps the span of the indices `O.incl` and acts on it by `g` sends `f`
to `ψ_w⁻¹(det g)` times the image of `u` under `g`, placed at `i`, in the representation
`O.chosenGLRep π`; the one other block (`s := 1`) carries the trivial character. 

### `coe_asAlgebraHom_chosenGLRep_apply`

 Let `v` have the level and character of the pair `O` under `π`, and let
`ψ_i = O.tamePart (O.chosenPlace i)`, a character of the residue field of the `i`-th chosen place.
The element `a` of the group algebra of `O.ChosenGL r = ∏ i, GL_r` of these residue fields acts on
`v` through `O.chosenGLRep π` as the sum over `g` of `a g` times `∏ i, ψ_i (det (g i))` times `π`
of the chosen lift of `diag (g, 1)`. 

### `componentOn_places_eq_self`

 An element of the finite adelic group that is supported at the places of `O` and their
conjugates equals its components there (`componentOn`). 

### `toSmoothForm_mem_levelSpace_componentOn`

 Let `π` be right translation (`formTranslation`) of forms of weight `(O.columnCount, O.detExp)`
by the components at the places of `O` and their conjugates (`componentOn`, which puts `1` at all
other places). A form `y` of `O` (`O.FormV`: a form of this weight with the level group and
character of `O`), regarded as a form of that weight (`y.toSmoothForm`), has this level and
character also under `π`. The reason is that taking components does not change the reductions at
the places of `O`, on which alone the level group and its character depend. 

### `toSmoothForm_typeProjection`

 Let `ψ_i = O.tamePart (O.chosenPlace i)`, a character of the residue field of the `i`-th chosen
place. For a form `y` of `O`, the projection `typeProjection O c y` is the sum over `g` of the
coefficient at `g` of the idempotent `tupleIdem r c` of the labels `c`, times
`∏ i, ψ_i (det (g i))`, times the right translate of `y` by the components at the places of `O` of
the chosen lift of `diag (g, 1)`. 

### `chosenGroupOrder_nsmul_typeProjection_mem_ellIntegralForms`

 Let the labels `c` at the chosen places of `O` form a lift setting with the twist `ϑ`. Let the
form `y` of `O` be integral above `ℓ`: `ιℓ` sends its values at the points integral above `ℓ` to
`ℓ`-adic integers. Then so is `D.chosenGroupOrder` times the projection `typeProjection O c y` of
`y` by the idempotent of `c`. 

### `notMem_and_star_notMem_range_union_places`

 Let the labels `c` form a lift setting for `O` and `ϑ`. Let `ϑ.Q` be auxiliary: its places have
prime norm, neither they nor their conjugates are bad, and the conjugates are not in `ϑ.Q`. Let `U`
be a family of places that are not bad. Suppose that neither `v` nor its conjugate is a chosen
place. Suppose also that `v` lies above `ℓ` or in `placesAboveM D`, or that neither `v` nor its
conjugate is in `ϑ.Q` or `range U`. Then `v` and its conjugate avoid `range U` and the places of
`O`. 

### `normalisedJumps`

 The jumps of a normalised representation (`normalisedRep`) attached to a form of weight
`(O.columnCount, O.detExp)`: the jumps of the weight minus the infinity type of the algebraic Hecke
character whose `ℓ`-adic avatar is `normalizingAvatar O`. 

### `isRepOfType_normalisedRep`

 Let the labels `c` form a lift setting for `O` and `ϑ`, and let `R` be attached to an eigenform
`f` of weight `(O.columnCount, O.detExp)`. Suppose that at the chosen places `f` has the labels
`scaledTypePoly O c i`, completed by the trivial character on further blocks of sizes `t`
(`HasProductLabel`). Suppose also that `f` is spherical at the places that are off `S`, above `ℓ` or
in `placesAboveM D` (above `p₀` or `p₁`), except the chosen places and their conjugates.

Then `normalisedRep O R`, the twist of `R` by `normalizingAvatar O`, satisfies `IsRepOfType`: it has
the jumps `normalisedJumps O` and the properties of a conjugate self-dual representation of level
`S`, and inertia at the chosen places acts through the roots of
`scaledTypePoly O c i * (X - 1) ^ t'`, with `t' = O.rankDiff = card n - card r`. 

### `normalisedJumps_eq_map_hcParameter`

 The pair `O` has hermitian spaces `W` and `V` with bases indexed by `r` and `n`.
`normalisedJumps O` are the jumps of the weight `(O.columnCount, O.detExp)` of forms on `V`, shifted
by minus the infinity type of the algebraic Hecke character whose `ℓ`-adic avatar is
`normalizingAvatar O`. They are computed here from the parameter of that weight. Let `a p` be entry
`p` of twice its Harish-Chandra parameter at the place of the complex embedding `σ` (`hcParameter`).
Let `r₋ = Exchange.negCount O.signs` be the number of minus signs among the signs `O.signs` of the
hermitian form of `W`. Let `t = O.rankDiff = card n - card r`. The jumps at `σ` are the
`(t - 1 ∓ (a p - 2 r₋ + card r)) / 2` for `p < card n`. The upper sign is taken when `σ` is on the
CM type (`cmSign σ = 1`), and the lower sign otherwise; the division is exact. 

### `normalisedJumps_eq_range_add_map`

 The Hodge–Tate jumps `normalisedJumps O` of the normalised representations, written out. The
pair `O` has hermitian spaces `W` and `V` with bases indexed by `r` and `n`; suppose that `card n`,
the rank of `V`, is even. Let `l = 2 λ` be the doubled parameter on `W` that fits `O`
(`DescentPair.FitsParams`), let `-κ'` be the weight `O.weight` of the character of `O`, and let
`t = O.rankDiff = card n - card r`. At a complex embedding `σ` with place `v` the jumps are
`0, 1, …, t - 1` and the `(t - 1) / 2 ∓ (λ v c + κ' v)` over the indices `c : r`, with the upper
sign on the CM type (`cmSign σ = 1`); the division in the statement is exact. 

### `apply_ofSplitPlace_eq_formTranslation`

 If `π` agrees with the translation of forms on the elements supported at the places of `O`, then
it does so on the local group at each such place. 

### `hasProductLabel_of_tupleIdem_apply_ne_zero`

 Let the labels `c` form a lift setting for `O` and `ϑ`. Let `π` be a representation on forms of
weight `(O.columnCount, O.detExp)` that agrees with right translation (`formTranslation`) on the
elements supported at the places of `O`, and let `u` have the level and character of `O` under `π`.
Suppose that the idempotent `tupleIdem r c` of the labels does not kill `u`. Then at each chosen
place `w = O.chosenPlace i`, which is not its own conjugate, the form `u` has a label with two
blocks. The first block has size `card r` and carries the class function of `scaledTypePoly O c i`,
formed with the injective character `faithfulChar k_w` of the algebraic closure of the residue field
`k_w`. The second block carries the trivial character `1`; its size, the last argument, is the
number of indices outside `range O.incl`. 

### `hasTwistParahoricType_levelSpace`

 Let `π` be a representation on forms of weight `(O.columnCount, O.detExp)` that agrees with
right translation on the elements supported at the places of `O`, and let `u` have the level and
character of `O` under `π`. Let `w = O.twistPlace i` be one of the twist places of the pair, and
`ψ_w = O.tamePart w`, a character of its residue field. Then `u` satisfies
`New.Selmer.HasTwistParahoricType` at `i`: an integral matrix at `w` whose reduction keeps the span
of the indices outside `range O.incl` multiplies `u` by `ψ_w⁻¹` of the determinant of the block of
that reduction on `range O.incl`. 

### `toSmoothForm_mem_levelSpace_repOff`

 Let `B` be base data at the places of `O`. The maximal level (`levelOf` of the empty family),
acting through its components off these places and their conjugates (`B.repOff`), fixes every form
of `O`. 

### `exists_mem_levelSpace_chosenGLRep_map_eq`

 Let `T` commute with `π k` for all `k` in the maximal level. Then `T` keeps the vectors with the
level and character of `O` under `π`, and commutes there with the action of each element `a` of the
group algebra of `O.ChosenGL r`. 

### `translationAtPlaces`

 Right translation of forms of weight `(O.columnCount, O.detExp)` by the components of an element
at the places of `O` and their conjugates (`componentOn`, which puts `1` at all other places). 

### `IsFormOfType`

 A `(c, S)`-form, for labels `c` at the chosen places of the descent pair `O` and a set `S` of
places: an eigenform `f` on the larger space of `O`, of the weight `(O.columnCount, O.detExp)` of
the pair and of type `c`, with the level and character of the forms of `O` off `S` and its
conjugate, and with any level there. The level of `O` is maximal off the places of `O` and their
conjugates; `S` is meant to avoid these. `H` gives the Hecke polynomials of `f`. 

### `IsFormOfType.isEigenform`

 The form `f` is a nonzero eigenform with Hecke polynomials `H` (`IsEigenform`). 

### `IsFormOfType.mem_levelSpace`

 At the places of `O`, the form `f` has the level and character of `O`. 

### `IsFormOfType.tupleIdem_apply`

 The form `f` is of type `c`: the idempotent `tupleIdem r c` of the labels fixes it, for the
  action `O.chosenGLRep` of `∏ GL_r(k_w)` over the chosen places `w`. 

### `IsFormOfType.mem_sphericalAt`

 The form `f` has maximal level at each place `v` such that `v` and its conjugate avoid `S`
  and the places of `O`. 

### `IsFormOfType.isRepOfType_normalisedRep`

 Let the labels `c` form a lift setting for `O` and the twist `ϑ` (`IsLiftSetting`), let the
modulus `ϑ.Q` be auxiliary (`IsAuxiliary`), and let `S` be a set of places outside `badPlaces D ℓ`,
the places dividing `ℓ p₀ p₁ N`. Let `f` be a `(c, S)`-form (`IsFormOfType`) and `R` attached to
its Hecke polynomials. Then the normalised representation `normalisedRep O R` is a representation
of a type (`IsRepOfType`): it is conjugate self-dual with jumps `normalisedJumps O` and level `ϑ.Q`,
`S` and their conjugates, and inertia at the chosen places acts through the roots of
`scaledTypePoly O c i * (X - 1) ^ O.rankDiff`. 

### `exists_baseLevel`

 Fix a prime `ℓ` with an isomorphism `ιℓ : ℂ ≃ ℚ̄_ℓ`, data `D` (among them a CM field `D.E`, two
primes `p₀`, `p₁` given by `D.levelPrime`, and a level `N = D.N`), and a descent pair `O`: hermitian
spaces with bases `r` and `n`, `card r < card n`, with chosen and twist places, weights and a
character. The weight `(O.columnCount, O.detExp)` of its forms on the larger space is given by
column numbers and a power of the determinant. Let `c` be labels at the chosen places that form a
lift setting with the twist `ϑ`. Let `ϑ.Q` be auxiliary: its places have prime norm, neither they
nor their conjugates divide `ℓ p₀ p₁ N` (`badPlaces D ℓ`), and the conjugates are not in `ϑ.Q`.

Then there are jumps `J` and base data `B` of that weight with three properties.
* (a) The projections `typeProjection O c y` of forms `y` of `O` by the idempotent of the labels `c`
  are forms of `B` with no extra level.
* (b) If `y` is integral above `ℓ`, so is `D.chosenGroupOrder • typeProjection O c y`.
* (c) Let `u` be a finite family of places outside `badPlaces D ℓ`, let `x` be an eigensystem of `B`
  of level `u`, and `R = normalisedRep O x.galRep` its representation twisted by
  `normalizingAvatar O`, the avatar of the inverse of the character of `O` with weight `-card r`.
  Then `R` satisfies `IsRepOfType` with jumps `J`, the level being `ϑ.Q`, `range u` and their
  conjugates: it is conjugate self-dual up to twist, has the local properties of
  `IsConjSelfDualOfLevel` off the level, and inertia at the chosen places acts through the roots of
  `scaledTypePoly O c i` (`c i` with roots scaled according to `(O.tamePart _)⁻¹`) times
  `(X - 1) ^ O.rankDiff`. Each `g` in the inertia above `ϑ.Q` and its conjugate satisfies
  `(R g - ϑ.invAvatar g) (R g - 1) = 0`. 
