---
{
  "module": "src/Lib/PadicComparison/HodgeTate/GaloisWeight.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/HodgeTate/GaloisWeight.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/HodgeTate/GaloisWeight.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Galois twists and the weight of the Hodge–Tate map

An element `g` of `Gal(ℚ̄_p/ℚ_p)` twists a p-adic test `c` by precomposing its structure map
`O_C → R` with `g` (`New.Variety.PadicTest.twist`). The twist leaves the rings `R`, `K = R[1/p]` and
`B = W(R♭)[1/p] / (ker θ)²` unchanged. Write `μ = [ε] − 1` and `χ` for the cyclotomic character.
Suppose `g` fixes `E` and `New.Variety.restrictToPairs ξ` is the image under
`New.Variety.hodgeTateMap h` of a Hodge class defined over `E`, and that `χ(g⁻¹)` is the image in
ℚ̄_p of some `t : k`. Then the twist by `g` multiplies `New.Variety.restrictToPairs ξ` by
`χ(g⁻¹)^h`.

## Main definitions and results

* `New.Variety.thickeningOver.mulMu_twist`: the inclusion `ι : K → B` (multiplication by `μ`)
  changes by the cyclotomic character `χ(g⁻¹)` (`New.cyclotomicGp`), as `g⁻¹ μ ≡ χ(g⁻¹) μ` modulo
  `μ²`.
* `New.Variety.HodgeTatePair.galTwist`: the twist on pairs `(c, K^n)` (`New.Variety.HodgeTatePair`).
* `New.Variety.HodgeTatePair.contractionPow_galTwist`: the classes
  `New.Variety.HodgeTatePair.contractionPow` (the `h`-th power of the contraction class, then the
  projection to degree zero) are compatible with the twist.

Notions from other files:
* `New.Variety.PadicTest`: A p-adic test: a non-empty family of cells (`New.Variety.IsCell`) with a
  ring map from O_C to their product R.
* `New.Variety.thickeningOver.mulMu`: The additive map ι: K → B sending θ(x) to the class of μx,
  where μ = [ε] − 1.
* `New.Variety.HodgeTatePair`: A pair (S,M) of a p-adic test S and a free module M of finite rank
  over T = S[1/p]; `New.Variety.HodgeTatePair.pairAlg` sends it to B_{S,M} = B_S ×_T (T ⊕ M).
* `New.Variety.hodgeTateMap`: The map λ_h: restrict a Hodge class along B_{S,M} → T ⊕ M, apply the
  h-th power of the contraction class, and project ⋀M to degree zero.
* `New.Variety.restrictToPairs`: Restriction along B_{S,M} → T, from the cohomology of N(T) on
  p-adic tests S to that of N(B_{S,M}) on pairs. `New.Variety.PairRestrictBijective` says that it is
  bijective in all degrees.

## Relation to the literature

Known; see `Lib.PadicComparison.HodgeTate.PeriodMap` for sources.


 ## Twisting p-adic tests, pairs and contraction classes 

### `PadicTest.genericStructureMap_twist`

 The structure map `ℂ_p → R[1/p]` of the `g`-twist of a test `c` is `g` followed by the
structure map of `c`. 

### `PadicTest.uniqueLift_comp_eq_uniqueLift_twist`

 The lift of the `g`-twist of a test `c` to its thickening is `g` followed by the lift for `c`:
both lifts reduce to the structure map, and the lift is unique (`PadicTest.eq_uniqueLift`). 

### `thickeningOver.mulMu_twist`

 For a `p`-adic test `c` with ring `R`, let `ι = mulMu` be the additive map from `K = R[1/p]` to
`B = W(R♭)[1/p]/(ker θ)²` sending `θ(x)` to the class of `μx`, where `μ = [ε] − 1`. For `g ∈ G_p`,
the `g`-twist of `c` has the same `K` and `B`, and `ι` of `c` at `t` equals `ι` of the twist at
`χ(g⁻¹) t`. Here `χ` is the cyclotomic character, and `χ(g⁻¹)` is mapped into `K` by the structure
map `ℂ_p → K`. 

### `twistGenericCoeff`

 The natural map from `New.Variety.genericCoeff` after the `g`-twist to
`New.Variety.genericCoeff`. It is the identity on each `R[1/p]`. 

### `HodgeTatePair.galTwist`

 For `g` in the Galois group of `ℚ̄_p/ℚ_p`, the endofunctor of `New.Variety.HodgeTatePair`
twisting the structure map of the underlying test by `g` and keeping all other data. 

### `HodgeTatePair.twistForms`

 The identity of the exterior algebra of K^n, K = R[1/p], as a natural map from
`New.Variety.HodgeTatePair.formCoeff` to `New.Variety.HodgeTatePair.formCoeff` composed with the
g-twist. 

### `HodgeTatePair.contractionPow_galTwist`

 The class `contractionPow h` is compatible with the `g`-twist. Restrict it along the twist of
pairs. Compose it with the identification `twistGenericCoeff g` of the coefficients. Then pull it
back along the identification `twistForms g` of the exterior algebras. The result is the class
`contractionPow h` itself. 

 ## Galois action in weight h 

### `hodgeTateMap_galois_twist`

 Let `g` in `Gal(ℚ̄_p/ℚ_p)` fix the subfield `E` of `k ⊆ ℚ̄_p`. Let `x` be a Hodge class of `N`
over `E`, meaning a degree-`q` Ext class from `(A, M) ↦ N(A ⊕ M)` to `(A, M) ↦ ⋀_A M`. Let `ξ` be a
degree-`n` class on `p`-adic tests `S` (families of valuation rings over O_C) with coefficients
`S[1/p]`, such that `hodgeTateMap h x.baseChange = restrictToPairs ξ`. Here `hodgeTateMap h` uses
the `h`-th power of the contraction class, and `restrictToPairs` is the restriction from tests to
pairs of a test and a free module. Let `t : k` map to the value of the cyclotomic character at
`g⁻¹`. Let `τ` be the identity of each ring `S[1/p]`, viewed as an `E`-algebra map from the ring of
`S` to that of its twist by `g`. Then the pull-back of `ξ` along the twist by `g`, `τ` and the
identification `twistGenericCoeff g` of the coefficients has the same image under `restrictToPairs`
as `t ^ h • ξ`. 
