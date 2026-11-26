---
{
  "module": "src/Lib/PadicHodge/Crystalline/HodgeTateForms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Crystalline/HodgeTateForms.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Crystalline/HodgeTateForms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Semilinear forms of given weight: independence, finiteness, and jumps read off a basis

`New.Period.hodgeTateMaps ρ γ u` is the `PadicAlgCl p`-space of `γ`-semilinear maps `f : T → ℂ_[p]`
with `f (ρ g x) = χ(g) ^ (-u) • toGp g • f x` for `g` near `1`. Here `toGp` is the map to `Gp p`
given by the instance `[OverGp Γ p]`, and the instance `[ThePrime p]` fixes `p` as a prime. For
`toGp` of open image and `T` finite over `R`:
* `New.Period.hodgeTateMaps.mem_span_same_weight`: a map of weight `u` in the `ℂ_[p]`-span of maps
  `f i` of weights `k i` lies in the `PadicAlgCl p`-span of those with `k i = u`;
* `New.Period.finite_hodgeTateMaps`: each space has finite dimension;
* `New.Period.hasJumps_of_basis`: the weights of a `ℂ_[p]`-basis of such maps are the jumps
  (`New.Period.HasJumps`).

The input is that an element of `ℂ_[p]` fixed near `1` is algebraic, and is zero if it is fixed
after twisting by a nonzero power of `χ`.

Notions from other files:
* `New.Period.nearOne`: The filter 'near 1' on Γ: the pull-back along `toGp : Γ → G_p` of the filter
  of neighbourhoods of the identity.
* `New.cyclotomicGp`: The p-adic cyclotomic character χ of G_p = Gal(Q̄_p over Q_p) (`New.Gp`); for
  `g : Γ`, `χ g` means χ applied to `toGp g`.
* `New.Period.jump`, `New.Period.HasJumps`: the multiplicity of the jump u is the dimension over
  `PadicAlgCl p` of `hodgeTateMaps ρ γ u`; a multiset J of integers gives the jumps if each u occurs
  in J with that multiplicity.

## Relation to the literature

Known; see `Lib.PadicHodge.Crystalline.Regularity` for sources.


### `evalOnBasis`

 For an R-basis b of T indexed by ι, the C_p-linear isomorphism from γ-semilinear maps f: T →
C_p to C_p^ι sending f to its values f(b_i). 

### `instance : Algebra.IsAlgebraic ℤ_[p] (PadicAlgCl p)`

 The algebraic closure `PadicAlgCl p` of `ℚ_p` is algebraic over `ℤ_[p]`. 

### `exists_algHom_lift`

 If R is algebraic over Z_p, every Z_p-algebra homomorphism γ: R → C_p factors through a
Z_p-algebra homomorphism δ: R → Q̄_p. 

### `mem_hodgeTateMaps_of_span`

 Let R be algebraic over Z_p and let the s_i, for i in an index type ι, span T over R. If a
γ-semilinear f: T → C_p satisfies f(g s_i) = χ(g)^(−u)·g f(s_i) for g near 1, for each i, then f
lies in `New.Period.hodgeTateMaps` for u. 

### `instance : Module.Finite ℂ_[p] (T →ₛₗ[toRingHom γ] ℂ_[p])`

 If `T` is finite over `R`, the `γ`-semilinear maps `T → ℂ_[p]` form a finite-dimensional
`ℂ_[p]`-space. 

### `hodgeTateMaps.mem_span_same_weight`

 Let `toGp` have open image (as the instance `OverGp Γ p` gives) and T be finite over R. Here
`hodgeTateMaps ρ γ k` is the Q̄_p-space of γ-semilinear maps f : T → ℂ_p with f(ρ g x) = χ(g)^(−k) •
toGp(g) • f(x) for g near 1, where χ is the cyclotomic character. If f_i lies in
`New.Period.hodgeTateMaps` for k_i, and φ in `New.Period.hodgeTateMaps` for u lies in the ℂ_p-span
of the f_i, then φ lies in the ℚ̄_p-span of the f_i with k_i = u. 

### `finite_hodgeTateMaps`

 If `toGp` has open image (as the instance `OverGp Γ p` gives) and T is finite over R, the
ℚ̄_p-space `New.Period.hodgeTateMaps` for γ and u is finite-dimensional, for every integer u. 

### `hasJumps_of_basis`

 Let `toGp` have open image (as the instance `OverGp Γ p` gives) and T be finite over R. If
a ℂ_p-basis b of the γ-semilinear maps has each `b i` in `New.Period.hodgeTateMaps` for `u i`, then
the `u i` are the jumps (`New.Period.HasJumps`). 
