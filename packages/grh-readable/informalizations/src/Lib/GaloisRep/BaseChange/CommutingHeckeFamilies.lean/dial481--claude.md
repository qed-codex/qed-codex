---
{
  "module": "src/Lib/GaloisRep/BaseChange/CommutingHeckeFamilies.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/CommutingHeckeFamilies.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/CommutingHeckeFamilies.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Steps E'/E of base change and commuting families of Hecke operators

This file sets up base change along an extension `E'/E` of prime degree. It records
place-by-place properties of base change `New.baseChangeGf` and of the Galois action
`New.galoisGf` on the finite adelic unitary group. It defines matching pairs of test functions at
the places above a set `S` of places. It relates operators on fixed vectors to functions on the
group through a common element of the group ring, and builds commuting families of local and
spherical Hecke operators.

## Main definitions and results

* `New.IsStep`: the extension `E'/E` with a character `μ` of the finite ideles of `E` that detects
  norms: `μ (z z̄) = 1` exactly when `z` is a principal idele times a norm from `E'`.
* `New.IsMatched`: the places of `E` that split completely in `E'` and at which `μ` is trivial.
* `New.placesAbove E' S`: the places of `E'` above `S ∪ S̄`; `New.IsMatchingPairAbove`: matching
  pairs of functions (`New.IsMatchingPair`) at these places.
* `New.IsLocalRetraction`, `New.isLocalRetraction_ofSplitPlace`: a group `A` that is a retract of
  the finite adelic unitary group at a set `S` of places; GL_n of the completion at a split place is
  one.
* `New.exists_isHeckeFunctionRelation`: the Hecke operators of `A` and spherical operators away from
  `S` commute on the vectors fixed by the level, and their products are operators of functions.

Notions from other files:
* `New.adeleNorm`: for an extension `L/K` of number fields, the norm from the finite adeles of `L`
  to the finite adeles of `K`, as a multiplicative map.
* `New.Gf.supportedOn`, `New.Gf.trivialOn`: the elements with component `1` at every place outside
  `S ∪ S̄`, and those with component `1` at every place of `S`.
* `New.localLevel`: the elements whose component at each `w ∈ S` lies in `K w`; by default `K w` is
  `New.localIntGL`, the integral matrices with integral inverse.

## Relation to the literature

Known; see `Lib.GaloisRep.BaseChange.PrimeDegreeTransfer` and `Lib.Adelic.Hecke.ClassSums` for
sources.



## Steps, compatible CM types and matched places

* `New.CMTypeOver`: a CM type of the larger field that restricts to the given one.
* `New.kerCompNorm`: the ideles of `E'` whose norm is killed by `μ`.


### `IsStep`

 A step `E'/E` with the character `μ` of the finite ideles of `E`: `E` contains a primitive root
of unity of order `5040`, and `E'` is a CM field Galois over `E` of prime degree. Some integer of
`E'` has trace `1`. The character `μ` has open kernel, is trivial on `E^×`, and `μ (z z̄) = 1`
exactly when `z` is a principal idele times a norm from `E'`. 

### `IsStep.isOpen_ker`

 The kernel of `μ` is open in the finite ideles of `E`. 

### `IsStep.apply_principal`

 `μ` is trivial on the principal ideles. 

### `IsStep.apply_norm_eq_one_iff`

 `μ (z z̄) = 1` exactly when `z` is a principal idele times the norm of a finite idele of
  `E'`. 

### `IsStep.exists_trace_eq_one`

 Some integer of `E'` has trace `1` down to `E`. 

### `CMTypeOver`

 A CM type of `L` that restricts to the given CM type of `K`: the embedding chosen at a place
extends the one chosen at the place below. 

### `CMTypeOver.eq_chosen_iff`

 An embedding of `L` is the one chosen at its place exactly when its restriction to `K` is the
  embedding chosen at the place below. 

### `kerCompNorm`

 The group of finite ideles of `E'` whose norm to `E` is killed by `μ`. 

### `IsMatched`

 The place `w` of `E` is matched: `μ` is trivial on `E_w^×`, and every place `u` of `E'` above
`w` has the same norm as `w` (`u.q = w.q`, the sizes of the residue fields; so `u` has residue
degree `1`) and is moved by every `σ ≠ 1`. 


## Base change and Galois action place by place

* `New.atPlace_galoisGf`, `New.atPlace_baseChangeGf`: local components;
  `New.baseChangeGf_mem_stdLevel`, `New.baseChangeGf_mem_supportedOn`: base change respects
  integrality and supports.

`g.atPlace w` is the component at `w`; `New.Gf.supportedOn n S` consists of the elements trivial
outside `S ∪ S̄`, `New.Gf.trivialOn n S` of those trivial on `S`; `New.idem S` is the indicator
adele of `S`.


 ### Places above `S` and local components 

### `placesAbove`

 The set of finite places of `E'` lying above a place of `S` or above the complex conjugate of a
place of `S`. 

### `atPlace_galoisGf`

 If `σ` pulls the place `u` back to `v`, the component of `σ g` at `u` is the image of the
component of `g` at `v` under `locMap σ h`, the map of completions given by `σ`, where
`h : u.comap σ = v`. 

### `IsMatchingPairAbove`

 The condition `New.IsMatchingPair` for `σ` on the finite adeles of `E'`, the degree `[E' : E]`,
the idempotent of the places above `S ∪ S̄`, the ideles killed by `μ ∘ Nm`, and the base change map
`New.baseChangeGf`. 

### `atPlace_baseChangeGf`

 The component of the base change of `g` at `u` is the image of the component of `g` at the
place below `u`. 

 ### Integrality and supports 

### `map_locMap_mem_intGL_iff`

 An invertible matrix over the completion at `w` is integral with integral inverse exactly when
its image at a place `u` above `w` is, under `locMap f h` with `h : u.comap f = w` (`v.integer`: the
valuation ring of `Valued.v`). 

### `idem_smul_eq_iff_mem_trivialOn`

 `g` agrees with the identity matrix after multiplication by the idempotent of `S` exactly when
its components at the places of `S` are `1`. 


## Operators on fixed vectors coming from one group ring element

Bookkeeping for the trace formula. For a representation `π` of `G` and a subgroup `K`,
`New.IsOperatorOf π K T f` says that the operator `T` on the `K`-fixed vectors and the function `f`
on `G` come from one element `a` of the group ring: `T` is the action of `a`, and `f` is read from
its image `New.Variety.cosetFn K a` in `ℂ[G ⧸ K]`.


### `Variety.leftTranslation`

 The left regular representation of `G` on functions `G → ℂ`: `(g • F) x = F (g⁻¹ * x)`. 

### `IsOperatorOf`

 There is `a` in the group ring such that `f g` is the coefficient of `gK` in the image of `a` in
`ℂ[G ⧸ K]`, and `T` is the action of `a` on the `K`-fixed vectors. So `f` is right `K`-invariant
and nonzero on finitely many cosets, and `T` is the operator `∑ g ∈ G ⧸ K, f g • π g`. 

### `IsOperatorOf.heckeFun_mul`

 Let `a : G' →* G` and let `F` live on finitely many cosets of `J`. If `T` is the operator of
`f`, then the Hecke sum `∑ q : G' ⧸ J, F q • π (a q)` composed with `T` is the operator of the
function `φ` obtained from `f` by the same sum of left translations. The hypothesis `s` says that
the Hecke sum keeps the `K`-fixed vectors. 


## Local retracts and commuting families of Hecke operators

* `New.exists_isHeckeFunctionRelation`: commuting local and spherical Hecke operators on the vectors
  fixed by the level, with the functions of their products.
* `New.exists_remaining_places`: the places not above `S ∪ S̄` are cut into those above `T ∪ T̄`,
  where the level is maximal, and the rest.


### `IsLocalRetraction`

 The group `A` is a retract of the finite adelic unitary group at `S`: the homomorphism `a` maps
`A` into the elements supported on `S ∪ S̄`, `r ∘ a` is the identity, and the kernel of `r` consists
of the elements trivial at the places of `S`. 

### `HeckeCommute`

 The Hecke operators of `φ` and `ψ` commute on the `L`-fixed vectors. 

### `IsHeckeProduct`

 On the `L`-fixed vectors, the Hecke operator of `φ` composed with that of `ψ` is the Hecke
operator of `χ`. 

### `heckeFamily`

 The local Hecke operators of the functions `F j` on `A` at level `L₀`, indexed by `j`, together
with the spherical operators at the split places `u x`, indexed by `(x, i)`:
`heckeSplit π (hu x) i`, the Hecke operator of the indicator of `basicDoubleCoset n (u x) i` at
level `localIntGL n (u x)`. 

### `IsCommutingHeckeFamily`

 Fixed by `L` means fixed by `L₀` and by the part of `L` that is trivial on `S`. `A` preserves
the vectors fixed by that part and commutes with the spherical operators. The operators of
`New.heckeFamily` preserve the `L`-fixed vectors and commute there. 

### `IsCommutingHeckeFamily.levelSpace_eq`

 Fixed by `L` means fixed by `L₀` and by the part of `L` that is trivial on `S`. 

### `IsCommutingHeckeFamily.apply_mem`

 `A` preserves the vectors fixed by the part of `L` that is trivial on `S`. 

### `IsCommutingHeckeFamily.commute_heckeSplit`

 `A` commutes with the spherical operators. 

### `IsCommutingHeckeFamily.heckeFamily_mem`

 The operators of the family preserve the `L`-fixed vectors. 

### `IsCommutingHeckeFamily.commute_restrict`

 The operators of the family commute on the `L`-fixed vectors. 

### `IsHeckeFunctionRelation`

 Let `family` be operators on the `L`-fixed vectors, indexed as in `New.heckeFamily`. The
relation `R k t φ` records operators `t` of the functions `(F k ∘ r) · φ · 1_C`. It holds for the
local operator of index `k` with `φ = 1_B`. Composing `t` with the local operator of index `i`
changes `k` to `j`, if the operator of `F i` composed with that of `F k` is that of `F j`. Composing
`t` with a spherical operator at `u x` applies it to `φ`, if the elements supported at `u x` lie in
`C`. 

### `IsHeckeFunctionRelation.base`

 The local operator of index `k` is related to the indicator of `B`. 

### `IsHeckeFunctionRelation.isOperatorOf`

 A related `t` is the operator of the function `(F k ∘ r) · φ · 1_C`. 

### `IsHeckeFunctionRelation.local_mul`

 Composing with the local operator of index `i` changes `k` to `j`, if the operator of `F i`
  composed with that of `F k` is that of `F j`. 

### `IsHeckeFunctionRelation.spherical_mul`

 Composing with a spherical operator at `u x` applies it to `φ`, if the elements supported
  at `u x` lie in `C`. 

### `isCommutingHeckeFamily_of_isLocalRetraction`

 Let `A` be a retract at `S`, and let `L ≤ New.stdLevel` be the level given by `L₀` through `r`
and by a subgroup `N` that contains the image of `a`. Let `F j` be `L₀`-bi-invariant functions with
commuting operators, and let `u x` be split places off `S ∪ S̄` where `L` is maximal. Then
`New.IsCommutingHeckeFamily` holds. In particular, the local and the spherical operators act on the
`L`-fixed vectors and commute. 

### `exists_isHeckeFunctionRelation`

 Let `A` be a retract at `S`, and let `L ≤ New.stdLevel` be `L₀.comap r ⊓ (B ⊓ C)`, where `a`
maps `A` into `B ⊓ C`. Let `F j` be `L₀`-bi-invariant functions with commuting operators, and let
`u x` be split places off `S ∪ S̄` where `L` is maximal. Then `New.IsCommutingHeckeFamily` holds, so
the local and the spherical operators act on the `L`-fixed vectors and commute. Also, some `R`
satisfies `New.IsHeckeFunctionRelation` for the restricted operators. That is, `R k t φ` records
operators `t` of the functions `(F k ∘ r) · φ · 1_C`, holds for the local operator of index `k` with
`φ = 1_B`, and is carried along by composing with local and spherical operators. 

### `isLocalRetraction_ofSplitPlace`

 Let `u` be the only place of `E'` above `w`, both split. Then (a) `GL_n(E_w)` is a retract at
`{w}` (`New.IsLocalRetraction`), (b) `GL_n(E'_u)` is a retract at the places above `w` and its
conjugate, and (c) an element is integral at these places iff its component at `u` is integral. 

### `Gf.supportedOn_le_trivialOn`

 If no place of `T` lies in `S` or in its conjugate, the elements supported on `S ∪ S̄` are
trivial at the places of `T`. 

### `exists_remaining_places`

 Let `T` avoid `S ∪ S̄`, and let the level `K` be maximal at the places above `T ∪ T̄`. Then
there is a set `Y` of places of `E` with these properties. (a) The places of `E'` above `T ∪ T̄`
and those above `Y ∪ Ȳ` are disjoint. (b) Elements supported above `T ∪ T̄` lie in the
level `K` above `Y`. (c), (d) Together the places above `T` and above `Y` are the places not above
`S ∪ S̄`, as sets and as idempotents. (e) The level `K` off `S` is the maximal level above `T`
intersected with `K` above `Y`. 
