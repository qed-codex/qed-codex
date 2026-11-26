---
{
  "module": "src/Lib/General/Groups/CongruenceSubgroups.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/CongruenceSubgroups.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/CongruenceSubgroups.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integral, congruence and unitary matrix groups over a ring, with their topology

The file opens with a few general facts on induction, reindexing, compact, open and closed sets, and
integrability.

* `New.intGL`, `New.congruenceGL`: the matrices of `GL n R` that are invertible over a subring `O`,
  and the congruence subgroups among them; `New.intGL.toMatrix` reads such a matrix over `O`, and
  `New.intGL.map` applies a ring map out of `O`.
* `New.U`: the unitary group of a matrix `J`, the `g` in `GL n R` with `gᴴ * J * g = J`, with change
  of ring `New.U.map`, change of basis `New.U.conj` and determinant `New.U.det`.
* `New.U.isClosedEmbedding_coe`: for invertible `J`, `U J` is closed in the space of matrices; with
  the bound on the entries of a unitary matrix, this gives that the complex unitary group of the
  identity matrix is compact.

The file also supplies the Polish and Borel instances on units, the measurable and measure space
structures on matrices, the Polish instance on unitary groups and the Borel instance on complex
ones, local compactness of unitary groups, and the additive Haar measure on matrices.


### `Finite.int_weight_induction`

 Well-founded induction on an integer weight `w` over a finite type: a property `P` holds
everywhere if it holds at each point as soon as it holds at all points of smaller weight. 

### `New.forall_reindex_equiv`

 A statement `∀ y, p y` about `β` is reindexed along an equivalence `e` from `α` to `β`. 

### `New.exists_reindex_equiv`

 A statement `∃ y, p y` about `β` is reindexed along an equivalence `e` from `α` to `β`. 

### `New.sum_reindex_equiv`

 A finite sum over `β` is reindexed along an equivalence `e` from `α` to `β`. 

### `New.prod_reindex_equiv`

 A finite product over `β` is reindexed along an equivalence `e` from `α` to `β`. 

### `New.reindex_equiv`

 For an equivalence `e` from `α` to `β`, statements `∀ y, p y` and `∃ y, p y` about `β`, and
finite sums and products over `β` of values in a type of universe 0, become those over `α` of the
composite with `e`. The four rules are joined so that `simp` takes them as one argument. 

### `IsCompact.preimage_val`

 If K is compact and s is closed in a topological space, then s ∩ K is compact as a subset of
the subspace s. 

### `IsCompact.image_of_continuous`

 The image of a compact set under a continuous map is compact; continuity is found by
automation unless supplied. 

### `IsOpen.preimage_of_continuous`

 The preimage of an open set under a continuous map is open; continuity is found by
automation unless supplied. 

### `IsClosed.preimage_of_continuous`

 The preimage of a closed set under a continuous map is closed; continuity is found by
automation unless supplied. 

### `IsCompact.integrableOn`

 A continuous function f from a Hausdorff space to a normed group is integrable on a compact
set K, for a measure ν finite on compact sets. Continuity is proved automatically by
default. 

### `HasCompactSupport.integrable`

 A continuous function f of compact support with values in a normed group is integrable, for
a measure ν finite on compact sets. Continuity is proved automatically by default. 

### `New.DiscreteSeries.integrable_of_compactSpace`

 A continuous function from a compact space `X` to a normed group is integrable for every measure
ν on `X` that is finite on compact sets. Continuity is proved automatically by default. 

 ### Special matrices 

### `inclMatrix`

 For a map u: m → n of index sets, the n×m matrix whose j-th column is the standard basis
vector e_{u(j)}. 

### `signMatrix`

 The diagonal complex matrix whose entries are the signs s_i = ±1. 

### `mul_inclMatrix`

 Multiplying M on the right by the inclusion matrix of u selects the columns u(j) of M. 

### `signMatrix_mul_self`

 The diagonal matrix of a vector of signs ε is its own inverse. 

### `diagGL`

 The homomorphism sending a family of units of R to the diagonal matrix in GL_n(R) with these
entries. 

### `transposeGL`

 The transpose of g, as an element of GL_n(R). 

### `transvectionGL`

 For distinct indices i, j and a in R, the element 1 + aE_{ij} of GL_n(R), with inverse
1 − aE_{ij}. 

 ### Integral matrices and congruence subgroups 

### `intGL`

 For a subring O of R, the subgroup GL_n(O) of GL_n(R): matrices with entries in O whose
inverse has entries in O. 

### `mem_intGL`

 A matrix lies in GL_n(O) if and only if its entries and those of its inverse lie in O. 

### `intGL.toMatrix`

 The matrix over `O` with the entries of an element `k` of GL_n(O). 

### `intGL.toMatrix_apply`

 The entry of `toMatrix k`, the matrix over `O` of an integral matrix `k`, at `(i, j)` is the
entry of `k`, read in `O`. 

### `intGL.map`

 For a ring homomorphism f: O → S, the homomorphism GL_n(O) → GL_n(S) applying f to each
entry. 

### `intGL.map_apply`

 The entries of the image of an integral matrix k are the images under f of its entries, read
in `O`. 

### `intGL.map_eq_one`

 An integral matrix `k` maps to `1` under `f` if and only if `f` kills every entry of
`k - 1`, read in `O`. 

### `mem_span_singleton_iff_exists_mul`

 For a subring O of R, the O-submodule of R spanned by a consists of the a y with y in O. 

### `congruenceGL`

 For an O-submodule M of R and a map e of index sets, the group of matrices in GL_n(O) whose
rows e(i) are congruent to those of 1 modulo M; for e the identity, the principal congruence
subgroup of level M. 

 ### Unitary groups 

### `map_conjTranspose_mul_mul`

 A ring map f that commutes with the involutions carries zᴴ B z to (f z)ᴴ (f B) (f z). 

### `gram_mul`

 The Gram matrix of XY for the form J is Yᴴ (Xᴴ J X) Y. 

### `gram_mul_of_gram_eq`

 If x carries the form J to J' and y carries J' to J'', then xy carries J to J''. 

### `gram_inv_of_gram_eq`

 If x carries the form J to J', then its inverse carries J' to J. 

### `U`

 The unitary group U(J) of a matrix J over a commutative ring with involution: the g in
GL_n(R) with gᴴJg = J. 

### `USign`

 For a vector of signs ε, the unitary group U(J) of the diagonal matrix J=diag(ε). 

### `form_mul_inv_eq`

 For g in the unitary group U(J), one has J g⁻¹ = gᴴ J. 

### `coe_inv`

 If J is an involution, the inverse of g in the unitary group U(J) is J gᴴ J. 

### `inv_val_eq_conjTranspose`

 In the unitary group of the identity matrix, the inverse is the conjugate transpose. 

### `gram_invariant`

 An element g of U(J) preserves the pairing Aᴴ J B of matrices A and B. 

### `form_mulVec_mulVec`

 An element g of U(J) preserves the sesquilinear form with matrix J. 

### `of`

 For invertible J and a matrix M with MᴴJM = J, the element of U(J) with matrix M. 

### `map`

 For a ring homomorphism f commuting with the involutions and carrying J to J', the
homomorphism U(J) → U(J') applying f to each entry. By default `simp` proves both conditions. 

### `mem_range_map`

 Let `f : R → S` be an injective ring map that commutes with the involutions and carries the
invertible n × n matrix `J` over `R` to `J'`. An element `g` of the unitary group `U J'` whose
matrix is the image under `f` of a matrix `M` over `R` is the image of an element of `U J` with
matrix `M`. 

### `conj`

 For x in GL_n(R) with xᴴJx = J', the isomorphism U(J') ≅ U(J), g ↦ x g x⁻¹. 

### `det`

 For J with unit determinant, the determinant as a homomorphism from U(J) to the group of
elements u of R with uū = 1. 

### `continuous_map`

 Let `f : R → S` be a continuous ring map that commutes with the involutions and carries `J` to
`J'`. The induced map `U J → U J'` of unitary groups is continuous. 

 ### Topology of unitary groups 

### `isClosed_U`

 The unitary group `U J` of a matrix J is closed in GL_n(R), for a Hausdorff topological ring R
with continuous involution. 

### `isClosed_of_entries_eq_one`

 A subgroup `H` of `U J` that is described by asking the entries `(i, j)` with `p i j` to equal
those of the identity matrix is closed. 

### `U.isClosedEmbedding_coe`

 For invertible J over a Hausdorff topological commutative ring with continuous involution,
the map sending an element of the unitary group U(J) to its matrix is a closed embedding. 

### `U_one_mem_unitaryGroup`

 An element of the complex unitary group U(1) of the identity matrix is a unitary matrix. 

### `U.borelSpace`

 For a complex matrix J, the unitary group U(J) carries the Borel σ-algebra of its topology. 

### `isAddHaarMeasure_pi`

 The product measure on functions from `n` to `A` is an additive Haar measure. 
