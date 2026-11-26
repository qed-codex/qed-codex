---
{
  "module": "src/Lib/PadicHodge/Kisin/Modules.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Kisin/Modules.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Kisin/Modules.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Kisin modules of Kummer charts: lattices with jump sets, letter projectors, invariant forms

For a Kummer chart `k : New.Lift.KummerChart Γ` there is a ring S ⊂ A_inf, the image of Λ⟦X⟧ with
Λ = W(𝔽_{p^f}), and a subgroup Γ' of Γ. Kisin modules are defined inside `L.Ambient = W(C^♭) ⊗ L`
for a lattice L with prescribed jump sets. The objects are functorial in L and compatible with
Frobenius and with Γ'. They split according to the letters `i ∈ 𝔽_{p^f}ˣ`, on which the root of
unity ζ of the coefficients acts as the Teichmüller lift `ω i = letterTeich i`.

## Main definitions and results

* `New.Lift.KummerChart.Letter`: the letters, the units i of 𝔽_{p^f}. For coefficients O with
  ζ^(p^f − 1) = 1 (`New.Lift.KummerChart.Coeffs`), the letter i cuts out the part
  `New.Lift.KummerChart.JumpLattice.letterPart` where ζ = [i].
* `New.Lift.KummerChart.JumpLattice`: a lattice L, crystalline over Γ', with a finite set
  `jumpSet i` of integers for each letter that holds its jumps at the embeddings above i.
* `New.Lift.KummerChart.JumpLattice.forms`: forms, A_inf-linear maps to B_dR that are Γ'-equivariant
  on 1 ⊗ L.
* `New.Lift.KummerChart.JumpLattice.kisinAinf`, `New.Lift.KummerChart.JumpLattice.kisinModule`,
  `New.Lift.KummerChart.JumpLattice.kisinLoc`: an A_inf-module cut out by forms, the Kisin module N,
  and N with all φ^a E inverted.
* `New.Lift.KummerChart.JumpLattice.mem_letterPart_iff_letterProj`,
  `New.Lift.KummerChart.JumpLattice.sum_letterProj`: `e i = letterProj i` projects onto the letter
  `i`, and the `e i` sum to the identity.
* `New.Lift.KummerChart.JumpLattice.exists_span_formsOfType_mod_pred`: the functionals of type `u`
  at `i`, modulo those of type `u - 1`, are spanned over Q̄_p by at most `L.jumpMultiplicity i u` of
  them.
* `New.Lift.KummerChart.JumpLattice.formsOfType_subset_pred_of_notMem`: if `n ∉ L.jumpSet i`, the
  functionals of type `n` at `i` are of type `n - 1`.

Notions from other files:
* `New.Lift.KummerChart`: a chart Λ⟦X⟧ → A_inf (ring `S`, element `E` generating ker θ,
  `frobE a` = φ^a(E)) together with a subgroup Γ' of Γ whose fixed field it belongs to.
* `New.Lift.GalLattice`: a finite free O-module with an O-linear representation of Γ.
* `New.Period.WittCFlat`: the ring W(C^♭) of p-typical Witt vectors over the fraction field C^♭ of
  the tilt O^♭ of the ring of integers of C_p.
* `New.Period.overZp`: a representation of Γ on a module T over a Z_p-algebra R, regarded as a
  Z_p-linear representation.
* `New.Period.jump`: the multiplicity of a Hodge–Tate jump u of a representation at an embedding γ
  of the coefficients into ℂ_p.

## Relation to the literature

Known result: Hodge–Tate weights of Kisin modules. This is the analogue, for the Kisin module of one
Kummer chart inside A_inf, of the statements on Wach modules in the literature. This file proves
only the bounds on the weights, not that the Galois action is trivial modulo the variable. It holds
per unramified embedding of the coefficients, and it gives only upper bounds by the multiplicity of
each jump.
Source: L. Berger, Limites de représentations cristallines, Compositio Math. 140 (2004), 1473–1498,
§III; N. Wach, Représentations p-adiques potentiellement cristallines, Bull. SMF 124 (1996),
375–400.

See also `Lib.PadicHodge.Kisin.PeriodMatrixFrame`.



## Letters, lattices with jump sets, forms and Kisin modules

* `New.Lift.saturateBy`: the saturation of a submodule P by a submonoid M, the x with mx in P for
  some m in M.
* `New.Lift.KummerChart.Letter`, `New.Lift.KummerChart.Coeffs`,
  `New.Lift.KummerChart.JumpLattice`: the letters, rings of coefficients with a root ζ, and
  lattices with jump sets.
* `New.Lift.KummerChart.JumpLattice.letterOp`, `letterPart`, `letterProj`: the operator ω(i)⁻¹ζ,
  the part at the letter i, and the projector onto it.

Conventions: `New.Lift.FrobGroup Γ` = ℤ × Γ acts on W(C^♭) ⊗ L, with φ the Frobenius;
`DiagTensor.mk 1 t` is 1 ⊗ t; `hodgeFil n` is tⁿB_dR^+; E is an element of S, a generator of ker θ,
and `k.frobE a` is φ^a E.


### `instance : SMulCommClass ℤ_[p] Ainf WittCFlat`

 The actions of ℤ_p and of A_inf on W(C^♭) commute. 

 ### Saturation of a submodule 

### `saturateBy`

 The saturation of a submodule P of X by a submonoid M: the x in X with mx in P for some m in
M. 

### `mem_saturateBy_of_smul`

 If `r` divides an element `s` of `M` and `r • x` lies in the saturation of `Q` by `M`, then
so does `x`. 

### `saturateBy_induction`

 Induction on the saturation by the monoid generated by the f(a): a property that holds on Q
and passes from f(a)·x to x holds on all of the saturation. 

 ### Letters, coefficients and lattices with jump sets 

### `Letter`

 The letters of a Kummer chart: the multiplicative group of the field with p^f elements in
O^♭. A letter i singles out the embeddings g of a ring of coefficients into ℂ_p with g(ζ) = θ([i]),
[i] the Teichmüller lift; these are the embeddings above i, and φ^a sends [i] to [i^(p^a)]. 

### `instance : Fintype Letter`

 The letters form a finite type. 

### `instance : Invertible (card Letter : ℤ_[p])`

 The number `p ^ f - 1` of letters is invertible in `ℤ_[p]`, being a unit modulo `p`. 

### `letterFrob`

 The permutation i ↦ i^p of the letters, the units of the field with p^f elements. 

### `letterTeich`

 The multiplicative map sending a letter to its Teichmüller lift in the Witt vectors of the
field with p^f elements, viewed in the ring S of the chart. 

### `LetterRoot`

 The elements ζ of O with ζ^q = 1, where q = p^f − 1 is the number of letters of the chart. 

### `Coeffs`

 A ring of coefficients: a finite free Z_p-algebra O with an element ζ, ζ^{p^f−1} = 1, which
cuts out the letters. 

### `Coeffs.O`

 The ring of coefficients O. 

### `Coeffs.commRing`

 O is a commutative ring. 

### `Coeffs.padicIntegerRing`

 O is a ℤ_p-algebra. 

### `Coeffs.ζ`

 An element ζ of O with ζ^(p^f − 1) = 1. 

### `JumpLattice`

 A lattice with jump sets: a finite free O-module with an action of Γ, crystalline over Γ', with,
for each letter i, a finite set of integers that contains its jumps at every embedding g of O with
g(ζ) = θ(ω(i)). 

### `JumpLattice.jumpSet`

 For each letter, a finite set of integers that holds the jumps at that letter. 

### `JumpLattice.embJumps`

 One set of integers for each embedding of O. 

### `JumpLattice.inClass`

 The lattice is crystalline over Γ' and has its jumps at each embedding in the set given for
  that embedding. 

### `JumpLattice.embJumps_subset`

 The set at a letter i contains the set of every embedding g with g(ζ) = θ(ω(i)). 

### `Letter.stepBack`

 The letter a steps before i: the image of i under the a-th power of the inverse of the
permutation x ↦ x^p, so that φ^a sends its Teichmüller lift to that of i. 

### `stdOrders`

 The standard exponent at the step `a` for the level `l` and the weight `u`: `0` for `a < l`
and `-u` for `a ≥ l`. 

 ### Forms and the Kisin module 

### `Ambient`

 The module W(C^♭)⊗L for the lattice underlying L. 

### `wittMap`

 For an O-linear map F: L → L' of lattices, the W(C^♭)-linear map W(C^♭) ⊗ L → W(C^♭) ⊗ L'
obtained by extension of scalars. 

### `ainfLattice`

 The A_inf-submodule of W(C^♭) ⊗ L spanned by the elements 1 ⊗ y, y in L. 

### `Functional`

 The type of A_inf-linear maps from W(C^♭) ⊗ L to B_dR. 

### `forms`

 The set of A_inf-linear maps μ: W(C^♭) ⊗ L → B_dR that are Γ'-equivariant on 1 ⊗ L, that is,
μ(1 ⊗ gt) = g·μ(1 ⊗ t). 

### `frobGroup_smul_smul`

 The action of m ∈ ℤ × Γ on W(C^♭) ⊗ L is semilinear: m • (r • x) = (m • r) • (m • x). 

### `semilinearAct`

 The action of an element m of ℤ × Γ on W(C^♭) ⊗ L, as a map semilinear for the action of m
on A_inf. 

### `kisinAinf`

 The A_inf-module of the x in A_inf[1/τ] ⊗ L (some power of the element `tau` of A_inf sends x
into the A_inf-span of the 1 ⊗ y, y in L) with μ(φ^n x) in B_dR^+ for all n ≥ 1 and all μ in
`New.Lift.KummerChart.JumpLattice.forms`. 

### `crysForms`

 The invariant functionals μ (`New.Lift.KummerChart.JumpLattice.forms`) whose restriction to
1 ⊗ L comes from a Z_p-linear map of L into the period ring `Bmax`. 

### `valueFieldPoints`

 For an A_inf-submodule Q of W(C^♭) ⊗ L, the S-submodule of the x in Q on which every form in
`New.Lift.KummerChart.JumpLattice.forms` takes values in the field 𝒦₀ = `valueField 0`, a subfield
of B_dR that contains the image of S. 

### `kisinModule`

 The Kisin module of L: the S-module of the x in `New.Lift.KummerChart.JumpLattice.kisinAinf` on
which all Γ'-equivariant forms take values in the field 𝒦₀ (`New.Lift.KummerChart.valueField`). 

### `frobKisinAinf`

 The image of `New.Lift.KummerChart.JumpLattice.kisinAinf` under φ^l. It is the A_inf-submodule
of the x in W(C^♭)⊗L with φ^{−l}x in `New.Lift.KummerChart.JumpLattice.kisinAinf`. 

### `kisinLocAinf`

 The x in W(C^♭) ⊗ L that some product of the φ^a E multiplies into
`New.Lift.KummerChart.JumpLattice.kisinAinf`. 

### `kisinLoc`

 The Kisin module N with all φ^a E inverted: the x in
`New.Lift.KummerChart.JumpLattice.kisinLocAinf` on which all forms take values in the field 𝒦₀. 

 ### Equivariant maps 

### `Hom`

 A Γ-equivariant O-linear map L → L' between lattices over the same coefficients O. 

### `Hom.wittMap`

 For an equivariant map F : L → L', the W(C^♭)-linear map W(C^♭)⊗L → W(C^♭)⊗L' obtained by
extension of scalars. 

### `mulZeta`

 Scalar multiplication on L by the root of unity ζ of the coefficient ring O, as an
equivariant map from L to itself. 

### `letterOp`

 The endomorphism ω(i)⁻¹ζ of W(C^♭) ⊗ L, with ζ acting through L and ω(i), the Teichmüller
lift of the letter i, as a scalar. 

### `letterPart`

 The part of W(C^♭) ⊗ L at the letter i: the A_inf-submodule on which ζ acts as the
Teichmüller lift ω(i). 

### `letterProj`

 The endomorphism q⁻¹ Σ_{n<q} (ω(i)⁻¹ζ)^n of W(C^♭) ⊗ L, q = p^f − 1; as ζ^q = 1 it
projects to the part at the letter i. 

### `formsOfType`

 The A_inf-linear μ: W(C^♭) ⊗ L → B_dR that are Γ'-equivariant on 1 ⊗ L and send the
projection of 1 ⊗ L to the letter i into t^{−u}B_dR^+. 

### `jumpMultiplicity`

 The total multiplicity of the Hodge–Tate jump u of L over all embeddings γ of O in ℂ_p above
the letter i, that is, with γ(ζ) = θ(ω(i)). 

### `fracSpan`

 The x in W(C^♭) ⊗ L that some non-zero divisor of A_inf multiplies into the A_inf-span of
the elements 1 ⊗ y, y in L. 

### `jumpBound`

 The least natural number a such that all Hodge–Tate jumps of L, as a Z_p-representation of
Γ', lie in [−a, a]; it is 0 if there is none. 

### `valueAt`

 For an A_inf-linear μ: W(C^♭) ⊗ L → B_dR, the map μ ∘ φ^{−a}, semilinear for φ^{−a}: A_inf →
B_dR. 


## Letter projectors, functoriality, and forms of a given type

A functional is an `A_inf`-linear map `L.Ambient → B_dR`. It is invariant (`forms`) if it is
`Γ'`-equivariant on `1 ⊗ L`. It is of type `u` at `i` (`formsOfType`) if moreover it maps
`letterProj i (1 ⊗ L)` into `t ^ (-u) B_dR⁺`.


### `Hom.wittMap_smul`

 The map `W(C^♭) ⊗ L → W(C^♭) ⊗ L'` induced by an equivariant `F` commutes with the action of
`m` in ℤ × Γ. 

### `wittMap_mem_ainfLattice`

 The map induced by an O-linear `F : L → L'` sends the A_inf-span of the `1 ⊗ y`, y in L, into
the corresponding span for L'. 

### `Hom.comp_wittMap_mem_forms`

 Composing an invariant functional on `L'` with the map induced by `F` gives an invariant
functional on `L`. 

### `Hom.wittMap_mem_kisinAinf`

 Let `F : L → L'` be an equivariant map of lattices with jump sets, and let
`F.wittMap : W(C^♭) ⊗ L → W(C^♭) ⊗ L'` be its extension of scalars. Then `F.wittMap` sends
`L.kisinAinf` into `L'.kisinAinf`. Here `kisinAinf` is the A_inf-module of those x in A_inf[1/τ] ⊗ L
with μ(φ^n x) ∈ B_dR^+ for all n ≥ 1 and all μ in `forms`. 

### `Hom.wittMap_mem_kisinModule`

 The map induced by an equivariant `F : L → L'` sends the Kisin module of L into that of L'. 

### `Hom.wittMap_mem_frobKisinAinf`

 The map induced by an equivariant `F : L → L'` sends `L.frobKisinAinf l`, the image of
`L.kisinAinf` under φ^l, into `L'.frobKisinAinf l`. 

 ### The projectors to the letters 

### `letterOp_pow_mk`

 The n-th power of `letterOp i`, that is of ω(i)⁻¹ζ, on a pure tensor `a ⊗ t`. 

### `mem_letterPart_iff_mulZeta`

 x lies in the part at the letter i exactly when ζ acts on it as the Teichmüller lift ω(i). 

### `smul_eq_val_smul`

 The ring S of the chart acts on W(C^♭) ⊗ L through its inclusion in A_inf. 

### `Hom.wittMap_letterProj`

 The map induced by an equivariant `F : L → L'` commutes with the projectors to the letter i. 

### `smul_letterProj`

 If `m` in ℤ × Γ sends ω(i)⁻¹ to ω(i')⁻¹, it carries the projector to the letter i into the
projector to the letter i'. 

### `gal_smul_letterProj`

 An element `g` of the Galois monoid of the chart commutes with the projector to each letter. 

### `phi_pow_smul_letterTeich`

 φ^l sends ω(i)⁻¹ to ω(j)⁻¹, where j is the image of i under the l-th power of i ↦ i^p. 

### `letterProj_mem_letterPart`

 The projector to the letter i takes values in the part at the letter i. 

### `mem_letterPart_iff_letterProj`

 x lies in the part at the letter i exactly when the projector to i fixes it. 

### `gal_smul_mem_letterPart`

 The part at each letter is stable under the Galois monoid of the chart, in both directions. 

### `phi_pow_smul_mem_letterPart_iff`

 `φ ^ a • x` lies in the part at the letter i exactly when x lies in the part at `i.stepBack a`,
the letter whose `p ^ a`-th power is i. 

 ### Small facts on the Kisin module and the constants 

### `frobEUnit_pow_smul`

 The unit `frobEUnit a` acts by the element φ^a E of S, also on powers. 

### `finrank_wittFq`

 The Witt vectors of the field with p^f elements have rank f over ℤ_p. 

### `basisValues`

 The B_dR-linear map sending μ: W(C^♭) ⊗ L → B_dR to the vector of its values μ(1 ⊗ e_l) on a
chosen Z_p-basis (e_l) of L. 

### `ainfLattice_eq_span_basis`

 The A_inf-span of the `1 ⊗ y`, y in L, is spanned by the `1 ⊗ e_l` for the chosen ℤ_p-basis
(e_l) of L. 

 ### Invariant functionals and their conjugates 

### `apply_eq_of_mem_fracSpan`

 Two functionals that agree on `1 ⊗ L` agree on `L.fracSpan`, since `B_dR` is torsion-free over
`A_inf`. 

### `inr_smul`

 An element g of Γ, embedded in ℤ × Γ, acts on A_inf through `toGp g`. 

### `conjForm`

 The conjugate of an A_inf-linear map μ: W(C^♭) ⊗ L → B_dR by g in Γ, namely
x ↦ (toGp g)⁻¹ · μ(g x). 

### `form_gal_smul`

 An invariant functional commutes with `Γ'` on all of `L.fracSpan`. 

### `smul_mem_ainfLattice`

 The A_inf-span of the `1 ⊗ y`, y in L, is stable under ℤ × Γ. 

### `smul_mem_fracSpan`

 `L.fracSpan` is stable under ℤ × Γ: if r x lies in the lattice, so does (m r)(m x). 

### `valueAt_frobEUnit_zpow_smul`

 `valueAt a μ`, which is μ ∘ φ^{-a}, turns the action of the n-th power of the unit φ^b E into
multiplication by the n-th power (n ∈ ℤ) of its image `phiInvToBdR a (frobE b)` in B_dR under
φ^{-a}. 

### `letterProj_mk_mem_ainfLattice`

 The projection of `1 ⊗ t` to a letter stays in the A_inf-span of the `1 ⊗ y`. 

### `comp_letterProj_mem_forms`

 An invariant functional composed with the projector to a letter is again invariant. 

 ### The letters decompose the module 

### `sum_letterProj`

 The projectors to the letters sum to the identity of W(C^♭) ⊗ L. 

 ### Functionals of given type and Hodge–Tate jumps 

### `exists_span_formsOfType_mod_pred`

 For a lattice with jump sets `L`, a letter `i` and `u : ℤ`, `formsOfType i u` is the set of
A_inf-linear maps W(C^♭) ⊗ L → B_dR that are Γ'-equivariant on 1 ⊗ L and send the projection of
1 ⊗ L to `i` into t^{−u}B_dR^+. `L.jumpMultiplicity i u` is the total multiplicity of the Hodge–Tate
jump `u` over the embeddings of `O` above `i`. There are `r ≤ L.jumpMultiplicity i u` forms `ν m` of
type `u` at `i` such that every form of type `u` at `i` is a `Q̄_p`-combination of the `ν m` modulo
a form in `formsOfType i (u - 1)`. 

### `formsOfType_subset_pred_of_notMem`

 If n is not in `L.jumpSet i`, every functional of type n at the letter i is of type n - 1. 
