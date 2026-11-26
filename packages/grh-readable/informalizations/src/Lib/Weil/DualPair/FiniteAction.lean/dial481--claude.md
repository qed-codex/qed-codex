---
{
  "module": "src/Lib/Weil/DualPair/FiniteAction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/FiniteAction.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/FiniteAction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Weil representation of unitary pairs: finite action, sums, negation and change of point

This file studies the Weil representation `New.pairWeil` S T a b of a pair of unitary groups on
data on Hom(S,T). Here S and T are hermitian spaces of ranks n and n′, Hom(S,T) is the space of
n′ × n matrices, and θ denotes the theta functional. The file describes the action of finite points
on named data. It also describes the behaviour of the action and of θ when a space is split as a
sum, when the form of one space is negated, and when a point is moved.

## Main definitions and results

* `New.pairWeil_schrodingerOp_of_mem_supportedOn`: a pair supported on `A` and its conjugate
  (`New.Gf.supportedOn`) replaces `Ψ` by `Ψ (h⁻¹ · g)`, up to an explicit scalar.
* `New.pairWeil_schrodingerOp_of_mem`: an integral pair (`New.stdLevel`) moves `Ψ` and the vector
  together.
* `New.conj_weilMultiplier_of_eq_neg`, `New.exists_theta_negSource`: negation conjugates the
  multiplier and θ, up to a factor; `New.pairWeil_negSource`: it intertwines the actions of the pair
  once the characters are changed.

Notions from other files:
* `New.pairWeil`: The representation ω_{a,b}(g, h) = a(det h) b(det g)⁻¹ ω(`onHom` (g, h)); the
  scalar is `New.pairChar a b (g, h)`.
* `New.weilMultiplier`: Δ(g) = Δ_f(g_f) ∏_τ conj(det d_τ), with d_τ the block of g_τ on the negative
  coordinates.
* `New.Space.boxProd`: the product f₁ ⊠ f₂ of data on two blocks of coordinates.
* `New.Space.ϱ`, `New.Space.ω`, `New.Space.vacElem`: The Heisenberg operators, the Weil
  representation and the vacuum vector of the space of data `New.𝒮 V`.

## Relation to the literature

Known; see `Lib.Weil.DualPair.GaloisLaw` for sources.



## Action of finite points of a pair on named data

The action `New.pairWeil S T a b` of a pair `(g, h)`, finite or integral at `A`, on named data. Let
`A` be a set of finite places disjoint from its conjugate. A Schwartz–Bruhat function `Ψ` above `A`
(`New.IsSchwartzBruhat`) names the operator `(S.hom T).schrodingerOp A Ψ` on the space of data of
Hom(S, T).

* `New.pairWeil_eq_smul_of_projOn_eq`, `New.SiegelWeil.projOn_pairWeil`: the action on vectors that
  are vacua above `A` (fixed by `New.Space.projOn`).


 ### Supports, integrality and determinants 

### `Exchange.detOn_preimage_star`

 For unitary `g`, the determinant on the conjugate of `A` is `x̄⁻¹`, with `x = detOn A g` the
idele equal to `det g` on `A` and to `1` elsewhere. 

### `G.onHom_mem_supportedOn`

 If the finite parts of both members of a pair are supported on `A` and its conjugate, so is the
finite part of their image `x ↦ h x g⁻¹` under `G.onHom`. 

### `G.onHom_atPlace_mem`

 If both members of a pair are integral at the place `w`, that is, lie in `localIntGL`, so is
their image under `G.onHom`. 

 ### Scalars and the finite multiplier 

### `scalarFin`

 The scalar matrices, as a homomorphism from the finite adeles of norm one to `Gf E n`. 

### `Seesaw.commute_scalarFin`

 Scalar finite points are central in the finite adelic unitary group. 

### `G.detFin_of_mem_supportedOn`

 Let `A` be disjoint from its conjugate. For `g` supported on `A` and its conjugate, the
determinant `detFin s g` of the adelic point `(1, g)` is `divStar x = x / x̄` with `x = detOn A g`,
the idele equal to `det g` on `A` and to `1` elsewhere. 

### `G.adeleMatrix_scalarFin`

 The adelic point with trivial real part and scalar finite part `ν` has matrix `(1, ν)` times the
identity. 

### `G.onHom_scalarFin`

 Take the pair of scalar finite points `ν` in `U(S)` and `ν'` in `U(T)`, with trivial archimedean
parts. `New.G.onHom` sends it to the scalar finite point `ν' / ν` on `Hom(S, T)`. 

### `finMultiplier_onHom_left`

 The finite multiplier `finMultiplier`, written Δ_f, of the image `G.onHom (g, 1)`, which acts on
Hom(S,T) by x ↦ x g⁻¹, is Δ_f(g_f⁻¹)^(n'), where n' is the rank of the second space. 

### `pairWeil_eq_smul_of_projOn_eq`

 Let `f` be a vacuum above `A`, that is, fixed by the projection `projOn A`. An integral pair
`(g, h)` of finite points supported on `A` and its conjugate acts on `f` through `pairWeil` by the
scalar a(det h) · b(det g)⁻¹, where `detFin` is the determinant of a finite point. 

### `SiegelWeil.projOn_pairWeil`

 If the finite part of the image `onHom p` is integral at the places of `A` (lies in
`localIntGL`), then `pairWeil S T a b p` maps a vector fixed by the projection `projOn A` onto vacua
above `A` to a vector that is again fixed by it. 

 ### The action on named data 

### `pairWeil_schrodingerOp_of_mem_supportedOn`

 Let `A` be disjoint from its conjugate, `Ψ` a Schwartz–Bruhat function above `A`, and `g`, `h`
finite points supported on `A` and its conjugate. Let `pairWeil` be the representation
(g, h) ↦ a(det h) b(det g)⁻¹ ω(x ↦ hxg⁻¹) on 𝒮 of `S.hom T`, the space of n' × n matrices, and let
`schrodingerOp A Ψ` be the operator Ψ⊗ on that 𝒮. Then `pairWeil` at `(g, h)` applied to
`schrodingerOp A Ψ f` equals `schrodingerOp A Ψ' f`, with Ψ'(x) = Ψ(h⁻¹ x g), times the factor
`χ_S (det h) / χ_T (det g) * |det g| ^ (n' / 2) / |det h| ^ (n / 2)`. Here determinants are on `A`
(`detOn`), `ideleAbs` is the idele norm, `χ_S = a.spaceChar n` and `χ_T = b.spaceChar n'`, with
`a.spaceChar k` the base change of `a` times `υ⁻ᵏ`. 

### `Space.omega_schrodingerOp_of_mem`

 Let `A` be a set of finite places disjoint from its conjugate, `Φ` a Schwartz–Bruhat function of
finite adelic vectors above `A`, and Φ⊗ = `schrodingerOp A Φ` the operator on `𝒮 S` that is the
combination of Heisenberg operators whose coefficients have `schrodingerCombination` equal to Φ. If
`g` is an adelic unitary whose finite part `g_f` lies in GL_n(O_w) at every w ∈ A, then `ω g` sends
Φ⊗ f to (Φ ∘ g_f⁻¹)⊗ (ω g f) for every f. 

### `pairWeil_schrodingerOp_of_mem`

 Let `A` be disjoint from its conjugate and `Ψ` Schwartz–Bruhat above `A`. For an integral pair
`(g, h)` (finite parts in `stdLevel`), `pairWeil` sends `schrodingerOp A Ψ f`, the vector named by
`Ψ` on `f`, to the vector named by `x ↦ Ψ (h⁻¹ x g)` on the image of `f` under `pairWeil`. 


## Pairs under sums of spaces, negation of a form and change of point

* `New.negSource`: the change of coordinates `x ↦ (1, u⁻¹) x` from Hom(S⁻,T) to Hom(S,T), with
  u ∈ Ô of norm −1 and S⁻ = `S.neg` the space with the negated form; `negSource.map` pulls data
  on Hom(S,T) back to data on Hom(S⁻,T).
* `New.theta_boxProd_target`, `New.theta_boxProd_source`: θ of a product f ⊠ f' of data is
  θ(f)θ(f').


### `Space.mem_ratVectors_hom`

 A vector x on pairs of indices is a rational point of Hom(S,T) exactly when the matrix
x_T · x · x_S⁻¹ has rational entries, x_S = `S.x` and x_T = `T.x` being the points of S and T, their
matrices in GL(𝔸); the point of Hom(S,T) is x_T ⊗ (x_S⁻¹)ᵀ. 

### `homSigns_sum_target`

 Let the bijection `e : n₁ ⊕ n₂ ≃ n` split the signs `s` into `s₁` and `s₂`. Then the induced
bijection `n₁ × n' ⊕ n₂ × n' ≃ n × n'` splits the signs `homSigns s' s` into `homSigns s' s₁` and
`homSigns s' s₂`. 

### `homSigns_sum_source`

 The signs of Hom(V₁ ⊕ V₂, T), for signs `s₁`, `s₂` and `s'` of V₁, V₂ and T, split into those of
Hom(V₁, T) and Hom(V₂, T). 

 ### Sums 

### `theta_boxProd_target`

 Let e split the coordinates of V compatibly with the signs (s ∘ e = s₁ ⊕ s₂). Suppose the point
of V, meaning its matrix x in GL_n(𝔸) with xᴴJx = diag(s) at the infinite places and 1 at the finite
places, becomes block diagonal when reindexed along e, with blocks the points of V₁ and V₂. Then for
data f on Hom(T,V₁) and f' on Hom(T,V₂), θ on Hom(T,V) of the product f ⊠ f' is θ(f)θ(f'); the
product is taken along the splitting of the coordinates of Hom(T,V) induced by e, which keeps the
signs by `New.homSigns_sum_target`. 

### `theta_boxProd_source`

 For data f on Hom(V₁,T) and f' on Hom(V₂,T), θ on Hom(V₁ ⊕ V₂, T) of the product f ⊠ f' is
θ(f)θ(f'). The product is taken along the splitting `New.homSigns_sum_source` of the coordinates. It
is induced by the identity of the index set n₁ ⊕ n₂ of V₁ ⊕ V₂. 

### `pairWeil_boxProd_source`

 On Hom(V₁ ⊕ V₂, T), the block diagonal element with blocks g₁ and g₂ acts on a product f ⊠ f'
factor by factor: ω_{bb',a}(g,h)(f ⊠ f') = ω_{b,a}(g₁,h)f ⊠ ω_{b',a}(g₂,h)f' for data f, f' on
Hom(V₁,T), Hom(V₂,T). 

### `pairWeil_boxProd_target`

 Let e split the coordinates of V compatibly with the signs, and let g be block diagonal along e
with blocks g₁, g₂. Then on Hom(T,V), ω_{a,bb'}(h,g)(f ⊠ f') = ω_{a,b}(h,g₁)f ⊠ ω_{a,b'}(h,g₂)f' for
data f, f' on Hom(T,V₁), Hom(T,V₂). 

 ### Negation of the source 

### `negSource`

 The negation change of coordinates from Hom(S⁻,T) to Hom(S,T): x ↦ (1, u⁻¹)x, u the chosen
element of Ô of norm −1. It conjugates the bicharacter β of the Heisenberg group, so it induces an
antilinear map `negSource.map` from data on Hom(S,T) to data on Hom(S⁻,T). 

### `conj_weilMultiplier_of_eq_neg`

 If g and g₁ lie in the adelic unitary groups of opposite signs s = −t and have the same
matrix, then the complex conjugate of Δ(g₁) is υ(det g₁) Δ(g), where Δ = `weilMultiplier` and υ is
the splitting character restricted to norm one ideles (`upsilonU1`). 

### `pairWeil_negSource`

 Let S⁻ = `S.neg` be the space with signs −s and matrix −J. Let `negSource.map` be the antilinear
map from data on Hom(S,T) to data on Hom(S⁻,T) induced by the change of coordinates x ↦ (1, u⁻¹)x,
with u in Ô of norm −1. This map carries ω_{a,b}(g,h) f to ω_{a⁻¹υ^n, b⁻¹υ^(n')}(g⁻,h) applied to
the image of f; these are the characters that belong to the inverse splitting characters. Here υ is
`New.WeilData.upsilonU1`, g⁻ = `New.G.neg` g is the element of signs −s with the same matrix as g,
and n, n' are the ranks of S and T. 

### `exists_theta_negSource`

 There is a complex number `c` of modulus one such that, for every datum `f` on `Hom(S, T)`, the
theta functional `θ` of `Hom(S⁻, T)` (with `S⁻ = S.neg`) at `c • negSource.map f` is the complex
conjugate of `θ f` for `Hom(S, T)`. Here `negSource.map` is the antilinear map from data on
`Hom(S, T)` to data on `Hom(S⁻, T)` induced by the change of coordinates x ↦ (1, u⁻¹)x, where u is
the chosen element of Ô of norm −1. 

 ### Change of point 

### `Space.pairTheta_move`

 Change of point for a pair. If the points of `S` and `T` are moved by `γ` and `γ'`, the theta
kernel for the characters `a` (of `det h`) and `b` (of `det g⁻¹`) at `(g, h)` becomes
`b (det γ) a (det γ')⁻¹` times the old kernel at `(γ g, γ' h)`. 
