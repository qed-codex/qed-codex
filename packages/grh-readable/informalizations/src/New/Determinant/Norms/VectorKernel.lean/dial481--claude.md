---
{
  "module": "src/New/Determinant/Norms/VectorKernel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Norms/VectorKernel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Norms/VectorKernel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The theta kernel of a descent pair with values in the weight representation

For a descent pair `O : New.DescentPair` with spaces `W` and `V`, the theta kernels of the data
`v_{P_ξ} ⊗ Ψ_bl ⊗ vac = O.fockDatum ξ` depend linearly on the vector `ξ` of the representation of
weight `(O.columnCount, O.detExp)`. Here `v_{P_ξ}` is the Fock vector of the polynomial
`P_ξ = O.fockPoly ξ`, and `Ψ_bl ⊗ vac = O.blockDatum` is the finite datum: a block datum at the
places of the level and the vacuum at the other finite places. So there is one kernel `θ_W(g, h)`
with values in this representation such that the kernel of `O.fockDatum ξ` is `⟨ξ̄, θ_W(g, h)⟩`. The
pairing `⟨ζ, η⟩` is `New.gramForm ζ η`, conjugate linear in `ζ`.

## Main definitions and results

* `New.DescentPair.vectorKernel`, `New.DescentPair.gramForm_vectorKernel`: the kernel `θ_W(g, h)`
  and its defining property.
* `New.DescentPair.vectorKernelForm`: the function `θ_W(g, ·)` as an algebraic form on `V`.
* `New.DescentPair.normalizedDescent_eq_inner_vectorKernelForm`: the normalized descent
  `New.DescentPair.normalizedDescent` of a form `Ξ` on `V` has the value `⟨θ_W(g, ·), Ξ⟩` at `g`.

Notions from other files:
* `New.DescentPair`: the data of a space `W` of signs `O.signs`, an embedding of its index set in
  that of `V = I_n`, weights and a character, from which `(O.columnCount, O.detExp)` and the level
  are built.
* `New.WeylIndex n κ`: the index set of the coordinates of the representation of weight `κ`, on
  which `New.weylGramOver` is the Gram matrix of `New.gramForm`.
* `New.G E s`, `New.Gf E n`: the adelic unitary group of signs `s` and the finite part of that of
  the standard definite space `New.stdSpace E n = I_n`.
* `New.stdClassSum K f`: the sum of `f` over the double cosets of the rational points and `K`, each
  weighted by the inverse of the order of its automorphism group.


### `conjKernel_apply`

 The value at `ξ` of the linear form `O.conjKernel g h` is the conjugate of the theta kernel at
`(g, h)` of `O.fockDatum (star ξ)`. The kernel `New.pairTheta` is formed with the characters
`O.charW` and `O.charV` at the point `(g, 1, h)`, whose component `(1, h)` in `U(V)(𝔸)` is trivial
at the infinite places. 

### `normalizedDescent_apply`

 The normalized descent `O.normalizedDescent Ξ` of a form `Ξ` on `V = stdSpace E n` has at `g`
the value `∑ O.conjKernel g h (Ξ h) / #(Γ ∩ h K h⁻¹)`, where `h` runs over chosen representatives of
the double cosets `Γ \ U(V)(𝔸_f) / K` of the rational points `Γ` and the level
`K = O.levelGroup`. 

### `vectorKernel`

 The theta kernel `θ_W(g, h)` with values in the representation of weight
`(O.columnCount, O.detExp)`, for `g` in `U(W)(𝔸)` and a finite point `h` of `U(V)`. It is the vector
whose pairing with `ζ` is the theta kernel of the datum `O.fockDatum (star ζ)` at `(g, h)`
(`New.DescentPair.gramForm_vectorKernel`). 

### `gramForm_vectorKernel`

 For every coordinate vector `ζ` of the representation of weight `(O.columnCount, O.detExp)`, the
Gram pairing `⟨ζ, θ_W(g, h)⟩` is the theta kernel `New.pairTheta` of `O.fockDatum (star ζ)` at
`(g, 1, h)`. 

### `gramForm_vectorKernel_left`

 The pairing of the kernel vector `θ_W(g, h) = O.vectorKernel g h` with `ξ` in the Gram form,
conjugate linear in its first argument, is `O.conjKernel g h ξ`, the conjugate of the theta kernel
at `(g, h)` of `O.fockDatum (star ξ)`. 

### `vectorKernel_equivariant`

 Let `O` be a descent pair over a CM field `E` with Weil data, let `g` be an adelic point of the
unitary group of `W`, whose signs are `O.signs`, and `x` a finite point of `U(V)`. For rational `γ`
in `U(V)` and `k` in the level `O.levelGroup`, `θ_W(g, γ x k) = c(k) ρ(γ) θ_W(g, x)`. Here
`θ_W = O.vectorKernel` and `stdEmbFin γ` is the image of `γ` in the finite points. With
`k⁺ = O.colsPlus`, `k⁻ = O.colsMinus` and `N` the rank of `V`, the representation `ρ` has at an
infinite place `τ` the weight with `O.columnCount τ i = k⁺(τ, i) + k⁻(τ, N - i)` columns of height
`i` and the power `O.detExp τ = -∑_{1 ≤ i < N} k⁻(τ, i)` of the determinant. The character
`c = O.levelChar` sends `k` to the product, over the places `w` of the family `O.twistPlace`, of
`(O.tamePart w)⁻¹ (det k_w)`. Here `O.tamePart w` is a multiplicative character of the residue field
at `w`, and `k_w` is the diagonal block of the reduction of `k` at `w` whose rows and columns are
indexed by the image of `O.incl : r ↪ n`, the embedding of the basis indices of `W` in those of
`V`. 

### `vectorKernel_rational_mul`

 For a rational point `γ` of `U(V)`, where `V = stdSpace E n` and `stdEmbFin γ` is the image of
`γ` in the finite points, `θ_W(g, γ x) = ρ(γ) θ_W(g, x)`. With `k⁺ = O.colsPlus`, `k⁻ = O.colsMinus`
and `N` the rank of `V`, the representation `ρ` has at an infinite place `τ` the weight with
`O.columnCount τ i = k⁺(τ, i) + k⁻(τ, N - i)` columns of height `i` and the power
`O.detExp τ = -∑_{1 ≤ i < N} k⁻(τ, i)` of the determinant. 

### `vectorKernel_mul_level`

 For `g` in `U(W)(𝔸)`, the kernel `θ_W(g, ·) = O.vectorKernel g` transforms under right
translation by the level `O.levelGroup` of `U(V)` by the character `O.levelChar`. 

### `vectorKernelForm`

 For `g` in `U(W)(𝔸)`, the function `θ_W(g, ·) = O.vectorKernel g` as an element of `O.FormV`,
the algebraic forms on `V`: smooth functions on the finite points of `U(V)` with values in the
representation of weight `(O.columnCount, O.detExp)` that are equivariant under the rational points
and transform by `O.levelChar` under the level `O.levelGroup`. 

### `normalizedDescent_eq_inner_vectorKernelForm`

 Let `Ξ` be an algebraic form on `V`. The normalized descent `O.normalizedDescent Ξ` has at `g`
the value `⟨θ_W(g, ·), Ξ⟩`, the inner product of the form `θ_W(g, ·) = O.vectorKernelForm g` with
`Ξ`. 
