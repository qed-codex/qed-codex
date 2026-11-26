---
{
  "module": "src/Lib/GaloisRep/BaseChange/CongruenceLevelMatching.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/CongruenceLevelMatching.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/CongruenceLevelMatching.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Matching unit pairs at congruence levels and at unramified places of a step

This file concerns base change along a step `E' / E` (`New.IsStep`): an extension of prime degree
with a character `μ` of the finite ideles of `E`. It constructs levels at which the unit functions
match in the sense of `New.IsMatchingPair`.

## Main definitions and results

* `New.cocyclesSplit_and_isMatchingPair_of_congruence`: at a principal congruence level over a
  profinite ring with tame action, the cocycles split and the indicator functions of the level form
  a matching pair.
* `New.IsStepUnramifiedAt`: `w` is unramified in `E'`, and `μ ∘ Nm` kills the local units above `w`.
* `New.exists_isTameAtLevel_intAdeleMap`: `σ ≠ 1` is tame (`New.IsTameAtLevel`) on the integral
  adeles of `E'` at every `σ`-fixed level that vanishes at the totally ramified places dividing a
  fixed integer `C`.
* `New.exists_isBaseChangeLevel`: below any open subgroup `H` over `E` there are local levels over
  `E'` whose groups above any set of places are `σ`-stable, have split cocycles, and carry matching
  indicator functions.

Notions from other files:
* `New.IsTameAtLevel`: the conditions on a ring endomorphism `τ` with `τ ^ p = 1` and a level `m`
  under which descent works.
* `New.CocyclesSplit`: every `s` in `K` of twisted norm `1` under `τ` is a coboundary `t * (τ t)⁻¹`
  on the support of `u`, for some `t ∈ K` that is `1` off it.
* `New.IsMatchingPair`: a function `f` and a twisted function `φ` match, one characteristic
  polynomial at a time, through a polynomial root (`New.IsNormRoot`).
* `New.localLevel`: the elements of `New.Gf E n` whose component at each place of a set `S` lies in
  a given local group, by default `GL_n` of the local integers, with no condition outside `S`.

## Relation to the literature

Known; see `Lib.GaloisRep.BaseChange.PrimeDegreeTransfer` for sources.



## Matching pairs at a congruence level over a profinite ring

The main lemma, `New.cocyclesSplit_and_isMatchingPair_of_congruence`, is the local input to the
comparison of trace formulas in base change at places with a principal congruence level.


### `New.charpoly_map_eq_self_of_smul_sub_one`

 If `ι Y = v • (g - 1)` with `ι` injective, `ι` carries `τ` to `σ`, and `σ` fixes `v` and the
characteristic polynomial of `g`, then `τ` fixes the characteristic polynomial of `Y`. 

### `New.exists_det_one_add_smul_eq`

 Let `O` be integrally closed in `R`, and let `-C` be a matrix over `R` killed by a monic
polynomial over `O`. If `M ∣ m` in `O`, then `det (1 + m • C)` is the image of an element of `O`
that is `1` modulo `M`. 

### `New.aeval_charpoly_dvd_of_smul_sub_one`

 Let `ι Y = v • (g - 1)`. For a polynomial `r` over `O`, the characteristic polynomial of `r Y`
at `r (v • (B - 1))` is a multiple of the characteristic polynomial of `g` at `B`. 

### `New.star_smul_sub_one_mul_one_add_smul_eq_neg`

 For a unitary `γ`, a hermitian `v` and `a` with `a * v * v = v`, the matrix `B = v • (γ - 1)`
satisfies `star B * (1 + a • B) = -B`. 

### `indicator_comp_eq_and_inv_mul_mem_of_mem_imp_mem`

 The two support conditions of `New.IsMatchingPair` for the indicator functions of a subgroup
`L` of `G`. Let `Nm : G → G` map `L` into itself, and let `γ ∈ L` imply `a ∈ L`. Then the
indicator of `L` takes the same value at `j x` and at `a` whenever `j x = γ = Nm a`, and
`a⁻¹ * δ ∈ L` whenever `Nm δ = γ` and `δ` lies in the support of the indicator of `L`. 

### `New.exists_twisted_root_of_smul_sub_one`

 Roots for one matrix in `New.cocyclesSplit_and_isMatchingPair_of_congruence`
(`ι = algebraMap O R`). Let `O` be profinite and integrally closed in `R`. Let `τ` commute with
`star`, be tame at levels `0` and `m = star m`, fix a `c` with `c - star c` a unit, and satisfy
`ι ∘ τ = σ ∘ ι`. Let `v` be `star`- and `σ`-fixed with `ι m * v = ι u` and `ι u * v = v`. If
`ι Y = v • (g - 1)`, `1 + m • Y` is a unit and `σ` fixes the characteristic polynomial of `g`, then
there are polynomials `z`, `z'` over `O` with the following property at `B' = v • (B - 1)`, for each
root `B` of that polynomial: `1 + m z'` inverts `1 + m z`, and the twisted norm
`T = (1 + m z) ⋯ τ^{p-1}(1 + m z)` has `(1 + m • B') * star T = T` if
`star B' * (1 + m • B') = -B'`. 

### `New.exists_det_one_add_smul_aeval_eq_of_smul_sub_one`

 Determinants for one matrix in `New.exists_isNormRoot_and_mem_of_mem`, where `ι` is
`algebraMap O R` and `m = u * M`. Let `O` be integrally closed in `R`, let `ι Y = v • (g - 1)`, let
`B` be a root of the characteristic polynomial of `g`, and let `(1 + m z') (1 + m z)` be `1` at
`B' = v • (B - 1)`. Then `det ((1 + m z) (B'))` is `1 + ι (M * w)` for some `w` over `O`, with
inverse `1 + ι (M * w')` for some `w'` over `O`. 

### `New.exists_isNormRoot_and_mem_of_mem`

 The root for one characteristic polynomial in
`New.cocyclesSplit_and_isMatchingPair_of_congruence`, in its setting, with `u` and `v` `star`-fixed,
`σ v = v` and `u * m = m`. Suppose `Y s` over `O` has `ι (Y s) = v • (s - 1)` for each `s ∈ L`, and
one `g ∈ L` has `1 + m • Y g` a unit and a `σ`-fixed characteristic polynomial `P`. Then some root
`z` for `P` (`New.IsNormRoot`; among its conditions, its value at each matrix root `B` of `P` has
determinant in `D`) has `γ ∈ L → a ∈ L` for unitary `γ` of characteristic polynomial `P` and
`a * (u • z)(γ)ᴴ = (u • z)(γ)`. 

### `New.cocyclesSplit_and_isMatchingPair_of_congruence`

 Let `O` be profinite and integrally closed in `R`. Let `τ`, with `τ ^ p = 1`, be tame on `O` at
the levels `0` and `m = u * M` (`star m = m`), commute with `star`, and fix some `c` with
`c - star c` a unit. `ι = algebraMap O R` carries `τ` to a `σ` that commutes with `star`;
`mapEnd hσ` applies `σ` to each entry of a unitary matrix. Let `L` be the `σ`-stable group of
unitary `g` over `R` with `v • (g - 1)` over `O`, where `m * v = u` and `u * v = v`. Then (a) the
cocycles in `L` split on the support of `u`, and (b) for any map `j : A → U 1`, the indicator of `L`
and its pull-back along `j` form a matching pair (`New.IsMatchingPair`) for every `D` that holds the
units `1 + ι (M * y)`. 


## Unramified places of a step and levels with matching unit pairs

`New.placesAbove E' S` is the set of places above `S` and its conjugates, `New.idem A` the adele
that is `1` at the places of `A` and `0` elsewhere, `New.kerCompNorm E' μ` the kernel of `μ ∘ Nm`,
`New.baseChangeGf` the inclusion of the unitary groups, `New.galoisGf σ` the Galois action, and
`New.IsMatchingPairAbove` the matching condition `New.IsMatchingPair` above `S`.


### `IsStepUnramifiedPlace`

 The place `u` of `E'` is unramified for the step `E' / E` and the character `μ`: its inertia
group is not all of `Gal(E'/E)`, and `μ` kills the norms of the local units at `u`. 

### `IsStepUnramifiedPlace.exists_notMem_inertia`

 The inertia group of `u` is not all of `Gal(E'/E)`. 

### `IsStepUnramifiedPlace.apply_localNorm_eq_one`

 `μ` is trivial on the norms of the local units at `u`. 

### `IsStepUnramifiedAt`

 The place `w` of `E` is unramified for the step `E' / E` and the character `μ`: so is every
place of `E'` above it. 

### `IsMatchingLevel`

 The subgroup `L` of the finite adelic unitary group over `E'` is a level at which the
indicator functions match above the set `S` of places of `E` and its conjugates: `L` is open and
stable under `σ`, its cocycles split above `S`, and the indicator function of `L` matches its
pull-back to `E`. 

### `IsMatchingLevel.isOpen`

 `L` is open. 

### `IsMatchingLevel.galoisGf_mem_iff`

 `L` is stable under `σ`. 

### `IsMatchingLevel.cocyclesSplit`

 The cocycles in `L` are coboundaries above `S`. 

### `IsMatchingLevel.isMatchingPairAbove_indicator`

 The indicator function of `L` and its pull-back to `E` form a matching pair above `S`. 

### `IsBaseChangeLevel`

 The local levels `K u` over `E'` form a base change level below the subgroup `H` of the finite
adelic unitary group over `E`. 

### `IsBaseChangeLevel.le_localIntGL`

 Each `K u` lies in `GL_n(O_u)`. 

### `IsBaseChangeLevel.isMatchingLevel`

 The group cut out by `K` above any set `S` and its conjugates is a matching level. 

### `IsBaseChangeLevel.comap_le`

 The elements over `E` that lie in `K u` at every `u` lie in `H`. 

### `IsBaseChangeLevel.eq_localIntGL`

 `K u = GL_n(O_u)` at the places `u` above an unramified place `w` and its conjugate, when
  `H` contains the integral points supported at `w` and its conjugate (`maxCompactAt n w`). 

### `IsStepUnramifiedPlace.of_star`

 If the conjugate place `star u` is unramified for the step, so is `u`. 

### `adeleOneOn`

 The finite adele that is `1` at the places of `A` and `x` at the others. 

### `continuous_adeleOneOn`

 The adele `adeleOneOn A x`, which is `1` on `A` and `x` off `A`, is continuous in `x`. 

### `adeleOneOn_mul_adeleOneOn_of_mul_eq_one`

 If `a * b = 1`, the adeles that are `1` on `A` and `a`, resp. `b`, off `A` are inverse to each
other. 

### `isStepUnramifiedPlace_of_mem_placesAbove`

 Let every place of the set `T` of places of `E` be unramified for the step. Then so is every
place of `E'` above a place of `T` or above the conjugate of one. 

### `eventually_mem_kerCompNorm_of_apply_localNorm_eq_one`

 Let `μ` kill the norms of the local units at the places of `A`. For `x` near `0`, a unit idele
congruent to `1` modulo `adeleOneOn A x` lies in `kerCompNorm E' μ`, the kernel of `μ ∘ Nm`. 

### `eventually_mem_kerCompNorm`

 Let `A` be a set of unramified places. For `x` near `0`, the norm of a unit idele congruent to
`1` modulo `adeleOneOn A x` is killed by `μ`. 

### `eventually_mem_of_baseChangeGf_congr`

 Let the open subgroup `H` contain the integral points that are trivial on `S`, and let no place
of `A` lie above `S`. For `x` near `0`, an integral point `g` over `E` whose matrix over `E'` is
congruent to `1` modulo `adeleOneOn A x` lies in `H`. 

### `congruenceLevel`

 The elements `g` of `GL_n(O_u)` with `k * (g - 1)` integral at `u`. For `k` the inverse of an
integral adele `m`, this is the principal congruence subgroup of level `m` at `u`. 

### `mem_congruenceLevel`

 An element `g` of `GL_n` of the completion at `u` lies in `congruenceLevel n k u` exactly when
it lies in `GL_n(O_u)` and `k * (g - 1)` has integral entries at `u`. 

### `mem_localLevel_congruenceLevel`

 Let `k` be the inverse of an integral adele `m`. Then `g` lies in the level given by
`congruenceLevel n k` at the places above `S` and their conjugates exactly when `k * (g - 1)` is
integral at these places: the integrality of `g` itself follows. 

### `isIntegrallyClosedIn_Ô`

 The integral adeles are integrally closed in the finite adeles, as each local ring of integers
is in its field. 

### `intAdeleMap`

 The ring homomorphism from the integral finite adeles of `E` to those of `F` induced by an
embedding `f : E → F`. 

### `intAdeleMap_iterate`

 For a ring endomorphism `f` of `E`, the `i`-th iterate of `intAdeleMap f` is the restriction of
`adeleMap f ^ i` to the integral adeles. 

### `notMem_inertia_of_comap_ne`

 If `σ` moves the place `u`, then `σ` is not in the inertia group of `u`. 

### `exists_intAdeleMap_eq_isUnit_sub_star`

 There is an integral adele `c` of `E'` fixed by `σ` such that `c - star c` is a unit. 

### `galoisGf_mem_localLevel_congruenceLevel_iff`

 Let `m * k = 1` with `k` fixed by `σ`. Then the level given by `congruenceLevel n k` at the
places above `S` and their conjugates is stable under `σ`. 

### `isMatchingLevel_congruenceLevel`

 Let `m` be an integral adele fixed by `star`, with an inverse `k` fixed by `σ`. Suppose that
`σ` is tame at level `e * m` for every integral `e` that it fixes, and that `μ` kills the norms of
the unit ideles congruent to `1` modulo `m`. Then the principal congruence level of `m` above any
`S` is a matching level. 

### `congruenceLevel_adeleOneOn_eq_localIntGL_of_mem`

 At a place `u` of `A` the adele `adeleOneOn A x` is `1`, so the level
`congruenceLevel n (adeleOneOn A x) u` is all of `GL_n(O_u)`. 

### `comap_localLevel_congruenceLevel_le`

 Let `m * k = 1`, and let `H` contain every integral point `g` over `E` whose matrix over `E'` is
congruent to `1` modulo `m`. Then `H` contains every point over `E` whose base change lies in
`congruenceLevel n k u` at every place `u` of `E'`, as `g - 1 = m • k • (g - 1)`. 

### `exists_isTameAtLevel_intAdeleMap`

 For a step `E' / E` and `σ ≠ 1` there is an integer `C ≠ 0` with the following property. Let
`m` be an integral adele of `E'` fixed by `σ` whose reduction vanishes at every place `u` of `E'`
that divides `C` and has all of `Gal(E'/E)` as inertia group (a totally ramified place). Then `σ`
acts tamely on the integral adeles at level `m` (`IsTameAtLevel`). 

### `exists_isBaseChangeLevel`

 Let `E'/E` be a step with character `μ` (`IsStep`): `E` contains a primitive 5040th root of
unity, and `E'` is a CM field Galois over `E` of prime degree. Let `σ ≠ 1` in `Gal(E'/E)` and let
`H` be an open subgroup of the finite adelic unitary group over `E`. Then some family `K` of
subgroups `K u` of `GL n` over the completions `E'_u` at the finite places `u` is a base change
level below `H` (`IsBaseChangeLevel σ μ H K`). 
