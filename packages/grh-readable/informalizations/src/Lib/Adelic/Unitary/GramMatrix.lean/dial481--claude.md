---
{
  "module": "src/Lib/Adelic/Unitary/GramMatrix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/GramMatrix.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/GramMatrix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Gram matrix of a space is invertible and hermitian; group elements from isometries

Let `E` be a number field and `s : n → ℤˣ` a family of signs. The standard form `New.stdForm E s`
is its own inverse. It is hermitian when `E` has a CM type (`CMType E`), and then the Gram matrix
of a space is invertible and hermitian. For a CM field, matrices that preserve the standard form
give elements of the adelic unitary group.

## Notation

* `New.𝔸 E`: the adeles of `E`, with the diagonal embedding `New.toAdele : E →+* 𝔸 E`, given at
  the infinite places by the chosen CM type of `E`.
* `New.stdForm E s`: the diagonal adelic matrix with the signs `s` at the infinite places and `1`
  at the finite places.
* `New.Space E n s`: a matrix `J` over `E` with an invertible adelic matrix `x` such that
  `xᴴ * J.map toAdele * x` is `New.stdForm E s`.
* `New.G E s`: the adelic unitary group of the standard form; `New.G.adeleMatrix` is the matrix of
  an element.

## Main definitions and results

* `New.Space.isUnit_J`, `New.Space.isHermitian_J`: `J` is invertible and hermitian.
* `New.G.ofMatrix`: the group element given by a matrix that preserves the standard form.


### `stdForm_mul_self`

 The standard form `stdForm E s`, which is diagonal with the signs `s` at the infinite places
and `1` at the finite places, is its own inverse. 

### `conjTranspose_stdForm`

 The standard form `stdForm E s`, a diagonal matrix with the signs `s` at the infinite places
and `1` at the finite places, is hermitian. 

### `conjTranspose_map_toAdele`

 The diagonal embedding `toAdele` of `E` in its adeles, given at the infinite places by the CM
type, commutes with the conjugate transpose of matrices. 

### `map_J`

 A space `V` is a matrix `J` over `E` with an invertible adelic matrix `x` such that
`xᴴ J x = S`, where `S = stdForm E s` is the diagonal matrix of signs and `toAdele` maps `E` to
its adeles. Over the adeles `J = (x⁻¹)ᴴ S x⁻¹`. 

### `conjTranspose_mul_J_mul_swap`

 The Gram matrix `J` of a space `V` is hermitian, so for matrices `X`, `Y` over `E` with rows
indexed by `n`, the matrix `Yᴴ J X` is the conjugate transpose of `Xᴴ J Y`. 

### `G.ofMatrix`

 The element of the adelic unitary group `G E s` given by an adelic matrix `m` with
`mᴴ S m = S`, where `S` is the standard form `stdForm E s`. 

### `G.adeleMatrix_ofMatrix`

 For a CM field `E` and signs `s` indexed by a finite type `n`, let `S = stdForm E s` be the
diagonal adelic matrix with the signs `s` at the infinite places and `1` at the finite places. If an
adelic matrix `m` satisfies `mᴴ S m = S`, the element `G.ofMatrix m h` of the adelic unitary group
`G E s` of `S` has matrix `m`. 
