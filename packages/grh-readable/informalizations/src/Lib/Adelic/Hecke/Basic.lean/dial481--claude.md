---
{
  "module": "src/Lib/Adelic/Hecke/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Hecke/Basic.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Hecke/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Level spaces, Hecke operators, stabilisers and class sums

For an abstract group `G` with subgroups `Γ`, `K`, `H` and a representation `π` over a commutative
semiring, this file defines the level space of `K`, Hecke operators and weighted class sums over
`Γ \ G / K`. The Hecke operator `New.heckeFun π K f = ∑ f(g) π(g)` sums over chosen representatives
`g` of `G ⧸ K` and is applied to vectors fixed by `K`. When `f (g * k) = f g` for `k ∈ K` and `v` is
such a vector, the term `f g • π g v` depends only on the coset `g K`. The file proves that, under
this condition, the value at `v` does not depend on the choice of representatives.

## Main definitions and results

* `New.levelSpace`: the vectors on which `K` acts through a character `χ`.
* `New.heckeFun`, `New.heckeCoset`: the operator `∑ f(g) π(g)` over chosen representatives of
  `G / K`, and its value on the indicator function of a double coset `K g K`.
* `New.classAut`, `New.classSum`: the stabiliser `Γ ∩ g K g⁻¹`, and the sum over `Γ \ G / K`
  weighted by the inverse orders of the stabilisers.
* `New.relIndex_mul_measure_inf`, `New.measure_inter_eq_inv_relIndex`: for `K` compact and `H` open,
  the volume of `H ∩ K` times the index `[K : H ∩ K]` is the volume of `K`.
* `New.heckeFun_eq_sum`, `New.heckeFun_eq_sum_pullback`: on a vector fixed by `K`, the sum over any
  other system of representatives.
* `New.heckeFun_heckeFun`: on a vector fixed by `K`, the composite of two operators is the operator
  of a convolution.

## Relation to the literature

Known; see `Lib.Adelic.Hecke.ClassSums` for sources.



## Level spaces, Hecke operators, class sums and volumes

The sums are Mathlib's `finsum`, which is zero when the support is infinite. Since `Nat.card` of an
infinite group is zero, a class with infinite stabiliser has weight zero.


### `scoped instance : CoeFun (Rep A G) (G → Module.End A ·)`

 A representation in `Rep A G` may be applied to a group element as a function. 

### `rightRegular`

 The right regular representation of G on functions G → W: (g·F)(x) = F(xg). 

### `levelSpace`

 For a representation π of G, a subgroup K and a character χ of K, the submodule of vectors v
with π(k)v = χ(k)v for all k in K. 

### `heckeFun`

 For a function f on G, the operator ∑ f(g)π(g), summed over chosen representatives g of G/K
(zero if infinitely many terms are nonzero). Let f be right K-invariant and supported on finitely
many cosets gK. On a vector fixed by K the value does not depend on the representatives
(`New.heckeFun_eq_sum`), and it is the action of f for the measure with vol K = 1. 

### `heckeCoset`

 The Hecke operator of the double coset KgK: the sum of π(h) over chosen representatives h of
the cosets hK in KgK (zero if there are infinitely many). 

### `classAut`

 The subgroup Γ ∩ gKg⁻¹, the stabiliser in Γ of the coset gK. 

### `DoubleCosets`

 The set Γ\G/K of double cosets of a group G with respect to subgroups Γ and K. 

### `map_mem_levelSpace_of_commute`

 If `π k v = χ k • v` for all `k ∈ K` and the linear map `a` commutes with every `π k`, then
`a v` satisfies the same equations: it lies in the level space of `(K, χ)`. 

### `exists_eq_map_mul_rep_mul`

 If `r` is a system of representatives of the double cosets `e(Δ) \ G / K`, every `g` is
`e γ * r c * k` with `γ ∈ Δ`, `c` a double coset and `k ∈ K`. 

### `eq_and_eq_one_of_doubleCoset_rep`

 Let e : Δ → G be a homomorphism and r a system of representatives of e(Δ)\G/K, and let Δ act
freely at the point r(d)K of G/K. Then e(γ) r(d)K = r(c)K only for c = d and γ = 1. 

### `classSum`

 The class sum of f: the sum over the double cosets c in Γ\G/K of f(g_c)/#(Γ ∩ g_c K g_c⁻¹), g_c
a chosen representative. For f left invariant under Γ and right invariant under K the choice of
representatives does not matter (`New.classSum_eq_finsum_of_rep`). 

### `card_classAut_mul_mul`

 The order of the stabiliser Γ ∩ gKg⁻¹ depends only on the double coset ΓgK. 

### `classSum_eq_finsum_of_rep`

 For f left invariant under Γ and right invariant under K, the class sum can be computed with
any system of representatives r of Γ\G/K. 

 ### Open and compact subgroups of a topological group 

### `isLocallyConstant_of_eventually_mul`

 A function on a topological group that is invariant under right translation by all elements
of a neighbourhood of 1 is locally constant. 

### `finite_quotient_image_of_isCompact`

 For an open subgroup `H` of a topological group `G`, a compact subset `C` of `G` meets only
finitely many cosets `g H`. 

### `_root_.IsCompact.relIndex_ne_zero`

 For a compact subgroup `K` and an open subgroup `H` of a topological group, the index
`[K : H ∩ K]` is finite, so it is nonzero as a natural number. 

### `relIndex_mul_measure_inf`

 For `K` compact, `H` open and `μ` left invariant, `[K : H ∩ K] · μ (H ∩ K) = μ K`. 

### `measure_inter_eq_inv_relIndex`

 For `K` compact of mass one, `H` open and `μ` left invariant, `H ∩ K` has mass
`1 / [K : H ∩ K]`. 


## Coset sums, transport and composition of Hecke operators

* `New.heckeFun_comp`, `New.heckeFun_comp_inv_mul`: transport of `New.heckeFun` along a group
  homomorphism, and its behaviour under left translation.
* `New.heckeFun_mem_levelSpace`: when the image under an operator lies in a level space.


### `HasFiniteCosets`

 The function f on G is nonzero at the chosen representatives of only finitely many cosets
gK. 

### `IsHeckeFunction`

 The function f on G is left and right K-invariant and supported on finitely many cosets gK. 

### `heckeFun_eq_sum_toFinset`

 If `f` lives on finitely many cosets, its operator is the finite sum over those cosets. 

### `map_heckeFun`

 Let `f` live on finitely many cosets `g K`. A linear map `L` that intertwines `π g` and `π' g`
at `v` for all `g` intertwines the two operators of `f` at `v`. 

### `isHeckeFunction_doubleCoset`

 For a compact open subgroup K of a topological group G and g in G, the indicator function of KgK
is K-invariant on both sides and supported on finitely many left cosets of K. 

### `heckeFun_eq_sum`

 Any representatives serve. Let `f (g * k) = f g` for `k ∈ K`, and let `v` be fixed by `K`.
Suppose the cosets `r i • K`, `i ∈ s`, are distinct and cover the support of `f`. Then (a) `f` lives
on finitely many cosets, and (b) its operator sends `v` to `∑ i ∈ s, f (r i) • π (r i) v`. 

### `heckeFun_eq_sum_pullback`

 Let f(gk) = f(g) for k ∈ K, let v be fixed by K, and let θ : G' → G induce an injection
G'/J → G/K covering the support of f. Suppose f(θ x) = 0 for the chosen representative x of every
coset outside a finite set s. Then f lives on finitely many cosets, and its operator sends v to
∑ f(θ x)π(θ x)v, over the representatives x of the cosets in s. 

### `heckeFun_comp`

 Let the homomorphism a : G' → G be surjective with a⁻¹(K) = J. Let f(gk) = f(g) and π(k)v = v
for k ∈ K, and let F = f∘a be nonzero on finitely many cosets gJ. If ρ(g)v = π(a(g))v for all g,
then the operator of F in ρ and the operator of f in π send v to the same vector. 

### `HasFiniteCosets.comp_inv_mul`

 Let `f (g * k) = f g` for `k ∈ K`. If `f` lives on finitely many cosets `g K`, so does its left
translate `g ↦ f (x⁻¹ * g)`. 

### `heckeFun_comp_inv_mul`

 Let `f (g * k) = f g` for `k ∈ K`, let `f` live on finitely many cosets, and let `v` be fixed by
`K`. The operator of the left translate `g ↦ f (x⁻¹ * g)` sends `v` to `π x` of the image of `v`
under the operator of `f`. 

### `heckeFun_heckeFun`

 Let `f` and `f'` live on finitely many cosets `g K`, let `f` be right `K`-invariant, and let `v`
be fixed by `K`. Applying the operator of `f` and then that of `f'` to `v` is the same as applying
the operator of `x ↦ ∑ f' g * f (g⁻¹ * x)`. The sum runs over the chosen representatives `g` of the
cosets where `f'` is nonzero. 

### `heckeFun_mem_levelSpace`

 Let `f` live on finitely many cosets `g K` with `f (g * k) = f g` for `k ∈ K` and
`χ' k * f (k * g) = f g` for `k ∈ K'`. The operator of `f` sends a vector fixed by `K` into the
level space of `(K', χ')`, where each `k ∈ K'` acts as the scalar `χ' k`. 

### `IsHeckeFunction.heckeFun_mem`

 The operator of a `K`-bi-invariant function on finitely many cosets preserves the space of
vectors fixed by `K`. 
