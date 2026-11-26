---
{
  "module": "src/Lib/Adelic/AutomorphicForms/BlockPeriods.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/BlockPeriods.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/BlockPeriods.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Periods of algebraic forms over a block subgroup as class sums via branching

This file takes an algebraic form `ψ` on a definite unitary group of rank `m + 1`, a finite point
`u` of rank one and an automorphic `Φ(x, g) = L_g(ρ₀(x) c)` on the block subgroup of rank `m`.
It turns the integral of `Φ(h) ψ_t(diag(h, u))` into a class sum (`New.classIntegral`) over the
finite adelic points. Here `ψ_t = New.algFormCoeff 1 t ψ`, and `ρ`, `ρ₀` are the representations
`New.conjWeylRep` of weights `(κ, e)` and `(κ₀, e₀)`. The archimedean integral gives an
intertwiner from weight `(κ, e)` to weight `(κ₀, e₀)`, which multiplicity one for branching
(`New.SpansBranchingMaps`) makes a multiple of the given matrix `A`.

## Main definitions and results

* `New.Seesaw.integral_algFormCoeff_blockEmb`: the period over a block subgroup as a class sum.
* `New.Seesaw.isAutomorphic_algFormCoeff_blockEmb`: for a finite point `u` of rank one, the
  restriction `h ↦ ψ_t(diag(h, u))` to a block is automorphic on the smaller standard space.

Notions from other files:
* `New.Space.IsAutomorphic`: a function on `G = G_∞ × G_f` that is continuous, left invariant under
  rational points and right invariant under an open subgroup of `G_f`.
* `New.algFormCoeff s L φ`: the function `(x, g) ↦ L (ρ(x⁻¹) φ(g))`; it is `New.ofAlgForm l s φ` for
  `L = ⟨v⁺, ·⟩`, where `⟨·, ·⟩ = New.gramForm`.
* `New.classIntegral Γ K f`: the integral of `f` over `Γ \ G_f` for `vol K = 1`, as a finite sum.

## Relation to the literature

Known; see `Lib.Adelic.AutomorphicForms.AutomorphicAsAlgebraic` for sources.


### `val_fst_blockEmb_one`

 The archimedean component of `diag((y, k), 1) = G.blockEmb hσ ((y, k), 1)` at a place `τ` is the
block matrix `diag(y τ, 1)`, reindexed along `σ` (`GL.blockScalar`). 

### `fst_blockEmb_one_one`

 The block embedding sends a finite point `(1, k)` of the block to a finite point. 

### `conjWeylMatrix_eq_weylRep_map_conj`

 `conjWeylMatrix κ e y` is `weylRep κ e` at the entrywise complex conjugate of `y`;
`conjWeylRep κ e y v` is `conjWeylMatrix κ e y *ᵥ v`. 

### `map_conj_mem_uSign_one`

 The entrywise complex conjugate of a unitary matrix is unitary. 

### `isAutomorphic_algFormCoeff_blockEmb`

 Let `ψ` be an algebraic form, `t` a linear functional and `ψ_t = algFormCoeff 1 t ψ` the
function `(x, g) ↦ t (ρ(x⁻¹) ψ(g))`. For a finite point `u` of rank one, the restriction
`h ↦ ψ_t(diag(h, u))` to a block is automorphic on the smaller standard space. Here
`diag = G.blockEmb hσ`. 

### `exists_eq_smul_of_intertwines`

 Suppose every intertwiner from weight `(κ, e)` to weight `(κ₀, e₀)` is a multiple of `A`
(`SpansBranchingMaps`). Then so is a matrix `B` with `B ρ(diag(y, 1)) = ρ₀(y) B` for all `y` in the
archimedean group of the block. Here `ρ` and `ρ₀` are the representations `conjWeylMatrix` of
weights `(κ, e)` and `(κ₀, e₀)`, and `diag(y, 1)` is the archimedean part of `G.blockEmb hσ`. 

### `integral_algFormCoeff_blockEmb`

 Let `V` be standard, `diag = G.blockEmb hσ` the embedding of the product of the block and the
rank-one group, and `A` a matrix of which every intertwiner from weight `(κ, e)` to weight
`(κ₀, e₀)` is a multiple (`SpansBranchingMaps`). For a linear form `t` and a vector `c` there is
`C` such that, for algebraic forms `ψ`, finite points `u` of rank one, every level `K` (an open
subgroup of `stdLevel`) and automorphic `Φ(x, g) = L_g(ρ₀(x) c)`, the integral of
`Φ(h) ψ_t(diag(h, u))` over `Γ \ G` is `C / [stdLevel : K]` times the class integral at level `K` of
`g ↦ L_g(A ψ(diag(g, u)))`. Here `ρ₀ = conjWeylRep κ₀ e₀`, `ψ_t = algFormCoeff 1 t ψ` and
`[stdLevel : K] = stdLevelIndex K`. 
