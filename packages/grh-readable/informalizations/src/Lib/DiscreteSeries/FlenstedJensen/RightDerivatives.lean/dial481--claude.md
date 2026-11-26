---
{
  "module": "src/Lib/DiscreteSeries/FlenstedJensen/RightDerivatives.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/FlenstedJensen/RightDerivatives.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/FlenstedJensen/RightDerivatives.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Right derivatives and bump convolution for smooth functions on U(p,q)

The file develops differential calculus on `U(p,q) = New.USign ε = U(diag ε)`. A smooth function on
the group is by definition the restriction of a smooth function on the matrix space, so no manifold
structure is needed. Continuous functions are convolved with compactly supported smooth functions
(bumps).

## Main definitions and results

* `New.smoothMatrixFunctions`, `New.SmoothU`: smooth `E`-valued functions on matrices, and their
  restrictions.
* `New.rightDerivMatrix`, `New.rightDeriv`: `gl_n(ℂ)` acts on them by right derivatives. An element
  `Y` of the real Lie algebra `New.unitaryLie J` acts by `f ↦ (x ↦ df_x(x Y))`, and the action
  extends `ℂ`-linearly through the splitting `X = Y₁ + i Y₂` of `New.eq_unitaryLiePart_add_I_smul`.
* `New.DiscreteSeries.Bumps`, `New.DiscreteSeries.bumpDeriv`: the smooth compactly supported
  functions, and the action on them of `gl n` by right derivatives.
* `New.DiscreteSeries.smear`: for continuous `F`, the linear map `α ↦ (g ↦ ∫ y, α y⁻¹ • F (g * y))`.
* `New.DiscreteSeries.hasDerivAt_smear`, `New.DiscreteSeries.rightDeriv_smear`: a right derivative
  of the convolution falls on `α`.

Notions from other files:
* `New.USign`: for a vector of signs `ε`, the unitary group `U J` of the diagonal matrix
  `J = diag ε`, which is `New.signMatrix ε`. For `g` in the group, `g.val.val` is its matrix.
* `New.unitaryLie`: the Lie algebra of `U J`, the real vector space of complex matrices `X` with
  `Xᴴ * J + J * X = 0`.
* `New.expU`: for `X` in `New.unitaryLie J`, the matrix exponential of `X` as an element of `U J`.
* `New.GlModule`: a `gl_n(ℂ)`-module structure on a complex vector space `M`, that is, a linear map
  from `n × n` matrices to endomorphisms of `M` that respects commutators.

## Relation to the literature

They are used for the function of Flensted-Jensen, the coefficient of the lowest K-type of a
discrete series (see `Lib.DiscreteSeries.FlenstedJensen.PsiKTypes`), and for two known results:
Schur orthogonality, and the fact that coefficients of integrable discrete series are cusp forms
(see `Lib.DiscreteSeries.CuspKernel`).


 ## Right derivatives of smooth functions as a gl_n-module 

 ### Smooth functions and the exponential map 

### `smoothMatrixFunctions`

 The space of real-smooth functions from complex `n × n` matrices to `E`. 

### `hasDerivAt_expU`

 For `g` in the unitary group `U J` and `Y` in its Lie algebra, the matrix of the curve
`s ↦ g exp(s Y)` has derivative `g exp(t Y) Y` at `t`. 

### `smoothMatrixFunctions.restrictU`

 The restriction to the group `U(diag ε)` of a smooth function on all matrices. 

### `SmoothU`

 Smooth functions on `U(diag ε)`: the restrictions to the group of the smooth functions on all
matrices. 

 ### The action induced on the range of a linear map 

### `GlModule.onRange`

 The action induced on the range of a linear map `ι` whose kernel is stable under the action,
through `M ⧸ ker ι ≃ range ι`: `X` sends `ι x` to `ι (X x)` (see `GlModule.onRange_apply`). 

### `GlModule.onRange_apply`

 The action induced by `ρ` on the range of `ι` sends `ι x` to `ι (X x)`. 

### `GlModule.exists_action_on_range`

 If the kernel of a linear map `ι` on a `gl_n`-module `ρ` is stable under the action, the action
descends to the range of `ι`: there is a `gl_n`-module structure `σ` on the range for which `ι`
commutes with the action of every matrix. 

 ### The splitting of `gl_n(ℂ)` and derivatives along linear vector fields 

### `unitaryLiePart`

 The component `(X - J⁻¹ Xᴴ J) / 2`, with `J = diag ε`, of a complex matrix `X` in the real Lie
algebra `𝔲` of `U(diag ε)`, for the splitting `gl_n(ℂ) = 𝔲 ⊕ i𝔲` (see
`eq_unitaryLiePart_add_I_smul`). 

### `eq_unitaryLiePart_add_I_smul`

 Every complex matrix `X` is `Y₁ + i Y₂`, where `Y₁ = unitaryLiePart ε X` and
`Y₂ = unitaryLiePart ε (-i X)` are the components of `X` and `-i X` in the real Lie algebra of
`U(diag ε)`. 

### `smoothMatrixFunctions.mulRightDeriv`

 The derivative along the vector field `x ↦ x Y` on matrices: it sends a smooth function `f` to
`x ↦ df_x(x Y)`. 

 ### The action of `gl_n(ℂ)` by right derivatives 

### `rightDerivMatrix`

 Right derivatives on smooth functions of a matrix. For `X = Y₁ + i Y₂` with
`Y₁ = unitaryLiePart ε X` and `Y₂ = unitaryLiePart ε (-i X)` in the real Lie algebra of
`U(diag ε)`, `X` sends `f` to `x ↦ df_x(x Y₁) + i df_x(x Y₂)`. 

### `rightDerivMatrix_apply_apply`

 The right derivative on matrices of a smooth function `f` along `X = Y₁ + i Y₂`, with
`Y₁ = unitaryLiePart ε X` and `Y₂ = unitaryLiePart ε (-i X)`, is `df_x(x Y₁) + i df_x(x Y₂)`
at `x`. 

### `restrictU_rightDerivMatrix_eq_zero`

 If a smooth function on matrices vanishes on the group `U(diag ε)`, then so does its right
derivative along every complex matrix `X`. 

### `rightDeriv`

 The `gl_n(ℂ)`-module of smooth functions on `U(diag ε)` under complexified right derivatives:
the action that `rightDerivMatrix` induces on restrictions to the group, well defined by
`restrictU_rightDerivMatrix_eq_zero`. See `rightDeriv_restrictU` and `hasDerivAt_curve`. 

### `rightDeriv_restrictU`

 The right derivative along `X` of the restriction to the group of a smooth function `F` on
matrices is the restriction of `rightDerivMatrix ε E X F`, its right derivative on matrices. 

### `hasDerivAt_curve`

 Chain rule along a curve `γ` in the group `USign ε = U(diag ε)`: if the matrix of `γ` satisfies
`γ'(t) = γ(t) X`, then, for a smooth function `f` on the group, the derivative of `f ∘ γ` at `t` is
the right derivative `rightDeriv ε E X f` of `f` along `X` at `γ t`. 

### `hasDerivAt_rightDeriv_expU`

 For a smooth function `f` on the group `USign ε = U(diag ε)`, a point `g` of the group and `Y`
in its real Lie algebra, the derivative of `s ↦ f (g exp(s Y))` at `t` is the right derivative
`rightDeriv ε E Y f` of `f` along `Y` at `g exp(t Y)`. 

### `rightDeriv_apply_eq_of_hasFDerivAt`

 If a smooth function `f` on the group `USign ε = U(diag ε)` is the restriction of a function `F`
on matrices with complex derivative `D` at `g`, then the right derivative `rightDeriv ε E X f` of
`f` along a complex matrix `X` has the value `D (g X)` at `g`. 

### `rightDeriv_comp_clm`

 Right derivatives of smooth functions on the group `USign ε = U(diag ε)` are local and commute
with continuous linear forms `L`: if `f' = L ∘ f` near `g`, then `X f' = L ∘ X f` near `g`, where
`X f = rightDeriv ε E X f` is the right derivative along the complex matrix `X`. 

 ## Convolution with bump functions and its right derivatives 

### `Bumps`

 The smooth complex functions with compact support on `U(diag ε)`. 

### `bumpDeriv`

 The `gl n`-module of smooth compactly supported functions: the restriction of
`rightDeriv ε ℂ`. A right derivative vanishes near every point outside the support. 

### `norm_bump_smul_sub_le_indicator`

 Let `A` be a smooth extension of a bump function `α` to all matrices, let `N` be a set in
`U(diag ε)` and let `K = tsupport α * N⁻¹`. If `A` is `L`-Lipschitz on the matrices of `K * N`,
then, for `g` and `g₀` in `N`, the function `y ↦ α (y⁻¹ * g) • F y - α (y⁻¹ * g₀) • F y` is
bounded by `‖F y‖ * L * ‖y⁻¹‖ * ‖g - g₀‖` on `K⁻¹` and vanishes elsewhere. 

### `integrable_bump_inv_smul`

 For continuous `F` and a smooth compactly supported `α`, the function `y ↦ α y⁻¹ • F y` on
`U(diag ε)` is integrable for the invariant measure. 

### `smear`

 Convolution with the continuous function `F`: the linear map that sends `α` to the function
`g ↦ ∫ y, α y⁻¹ • F (g * y)`. 

### `smear_apply_eq_integral_inv_mul`

 By invariance of the measure, the convolution `smear F` of a bump function `β` at `g` is
`∫ y, β (y⁻¹ * g) • F y`, in which the variable `g` sits in `β`. 

### `hasDerivAt_smear`

 If a curve `γ` in `U(diag ε)` has `γ'(t) = γ(t) X`, then, for continuous `F` and a smooth
compactly supported `α`, the convolution `smear F α : g ↦ ∫ y, α y⁻¹ • F (g * y)` along `γ` has at
`t` the derivative `smear F (X α) (γ t)`, where `X α = bumpDeriv X α` is the right derivative. 

### `rightDeriv_smear`

 Suppose the convolution `smear F α` of a continuous function `F` with a bump function `α` is
the smooth function `f`. Then for every matrix `X`, the convolution with the right derivative
`bumpDeriv X α` is the right derivative of `f` along `X`. 
