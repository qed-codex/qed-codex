---
{
  "module": "src/Lib/PadicComparison/HodgeTate/Map.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/HodgeTate/Map.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/HodgeTate/Map.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Hodge–Tate maps λ_h on pairs (S, M): construction, properties and restriction

The field `k` is embedded in `ℚ̄_p`, so it has characteristic zero. For a `p`-adic test `S`, put
`T = S[1/p]`, and let `B_S = W(S^♭)[1/p] / (ker θ)²` be the square-zero extension
`New.Variety.thickeningOver` of `T` by `T`.
Put `B_{S,M} = B_S ×_T (T ⊕ M)`. All groups are `Ext` groups of functors to abelian groups
(`New.Variety.H`). On pairs `(S, M)` with `M = T ^ n`, the Hodge–Tate map `λ_h` restricts a Hodge
class to the pairs. It then composes it with the `h`-th Yoneda power of the class of a contraction
cocycle, followed by the projection to degree zero. So `λ_h` lands in the cohomology of `N(B_{S,M})`
on pairs. This map is natural, turns scaling by `t` into multiplication by `t ^ h`, and satisfies a
binomial product rule.

## Main definitions and results

* `New.Variety.HodgeTatePair`: pairs `(S, M)` with `M = T ^ n`; a map has a semilinear part
  `M → T' × M'`.
* `New.Variety.HodgeTatePair.contractionPow`: the `h`-th Yoneda power of the class of the
  contraction cocycle `New.Variety.HodgeTatePair.contractionCocycle`, followed by the projection to
  degree zero. It is `k`-linear (`New.Variety.HodgeTatePair.act_comp_contractionPow`)
  and has weight `h` (`New.Variety.HodgeTatePair.scaleModule_comp_contractionPow`).
* `New.Variety.hodgeTateMap`: restrict a class of `New.Variety.HodgeH` to these pairs and compose
  with `contractionPow h`. `New.Variety.restrictToPairs` maps the degree-`n` cohomology of `N(T)` on
  `p`-adic tests to the same target `New.Variety.PairH`.
* `New.Variety.PairRestrictBijective`: restriction along `B_{S,M} → T` is bijective on cohomology in
  all degrees.
* `New.Variety.PairRestrictBijective.exists_hodgeTateMap_eq`: under this hypothesis,
  `hodgeTateMap h x` for `x` of degree `q` comes from a class of degree `q + h`.
* `New.Variety.IsChartCovered.pairRestrictBijective`: `PairRestrictBijective` holds for `ℤ[X]` if
  `X` is covered by étale charts. The map `B_{S,M} → T` is a square-zero extension
  (`New.Variety.HodgeTatePair.isSquareZero_toGeneric`), so the lifts of a point of a chart of
  dimension `n` are represented by one pair `(S, T ^ n)`.

Notions from other files:
* `New.Variety.PadicTest`: a p-adic test, a non-empty family of cells (`New.Variety.IsCell`) with a
  ring map from O_C to their product.
* `New.Variety.Cocycle`: a 1-cocycle from F to G, homomorphisms D(f): F(c) → G(d) for f: c → d, with
  D(gf) = G(g)D(f) + D(g)F(f); `D.cohomClass` is its class in Ext¹(F, G).
* `New.Variety.contraction`: for semilinear φ = (φ₀, φ₁): M → T' × M', the map ⋀M → ⋀M' that
  contracts with φ₀ and applies φ₁.
* `New.Variety.TotalH`: the total Ext group, the direct sum of the Ext^n(N,F) over all n ≥ 0;
  `comp x y` is the Yoneda product, `x` followed by `y`.
* `New.Variety.HodgeH`: Hodge cohomology of a functor N on k-algebras, Ext^q from (A, M) ↦ N(A ⊕ M)
  to (A, M) ↦ ⋀_A M on pairs of a k-algebra A and a free module M = A^ι.

## Relation to the literature

Known; see `Lib.PadicComparison.HodgeTate.PeriodMap` for sources.



## The site of Hodge–Tate pairs and powers of the contraction class

* `New.Variety.HodgeTatePair.pairAlg`: the ring `B_{S,M} = B_S ×_T (T ⊕ M)`, with its projections
  `New.Variety.HodgeTatePair.toSqZero` to `T ⊕ M` and `New.Variety.HodgeTatePair.toGeneric` to `T`.
* `New.Variety.HodgeTatePair.contractionCocycle`: contraction with the component `M → T'` is a
  1-cocycle from `Λ = ⋀_T M` to `Λ`.


 ### The category of pairs 

### `HodgeTatePair`

 A pair (S, M) of a p-adic test S and the free module M = T^n over T = S[1/p], given by S and
the rank n. 

### `HodgeTatePair.test`

 The `p`-adic test `S`. 

### `HodgeTatePair.rank`

 The rank `n` of the free module `M = T ^ n` over `T = S[1/p]`. 

### `GenericRing`

 For a pair (S, M), the k-algebra T = S[1/p]: `New.Variety.genericOver` of the test S, its ring
with p inverted. 

### `instance : Category HodgeTatePair`

 Morphisms of pairs. A morphism (S, M) ⟶ (S', M') is a pair (f, φ) of a map of tests
f : S ⟶ S' and a map φ = (φ₀, φ₁) : M → T' × M' that is semilinear over the ring map T → T'
induced by f. The identity is (𝟙, m ↦ (0, m)), and (f, φ) followed by (g, ψ) is
(f ≫ g, m ↦ (g(φ₀ m), 0) + ψ(φ₁ m)). 

### `testMap`

 The map of tests `S ⟶ S'` of a morphism of pairs `(S, M) ⟶ (S', M')`. 

### `moduleMap`

 The map `φ = (φ₀, φ₁) : M → T' × M'` of a morphism of pairs, semilinear over `T → T'`. 

### `toTest`

 The forgetful functor from pairs (S,M) to p-adic tests, sending (f,φ) to f. 

### `toHodgeTest`

 The functor (S,M) ↦ (T,M) to the tests of Hodge cohomology, sending (f,φ) to the ring map
induced by f and the second component of φ. 

 ### The rings `B_{S,M}` 

### `PairRing`

 For a pair (S,M), the k-algebra B_S ×_T (T ⊕ M), with B_S as in `New.Variety.thickeningOver`
and T ⊕ M the trivial square-zero extension. 

### `PairRing.base`

 The `B_S` component `b` of a point `x = (b, (s, m))` of `B_S ×_T (T ⊕ M)`. 

### `PairRing.sqZero`

 The `T ⊕ M` component `(s, m)` of a point `x = (b, (s, m))` of `B_S ×_T (T ⊕ M)`. 

### `proj_map_fst`

 Let `f : X ⟶ Y` be a morphism of pairs and `x = (b, (s, m))` a point of `B_S ×_T (T ⊕ M)`, so
that `b` projects to `s` in `T`. Then the image of `b` under the map of tests `testMap f`
projects to the image of `s` in `T'`. 

### `map_base_add_mulMu_mul`

 Let `f : X ⟶ Y` be a morphism of pairs with `moduleMap f = (φ₀, φ₁)`. The map from
`B_S ×_T (T ⊕ M)` to `B_{S'}` sending `x = (b, (s, m))` to `f₀(b) + μ·φ₀(m)` is multiplicative,
where `f₀ = testMap f` and `μ·_` is `thickeningOver.mulMu`, induced by multiplication by
`μ = [ε] − 1`. 

### `map_fst_add_mulMu_add`

 Let `f : X ⟶ Y` be a morphism of pairs with `moduleMap f = (φ₀, φ₁)`. The map from
`B_S ×_T (T ⊕ M)` to `B_{S'}` sending `x = (b, (s, m))` to `f₀(b) + μ·φ₀(m)`, `f₀ = testMap f`, is
additive; `map_base_add_mulMu_mul` says that it is multiplicative. 

### `pairAlg`

 The functor (S, M) ↦ B_{S,M} = B_S ×_T (T ⊕ M) to k-algebras. A morphism (f, (φ₀, φ₁)) acts by
(b, (s, m)) ↦ (f(b) + μ·φ₀(m), (f(s), φ₁(m))), where μ·_ is `thickeningOver.mulMu`; the first
component is additive and multiplicative by `map_fst_add_mulMu_add` and `map_base_add_mulMu_mul`. 

### `toSqZero`

 The natural projection of k-algebras B_S ×_T (T ⊕ M) → T ⊕ M. 

### `toGeneric`

 The natural map of k-algebras B_S ×_T (T ⊕ M) → T: `toSqZero` followed by the projection
T ⊕ M → T, (s, m) ↦ s. 

 ### Coefficients, the contraction cocycle and its powers 

### `formCoeff`

 The functor sending a pair (S,M) to the abelian group ⋀_T M, the restriction of the
coefficients of Hodge cohomology. 

### `scalarCoeff`

 The coefficient functor `New.Variety.genericCoeff` (S ↦ T = S[1/p]) on p-adic tests, restricted
to pairs along (S,M) ↦ S. 

### `instance : CoeffAction k scalarCoeff`

 The field k acts on F = `scalarCoeff`, (S, M) ↦ T, by natural endomorphisms `CoeffAction.act t`,
here multiplication by t on T, through its action on `New.Variety.genericCoeff`. 

### `contractionCocycle`

 The cocycle from Λ = ⋀_T M (`formCoeff`) to itself that assigns to a morphism (f, φ) with
φ = (φ₀, φ₁) the map `New.Variety.contraction φ` : ⋀M → ⋀M', which contracts with φ₀ and applies
φ₁ to the remaining factors. 

### `contractionPow`

 For h : ℕ, the class in total Ext(Λ, F) given by the h-th Yoneda power of the class of
`contractionCocycle` in Ext¹(Λ, Λ), followed by the projection of ⋀M onto its degree-zero part T.
Here Λ = `formCoeff`, (S, M) ↦ ⋀_T M, and F = `scalarCoeff`, (S, M) ↦ T. 

### `wedgePairing`

 The natural map Λ ⊗ Λ → Λ given by the wedge product in ⋀_T M. 

### `act_comp_contractionPow`

 The class `contractionPow h` is `k`-linear. For `t : k`, multiplication by `t` on `Λ = ⋀ M`
(`CoeffAction.act t` on `hodgeCoeff`), followed by `contractionPow h`, is `t • contractionPow h`,
where `k` acts on `F = T` by the `CoeffAction` instance on `scalarCoeff`. 

### `scaleModule_comp_contractionPow`

 On pairs `(S, M)` of a `p`-adic test `S` and a free module `M = T^n` over `T = S[1/p]`, let `Λ`
be `(S, M) ↦ ⋀_T M`. `contractionPow h` is the class in total Ext from `Λ` to `(S, M) ↦ T` given by
the `h`-th Yoneda power of the contraction class in `Ext¹(Λ, Λ)`, followed by the projection of
`⋀ M` onto degree zero. This class has weight `h`: for `t : k`, precomposing it with the
endomorphism of `Λ` induced by `m ↦ t • m` (`HodgeTest.scaleModule`, which multiplies forms of
degree `d` by `t ^ d`) gives `t ^ h • contractionPow h`. 

 ## The Hodge–Tate maps λ_h: naturality, scaling and the product rule 

### `PairH`

 For a functor `N` from `k`-algebras to abelian groups, the total cohomology on pairs `(S, M)`
of `(S, M) ↦ N(B_{S,M})` with coefficients `scalarCoeff`, `(S, M) ↦ T = S[1/p]`; the target of
`λ_h`. 

### `hodgeTateMap`

 The Hodge–Tate map `λ_h` on the degree-`q` Hodge cohomology of `N`. A class `x` is pulled back
along `B_{S,M} → T ⊕ M` to the cohomology on pairs, put in total degree `q`, and composed with
`contractionPow h`: the `h`-th power of the class of the contraction cocycle, followed by the
projection of `⋀ M` to degree zero. 

### `PairH.map`

 For `α : N' ⟶ N`, the `k`-linear pull-back from `PairH N` to `PairH N'` along the natural map
`N'(B_{S,M}) → N(B_{S,M})` induced by `α`. 

### `restrictToPairs`

 The `k`-linear map from the degree-`n` cohomology on `p`-adic tests `S` of `S ↦ N(T)`,
`T = S[1/p]` (`genericOver`), with coefficients `genericCoeff` (`S ↦ T`), to `PairH N`: pull back
along `B_{S,M} → T` and include as the degree-`n` summand. 

### `restrictToPairs_map`

 `restrictToPairs` is natural in `N`: for `α : N' ⟶ N`, restricting the pull-back of `x` along
`α` gives `PairH.map α` of the restriction of `x`. 

### `hodgeTateMap_map`

 The Hodge–Tate map is natural in the functor `N` from `k`-algebras to abelian groups: for
`α : N' ⟶ N` and a Hodge class `x` on `N`, `λ_h` of the pull-back of `x` along `α` is `PairH.map α`
of `λ_h x`. 

### `hodgeTateMap_scale`

 The map `λ_h` has weight `h`: for `t : k` it turns `HodgeH.scale t`, the endomorphism of Hodge
cohomology induced by `(a, m) ↦ (a, t m)` on `A ⊕ M`, into multiplication by `t ^ h`. 

### `HodgeTatePair.cross`

 For functors `M`, `L` on pairs (`M` with flat values) and `y` in the total cohomology of `L`
with coefficients `scalarCoeff` (`(S, M) ↦ T`), the `k`-linear map `x ↦ x × y` to the total
cohomology of `M ⊗ L` (`abTensor`, the objectwise tensor product): the external product
`x.cup y` followed by the multiplication `T ⊗ T → T`. 

### `HodgeTatePair.tensorContractionCocycle`

 The cocycle on `formCoeff ⊗ formCoeff` (`Λ ⊗ Λ`, `Λ = ⋀ M`) with values in two copies of it.
At a morphism `f`, its `true` component is `D(f) ⊗ Λ(f)` and its `false` component is
`Λ(f) ⊗ D(f)`, where `D` is `contractionCocycle`. 

### `HodgeTatePair.cup_comp_tensorContractionCocycle_π_true`

 Let `M`, `L` be functors on pairs, `M` with flat values, `x` a class of degree `a` on `M` and
`y` a total class on `L`, both with coefficients `formCoeff` (`Λ = ⋀ M`). The `true` component
(`piAbFunctor.π _ true`) of the class of `tensorContractionCocycle`, after the external product of
`x` and `y`, is the class of `contractionCocycle` applied to the first factor `x`. 

### `HodgeTatePair.cup_comp_tensorContractionCocycle_π_false`

 Let `M`, `L` be functors on pairs, `M` with flat values, `x` a class of degree `a` on `M` and
`y` a total class on `L`, both with coefficients `formCoeff` (`Λ = ⋀ M`). The `false` component
(`piAbFunctor.π _ false`) of the class of `tensorContractionCocycle`, after the external product of
`x` and `y`, is the class of `contractionCocycle` applied to the second factor `y`, times the sign
`(-1) ^ a` for moving it past `x`. 

### `HodgeTatePair.tensorContractionCocycle_comp_wedgePairing`

 The Leibniz rule for the contraction (`contraction_mul`) on classes. The `false` component of
`tensorContractionCocycle`, followed by the grade involution (scaling by `-1`) on the first
factor, plus its `true` component, followed by the wedge product, is the class of
`contractionCocycle` pulled back along the wedge product. 

### `HodgeTatePair.contractionPow_cup`

 The binomial rule for the powers of the contraction class. Pairs are `(S, M)` with `S` a
`p`-adic test and `M = T^n`, `T = S[1/p]`; let `M`, `L` be functors on pairs, `M` with flat values.
Write `u_l(z)` for a class `z` with coefficients `formCoeff` (`(S, M) ↦ ⋀_T M`) followed by
`contractionPow l`. This is the `l`-th Yoneda power of the contraction class in `Ext¹`, then the
projection of `⋀ M` onto `T`. Write `x ∧ y` for `TotalH.cup` followed by `wedgePairing`, and `X × Y`
for `cross Y X`, the external product followed by `T ⊗ T → T`. For `x` of degree `a` and any `y`,
`u_l(x ∧ y) = ∑_{h ≤ l} C(l, h) (-1)^((a + h)(l - h)) u_h(x) × u_{l-h}(y)`. 

### `hodgeTateMap_cup`

 Product formula: let `N`, `N'` be functors from `k`-algebras to abelian groups, `x` a Hodge
class of degree `a` on `N` (with flat values) and `y` one of degree `b` on `N'`. Their product
`x ∧ y = cup exteriorAlg.mulPairing x y e`, through the wedge product, is a Hodge class of degree
`n = b + a` on `N ⊗ N'` (`abTensor`, objectwise), and `λ_l(x ∧ y) = ∑_{h ≤ l} C(l, h)
(-1)^((a + h)(l - h)) λ_h(x) × λ_{l-h}(y)`. On the right `New.Variety.HodgeTatePair.cross Y` is the
linear map `X ↦ X × Y`; the binomial coefficient and the sign multiply this map before it is applied
to `λ_h(x)`. 


## Bijectivity of restriction along B_{S,M} → S[1/p] for chart-covered functors

`New.Variety.Comparison.pull` is the pull-back of classes between two sites, and
`New.Variety.genericCoeff` is the functor `S ↦ T`.


### `PairRestrictBijective`

 For a functor `N` from `k`-algebras to abelian groups: pull-back along `B_{S,M} → T`, from the
cohomology of `S ↦ N(T)` on `p`-adic tests `S` to that of `(S, M) ↦ N(B_{S,M})` on pairs `(S, M)`,
both with coefficients `T = S[1/p]`, is bijective in every degree. 

### `PairRestrictBijective.injective_restrictToPairs`

 Under `New.Variety.PairRestrictBijective` the map `New.Variety.restrictToPairs` from degree `n`
to total cohomology on pairs is injective, for every `n`. 

### `HodgeTatePair.exists_contractionPow_eq_directSum_of`

 The class `contractionPow h` is homogeneous of degree `h`: it is the image under `DirectSum.of`
of a class of degree `h`. 

### `PairRestrictBijective.exists_hodgeTateMap_eq`

 If restriction along B_{S,M} → T = S[1/p] is bijective on the cohomology of N
(`New.Variety.PairRestrictBijective`), then for `x : HodgeH N q` the class `hodgeTateMap h x` is the
restriction (`New.Variety.restrictToPairs`) of a class of degree q + h on p-adic tests. 

### `HodgeTatePair.existsUnique_hom`

 Let `A = (S, T ^ r)` and `D = (S', M')` be pairs, `f : S ⟶ S'` a map of tests and
`v i ∈ T' × M'` for `i < r`. Exactly one map of pairs `g : A ⟶ D` has map of tests `testMap g = f`
and semilinear part `moduleMap g : T ^ r → T' × M'` sending the `i`-th basis vector to `v i`. 

### `HodgeTatePair.isSquareZero_toGeneric`

 For a pair `A = (S, M)`, the map `toGeneric : B_{S,M} → T = S[1/p]` is a square-zero extension:
it is surjective and its kernel has square zero. 

### `hasPartitions_genericCoeff`

 The coefficients `genericCoeff` (`S ↦ T = S[1/p]`) are additive on `p`-adic tests
(`HasPartitions`): a decomposition of the ring of a test by idempotents gives one of the group. 

### `HodgeTatePair.hasPartitions_scalarCoeff`

 The coefficients `scalarCoeff` (`(S, M) ↦ T`) on pairs are additive (`HasPartitions`, for the
rings of the underlying tests): a pair is cut along an idempotent by cutting its test and keeping
its rank. 

### `IsChartCovered.pairRestrictBijective`

 Let `X` be a functor from `k`-algebras to types such that every field-valued point of `X` lies
in an étale chart with `n` coordinates (`IsChartCovered n X`). Then `freeAb X`, the functor
`A ↦ ℤ[X(A)]`, satisfies `New.Variety.PairRestrictBijective`. With `T = S[1/p]`, this means that
pull-back along `B_{S,M} → T` is bijective in every degree, from the cohomology of `S ↦ ℤ[X(T)]` on
`p`-adic tests `S` to that of `(S, M) ↦ ℤ[X(B_{S,M})]` on pairs `(S, M)`, both with coefficients
`T`. 
