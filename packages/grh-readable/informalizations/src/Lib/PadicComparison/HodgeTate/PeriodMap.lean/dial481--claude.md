---
{
  "module": "src/Lib/PadicComparison/HodgeTate/PeriodMap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/HodgeTate/PeriodMap.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/HodgeTate/PeriodMap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The period map for ℓ-adic cohomology on p-adic tests, and Hodge–Tate weights

This file compares the geometric cohomology `New.Variety.ellAdicCohom R Ω n` of an `R`-scheme `Y`
(`Ω` an `R`-algebra on which a group `Γ` acts by ring maps fixing the image of `R`), written
`V^n(Y)`, with the cohomology of the points of `Y` in `p`-adic tests. A vector has weight `h`
(`New.HasHodgeTateWeight`) if Galois acts on it by the `(-h)`-th power of the cyclotomic character.

## Main definitions and results

* `New.Variety.toTwistAlg`: the identity of a `p`-adic test as an `R`-algebra map to its Galois
  twist.
* `New.Variety.exists_period_map`: the period map is natural, Galois equivariant, and bijective for
  proper charted `Y`. It is the pull-back along the comparison of
  `New.Variety.exists_primitive_period_comparison`.
* `New.Variety.exists_hasHodgeTateWeight`: the value of the Hodge–Tate map on a Hodge class comes
  from a vector of weight `h`, naturally in maps to `Y`.

Notions from other files:
* `New.Variety.PadicTest`: A p-adic test c: a non-empty family of cells, whose product is the ring
  `c.ProdRing`, with a ring map from O_C, the integers of ℂ_p, to that product.
* `New.Variety.PadicTest.twist`: For g in G_p, the endofunctor of p-adic tests that keeps the ring
  and precomposes its structure map O_C → c.ProdRing with the action of g.

## Relation to the literature

Known result: The primitive comparison theorem and the period isomorphism. Here coefficients are
constant, schemes are proper and charted (`New.Variety.IsCharted`), cohomology is taken on test
rings, and the maximal ideal is put into the coefficients. The result is deduced from the duality
comparison on products of projective lines, without almost finiteness. Source: P. Scholze, p-adic
Hodge theory for rigid-analytic varieties, Forum Math. Pi 1 (2013), Thm 1.3 and 5.1; for the method,
B. Zavyalov, Poincaré duality in abstract 6-functor formalisms, arXiv 2301.03821, Thm 3.3.3 and
Appl. 1.3.4; Li–Reinecke–Zavyalov, arXiv 2410.08200, §6.4.

Known result: The Hodge–Tate map from Hodge cohomology to p-adic étale cohomology. The target here
is cohomology on test rings, which is not identified with étale cohomology. Only the natural
multiplicative map into the part of weight h is built, from the torsor of lifts modulo the square of
the kernel of Fontaine's map, and bijectivity is not proved. Source: Scholze, p-adic Hodge theory
for rigid-analytic varieties, Forum Math. Pi 1 (2013), Cor. 1.8; the construction follows Bhatt, The
Hodge–Tate decomposition via perfectoid spaces, Arizona Winter School 2017, §3.4.



## The period map on p-adic tests

The period map compares the geometric `p`-adic cohomology `New.Variety.ellAdicCohom R Ω n` of an
`R`-scheme `Y`, extended to a period ring `K`, with the cohomology of the points of `Y` in `p`-adic
tests (`New.Variety.PadicTest`, `New.Variety.testPoints`) with coefficients `Ψ`. Here `θ` identifies
`Ψ c` with `K ⊗_S (S ⊗_{A_inf} W(c^♭))^`, the hat denoting `p`-adic completion, for an
`A_inf`-algebra `S`.


### `toTwistAlg`

 The identity of a test is a map of `R`-algebras to its twist by `j g`. Here
`algFunctor ⋙ restrictAlg R OC` sends a test `c` to the ring `c.ProdRing`, made an `R`-algebra
through `R → O_C`. 

### `toTwistPoints`

 A point of `Y` in a test is a point of `Y` in the twist of the test by `j g`. 

### `instance (M : ModuleCat ℚ_[p]) : CompatibleSMul ℤ_[p] ℚ_[p] K M`

 `ℚ_p` is a localization of `ℤ_p`, so the two scalar actions on `K ⊗ M` agree. 

### `periodTmul`

 The element `θ (a ⊗ 1 ⊗ w)` of `Ψ c`, for `a` in `K` and a Witt vector `w` over the tilt of
the test `c`. 

### `ActsAsOnFrobeniusFixed`

 The map of coefficients `β`, from the twist of `Ψ` by `g` to `Ψ`, acts as `σ` on the elements
`θ (a ⊗ 1 ⊗ w)`, where `w` is a Witt vector whose coordinates are fixed by Frobenius.
`moduleCoeff Ψ` is `Ψ` with values lifted by `ULift`, and `⟨_⟩` wraps an element of `Ψ c`. 

### `IsPadicPeriodMap`

 A `p`-adic period map: `K`-linear maps `J Y` from `K ⊗ V^n(Y)` to `H^n` of the points of `Y`
in tests, with coefficients `Ψ`, that are natural, Galois equivariant and bijective on proper
charted `Y`. Here `V^n(Y)` is the geometric `p`-adic cohomology `ellAdicCohom R Ω n` of `Y`. 

### `IsPadicPeriodMap.natural`

 `J` commutes with the pull-back along `f : W ⟶ Y`. 

### `IsPadicPeriodMap.equivariant`

 `J` carries `σ ⊗ g` to the pull-back along `β` and the twist by `j g`, if `β` acts as `σ`. 

### `IsPadicPeriodMap.bijective`

 `J Y` is bijective if `Y` is proper and charted over `Ω`. 

### `coeffHom_eq_coeffHom_trans_of_actsAsOnFrobeniusFixed`

 Let `γ` send `a ⊗ x` to `θ (a ⊗ 1 ⊗ w)`, where `w` is the Witt vector over the tilt obtained
from `x`, and let `β` act as `σ` on the elements `θ (a ⊗ 1 ⊗ w)` with `w` fixed by Frobenius
(`ActsAsOnFrobeniusFixed`). Then the comparison `x ↦ γ (σ a ⊗ x)` is the comparison
`x ↦ γ (a ⊗ x)` followed by `β`, since Witt vectors of locally constant `𝔽_p`-valued functions are
fixed by Frobenius. 

### `exists_period_map`

 Let `(S, K)` be a period ring pair (`New.Variety.IsPeriodRingPair`: `S` is a `p`-torsion-free,
`p`-adically complete `A_inf`-algebra in which `p` divides `ξ`, and `τ` is a unit in `K`), with `K`
flat over `S`. Let `Ψ` be a functor from `p`-adic tests `B` to `K`-modules, identified by `θ` with
`K ⊗_S (p-adic completion of S ⊗_{A_inf} W(B^♭))`. Let `e : Ω →+* ℚ̄_p` agree with `R → O_C` on `R`,
and let `j : Γ → G_p` satisfy `j g (e x) = e (g • x)`. Then there are `K`-linear maps `J Y` from
`K ⊗ V^n(Y)` to `H^n` of `ℤ[Y(B)]` (the `R`-points of `Y` in tests), with coefficients `Ψ`, that
form a `p`-adic period map (`IsPadicPeriodMap`): natural in `Y`, Galois equivariant, and bijective
for proper charted `Y`. 

 ## Hodge–Tate weights of values of the Hodge–Tate map 

### `New.Variety.exists_hasHodgeTateWeight`

 Let `Y`, `W` be proper over `R`, with `Y` smooth of relative dimension `d` and charted over `Ω`.
Let `E` be a field between `R` and `Ω` that is mapped to `k ⊆ ℚ̄_p`, and `A` a subring of `Ω`
containing the image of `R`. Let `e : Ω → ℚ̄_p` be a `p`-adic place embedding for `A` over `E`
(`New.GaloisRep.PadicPlaceEmbedding`) agreeing with `E → k → ℚ̄_p` on `E`, and `ε` a section of
`k → ℚ̄_p`. Take any `h` and a Hodge class `x` of degree `q` of `Y` over `E` (in Ext^q from
`(S, M) ↦ ℤ[Y(S ⊕ M)]` to `(S, M) ↦ ⋀_S M`). Then there are a vector `v` of `ℂ_p ⊗ V^(q+h)(Y)` and
an `ε`-semilinear map `Θ` from `ℂ_p ⊗ V^(q+h)(W)` to cohomology on pairs with coefficients `S[1/p]`
(`PairH`) such that: (a) `v` has Hodge–Tate weight `h` for the decomposition group of `A` in
`Gal(Ω/E)`; (b) `hodgeTateMap h (u^* x) = Θ (u^* v)` for all `u : W ⟶ Y`, where `hodgeTateMap h`
pulls back along `B_{S,M} → T ⊕ M` and applies the `h`-th power of the contraction class. 
