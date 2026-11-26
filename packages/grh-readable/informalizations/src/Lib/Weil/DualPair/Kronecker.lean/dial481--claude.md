---
{
  "module": "src/Lib/Weil/DualPair/Kronecker.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/Kronecker.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/Kronecker.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The action x ↦ hxg⁻¹ on matrices as a map of unitary groups

`New.U.kroneckerHom` sends `(g, h)` in `U S × U T` to the Kronecker product `h ⊗ₖ g⁻¹ᵀ`, the matrix
of `x ↦ h x g⁻¹` on matrices indexed by pairs (row, column). Here `New.U J` is the group of
invertible `g` with `gᴴ J g = J`.

* `New.kroneckerGL`: the Kronecker product of two invertible matrices, as an invertible matrix.
* `New.U.kroneckerHom`: the homomorphism of unitary groups.
* `New.map_kronecker`: applying a ring homomorphism entrywise commutes with the Kronecker product.

## Relation to the literature

Known; see `Lib.Weil.DualPair.ThetaLiftConvergence` for sources.


### `New.kroneckerGL`

 The Kronecker product x ⊗ y of invertible matrices x and y over a commutative semiring, as
an invertible matrix with inverse x⁻¹ ⊗ y⁻¹. 

### `New.U.kroneckerHom`

 For SK = 1 and J = T ⊗ Kᵀ, the homomorphism (g, h) ↦ h ⊗ (g⁻¹)ᵀ from U(S) × U(T) to U(J). 

### `New.map_kronecker`

 Applying a ring homomorphism `f` entrywise commutes with the Kronecker product:
(A ⊗ B).map f = A.map f ⊗ B.map f. 
