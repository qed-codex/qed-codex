---
{
  "module": "src/Lib/Adelic/Unitary/WeakApproximation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/WeakApproximation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/WeakApproximation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Closed matrix embedding of adelic unitary groups, discrete rational points, weak approximation

This file concerns the adelic unitary group `New.G E s = G_∞ × G_f` over a CM field `E` (hypothesis
`IsCMField E`; the discreteness instance and the `New.Space` results assume `CMType E` instead,
which makes `E` a CM field), together with the rational points of a hermitian space `V` with signs
`s`. When all signs are `1`, the finite parts of the rational points form a discrete subgroup of
`G_f`.

## Main definitions and results

* `New.G.isClosedEmbedding_adeleMatrix`: sending `g` to its adelic matrix is a closed embedding.
  Hence a map into the group is continuous when its matrix is (`New.G.continuous_iff`), and elements
  with the same matrix are equal (`New.G.ext_adeleMatrix`).
* An instance: for a space `W` whose signs are all `1`, the group `New.Space.Γf` of finite parts of
  the rational points is discrete in `G_f`.
* `New.Space.cayleyMap`: a map from all rational matrices to the rational points, through the Cayley
  transform of a rational skew matrix.
* `New.Space.eventually_tendsto_cayleyMap`: for all but finitely many parameters `c`, the image of
  `A` under this map tends to `g` at a given place as `A + e • B` (`A` rational, `B` adelic) tends
  to `V.toRatCoords g`, if the place kills the adeles `e` and `star e`.
* `New.Space.weak_approximation`: weak approximation. The consequence that a rational translate of a
  finite adelic point is integral above a prime is `New.exists_mul_mem_integralAbove`, in
  `Lib.Adelic.AutomorphicForms.PAdicGauge`.

Notions from other files:
* `New.G E s`: the adelic unitary group for the signs `s`; `New.G.adeleMatrix g` is the `n × n`
  matrix over the adeles of its element `g`.
* `New.Space E n s`: a hermitian space with a point, given by a matrix `J` over `E` and `x` in
  `GL_n(𝔸)` with `xᴴ J x` equal to `diag s` at the infinite places and `1` at the finite places.
* `New.Space.ratEmbed`, `New.Space.embFin`: `γ ↦ x⁻¹ γ x` from the rational unitary group of `J` to
  `G`, and its finite part; their images are `New.Space.Γ` and `New.Space.Γf`.
* `New.Space.toRatCoords`: `g ↦ x g x⁻¹` from `G` to the adelic unitary group of `J`.

## Relation to the literature

Known result: weak approximation for unitary groups. Source: V. Platonov, A. Rapinchuk, Algebraic
Groups and Number Theory, 1994, ch. 7. Here a hermitian space comes with an adelic frame to a fixed
diagonal form, and this form is the identity at all finite places, so every space of one signature
shares one adelic group.


 ## Closed embedding into matrices and discreteness of rational points 

### `G.isClosedEmbedding_adeleMatrix`

 Sending an element of the adelic unitary group to its adelic matrix is a closed embedding. 

### `G.ext_adeleMatrix`

 Elements of the adelic unitary group with the same adelic matrix are equal. 

### `G.continuous_iff`

 A map into the adelic unitary group is continuous if and only if its adelic matrix is. 

### `instance {E : Type*} [Field E] [CMType E] (W : Space E n 1) : DiscreteTopology W.Γf`

 For a space `W` whose signs are all `1`, the finite parts of the rational points form a
discrete subgroup `W.Γf` of `G_f`. 


## Weak approximation at infinity and finitely many finite places

Let `x` be the point of `V`. Then `V.toRatCoords g = x g x⁻¹` and `V.ratEmbed γ = x⁻¹ γ x`
translate between `New.G` and the unitary group of `V.J`.

The idea: let `γ = V.toRatCoords g` and take a rational `c` with `star c * c = 1` and `1 + c γ`
invertible at the given places. The Cayley transform of `c γ` is skew for `V.J`, rational skew
matrices `u` approach it, and the rational isometries `c⁻¹ (1 - u) (1 + u)⁻¹` approach `γ`; so
their images under `V.ratEmbed` approach `g`. The matrices `u` come from rational matrices that
approach `γ` (`New.Exchange.denseRange_rat_matrix_add`).


### `instance : Infinite (unitary E)`

 A CM field has infinitely many elements `c` with `star c * c = 1`. 

### `_root_.New.cayleyTransform`

 The Cayley transform `(1 - A) (1 + A)⁻¹` of a square matrix (`0` if `1 + A` is singular). 

### `_root_.New.cayleyTransform_cayleyTransform`

 The Cayley transform is an involution where it is defined: if `2 ≠ 0` in `K` and `1 + A` is
invertible and `C` is the transform of `A`, then `1 + C` is invertible and the transform of `C` is
`A`. 

### `_root_.New.cayleyTransform_eq_inv_mul`

 The two factors of the Cayley transform commute. 

### `_root_.New.cayleyTransform_mul_eq_neg`

 The Cayley transform of an isometry is skew. Here `B` stands for the conjugate transpose of
`A`: if `B J A = J` with `J` and `1 + A` invertible, then `1 + B` is invertible and the
transforms `A'`, `B'` satisfy `B' J = -J A'`. 

### `_root_.New.map_nonsing_inv`

 Inversion of matrices commutes with maps of fields. 

### `_root_.New.cayleyTransform_map`

 The Cayley transform commutes with maps of fields. 

### `_root_.New.continuousAt_cayleyTransform`

 The Cayley transform is continuous where `1 + A` is invertible. 

### `formSkewPart`

 The part of a rational matrix `C` that is skew for the form `J = V.J`, namely
`(C - J⁻¹ Cᴴ J) / 2`. 

### `conjTranspose_formSkewPart_mul`

 The skew part `u` of a matrix satisfies `uᴴ J = -J u`. 

### `smul_cayleyTransform_isometry`

 If `u` is skew for the form of `V`, `1 + u` is invertible and `star c * c = 1`, then `c⁻¹` times
the Cayley transform of `u` is an isometry of `V`. 

### `cayleyMap`

 A map from rational matrices to rational points of the space `V`. For `star c * c = 1` and a
square matrix `A` over `E`, let `u` be the skew part of the Cayley transform of `c A`. The value is
the image under `V.ratEmbed` of the isometry `c⁻¹ (1 - u) (1 + u)⁻¹` of `V.J` if `1 + u` is
invertible, and `1` otherwise. 

### `eventually_tendsto_cayleyMap`

 Let `V` be a hermitian space over the CM field `E`: a matrix `J` with a point `x` in `GL_n(𝔸)`
such that `xᴴ J x` is `diag s` at the infinite places and `1` at the finite places. Let `f` be a
continuous ring map from the adeles to a normed field that kills both the adele `e` and `star e`.
Then for all but finitely many `c` in `E` with `star c * c = 1`, the following holds: when
`A + e • B` tends to `V.toRatCoords g = x g x⁻¹`, with `A` rational (embedded diagonally by
`toAdele`) and `B` adelic, the adelic matrix of the rational point `V.cayleyMap c A` tends to that
of `g` after applying `f`. Here `V.cayleyMap c A` is `x⁻¹ c⁻¹ (1 - u) (1 + u)⁻¹ x`, where `u` is the
skew part of the Cayley transform of `c A`, and it is `1` if `1 + u` is not invertible. 

### `_root_.New.idem_mul_eq_sum_singleAdele`

 For a finite set `T` of finite places, multiplying a finite adele `y` by the idempotent
`idem T` (component `1` on `T` and `0` elsewhere) gives the sum over `w ∈ T` of the adeles
`singleAdele w (evalAt w y)` with component `evalAt w y = y w` at `w` and `0` elsewhere. 

### `_root_.New.G.tendsto_componentOn`

 Convergence in `G` from convergence place by place: for an adele `a`, `a.1 w` is its component
at an infinite place and `evalAt w a.2` at a finite one. If the matrices of `x i` tend to the
matrix of `g` at every infinite place and at every place of the finite set `S` or conjugate to
one (`S.conjClosure`), then `x i` tends to `g` once the components at all other finite places are
replaced by `1` (`componentOn n S`). 

### `weak_approximation`

 Weak approximation. For a finite set `S` of finite places, the products `γ * (1, h)` are dense
in the adelic unitary group `G = G_∞ × G_f`, where `γ` runs over the rational points `V.Γ` and
`h` over the elements of `G_f` with component `1` at every place of `S`. So `V.Γ` is dense at
infinity and at the places of `S`. 
