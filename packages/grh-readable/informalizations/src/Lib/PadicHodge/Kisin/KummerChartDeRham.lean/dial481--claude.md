---
{
  "module": "src/Lib/PadicHodge/Kisin/KummerChartDeRham.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Kisin/KummerChartDeRham.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Kisin/KummerChartDeRham.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Kummer charts: the different, the primes φ^a E of A_inf and their images in B_dR

Fix a Kummer chart `k` (`New.Lift.KummerChart`) with ring `S ⊆ A_inf` and distinguished element `E`.
The file studies the elements p_a = φ^a E and δ = zτ of A_inf and bounds the different of the chart.

## Main definitions and results

* `New.Lift.KummerChart.exists_derivative_dvd_p_pow`: a bound for the different.
* `New.Lift.phiInvToBdR`: the map `r ↦ φ^{-a} r` from `A_inf` to `B_dR`.
* `New.Lift.KummerChart.phiInvToBdR_mem_hodgeFil_one_iff`,
  `New.Lift.KummerChart.phiInvToBdR_frobE_zpow_mem_hodgeFil`: it sends `r` to an element of positive
  order exactly when `φ^a E` divides `r`, and the `m`-th power of the image of `φ^a E` has order at
  least `m`.
* `New.Lift.KummerChart.valueField`: the subfield `𝒦_a` of `B_dR` in which values are taken.
* `New.Lift.KummerChart.sum_phiInvToBdR_map_mul_mem_of_mem_valueField`: `S`-linear maps `A_inf → S`
  preserve linear relations over `𝒦_a`.
* `New.Lift.KummerChart.smul_sub_mem_hodgeFil_of_valueField`: if `φ^a E` divides `gs − s` for all
  `s` in `S`, then `g` fixes the elements of `𝒦_a` of order at least `0` modulo `t`; more generally,
  the same holds for the sums `∑ l, t l s` and `∑ l, t l x`, with the `t l` in the Galois monoid.

Notions from other files:
* `New.Period.Ainf`: the ring A_inf of p-typical Witt vectors over the tilt O^♭ of the ring O_C of
  integers of C_p.
* `New.Period.tau`, `New.Period.xi`: τ = [ε^(1/p)] − 1, with φ τ = μ = [ε] − 1, and ξ = μ/τ.
* `New.Lift.FrobGroup`: the group ℤ × Γ, acting on A_inf by (n, g) ↦ φ^n j(g).
* `New.Lift.Chart.S`, `New.Lift.Chart.bicommutant`: for a chart, the Λ-subalgebra S of A_inf that is
  the image of the chart's map Λ[[X]] → A_inf, with `k.coord₀ : A_inf → S` an S-linear retraction of
  A_inf onto S, and the subalgebra S_B of B^+, the closure of S[E/p] with p inverted.
* `New.Period.hodgeFil`: the step Fil^n = t^n B_dR^+ of the filtration of B_dR, for n in ℤ.

## Relation to the literature

Known; see `Lib.PadicHodge.Kisin.PeriodMatrixFrame` for sources.


 ### The primes p_a = φ^a E and the element δ = zτ 

### `galMonoid`

 The submonoid of ℤ × Γ consisting of the elements (0,g) with g in the subgroup Γ' of the
Kummer chart. 

### `zTau`

 The element δ = zτ of A_inf, where z is the coordinate of the Kummer chart. 

### `not_p_dvd_val_frobE`

 The prime p does not divide p_a = φ^a E in A_inf. 

### `frobEUnit`

 The image in W(C^♭) of p_a = φ^a(E), as a unit; it is invertible because p does not divide
p_a in A_inf. 

### `zTauUnit`

 The image in W(C^♭) of δ = zτ, as a unit; it is invertible because p divides neither z nor τ
in A_inf. 

### `exists_derivative_dvd_p_pow`

 Bound for the different of a chart: write the Kummer chart as S = Λ⟦z⟧ ⊂ A_inf with
Λ = `WittFq k.f` (Witt vectors of a finite field), let E = `k.E` ∈ S be the image of X^e A + p, and
let e be the ramification index of the chart. Then there is a polynomial P over Λ with E ∣ P(z) in S
such that θ(P'(z)) divides p^d in O_C, where θ : A_inf → O_C is Fontaine's map, where
d = `differentBound` is 0 if e = 1 and v_p(e) + 1 otherwise. 

### `instance : OverGp k.subgroup p`

 The subgroup Γ', with the restriction of j, is a group over G_p: its image is open. 

### `not_frobE_dvd_frobE_of_ne`

 For a ≠ b, the element p_a = φ^a E does not divide p_b = φ^b E in A_inf. 

### `smul_phi_pow_comm`

 For any action of ℤ × Γ on a type X, an element g of the Galois monoid of the chart commutes
with φ^a. 

### `phi_pow_smul_z`

 The coordinate z is a Teichmüller lift, so φ^a z = z^(p^a). 

 ### The action of Γ' on the chart 

### `zTau_mul_E_dvd_smul_sub`

 Let Γ' be the subgroup of Γ of index prime to p attached to the Kummer chart S = Λ⟦z⟧, and let g
be in the Galois monoid, that is, an element (0, γ) of ℤ × Γ with γ ∈ Γ', acting through γ. Then for
every s ∈ S, the element zτ·E divides gs − s in A_inf, where zτ = `zTau` and z is the coordinate of
the chart. 

 ## The fields 𝒦_a in B_dR and linearity of coordinate maps over them 

### `phiInvToBdR`

 The ring homomorphism `A_inf → B_dR` that sends `r` to the image of `φ^{-a} r`. 

### `KummerChart.valueField`

 The subfield `𝒦_a` of `B_dR` generated over the fixed field of `Γ'` by the products
`b * φ^{-a} s` with `b` in `S_B` and `s` in `S`. It is the field generated by the images of `S_B`
and of `φ^{-a} S`, see `KummerChart.valueField_eq_adjoin_union`. 

### `instance : MulSemiringAction k.galMonoid BdR`

 The Galois monoid acts on B_dR through the Galois group G_p. 

### `instance : SMulDistribClass k.galMonoid Ainf BdR`

 The action of the Galois monoid on B_dR is compatible with its action on A_inf. 

### `smul_phiInvToBdR`

 An element g of the Galois monoid commutes with the map `r ↦ φ^{-a} r` from A_inf to
BdR. 

### `phiInvToBdR_mem_hodgeFil_one_iff`

 For r in A_inf, the image of φ^{−a}(r) in B_dR lies in tB_dR^+ if and only if φ^a(E) divides
r in A_inf. 

### `mul_mem_hodgeFil_iff_of_not_frobE_dvd`

 Let `r` in A_inf be prime to `φ^a E`. Then for every integer `m` and every `y` in B_dR, the
product of `(φ^{-a} r)^m` and `y` lies in Fil^n = t^n B_dR^+ exactly when `y` does. 

### `phiInvToBdR_frobE_zpow_mem_hodgeFil`

 For every integer m, let u be the image in B_dR of φ^{−a}(φ^a E), that is, of E. Then u^m lies
in Fil^m = t^m B_dR^+. 

### `valueField_eq_adjoin_union`

 The field `𝒦_a` is generated by the images of `S_B` and of `φ^{-a} S`. 

### `algebraMap_ainf_eq_algebraMap_bicommutant`

 The image in B_dR of an element `s` of S is the image of `s` under S_B → B_dR: both maps
factor through B^+. 

### `valueField_zero_le`

 The field `𝒦_0` is contained in `𝒦_a`. 

### `mem_hodgeFil_zero_and_mem_valueField_zero_of_fixed`

 An element of `B_dR` fixed by `Γ'` lies in `Fil⁰` and in `𝒦₀`. 

### `sum_phiInvToBdR_map_mul_mem_of_mem_valueField`

 Let `f : A_inf → S` be `S`-linear, and let the `v l` lie in `𝒦_a` = `valueField a`, the subfield
of `B_dR` generated over the fixed field of Γ' by the images of `S_B` and of φ^{-a} S. If the sum of
the `φ^{-a} (r l) * v l` lies in a `B_dR^+`-submodule `W` of `B_dR`, then so does the sum of the
`φ^{-a} (f (r l)) * v l`. 

### `smul_sub_mem_hodgeFil_of_valueField`

 Let `g` and `t 0, …, t (m - 1)` be elements of the Galois monoid of the chart, that is, elements
(0, γ) of ℤ × Γ with γ in the subgroup Γ', each acting through γ. Let `x` be an element of `𝒦_a`
(the subfield of `B_dR` generated over the fixed field of Γ' by `S_B` and φ^{-a} S) that lies in
Fil⁰ = B_dR^+. Suppose that for every `s` in `S`, `φ^a E` divides `g (∑ l, t l s) - ∑ l, t l s` in
A_inf; then `g (∑ l, t l x) - ∑ l, t l x` lies in Fil¹ = t B_dR^+. 
