---
{
  "module": "src/Lib/Weil/MixedModel/AdaptedSplitting.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/AdaptedSplitting.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/AdaptedSplitting.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Adapted splittings: hyperbolic polarisation, Hom spaces, composition and stages

A splitting `D : V'.Splitting V p` (`New.Space.Splitting`) writes a hermitian space `V'` as `V` plus
`p` hyperbolic planes, by dual isotropic frames `D.l`, `D.k` and an isometry `D.i`. An adelic matrix
is `New.Exchange.IsOrthoIntegral` if it has orthonormal columns at the infinite places and integral
finite part. The splitting `D` is adapted, `New.Exchange.IsBaseAdapted D`, if its adelic frame
`(l, k, i)` has this property.

## Main definitions and results

* `New.hyperbolicSplitting`: the hyperbolic space `New.hyperbolicSpace E p` splits
  (`New.Space.Splitting`) over the zero space `New.stdSpace E Empty`. Here `l` is the first `p`
  basis vectors and `k` is the last `p` basis vectors.
* `New.Exchange.removePlanes`: the tautological splitting over V of the sum
  `New.Exchange.hyperbolicSum` of hyperbolic planes and V. An instance shows that the tautological
  splitting is adapted.
* `New.Exchange.adaptedHomBasis`: the change of basis `(x⁻¹)ᴴ ⊗ 1` given by the adelic frame `x` of
  `T`.
* `New.Exchange.homSlice_eq_adapted_slice`: the term `A.homSlice T x` is a mixed term of
  `A.homSource T`, after the change of basis `adaptedHomBasis p T`.
* `New.Exchange.isAdapted_homSource`: if `A` is adapted, `A.homSource T` is adapted in the basis
  `adaptedHomBasis p T`.
* `New.Exchange.exists_isBaseAdapted_reindex`,
  `New.Exchange.exists_isBaseAdapted_comp_removePlanes`: an adapted splitting with a single plane
  (`e : Unit ≃ p`) can be reindexed by `Unit`. An adapted splitting can be factored through `V` plus
  some of the planes.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to the diagonal matrix of its signs at the infinite places and 1 at the finite places.
* `New.Space.Splitting.IsAdapted`: `D.IsAdapted g t` says that the matrix g⁻¹(l tᴴ⁻¹, k t, ι) of
  adelic frames (`frameAt`) is `IsOrthoIntegral`.
* `New.Space.Splitting.homSource`: From a splitting (k, l, ι) of V over V₀, the splitting of
  Hom(V,T) over Hom(V₀,T) with frames J_T⁻¹⊗(kᴴJ)ᵀ, 1⊗(lᴴJ)ᵀ, 1⊗(J₀⁻¹ιᴴJ)ᵀ.
* `New.Space.Splitting.comp`: From splittings of V over V₀ (rank p) and V₀ over V₁ (rank q), the
  splitting of V over V₁ with frames (k, ik'), (l, il') and embedding ii'.
* `New.Space.Splitting.kCoord`, `lCoord`: the adelic matrices lᴴε, kᴴε (ε = `stdForm`), which send
  la + ιw + kb to b and to a; `iCoord`, built from ιᴴε and the signs, sends it to w.
* `New.Space.Splitting.homSlice`: `A.homSlice T x` is the zero term of `A.homSource T` after the
  Heisenberg operator of the map `x * A.kCoord` in `Hom(W', T)`.

## Relation to the literature

Known; see `Lib.Weil.MixedModel.ZeroTerm` for sources.


### `Matrix.submatrix_conjTranspose_mul_mul`

 Restricting the Gram matrix `Mᴴ * J * M` to the rows and columns chosen by `e` gives the Gram
matrix of the columns of `M` chosen by `e`. 

 ## The hyperbolic space as a splitting over the zero space 

### `New.hyperbolicSplitting`

 The splitting of hyperbolic space of rank 2p over the zero space. Here l is the first p basis
vectors and k is the last p basis vectors. 

 ## Adapted splittings and the removal of all hyperbolic planes 

### `IsBaseAdapted`

 The splitting `D` of `V'` over `V` (with `card p` hyperbolic planes) is adapted: the adelic
matrix with column blocks `lAdelic`, `kAdelic`, `iAdelic` has orthonormal columns at every infinite
place and integral entries at every finite place. 

### `IsBaseAdapted.isOrthoIntegral`

 The block matrix of the three adelic frames is orthonormal at the infinite places and integral
  at the finite places. 

### `removePlanes`

 The tautological splitting over V of the sum of `card p` hyperbolic planes and V: the
frames l, k, i are the column blocks of the identity matrix. 

### `instance : IsBaseAdapted (removePlanes p V)`

 The tautological splitting `removePlanes p V` is adapted. 


## Adapted splittings of Hom spaces

Here `A` is a splitting of `W'` over `W`, `T` is a space, and `A.homSource T` is the induced
splitting of `Hom(W', T)`.


### `adaptedHomBasis`

 The invertible adelic matrix (x⁻¹)ᴴ ⊗ 1, where x is the adelic frame of T and 1 is the p×p
identity. 

### `frameAt_homSource`

 In the basis `adaptedHomBasis p T`, the adelic frame of the induced splitting `A.homSource T`
(for the group element `1`) has the three column blocks `1 ⊗ₖ A.kCoordᵀ`,
`stdForm E t ⊗ₖ A.lCoordᵀ` and `1 ⊗ₖ A.iCoordᵀ`. 

### `homSlice_eq_adapted_slice`

 The term `A.homSlice T x` is the mixed term `slice` of the induced splitting
`A.homSource T` at the vector of entries of `x` (`matrixToVec x`), after the change of basis
`adaptedHomBasis p T`. 

### `IsOrthoIntegral.kronecker`

 If `M` and `B` are `IsOrthoIntegral`, so is the Kronecker product of `M` and the entrywise
conjugate `Bᴴᵀ` of `B`. 

### `isAdapted_homSource`

 If the splitting `A` of `W'` over `W` is adapted (`IsBaseAdapted`: its adelic frame is
orthonormal at the infinite places and integral at the finite places), then so is the induced
splitting `A.homSource T` of `Hom(W', T)` over `Hom(W, T)` (`Space.Splitting.IsAdapted`) for the
group element `1` and the change of basis `t = adaptedHomBasis p T = (x⁻¹)ᴴ ⊗ 1`, where `x` is the
adelic frame of `T`. That is, the matrix `(l (t⁻¹)ᴴ, k t, ι)` built from the frames of
`A.homSource T` has orthonormal columns at every infinite place and integral entries at every finite
place. 


## Composition, reindexing and staging of adapted splittings

Bookkeeping for removing hyperbolic planes from a hermitian space in several steps.


### `instance [hD : IsBaseAdapted D] : IsBaseAdapted D.symm`

 If `D` is adapted, so is `D.symm`, the splitting with the frames `k` and `l` exchanged. 

### `isIntMatrix_kAdelic_and_lCoord`

 For an adapted splitting `D`, the adelic matrices `D.kAdelic` (the frame `k` in standard
coordinates) and `D.lCoord` have integral entries: they lie in the ring `O` of adeles whose finite
part lies in `Ô E`, the integral finite adeles. 

### `exists_isBaseAdapted_reindex`

 Let `D` be an adapted splitting of `V'` over `V` with a single hyperbolic plane, given by
`e : Unit ≃ p`. Then there is an adapted splitting indexed by `Unit` with the same embedding `i`,
whose frame `k` is that of `D` reindexed by `e`. 

### `exists_isBaseAdapted_comp_removePlanes`

 Let `D` be an adapted splitting (`IsBaseAdapted`) of `V'` over `V` with `card p` hyperbolic
planes. A splitting is a Witt decomposition with isotropic frames `l`, `k` and an embedding `i` of
`V`. Adapted means the adelic matrix of `l`, `k`, `i` has orthonormal columns at every infinite
place and integral entries at every finite place. For any `e : n₁ ⊕ q ≃ p`, there is an adapted
splitting `A₁` of `V'` over `hyperbolicSum q V` with `card n₁` planes such that
`A₁.comp (removePlanes q V)` has frame `k` equal to `D.k` reindexed by `e` and embedding `i` equal
to `D.i`, where `removePlanes q V` is the tautological splitting of `hyperbolicSum q V` over `V`
with `card q` planes. 

### `instance [hD : IsBaseAdapted D] {r : n₁ → ℤˣ} {W : Space E n₁ r} {A : V.Splitting W q} [hA : IsBaseAdapted A] : IsBaseAdapted (D.comp A)`

 If `D` (a splitting of `V'` over `V`) and `A` (a splitting of `V` over `W`) are adapted, so
is their composite `D.comp A`, a splitting of `V'` over `W`. 
