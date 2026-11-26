---
{
  "module": "src/Lib/Adelic/AutomorphicForms/UnipotentRadical.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/UnipotentRadical.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/UnipotentRadical.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The mean along a unipotent radical vanishes; reduction in the radical

This file defines the adelic unipotent radical `New.unipotentRadical` of the stabiliser of the
span of the columns of an isotropic adelic matrix. A bounded continuous function that is fixed by
right convolution with a cusp kernel `e` (`New.IsCuspKernel`) and invariant under the rational
points of the radical, of finite covolume, has mean zero along the radical. From this it derives a
bound by the oscillation for such functions. It also gives the matrix algebra for the reduction
step, `New.Reduction.radicalElem` and `New.Reduction.IsIntBounded`, which moves an adelic point of a
unipotent radical close to `1` by a rational element.

## Main definitions and results

* `New.Space.integral_unipotentRadical_eq_zero`: the mean along the radical vanishes.
* `New.unipotentRadical`: the points `g` of the adelic unitary group that fix the span `A` of the
  columns of `a` pointwise and satisfy `uᴴ J (g v) = uᴴ J v` for all `u`, `v` in `A^⊥`, where
  `J = stdForm E s`.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to diag(s) at the infinite places and 1 at the finite places (in the coordinates x⁻¹ X this
  form is the adelic matrix `stdForm E s`); `V.Γ` is its group of rational points in the adelic
  group G = G_∞ × G_f, and `V.move g` has the point xg.
* `New.realConv`: R(k)F(g) = ∫ k(x) F(gx) dx over G_∞ (`New.GInf`, one copy of U(diag s) for each
  infinite place of E), for k on G_∞ and F on G.
* `New.IsCuspKernel`: a minimal idempotent for convolution on G_∞ that decays polynomially and is
  reproduced by a compactly supported function.
* `New.dilationGroup a`: the pairs (g, c) such that g is the scalar c on the columns of a and
  wᴴ J (g v) = wᴴ J v for all v, w orthogonal to these columns.

## Relation to the literature

Known; see `Lib.Adelic.AutomorphicForms.Cuspidality` for sources.


 ## The mean along a unipotent radical vanishes 

### `mk_one_mem_dilationGroup_iff`

 An element `x` of the unitary group of `J` is a dilation along `A` by the factor `1` if and only
if it fixes `A` and `wᴴ J x v = wᴴ J v` for all `v`, `w` orthogonal to `A`. 

### `unipotentRadical`

 The points `g` of the adelic unitary group that fix the span `A` of the columns of `a` pointwise
and satisfy `uᴴ J (g v) = uᴴ J v` for all `u`, `v` in `A^⊥`, where `J = stdForm E s`. For isotropic
`A` with `A^⊥⊥ = A` these are the points that fix `A` and `A^⊥ / A` pointwise: the unipotent radical
of the stabiliser of `A`. 

### `conjTranspose_map_evalInf_mul_signMatrix_mul`

 The pairing `xᴴ (stdForm E s) y` of two adelic matrices, read at an infinite place `w`, is the
pairing of their components at `w` for the diagonal matrix of the signs `s`. 

### `mem_unipotentRadical_iff`

 A point `g` lies in the radical of `a` if and only if it fixes `a` and `uᴴ J g v = uᴴ J v` for
all `v`, `u` orthogonal to `a`, where `J` is the standard form. 

### `isClosed_unipotentRadical`

 The radical is closed in the adelic unitary group. 

### `mk_one_mem_unipotentRadical`

 If at every infinite place `w` the component `r w` of a real point `r` is a dilation by the
factor `1` along the component of `a`, then `(r, 1)` lies in the adelic radical of `a`. 

### `abs_log_norm_inv_mul_sub_le`

 For a matrix `A ≠ 0`, the function `x ↦ log ‖x⁻¹ A‖` on the unitary group of signature `s`
changes by at most `‖y‖` under right translation by `y` (operator norms). 

### `log_norm_inv_mul_of_mem_dilationGroup`

 If `r ∈ U(diag s)` dilates the non-zero matrix `A` by the factor `c` (in particular
`r A = c A`), left translation by `r` lowers `log ‖x⁻¹ A‖` by `log ‖c‖`. 

### `IsCuspKernel.integral_mul_eq_zero`

 For E a CM field, let `GInf E s` be the product of the unitary groups U(diag s) over the
infinite places, and `A` a family of non-zero matrices with (A w)ᴴ diag(s) A w = 0. A cusp kernel
`e` of order `B` is a minimal idempotent with ‖x‖^(B+1)e(x) integrable, ‖x‖^B e(x) bounded and α ∗
e = e for some compactly supported continuous α. It annihilates every bounded continuous `Ψ` that is
left invariant under each `r` whose components `r w` fix the columns of `A w` and satisfy vᴴ diag(s)
(r w) u = vᴴ diag(s) u for v, u orthogonal to them: `∫ e(x) Ψ(y x) dx = 0` for all `y`.

A case of Harish-Chandra's theorem that the K-finite coefficients of a discrete series have
vanishing constant terms. 

### `integral_unipotentRadical_eq_zero`

 The mean along a unipotent radical vanishes. Let `N` be the radical of an isotropic adelic
matrix `a` that vanishes at no infinite place, let `Γ` be the group of rational points of `W`, and
let `Γ ∩ N` have finite covolume in `N`. If the bounded continuous function `F` is fixed by right
convolution with a cusp kernel `e` and `F (g ·)` is left invariant under `Γ ∩ N`, the integral of
`F (g v y)` over `v ∈ (Γ ∩ N) \ N` is zero for every real `y`. Integrals over the quotient are taken
against `Subgroup.quotMeasure`, the Haar measure of `N` weighted by a cutoff for `Γ ∩ N`. 

### `isFiniteMeasure_quotMeasure_of_isCompact`

 Let `Γ` be the group of rational points of `W`. If the radical `N` of `a` lies in `(Γ ∩ N) K`
with `K` compact, then `Γ ∩ N` has finite covolume in `N`. 

### `norm_le_of_integral_eq_zero`

 Let `Γ` be the group of rational points of `W`, and let the radical `N` of `a` lie in
`(Γ ∩ N) K` with `K` compact. If a continuous function `f`, left invariant under `Γ ∩ N`, has
integral zero over `(Γ ∩ N) \ N` and stays within `D` of a number `c` on `K`, then `‖c‖ ≤ D`. 

### `norm_le_of_dist_le`

 A bound by the oscillation. Let `a` be isotropic and vanish at no infinite place, and let its
radical `N` lie in `(Γ ∩ N) K`, with `Γ` the rational points of `W` and `K` compact. Let `F` be
bounded, continuous and fixed by right convolution with a cusp kernel `e`, with `F (g ·)` left
invariant under `Γ ∩ N`. If `F (g x y)` is within `D` of `F (g y)` for all `x ∈ K`, with `y` real,
then `‖F (g y)‖ ≤ D`. 


## Unipotent radical elements and bounded adelic matrices

Algebra for the reduction step, which moves an adelic point of a unipotent radical close to `1` by a
rational element. The algebra is done for square matrices over a commutative ring `R` with
involution and a hermitian unit `J`.

* `New.Reduction.IsIntBounded`: adelic matrices that are integral at the finite places and of
  operator norm at most `r` at the infinite ones, with the behaviour of the bound under `star`,
  multiples, products and differences.


### `radicalElem`

 The matrix `1 + 2 (T - Tᴴ - Tᴴ J T) J`. If `J` is hermitian and `T = w aᴴ` with
`aᴴ J a = aᴴ J w = 0`, it is `exp (2 S) = 1 + 2 S + 2 S²` for `S = (T - Tᴴ) J`, which has `S³ = 0`;
it preserves `J`, fixes `a` and acts trivially on `a^⊥ / a`. 

### `form_mul_eq_zero`

 If `J` is hermitian and `aᴴ J w = 0`, then `aᴴ J w z = 0` and `wᴴ J a z = 0` for all `z`. 

### `gram_radicalElem`

 If `J` is hermitian and `aᴴ J a = aᴴ J w = 0`, then `radicalElem J (w aᴴ)` preserves `J`. 

### `mem_dilationGroup_of_eq_radicalElem`

 If `J` is hermitian and `aᴴ J a = aᴴ J w = 0`, then an element of `U J` with matrix
`radicalElem J (w aᴴ)` fixes `a` and acts trivially on `a^⊥ / a`. 

### `radicalElem_mul`

 Let `J` be hermitian and `aᴴ J a = aᴴ J w = aᴴ J z = 0`. The product of the elements of the
radical of `a` with parameters `w` and `z` has the parameter `w + z - a wᴴ J z`. 

### `eq_radicalElem_of_mem_dilationGroup`

 Let `J` be hermitian and invertible, `aᴴ J a = aᴴ J y = 0` and `y e + 2 b aᴴ J = 1`, so that the
columns of `y` span `a^⊥`. Let `u` be an element of the unitary group `U J` that fixes the columns
of `a` and satisfies `wᴴ J u v = wᴴ J v` for `v`, `w` orthogonal to `a`, so it acts trivially on
`a^⊥ / a`. Then `u = radicalElem J (y e (u - 1 - a bᴴ J u) b aᴴ)`, where
`radicalElem J T = 1 + 2 (T - Tᴴ - Tᴴ J T) J`. 

### `exists_radicalElem_mul_eq`

 Reduction in the radical of an isotropic matrix `a`. Let `J` be hermitian and invertible,
`aᴴ J a = aᴴ J y = 0` and `y e + 2 b s aᴴ J = 1`, so that the columns of `y` span `a^⊥`, and let
`u` fix `a` and act trivially on `a^⊥ / a`. Let `r` be any map on matrices; think of `r c` as a
lattice point near `c`, and of `s` as a scaling. Then there are matrices `c`, `d` and an element `x`
of `U J` with matrix `radicalElem J ((a (r d) - y (r c)) s aᴴ)` such that `x` fixes `a` and acts
trivially on `a^⊥ / a`, and `x u` is `radicalElem J ((y (c - r c) - a (d - r d)) s aᴴ)`. 

### `IsIntBounded`

 The adelic matrix `a` is integral at all finite places and has operator norm at most `r` at
each infinite place. 
