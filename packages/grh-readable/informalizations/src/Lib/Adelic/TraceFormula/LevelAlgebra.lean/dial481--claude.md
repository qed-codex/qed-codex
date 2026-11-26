---
{
  "module": "src/Lib/Adelic/TraceFormula/LevelAlgebra.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/LevelAlgebra.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/LevelAlgebra.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The elements of a group algebra that keep a level

For a representation `ρ` of a group `G` and a subgroup `K`, the elements of the group algebra
`ℂ[G]` that map `K`-fixed vectors to `K`-fixed vectors form an algebra, and it acts on the
`K`-fixed vectors.

Notions from other files:

* `levelSpace ρ K`: the subspace of the vectors that `ρ k` fixes for every `k ∈ K`.

## Relation to the literature

Known result: the elements of a group algebra that keep the vectors fixed by a subgroup, and their
action on these vectors. The related class sums are in `Lib.Adelic.Hecke.ClassSums`.


### `asAlgebraHom_mapDomain`

 Pushing an element of `H`'s group algebra forward along `f : H →* G` and letting it act by `ρ`
is letting it act by the restricted representation `ρ ∘ f`. 

### `commute_asAlgebraHom`

 An operator that commutes with the group commutes with the group algebra. 

### `levelAlgebra`

 The elements of the group algebra that map `K`-fixed vectors of `ρ` to `K`-fixed vectors. 

### `levelAction`

 The action of `levelAlgebra ρ K` on the `K`-fixed vectors. 

### `coe_levelAction_apply`

 The operator `levelAction ρ K a` sends a `K`-fixed vector `y` to `ρ.asAlgebraHom a y`. 

### `universalLevelAlgebra`

 The elements of the group algebra that keep the `K`-fixed vectors in every representation of
`G` on a complex vector space in `Type`. 

### `mem_universalLevelAlgebra`

 An element of `ℂ[G]` lies in `universalLevelAlgebra K` iff, for every representation `ρ` of `G`
on a complex vector space in `Type`, it lies in `levelAlgebra ρ K`, i.e. keeps the `K`-fixed
vectors. 

### `universalLevelAlgebra_le`

 For every representation `ρ` of `G` on a complex vector space in `Type`, the algebra
`universalLevelAlgebra K` is contained in `levelAlgebra ρ K`. 
