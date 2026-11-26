---
{
  "module": "src/Lib/General/Measure/HaarModulus.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/HaarModulus.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/HaarModulus.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Pushforward of Haar measures, the modulus of GL_n and the generalised index

This file compares Haar measures under pushforward and computes the factors by which maps scale
them. Mathlib's `distribHaarChar A g` is the factor by which `g` scales Haar measure on the additive
group `A`. For a unit `a`, `New.genIndex a` is the inverse of this factor for multiplication by `a`.
For a pair `R ⊆ A` with `New.IsAdelic R`, the indices of column lattices are expressed through
`genIndex` of determinants.

## Main definitions and results

* `New.measure_smul_map_restrict_eq_smul_inv`: the pushforward under a homomorphism of a
  bi-invariant measure restricted to a set `O`, compared with a left invariant measure on the
  target. The condition on `O` is `New.HasStableLifts`.
* `New.inv_distribHaarChar_eq_relIndex_div`: the inverse of the scaling factor is a ratio of
  relative indices of compact open subgroups.
* `New.genIndex`: the generalised index of `a : R`, for a unit the inverse of the factor by which
  `a` scales Haar measure on `R`, and `0` otherwise. Let `O` be a compact open subring and `a ∈ O`
  a unit of `R`. Then it is the cardinality of `O / a O` (`New.genIndex_eq_card`).
* `New.inv_distribHaarChar_GL_eq_genIndex_det`: `g : GL n R` scales Haar measure on `n → R` as
  `det g` does on `R`, if `R` has a compact open subring with the property `New.IsValuationPair`.
* `New.submoduleIndex_colLattice_div`: the ratio of the two indices between the column lattice of
  an invertible matrix and the standard lattice is `genIndex` of the determinant.
* `New.submoduleIndex_colLattice_intVectors`: if the matrix has entries in `R`, the index of its
  column lattice in the standard lattice is `genIndex` of the determinant.

Notions from other files:
* `New.IsValuationPair O`: any two elements `a`, `b` of the ambient ring are `O`-multiples of
  `(1 - e) a + e b` for some idempotent `e` of the subring `O`.
* `New.IsAdelic R`: the subring `R` of `A` is open, compact, stable under `star` and satisfies
  `New.IsValuationPair`, with further properties that are not used here.



## Units along non-unital ring maps and invertible matrices from spanning sets

`New.unitsMapNonUnital` maps units along a ring map that need not preserve 1.
`New.exists_GL_col_mem_of_span` picks the columns of an invertible matrix from a spanning set.


### `New.unitsMapNonUnital`

 For a ring homomorphism `f : K → R` that need not preserve `1`, the homomorphism of unit groups
`x ↦ 1 + f (x - 1)`. 

### `New.exists_GL_col_mem_of_span`

 If a set `s` spans `n → K` over a field `K`, then some invertible matrix has all its columns
in `s`. 

 ## Haar pushforwards and the modulus of a matrix 

### `measure_le_of_div_mem`

 Let `ζ` be a right invariant measure on a group `Z`. If `E` is empty or some right translate of
`E` lies in `K`, then `ζ E ≤ ζ K`. 

### `HasStableLifts`

 Every `h : G` has a preimage `g` under `π` whose left and right translations preserve the
set `O`. 

### `HasAddStableLifts`

 Every `h : G` has a preimage `g` under `π` whose left and right
translations preserve the set `O`. 

### `map_restrict_apply_preimage_mul_mul`

 Let `μ` be a bi-invariant measure on `Z`, `π : Z →* G` measurable, and `O` a measurable set
preserved by the translations by suitable lifts of the elements of `G` (`New.HasStableLifts`). Then
the pushforward of `μ.restrict O` gives every two-sided translate of a measurable set `S` the
measure `μ (π ⁻¹' S ∩ O)`. 

### `isMulLeftInvariant_map_restrict`

 Let `μ` be a bi-invariant measure on `Z`, `π : Z →* G` measurable, and `O` a measurable set
with `New.HasStableLifts π O`. Then the pushforward of `μ.restrict O` is left invariant. 

### `measure_smul_map_restrict_eq_smul_inv`

 Let `μ` be an s-finite bi-invariant measure on `Z`, `η` an s-finite left invariant measure on
`G`, `π : Z →* G` measurable, `O` a measurable set with `New.HasStableLifts π O`, and `K`
measurable in `G`. Then `η K` times the pushforward of `μ.restrict O` equals `μ (π ⁻¹' K ∩ O)`
times `η.inv`, the image of `η` under inversion. 

### `isMulLeftInvariant_measure_smul_inv`

 Let `μ` be an s-finite bi-invariant measure on `Z`, `η` an s-finite left invariant measure on
`G`, `π : Z →* G` measurable, `O` a measurable set with `New.HasStableLifts π O`, and `K`
measurable in `G`. Then `μ (π ⁻¹' K ∩ O)` times `η.inv`, the image of `η` under inversion, is left
invariant. 

### `map_restrict_haar_eq`

 Let `μ` be an s-finite bi-invariant measure on `Z`, `η` an s-finite left invariant measure on
`G`, `π : Z →* G` measurable, `K` measurable in `G`, and `O` a measurable set such that every
element of `G` has a preimage under `π` whose translations preserve `O` (`New.HasStableLifts`).
Then `η K` times the pushforward of `μ.restrict O` equals `μ (π ⁻¹' K ∩ O)` times `η.inv`, the
image of `η` under inversion, and this measure is left invariant. 

### `inv_distribHaarChar_eq_relIndex_div`

 Let `G` act by continuous additive automorphisms on a locally compact Polish abelian group `A`,
and let `L` be a compact open subgroup. Then the inverse of `distribHaarChar A g`, the factor by
which `g` scales Haar measure, is `[L : gL ∩ L] / [gL : gL ∩ L]`. 

### `map_addHaar_eq_smul_of_semiconj`

 Let `e : B → A` be an isomorphism of topological groups, with `A` Polish, locally compact and
abelian, and let `e ∘ φ = ψ ∘ e` with `ψ` measurable. If `ψ` pushes a Haar measure `ν` on `A` to
`c • ν`, then `φ` pushes every Haar measure `μ` on `B` to `c • μ`. 

### `map_const_smul_eq_inv_distribHaarChar_smul`

 The action of `a : G` pushes a Haar measure `ν` on `A` forward to `ν` divided by
`distribHaarChar A a`, the factor by which `a` scales Haar measure. 

### `map_smul_eq_inv_distribHaarChar_smul`

 `map_const_smul_eq_inv_distribHaarChar_smul` with the scalar written as `ENNReal.ofReal` of a
real number: `a : G` pushes a Haar measure `ν` on `A` forward to `ν` divided by
`distribHaarChar A a`, the factor by which `a` scales Haar measure. 

### `instance : ContinuousSMul (GL n R) (n → R)`

 The action of invertible matrices on vectors is jointly continuous. 

### `instance : ContinuousConstSMul (GL n R) (n → R)`

 Each invertible matrix acts continuously on vectors. 

### `genIndex`

 The generalised index of `a : R`, as a real number. For a unit `a` it is the inverse of the
factor by which multiplication by `a` scales Haar measure on `R`; for a non-unit it is `0`. 

### `genIndex_eq_relIndex_div`

 Let `L` be a compact open additive subgroup of `R` and `u` a unit. The generalised index
`genIndex u` is the quotient of indices `[L : uL ∩ L] / [uL : uL ∩ L]`. 

 ### The generalised index for a compact open subring 

### `genIndex_eq_card`

 Let `O` be a compact open subring of `R`. For `a ∈ O` that is a unit of `R`, the generalised
index `genIndex a` (the inverse of the factor by which `a` scales Haar measure on `R`) equals the
cardinality of the quotient ring of `O` by `a O`. 

### `genIndex_det_eq_one`

 Let `O` be a compact open subring of `R`. If `V` lies in `intGL n O`, that is, `V` and its
inverse have entries in `O`, then the generalised index `genIndex (det V)` (the inverse of the
factor by which `det V` scales Haar measure on `R`) is `1`. 

### `distribHaarChar_eq_one_of_mem_intGL`

 Let `O` be a compact open subring of `R`. A matrix `k` that has, like its inverse, entries in
`O` preserves Haar measure on `n → R`. 

### `distribHaarChar_diagGL`

 The diagonal matrix `diagGL d` with unit entries `d i` scales Haar measure on `n → R` by the
product of the factors by which the `d i` scale Haar measure on `R`. 

### `inv_distribHaarChar_GL_eq_genIndex_det`

 Let `R` be a locally compact Polish commutative ring with a compact open subring `O` satisfying
`New.IsValuationPair` (any `a b : R` are `O`-multiples of `(1 - e) a + e b` for an idempotent `e`
of `O`). Then `g : GL n R` scales Haar measure on `n → R` by the same factor as
`det g` scales Haar measure on `R`; the inverse of the latter factor is `genIndex (det g)`. 


## Integral matrices, the generalised index and indices of lattices

`New.genIndex a = [R : R ∩ a R] / [a R : R ∩ a R]` for a unit `a` of `A` and a pair `R ⊆ A` with
`New.IsAdelic R`.
`New.colLattice R M` is the `R`-span of the columns of `M`. `New.submoduleIndex L L'` is the index
of `L ⊓ L'` in `L'` (`0` if infinite). `New.IsIntMatrix R M` says that `M` has entries in `R`.

* `New.one_le_genIndex`, `New.genIndex_star`: the index is at least `1` on elements of `R` that are
  units of `A`, and it is invariant under `star`.


 ### Integral matrices 

 ### The generalised index for an adelic pair 

### `one_le_genIndex`

 Let `R ⊆ A` satisfy `New.IsAdelic`, so that `R` is compact and open. The generalised index
`genIndex u` (the inverse of the factor by which `u` scales Haar measure on `A`) is at least `1` if
`u ∈ R` is a unit of `A`. 

### `genIndex_star`

 Let `R ⊆ A` satisfy `New.IsAdelic`, so that `R` is compact, open and stable under `star`. Then
the generalised index `genIndex a` (the inverse of the factor by which `a` scales Haar measure on
`A`, and `0` for a non-unit) is invariant under `star`. 

 ### Indices of lattices 

### `toAddSubgroup_colLattice`

 The lattice `colLattice R M` spanned by the columns of an invertible matrix `M` is the image
under `M` of the lattice `intVectors R n` of vectors with entries in `R`. 

### `submoduleIndex_colLattice_div`

 Let `R ⊆ A` satisfy `New.IsAdelic`, so that `R` is compact and open, and let `M` be invertible
over `A`. Let `L = colLattice R M` be the `R`-span of the columns of `M` and `L₀ = intVectors R n`
the lattice of vectors with entries in `R`. Then the quotient of the indices
`submoduleIndex L L₀ = [L₀ : L ∩ L₀]` and `submoduleIndex L₀ L = [L : L ∩ L₀]` is
`genIndex (det M)`, the inverse of the factor by which `det M` scales Haar measure on `A`. 

### `submoduleIndex_colLattice_intVectors`

 Let `R ⊆ A` satisfy `New.IsAdelic`, so that `R` is compact and open. The `R`-span
`colLattice R M` of the columns of an invertible matrix `M` with entries in `R` has index
`genIndex (det M)` (the inverse of the factor by which `det M` scales Haar measure on `A`) in the
lattice `intVectors R n` of vectors with entries in `R`. 
