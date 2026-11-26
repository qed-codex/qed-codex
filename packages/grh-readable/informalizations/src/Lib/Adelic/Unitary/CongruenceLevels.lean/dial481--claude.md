---
{
  "module": "src/Lib/Adelic/Unitary/CongruenceLevels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/CongruenceLevels.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/CongruenceLevels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Principal levels and levels defined by reductions in the finite adelic unitary group

Let G_f = `New.Gf` be the finite adelic unitary group of the CM field E. Let Ô = `New.Ô` be the
integral finite adeles of E. Let K₀ = `New.stdLevel` be the elements of G_f lying in GL_n(Ô). This
file studies open subgroups (levels) of K₀ of two kinds. The first is the principal level of a
nonzero integer a of E. It consists of the g in K₀ with all entries of g - 1 in aÔ. The second is
the level `New.levelOf w H` of the elements whose reductions at a family of places w_i lie in a
subgroup H. If the places are finitely many, distinct, and none is conjugate to any w_j, then
reduction is onto the product. For a character χ of H, the vectors on which this level acts through
reduction and χ carry an action of the groups that normalise H and fix χ.

## Main definitions and results

* `New.exists_congruenceGL_subset`: every neighbourhood of `1` in `GL n` of the finite adeles
  contains a principal congruence subgroup of integer level. Here `New.Ô` is the ring of integral
  finite adeles, and `New.congruenceGL I id` is the group of matrices in `GL n` of it that are `1`
  modulo `I`.
* `New.principalLevel`, `New.isOpen_principalLevel`: the principal level of an integer a, open for
  a ≠ 0.
* `New.levelOf`: the k in K₀ whose reductions at a family of places w_i lie in a subgroup H of ∏
  GL_n(k_{w_i}); it is open for a finite family (`New.isOpen_levelOf`).
* `New.exists_reduceFamily_eq`, `New.relIndex_levelOf`: if the w_i are finitely many, distinct, and
  none is conjugate to a w_j, reduction is onto the product and the level has index [∏ GL_n : H].
* `New.relIndex_principalLevel_le`: the index of the principal level of `a ≠ 0` is at most
  `N(a) ^ (n ^ 2)`, where `N(a)` is the norm of `a`.
* `New.levelRep`: a group that normalises `H` and fixes `χ` acts on the vectors on which the level
  `New.levelOf w H` acts through reduction and `χ`.

Notions from other files:
* `New.Gf.atPlace`, `New.stdLevel.reduceAt`: The component at w of an element of G_f, and the
  reduction modulo w of an element of K₀. Elements of `trivialOn n P` have component 1 at each place
  in P.
* `New.ResField`: The residue field of the completion E_w of E at the finite place w.
* `New.levelSpace`: The vectors v with π(k)v = χ(k)v for all k in the level.

## Relation to the literature

Known result: Congruence subgroups and level structures of adelic groups. Here levels are preimages
of subgroups of the reductions at a family of places, or principal levels of a global modulus, in
the unitary group of the identity form. Source: V. Platonov, A. Rapinchuk, Algebraic groups and
number theory, ch. 3 and 5; B. H. Gross, Algebraic modular forms, Israel J. Math. 113 (1999) 61-93.


 ## Principal congruence subgroups in adelic GL_n 

### `New.exists_congruenceGL_subset`

 Every neighbourhood of `1` in `GL n` of the finite adeles of `E` contains a principal congruence
subgroup. This is the group `New.congruenceGL` of level `M` times the integral finite adeles
`New.Ô E`, for some nonzero natural number `M`. 


## Reduction at places, principal levels and levels defined by reductions

`star w` is the complex conjugate place; `New.ofSplitPlace` puts a matrix of GL_n(E_w) into G_f at a
place w ≠ `star w`, with component 1 away from w and `star w`.


 ### Reduction of GL_n and divisibility in the integral finite adeles 

### `GL_map_surjective`

 Entrywise application of a surjective local ring homomorphism gives a surjective map on
GL_n. 

### `reduceGL`

 The reduction homomorphism from GL_n(O_w) to GL_n of the residue field at w. 

### `reduceGL_surjective`

 Reduction GL_n(O_w) → GL_n(k_w) to the residue field k_w at the place w is surjective. 

### `mem_span_iff_valuation_le`

 For an integer a of E, a finite adele y lies in aÔ if and only if y lies in the ring Ô of
integral finite adeles and |y|_u ≤ |a|_u at every finite place u dividing a. 

### `stdLevel.map_apply`

 The entries of the image of g ∈ K₀ = `stdLevel E n` under `stdLevel.map n f` are the images
under f of the entries of g. 

### `stdLevel.map_eq_one`

 An element g of K₀ = `stdLevel E n` maps to 1 under the entrywise homomorphism
`stdLevel.map n f` if and only if f kills every entry of g - 1, read in Ô. 

 ### Principal levels 

### `principalLevel`

 The principal level K(a) for an integer a of E is the subgroup of g in K₀ = `New.stdLevel` such
that every entry of g - 1 is a·y for some y in Ô. It is the principal congruence subgroup
`New.congruenceGL` of level aÔ intersected with G_f, here the unitary group `U 1` of the identity
form, a subgroup of GL_n of the finite adeles; `Subgroup.copy` only restates the carrier so that
membership unfolds to the displayed condition. 

### `mem_principalLevel`

 An element g of G_f is in the principal level of a if and only if it lies in K₀ = `stdLevel E n`
and every entry of g - 1 is a times an element of Ô. 

### `map_eq_one_of_mem_principalLevel`

 If f : Ô → S kills the integer a, then an element k of the principal level of a maps to 1 in
GL_n(S) under entrywise application of f. 

### `Variety.isOpen_congruenceGL_span`

 For a nonzero integer a, the congruence subgroup of GL_n of the finite adeles of level aÔ is
open. 

### `exists_principalLevel_subset`

 Every neighbourhood of 1 in G_f contains the principal level `New.principalLevel` of some
nonzero natural number M. 

 ### Reduction of an element with given component 

### `stdLevel.reduceAt_eq_of_atPlace`

 If the component at w of k ∈ K₀ is the integral matrix t, the reduction of k at w is t modulo
w. 

### `stdLevel.reduceAt_eq_one_of_atPlace`

 An element of K₀ with component 1 at w reduces to 1 modulo w. 

 ### Levels cut out by reductions at a family of places 

### `IsConjApart`

 The family w of finite places of the CM field E is injective and no w j is the conjugate of
any w i; in particular no w i is its own conjugate. 

### `IsConjApart.injective`

 The places of the family are pairwise distinct. 

### `IsConjApart.star_ne`

 The conjugate of a place of the family is never a place of the family. 

### `stdLevel.reduceFamily`

 The homomorphism from K₀ to ∏_i GL_n(k_{w_i}) given by reduction modulo each place of the
family w_i. 

### `levelOf`

 The subgroup of G_f of elements of K₀ whose reductions modulo the places w_i form an element
of the subgroup H of ∏_i GL_n(k_{w_i}). 

### `mem_levelOf`

 An element of G_f is in `levelOf w H` if and only if it lies in K₀ = `stdLevel E n` and its
family of reductions at the places w_i lies in H. 

### `levelOf.reduction`

 The homomorphism from the level `New.levelOf` w H to H given by reduction modulo the places
w_i. 

### `principalLevel_le_levelOf`

 If the integer a lies in every w_i, the principal level of a is contained in
`levelOf w H`. 

### `isOpen_levelOf`

 For a finite family of places, the level `levelOf w H` is open in G_f. 

### `instIsLevelLevelOf`

 For finite `ι`, `levelOf w H` is a level (an instance of `IsLevel`): it is open and contained in
the standard level. 

### `relIndex_ne_zero_of_isLevel`

 A level K, that is an open subgroup of G_f inside K₀, has finite index in the compact group
K₀. 

### `reduceFamily_ofSplitPlace`

 For distinct places `w i`, none conjugate to a `w j` (`IsConjApart w`, whose field `star_ne`
says that `w i` is split), a matrix `k` in `localIntGL n (w i)` = GL_n(O_{w i}) put at the split
place `w i` by `New.ofSplitPlace` reduces to `reduceGL k`, the reduction of `k` modulo `w i`, at
`w i` and to `1` at the other places of the family. 

### `exists_reduceFamily_eq`

 For finitely many distinct places w_i, none conjugate to a w_j, every family s of matrices in
GL_n(k_{w_i}) is the reduction of some k in K₀ with component 1 away from the w_i and their
conjugates. 

### `relIndex_levelOf`

 For finitely many distinct places w_i, none conjugate to a w_j, the index of the level
`New.levelOf` w H in K₀ is the index of H in ∏ GL_n(k_{w_i}). 


## Index bounds for principal levels and auxiliary facts on Ô and integers

* `New.relIndex_principalLevel_le`: the principal level of `a ≠ 0` has index at most
  `N(a) ^ (n ^ 2)` in K₀.
* `New.bijective_quot_Ô`, `New.card_Ô_quot_span`: `𝓞 / J ≃ Ô / I` when the ideal `I` of `Ô`
  contracts to `J` and `J` contains a nonzero integer. For `a ≠ 0`, `Ô / a Ô` has `N(a)` elements.
* Further lemmas on characters of nonarchimedean groups, on divisibility by an integer in `Ô` and
  on products of distinct places.


### `char_eventually_eq_one`

 A continuous character χ : G → S¹ of a nonarchimedean topological group G is trivial on a
neighbourhood of 1. 

### `card_GL_le`

 For a finite commutative ring R, the group GL_n(R) has at most |R|^(n²) elements. 

### `dvd_iff_reduceAt_eq_zero`

 Let `a` vanish to order one at each place that contains it. Then `a` divides `y ∈ Ô` if and only
if the reduction `reduceAt w y` of `y` modulo w is `0` for every place w that contains `a`. 

### `mem_prod_finPlace_iff`

 For distinct places w_i, an integer x of E lies in their product if and only if it lies in
each w_i. 

### `dvd_iff_Ô`

 For integers a ≠ 0 and b of E, a divides b in Ô if and only if it does so in 𝓞_E. 

### `bijective_quot_Ô`

 If an ideal I of Ô contracts to the ideal J of 𝓞_E and J contains a nonzero element a, then
𝓞_E/J → Ô/I is bijective. 

### `map_under_Ô`

 An ideal I of Ô that contains a nonzero element a of 𝓞_E is generated by its contraction to
𝓞_E. 

### `card_Ô_quot_span`

 For a nonzero integer a of E, the quotient Ô/aÔ has N(a) elements, where N(a) is the absolute
norm of (a). 

### `principalLevel_subgroupOf_stdLevel_eq_ker`

 For a CM field `E` and an integer `a` of `E`, the principal level K(a) (the g in K₀ with g -
1 ≡ 0 mod aÔ) is the kernel of reduction K₀ → GL_n(Ô/aÔ). Here K₀ = `stdLevel E n` is G_f ∩ GL_n(Ô),
the stabiliser of Ô^n in the finite adelic unitary group G_f. 

### `relIndex_principalLevel_le`

 For a nonzero integer a of E, the index of the principal level K(a) in K₀ = `New.stdLevel` is at
most N(a)^(n²). Here N(a) is the absolute norm of (a) and n in the exponent is the size of the index
type. 


## Action on vectors of a level through lifts

* `New.liftResidue`: a chosen lift of an element of the product, supported at the `w i` and their
  conjugates.
* `New.apply_liftResidue_eq`: on vectors of level `levelOf w H` and character `χ` composed with
  reduction, all lifts act alike.


### `levelSpace_levelOf_apply`

 An element `k` of `New.stdLevel E n` with reduction `x ∈ H` acts on vectors of level
`New.levelOf w H` and character `χ` by the scalar `χ x`. 

### `liftResidue`

 For finitely many distinct places w_i, none conjugate to another or itself, a chosen element
of K₀ supported at the w_i and their conjugates whose reductions modulo the w_i are s. 

### `apply_liftResidue_eq`

 On a vector `v` of level `New.levelOf w H` and character `χ`, the chosen lift of `s` acts as any
`k` in `New.stdLevel E n` with reduction `s` does. 

### `map_liftResidue_mem_levelSpace`

 If s normalises H and fixes χ, then π of the chosen lift of s maps vectors of level
`New.levelOf` w H and character χ to vectors of the same kind. 

### `levelRep`

 For finitely many distinct places w_i, none conjugate to a w_j, and φ : S → ∏ GL_n(k_{w_i})
normalising H and fixing χ, the representation s ↦ π(`New.liftResidue` φ(s)) of S on vectors of
level `New.levelOf` w H and character χ. 
