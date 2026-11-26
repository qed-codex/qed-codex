---
{
  "module": "src/Lib/General/Algebra/CohomologyBaseChange.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/CohomologyBaseChange.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/CohomologyBaseChange.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Flat base change in functor cohomology, and the base change adjunction for algebras

Cohomology here is H^n(N, Φ) = Ext^n(N, Φ) in the category of functors from C to abelian groups,
where Φ is a functor to S-modules. For a module M over an S-algebra T, the base change map
`New.Variety.baseChangeMap` goes from M ⊗_S H^n(N, Φ) to H^n(N, M ⊗_S Φ).
`New.Variety.HasFlatBaseChange N` says that this map is bijective for all S, T, Φ, n and all M flat
over S. The file proves bijectivity for N = ℤ[h_A], with h_A the functor represented by A, by the
Yoneda lemma, shows that for flat M the maps admit dévissage in N, and transfers bijectivity along
bijective comparisons. It also shows that base change of algebras is left adjoint to restriction of
scalars, and that ring maps send powers of p to powers of p.

## Main definitions and results

* `New.Variety.HasBaseChange.baseChangeMap_bijective_freeAb_reprBy`: the base change map is
  bijective for N = ℤ[h_A], by the Yoneda lemma.
* `New.Variety.HasBaseChange.devissage`: for M flat it admits dévissage, being compatible with the
  long exact sequences of short exact sequences.
* `New.Variety.Comparison.IsBijective.baseChangeMap_bijective_iff`: along a bijective comparison
  from an N with flat base change, base change by a flat M on the target holds exactly when the
  comparison stays bijective after tensoring the coefficients with M.
* `New.Variety.algBaseChangeAdj`: for a k-algebra S, the functor A ↦ S ⊗_k A
  (`New.Variety.algBaseChange`) is left adjoint to restriction of scalars
  (`New.Variety.restrictAlg`).
* `New.Variety.pointMap_algBaseChange_unit_bijective`: the base change S ⊗_k B represents Hom(B, -)
  on S-algebras.

Notions from other files:
* `New.Variety.moduleCoeff`: A functor F from C to k-modules, regarded as a functor to abelian
  groups, so that it can serve as the coefficients of cohomology.
* `New.Variety.freeAb`: The functor sending a set-valued functor Y to Z[Y], whose value at A is the
  free abelian group on Y(A).
* `New.Variety.tensorWith`: For a module M over the S-algebra T, the functor X ↦ M ⊗_S X from
  S-modules to T-modules.

## Relation to the literature

The arguments are the usual ones: the Yoneda lemma, exactness of tensoring with a flat module, and
the tensor-hom adjunction.


 ## Flat base change in functor cohomology: representable case and dévissage 

### `baseChangeMap_tmul`

 The base change map sends m ⊗ x to the image of the class x under the map of coefficients
y ↦ m ⊗ y. 

### `Comparison.pullₗ`

 For β: Φ∘φ → Φ' of functors to S-modules and α: N' → N∘φ, the comparison map H^n(N, Φ) → H^n(N',
Φ') (the map `pull α` of the comparison `ofModuleHom φ β` built from β), as an S-linear map. 

### `Comparison.pullₗ_apply`

 The linear comparison map `pullₗ` has the same values as the additive one. 

### `tensorWith.whiskerLeft_mk_comp_coeffHom`

 For β: Φ∘φ → Φ' and m ∈ M, the maps of coefficients y ↦ m ⊗ y (`tensorWith.mk T m`) commute with
β and M ⊗_S β, regarded as maps of coefficients in abelian groups (`coeffHom` of `ofModuleHom`):
both composites send y to m ⊗ β y. 

### `baseChangeMap_pull`

 Let β: Φ∘φ → Φ' be a map of functors to S-modules and α: N' → N∘φ. The base change maps
M ⊗_S H^n(N, Φ) → H^n(N, M ⊗_S Φ), and likewise for N' and Φ', commute with the comparison maps
`pullₗ` induced by (β, α) and by (M ⊗_S β, α). Here `tensorWith T M` is the functor M ⊗_S –, and
`moduleCoeff Φ` is Φ regarded as a functor to abelian groups. 

### `push_homReprEquiv_symm`

 The Yoneda isomorphism `homReprEquiv`: Hom(ℤ[h_A], K) ≅ K(A), h_A the functor represented by A,
is natural in K: for a map γ: K → N of functors to abelian groups and x ∈ K(A), pushing along γ the
class of degree 0 that corresponds to x gives the class that corresponds to γ_A(x). Here `mk₀`
sends a morphism to its class in Ext^0. 

### `HasBaseChange.yonedaEquiv₀`

 The Yoneda isomorphism Φ(A) ≅ H^0(ℤ[h_A], Φ), as an S-linear map. 

### `HasBaseChange.yonedaEquiv₀_apply`

 `yonedaEquiv₀` sends x to the class of the map ℤ[h_A] → Φ that corresponds to x. 

### `HasBaseChange.baseChangeMap_bijective_freeAb_reprBy`

 For every object A, the map M ⊗_S H^n(ℤ[h_A], Φ) → H^n(ℤ[h_A], M ⊗_S Φ) is bijective in
every degree n (`AllBijective`), h_A the functor represented by A; no flatness of M is assumed. 

### `hasFlatBaseChange_freeAb_reprBy`

 The functor ℤ[h_A] has flat base change, h_A being the functor represented by A: the map
M ⊗_S H^n(ℤ[h_A], Φ) → H^n(ℤ[h_A], M ⊗_S Φ) is bijective for all n, all Φ and all flat M. 

### `HasBaseChange.precompₗ`

 Composition with a class e in Ext^a(N', N), as an S-linear map from H^n(N, Φ) to
H^(a+n)(N', Φ). 

### `HasBaseChange.baseChangeMap_lTensor_precompₗ`

 The base change map M ⊗_S H^n(N, Φ) → H^n(N, M ⊗_S Φ) turns M ⊗ (composition with a class e,
`precompₗ`) into composition with e. 

### `HasBaseChange.tensoredSeq`

 For M flat, the long exact sequence of Ext(–, Φ) of a short exact sequence X, tensored
with M. 

### `HasBaseChange.devissage`

 For M flat over S, with M a module over the S-algebra T, the maps M ⊗_S H^n(N, Φ) → H^n(N,
M ⊗ Φ) admit dévissage in N (`New.Variety.Devissage`): the four and five lemmas apply to them along
short exact sequences, and they are bijective for N = 0. 

### `IsAcyclicAt`

 `IsAcyclicAt φ F B` says that restriction along φ (the comparison `Comparison.restrict φ F`,
taken with α = `freeAbMap` of the identity of h_B∘φ) from H^n(ℤ[h_B], F) to H^n(ℤ[Hom(B, φ –)], F∘φ)
is bijective for all n; so the latter is F(B) in degree 0 and zero in positive degree. 

### `CoeffCompBijective`

 For β: Ψ∘φ → Ψ', α: N' → N∘φ and a functor F to S-modules, the statement that the comparison map
(built from F∘β and α, as in `pullₗ`; `IsBijective` of `ofModuleHom`) H^n(N, F∘Ψ) → H^n(N', F∘Ψ') is
bijective for all n. 

### `Comparison.IsBijective.baseChangeMap_bijective_iff`

 Suppose β and α induce bijections H^n(N, Φ) → H^n(N', Φ'), M is flat over S and N has flat
base change (its base change maps are bijective for every flat tensor factor). Then
M ⊗ H^n(N', Φ') → H^n(N', M ⊗ Φ') is bijective for all n if and only if the comparison map
H^n(N, M ⊗ Φ) → H^n(N', M ⊗ Φ') is, which is what `CoeffCompBijective` says. 

 ## Base change of algebras as left adjoint to restriction of scalars 

### `algBaseChangeAdj`

 Base change from commutative k-algebras to commutative S-algebras is left adjoint to
restriction of scalars. 

### `baseChangeTranspose`

 For functors X to k-algebras and Y to S-algebras, the bijection between natural S-algebra maps
S ⊗_k X → Y and natural k-algebra maps X → Y. Its inverse sends β to the map s ⊗ a ↦ s • β a. 

### `pointMap_algBaseChange_unit_bijective`

 For a k-algebra B and an S-algebra A, composing with the unit B → S ⊗ B is a bijection from the
S-algebra maps S ⊗ B → A to the k-algebra maps B → A. Here `pointMap` is the Yoneda map given by
the unit, from Hom(S ⊗ B, –) to Hom(B, –) restricted to S-algebras. 


## Ring maps and powers of p

A ring map `f : A → B` sends powers of p to powers of p; this is the condition under which it
induces a map of localisations `A[1/p] → B[1/p]`.


### `New.Variety.powers_le_comap_powers`

 Every ring map f : A → B maps the powers of a natural number p in A into the powers of p
in B. 
