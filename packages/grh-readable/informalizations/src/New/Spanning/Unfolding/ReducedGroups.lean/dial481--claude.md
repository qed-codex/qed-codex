---
{
  "module": "src/New/Spanning/Unfolding/ReducedGroups.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedGroups.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedGroups.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The finite groups `Ū`, `H̄` and `R̄`

The reductions `Ū`, `H̄`, `R̄` of the groups `besselU`, `besselH`, `besselS` at the chosen places
are products over these places (`mem_reducedImage_iff_forall_place`). The factor of `Ū` at `w`
consists of the block unitriangular matrices over `𝔽_w` (`mem_reducedImage_besselU`), and that of
`H̄` is `GL_k(𝔽_w)` with `k = |𝔰.κ|` (`reducedImageBesselHEquiv`). Counting free entries gives the
order of `Ū` (`card_reducedImage_besselU`). Each element of `R̄` is a product of elements of `Ū` and
`H̄` (`mem_reducedImage_besselS`); these two meet in the identity, and `R̄` normalises `Ū`. For
admissible `S`, the order of `H̄` is the index of the level `S.sourceLevel` in the points of the
unitary group of `X₀` that preserve the lattice (`relIndex_sourceLevel`).

Notions from other files:
* `unitriangular lev R`: the invertible matrices over `R` that agree with `1` at the entries
  `(i, j)` with `lev j ≤ lev i`; `BesselIndex.level` is the level function of the Bessel basis.
* `S : Filling E 𝔰`: the data of the filling theorem, among them the sets `S.chosenPlaces i`.
* `S.latticeStabilizer`: the elements of the finite adelic unitary group `S.GFin` that are
  invertible over the integral adeles `Ô E`; `S.reduction` reduces them modulo the chosen places.
* `S.reducedImage B`: the image of `B ⊓ S.latticeStabilizer` under `S.reduction`.


### `map_matrix_one_apply`

 A ring homomorphism maps the entries of the identity matrix to those of the identity matrix:
the entrywise form of `Matrix.map_one`. 

### `mulEquivOfKerEq`

 Two surjective homomorphisms with the same kernel have isomorphic targets: both are isomorphic
to the quotient by the kernel. 

### `mulEquivOfKerEq_apply`

 For surjective homomorphisms `f` and `g` with the same kernel, the isomorphism
`mulEquivOfKerEq hf hg h_ker` sends `f a` to `g a` for every `a : G`. 

### `FreeEntry`

 The free entries of a block unitriangular matrix: the pairs `(i, j)` with `lev i < lev j`. 

### `unitriangularEquiv`

 A matrix that is block unitriangular for the level function `lev` (equal to `1` at the entries
`(i, j)` with `lev j ≤ lev i`) is the same as a choice of its free entries. 

### `unitriangularEquiv_symm_apply_of_lt`

 The block unitriangular matrix with the free entries `a` has the entry `a (i, j)` at a pair
`(i, j)` with `lev i < lev j`. 

### `card_unitriangular`

 The number of matrices over a ring with `q` elements that are block unitriangular for the level
function `lev` is `q` to the power of the number of free entries. 

### `exists_unitriangular_map_eq`

 Let `n` be the index type and `lev : n → α` a level function. Suppose every family `t` has a
common preimage `y` under the maps `f p : R → F p`. Then a family `s p` in `unitriangular lev (F p)`
lifts to one `u` in `unitriangular lev R` with `GeneralLinearGroup.map (f p) u = s p`. 

### `card_freeEntry_level`

 The level function `BesselIndex.level` has the block sizes `1, …, 1, m, 1, …, 1`, with `ϱ` ones
on each side and `m` the cardinality of `μ`. It has `(2ϱ choose 2) + 2ϱ m` free entries. 

### `conjTranspose_one_add_smul_sub_one_mul_mul_eq`

 Let `J` be a hermitian matrix, `e` an idempotent with `e ē = 0`, and `u'` an inverse adjoint of
`u`, that is `uᴴ J u' = J`. The matrix that is `u` on the factor `e R`, `u'` on the factor `ē R`
and `1` on the remaining factor preserves `J`. 

### `splitGram_apply_eq_zero`

 The split form `T.splitGram` (`ϱ` hyperbolic planes and a middle space with Gram matrix `T`)
has the entry zero at `(i, j)` unless the levels of `i` and `j` add up to `2ϱ`. The level is `a`
at the index `a` of the first block, `ϱ` on the middle block and `2ϱ - a` at the index `a` of the
last block. 

### `splitGram_mul_conjTranspose_mul_splitGram_apply_eq_zero`

 Let `T'` and `T` be arbitrary, and let `Z` be strictly block upper triangular: it vanishes at
the entries `(d, c)` where the level of `c` is at most that of `d`. Then so is
`T'.splitGram * Zᴴ * T.splitGram`: the transpose reverses the order of the levels, and the two Gram
matrices reverse it back. 

### `exists_invAdjoint_unitriangular`

 Let `J = T.splitGram` be the Gram matrix of `ϱ` hyperbolic planes and a middle space with
invertible Gram matrix `T`. A matrix `u` that is block unitriangular for `BesselIndex.level` has an
inverse adjoint `u'`, that is `uᴴ J u' = J`, which is again block unitriangular. 

### `exists_idempotent_reduceAt_eq_ite`

 Let `P` be a set of chosen places of the filling data `S`. There is an idempotent `e` of the
ring `Ô E` of integral finite adeles with `e * star e = 0`, where `star` is complex conjugation.
Modulo the places of `P`, `e` reduces (`reduceAt`) to `1`, and modulo the other chosen places it
reduces to `0`. `star e` reduces to `0` modulo all the chosen places. 

### `exists_reduction_eq_of_invAdjoint`

 Let `J = (S.latticeMiddle (Ô E)).splitGram` be the Gram matrix in the lattice basis of the
filling data `S`, let `u` and `u'` be matrices over the integral finite adeles with `uᴴ J u' = J`,
and let `P` be a set of chosen places. Some `k` in the stabiliser of the lattice agrees with `1` at
every entry where `u` and `u'` do, and its reduction is that of `u` modulo the places of `P` and `1`
modulo the other chosen places. 

### `reduction_apply_eq_one_apply`

 Let `k` lie in the stabiliser of the lattice (the integral points of the finite adelic unitary
group of the filling `S`). If `k` agrees with `1` at the entry `(a, b)`, so does its reduction at
every chosen place `w`. 

### `mem_reducedImage_besselU`

 Let `Ū = S.reducedImage besselU` be the reduction at the chosen places of the integral points of
the Bessel unipotent group. An element `s` of `S.ResidueGL`, the product of the general linear
groups over the residue fields at the chosen places, lies in `Ū` if and only if all its components
`s i w` are block upper unitriangular for `BesselIndex.level`. 

### `card_freeEntry_besselIndex`

 Let the shape `𝔰` have `ϱ = 𝔰.ϱ` hyperbolic planes and a summand `X₀` of rank `k = 𝔰.k`. The
function `BesselIndex.level` cuts the basis indices `𝔰.BesselIndex` into blocks of sizes
`1, …, 1, k + 1, 1, …, 1`, with `ϱ` ones on each side. There are `ϱ (2k + 2ϱ + 1)` free entries, the
positions `(i, j)` above the block diagonal. 

### `card_reducedImage_besselU`

 The order of `Ū = S.reducedImage besselU`, the reduction of the integral points of the Bessel
unipotent group, is `S.unipotentOrder = M ^ (f ϱ (2k + 2ϱ + 1))`. Here `M` is the product of the two
level primes, `f` the number of infinite places of `E`, `k` the dimension of `X₀` and `ϱ` the number
of hyperbolic planes. 

### `mem_reducedImage_iff_forall_place`

 Let `r` be a relation on the indices, and let `B` be a subgroup of the finite adelic unitary
group `S.GFin` that consists of the elements that agree with `1` at all entries `(a, b)` with
`r a b`. Its reduction `S.reducedImage B` is the product of its projections to the chosen places:
`s` lies in it if and only if each component `s i w` is the component of some element of it. 

### `mem_reducedImage_besselS_iff_forall_place`

 The group `R̄ = S.reducedImage besselS`, the reduction of the integral points of the Bessel
subgroup, is the product of its projections to the chosen places: `s` lies in `R̄` if and only if
each component `s i w` is the component of some element of `R̄`. 

### `inclHFin_mem_latticeStabilizer_of_supportedOn`

 The hermitian space `V` of the filling data `S` is the sum of `𝔰.ϱ` hyperbolic planes, the
standard hermitian space `X₀` with basis indexed by `𝔰.κ`, and a line. The map `S.inclHFin` extends
an isometry of `X₀` to `V` by the identity on the other summands and writes it in the lattice basis
of `S`; `S.latticeStabilizer` is the group of isometries that are invertible over `Ô E` in this
basis. Let `k` be an element of the finite adelic unitary group `Gf E 𝔰.κ` of `X₀` that is integral
and is `1` away from the chosen places and their conjugates. Then `S.inclHFin k` lies in
`S.latticeStabilizer`. 

### `isConjApart_chosenPlaces`

 The chosen places of the filling `S` are distinct, and none is conjugate to a chosen place. 

### `latticeStabilizerH`

 The integral elements `k` of the unitary group of `X₀` whose image `S.inclHFin k` in the unitary
group of the whole space preserves the lattice. 

### `reduction_inclHFin_mem_reducedImage_besselH`

 If the image `S.inclHFin k` of an element `k` of the unitary group of `X₀` preserves the
lattice, then its reduction lies in `H̄ = S.reducedImage besselH`. 

### `toReducedImageBesselH`

 The homomorphism from `S.latticeStabilizerH` to `H̄ = S.reducedImage besselH` that sends `k` to
the reduction of `S.inclHFin k` at the chosen places. 

### `toReducedImageBesselH_surjective`

 Every element of `H̄ = S.reducedImage besselH` is the reduction of `S.inclHFin k` for some `k`
in `S.latticeStabilizerH`. 

### `reduceLatticeStabilizerH`

 The homomorphism from `S.latticeStabilizerH` to the product of the groups `GL_κ(𝔽_w)` over the
chosen places `w` that sends `k` to the family of its reductions. 

### `reduceLatticeStabilizerH_surjective`

 Every family of invertible matrices over the residue fields at the chosen places is the family
of the reductions of some element of `S.latticeStabilizerH`. 

### `ker_toReducedImageBesselH`

 For `k` in `S.latticeStabilizerH`, the image `S.inclHFin k` reduces to `1` at the chosen places
if and only if `k` does. 

### `reducedImageBesselHEquiv`

 The group `H̄ = S.reducedImage besselH`, the reduction of the integral points of the fixer of
the basis vectors outside `X₀`, is the product of the groups `GL_κ(𝔽_w)` over the chosen places `w`,
where `κ` indexes the standard basis of `X₀`. Both groups are images of `S.latticeStabilizerH`, with
the same kernel. 

### `reducedImageBesselHEquiv_reduction_inclHFin`

 Let `k` be an integral element of the unitary group of `X₀` whose image `S.inclHFin k` preserves
the lattice. The isomorphism `S.reducedImageBesselHEquiv` sends the reduction of `S.inclHFin k` to
the family of the reductions of `k` at the chosen places. 

### `exists_mulEquiv_reducedImage_besselH`

 The group `H̄ = S.reducedImage besselH` is isomorphic to the product of the groups `GL_κ(𝔽_w)`
over the chosen places `w`, compatibly with reduction: for an integral element `k` of the unitary
group of `X₀` whose image `S.inclHFin k` preserves the lattice, the reduction of `S.inclHFin k`
corresponds to the family of the reductions `stdLevel.reduceAt w k`. 

### `coe_mem_principalLevel_iff_reduction_eq_one`

 An element of the stabiliser of the lattice lies in the principal congruence subgroup
`S.principalLevel` if and only if it reduces to `1` at all chosen places. 

### `relIndex_comap_principalLevel`

 The finite adelic points `k` of the unitary group of `X₀` with `S.inclHFin k` in
`S.principalLevel` (the principal congruence subgroup) have index `|H̄|` among those with
`S.inclHFin k` in `S.latticeStabilizer`. 

### `relIndex_sourceLevel`

 For admissible data `S`, the level `S.sourceLevel` has index `|H̄|` in the group of the finite
adelic points `k` of the unitary group of `X₀` whose image `S.inclHFin k` preserves the lattice. 

### `disjoint_reducedImage_besselU_besselH`

 The reductions `Ū` and `H̄` of the integral points of `besselU` and `besselH` at the chosen
places meet in the identity only. 

### `mem_reducedImage_besselS`

 Let `S : Filling E 𝔰`. In `S.ResidueGL`, the matrix groups over the residue fields at the chosen
places of `S`, the reduction `R̄` of the integral points of `besselS` is the set of products `u * h`
with `u` in `Ū` and `h` in `H̄`. 

### `reducedImage_besselS_le_normalizer`

 The reduction `R̄` of the Bessel subgroup `besselS` normalises the reduction `Ū` of its
unipotent subgroup `besselU`. This is a corollary of `besselS_le_normalizer_besselU`. 

### `card_reducedImage_besselS`

 Let `Ū`, `H̄`, `R̄` be the reductions of `besselU`, `besselH` (the fixer of the basis vectors
outside `X₀`) and `besselS`. Then `|R̄| = |H̄| |Ū|`, where `|Ū| = S.unipotentOrder`. 
