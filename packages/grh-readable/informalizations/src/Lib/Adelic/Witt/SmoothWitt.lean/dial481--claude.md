---
{
  "module": "src/Lib/Adelic/Witt/SmoothWitt.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Witt/SmoothWitt.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Witt/SmoothWitt.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Smooth families of isometries that carry an isotropic vector to its neighbours

Let `x₀` and `y₀` be isotropic vectors of a hermitian space over `ℂ` that are not orthogonal.
Elements of the unitary group that depend smoothly on `x` carry `y₀` to `x` for isotropic `x` near
`x₀` (they are built as quasi-reflections). For a form given by signs, each such element, composed
with the inverse of the one at `x₀`, carries `x₀` itself to `x`.

The notions used in the statements:
* `U J` is the unitary group of a matrix `J`: the invertible `g` with `gᴴ * J * g = J`.
* `signMatrix ε` is the diagonal matrix of the signs `ε i`, and `USign ε = U (signMatrix ε)`.

## Relation to the literature

Known result: Witt's extension theorem for hermitian forms, here in a smooth local form for
isotropic vectors. See also `Lib.Adelic.Witt.IwasawaDecomposition`.


### `exists_contDiff_mem_eventually_eq_self`

 For every neighbourhood `N` of `x₀` in a finite-dimensional real normed space there is a
smooth map of the whole space into `N` that is the identity near `x₀`. 

### `exists_contDiff_carrying_isotropic`

 Let `J` be an invertible hermitian matrix, and let `x₀` and `y₀` be isotropic and not
orthogonal for the form `(v, w) ↦ star v ⬝ᵥ J *ᵥ w`. There are elements `k x` of the unitary
group `U J` of this form, smooth in `x`, with `k x *ᵥ y₀ = x` for all isotropic `x` near `x₀`. 

### `exists_contDiff_eventually_mulVec_eq`

 Let `x₀ ≠ 0` be isotropic for the form of `signMatrix ε`, the diagonal matrix of the signs `ε`.
There are elements `k x` of its unitary group `USign ε`, smooth in `x`, that carry `x₀` to `x` for
all isotropic `x` near `x₀`. 
