---
{
  "module": "src/Lib/Shimura/HeckeTower/Model.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/HeckeTower/Model.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/HeckeTower/Model.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Properties of a Kuga–Sato tower, Hecke operators at split places, torsion counts and levels

The structure `New.Variety.Model` collects the geometry of a tower of Kuga–Sato varieties that the
point count uses. K(𝔑) denotes the principal level `New.Variety.levelGU n 𝔑`. τ_{w,j} denotes the
Hecke element `New.Variety.heckeSum` at a safe split place w of E. The file shows that these
elements lie in the Hecke algebra of K(𝔑). It counts the `I`-torsion of the adelic module
`New.AdelicTorsion E n`: it has N(I) ^ card n elements, where N(I) is the norm of the ideal I. It
proves finiteness statements for multiplication by integers on the abelian schemes of a family
`X : New.ThetaFamily D Z τ`.

## Main definitions and results

* `New.Variety.Model`: the tower of varieties with its properties.
* `New.Variety.asAlgebraHom_heckeSum`: τ_{w,j} acts on K(𝔑)-fixed vectors as a central element times
  the j-th Hecke operator of GL_n(E_w); `New.Variety.tauHecke` is τ_{w,j} in the Hecke algebra.
* `New.Variety.Model.exists_isHeckeAction`: the commuting operators on F(Z), for the base Z of a
  model and a functor F with descent.
* `New.card_torsionBySet_adelicTorsion`: for `I ≠ 0` the `I`-torsion of `New.AdelicTorsion E n` has
  `N(I) ^ card n` elements.
* `New.Variety.exists_level_conj_mem`: a principal level deep enough for finitely many isogenies.

Notions from other files:
* `New.Variety.SplitFinPlace`: The finite places w of E with w̄ ≠ w, that is, those split over the
  maximal real subfield.
* `New.Variety.levelGU`: the principal level K(𝔑), the similitudes in `GL_n(Ô E)` that are congruent
  to `1` modulo `𝔑`.
* `New.Variety.conjAtSplit w g`: for a split place w, the adelic matrix that is g⁻ᵀ at w, the
  conjugate of g at w̄, and 1 elsewhere.
* `New.Variety.heckeSum n k w j`: the Hecke element τ_{w,j}, the sum of
  `New.Variety.invHeckeIsogeny w U` over the subspaces U of dimension j.
* `New.Variety.IsSafe`: Safe places w of E: the place u of ℚ(√−d₀) below w satisfies
  `New.GaloisRep.IsSplitPrimeToDisc`, and 𝔑 lies neither in w nor in any place above ū.

## Relation to the literature

Known result: Hecke algebra of a pair acting by correspondences on the base of a tower. Here only a
semigroup acts, and only far enough up the tower, and the algebra is a subalgebra of the group ring.
The cohomology theory may be any functor to modules for which the base is the invariants of each
cover. Source: Shimura, Introduction to the arithmetic theory of automorphic functions, 1971, ch. 3
and 7–8.

See also `Lib.Shimura.IntegralModel.TowerExistence`, `Lib.Shimura.Uniformisation.AppellHumbert` and
`Lib.Shimura.AbelianScheme.IsogenyFlatness`.



## The tower of varieties and its required properties

Conventions: `New.Variety.levelGU n 𝔑` is the principal level K(𝔑) in the similitude group
`New.Variety.GU`; `New.Variety.GUPlus` is the monoid of similitudes with integral inverse;
`New.Variety.ModuliPoint E n ν` is the type of analytic points a = (frame, reflection, ν marked
vectors), with isomorphisms `New.Variety.ModuliPoint.IsLevelIso` and the action a·(g, α)
`New.Variety.ModuliPoint.act`.


### `New.Variety.Model`

 The tower of Kuga–Sato varieties over `R`, given by a list of properties. A level `i` is a
finite set of pairs (non-zero integer of `E`, element of `New.Variety.GUPlus`), ordered by
inclusion. The data are a base Z = `base`, schemes W_i = `cover i` with legs p_g = `leg i g` from
W_i to Z (π = p_1), sets s_i = `legIndices i`, finite groups Δ_i = `deckGroup i` acting through
`deck i`, maps m_α = `mulMap α` of Z, complex points `point i` and the relative dimension
`dimension` of Z; the other fields are properties of these. 

### `New.Variety.Model.base`

 The base scheme Z over `Spec R`. 

### `New.Variety.Model.cover`

 The scheme W_i over `Spec R` at level `i`. 

### `New.Variety.Model.legIndices`

 The set s_i of adelic matrices whose legs the fields at level `i` speak about. 

### `New.Variety.Model.leg`

 The legs p_g : W_i → Z, one for each coset gK(𝔑); the leg of `1` is called π. 

### `New.Variety.Model.one_mem`

 The identity lies in every s_i. 

### `New.Variety.Model.eventually_translate`

 For `g` in `GUPlus E n` and any level `j`, all large levels `i` have g ∈ s_i and a map
  f : W_i → W_j with p_q ∘ f = p_{gq} for all q ∈ s_j. 

### `New.Variety.Model.deckGroup`

 The finite group Δ_i at level `i`. 

### `New.Variety.Model.deck`

 The action of Δ_i on W_i. 

### `New.Variety.Model.deck_comp_leg`

 For each δ ∈ Δ_i there is κ ∈ K(𝔑) with p_q ∘ δ = p_{κq} for all q ∈ s_i. 

### `New.Variety.Model.mulMap`

 The maps m_α : Z → Z, one for each family `α` of `ν` integers of `E`. 

### `New.Variety.Model.point`

 The complex point [a]_i of W_i attached to `a`. 

### `New.Variety.Model.point_surjective`

 Every complex point of W_i is some [a]_i. 

### `New.Variety.Model.point_eq_iff`

 π[a]_i = π[b]_i exactly when `a` and `b` are isomorphic at level K(𝔑). 

### `New.Variety.Model.point_leg`

 For `g` in `GUPlus E n` with g ∈ s_i, m_α p_g [a]_i = π[a·(g, α)]_i. 

### `New.Variety.Model.dimension`

 The relative dimension of Z over `Spec R`. 

### `New.Variety.Model.smooth`

 Z is smooth over `Spec R` of relative dimension `dimension`. 

### `New.Variety.Model.proper`

 Z is proper over `Spec R`. 

### `New.Variety.Model.projective`

 W_i is a closed subscheme of a projective space over `Spec R`. 

### `New.Variety.Model.isReduced`

 W_i is reduced. 

### `New.Variety.Model.covering`

 π is onto, and its fibres in characteristic `0` are torsors under Δ_i. 

### `New.Variety.Model.tangent`

 Let g ∈ s_i and let z : a·(g, α) ≅ a at level K(𝔑) have separable characteristic polynomial,
  with `a.reflection` the involution `markedReflection` of `z` at its `μ`-th listed root. Then at
  [a]_i the polynomial `localTerm` is a constant times det(1 - X (dπ)⁻¹ d(m_α p_g)), in the sense
  of `IsTangentPoly`. 

### `New.Variety.Model.congruence`

 The congruence relation at a split place `w` satisfying `IsSafe`, with residue field k_w of
  order q = p^f: if `𝔭` contains the image of `w` and all g_A = `invHeckeIsogeny w A` lie in s_i, A
  a subspace of k_wⁿ of dimension r, then ∑_A (-1)^r q^{r(r-1)/2} [Frob_p^{(n-r)f} p_{g_A}(x)] = 0
  in the sense of `CongruenceRelation`. 


## Hecke elements τ_{w,j} at safe split places and their operators

* `New.Variety.conj_conjAtSplit`, `New.Variety.conjAtSplit_dualComponent` (with its two parts
  `New.Variety.conjAtSplit_dualComponent_mem_levelGU` and
  `New.Variety.commute_inv_conjAtSplit_dualComponent_mul`): the embedding `New.Variety.conjAtSplit`
  of GL_n(E_w) into the similitudes `New.Variety.GU` and its retraction `New.Variety.dualComponent`.


### `entryConj`

 The endomorphism of the unitary group {g : gᴴg = 1} of matrices over R indexed by `n` that
applies the involution of R to each entry. 

### `conjAtSplit_mem_GU`

 `conjAtSplit w g` is a unitary similitude (with multiplier `1`). 

### `evalAt_conjAtSplit_of_ne`

 At a place `u` other than `w` and its conjugate, the component of `conjAtSplit w g` is `1`. 

### `conj_conjAtSplit`

 Let w be a split place and g a unitary similitude. Then conjugating `conjAtSplit w m` by g gives
`conjAtSplit w` of the conjugate of m by the component `dualComponent w g`. 

### `commute_conjAtSplit`

 A unitary similitude whose component `dualComponent w g` is `1` commutes with the image of
`conjAtSplit w`. 

### `conjAtSplit_mem_intGL_iff`

 `conjAtSplit w g` is an integral matrix exactly when `g` lies in the maximal compact subgroup
`localIntGL n w` of `GL_n(E_w)`. 

 ### The level, place by place 

### `mem_levelGU_of_map_evalAt_eq`

 A similitude g in GL_n(Ô) lies in the principal level K(𝔑) if at each place u dividing 𝔑 it
has the same u-component as some element of K(𝔑). 

### `isOpen_comap_conjAtSplit`

 For `𝔑 ≠ 0`, the preimage of the principal level K(𝔑) under `conjAtSplit w` is open in
`GL_n(E_w)`. 

### `conjAtSplit_dualComponent_mem_levelGU`

 Let w be split with 𝔑 ∉ w̄, and let κ ∈ K(𝔑). Then `conjAtSplit w (dualComponent w κ)`, the
unitary element equal to κ at w and to 1 away from w and w̄, lies in K(𝔑). 

### `commute_inv_conjAtSplit_dualComponent_mul`

 Let κ be a unitary similitude and c = `conjAtSplit w (dualComponent w κ)`. Then c⁻¹κ commutes
with every element `conjAtSplit w m` of the image of `conjAtSplit w`. 

### `conjAtSplit_dualComponent`

 Both `conjAtSplit_dualComponent_mem_levelGU` and `commute_inv_conjAtSplit_dualComponent_mul`:
for w split with 𝔑 ∉ w̄ and κ ∈ K(𝔑), c = `conjAtSplit w (dualComponent w κ)` lies in K(𝔑), and
c⁻¹κ commutes with the whole image of `conjAtSplit w`. 

### `mem_heckeAlgebra_of_mem_fixedToEigen`

 Let w̄ ∤ 𝔑 and let b be a combination of elements g of D. Assume that each g in D lies in
`New.Variety.GUPlus` and commutes with everything commuting with the local group at w. If in every
representation b sends K(𝔑)-fixed vectors to vectors fixed by the preimage of K(𝔑) under
`New.Variety.conjAtSplit` at w, then b lies in the Hecke algebra `heckeAlgebra n k 𝔑`: the
combinations of elements of `GUPlus E n` that in every representation send K(𝔑)-fixed vectors to
K(𝔑)-fixed vectors. 

 ### The Hecke elements 

### `conjTranspose_centralScalar_mul_centralScalar`

 For a finite idele x of K₀ and z = `centralScalar x`, the scalar matrix of the conjugate of x,
the matrix zᴴz is the scalar matrix of the norm of x to ℚ. 

### `mem_GU_centralScalar`

 The scalar matrix `centralScalar x` of a finite idele x of K₀ is a unitary similitude. 

### `isScalarFrame_centralScalar`

 For a finite idele x of K₀ and a rational c equal to the idelic absolute value of the norm of x
to ℚ, the scalar matrix `centralScalar x` is a frame for the scalar form c·1. 

### `centralScalar_mem_GU`

 For a finite idele x of K₀, both `mem_GU_centralScalar` and `isScalarFrame_centralScalar`:
`centralScalar x` is a unitary similitude, and a frame for c·1 whenever the rational c is the
idelic absolute value of the norm of x to ℚ. 

### `heckeSum_mem_spanOn`

 The Hecke element `τ_{w,j} = heckeSum n k w j` is a combination of the elements
`invHeckeIsogeny w U`. 

### `evalAt_centralScalar_of_ne`

 Let `x` be a unit of the completion at `w`, and let `u` be a place whose restriction to `K₀` is
not the conjugate of that of `w`. Then the `u`-component of the scalar matrix `centralScalar` of
the norm of the local idele of `x` is `1`. 

### `val_inv_centralScalar`

 The matrix of the inverse of `centralScalar x` is the scalar matrix of the conjugate of
`x⁻¹`. 

### `invHeckeIsogeny_mem_GUPlus`

 For a split finite place w of E and a subspace U of k_wⁿ of dimension r, where k_w is the
residue field at w, the matrix `invHeckeIsogeny w U` lies in `GUPlus E n`: it is a similitude whose
inverse has integral entries. This matrix is the scalar matrix of the conjugate of the (−r)-th power
of `uniformizerNorm w`, the norm to K₀ of the idele that is a uniformiser at w and 1 elsewhere,
times `conjAtSplit w` of the transpose of `basicCosetRep U`, an integral matrix at w whose
determinant has order r. 

### `SafePlace.mem_levelSpace_conjAtSplit`

 Let `x` be fixed by the level K(𝔑), and let `w` be the safe place of the pair `s = (w, j)`. Then
`x` is fixed by GL_n(O_w) (`New.localIntGL`), acting through `New.Variety.conjAtSplit w`. 

### `asAlgebraHom_heckeSum`

 Let `s = (w, j)` with `w` a safe place, and let `x` be fixed by K(𝔑) in the representation `π`.
Then τ_{w,j} sends `x` to the j-th Hecke operator of GL_n(E_w) (acting through
`conjAtSplit w`) applied to `x`, followed by the central scalar of the inverse of
`New.Variety.uniformizerNorm w ^ j`. 

### `heckeSum_mem_heckeAlgebra`

 For `s = (w, j)` with `w` a safe place, τ_{w,j} lies in the Hecke algebra of the level K(𝔑). 

### `tauHecke`

 For s = (w, j), with w a safe split place and j a natural number, the element τ_{w,j} as a
member of the Hecke algebra of level K(𝔑) over k. The pair is one argument so that words in
these elements are lists. 

### `asAlgebraHom_tauHecke_mem_levelSpace`

 The element τ_{w,j} of the Hecke algebra keeps the vectors fixed by K(𝔑). 

### `asAlgebraHom_tauHecke_comm`

 Let π be a representation of GL_n(𝔸f E) on the k-module W, and let s = (w, j) and s' be pairs of
a split place of E that is safe for the level 𝔑 (`SafePlace 𝔑`) and a natural number. The Hecke
elements τ_{w,j} = `tauHecke s` and `tauHecke s'` of level K(𝔑) over k then act through π by
commuting operators on any vector `x` fixed by K(𝔑) = `levelGU n 𝔑`, the similitudes in GL_n(Ô_E)
congruent to 1 modulo 𝔑. 

### `Model.legPullback`

 For a contravariant functor F to k-modules, the pull-back F(Z) → F(W_i) along the leg of level
`i` at the coset `q`. 

### `Model.IsHeckeAction`

 The operators t(w, j) on F(Z), indexed by a safe place w and a natural number j, are the action
of the Hecke elements τ_{w,j}, read on the level `I w`. 

### `Model.IsHeckeAction.commute`

 The operators commute. 

### `Model.IsHeckeAction.legPullback_comp`

 Pulled back to the level `I w`, t(w, j) is the sum of the legs over τ_{w,j}. 

### `Model.IsHeckeAction.eventually_cosetSum_mul_prod`

 On deep levels, a word L in the Hecke elements acts as the same word in the operators: for a
  ring k', b ∈ k'[G] supported on `GUPlus E n` and Ψ additive, the sum of Ψ of the legs over
  b · L(τ) is the sum over b of Ψ of the legs composed with L(t). 

### `Model.eventually_cosetSum_mul_prod_of_legPullback_comp`

 Suppose the level `I w` has legs for all `invHeckeIsogeny w U`, and each t(w, j), pulled back to
the level `I w`, is the sum of the legs over τ_{w,j} (`cosetSum`: the legs at the cosets of the
terms of τ_{w,j}, weighted by their coefficients). Then on deep levels a word in the Hecke elements
acts as the same word in the operators t. 

 ### The operators on the base of a model 

### `Model.exists_isHeckeAction`

 Let `T` be a model of the Kuga–Sato tower over `R`, with base Z = `T.base`, schemes
W_i = `T.cover i` over levels `i`, legs W_i → Z and finite deck groups Δ_i = `T.deckGroup i`, and
let F be a contravariant functor to k-modules. Suppose each pull-back along the leg of 1 is
injective with image containing the Δ_i-invariants, and that for every safe place w and subspace U
of the residue-field space, `invHeckeIsogeny w U` lies in `T.legIndices (I w)`, the set of matrices
g whose legs p_g at level `I w` the fields of `T` speak about. Then the Hecke elements act on F(Z)
by commuting operators, in the sense of `New.Variety.Model.IsHeckeAction`.

Known result: Hecke algebra of a pair and its action by correspondences on the base of a tower. 


## Adelic torsion and multiplication by integers

Degrees and torsion on the abelian schemes of a family `X : New.ThetaFamily D Z τ`.

`New.ThetaObject X T` is a point `T ⟶ Z` of the base `Z` of the family. For such a point `y`,
`y.groupScheme` is the abelian scheme over `T` pulled back along it, and `𝟙_ _ ⟶ y.groupScheme` is
the group of its sections. `New.AdelicTorsion E n` is the module `(𝔸f E / Ô E)ⁿ`, an adelic model of
`(E / 𝓞 E)ⁿ`.


### `card_torsionBySet_adelicTorsion`

 For a non-zero ideal I of O_E, the submodule of (𝔸_f / Ô)ⁿ killed by I has N(I)^|n|
elements, where N(I) is the absolute norm and |n| the size of the index set. 

### `ThetaObject.isIsogeny_smul_id`

 On the abelian scheme of an object y over a local ring, multiplication by a non-zero element
a of O_E is finite, flat and surjective. 

### `ThetaObject.exists_apply_eq_of_torsion`

 Let A be the abelian variety of an object of the family over ℂ. Every injective O_E-linear map
from `New.AdelicTorsion E D.Index` to A(ℂ) has all torsion points of A(ℂ) in its image. 

 ## Levels for finitely many isogenies, torsion classes and finite index 

### `exists_level_conj_mem`

 Let `𝔑 ≠ 0` and let `s` be a finite set of pairs `(𝔞, g)` of a nonzero integer of `E` and a
similitude in `New.Variety.GUPlus`. There is a level `m` with `g⁻¹ K(m) g ⊆ K(𝔑) ∩ K(𝔞)` for all
`(𝔞, g)` in `s` and for the pairs `(1, 1)` and `(m, 1)`. 

### `NonzeroTorsion`

 For a non-zero element 𝔪 of O_E, the set of non-zero elements of (𝔸_f / Ô)ⁿ ≅ (E / O_E)ⁿ
killed by 𝔪. 

### `finite_torsionBy`

 For a non-zero element 𝔪 of O_E, the 𝔪-torsion of (𝔸_f / Ô)ⁿ is finite. 

### `instance : ((levelGU n 𝔪).subgroupOf (levelGU n 𝔑)).FiniteIndex`

 For non-zero 𝔪, the level K(𝔪) ∩ K(𝔑) has finite index in K(𝔑). 
