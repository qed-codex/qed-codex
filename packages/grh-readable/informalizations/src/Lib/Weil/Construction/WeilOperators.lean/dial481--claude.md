---
{
  "module": "src/Lib/Weil/Construction/WeilOperators.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/WeilOperators.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/WeilOperators.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Weil operators, orthogonal sums and transport of the reproducing model

This file defines the Weil operators of a multiplier action of a group `G` on `W` on the
reproducing model of a vacuum. It proves their cocycle relation, and shows that they preserve the
inner product. For cocycle `1` it defines the Weil representation and proves that it intertwines
the Heisenberg operators and is continuous. The file then treats orthogonal sums `W = W₁ × W₂`,
with tensor products of model vectors and Wiener's bound, and the transport of the model along
isomorphisms.

## Main definitions and results

* `New.Heisenberg.IsVacuum.weilOp_mul`, `New.Heisenberg.IsVacuum.modelInner_weilOp`: if c(g, 1) = 1,
  the Weil operators `New.Heisenberg.IsVacuum.weilOp` multiply up to the cocycle c and preserve the
  inner product.
* `New.Heisenberg.IsVacuum.weilRep`: for c = 1 the Weil representation; it intertwines ρ(x) and
  ρ(gx) (`New.Heisenberg.IsVacuum.weilRep_heisenbergOp`) and, for first countable G, is jointly
  continuous (`New.Heisenberg.IsVacuum.continuous_weilRep`). Elements that preserve `e` act by Δ(g)
  times substitution (`New.Heisenberg.IsVacuum.weilRep_apply_of_vacuum_smul`). The operator of g
  has norm at most ‖vac‖ |Δ(g)| (`New.Heisenberg.IsVacuum.norm_weilRep_le`).

Notions from other files:
* `New.Heisenberg.IsVacuum.Model`: the integrable functions v with v x = ∫ v y β(y, x) e(x - y),
  with the L¹ norm and the inner product `New.Heisenberg.IsVacuum.modelInner`.
* `New.Heisenberg.MultiplierAction`: an action of `G` on `W` preserving `β` and `μ`, with a
  multiplier `Δ` and a cocycle `c`.
* `New.Heisenberg.IsVacuum.heisenbergOp`, `New.Heisenberg.IsVacuum.vacElem`: the Heisenberg
  operators ρ(x) on the model and the vacuum `e` as an element of the model.

## Relation to the literature

This file contributes to the adelic Weil representation of a unitary group and the invariant theta
functional. See `Lib.Weil.MixedModel.ZeroTerm`. Sources: Weil; Kudla.

The usual proof of the product rule ω(g) ω(h) = ω(gh) compares ω with a Schrödinger model on a
Siegel parabolic subgroup of a split space, and then uses the Iwasawa decomposition and the sum
V ⊕ V⁻. The proof here does not use a Schrödinger model. The scalar c(g, h) in
ω(g) ω(h) = c(g, h) ω(gh) is an integral of three vacua times values of the multiplier
(`New.Heisenberg.IsVacuum.weilOp_inv_mul_weilOp_mul_weilOp`). Later files show directly that it is
1, from three local facts: a Gaussian determinant at the real places (`New.Fock.realAction`),
positivity at the split places and the sign of a Gauss sum at the inert places
(`New.stdLattice.mem_cocycleRadical`). The formulas of the Schrödinger model are then proved for the
slices in `Lib.Weil.MixedModel.ZeroTerm`.



## Weil operators: cocycle relation, unitarity and continuity

Below, `B` is an action of `G` on `W` with multiplier `Δ` and cocycle `c`
(`New.Heisenberg.MultiplierAction`), `A` one with cocycle `1`, `ρ = heisenbergOp` and
`vac = vacElem`.

* `New.Heisenberg.IsVacuum.weilOp`: the operator v ↦ Δ(g) ∫ v(y) ρ(gy) vac dμ(y).
* `New.Heisenberg.IsVacuum.integrated_moveBy_vacElem_eq_smul`: a nonzero overlap with the vacuum
  determines a unitary intertwining operator.
* `New.Heisenberg.IsVacuum.cocycleRadical`: the elements s with c(g, s) = 1 for all g, a subgroup.


 ### The operators of an action with a cocycle 

### `weilOp`

 The Weil operator of `g` for the action `B`: the operator v ↦ Δ(g) ∫ v(y) ρ(g • y) vac dμ(y) on
the model space, where `Δ = B.Δ`, `ρ = heisenbergOp` and `vac = vacElem`. The integral is the
integrated action of `v` on `vac` for the representation `y ↦ ρ (g • y)`
(`New.Heisenberg.Rep.moveBy`). 

### `integrated_moveBy_integrated`

 Write P_g(w) for the operator ∫ w(y) ρ(g • y) dμ(y) on the model space, the integrated action
`(heisenbergRep.moveBy B g).integrated w` of `w`. For vectors `v`, `w`, `x` of the model space,
P_g(P_k(w) v) x = P_{gk}(w) (P_g(v) x). 

### `map_integrated_moveBy`

 For a bounded functional `T` on the model space, `T` of the integrated action of `w` on `v` for
the representation `y ↦ ρ (g • y)` is ∫ w(g⁻¹ • y) T(ρ(y) v) dμ(y). 

### `modelInner_vacElem`

 Let `e` be a vacuum for the Heisenberg datum `H` and Haar measure `μ`, and let `Model H` be the
space of integrable `v` with v(x) = ∫ v(y) β(y,x) e(x−y) dμ(y). Then the pairing ∫ conj(e) v dμ
(`modelInner`) of the vacuum `vacElem` (the function `e` itself) with any `v` in `Model H` equals
v(0). 

### `integrated_moveBy_vacElem_eq_smul`

 Let `B` be a multiplier action of `G` on the vacuum datum (`H`, `μ`, `e`), let `g : G`, and on
the model space of `e` let ρ(y) = `heisenbergOp y` and vac = `vacElem`. If `T` is a bounded
surjective operator on the model that preserves `modelInner` and satisfies T ρ(y) = ρ(g • y) T, then
for every model vector `v`, ∫ v(y) ρ(g • y) vac dμ(y) = conj((T vac)(0)) · T v. So the overlap ⟨vac,
T vac⟩ = (T vac)(0) determines `T` when it is not zero. 

### `weilOp_inv_mul_weilOp_mul_weilOp`

 The cocycle relation: the product of the Weil operators of (gh)⁻¹, g and h, in this order, is
the scalar c(g, h). 

### `norm_integrated_flip_le`

 For a representation R on the model space and a vector v, the operator sending w in the model
space to ∫ w(y) R.ρ(y) v dμ(y) has norm at most ‖v‖. 

### `weilOp_mul`

 Cocycle relation for the Weil operators ω = `weilOp B` of an action with cocycle c: if
c(g, 1) = 1 for all g, then ω(g)ω(h) = c(g, h)·ω(gh). 

### `modelInner_weilOp`

 If c(g, 1) = 1, the Weil operator `weilOp B g` preserves the inner product
`New.Heisenberg.IsVacuum.modelInner` (v, w) ↦ ∫ conj(v) w dμ of the model space. 

### `cocycleRadical`

 For an action `B` with cocycle c such that c(g, 1) = 1 for all g, the subgroup of those s in G
with c(g, s) = 1 for every g. 

 ### The Weil representation 

### `weilRep`

 The Weil representation of an action `A` with cocycle 1: the homomorphism
g ↦ (v ↦ Δ(g) ∫ v(y) ρ(g • y) vac dμ(y)) from G to the bounded operators on the model space, whose
value at g is `weilOp A g`. 

### `modelInner_weilRep`

 Let `e` be a vacuum for `H` and `μ`, with model space `Model H` of integrable `v` satisfying
v(x) = ∫ v(y) β(y,x) e(x−y) dμ(y). Let `A` be an action of `G` on `W` that preserves β and μ and has
multiplier Δ and cocycle 1. Then each Weil operator `weilRep A g`, v ↦ Δ(g) ∫ v(y) ρ(g • y) e dμ(y),
preserves the pairing `modelInner` (v, w) = ∫ conj(v) w dμ. 

### `weilRep_heisenbergOp`

 The Weil operator of `g` intertwines ρ(x) with ρ(g • x): ω(g) ρ(x) v = ρ(g • x) ω(g) v. Here
ρ(x) is `heisenbergOp x`, v ↦ (z ↦ β(x,z) v(z − x)), acting on the model space of the vacuum `e`.
`A` is an action of `G` on `W` that preserves β and μ and has multiplier Δ and cocycle 1. 

### `weilRep_eq_integral`

 The Weil operator of `g` sends `v` to Δ(g) ∫ v(g⁻¹ • y) ρ(y) vac dμ(y). 

### `weilRep_apply_eq_integral`

 The value at `x` of the Weil operator of `g` on `v` is Δ(g) ∫ v(y) β(g • y, x) e(x − g • y)
dμ(y). 

### `weilRep_apply_of_vacuum_smul`

 Let `A` be a multiplier action of `G` on the vacuum datum (`H`, `μ`, `e`) with cocycle 1 and
multiplier `A.Δ`, and let ω = `weilRep A` be its Weil representation on the model space of `e`. If
`g` preserves the vacuum function, that is e(g • y) = e(y) for all `y`, then `g` acts by
substitution up to its multiplier: for every model vector `v`, `(ω g v) x = Δ g * v (g⁻¹ x)`. 

### `conj_delta_mul_weilRep_vacElem`

 Let e be a vacuum for β and μ, and let `A` be a multiplier action of G on W with trivial
cocycle, that is, an action preserving β and μ with multiplier Δ. Let ω = `weilRep A` be the Weil
representation on `Model H` (the integrable v with v(x) = ∫ v(y) β(y,x) e(x−y) dμ(y)), given by
ω(g)v = Δ(g) ∫ v(y) ρ(g • y) e dμ(y). Then the overlap ⟨vac, ω(g) vac⟩ = (ω(g) vac)(0) of the Weil
operator of `g` is the inverse of conj Δ(g): conj Δ(g) · (ω(g) e)(0) = 1. 

### `norm_weilRep_le`

 For a multiplier action `A` of `G` on `W` with cocycle 1, preserving β and `μ`, with vacuum `e`,
consider the Weil operator `weilRep A g` on the model space `Model H`, which carries the L¹ norm.
Its operator norm is at most the norm of `he.vacElem` (the vacuum `e` as an element of the model
space) times the modulus of the complex multiplier `A.Δ g`. 

### `continuous_weilRep`

 Let e be a vacuum for β and μ, and let `A` be a multiplier action of G on W with trivial
cocycle, that is, a continuous action preserving β and μ with multiplier Δ. For a first countable
group `G`, the map (g, v) ↦ `weilRep A g v` on `G × Model H` is continuous, where ω(g)v = Δ(g) ∫
v(y) ρ(g • y) e dμ(y) and `Model H` is the space of integrable v with v(x) = ∫ v(y) β(y,x) e(x−y)
dμ(y), with the L¹ norm. 


## Orthogonal sums, tensor products of model vectors and Wiener's bound

* `New.Heisenberg.IsVacuum.wiener_bound`: a sum of coefficients along a group homomorphism into `W₁`
  is bounded by the number of terms that fall in a fixed compact set, times a constant `M` and the
  norm of the model vector `v`.
* `New.Heisenberg.OrthogonalSum.tmul`: the tensor product of model vectors, a product of functions.
  It is multiplicative for norms and inner products (`New.Heisenberg.OrthogonalSum.norm_tmul`,
  `New.Heisenberg.OrthogonalSum.modelInner_tmul`).
* `New.Heisenberg.OrthogonalSum.weilRep_tmul`, `New.Heisenberg.Rep.integrated_tmul`: the tensor
  product is compatible with the Weil representation and with the integrated action.


### `OrthogonalSum`

 An isomorphism φ: W₁ × W₂ → W of topological groups under which the bicharacter of H and the
function e are the products of those of the factors (β₁β₂, e₁e₂). 

### `OrthogonalSum.equiv`

 The isomorphism of topological groups from `W₁ × W₂` onto `W`. 

### `OrthogonalSum.beta_equiv`

 Along `equiv`, the cocycle of `H` is the product of the cocycles of `H₁` and `H₂`. 

### `OrthogonalSum.vac_equiv`

 Along `equiv`, the function `e` is the product of the two vacua `e₁` and `e₂`. 

 ### Wiener's bound 

### `IsVacuum.wiener_bound`

 Wiener's bound. Let `T` be a bounded map from the model space of the vacuum `e` to a space `X`,
and let `W` act on the model space by `ρ = heisenbergOp`. Assume that a vector `u` has `u 0 ≠ 0`,
that `W₁` is Hausdorff, that `κ : W₁ → W` is a continuous homomorphism, and that
`‖T ρ(z + κ x) u‖ = ‖g (t z + x)‖` for all `z` in `W` and `x` in `W₁`, with an integrable `g` on
`W₁` and some function `t : W → W₁`. Then there are a compact set `B` in `W₁` and a constant `M`
with the following property. For every additive group `I`, every homomorphism `φ : I → W₁` and
every `v`, the sum over `i` of `‖T ρ(κ (φ i)) v‖` is at most `M ‖v‖` times the number of `i` with
`φ i ∈ B`. 

 ### Tensor products along a splitting 

### `Rep.left`

 For a representation `R` of `H` on `X` and an orthogonal splitting `S` with `φ = S.equiv`, the
representation x ↦ R.ρ(φ(x, 0)) of `H₁` on `X`. 

### `Rep.right`

 For a representation `R` of `H` on `X` and an orthogonal splitting `S` with `φ = S.equiv`, the
representation x ↦ R.ρ(φ(0, x)) of `H₂` on `X`. 

### `OrthogonalSum.tmul`

 The tensor product of model vectors, a bounded bilinear map
`Model H₁ →L[ℂ] Model H₂ →L[ℂ] Model H`. With `φ = S.equiv`, it sends `v`, `w` to the iterated
integral `∫ v(y₁) ρ(φ(y₁, 0)) (∫ w(y₂) ρ(φ(0, y₂)) e dμ₂) dμ₁`, where `ρ` acts on the model space of
`e`. As a function it is `φ(x₁, x₂) ↦ v x₁ * w x₂`, see
`New.Heisenberg.OrthogonalSum.tmul_apply`. 

### `OrthogonalSum.isVacuum`

 Let `S` split `H` along `S.equiv : W₁ × W₂ ≃ W`, with `e` the product of the vacua `e₁` (for
`μ₁`) and `e₂` (for `μ₂`). Then `e` is a vacuum for `H` and the image of `μ₁ × μ₂` under
`S.equiv`. 

### `OrthogonalSum.measurePreserving_equiv`

 A vacuum fixes the normalisation of the Haar measure, so `S.equiv` carries `μ₁ × μ₂` to `μ`. 

### `OrthogonalSum.tmul_apply`

 Let `S` be an orthogonal sum, that is, an isomorphism φ = `S.equiv` : W₁ × W₂ → W of topological
groups under which β and e are the products β₁β₂ and e₁e₂. Let v and w lie in the model spaces of e₁
and e₂, the integrable functions reproduced by e₁ and e₂. Read through φ, the tensor product
`S.tmul v w` is the function (x₁, x₂) ↦ v x₁ * w x₂, so its value at x is
v((φ⁻¹x).1) · w((φ⁻¹x).2). 

### `OrthogonalSum.modelInner_tmul`

 Let `S` be an orthogonal sum, that is, an isomorphism φ: W₁ × W₂ → W of topological groups under
which β and e are the products β₁β₂ and e₁e₂. The tensor product `S.tmul` of model vectors (elements
of the reproducing spaces of e₁ and e₂) is multiplicative for the inner products ⟨v, w⟩ = ∫ conj(v)
w dμ: `⟨v ⊗ w, v' ⊗ w'⟩ = ⟨v, v'⟩ ⟨w, w'⟩`. 

### `OrthogonalSum.norm_tmul`

 Let `S` present `W` as the orthogonal sum of `W₁` and `W₂`, with `H` and the vacuum `e` being
the products of the data on the factors. For model vectors `v` of `e₁` and `w` of `e₂`, the tensor
product `S.tmul v w` (the function `S.equiv (x₁, x₂) ↦ v x₁ * w x₂`) has L¹ norm ‖v‖ · ‖w‖. 

### `OrthogonalSum.weilRep_tmul`

 The product rule for the Weil representation of an orthogonal sum. Identify `W` with
`W₁ × W₂` by `S.equiv`, and let `A`, `A₁`, `A₂` be actions with cocycle 1 of groups `G`, `G₁`,
`G₂` on `W`, `W₁`, `W₂`. If `g` acts as `(g₁, g₂)` and its multiplier is the product of theirs,
then the Weil operator of `g` is the tensor product of those of `g₁` and `g₂`. 

### `Rep.integrated_tmul`

 Integrating `v ⊗ w` against `R` is integrating `w` against the restriction `R.right S` of `R` to
`W₂`, then `v` against its restriction `R.left S` to `W₁`. 

### `OrthogonalSum.tmul_vacElem`

 Let `S` be an orthogonal sum: an isomorphism φ : W₁ × W₂ ≃ W of topological groups under which
β = β₁β₂ and e = e₁e₂. Then the tensor product `S.tmul`, which sends `v`, `w` to the function φ(x₁,
x₂) ↦ v(x₁) w(x₂) in `Model H`, takes the pair of vacua `vacElem` (e₁ and e₂) to the vacuum
`vacElem` (e). 

### `OrthogonalSum.heisenbergOp_tmul`

 Let `S` be an orthogonal sum φ : W₁ × W₂ ≃ W, under which β = β₁β₂ and e = e₁e₂, and let
v ⊗ w = `S.tmul v w` be the model vector φ(x₁, x₂) ↦ v(x₁) w(x₂). Then ρ(x) of `v ⊗ w` is ρ₁(x₁)
v ⊗ ρ₂(x₂) w, where (x₁, x₂) = `S.equiv.symm x` and ρ(x) is `heisenbergOp x`, v ↦ (z ↦ β(x,z)
v(z − x)). 

### `OrthogonalSum.heisenbergOp_equiv_vacElem`

 A translate of the vacuum is the product of translates of the two vacua. 

### `OrthogonalSum.exists_restriction`

 Restriction of functions to `W₂` along `φ = S.equiv` is a bounded map `r` from the model of `e`
to the model of `e₂`, and ∫ v(y) ρ(φ(y, 0)) u dμ₁(y) = v ⊗ r u for `v` in the model of `e₁` and
`u` in the model of `e`. 


## Transport of the model along a linear or conjugate linear isomorphism

Let `e`, `e'` be vacua (`New.Heisenberg.IsVacuum`) for Heisenberg cocycles on `W`, `W'`, and let
`φ : W' ≃ W` be an isomorphism of topological groups that matches the vacua and matches the cocycles
up to `σ`, the identity or the conjugation of `ℂ`. `New.Heisenberg.IsVacuum.transport` is the
`σ`-semilinear map `v ↦ σ ∘ v ∘ φ` between the models `New.Heisenberg.IsVacuum.Model` (integrable
functions reproduced by the vacuum kernel); `New.Heisenberg.IsVacuum.map_integral_and_map_vacuum` is
the change of variables behind it.


### `measurePreserving_equiv`

 Let `e`, `e'` be vacua for the Haar measures `μ`, `μ'`. An isomorphism of topological groups
`φ : W' ≃ W` with `e ∘ φ = e'` carries `μ'` to `μ`. 

### `map_integral_eq_integral_comp_equiv`

 Let `e`, `e'` be vacua for the Haar measures `μ`, `μ'`. Change of variables along an isometric
ring map `σ` of `ℂ` (the identity or the conjugation) and an isomorphism `φ : W' ≃ W` with
`e ∘ φ = e'`: `σ (∫ f dμ) = ∫ σ ∘ f ∘ φ dμ'` for every `f`. 

### `map_vacuum_comp_equiv`

 For an isometric ring map `σ` of `ℂ` and `φ : W' ≃ W` with `e ∘ φ = e'`, also `σ ∘ e ∘ φ = e'`,
as the vacuum `e'` of `H'` and `μ'` is real-valued. 

### `map_integral_and_map_vacuum`

 Change of variables along an isometric ring map `σ` of `ℂ` (the identity or the conjugation)
and an isomorphism `φ : W' ≃ W` that matches the vacua and, up to `σ`, the cocycles:
`σ (∫ f dμ) = ∫ σ ∘ f ∘ φ dμ'` for every `f`, and `σ ∘ e ∘ φ = e'`. The two parts are
`map_integral_eq_integral_comp_equiv` and `map_vacuum_comp_equiv`, which do not need `hβ`. 

### `transport`

 For a topological isomorphism `φ : W' ≃ W` matching the vacua and, up to `σ`, the
bicharacters, the continuous `σ`-semilinear map `v ↦ σ ∘ v ∘ φ` between the reproducing spaces. 

### `norm_transport`

 Transport keeps the `L¹` norm, as `σ` is isometric and `φ` preserves the measure. 
