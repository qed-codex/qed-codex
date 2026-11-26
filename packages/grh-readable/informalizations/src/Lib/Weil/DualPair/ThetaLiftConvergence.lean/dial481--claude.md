---
{
  "module": "src/Lib/Weil/DualPair/ThetaLiftConvergence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/ThetaLiftConvergence.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/ThetaLiftConvergence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Growth of theta kernels and convergence of theta lifts

This file proves growth estimates for theta kernels `(g, h) ↦ θ (ω (g, h) φ)` on the product of
the adelic groups of two spaces `S` and `T`, for a representation `ω`, a functional `θ` and a
vector `φ`. Using reduction theory, it first bounds the norm of `ω (g₀, γ g)`, for fixed `g₀` and
a suitable rational translate `γ g`, by a power of the height `New.Space.height` of `g`. The lift
`New.Space.lift` of a function `y` integrates the kernel against `y g` over `[S] = Γ_S \ G_S`.
For `y` of rapid decay the lift converges, the lifts from `S` and from `T` are transposes of each
other, and the adjoint of the lift for the Petersson products is the descent.

## Main definitions and results

* `New.ThetaKernel.moderate_growth`: the kernel grows at most like a power of the heights
  `New.Space.height`.
* `New.ThetaKernel.integrable_theta_mul`, `New.ThetaKernel.liftBilin`,
  `New.ThetaKernel.exists_clm_lift`: for `y` of rapid decay (`New.Space.rapidFunctions`) the lift
  converges, is bilinear in `φ` and `y`, and is continuous in `φ`.
* `New.ThetaKernel.integral_mul_lift_eq_integral_mul_lift_swap`,
  `New.ThetaKernel.petersson_lift_eq_petersson_descent`: the lifts from `S` and from `T` are
  transposes of each other, and the descent is the adjoint of the lift.

Notions from other files:
* `New.G`: The adelic unitary group G = G_∞ × G_f for signs s at the infinite places and the
  identity matrix at the finite places.
* `New.Space`: A hermitian space with a point: a matrix J over E and x in GL_n(𝔸) with xᴴJx equal to
  diag(s) at the infinite places and 1 at the finite places; Γ = x⁻¹U(J)(E)x.
* `New.Space.IsAutomorphic`, `New.Space.IsRapid`: a function F is automorphic if it is continuous,
  left Γ-invariant and right invariant under an open subgroup of G_f; it is rapid if |F(g)|·ht(g)^B
  is bounded for every B, and moderate (`New.Space.IsModerate`) if |F(g)| ≤ C·ht(g)^A for some C and
  A.

## Relation to the literature

Known; see `Lib.Weil.DualPair.KernelDecay` for sources.



## Bounds on the operators of a theta kernel

Let `Θ` be a theta kernel (`New.ThetaKernel`) for spaces `S` and `V`, acting by ω on a Banach space.


### `exists_norm_le_of_isCompact`

 The operator norms ‖ω(k)‖ of a theta kernel on a Banach space are bounded for k in a compact
subset of the product of the two adelic groups (Banach–Steinhaus). 

### `_root_.New.Space.exists_height_mul_inv_le_max`

 One step of reduction: for `g` an adelic point of the unitary group of `V`, there is an
archimedean point `y` with operator norm at most `2` at every infinite place such that the height of
`g (y,1)⁻¹` is at most half the height of `g`, or at most `2`. Height is 1/λ, where λ is the first
minimum, cut off at 1, of `V` moved by `g`. 

### `_root_.New.Space.exists_reduction_norm_le_height`

 Reduction theory with a height bound: there is a compact set `Ω` such that every `g` has a
rational `γ` and a real point `x` with `γ g x⁻¹ ∈ Ω` and operator norm at most the height of `g`
at every infinite place. Here `x` is the product of a list `l` of real points of norm at most `2`,
and `2 ^ l.length` is at most the height of `g`. 

### `eventually_exists_norm_omega_le_mul_height_pow`

 Fix `g₀` in the group of `S`. For every large exponent `a`, each `g` in the group of `V` has a
rational translate `γ g` such that the operator `ω (g₀, γ g)` has norm at most
`(2 * height g) ^ a`. 

### `_root_.New.norm_realPairWeil_le`

 The real Weil representation of a pair of ranks `n`, `n'`, which depends on `γ`, `γ'` only
through a scalar of modulus one, has at `(y, y')` operator norm at most the norm of the vacuum times
`(‖y‖ ‖y'‖) ^ (n n')`, where the norm of a real point is the product of the operator norms of its
components at the infinite places. 

### `_root_.New.exists_norm_pairWeil_mul_real_le`

 Let `S` and `T` be hermitian spaces of ranks `n` and `n'`, let `a` and `b` be automorphic
characters, and let `pairWeil S T a b` be the resulting Weil representation of the product of the
two adelic unitary groups. For a compact set `Ξ` of adelic points there is a constant `C`, depending
on `S`, `T`, `a`, `b` and `Ξ`, such that for every `z` in `Ξ` and all archimedean points `y`, `y'`
(placed in the infinite components of the two groups), the operator
`pairWeil S T a b (z ((y, 1), (y', 1)))` has norm at most `C (‖y‖ ‖y'‖) ^ (n n')`. Here the norm of
an archimedean point is the product of the operator norms of its components at the infinite places,
and the exponent is the product of the cardinalities of `n` and `n'`. 

 ## Convergence and adjointness of theta lifts of rapid functions 

### `Space.lift`

 The theta lift from S with datum φ is the function h ↦ ∫_{Γ_S\G} θ(ω(g, h)φ) y(g) dg on the
group of T. 

### `Space.ModerateWeight`

 A continuous function `weightFn` of moderate growth on the adelic unitary group of `S`, with a
continuous map `comparisonMap` to the group of `T` whose heights are bounded by a constant times the
heights in `S`. 

### `Space.ModerateWeight.weightFn`

 The weight function, continuous on the group of `S`. 

### `Space.ModerateWeight.comparisonMap`

 A continuous map from the group of `S` to the group of `T`. 

### `Space.ModerateWeight.isModerate`

 The weight function has moderate growth for `S`. 

### `Space.ModerateWeight.height_le`

 The height in `T` of the image of `g` is at most a constant times the height of `g` in `S`. 

### `lift_mul_right`

 Translating the argument of the lift on the right by `k` translates the datum: the lift of `y`
with datum `φ` at `h k` is the lift with datum `K.ω (1, k) φ` at `h`. 

### `swap`

 The theta kernel for the pair `T`, `S`. It uses the representation `(h, g) ↦ ω (g, h)` of the
pair of groups in the other order, and the same functional `K.θ`. Its lifts are the transposed
lifts of `K`. 

### `theta_rat_mul`

 The kernel `g ↦ θ (ω (g, h) φ)` is left invariant under the rational points `S.Γ`. 

### `isAutomorphic`

 If the datum `φ` is fixed by `ω ((1, k), 1)` for `k` in an open subgroup `L` of `G_f`, the
kernel `g ↦ θ (ω (g, h) φ)` is automorphic for `S`: continuous, left invariant under `S.Γ`, and of
some level. 

### `moderate_growth`

 Moderate growth of theta kernels: for a kernel (ω, θ) for S, T there are C and A with
|θ(ω(g, h)φ)| ≤ C‖φ‖(ht(g) ht(h))^A for all g, h and all data φ. 

### `isModerate`

 For fixed `h` and `φ`, the kernel `g ↦ θ (ω (g, h) φ)` has moderate growth on the group of
`S`: it is at most a constant times a power of the height. 

### `fixesLeft_lift`

 The lift is left invariant under the rational points `T.Γ`. 

### `lift_equivariant`

 Equivariance of the theta lift: for a theta kernel and y automorphic on the group of S, the
lift of y with datum φ, at hl, equals the lift of g ↦ y(gk) with datum ω(k, l)φ, at h. 

### `lift_omega_left`

 For `y` automorphic, the lift with datum `ω (k, 1) φ` is the lift of `g ↦ y (g k⁻¹)` with
datum `φ`. 

### `exists_norm_theta_mul_le`

 For `y` automorphic of rapid decay for `S` (`S.rapidFunctions`), the integrand
`θ (ω (g, h) φ) y (g)` of the lift is bounded in `g`: there are `C` and `A` with
`|θ (ω (g, h) φ) y (g)| ≤ ht(h)^A |C| ‖φ‖` for all `φ`, `g` and `h`. 

### `integrable_theta_mul`

 For `y` automorphic of rapid decay for `S`, the integrand `g ↦ θ (ω (g, h) φ) y (g)` of the
lift is integrable on `S.Γ \ G`. 

### `liftBilin`

 The theta lift (φ, y) ↦ `New.Space.lift` K φ y as a ℂ-bilinear map from X and rapidly
decaying automorphic functions for S to functions on the group of T. The definition also takes an
argument `hr : y ∈ S.rapidFunctions` for a function `y` that the map does not use. 

### `exists_clm_lift`

 For y automorphic of rapid decay for S and each h in the group of T, the value at h of the
theta lift of y is a continuous linear functional of the datum φ. 

### `continuous_lift`

 The theta lift of an automorphic function `y` of rapid decay for `S`, with any datum `φ`, is a
continuous function on the group of `T`. 

### `isModerate_lift`

 The theta lift of an automorphic function `y` of rapid decay for `S` has moderate growth on the
group of `T`: its norm is at most a constant times a power of the height. 

### `isLinearMap_petersson_lift`

 For y, y' automorphic of rapid decay on S, T, the Petersson product of y' with the lift of y
is linear in the datum. 

### `integrable_prod_weightFn`

 Let y and F be of rapid decay for S and U, and w a `New.Space.ModerateWeight` from U to T, with
weight function `M = w.weightFn` and map `j = w.comparisonMap`. Then
`(v, g) ↦ M(v) F(v) θ(ω(g, j v) φ) y(g)` is integrable for the product of the quotient measures. 

### `integral_mul_lift_eq_integral_mul_lift_swap`

 For a kernel (ω, θ), y automorphic and rapid on S, and y' automorphic and rapid on T, ∫_{[T]}
y'·(lift of y by φ) equals ∫_{[S]} y·(transposed lift of y' by φ). 

### `petersson_lift_eq_petersson_descent`

 On automorphic functions of rapid decay, the adjoint of the lift for the Petersson products is
the descent, which sends `y'` to the conjugate of the transposed lift of the conjugate of `y'`. 
