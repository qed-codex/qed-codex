---
{
  "module": "src/Lib/PadicComparison/Primitive/Periods.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/Primitive/Periods.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/Primitive/Periods.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The primitive comparison with period coefficients

The primitive comparison, passed from coefficients modulo `p` to period coefficients. For a `p`-adic
test `c` with ring `R`, let `L` be the ring of locally constant `𝔽_p`-valued functions on
`Spec R[1/p]` (for a test ring `A`, the same ring on `Spec A`; a `p`-adic test gives `A = R[1/p]`).
`New.Variety.primitiveMap` is the natural map of `O♭`-algebras from `O♭ ⊗ L` to the tilt `R♭`; on
`1 ⊗ L` it restricts to `locConstToTilt : L → R♭`, `ℓ ↦ primitiveMap (1 ⊗ ℓ)`. Let `S` be an
`A_inf`-algebra and `K` an `S`-algebra, and let `Ψ` be isomorphic (by `θ`) to the period
coefficients `c ↦ K ⊗ (S ⊗ W(R♭))^`, where `^` is `p`-adic completion.

* `New.Variety.primitivePeriodMap`: the natural map `K ⊗ W(L) → Ψ` induced by
  `New.Variety.primitiveMap`.
* `New.Variety.primitivePeriodMap_isBijective`: this map is bijective on cohomology under several
  conditions. `S` and `K` form a period ring pair, and `K` is flat over `S`. `N` and `N'` have flat
  base change. The cohomology of `N` with coefficients `ℤ_p` is finite over `ℤ_[p]`. The map that
  `New.Variety.primitiveMap` induces on the coefficients `b ↦ b ⊗ (O♭ ⊗ S) ⊗ 𝔪` is bijective on
  cohomology.
* `New.Variety.exists_primitive_period_comparison`: the same, in existential form.

Notions from other files:
* `New.Variety.CoeffCompBijective β α F`: the comparison of cohomology groups along `β` and `α` is
  bijective in every degree for the coefficients `F`.
* `New.Variety.HasFlatBaseChange N`: the cohomology of `N` commutes with flat extension of the
  coefficients.
* `New.Variety.IsPeriodRingPair`: `S` is `p`-torsion-free and `p`-complete, `p` divides the image of
  `ξ` in `S`, and `τ` is a unit in `K`.
* `New.Variety.almostCoeff`: for an `O♭`-module `N`, the functor `b ↦ b ⊗ N ⊗ 𝔪` on `O♭`-algebras,
  `𝔪` the maximal ideal of `O♭`.
* `New.Variety.oFlatLocConst`: the functor from test rings to `O♭`-algebras sending `A` to
  `O♭ ⊗_{𝔽_p} LC(A)`, `LC(A)` the locally constant functions `Spec A → 𝔽_p`.
* `New.Variety.ellAdicCoeff`: the coefficient `ℤ_ℓ` (here `ℓ = p`): a test ring `A` goes to the Witt
  vectors of the ring of locally constant functions `Spec A → 𝔽_ℓ`.

## Relation to the literature

Known; see `Lib.PadicComparison.HodgeTate.PeriodMap` for sources.


### `noncomputable local instance : Algebra ℤ_[p] b`

 An `𝔽_p`-algebra `b` is a `ℤ_[p]`-algebra through reduction modulo `p`. 

### `IsReductionMod.comp_of_exact_of_comp`

 Let `q` and `π` be additive maps on `X` with kernel the multiples of `m`, and `q` onto. If
`π ∘ j` is a reduction modulo `m` (onto, with kernel the multiples of `m`), then so is `q ∘ j`. 

### `wittLocConst`

 The functor from test rings to `ℤ_[p]`-algebras sending `A` to `W(L)`, where `L` is the ring
of locally constant functions `Spec A → 𝔽_p`. 

### `wittIncludeRight`

 For a test ring `A`, with `L` the ring of locally constant functions `Spec A → 𝔽_p`, the
`ℤ_[p]`-algebra map `W(L) → W(O♭ ⊗ L) → S ⊗_{A_inf} W(O♭ ⊗ L)`, `w ↦ 1 ⊗ W(1 ⊗ –)(w)`. 

### `wittLocConstBaseChange`

 The `S`-algebra map `S ⊗_{ℤ_p} W(L) → S ⊗_{A_inf} W(O♭ ⊗ L)`, natural in the test ring: the
extension of `wittIncludeRight` to `S`-algebras, its transpose under base change to `S`. 

### `wittLocConstToPeriodAlg`

 The map `S ⊗_{ℤ_p} W(L) → (S ⊗_{A_inf} W(O♭ ⊗ L))^` of `S`-modules, where `^` is the `p`-adic
completion: `wittLocConstBaseChange` followed by the map to the completion. 

### `wittLocConstCancelIso`

 The isomorphism `K ⊗_{ℤ_p} W(L) ≅ K ⊗_S (S ⊗_{ℤ_p} W(L))`, natural in the test ring. 

### `wittToPeriodAlg`

 The image `1 ⊗ w` of a Witt vector `w ∈ W(B)` in the `p`-adic completion of `S ⊗ W(B)`. 

### `primitivePeriodMap`

 Let `θ` be an isomorphism from the functor `c ↦ K ⊗ (S ⊗ W(R♭))^` to `Ψ`, where `R` is the ring
of the test `c` and `^` is the `p`-adic completion. This is the natural map from `K ⊗ W(L)` to `Ψ`,
where `L` is the ring of locally constant `𝔽_p`-valued functions on `Spec R[1/p]`. It is the
composite `K ⊗ W(L) ≅ K ⊗ (S ⊗ W(L)) → K ⊗ (S ⊗ W(O♭ ⊗ L))^ → K ⊗ (S ⊗ W(R♭))^ ≅ Ψ c`, the
third map induced by `primitiveMap`. 

### `primitivePeriodMap_app_tmul`

 `primitivePeriodMap K θ` sends `a ⊗ x` to `θ (a ⊗ 1 ⊗ x')`, where `x'` is the image of `x`
under the map of Witt vectors induced by `locConstToTilt`, and `1 ⊗ x'` is taken in the completion
(`wittToPeriodAlg`). 

### `isPerfectTorsionFree_oFlatLocConst`

 For every test ring `A`, the `O♭`-algebra `O♭ ⊗_{𝔽_p} LC(A)` is perfect, and `pFlat` (the class
of `ξ` modulo `p`) is a non-zero-divisor on it. 

### `IsReductionMod.comp_wittLocConstBaseChange`

 Let `S` be an `A_inf`-algebra, `A` a test ring and `L` the ring of locally constant functions
`Spec A → 𝔽_p`. The map `S ⊗ W(L) → S ⊗ W(O♭ ⊗ L)` (`wittLocConstBaseChange`) is bijective
modulo `p`: followed by a reduction `q` modulo `p` of the target (`IsReductionMod p q`: `q` onto,
with kernel the multiples of `p`), it is a reduction modulo `p` of the source. 

### `primitivePeriodMap_isBijective`

 The primitive comparison with period coefficients. Let `p` be a prime, `(S, K)` a period ring
pair (`S` an `A_inf`-algebra, `K` a flat `S`-algebra), `θ` an isomorphism from
`c ↦ K ⊗ (S ⊗ W(R♭))^` to `Ψ : PadicTest ⥤ ModuleCat K`, and `α : N' ⟶ genericTest ⋙ N` the map that
compares cohomology over `p`-adic tests with cohomology over test rings. Suppose that `N` and `N'`
have flat base change, that each `H N ellAdicCoeff n` (the `n`-th cohomology of `N` with
coefficients `ℤ_p`) is finite over `ℤ_[p]`, and that `primitiveMap` is bijective on cohomology along
`α` for the coefficients `almostCoeff (O♭ ⊗ S)` (`CoeffCompBijective`). Then
`primitivePeriodMap K θ`, viewed by `ofModuleHom genericTest` as a map of coefficients, is bijective
on cohomology along `α`, in every degree. 

### `exists_primitive_period_comparison`

 The primitive comparison in existential form. For a period ring pair `(S, K)` and an isomorphism
`θ` from `c ↦ K ⊗ (S ⊗ W(R♭))^` to `Ψ : PadicTest ⥤ ModuleCat K` (`R` the ring of the test `c`),
there is a natural map `γ : K ⊗ W(L) → Ψ` (`L`: locally constant `Spec R[1/p] → 𝔽_p`) with
`γ (a ⊗ x) = θ (a ⊗ (1 ⊗ x'))`, `x'` the image of `x` under the Witt vector map of `locConstToTilt`;
`γ` is bijective on cohomology under the conditions of `primitivePeriodMap_isBijective`. 
