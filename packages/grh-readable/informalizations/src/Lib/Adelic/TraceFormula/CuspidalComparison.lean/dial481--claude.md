---
{
  "module": "src/Lib/Adelic/TraceFormula/CuspidalComparison.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/CuspidalComparison.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/CuspidalComparison.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Comparison of traces for a cuspidal test function

The comparison of traces `trace_comparison` asks for a test function that is cuspidal at a split
place `w` and is supported at a second place on elements whose characteristic polynomial has a
simple zero at `0` modulo that place. The second condition is removed here: at an auxiliary split
place `v` the level is cut down to the stabiliser of a line, where `T⁺ = lineHecke` forces the
simple zero and counts the spherical vectors through its determinant (`trace_eq_of_isCuspidalAt`).

## Relation to the literature

Known; see `Lib.Adelic.TraceFormula.TraceComparison` for sources.


### `eventually_mem_spanOn_atPlace_mem_localIntGL`

 An element `a` of the group algebra of the finite adelic group is integral at almost all places
`v`: it is a combination of group elements whose component at `v` lies in
`localIntGL n v = GL_n(O_v)`. 

### `exists_auxiliary_place`

 The auxiliary place: let `E` contain the 5040th roots of unity. For an open subgroup `K`, an
element `a` of the group algebra and a place `w`, some split place `v` is neither `w` nor its
conjugate, `K` contains `maxCompactAt n v` (the integral elements that are `1` away from `v` and its
conjugate), and `a` is a combination of elements that are integral at `v`. 

### `trace_eq_of_isCuspidalAt`

 Comparison of traces without the condition at a second place. Let the CM field `E` contain the
5040th roots of unity and have an even number of infinite places, let `V`, `V'` be hermitian spaces
of rank `N = card n ≥ 2` over `E` with signs `s`, `s'`, and let `l = 2λ` be a doubled Harish-Chandra
parameter whose `toHCParam s (l v)` and `toHCParam s' (l v)` have gap at least `500 N³ + 10 N⁵` at
every infinite place `v` (`HasLargeGap A` means gap `500 N³ + A`). Let `K` be a level (`IsLevel K`,
so `K` is open and compact), let `a` keep the `K`-fixed vectors in every representation
(`universalLevelAlgebra K`), and let the test function `a ⋆ 1_K` (`convIndicator`) be cuspidal at a
split place `w`. Then operators that act as `a` on the forms of parameter `l` and level `K`
(`levelSpace` of `formRep` at `typeKernel l s`, resp. `typeKernel l s'`, which the gap bound makes a
cusp kernel by `isCuspKernel_typeKernel`) on `V` and on `V'` have the same trace. 
