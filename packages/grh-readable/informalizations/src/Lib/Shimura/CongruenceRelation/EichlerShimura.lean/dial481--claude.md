---
{
  "module": "src/Lib/Shimura/CongruenceRelation/EichlerShimura.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/CongruenceRelation/EichlerShimura.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/CongruenceRelation/EichlerShimura.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The congruence relation and the trivial action of inertia on ℓ-adic cohomology

The Eichler–Shimura argument: a relation between Frobenius twists of points in characteristic p
gives a relation between pull-backs and Galois action on ℓ-adic cohomology.

* `New.Variety.ellAdicCohom.ellAdicPull_frobEnd`: the absolute Frobenius acts trivially on
  cohomology.
* `New.Variety.ellAdicCohom.congruence_relation`: the congruence relation
  `New.Variety.CongruenceRelation` on points gives ∑ mᵢ uᵢ^* g^(−eᵢ) = 0 on Vⁿ(Y), for a Frobenius
  element g.
* `New.Variety.ellAdicCohom.galoisAction_eq_one_of_inertia`: inertia acts trivially (the case q = 1
  of the relation).

The idea: extend classes from Ω to the valuation ring A, then restrict to the special fibre.
`New.Variety.ellAdicCohom` is X ↦ Vⁿ(X) = ℚ_ℓ ⊗ Hⁿ(X_Ω, ℤ_ℓ), with the action
`New.Variety.ellAdicCohom.galoisAction` of Γ; `New.Variety.ellAdicPull` is the pull-back along a map
of free abelian functors (`freeAb` sends a functor to its pointwise free abelian group);
`New.Variety.IsCharted` is the hypothesis on Y that stands in for smoothness: it gives smooth base
change, so that pull-back from A to Ω is bijective on the cohomology of Y.

Notions from other files:
* `New.IsFrob`: σ stabilises the valuation subring A and σx ≡ x^q modulo the maximal ideal for all x
  in A; for q = 1 this is membership in the inertia group.
* `New.Variety.mapOnTests`: For a map u: X → Y of set-valued functors on rings, its restriction to a
  map of functors on test rings.
* `New.Variety.ellAdicCoeff`: The coefficient `ℤ_ℓ`: a test ring `A` goes to the Witt vectors of the
  ring of locally constant functions `Spec A → 𝔽_ℓ`.

## Relation to the literature

Known result: Smooth proper reduction gives unramified ℓ-adic cohomology, and Frobenius relations
pass to it. Here the base is the valuation ring of a place. Source: Stacks project, Tags 0GKD (SGA4
XVI 2.2) and 03SN (SGA5 XV); Deligne, Formes modulaires et représentations ℓ-adiques, Sém. Bourbaki
355 (1969).


### `frobEnd`

 For a functor U on rings with points only in rings where p = 0, the endomorphism sending x
in U(B) to its image under b ↦ b^(p^j). 

### `frobEnd_app`

 The value of `New.Variety.ellAdicCohom.frobEnd` at a point x ∈ U(B): the image of x under the
ring map b ↦ b^(p^j) of B. 

### `ellAdicPull_frobEnd`

 The absolute Frobenius acts trivially on ℓ-adic cohomology. Let p = 0 in every ring B in which
U has a point (`hU_char`). Then the endomorphism `New.Variety.ellAdicCohom.frobEnd` of U, which
moves a point x ∈ U(B) along the ring map b ↦ b^(p^j) of B, pulls back to the identity of
ℚ_ℓ ⊗ Hⁿ(U, ℤ_ℓ). 

### `congruence_relation`

 The Eichler–Shimura relation. Let A ⊂ Ω (an algebraic closure of ℚ) be a valuation ring
containing the image of R (`hR`), with p in its maximal ideal (`hp`) and ℓ a unit (`hℓ`); let Γ act
on Ω by R-algebra automorphisms, and let g ∈ Γ be a Frobenius for p^f at A, i.e. g stabilises A and
acts as x ↦ x^(p^f) modulo its maximal ideal. Let W, Y be proper over R with Y charted over R
(`New.Variety.IsCharted`); if uᵢ : W → Y satisfy ∑ mᵢ [Frob_(p^(f eᵢ)) uᵢ(w)] = 0 (in the sense of
`Cancels`; Frob_q composes a k-point with Spec of the map x ↦ x^q of k) at the field points w of W
of characteristic p killing the preimage in R of A's maximal ideal
(`New.Variety.CongruenceRelation`), then ∑ mᵢ uᵢ^*(g^(−eᵢ) x) = 0 for every x in Vⁿ(Y) = ℚ_ℓ ⊗ Hⁿ(Y
×_R Ω, ℤ_ℓ), with Γ acting through Ω. 

### `galoisAction_eq_one_of_inertia`

 Inertia acts trivially. Let Ω be an algebraic closure of ℚ and an R-algebra, A ⊂ Ω a valuation
ring that contains the image of R (`hR`), with a prime p in its maximal ideal (`hp`) and ℓ a unit
(`hℓ`). For Y proper over R and as in `New.Variety.IsCharted`, the inertia group of A acts
trivially on Vⁿ(Y). 
