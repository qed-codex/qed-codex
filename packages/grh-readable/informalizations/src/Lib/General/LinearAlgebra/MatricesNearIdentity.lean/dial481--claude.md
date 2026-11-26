---
{
  "module": "src/Lib/General/LinearAlgebra/MatricesNearIdentity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/MatricesNearIdentity.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/MatricesNearIdentity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Matrices near the identity: Jacobi's formula and norm estimates

This file collects known facts on complex matrices near the identity.
It proves Jacobi's formula for the derivative of the determinant at the identity and
`det (exp M) = exp (tr M)`.
Estimates in the Hilbert–Schmidt norm, which is the norm of all matrices in this file, control the
inverse and the logarithm of `1 + X` and the exponential of `X`.
The logarithm of an element of `USign ε` near `1` lies in the Lie algebra.
A matrix at distance less than `1` from the identity is accretive.

## Main definitions and results

* `New.hasDerivAt_det_of_eq_one`: along a differentiable curve of complex matrices through the
  identity, the derivative of the determinant there is the trace of the velocity.
* `New.DiscreteSeries.logOneAdd` and `exp_logOneAdd`: the logarithm of `1 + X` for `‖X‖ ≤ 1 / 2`.

Notions from other files:
* `signMatrix ε` is the diagonal matrix with entries `ε i = ±1`, and `USign ε` is its unitary group.
* `unitaryLie J` is the space of matrices `X` with `Xᴴ * J + J * X = 0`.
* `entryMask r X` keeps the entries `(i, j)` of `X` with `r i j` and replaces the others by `0`.
* A matrix `A` is accretive (`A.IsAccretive`) if `A + Aᴴ` is positive definite.


 ## Jacobi's formula for the derivative of the determinant 

### `New.hasDerivAt_det_of_eq_one`

 Jacobi's formula at the identity: if `γ s = 1` and `γ` has derivative `Y` at `s`, then
`det ∘ γ` has derivative `Y.trace` at `s`. 


## Matrices near the identity in the Hilbert–Schmidt norm

The main results are the bound `‖tr (X Y)‖ ≤ ‖X‖ ‖Y‖`, invariance under unitary left factors, the
inverse of `1 + X` for small `X`, the formula `det (exp M) = exp (tr M)`, and the logarithm of
`1 + X`, written as the integral of `(1 + s X)⁻¹ X` over `[0, 1]`. The logarithm of an element of
`USign ε` near `1` lies in the Lie algebra, and a matrix at distance less than `1` from the identity
is accretive.


### `intDiagonal`

 An integral weight as a diagonal matrix. 

### `norm_trace_mul_le_norm_mul_norm`

 The Cauchy–Schwarz inequality for the trace form: `‖tr (X * Y)‖` is at most the product of the
Hilbert–Schmidt norms of `X` and `Y`. 

### `frobenius_norm_mul_of_unitary`

 Left multiplication by a unitary matrix preserves the Hilbert–Schmidt norm. 

### `norm_inv_one_add_sub_one_le`

 If `X` has Hilbert–Schmidt norm at most `1 / 2`, then `(1 + X)⁻¹` is within `2 * ‖X‖` of `1`. 

### `logOneAdd`

 The logarithm of `1 + X`, as the integral of `(1 + s • X)⁻¹ * X` over `[0, 1]`. 

### `continuousAt_inv_one_add_smul_mul`

 For `‖X‖ ≤ 1 / 2` the integrand of `logOneAdd X` is continuous at every point of `[0, 1]`. 

### `continuousOn_inv_one_add_smul_mul`

 For `‖X‖ ≤ 1 / 2` the integrand of `logOneAdd X` is continuous on `[0, 1]`. 

### `hasDerivAt_integral_inv_one_add_smul_mul`

 For `‖X‖ ≤ 1 / 2` and `0 ≤ s ≤ 1` the integral of `(1 + u • X)⁻¹ * X` over `[0, t]` has
derivative `(1 + s • X)⁻¹ * X` at `t = s`. 

### `commute_intervalIntegral`

 A matrix that commutes with all values of a continuous function `G` commutes with its
integral. 

### `intervalIntegrable_trace_mul_inv_one_add_smul_mul`

 For `‖X‖ ≤ 1 / 2` the function `s ↦ tr (D * (1 + s • X)⁻¹ * X)` is integrable on `[0, 1]`. 

### `integral_trace_mul_inv_one_add_smul_mul`

 For `‖X‖ ≤ 1 / 2` the integral of `s ↦ tr (D * (1 + s • X)⁻¹ * X)` over `[0, 1]` is
`tr (D * logOneAdd X)`, where `logOneAdd X` is the integral of `(1 + s • X)⁻¹ * X`. 

### `hasDerivAt_det_exp_smul`

 Jacobi's formula along `t ↦ exp (t • M)`: the derivative of `det (exp (t • M))` at `s` is
`det (exp (s • M)) * tr M`. 

### `det_exp`

 The determinant of the exponential of a matrix is the exponential of its trace. 

### `hasDerivWithinAt_exp_neg_of_commute`

 If `L` has derivative `L'` at `s` and `L s` commutes with `L t` for all `t ∈ S`, then
`exp (-L t)` has derivative `exp (-L s) * -L'` at `s` within `S`. 

### `inv_one_add_smul_mul_mul_one_add_smul`

 For `‖X‖ ≤ 1 / 2` and `0 ≤ s ≤ 1` the matrix `(1 + s • X)⁻¹ * X` times `1 + s • X` is `X`. 

### `exp_logOneAdd`

 If the Hilbert–Schmidt norm of `X` is at most `1 / 2`, then `logOneAdd X`, the integral of
`(1 + s • X)⁻¹ * X` over `[0, 1]`, is a logarithm of `1 + X`. 

### `conjTranspose_inv_one_add_smul_mul_form`

 If `1 + X` preserves the form `J`, that is `(1 + X)ᴴ * J * (1 + X) = J`, and `‖X‖ ≤ 1 / 2`, then
for `0 ≤ s ≤ 1` the integrand `G s = (1 + s • X)⁻¹ * X` of `logOneAdd X` satisfies
`(G s)ᴴ * J = -(J * G (1 - s))`. 

### `logOneAdd_mem_unitaryLie`

 Let `g` be in `USign ε`, the unitary group of the sign matrix `J = signMatrix ε`, with
Hilbert–Schmidt distance at most `1 / 2` from `1`. Then its logarithm `L = logOneAdd (g - 1)` lies
in the Lie algebra `unitaryLie J`, that is, `Lᴴ * J + J * L = 0`. 

### `norm_exp_sub_one_le`

 If `X` has Hilbert–Schmidt norm at most `1`, then `exp X` is within `2 * ‖X‖` of `1`. 

### `norm_logOneAdd_le`

 If `X` has Hilbert–Schmidt norm at most `1 / 2`, then `logOneAdd X`, the integral of
`(1 + s • X)⁻¹ * X` over `[0, 1]`, has norm at most `2 * ‖X‖`. 

### `norm_proj_mul_le`

 If `P` is an orthogonal projection and `X` has Hilbert–Schmidt norm at most `ρ`, then so has
`P * X`. 

### `coordProj`

 The diagonal matrix whose entry at `i` is `1` if `p i` holds and `0` otherwise. It is the
coordinate projection onto the indices satisfying `p`. 

### `norm_entryMask_le`

 Replacing some entries of a matrix by `0` does not increase its Hilbert–Schmidt norm. 

### `pos_of_mem_spectrum_add_star`

 If `X` has Hilbert–Schmidt distance less than `1` from the identity, then the real spectrum of
`X + star X` is positive. 

### `isAccretive_of_norm_sub_one_lt`

 A matrix `X` at Hilbert–Schmidt distance less than `1` from the identity is accretive, that is,
`X + Xᴴ` is positive definite. 
