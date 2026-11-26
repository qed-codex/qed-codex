---
{
  "module": "src/Lib/PadicComparison/Descent/TestCategory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/Descent/TestCategory.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/Descent/TestCategory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Divided power ideal, p-adic test rings, tilt, Witt vectors and reduction modulo p

This file sets up basic objects of the p-adic and crystalline comparison, for a prime p.
O_C = `New.OC` is the ring of integers of ℂ_p, O♭ = `New.Period.OFlat` is its tilt, and
ξ = `New.Period.xi` generates ker θ in A_inf = W(O♭). The prime p is implicit in `New.Period.OFlat`
and `New.Period.xi`. The file defines the ideal 𝔡(S) of the x with n! ∣ x^n for all n, and
categories of p-complete p-torsion-free test rings. Finally, it collects the commutative algebra of
flatness, reduction modulo an element and Witt vectors that is used throughout the p-adic
comparison.

## Main definitions and results

* `New.Variety.pdIdeal`: the ideal 𝔡(S) of the x with n! ∣ x^n for all n.
  `New.Variety.pdIdeal_le_comap`: ring maps send 𝔡(B) into 𝔡(k).
* `New.Variety.IsCompleteTorsionFree` and `New.Variety.CrysTest`: p-torsion-free p-complete rings,
  and the category of such S-algebras. `New.Variety.CrysTest.restrictScalars` restricts scalars.
* `New.Variety.baseChangeMap`, `New.Variety.HasFlatBaseChange`: the map M ⊗ H^n(N, Φ) → H^n(N,
  M ⊗ Φ), and the statement that it is bijective for flat M.
* `New.Variety.IsCell`, `New.Variety.PadicTest`: cells, and p-adic tests, which are non-empty
  products S of cells with a map from O_C = `New.OC`.
* `New.Variety.PadicTest.tilt`, `New.Variety.algCompletion`, `New.Variety.wittFunctor`,
  `New.Variety.periodAlg`: tilt, p-adic completion, Witt vectors, and the completion of T ⊗ W(b)
  over A_inf.

Notions from other files:
* `New.Variety.Comparison`: A comparison from F on C to F' on C': a functor φ: C' → C with a natural
  transformation β: F∘φ → F'.

## Relation to the literature

Known; see `Lib.PadicComparison.Crystalline.ComparisonMap`, `Lib.PadicComparison.Completion`,
`Lib.PadicComparison.Descent.AlmostDescent` and `Lib.PadicComparison.HodgeTate.PeriodMap` for
sources.



## The divided power ideal and p-complete p-torsion-free test rings

No divided power structure is chosen.


### `pdIdeal`

 The ideal 𝔡(S) of the elements x of S such that n! divides x^n for every n. 

### `pdIdeal_le_comap`

 A ring map `f : B → k` sends the ideal `pdIdeal B` of the `x` with `n! ∣ x ^ n` for all `n`
into `pdIdeal k`. 

### `pdQuotientMk`

 The quotient map S → S/𝔡(S), where 𝔡(S) = `New.Variety.pdIdeal` S is the ideal of the x with n!
dividing x^n for all n. 

### `pdQuotientMap`

 For a ring homomorphism f: B → k, the induced homomorphism B/𝔡(B) → k/𝔡(k), where 𝔡 is the ideal
`New.Variety.pdIdeal`. 

### `IsCompleteTorsionFree`

 The ring S is p-torsion-free and p-adically complete. 

### `IsCompleteTorsionFree.regular`

 `S` is `p`-torsion-free: multiplication by `p` is injective. 

### `IsCompleteTorsionFree.complete`

 `S` is `p`-adically complete. 

### `CrysTest`

 The full subcategory of commutative S-algebras that are p-torsion-free and p-adically
complete. 

### `pdReduction`

 For a ring map r: k → B/𝔡(B), the functor A ↦ A/𝔡(A) from p-torsion-free p-complete B-algebras
to k-algebras, with 𝔡 the ideal `New.Variety.pdIdeal`. 

### `CrysTest.restrictScalars`

 Restriction of scalars along S → B, from p-torsion-free p-complete B-algebras to p-torsion-free
p-complete S-algebras. 

### `isCompleteTorsionFree_completion`

 If `p` is a non-zero-divisor on `B`, the `p`-adic completion `PrincipalCompletion B p` is
`p`-torsion-free and `p`-adically complete. 


## The test category and coefficient functors

The test category and the coefficient functors of the p-adic comparison theorems. Cohomology
`New.Variety.H` N F n is an Ext group of functors C → Ab, and `New.Variety.moduleCoeff` makes a
functor to modules into coefficients.


 ### Tensor products of coefficients 

### `asModules`

 For a functor Φ to commutative S-algebras, the functor of underlying S-modules. 

### `tensorWith`

 For a module M over the S-algebra T, the functor X ↦ M ⊗_S X from S-modules to T-modules. 

### `tensorWith.mk`

 For m in M and a functor Φ to S-modules, the natural map of abelian-group-valued coefficient
functors Φ → M ⊗_S Φ sending x to m ⊗ x. 

### `tensorWith.mk_add`

 The map `x ↦ m ⊗ x` is additive in `m`. 

### `tensorWith.mk_smul`

 Scalars from `S` pass through the tensor sign, where `End.asHom (CoeffAction.act s)` is
multiplication by `s` on the coefficient functor `moduleCoeff Φ`: `(s • m) ⊗ x = m ⊗ (s • x)`. 

### `baseChangeMap`

 The canonical T-linear map M ⊗_S H^n(N, Φ) → H^n(N, M ⊗_S Φ), sending m ⊗ z to the image of
z under x ↦ m ⊗ x. 

### `HasFlatBaseChange`

 The abelian-group-valued functor N : `New.Variety.AbFunctor` C on C has flat base change: M ⊗_S
H^n(N, Φ) → H^n(N, M ⊗_S Φ) is bijective for all n, all functors Φ to S-modules and all S-flat M. 

### `coeffMap`

 For a natural map β: Φ → Ψ of functors to S-modules, the induced map of abelian-group-valued
coefficient functors. 

### `Comparison.ofModuleHom`

 The cohomological comparison datum along a functor φ: C' → C whose coefficient map comes
from a natural transformation Φ∘φ → Φ' of module-valued functors. 

### `Comparison.restrict`

 The cohomological comparison datum along a functor φ: C' → C from an abelian-group-valued
functor N to N∘φ, with identity coefficient map. 

### `algBaseChange`

 Base change along S → T: the functor B ↦ T ⊗_S B from commutative S-algebras to commutative
T-algebras. 

### `not_isUnit_p`

 In a nontrivial ring that is `p`-adically complete, `p` is not a unit. 

 ### Cells and p-adic tests 

### `IsCell`

 A cell: a p-adically complete, absolutely integrally closed valuation ring T (a domain) in which
p is not zero. By `New.Variety.not_isUnit_p`, p is then not a unit in T. 

### `IsCell.p_ne_zero`

 `p` is not zero in `T`. 

### `PadicTest`

 A p-adic test: a non-empty family of cells (`New.Variety.IsCell`) with a ring map from O_C to
their product. 

### `PadicTest.Index`

 The index set of the product. 

### `PadicTest.Cell`

 The factors of the product, as types. 

### `PadicTest.nonempty`

 There is at least one factor. 

### `PadicTest.commRing`

 The ring structure of each factor. 

### `PadicTest.isCell`

 Each factor is a cell. 

### `PadicTest.structureMap`

 The structure map from O_C to the product of the factors. 

### `ProdRing`

 The ring S underlying a p-adic test, namely the product of its family of valuation rings. 

### `isAdicComplete_prodRing`

 The ring S of a p-adic test is p-adically complete, since each of its factors is. 

### `TiltRing`

 The tilt S^♭ of the ring S of a p-adic test, the inverse limit of S/p along Frobenius. 

### `twist`

 For g in the Galois group `New.Gp` p, which acts on O_C by ring automorphisms, the endofunctor
of p-adic tests that keeps the ring S and precomposes its structure map O_C → S with the action of
g. 

### `algFunctor`

 The functor from p-adic tests to commutative O_C-algebras sending a test to its product ring
S with its structure map. 

### `ringFunctor`

 The functor from p-adic tests to commutative rings sending a test to its underlying product
ring S. 

### `tilt`

 The functor from p-adic tests to commutative O^♭-algebras sending a test S to its tilt S^♭. 

 ### Completion, Witt vectors and functors of points 

### `algCompletion`

 The functor sending a commutative S-algebra to its p-adic completion. 

### `wittFunctor`

 For a ring S with a map to W(k), by default S = W(k), the functor sending a k-algebra b to
its p-typical Witt vectors W(b), as an S-algebra. 

### `periodAlg`

 For an A_inf-algebra T, the functor sending an O^♭-algebra b to the p-adic completion of T
⊗_{A_inf} W(b). 

### `testPoints`

 For R → O_C, the functor sending an R-scheme X to the functor S ↦ X(S) of its points over R
in p-adic tests. 

### `exists_compatible_roots`

 If S is absolutely integrally closed, then for every unit x of S there is a homomorphism χ from
ℚ to Sˣ with χ(1) = x, that is, a compatible system of roots of x. 


## Flatness, reduction modulo an element and Witt vectors

* `New.Variety.pFlat`: the nonzero nonunit p♭ = ξ mod p of O♭. `New.Variety.IsPerfectTorsionFree` is
  the class of perfect, p♭-torsion-free O♭-algebras.


 ### Locally constant functions on the prime spectrum 

### `exists_ringHom_of_locallyConstant`

 For an M-algebra S there is a ring map f from the locally constant functions Spec S → M to S
such that, for every prime q, f(x) and x(q) have the same image in the localisation S_q. 

### `comapAddMonoidHom_surjective_of_isComparableRing`

 Let f : S → S' be a ring map such that any two elements of S' become comparable for divisibility
after the partition given by f(e), for an idempotent e of S (`New.Variety.IsComparableRing`). Then
pull-back of locally constant Λ-valued functions from Spec S to Spec S' is onto. 

### `locConstAlg`

 The functor sending a commutative ring S to the ℤ/p-algebra of locally constant functions Spec
S → ℤ/p. 

### `perfectRing_locConstAlg`

 For every commutative ring A, the algebra of locally constant functions Spec A → ℤ/p
(`New.Variety.locConstAlg`) is perfect. 

 ### The element p♭ 

### `pFlat`

 The element p♭ = ξ mod p of O^♭ = A_inf/p, the zeroth Witt coefficient of ξ. 

### `IsPerfectTorsionFree`

 The O^♭-algebra b is perfect and p♭-torsion-free, where p♭ = ξ mod p (`New.Variety.pFlat`). 

 ### Reduction modulo an integer, flatness and torsion 

### `IsReductionMod`

 The map f: A → B is surjective, and f(x) = 0 exactly when x = m·y for some y. 

### `IsReductionMod.surjective`

 A reduction map modulo `m` (`New.Variety.IsReductionMod`) is onto. 

### `IsReductionMod.exact`

 For a reduction map `g` modulo `m` (`New.Variety.IsReductionMod`), `g x = 0` exactly when
`x = m • y` for some `y`. 

### `isReductionMod_constantCoeff`

 For a perfect algebra `S` over a domain `M` of characteristic `p`, the zeroth Witt coefficient
`W(S) → S` is reduction modulo `p` (`New.Variety.IsReductionMod`). 

### `isCompleteTorsionFree_wittVector`

 For a perfect algebra `S` over a domain `M` of characteristic `p`, the Witt vectors `W(S)` have
no `p`-torsion and are `p`-adically complete. 

### `ker_constantCoeff_eq_span_p`

 For a perfect algebra `S` over a domain `M` of characteristic `p`, the kernel of the zeroth
Witt coefficient `W(S) → S` is the ideal generated by `p`. 

### `coeff_lt_eq_zero_iff_exists_p_pow_smul_eq`

 For a perfect algebra `S` over a domain `M` of characteristic `p`, a Witt vector is a multiple
of `p ^ k` exactly when its first `k` coefficients vanish. 

### `isReductionMod_constantCoeff_and_isCompleteTorsionFree`

 Four facts on the Witt vectors `W(S)` of a perfect algebra `S` over a domain `M` of
characteristic `p`, bundled: `New.Variety.isReductionMod_constantCoeff`,
`New.Variety.isCompleteTorsionFree_wittVector`, `New.Variety.ker_constantCoeff_eq_span_p` and
`New.Variety.coeff_lt_eq_zero_iff_exists_p_pow_smul_eq`. 

### `pFlat_ne_zero`

 The element `p♭ = ξ mod p` of `O^♭` is nonzero, since `p` does not divide `ξ` in `A_inf`. 

### `not_isUnit_pFlat`

 The element `p♭ = ξ mod p` of `O^♭` is not a unit, since `ξ` is prime in `A_inf` and a Witt
vector is a unit exactly when its zeroth coefficient is. 

### `IsReductionMod.lTensor`

 Reduction modulo `m` is kept by tensoring on the left: if `f : M → M'` is reduction modulo `m`
(`New.Variety.IsReductionMod`: onto, with kernel `m M`), then so is `L ⊗ f`. 

### `IsReductionMod.bijective_rTensor`

 If `f : M → M'` is reduction modulo `m` (`New.Variety.IsReductionMod`) and `m` kills `L`, then
`f ⊗ L` is bijective. 

### `tmul_ext`

 Two additive maps out of `M ⊗[S] L`, bundled in any type `F` of additive maps, are equal if
they agree on pure tensors. 

### `instance [IsDomain S] [IsBezout S] [IsTorsionFree S L] : Flat S L`

 Over a Bézout domain, a torsion-free module is flat. 

### `isTorsionFree_of_dvd_pow`

 Let `S` be a domain and `π` an element such that every nonzero element of `S` divides some power
of `π`. Then an `S`-module without `π`-torsion is torsion-free. 

### `isSMulRegular_tensor_of_flat_mod`

 Let O = S/m and M' = M/m (`New.Variety.IsReductionMod`), with M' flat over O. If the S-modules M
and L have no m-torsion, then L ⊗_S M has no m-torsion either. 
