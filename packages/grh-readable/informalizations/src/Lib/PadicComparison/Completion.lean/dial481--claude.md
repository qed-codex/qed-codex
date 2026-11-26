---
{
  "module": "src/Lib/PadicComparison/Completion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/Completion.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/Completion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Derived completeness, adic approximation of comparisons and completed base change

This file shows that comparison maps of cohomology are bijective, by reduction modulo a scalar and
successive approximation. `New.Variety.H N F n` is `Extⁿ(N, F)` in the category `AbFunctor C` of
functors `C ⥤ Ab`. `New.Variety.moduleCoeff Φ` is a module-valued functor `Φ` (`act a` is
multiplication by `a` on it, `push N q n` is the map on `Hⁿ` induced by `q`, and `a • x` on `Hⁿ` is
`push N (act a) n x`), read as such a functor of coefficients.

## Main definitions and results

* `New.Variety.IsDerivedComplete`: derived π-completeness, the bijectivity of `New.shiftDiff π` on
  sequences. It passes to powers `ι → X`, to retracts up to a power of π, to cohomology
  (`New.Variety.IsDerivedComplete.cohomology`) and, in finite rank, to base change
  (`New.Variety.IsDerivedComplete.baseChange`).
* `New.Variety.Comparison.IsBijective.of_mod`: a comparison of complete cohomology groups that is
  bijective modulo `a` is bijective.
* `New.Variety.IsCompletionBijective`, `New.Variety.moduleCompletionIso`: linear maps that are
  bijective on p-adic completions, and the p-adic completion of an algebra, as a module.
* `New.Variety.HasFlatBaseChange.isBijective_of_isReductionMod`: `Hⁿ(N, S ⊗ Θ) → Hⁿ(N, X)` is
  bijective if `S ⊗ Θ → X` is so modulo p. The cohomology of `N` must commute with flat base change.
  `W` must be a discrete valuation ring with uniformiser p, and `S` must be flat over `W`. The lemma
  also needs completeness and no p-torsion of `W`, `S` and every value of `Θ` and `X`, and finite
  rank of `Hⁿ(N, Θ)` for each n where the kernel of the map on `Hⁿ` is p-divisible.

Notions from other files:
* `New.shiftDiff`: The operator (x_j) ↦ (x_j − π x_{j+1}) on sequences in a module.
* `New.Variety.Comparison.IsBijective`: For a functor φ: C' → C, a map β: F∘φ → F' and α: N' → N∘φ,
  the map Ext^n(N, F) → Ext^n(N', F') is bijective for every n.
* `New.Variety.IsReductionMod`: The map f is surjective, and f(x) = 0 exactly when x is a multiple
  m·y of m.
* `New.Variety.HasFlatBaseChange`: a functor N to abelian groups has it if M ⊗_S Hⁿ(N, Φ) → Hⁿ(N, M
  ⊗_S Φ) is bijective for all n, all functors Φ to S-modules and all S-flat M.
* `New.Variety.Comparison.restrict`: The cohomological comparison datum along a functor φ: C' → C
  from an abelian-group-valued functor N to N∘φ, with identity coefficient map.

## Relation to the literature

Known result: Derived completeness for a principal ideal, covering Nakayama, finiteness and
completed base change. Only modules and Ext groups are treated, and completeness is defined as
bijectivity of x_n - a x_(n+1) on sequences. Base change is proved for modules of finite rank over a
discrete valuation ring, with bounded torsion shown by hand. Source: Stacks Project 091N, 091P,
0G1U, 09BA, 0CQY; B. Bhatt, Torsion completions are bounded, JPAA (2019); L. Positselski,
Contraadjusted modules, contramodules, and reduced cotorsion modules, arXiv 1605.03934.


 ### Derived completeness 

### `IsDerivedComplete`

 `X` is derived π-complete: the map `(x j) ↦ (x j - π • x (j + 1))` on sequences in `X` is
bijective. 

### `IsDerivedComplete.of_isAdicComplete`

 A π-adically complete module is derived π-complete. 

### `IsDerivedComplete.exists_apply_eq_of_approx`

 Successive approximation. Let `f : E → X` be a linear map of derived π-complete modules and
`g : F → X` a family whose image lies in `f E + π • g F`. Then the image of `g` lies in `f E`. 

### `IsDerivedComplete.of_retract`

 A retract, up to a power of `π`, of a derived π-complete module is derived π-complete. 

### `partialSums`

 The partial sums `t 0 = 0`, `t (j + 1) = t j + π ^ j • y j (t j)` of a series whose `j`-th term
may depend on the partial sum before it. 

### `IsDerivedComplete.baseChange`

 Let `W` be a discrete valuation ring with uniformiser `π` and `S` a `W`-algebra. Assume that
`W`, `S` and the `W`-module `X` are derived π-complete and that `X` has finite rank. Then
`S ⊗[W] X` is derived π-complete. On `S`-modules `π` acts through its image in `S`. 

### `IsDerivedComplete.cohomology`

 If every value of `Φ` is derived `a`-complete, so is the cohomology `Hⁿ(N, Φ)`. 

 ### Reduction modulo a scalar and the adic step 

### `ModShortExact`

 The sequence `0 → Φ → Φ → G → 0` formed by multiplication by `a` and by `q` is short exact. 

### `modShortExact_of_isSMulRegular_of_isReductionMod`

 If every `Φ A` is `m`-torsion-free and `q` is a reduction modulo `m` at every `A`, then
`0 → Φ → Φ → F → 0` is short exact (after the universe lift of `Ab`), the first map being
multiplication by `m`. 

### `modShortExact_of_isReductionMod`

 `modShortExact_of_isSMulRegular_of_isReductionMod` with both conditions in one hypothesis. 

### `ModShortExact.exists_smul_eq_of_push_eq_zero`

 A class killed by reduction modulo a is a multiple of a. 

### `IsSMulDivisible`

 `M` is `c`-divisible: multiplication by `c` on `M` is surjective. 

### `IsDerivedComplete.eq_zero_of_mem_of_isSMulDivisible`

 A submodule `K` of a derived π-complete module on which multiplication by `π` is onto is
zero. 

### `Comparison.IsBijective.of_mod`

 The adic step. Let `α : N' ⟶ φ ⋙ N`, let `0 → Φ → Φ → G → 0` and `0 → Φ' → Φ' → G' → 0` be exact
with first maps multiplication by `a`, and let `β : φ ⋙ Φ ⟶ Φ'` induce `γ : φ ⋙ G ⟶ G'` on the
quotients (`β` followed by `q'` equals `q` followed by `γ`); with `α`, these induce comparison maps
`Hⁿ(N, Φ) → Hⁿ(N', Φ')` and `Hⁿ(N, G) → Hⁿ(N', G')`. Assume every `Hⁿ(N', Φ')` is derived
`a`-complete, and `Hⁿ(N, Φ)` is derived `a`-complete whenever the kernel of the degree-`n`
comparison map for `β` is `a`-divisible. If the comparison maps for `γ` are bijective in every
degree `n`, then so are those for `β`. 

 ### p-adic completion of algebras and modules 

### `IsCompleteTorsionFree.isDerivedComplete`

 A `p`-torsion-free, `p`-adically complete algebra (`IsCompleteTorsionFree B`, with fields
`complete` and `regular`) is derived `p`-complete. Here `p` is the prime fixed by `ThePrime p`. 

### `IsCompletionBijective`

 The linear map `j` induces a bijection of the `p`-adic completions. 

### `IsCompletionBijective.of_dvd_sub_of_pow_dvd`

 An algebra map that is onto modulo `p` and injective modulo every power of `p` is bijective
on the `p`-adic completions. 

### `exists_dvd_sub_algebraMap`

 Every element of the `p`-adic completion of `B` is congruent modulo `p` to the image of an
element of `B`. 

### `isCompletionBijective_completion`

 The map from `B` to its `p`-adic completion `PrincipalCompletion B p` is bijective on the
`p`-adic completions. 

### `IsCompletionBijective.linearMap_comp_bijective`

 If `j : X → E` is bijective on the `p`-adic completions, every linear map from `X` to a
`p`-adically complete module extends uniquely along `j`. 

### `IsReductionMod.comp_algebraMap`

 A reduction modulo `p` of the `p`-adic completion of `B` restricts to a reduction modulo `p`
of `B`. 

### `HasFlatBaseChange.isBijective_of_isReductionMod`

 Completed base change. Let `W` be a discrete valuation ring with uniformiser `p`, `S` a flat
`W`-algebra, `Θ` a functor to `W`-algebras and `X` a functor to `S`-algebras. Assume that `W`,
`S`, every `Θ A` and every `X A` are `p`-torsion-free and `p`-complete, and that the cohomology
of `N` commutes with flat base change. Let `j : S ⊗ Θ ⟶ X` be bijective modulo `p`, and let
`Hⁿ(N, Θ)` have finite rank over `W` whenever the kernel of `Hⁿ(j)` is `p`-divisible. Then
`Hⁿ(j) : Hⁿ(N, S ⊗ Θ) → Hⁿ(N, X)` is bijective for all `n`. 

### `algCompletion.of`

 The natural transformation from the identity functor on commutative S-algebras to the p-adic
completion functor, given by the canonical map from B to its completion. 

### `moduleCompletion`

 The functor sending an S-module to its p-adic completion. 

### `instance : (moduleCompletion S p).Additive`

 The `p`-adic completion functor on `S`-modules is additive. 

### `moduleCompletionIso`

 For commutative S-algebras B, the p-adic completion of the S-module B is naturally
isomorphic to the S-module underlying the p-adic completion of the algebra B. 

 ## Comparisons with identity coefficient map as restrictions 

### `New.Variety.Comparison.coeffCompBijective_id_iff_restrict`

 Let `θ : Ψ ⋙ G ≅ M` be an isomorphism of coefficient functors. The comparison maps
`Hⁿ(N, G∘Ψ) → Hⁿ(N', G∘Ψ∘φ)` along `α : N' ⟶ φ ⋙ N`, with identity map `𝟙 (φ ⋙ Ψ)` of coefficients
(the statement `CoeffCompBijective (𝟙 (φ ⋙ Ψ)) α G`), are bijective for all `n` if and only if
restriction along `φ` with coefficients `M`, `Hⁿ(N, M) → Hⁿ(N', M∘φ)`, is bijective for all `n`. 
