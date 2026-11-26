---
{
  "module": "src/Lib/Adelic/TraceFormula/LevelCut.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/LevelCut.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/LevelCut.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Passage to the stabiliser of a line at an auxiliary place

Let `w` be a split place at which the level `K` is maximal, and let `K'` be the level that is the
stabiliser `J` of a line at `w` and agrees with `K` elsewhere. On the vectors of level `K'` of a
representation, an operator `A` that comes from the places off `w` commutes with the operators `T⁺`,
`T⁻` of `J`, and the mean `e` over `GL_n(𝒪_w)` projects onto the vectors of level `K`. If the
representation is unitary and the vectors of level `K'` form a finite-dimensional space, then the
traces of the `A ^ l * T⁺ ^ m`, `l, m ≥ 1`, at level `K'` determine the trace of `A` at level `K`
(`trace_eq_of_trace_cutLevel_eq`).

Notions from other files:
* `levelSpace ρ K`: the vectors of the representation `ρ` that are fixed by `K`; `levelAlgebra ρ K`:
  the elements of the group algebra that map this space to itself.
* `Gf E n`: the group of finite-adelic unitary elements, whose component at `w` is `g.atPlace w` in
  `GL n (LocField w)`; `localIntGL n w`: the group `GL_n(𝒪_w)`; `stdLevel E n`: the finite-adelic
  unitary elements that are integral at every place; `maxCompactAt n w`: those elements of
  `stdLevel E n` that are trivial away from `w` and its conjugate.
* `ofSplitPlace hw x`: the finite-adelic unitary element with component `x` at the split place `w`;
  `offPlace hw g`: the part of `g` away from `w` and its conjugate.
* `lineStabilizer w i`: the stabiliser in `GL_n(𝒪_w)` of the `i`-th coordinate line modulo `w`;
  `lineHecke w i` and `lineHeckeLower w i` act as its Hecke operators `T⁺` and `T⁻`.
* `LineRelation d c A T⁺ T⁻ e`: `T⁻` is adjoint to `T⁺`, `T⁺ T⁻ = d (1 + c e)`, `e` is idempotent,
  `A` commutes with `T⁺` and `T⁻`, and `d, c > 0`.


### `cutLevel`

 The part of `K` whose component at `w` lies in `J`. 

### `isLevel_cutLevel_lineStabilizer`

 The cut of a level by the stabiliser of a line at `w` is again a level: it is open and lies in
`stdLevel E n`, the subgroup of elements that are integral at every place. 

### `commute_offPlace_ofSplitPlace`

 The part of `g` off the split place `w` commutes with every element supported at `w`. 

### `ofSplitPlace_mem_of_maxCompactAt_le`

 If `K` contains the maximal compact subgroup at the split place `w`, it contains the image of
`GL_n(𝒪_w)` under `ofSplitPlace`. 

### `offRep`

 The action of an element through its part off `w`. 

### `localRep`

 The action of the group at `w`. 

### `apply_eq_offRep_localRep`

 An element acts as its component at `w` followed by its part off `w`. 

### `commute_offRep_localRep`

 The action of an element off `w` commutes with the action of the group algebra at `w`. 

### `commute_localRep_offRep`

 The action of an element at `w` commutes with the action of the group algebra through the parts
off `w`. 

### `asAlgebraHom_offRep_apply`

 Let `a` be a combination of group elements whose components at the split place `w` lie in
`GL_n(𝒪_w)`. On vectors that are spherical at `w` (fixed by the maximal compact subgroup there),
`a` acts through its part off `w`. 

### `cutInclusion`

 The inclusion of the vectors of level `K` in those of the level that is cut down to the
stabiliser of the `i`-th coordinate line at `w`. 

### `mem_levelSpace_cutLevel_iff`

 If `K` contains the maximal compact subgroup at the split place `w` and `J ≤ GL_n(𝒪_w)`, a
vector is fixed by the cut level `{k ∈ K | k_w ∈ J}` exactly when it is fixed by the part of `K`
off `w` and by `J` acting at `w`. 

### `mem_levelSpace_iff_offRep_localRep`

 If `K` is maximal at `w`, a vector is fixed by `K` exactly when it is fixed by the part of `K`
off `w` and by `GL_n(𝒪_w)`. 

### `offAction`

 The elements of the group algebra that map the space of vectors fixed by the part of `K` off
`w` to itself act on the vectors of the cut level through their parts off `w`. 

### `localAction`

 The elements of the group algebra at `w` that map the space of vectors fixed by `J` to itself
act on the vectors of the cut level. 

### `coe_offAction_apply`

 On the vectors of the cut level, `offAction` of `a` is the action of `a` through the parts off
`w`. 

### `coe_localAction_apply`

 On the vectors of the cut level, `localAction` of `u` is the action of `u` at `w`. 

### `commute_offAction_localAction`

 On the vectors of the cut level, the operators from the parts off `w` commute with those from
the component at `w`. 

### `coe_offAction_mul_localAction_apply`

 Let `a` map the vectors fixed by the part of `K` off `w` to themselves, and `u` those fixed by
`J` at `w`. On the cut level, the operator of `a` times that of `u` is the action of the product of
the images of `u` under `ofSplitPlace` and of `a` under `offPlace`. 

### `raiseAt`

 The operator `T⁺` at `w` on the vectors whose level is the stabiliser of the `i`-th coordinate
line at `w` and `K` elsewhere. 

### `lowerAt`

 The operator `T⁻` at `w` on the vectors whose level is the stabiliser of the `i`-th coordinate
line at `w` and `K` elsewhere. 

### `meanAt`

 The mean over `GL_n(𝒪_w)`, from the level that is cut at `w` to the level `K`. 

### `coe_raiseAt_apply`

 `raiseAt` is the restriction of the operator `T⁺ = lineRaise` of the representation at `w`. 

### `coe_lowerAt_apply`

 `lowerAt` is the restriction of the operator `T⁻ = lineLower` of the representation at `w`. 

### `coe_cutInclusion_meanAt_apply`

 `meanAt`, followed by the inclusion of the vectors of level `K`, is `sphericalMean`, the mean
over `GL_n(𝒪_w)`. 

### `meanAt_comp_cutInclusion`

 If `K` contains the maximal compact subgroup at the split place `w`, the mean over `GL_n(𝒪_w)`
fixes the vectors of level `K`: `meanAt` is a left inverse of the inclusion `cutInclusion` of these
vectors in those of the level cut by the stabiliser of the `i`-th coordinate line at `w`. 

### `trace_offAction_mul_mean`

 Let `K` contain the maximal compact subgroup at the split place `w`, and let the vectors of the
level cut by the stabiliser of a line at `w` form a finite-dimensional space. Let `a` map the space
of vectors fixed by the part of `K` off `w` to itself, let `A` and `T` be its actions through the
parts off `w` at the cut level and at level `K`, and let `e` be the mean over `GL_n(𝒪_w)`
(`meanAt` followed by the inclusion `cutInclusion`). Then `A * e` and `T` have the same trace. 

### `coe_offAction_pow_mul_raiseAt_pow_apply`

 Let `K` contain the maximal compact subgroup at the split place `w` and let `a` map the space of
vectors fixed by the part of `K` off `w` to itself. On the level cut by the stabiliser of the `i`-th
coordinate line at `w`, the `l`-th power of the operator of `a` times `(T⁺) ^ m` (`T⁺ = raiseAt`)
is the action of the group algebra element obtained from `lineHecke w i ^ m` by `ofSplitPlace`
(placing it at `w`), times the one obtained from `a ^ l` by `offPlace` (taking the part off `w`). 

### `lineRelation_offAction`

 Let `K` contain the maximal compact subgroup at the split place `w`, whose residue field has
`q` elements, and let `a` map the vectors fixed by the part of `K` off `w` to themselves. In a
unitary representation, on the level cut by the stabiliser of a line at `w`, the operator `A` of
`a`, the operators `T⁺`, `T⁻` and the mean `e` over `GL_n(𝒪_w)` satisfy `LineRelation d c` with
`d = q ^ (n - 2)` and `c = q ^ n - 1`: `T⁻` is adjoint to `T⁺`, `T⁺ T⁻ = d (1 + c e)`, `e` is
idempotent, and `A` commutes with `T⁺` and `T⁻`. 

### `trace_eq_of_trace_cutLevel_eq`

 Let the level `K` contain the maximal compact subgroup at the split place `w`, and let `a` be
in `universalLevelAlgebra K` (it maps the space of `K`-fixed vectors to itself in every
representation) and be a combination of elements that are integral at `w`. Consider two unitary
representations whose spaces of vectors of level `K'`, the level cut by the stabiliser of a line at
`w`, are finite-dimensional. Suppose that for all `l`, `m` the element
`b = (T⁺) ^ (m + 1) * a' ^ (l + 1)` of the group algebra, with `T⁺ = lineHecke w i` placed at `w`
and `a'` the part of `a` off `w`, has the same trace in both at level `K'` (`h_trace`, where `S`,
`S'` are the two operators by which `b` acts there). Then `a` has the same trace at level `K` in
both. 
