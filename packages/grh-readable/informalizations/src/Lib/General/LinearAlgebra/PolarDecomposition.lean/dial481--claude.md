---
{
  "module": "src/Lib/General/LinearAlgebra/PolarDecomposition.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/PolarDecomposition.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/PolarDecomposition.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Gram–Schmidt, tight frames, polar decomposition in U(p,q), forms representing one

This file collects four topics of linear algebra. The first is a Gram–Schmidt process
whose change of basis is block triangular for a weight on the columns. The second concerns tight
frames of `ℂ^Φ` made of vectors of the lattice `𝔞₀` attached to a CM field. The third is the polar
decomposition in the unitary group of a diagonal sign form, with properties of accretive matrices.
The last gives a condition under which a Hermitian form takes the value `1` on a subspace.

## Main definitions and results

* `New.exists_orthonormal_mul`: the columns of a complex matrix with a left inverse
  (`New.HasLeftInv`) become orthonormal after right multiplication by an invertible matrix `b` that
  is block triangular for a given weight `wt` on the columns: `b i j = 0` whenever `wt j < wt i`.
* `New.IsTightFrame`: vectors of `𝔞₀`, with multiplicities, that form a tight frame of `ℂ^Φ`.
* `New.exists_polar`: `g = k * z` with `k` unitary and `z` positive definite and an exponential.
* `New.isAccretive_blockDiagPart_inv_mul`: the block diagonal part of `g` is invertible and
  `(blockDiagPart ε g)⁻¹ * g` is accretive.
* `New.exists_mem_dotProduct_mulVec_eq_one`: a Hermitian form on `ℂ^m` that is not negative
  semidefinite on a subspace takes the value `1` on that subspace.

Notions from other files:
* `New.signMatrix ε`: the diagonal matrix of the signs `ε`; `New.USign ε` is its unitary group, the
  invertible complex matrices `g` with `gᴴ * signMatrix ε * g = signMatrix ε`.
* `New.unitaryLie J`: the Lie algebra of this group for `J = signMatrix ε`: the real vector space
  of complex matrices `X` with `Xᴴ * J + J * X = 0`; `New.expU X` is `exp X` in the group.
* `Matrix.IsAccretive z`: the matrix `z + zᴴ` is positive definite.
* `New.WeilData E`: data on a CM field `E`; only its finite idele `α` is used here.


 ## Gram–Schmidt with a block triangular change of basis 

### `New.exists_orthonormal_mul`

 Gram–Schmidt: if the complex n × k matrix X has a left inverse and wt is a weight on its
columns with values in a linear order, then there is an invertible matrix b, block upper triangular
for wt, such that the columns of X b are orthonormal. 


## Tight frames in the lattice 𝔞₀

For a CM field `E` with CM type `Φ` (`New.CMType`) and the finite idele `α` of `New.WeilData`,
`𝔞₀ = E ∩ α Ô` is a lattice in `ℂ^Φ`; `New.Ô` is the ring of integral finite adeles.


### `finiteImage`

 The finite image of a family w of elements of E: the finite adelic vector α⁻¹w, with α the
idele of the Weil data. 

### `IsTightFrame`

 The w_i lie in the lattice E ∩ αÔ and, taken m_i times, form a tight frame with frame bound M.
That is, ∑ m_i Φσ(w_i)·conj(Φτ(w_i)) = Mδ_{στ} for all infinite places σ, τ of E, with Φ the CM
type. 

### `IsTightFrame.finiteImage_mem`

 Each w_i lies in the lattice E ∩ αÔ. 

### `IsTightFrame.sum_mul_conj`

 The matrix ∑ m_i Φσ(w_i)·conj(Φτ(w_i)) is M times the identity. 

### `IsTightFrame.repeat_vectors`

 Let E be a CM field with CM type Φ and Weil data. If the w_i, taken with multiplicities m_i, are
a tight frame with bound M (they lie in the lattice E ∩ αÔ and ∑ m_i Φσ(w_i)·conj(Φτ(w_i)) = Mδ_στ),
then so is the family with each w_i repeated m_i times, all with multiplicity one. 

 ## Polar decomposition in U(p,q) and accretive matrices 

### `New.exists_polar`

 Polar decomposition in `USign ε = U(diag ε)`, the unitary group of the diagonal form with signs
ε: every g is kz with k in `maxCompactU ε`, the subgroup of unitary matrices, and z positive
definite and in the range of `expU`, the exponential map on the Lie algebra of the group. 

### `Matrix.IsAccretive.setOf_mem_nhds`

 The accretive matrices, those with `z + zᴴ` positive definite, form a neighbourhood of each
accretive matrix `z`. 

### `Matrix.IsAccretive.weightMinors_ne_zero`

 If `z` is accretive (`z + zᴴ` positive definite) and `w` assigns integer weights to the indices,
then `weightMinors w z` is non-zero. Here `weightMinors w z` is the product over `t : ℤ` of the
principal minor of `z` on `{i | t ≤ w i}`, each factor with `t ≤ 0` divided by `det z`. 

### `Matrix.IsAccretive.conjTranspose_mul_mul`

 If `z` is accretive (`z + zᴴ` positive definite) and `k` has non-zero determinant, then
`kᴴ * z * k` is accretive. 

### `Matrix.IsAccretive.det_ne_zero_and_inv_mul`

 If `k⁻¹ * z` is accretive (its sum with its conjugate transpose is positive definite), then `z`
has non-zero determinant and `z⁻¹ * k` is accretive. 

### `New.isAccretive_blockDiagPart_inv_mul`

 For g in `USign ε`, the unitary group of the diagonal form with signs ε, the block diagonal
part B of g (the entries g_ij with ε_i = ε_j) is invertible and B⁻¹ g is accretive: the sum of
B⁻¹ g and its conjugate transpose is positive definite. 

 ## Hermitian forms that represent one 

### `New.exists_mem_dotProduct_mulVec_eq_one`

 If the form `v ↦ star v ⬝ᵥ β *ᵥ v` of a Hermitian matrix `β` is not negative semidefinite on a
subspace `S`, then it takes the value `1` on `S`. 
