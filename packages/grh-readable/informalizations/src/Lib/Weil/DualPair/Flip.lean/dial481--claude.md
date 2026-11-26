---
{
  "module": "src/Lib/Weil/DualPair/Flip.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/Flip.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/Flip.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Flipping a dual pair by adjoints: Weil actions and theta kernels modulo ideals

For hermitian spaces `V`, `W`, the Weil representation on the data space of `Hom(V, W)` gives the
action `New.pairWeil V W` of the two unitary groups and the theta kernel `New.pairTheta V W`.
Taking adjoints identifies this pair with the pair `(W, V⁻)`, where `V⁻ = New.Seesaw.flipSpace V`
has the signs opposite to those of `V`. This file gives the effect of the adjoint on Weil actions,
on theta kernels and on the polynomial vectors of the Fock model (`New.flipPoly`). For theta
kernels `New.modKernel` built from functions on matrices modulo an ideal `𝔪`, the flip is expressed
by a finite Fourier transform.

## Main definitions and results

* `New.flipCoords`: the adjoint, twisted by the idele `New.flipIdele`, as a change of coordinates
  `New.CoordChange`; it depends on a unit `c` of `Ô` with `c̄ c = -1`. `New.Seesaw.flipSpace` is the
  opposite space `V⁻`.
* `New.flipCoords_map_pairWeil`, `New.exists_theta_flipCoords_map_eq_mul`,
  `New.flipCoords_map_schrodingerOp`: it intertwines the actions of the pairs once the characters
  are changed, keeps the theta functional up to a number of modulus one, and moves a datum to the
  conjugate places.
* `New.exists_pairTheta_flip`: the resulting identity of theta kernels, after a change of point.
* `New.Modulus.exists_modKernel_flip`: a kernel `New.modKernel` of (V, S) as a constant times a
  kernel of (S, T), where V has the signs opposite to T.
* `New.Exchange.exists_conj_modKernel_eq_swap`: the complex conjugate of a kernel of (S, T) as a
  kernel of (T, S).

Notions from other files:
* `New.WeilData`: Weil data on a stably unramified E. They consist of ȷ in E with ȷ = −ȷ̄, Im τȷ > 0
  for every τ in the CM type and (1 − ȷ⁻¹)/2 integral; a finite idele α for which the completed
  integers Ô are self-dual under (z, u) ↦ ψ_f(ȷαᾱzu); and a splitting character υ equal to −1 at
  uniformisers of the places w with w = w̄; its restriction to the norm-one ideles is
  `New.WeilData.upsilonU1`.
* `New.Modulus`: a nonzero ideal 𝔪 of O_E prime to its complex conjugate; `𝔪.ResidueRing` is O_E/𝔪,
  `𝔪.generator` a finite idele generating 𝔪 in Ô, equal to 1 off 𝔪, and `𝔪.primAddChar` the
  primitive additive character x ↦ ψ_f(ȷαᾱ x / 𝔪.generator) of O_E/𝔪.
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to the diagonal matrix of its signs at the infinite places and 1 at the finite places.
* `New.𝒮`: The Banach space 𝒮(V) of integrable functions c on 𝔸^n with c(x) = ∫ c(y)β(y,x)e(x−y) dy,
  under the L¹ norm; β is the adelic bicharacter and e the vacuum function `New.vacuumFn`.
* `New.pairWeil`: The action ω_{a,b}(g, h) = χ_{a,b}(g, h) ω(x ↦ hxg⁻¹) on 𝒮(Hom(S, T)), where
  χ_{a,b}(g, h) = a(det h) b(det g)⁻¹ is `New.pairChar`. The theta kernel `New.pairTheta` S T a b f
  (g, h) is θ(ω_{a,b}(g, h) f), where θ is the theta functional `New.Space.θ`.

## Relation to the literature

Known; see `Lib.Weil.DualPair.ThetaLiftConvergence` for sources.



## The adjoint flip on Weil actions and theta kernels

The change of coordinates `New.flipCoords`, its effect on Weil actions and theta kernels, the
opposite space `New.Seesaw.flipSpace`, and its effect on the polynomial vectors of the Fock model
(`New.flipPoly`, `New.realMap_flipCoords_polyVector`).


### `flipIdele`

 For a unit `c` of `Ô` and a sign `t`, the idele with component `t` at every infinite place and
finite part `c α / ᾱ`, where `α` is the finite idele of the Weil data. 

### `flipCoords`

 For a unit c of Ô with c̄c = −1 (hypothesis `hc`) and signs t′ = −t (hypothesis `ht`), the
change of coordinates x ↦ (1, cα/ᾱ) ε_s xᴴ ε_t, where ε_s, ε_t are the standard diagonal forms of
the signs (`New.flipCoords_apply`). On points it goes from signs t′_i s_j to signs s_j t_i. It
carries functions from signs s_j t_i to signs t′_i s_j. 

### `flipCoords_apply`

 For a unit `c` of `Ô E` with c̄c = −1 and signs `t' = -t`, the map `φ` of the change of
coordinates `flipCoords` is computed as follows. It reads a vector `x` on pairs in `a × n` as a
matrix and sends it to ε_s xᴴ ε_t, where ε_s = `stdForm E s` and ε_t = `stdForm E t` are diag(s) and
diag(t) at the infinite places and the identity at the finite places. It then scales by the idele
`flipIdele c 1` (1 at the infinite places, cα/ᾱ at the finite places, α from the Weil data) and
reads the result back as a vector on pairs. 

### `flipCoords_map_omega`

 Let V, W be spaces of ranks |a| and |n|, let V' have the signs opposite to those of V, and let c
be a unit of Ô with c̄c = −1. Transport by `New.flipCoords` is the change of coordinates x ↦ (1,
cα/ᾱ) ε_s xᴴ ε_t, where α is the idele of the Weil data and ε are the diagonal sign forms. It sends
ω(g, h) f of the pair (V, W) to the value at (h, g) of `New.pairChar` for υ^|n| and υ^|a|, times
ω(h, g⁻) of the pair (W, V') applied to the transported f. Here ω(g, h) is the Weil action of
`New.G.onHom` (g, h), υ is `New.WeilData.upsilonU1`, and g⁻ = `New.G.neg` g has the matrix of g, in
the group of the opposite signs. 

### `Seesaw.flipSpace`

 The opposite space of the space V with matrix J and point x: it has matrix −J and the opposite
signs. Its point is x scaled by the idele (1, ūᾱ/α), where u = `New.Weil.normNegOne` is a fixed
unit of Ô with ūu = −1. 

### `flipCoords_map_pairWeil`

 The adjoint intertwines the actions of the pairs. Let V, W be spaces of ranks |a| and |n|, and
let V' have the signs opposite to those of V. Transport by `New.flipCoords` takes ω_{a',b}(g, h) of
the pair (V, W) to ω_{b⁻¹υ^|n|, a'⁻¹υ^|a|}(h, g⁻) of the pair (W, V'); these are the characters that
belong to the inverse splitting characters. Here ω is `New.pairWeil`, υ is
`New.WeilData.upsilonU1` and g⁻ = `New.G.neg` g has the matrix of g. 

### `exists_theta_flipCoords_map_eq_mul`

 The adjoint keeps the theta functional up to a number of modulus one. Let E be a CM field with
Weil data and finite idele α, and let c be a unit of Ô with c̄c = −1. Let V' have the signs t′ = −t
opposite to those of V, and let its point be `star (flipIdele c 1) • x_V`, that is, x_V multiplied
by 1 at the infinite places and by conj(cα/ᾱ) at the finite places.

Then there is z ∈ ℂ with ‖z‖ = 1 such that θ(f^φ) = z θ(f) for all f in 𝒮(Hom(V, W)). Here f^φ on
Hom(W, V') is the transport of f by φ = `New.flipCoords`. 

### `flipCoords_map_schrodingerOp`

 The adjoint moves a datum to the conjugate places. Let `A` be a set of finite places disjoint
from its conjugate and `Ψ` a Schwartz–Bruhat function above `A`. Transport by `New.flipCoords`
sends the vector named by `Ψ` at `A` on the vacuum of Hom(V, W) to the vector named by
`y ↦ Ψ (c yᴴ)` at the conjugate of `A` on the vacuum of Hom(W, V'). 

### `exists_pairTheta_flip`

 The adjoint followed by a change of point. Let V, W be spaces of ranks |a| and |n|, let V' be a
space with the signs t′ = −t opposite to those of V, and let l in the group of V' satisfy
x_{V'} l = (1, conj(cα/ᾱ)) x_V on the points. For each character b there is a z of modulus one such
that θ^{W,V'}_{b⁻¹υ^|n|, a'⁻¹υ^|a|}(f^φ)(h, g') = z θ^{V,W}_{a',b}(f)(g, h)
for all characters a', data f, and g, h, g' where g' has the matrix l g. Here θ is `New.pairTheta`,
υ is `New.WeilData.upsilonU1` and f^φ is the transport of f by φ = `New.flipCoords`. 

### `flipPoly`

 The ℂ-algebra map on polynomials sending the variable X_(τ,i,j) to −s_i t_j X_(τ,j,i):
transposition with signs. 

### `realMap_flipCoords_polyVector`

 The archimedean part `New.CoordChange.realMap` of `New.flipCoords` sends the Fock vector of a
polynomial `P` to the Fock vector of `New.flipPoly t' s P`. 


## Flipped and conjugate theta kernels modulo an ideal

A theta kernel `New.modKernel` S T a b 𝔪 D P g h is attached to spaces S, T, characters a, b of
[U(1)], a function D on matrices modulo 𝔪 and a polynomial P. A kernel of one pair is written as a
constant times a kernel of the reversed pair.

The idea: the indicator of a class modulo 𝔪 comes from a translate of the vacuum, and after the flip
this translate is the datum of an additive character modulo 𝔪. Throughout υ is
`New.WeilData.upsilonU1`, and a constant is controlled only through the square of its modulus.


### `Modulus.flipScalar`

 The scalar matrix ū / u in the finite adelic unitary group `Gf E n` of rank n, where u is α
times the chosen idele generating 𝔪. The index type n defaults to `Unit`: a bare `𝔪.flipScalar`
is the rank-one case `𝔪.flipScalar Unit`. 

### `Modulus.vacTranslate`

 The Heisenberg translate of the vacuum of a space `X` by the finite vector with entries
−α w_i / 𝔪.generator at the places dividing 𝔪 and 0 at the other places (`New.finVec` multiplies
by α), for an integral vector `w`. 

### `Modulus.vacTranslate_eq_schrodingerOp_boxIndicator`

 The translate of the vacuum by a vector above 𝔪 is the operator named by the indicator of the
translated integral box, applied to the vacuum. 

### `Modulus.finIdeleAbs_generator`

 The module of the idele `𝔪.generator` is the inverse of the number N𝔪 of elements of O_E/𝔪. 

### `Modulus.exists_pairWeil_vacTranslate`

 Let u = ḡ / g for the generator g of 𝔪, as a scalar in the finite unitary group of rank m.
For a space V of rank m with signs −t, a space S of rank n and characters a, b there is one
constant C, with |C|² = N𝔪^(mn), such that ω_{a,b}(u, 1) sends the vacuum translate
(`New.Modulus.vacTranslate`) by every integral w to C times the operator named by the lift of the
point mass at the class of w modulo 𝔪, applied to the vacuum. Here ω_{a,b} is `New.pairWeil` of the
pair (V, S), and N𝔪 is the number of elements of O_E/𝔪. 

### `Modulus.flipCoords_map_vacTranslate`

 Let c be a unit of Ô such that −c satisfies c̄c = −1 (the form in which the flip takes it), V a
space of rank m with signs −t, and v an integral n × m matrix. The flip φ = `New.flipCoords` for
the unit −c carries the vacuum translate by v (`New.Modulus.vacTranslate`) of Hom(V, S) to the
operator of Hom(S, T) named by the lift of the character ρ ↦ ψ(tr(ρ v)) modulo 𝔪, applied to the
vacuum; here ψ is `New.Modulus.primAddChar` shifted by −c̄. 

### `Modulus.exists_modKernel_flip`

 Flip of a pair. Let c be a unit of Ô with c̄c = −1, T a space of rank m, V a space with the
opposite signs whose point is (1, c) times that of T (hypothesis `hV`), and S a space of rank n.
Thus T has the negated form of V and the point of V times (1, c⁻¹), where c⁻¹ = −c̄. For characters
a, b of [U(1)] there is a complex C such that (a) |C|² · N𝔪^(mn) = 1, N𝔪^(mn) being the number of
m × n matrices over O_E/𝔪, and (b) θ^{V,S}_{a,b}[D,P](g⁻,h) = C θ^{S,T}_{b⁻¹υⁿ,a⁻¹υᵐ}[D̂,P′](h,gu)
for all D, P, g, h. Here θ[D,P] is the kernel `New.modKernel` of the function D modulo 𝔪 and the
polynomial P, and g⁻ = `New.G.neg` g is g in the group of V. The character υ is the splitting
character restricted to the norm-one ideles. D̂(ρ) = ∑_v D(v)ψ(−c̄ tr ρv), where
ψ = `New.Modulus.primAddChar` is the primitive character of O_E/𝔪. P′ = `New.flipPoly` of P sends
X_(τ,i,j) to −s_i t_j X_(τ,j,i). u = `New.Modulus.flipScalar` of rank m is the scalar ū₀/u₀, with u₀
equal to α times the idele generating 𝔪, placed at the finite places. 

### `Exchange.exists_conj_modKernel_eq_swap`

 Reversal of a pair. For spaces S, T of ranks n, m and characters a, b there is a complex c
such that (a) |c|² · N𝔪^(nm) = 1, with N𝔪 the number of elements of O_E/𝔪, and (b) for all
D, P, g, h the complex conjugate of θ^{S,T}_{a,b}[D,P](g,h) is c θ^{T,S}_{b,a}[D′,P′](h,gu).
Here D′ is the Fourier transform of D̄ for `New.Modulus.primAddChar`, P′ is the signed transpose
`New.flipPoly` of P̄ (the polynomial with conjugate coefficients) and u = `New.Modulus.flipScalar`,
placed at the finite places. 

### `exists_modKernel_flip_line`

 Flip for lines. Let S have rank n, let ε = ±1 in ℤˣ, and let L, L′ be the standard lines
`New.signedSpace` of signs −ε and ε. For every modulus 𝔪, characters b, a′ and k in the finite
unitary group of rank one there are an additive character ψ of O_E/𝔪 and a nonzero c such that
(a) |c|² · N𝔪ⁿ = 1, N𝔪ⁿ being the number of columns of length n over O_E/𝔪, and
(b) θ^{L,S}_{1,b}[D,P](k,h) = c θ^{S,L′}_{a′,υ}[D̂,P′](h,kf) for all P, D, h.
Here θ[D,P] is `New.modKernel`, υ is `New.WeilData.upsilonU1`, D̂ is the Fourier transform
`New.Exchange.matrixFourier` of D for ψ, P′ is the signed transpose `New.flipPoly` of P,
f = `New.Modulus.flipScalar`, and k, kf are placed at the finite places. Any a′ is allowed since c
may depend on k. 
