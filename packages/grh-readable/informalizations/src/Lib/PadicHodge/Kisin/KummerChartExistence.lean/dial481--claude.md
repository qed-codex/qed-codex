---
{
  "module": "src/Lib/PadicHodge/Kisin/KummerChartExistence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Kisin/KummerChartExistence.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Kisin/KummerChartExistence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Witt coefficients, the Frobenius group action and existence of Kummer charts

Let Λ = `New.Lift.WittFq f` be the ring of Witt vectors of the field with p^f elements inside O^♭,
with p implicit, and let θ be Fontaine's map from A_inf to O_C. The group ℤ × Γ acts on O^♭, A_inf
and W(C^♭), where (n, g) acts as φ^n j(g) and φ is the bijective Frobenius. A local field is given
by `Γ : GroupOverGp p`, a group with a homomorphism j = `toGp` to `Gp p` of open image; the field is
the subfield of ℚ̄_p fixed by the image. Every such field has a Kummer chart: a chart
S = Λ⟦z⟧ ⊂ A_inf with a subgroup Γ' of Γ of index prime to p, such that j(Γ') fixes Λ and θ(z) and
moves z to every [ε]^l z.

## Main definitions and results

* `New.Lift.wittToQpBar`: the restriction of θ to Λ, with values in the algebraic closure of
  `ℚ_[p]`; it is injective (`New.Lift.wittToQpBar_injective`).
* `New.Lift.FrobGroup`: the group ℤ × Γ, with Frobenius `New.Lift.FrobGroup.φ`.
* `New.Lift.KummerChart`: a Kummer chart; `New.Lift.KummerChart.IsUnramified`: it is unramified.
* `New.Lift.exists_kummerChart`: every such field has a Kummer chart, with ef the degree of the
  field.

Notions from other files:
* `New.Period.OFlat`: The ring O^♭, the inverse limit of O_C/p along x ↦ x^p, where O_C is the ring
  of integers of C_p.
* `New.Lift.Chart`: A Λ-algebra map Λ[[X]] → A_inf with image S, sending X to a non-unit Teichmüller
  lift z and a series X^e A + p, A a unit, to an element E that generates ker θ.

## Relation to the literature

Known; see `Lib.PadicHodge.Kisin.PeriodMatrixFrame` and `Lib.PadicHodge.PeriodRings.DeRhamPeriods`
for sources.


 ## Embedding the Witt coefficients in ℚ̄_p by θ 

### `wittToQpBar`

 The Z_p-algebra homomorphism from Λ = W(F_{p^f}) to Q̄_p that becomes the restriction of θ
after the inclusion of Q̄_p in C_p. 

### `wittToQpBar_injective`

 The map from Λ = W(F_{p^f}) to Q̄_p given by θ is injective. 

### `smul_algebraMap_wittFq_eq_iff`

 An element g of G_p fixes the image in A_inf of c ∈ Λ if and only if g fixes the image of c
in Q̄_p under `New.Lift.wittToQpBar`. 

 ## Frobenius and Galois actions, and Teichmüller roots of unity 

 ### The action of ℤ × Γ 

### `FrobGroup`

 The group ℤ × Γ (ℤ written multiplicatively); on rings with bijective Frobenius φ, such as
A_inf, the pair (n, g) acts as φ^n j(g). 

### `FrobGroup.snd`

 The projection ℤ × Γ → Γ. 

### `FrobGroup.φ`

 The element (1, identity) of ℤ × Γ, which acts on O^♭, A_inf and W(C^♭) as the Frobenius φ. 

### `FrobGroup.inr`

 The inclusion Γ → ℤ × Γ, g ↦ (0, g). 

### `phi_smul_oFlat`

 The element φ = (1, 1) of ℤ × Γ acts on O^♭ as the Frobenius x ↦ x^p. 

 ### Teichmüller roots of unity 

### `isUnit_teichmuller_sub`

 For distinct elements a ≠ b of the field with p^f elements in O^♭, the difference [a] − [b]
of their Teichmüller lifts is a unit of W(F_{p^f}). 

### `exists_flatFq_teichmuller_eq`

 Let k be the field of p^f elements in O^♭ and s: W(k) → K a ring homomorphism to a field.
Every x in K with x^{p^f} = x is s([a]) for the Teichmüller lift [a] of some a in k. 

### `fixes_roots_iff_fixesLambda`

 An element of G_p fixes all (p^f - 1)-th roots of unity in Q̄_p if and only if it fixes the
image of W(F_{p^f}) in A_inf pointwise. 


## Existence of Kummer charts

Here z = [u] is the Teichmüller lift of some u in O^♭, and `epsTilt` is ε = (1, ζ_p, ζ_{p²}, …).

* `New.Lift.exists_smul_teichmuller_eq`: the compactness step from roots of π to compatible towers
  of roots.


### `exists_smul_teichmuller_eq`

 Let C be a closed subgroup of G_p that is transitive on the n-th roots of π ∈ Q̄_p for every
n > 0 (`h_transitive`). Let u, v ∈ O^♭ and e > 0 be such that the untilt u^♯ of u satisfies
(u^♯)^e = π and the untilt of v has the same e-th power. Then some g in C sends the Teichmüller
lift [u] to [v]. 

### `KummerChart`

 A Kummer chart for j : Γ → G_p with open image: a chart S = Λ⟦z⟧ ⊂ A_inf, Λ = W(𝔽_{p^f}), and a
subgroup Γ' (the field `subgroup`) of Γ of index prime to p, with four properties. The image j(Γ')
fixes Λ and θ(z), and it contains every element of G_p that fixes Λ and θ(z). Γ' contains all g with
j(g) close enough to 1, that is, ∀ᶠ g in `New.Period.nearOne` Γ, g ∈ Γ'. For each l ≥ 0 some g in Γ'
has g z = [ε]^l z. 

### `KummerChart.subgroup`

 The subgroup `Γ'` of `Γ` whose fixed field the chart belongs to. 

### `KummerChart.index_coprime`

 The index of `Γ'` in `Γ` is prime to `p`. 

### `KummerChart.fixes`

 Every element of `Γ'` fixes the constants `Λ` and `θ(z)`. 

### `KummerChart.isChartOf`

 Every element of `G_p` that fixes `Λ` pointwise and fixes `θ(z)` lies in `j Γ'`. 

### `KummerChart.nearOne_le`

 The elements of `Γ` whose image under `j` is close enough to `1` lie in `Γ'`. 

### `KummerChart.exists_smul_z`

 For every natural number `l`, some `g` in `Γ'` has `g z = [ε] ^ l z`. 

### `KummerChart.thetaPhiInv_phi_pow`

 The map `thetaPhiInv a` = θ ∘ φ^{−a} sends φ^a • r to θ(r), for r in A_inf and φ = (1, 1). 

### `KummerChart.differentBound`

 The number d = 0 if the ramification index e of the chart is 1, and d = v_p(e) + 1 otherwise. 

### `KummerChart.IsUnramified`

 The Kummer chart is unramified: E = z + p and the ramification index e is 1. The third
condition d = 0 follows from e = 1 by the definition of `New.Lift.KummerChart.differentBound`; it is
recorded for convenience. 

### `KummerChart.chart_isChartOf`

 The chart of a Kummer chart belongs to the field fixed by j(Γ): every element of G_p that fixes
Λ pointwise and fixes θ(z) lies in j(Γ). 

### `Chart.exists_smul_z_eq_of_transitive`

 Let Γ act on Q̄_p through j : Γ → G_p, and let c be a chart whose element ϖ^♭ of O^♭ has untilt
π₀ ∈ Q̄_p. If j(Γ) is transitive on the n-th roots of π₀ for every n > 0, then for every l some
g ∈ Γ moves z = [ϖ^♭] to [ε]^l z. 

### `associated_pow_neg_of_irreducible`

 Let K be the subfield of Q̄_p fixed by an open subgroup V of G_p, local with group V (`L`),
whose normalised order is e times that of ℚ_p (`h_ord`). Then for an irreducible element π of the
integers of K, π^e is −p times a unit. 

### `KummerChart.IsChartFor`

 A Kummer chart `k` for `Γ`, seen in `G_p` through `j = 𝒥.toGp`, fits the field fixed by
`j(Γ)`: the four properties that `exists_kummerChart` provides. 

### `KummerChart.IsChartFor.fixes_thetaZ`

 All of `j(Γ)` fixes `Λ` pointwise and `θ(z)`. 

### `KummerChart.IsChartFor.e_mul_f_eq_index`

 The ramification index times the residue degree is the index `[G_p : j(Γ)]`. 

### `KummerChart.IsChartFor.isUnramified_of_inertia_le`

 If `j(Γ)` contains the inertia group of `G_p`, the chart is unramified. 

### `KummerChart.IsChartFor.exists_isFrob`

 `j(Γ)` contains an element `φ` with `φ x ≡ x ^ (p ^ f)` on the integers of `ℚ̄_p`, modulo
  their maximal ideal. 

### `exists_kummerChart`

 The Kummer chart of the field fixed by j(Γ), where `Γ` carries a homomorphism j to G_p with open
image. There is a Kummer chart for Γ over Λ = W(F_{p^f}), with coordinate z (a Teichmüller lift in
A_inf) and E = z^e A + p with A a unit, that fits that field (`KummerChart.IsChartFor`): j(Γ) fixes
Λ and θ(z), ef = [G_p : j(Γ)], the chart is unramified if j(Γ) contains inertia, and j(Γ) contains a
Frobenius. 
