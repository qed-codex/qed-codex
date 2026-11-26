---
{
  "module": "src/Lib/Cohomology/Etale/RelativeChains.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Etale/RelativeChains.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Etale/RelativeChains.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Relative chains ℤ[V]/ℤ[U]: local isomorphisms, transfer, excision and gluing

This file provides tools for computing the groups Ext^n(N, F) (`New.Variety.H`) of functors from a
category C to abelian groups. For a subfunctor U of a set-valued functor V,
`New.Variety.relFreeAb U` is the quotient ℤ[V]/ℤ[U] of free abelian groups (`New.Variety.freeAb`).
Its Ext^n into F is the relative cohomology H^n(V, U). A map is an equivalence for F
(`New.Variety.IsCohomEquiv`) if it is bijective on all Ext^n(·, F). A subfunctor U of Y is dense
(`New.Variety.IsCohomDense`) if over every point h_A → Y its preimage gives an equivalence; with
these notions the file proves vanishing for locally zero functors, transfer, excision and gluing of
relative classes over finite covers.

## Main definitions and results

* `New.Variety.cohomology_eq_zero_of_locallyZero`, `New.Variety.isCohomEquiv_of_locallyZero`: a
  functor whose sections all die on dense sieves has no cohomology, so a map with such a kernel and
  cokernel is an equivalence.
* `New.Variety.exists_transfer_map`: the transfer attached to finitely many locally permuted maps
  (`New.Variety.permutedPairs`: the pairs on which they are permuted).
* `New.Variety.relFreeAb.shortExact_triple`, `New.Variety.relFreeAb.isCohomEquiv_of_le`,
  `New.Variety.relFreeAb.excision`: the exact sequence of a monomorphism, invariance under enlarging
  U′ to U when U′ is dense in U, and excision.
* `New.Variety.relFreeAb.exists_glued_class`: in the lowest degree where it may be nonzero, relative
  cohomology glues over a finite cover (a Mayer–Vietoris induction).
* `New.Variety.relFreeAb.prod`: the map of pairs that gives exterior products of relative classes.

Notions from other files:
* `New.Variety.isCohomEquiv_iff_subsingleton`, `New.Variety.isCohomEquiv_quotient_of_acyclic`: for
  0 → X₁ → X₂ → X₃ → 0 short exact, X₁ → X₂ is an equivalence for F exactly when all Ext^n(X₃, F)
  vanish, and X₂ → X₃ is one when all Ext^n(X₁, F) vanish.
* `New.Variety.pointMap`: The map h_A → Y from h_A = Hom(A,−) corresponding to a point y of Y(A) by
  the Yoneda lemma.

## Relation to the literature

Known; see `Lib.Cohomology.Etale.FilteredLimits` for sources.


### `relFreeAb.shortExact`

 For a subfunctor `U` of `V`, the sequence `0 → ℤ[U] → ℤ[V] → ℤ[V]/ℤ[U] → 0` (inclusion, then the
quotient map `π U`) is short exact. 

### `relFreeAb.isCohomEquiv_iff_subsingleton_rel`

 The inclusion `ℤ[U] → ℤ[V]` is an equivalence for `F` (bijective on all `Ext^n(·, F)`) exactly
when all the relative groups `H^n(V, U) = Ext^n(ℤ[V]/ℤ[U], F)` vanish. 

### `instance : HasFlatValues (freeAb V)`

 The free abelian groups `ℤ[V(A)]` are flat, being free. 

### `relFreeAb.mem_of_mk_mem`

 The classes of the generators `[y]` generate `ℤ[V(A)] / ℤ[U(A)]`. 

### `instance : HasFlatValues (relFreeAb U)`

 The groups `ℤ[V(A)]/ℤ[U(A)]` are flat: each is a direct summand of the free group `ℤ[V(A)]`. 

### `freeAb.prod`

 For set-valued functors X, Y, the map ℤ[X × Y] → ℤ[X] ⊗ ℤ[Y] sending [(x, y)] to [x] ⊗ [y]. 

### `instance : IsIso (freeAb.prod V V')`

 The map `ℤ[V × V'] → ℤ[V] ⊗ ℤ[V']`, `[(x, y)] ↦ [x] ⊗ [y]`, is an isomorphism. 

### `relFreeAb.mem_of_map_eq_zero`

 Let u: V' → V, φ: ℤ[V'] → N and S ⊂ N(A) a subgroup containing φ[x] − φ[y] when u(x) = u(y)
and φ[x] when u(x) ∈ U(A). Then φ maps the kernel of ℤ[V'(A)] → ℤ[V(A)]/ℤ[U(A)] into S. 

 ### Locally zero functors, locally bijective maps and the transfer 

### `zeroSection`

 The zero section of N: the subfunctor c ↦ {0} of the set-valued functor underlying N. 

### `locallyZero`

 The subgroup of locally zero elements of N(A): the s such that the maps A → B killing s form
a subfunctor of h_A that is dense for F. 

### `cohomology_eq_zero_of_locallyZero`

 If every section of N is locally zero for F (`New.Variety.locallyZero`), then Ext^n(N, F) = 0
for all n. 

### `isCohomEquiv_of_locallyZero`

 Let `α : M → N` be a map of functors from `C` to abelian groups. Call an element `s` of `M(c)`
locally zero for `F` if the maps `c → d` that kill `s` form a subfunctor of h_c that is dense for
`F`, meaning that its inclusion into h_c, pulled back along every point h_A → h_c, induces
bijections on all `Ext^n(−, F)`. If every section of the kernel of `α` is locally zero for `F`
(`h_ker`), and so is every section of its objectwise cokernel `abCoker α` (`h_coker`), then `α`
induces bijections on all `Ext^n(−, F)`. 

### `LocalIso.isCohomEquiv`

 `New.Variety.isCohomEquiv_of_locallyZero`, with its two hypotheses given as one conjunction. 

### `permutedPairs`

 The pairs `(w, w')` in a fibre of `p : V' → V` (points of `V' ×_V V'`) whose tuples `(f i w)ᵢ`
and `(f i w')ᵢ` agree up to a permutation of `ι`. 

### `exists_transfer_map`

 Transfer. Let `f i : V' → V''` (`i` in a finite type `ι`), `p : V' → V` and `p' : V'' → V`
satisfy `f i ≫ p' = p`. Then there are `Q` and `m : ℤ[V'] → Q`, `l : Q → ℤ[V]`, `ν : Q → ℤ[V'']`
with `m ≫ l = ℤ[p]`, `m ≫ ν = ∑ i, ℤ[f i]` and `ν ≫ ℤ[p'] = card ι • l`. Moreover `l` is an
equivalence for every `F` for which the image of `p` is dense in `V` and `permutedPairs f p` is
dense in `V' ×_V V'`. Here `permutedPairs f p` consists of the pairs `(w, w')` whose tuples
`(f i w)ᵢ` and `(f i w')ᵢ` agree up to a permutation of `ι`. 

### `map`

 For `u : V' → V` carrying `U'` into `U`, the induced morphism `ℤ[V']/ℤ[U'] → ℤ[V]/ℤ[U]`. 

### `shortExact_triple`

 For a monomorphism u: V' → V and a subfunctor U ⊂ V, the natural maps form a short exact
sequence 0 → ℤ[V']/ℤ[u⁻¹U] → ℤ[V]/ℤ[U] → ℤ[V]/ℤ[u(V') ∪ U] → 0 of functors to abelian
groups. 

### `isCohomEquiv_of_le`

 If U′ ≤ U are subfunctors of V and U′ is dense in U for F, then ℤ[V]/ℤ[U′] → ℤ[V]/ℤ[U] induces
bijections on Ext^n(·, F) for all n. 

### `excision`

 Excision: let u : V′ → V be a monomorphism, U′ = u⁻¹U, and u(V′) ∪ U dense in V for the
coefficient F. Then ℤ[V′]/ℤ[U′] → ℤ[V]/ℤ[U] induces bijections on Ext^n(·, F) for all n. 

 ## Gluing relative classes over a finite cover and products of pairs 

### `relFreeAb.restrict`

 For subfunctors U and A ⊆ B of V, the map ℤ[A]/ℤ[U ∩ A] → ℤ[B]/ℤ[U ∩ B]. 

### `relFreeAb.shortExact_restrict_of_inf_eq`

 For subfunctors `A`, `B` of `V` with `A ⊓ B = D`, the restriction and quotient maps form a short
exact sequence `0 → ℤ[D]/ℤ[U ∩ D] → ℤ[B]/ℤ[U ∩ B] → ℤ[B]/ℤ[(A ∪ U) ∩ B] → 0`. 

### `homOfLe_comp_homOfLe`

 The inclusion of `A` in `B` followed by that of `B` in `D` is the inclusion of `A` in `D`. 

### `relFreeAb.eq_zero_and_exists_glued_of_iSup`

 Gluing on the union of the `W i`. Let `S` be a set of subfunctors of `V`, closed under
intersection, whose members `A` have `H^n(A, U ∩ A) = 0` for `n < d`, and let the `W i` lie in `S`.
On the union `⨆ i, W i`: a class of degree `n ≤ d` that restricts to zero on every `W i` is zero;
and classes `x i` in `H^d(W i, U ∩ W i)` that agree on the intersections `W i ⊓ W j` are the
restrictions of one class. 

### `relFreeAb.exists_glued_class`

 Let `S` be a set of subfunctors of `V`, closed under intersection, whose members `A` have
`H^n(A, U ∩ A) = 0` for `n < d`. Let finitely many `W i` lie in `S`, with the union of `U` and the
`W i` dense for `F`. Then classes `x i` in `H^d(W i, U ∩ W i)` that agree on the intersections
`W i ⊓ W j` are the restrictions of one class in `H^d(V, U)`. 

### `relFreeAb.prod`

 For `U ⊆ V` and `W ⊆ X`, the map `ℤ[V × X] / ℤ[U × X ∪ V × W] → ℤ[V] / ℤ[U] ⊗ ℤ[X] / ℤ[W]` that
sends `[(v, w)]` to `[v] ⊗ [w]`. 
