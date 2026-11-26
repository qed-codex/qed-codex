---
{
  "module": "src/Lib/Cohomology/Etale/EllAdicCohomology.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Etale/EllAdicCohomology.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/Etale/EllAdicCohomology.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# ℓ-adic cohomology with its Galois action; finiteness and bijectivity from coefficients mod ℓ

`ℓ`-adic cohomology is defined as `Ext` on test rings, with coefficients in the Witt vectors of the
locally constant `𝔽_ℓ`-valued functions on the spectrum.

* `New.Variety.ellAdicCoeff`: the coefficient `ℤ_ℓ`; `New.Variety.ellAdicPull`: pull-back on
  cohomology, over `ℚ_ℓ`.
* `New.Variety.ellAdicCohom`, `New.Variety.ellAdicCohom.galoisAction`: cohomology of the base change
  to `Ω`, and the action of `Γ`.
* `New.Variety.exists_ellAdicCoeff_modShortExact_pow`,
  `New.Variety.exists_ellAdicCoeff_modShortExact`: reduction modulo `ℓ ^ k` and `ℓ`; completeness.
* `New.Variety.finite_H_ellAdicCoeff`, `New.Variety.IsCohomEquiv.bijective_ellAdicPull`: finiteness
  and bijectivity lift from `𝔽_ℓ`.

Notions from other files:
* `New.Variety.ModShortExact`: `ModShortExact a q` says that `0 → Φ → Φ → G → 0`, formed by
  multiplication by `a` and by `q`, is short exact.
* `New.Variety.TestRing`: The category of test rings (`New.Variety.IsTest`), as a full subcategory
  of commutative rings; `New.Variety.testIncl` is its inclusion functor.

## Relation to the literature

Known; see `Lib.Cohomology.Etale.FilteredLimits`, `Lib.PadicComparison.Completion` and
`Lib.PadicComparison.Primitive.ComparisonTheorem` for sources.


 ### Definitions 

### `ellAdicCoeff`

 The coefficient `ℤ_ℓ`: a test ring `A` goes to the Witt vectors of the ring of locally constant
functions `Spec A → 𝔽_ℓ`. 

### `ellAdicPull`

 Pull-back along `α : M ⟶ N` on `ℚ_ℓ ⊗ Ext^n(-, ℤ_ℓ)`, as an additive function of `α`. 

### `ellAdicPull.comp`

 Pulling back along `β` and then along `α` is pulling back along `α ≫ β`. 

### `geomPoints`

 The functor of points (a functor from commutative rings to types, `PointFunctor`) of the base
change `X ×_R Ω` of a scheme `X` over `R`. 

### `ellAdicCohom`

 Geometric `ℓ`-adic cohomology in degree `n`: `X ↦ ℚ_ℓ ⊗ H^n(X ×_R Ω, ℤ_ℓ)`. 

### `ellAdicCohom.galoisAction`

 The action on `H^n(X ×_R Ω)` of a group `Γ` acting on `Ω` by `R`-algebra automorphisms. 

### `ellAdicCohom.map_galoisAction`

 Pull-back along a map `f : X ⟶ Y` of `R`-schemes commutes with the action of `Γ`. 

 ### Comparison with finite coefficients 

### `exists_ellAdicCoeff_modShortExact_pow`

 There is an exact sequence `0 → ℤ_ℓ → ℤ_ℓ → W_k(𝔽_ℓ) → 0` of coefficients whose first map is
`ℓ ^ k`, where the third term is the locally constant functions with values in `W_k(𝔽_ℓ)`, the
Witt vectors of length `k`. 

### `exists_ellAdicCoeff_modShortExact`

 Two facts on the coefficient `ℤ_ℓ`: (a) there is a map `q` to `𝔽_ℓ` with
`0 → ℤ_ℓ → ℤ_ℓ → 𝔽_ℓ → 0` exact, the first map being `ℓ`; (b) every `Ext^n(N, ℤ_ℓ)` is derived
`ℓ`-complete (`IsDerivedComplete`; `ℓ`-adic completeness implies it, and it allows solving by
successive approximation) (this does not involve `q`). 

### `finite_H_ellAdicCoeff`

 If `Ext^n(N, 𝔽_ℓ)` is finite, then `Ext^n(N, ℤ_ℓ)` is a finitely generated `ℤ_ℓ`-module. 

### `IsCohomEquiv.bijective_ellAdicPull`

 An equivalence for `𝔽_ℓ`-coefficients induces bijections on `ℓ`-adic cohomology. 
