---
{
  "module": "src/Lib/Adelic/Unitary/ComponentsAndBlockSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/ComponentsAndBlockSums.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/ComponentsAndBlockSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Components of unitary adelic points at places; sums and moves of hermitian spaces

Elements of the finite adelic unitary group `New.Gf` of a CM field are studied through their
components `g.atPlace w`. The component at `w̄` is determined by the one at `w`, and is `1` exactly
when that one is, so supports have the form `S ∪ S̄`. Elements are cut along the idempotent
`New.idem` of a set of places. A hermitian space with a point `New.Space E n s` is a matrix `J` over
`E` together with `x` in `GL n (𝔸 E)` such that `xᴴ J x` is the diagonal matrix of the signs `s` at
infinity and `1` at the finite places.

## Main definitions and results

* `New.Gf.componentOn`: keeps the components at `S ∪ S̄` and replaces the others by `1`.
* `New.Gf.exists_supportedOn_mul_trivialOn`: splitting into a part supported on `S ∪ S̄` and one
  trivial there.
* `New.Gf.mem_of_stdLevel_le_of_supportedOn_le`: `New.stdLevel` and the elements supported at one
  pair `w, w̄` generate the group.
* `New.range_ofSplitPlace`, `New.ofSplitPlaces`: elements with prescribed components at split
  places.
* `New.U.sum`, `New.G.sum`, `New.Space.sum`: block diagonal sums.
* `New.G.neg`, `New.Space.neg`: passing from signs `s` to `-s` (and from `J` to `-J`).
* `New.signedSpace`: the standard space with matrix `diag(s)`.

Notions from other files:
* `New.idem`: The finite adele with component 1 at the places of a set and 0 elsewhere.
* `New.ofSplitPlace`: For a split place w, the homomorphism GL_n(E_w) → G_f sending g to the unitary
  element with component g at w and 1 off w, w̄.
* `New.G`: The adelic unitary group G = G_∞ × G_f (an element `g` has adelic matrix `g.adeleMatrix`)
  for signs s at the infinite places and the identity matrix at the finite places.
* `New.stdForm`: The diagonal adelic matrix that is diag(s) at infinity and 1 at the finite places.



## Components at sets of places and elements at split places

Conventions: `star` is complex conjugation, on places too; `New.Gf.supportedOn` is the subgroup
trivial outside `S ∪ S̄` and `New.Gf.trivialOn` the one trivial on `S`; `New.localIntGL` is
`GL_n(O_w)`, and `New.stdLevel` is the subgroup of `New.Gf` of integral matrices with integral
inverse.


### `map_evalAt_cutGL`

 For a set `S` of places, cutting `g` along the idempotent of `S` (`cutGL`) keeps the component
`g.map (evalAt w)` at `w` if `w ∈ S` and replaces it by `1` otherwise. 

### `mem_intGL_Ô`

 A matrix over the finite adeles lies in `intGL n (Ô E) = GL_n(Ô)` (entries of `g` and `g⁻¹` in
`Ô`), where `Ô` is the ring of integral finite adeles, if and only if its component at each place
`w` lies in `localIntGL n w = GL_n(O_w)`. 

### `_root_.Set.conjClosure`

 The set S ∪ S̄ of the finite places in S and their complex conjugates. 

### `_root_.Set.IsConjDisjoint`

 The set S of finite places is disjoint from its complex conjugate: its places are not
self-conjugate, and it holds at most one place of each conjugate pair. 

 ### Integrality and supports in the unitary group 

### `Gf.atPlace_star`

 For a unitary adelic matrix `g` and places with `ū = w`, the component at `w` is the
transpose of the conjugate (`conjLoc`, carrying `E_u` to `E_w`) of the inverse of the component
at `u`. 

### `Gf.eventually_atPlace_mem_localIntGL`

 The component of an element of the finite adelic unitary group lies in
`localIntGL n w = GL_n(O_w)` for all but finitely many places `w`. 

### `mem_stdLevel_iff`

 An element lies in the integral subgroup `stdLevel` if and only if each of its components lies
in `localIntGL n w = GL_n(O_w)`. 

### `Gf.atPlace_star_mem_iff`

 By unitarity, the component at `w̄` is integral if and only if the component at `w` is. 

### `Gf.mem_supportedOn`

 `g` is supported on `S ∪ S̄` if and only if its component is `1` at every place `w` with
neither `w` nor `w̄` in `S`. 

### `Gf.atPlace_star_eq_one_iff`

 By unitarity, the component at `w̄` is `1` if and only if the component at `w` is. 

### `Gf.atPlace_eq_one_or`

 If `g` is supported on `S ∪ S̄` and `k` is trivial on `S`, one of them is `1` at each place. 

### `Gf.supportedOn_compl`

 The elements supported outside `S ∪ S̄` are those whose components at the places of `S`
are `1`. 

### `Gf.commute_supportedOn_trivialOn`

 An element supported on `S ∪ S̄` commutes with one that is trivial on `S`. 

### `Gf.eq_of_supportedOn`

 Two elements supported on `S ∪ S̄` that agree at the places of `S` are equal. 

### `Gf.mem_stdLevel_iff_of_supportedOn`

 An element supported on `S ∪ S̄` is integral if and only if its components at the places
of `S` are integral. 

 ### The part supported on `S ∪ S̄`, and generation by local elements 

### `Gf.componentOn`

 The endomorphism of the finite adelic unitary group that keeps the components at the places
of S ∪ S̄ and replaces the others by 1. 

### `Gf.exists_supportedOn_mul_trivialOn`

 Every `g` in the finite adelic unitary group is a product `a * b` with `a` supported on `S ∪ S̄`
and `b` trivial at the places of `S`, such that `a` and `b` lie in the integral subgroup `stdLevel`
whenever `g` does. 

### `Gf.mem_of_stdLevel_le_of_supportedOn_le`

 A subgroup `H` of the finite adelic unitary group that contains the integral subgroup `stdLevel`
and, for every finite place `w`, all elements supported on `{w, w̄}` contains every element of the
group. 

 ### Split places 

### `atPlace_ofSplitPlace_of_ne`

 For a place `w ≠ w̄`, the component of `ofSplitPlace hw g` (the unitary element with component
`g` at `w`) at a place other than `w` and `w̄` is `1`. 

### `range_ofSplitPlace`

 For a finite place `w` of the CM field `E` with `w̄ ≠ w`, the image of the homomorphism
`ofSplitPlace hw` from `GL_n(E_w)` to the finite adelic unitary group, which sends `g` to the
element with component `g` at `w` and `1` off `w, w̄`, is the subgroup `supportedOn n {w}` of
elements with component `1` at every place other than `w` and `w̄`. 

### `ofSplitPlace_mem_stdLevel`

 For a split place `w`, the element `ofSplitPlace hw g` is integral if and only if
`g ∈ localIntGL n w = GL_n(O_w)`. 

### `continuous_ofSplitPlace`

 For a split place `w`, the embedding `ofSplitPlace hw` of `GL_n(E_w)` into the finite adelic
unitary group is continuous. 

### `ofSplitPlaces`

 For a finite set `S` of finite places disjoint from `S̄`, the homomorphism sending a family
`(g_w)` in `∏ w ∈ S, GL_n(E_w)` to the unitary element with component `g_w` at each `w` in `S`
and `1` off `S ∪ S̄`. 

### `atPlace_ofSplitPlaces`

 For a finite set `S` of places of the CM field `E` disjoint from `S̄` and a family
`g w ∈ GL_n(E_w)` for `w` in `S`, the component at `w ∈ S` of the finite adelic unitary element
`ofSplitPlaces hS g` (the product of the elements `ofSplitPlace _ (g w)` concentrated at `w, w̄`) is
`g w`. 

### `ofSplitPlaces_mem_supportedOn`

 For a finite set `S` of places disjoint from `S̄`, the finite adelic unitary element
`ofSplitPlaces hS g` with component `g w` at each `w ∈ S` is `1` at every place outside `S ∪ S̄`. 

### `ofSplitPlaces_mem_stdLevel`

 For a finite set `S` of places disjoint from `S̄`, the element `ofSplitPlaces hS g` with
component `g w` at each `w ∈ S` lies in the integral subgroup `stdLevel E n` if and only if every
`g w` lies in `localIntGL n w = GL_n(O_w)`. 


## Constructions on hermitian spaces with a point

Negation of spaces and the standard spaces need an element of norm `-1` in the integral finite
adeles (`New.Weil.normNegOne`), which exists under the hypothesis `New.HasPrimitiveRoot5040`: the
field contains a primitive root of unity of order `5040`.


 ### Sign matrices, and blocks and reindexing over a ring 

### `blockGL`

 The homomorphism GL_m(R) × GL_n(R) → GL_{m+n}(R) sending (g, h) to the block diagonal matrix
diag(g, h). 

### `signMatrix_sum`

 The block diagonal sum of the sign matrices `signMatrix s = diag(s)` and `signMatrix t` of s and
t is that of the concatenated signs. 

### `reindexGL`

 For a bijection e of index sets, the isomorphism GL_m(R) ≅ GL_n(R) relabelling rows and
columns along e. 

### `U.sum`

 The block embedding `U J × U J' → U J''`, `(g, h) ↦ diag(g, h)`, where `J''` is the block
diagonal sum of `J` and `J'`. 

### `U.blockSumOne`

 The block diagonal homomorphism U_m(R) × U_n(R) → U_{m+n}(R), (g, h) ↦ diag(g, h), between
the unitary groups of identity matrices. 

### `U.reindex`

 Renaming the basis by `e` identifies the unitary group of `J` with that of the form `J'`
obtained from `J` by the same renaming of rows and columns. 

### `U.block`

 The block diagonal embedding U(1_m) × U(1_l) → U(1_n) of unitary groups of identity
matrices, along a bijection of the disjoint union of m and l with n. 

### `U.block_val`

 The matrix of the image of a pair `g = (g₁, g₂)` of unitary matrices (`New.U J` is the unitary
group of the form `J`) under `New.U.block e` is diag(g₁, g₂) with rows and columns relabelled
along `e`. 

 ### The adelic unitary groups 

### `G.sum`

 The block diagonal embedding of the product of the adelic unitary groups for signs s and t
into the one for the concatenated signs. 

### `G.adeleMatrix_sum`

 The adelic matrix (`New.G.adeleMatrix`) of the block sum of g₁ and g₂ is diag(g₁, g₂). 

### `G.neg`

 The isomorphism between the adelic unitary groups for signs s and −s that is the identity on
matrices, since U(J) = U(−J) at each infinite place. 

### `stdForm_sum`

 The standard adelic forms for signs s and t have as block diagonal sum the standard form for
the concatenated signs. 

### `gram_mkAdelicGL`

 If `a w` carries `J`, embedded in `ℂ` by the CM type, to the diagonal matrix of signs `s` at
each infinite place `w` and `b` carries `J` to `1` over the finite adeles, then the adelic matrix
with components `a` and `b` (`New.mkAdelicGL`) carries `J` to the standard form. Here `Φ w` is
the embedding of `E` chosen at `w` and `toAdele` is the diagonal embedding of `E`. 

### `G.reindex`

 For a bijection of index sets carrying signs s to signs t, the isomorphism of the
corresponding adelic unitary groups relabelling rows and columns in every component. 

 ### A unit of norm `-1` and the standard spaces 

### `Weil.normNegOne`

 For a field `E` with a primitive root of unity of order 5040, a chosen element ε of Ô with
ε̄ε = −1, as a unit with inverse −ε̄. It exists by `New.exists_unit_star_mul_self_eq`. 

### `normNegOneIdele`

 The idele that is 1 at the infinite places and whose finite part is the unit
ε = `New.Weil.normNegOne` of Ô, with ε̄ε = −1. 

### `signedSpace`

 If `E` contains a primitive root of unity of order 5040, the standard space with matrix
diag(s). Its point is diagonal, with entry 1 where s_i = 1 and `normNegOneIdele E` (the idele
with finite part of norm −1) where s_i = −1. 

 ### Operations on spaces 

### `sum`

 For spaces V, W with signs s, t, the space with concatenated signs whose matrix and point
are the block diagonal sums of those of V and W. 

### `reindex`

 For a space V with signs s and an index bijection carrying s to t, the space with signs t
obtained by relabelling its matrix and point. 

### `neg`

 If `E` contains a primitive root of unity of order 5040 and (J, x) is a space with signs s,
the space with signs −s, matrix −J and point x multiplied by the scalar `normNegOneIdele E`, the
idele that is 1 at infinity and whose finite part has norm −1. 

### `move`

 For a space (J, x) and g in G, the space (J, xg): the same matrix with the point moved by g. 
