---
{
  "module": "src/Lib/PadicHodge/PeriodRings/DeRhamPeriods.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/PeriodRings/DeRhamPeriods.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/PeriodRings/DeRhamPeriods.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The cyclotomic action on μ, the period t, and the de Rham field B_dR

This file studies the Galois and Frobenius actions on Fontaine's period rings for `ℂ_[p]`. We write
A_inf = `New.Period.Ainf` (Witt vectors of `OFlat`, the tilt of the integers of `ℂ_[p]`),
ε = `New.Period.epsTilt` (a compatible system of `p`-power roots of unity in the tilt), μ = [ε] − 1,
ξ for the generator of the kernel of θ, φ for Frobenius (`New.Period.frobEnd`) and χ for the
cyclotomic character `New.cyclotomicGp`. Let B_dR⁺ = `New.Period.BdRPlus`, the ξ-adic completion of
B⁺ = `New.Period.BPlus`. The fraction field B_dR of B_dR⁺ contains B = B⁺[1/μ] and Q̄_p
equivariantly.

## Main definitions and results

* `New.Lift.mu_sq_dvd_smul_mu_sub`: in `New.Period.Ainf`, the Witt vectors of the tilt of the
  integers of `ℂ_[p]`, an element `g` of the Galois group `New.Gp p` sends `μ = [ε] - 1` to `χ(g) μ`
  modulo `μ ^ 2`. Here `ε` is `New.Period.epsTilt` and `χ` is the cyclotomic character. The
  divisibility `μ ^ 2 ∣ g μ - χ(g) μ` holds in `A_inf` itself; the proof checks it modulo every
  power of the ideal `(p, ξ)`, where `ξ` generates the kernel of Fontaine's map `θ`.
* `New.Period.exists_tPeriod`: some unit multiple `t` of `p μ` has `φ t = p t` and `g t = χ(g) t`.
* `New.Period.BdR`: the fraction field of B_dR⁺; G_p acts on it and B embeds in it equivariantly.
* An embedding of Q̄_p in B_dR⁺, got by lifting along θ since Q̄_p is formally étale over ℚ_p;
  `New.Period.thetaBdR_algebraMap_padicAlgCl` says it is a section of θ,
  `New.Period.BdR.smul_algebraMap_padicAlgCl` that it is G_p-equivariant.
* `New.Period.Bmax.fundamental_sequence_surjective`: (φ − 1, inclusion) maps B onto
  B × B_dR / B_dR⁺, the surjectivity in the fundamental exact sequence.

Notions from other files:
* `New.Period.Amax`: The ring A, the p-adic completion of A_inf[ξ/p]; B⁺ = A[1/p].
* `New.Period.mu`, `New.Period.tau`, `New.Period.xi`: The elements μ = [ε] − 1, τ = [ε^{1/p}] − 1
  and ξ = Σ_{0 ≤ i < p} [ε^{1/p}]^i of A_inf; ξτ = μ and φ(τ) = μ.

## Relation to the literature

Known result: Fontaine's period rings and the fundamental exact sequence. Here Colmez's B_max
replaces B_cris and the period t is built without logarithms. The part of Fontaine's regularity that
is used, namely that the invariants of the fraction field of B already lie in B, is proved in
`Lib.PadicHodge.Crystalline.Regularity` (`New.Period.fontaine_regularity`). Source: P. Colmez,
Théorie d'Iwasawa des représentations de de Rham d'un corps local, Ann. of Math. 148 (1998),
III.2-III.3; J.-M. Fontaine, Le corps des périodes p-adiques, Astérisque 223 (1994); X. Caruso, An
introduction to p-adic period rings (2019), §3.


 ## The action of G_p on μ modulo μ² 

### `pow_p_pow_sub_mem_of_xi_dvd`

 If `ξ` divides `x - y` in `A_inf`, then `x ^ p ^ m - y ^ p ^ m` lies in the `m`-th power of the
ideal `(p, ξ)`. 

### `mu_sq_dvd_smul_mu_sub`

 Let `g` be an element of the Galois group `G_p` and `χ(g)` in `ℤ_[p]ˣ` its cyclotomic
character. Then `μ ^ 2` divides `g μ - χ(g) μ` in `A_inf`, where `μ = [ε] - 1`: the element `g`
sends `μ` to `χ(g) μ` modulo `μ ^ 2`. 


## The period t with φt = pt and gt = χ(g)t

The period is constructed without logarithms, in `New.Period.Amax`, the `p`-adic completion of
`A_inf[ξ / p]`.


### `Amax.exists_sub_mul_frobEnd_eq`

 Let `u` be an element of `Amax` divisible by `p`. Then for every `w` the equation
`c - u φ(c) = w` has a solution `c` in `Amax`, where `φ` is the Frobenius `frobEnd`. 

### `frobEnd_eq_smul`

 The Frobenius `frobEnd` of `Amax` is the action of the Frobenius element `(ofAdd 1, 1)` of
`FrobGal`. 

### `exists_tPeriod`

 There is an element `t` of Colmez's period ring `Amax` (the p-adic completion of
`A_inf[X]/(pX − ξ)`) that is a unit multiple of `μ p`, where `μ = [ε] − 1` is the element `mu` of
`A_inf`. It satisfies `φ t = p t` and `g t = χ(g) t` for all `g` in `G_p = Gal(Q̄_p/Q_p)`, where `χ`
is the p-adic cyclotomic character.

The element `t` plays the role of Fontaine's period `t`, up to the factor `p`. 

### `tPeriodAmax`

 A chosen element `t` of `Amax` with the three properties of `exists_tPeriod`. These properties
are unchanged when `t` is multiplied by a unit of `ℤ_[p]`, so they do not fix a normalisation. 

### `associated_mu_mul_p_tPeriodAmax`

 In Colmez's ring `Amax` (A_max), the product of μ = [ε] − 1 (the Teichmüller lift of ε minus
one) with p is associated to the chosen period `tPeriodAmax`. That is, `mu * p` equals `tPeriodAmax`
times a unit of `Amax`. 

### `smul_tPeriodAmax`

 For every `g` in the absolute Galois group G_p of Q_p, `g` acts on the chosen period
`tPeriodAmax` in `Amax` by multiplication by χ(`g`) ∈ ℤ_p, where χ = `cyclotomicGp` is the p-adic
cyclotomic character. 

### `tPeriod`

 The image of `tPeriodAmax` in `B_dR⁺`. It plays the role of `p` times Fontaine's period `t`. 


## The field B_dR, the embedding of Q̄_p, and the fundamental sequence

The de Rham period field and its relation to the crystalline ring. Notation:
B⁺ = `New.Period.BPlus`, B = B⁺[1/μ] = `New.Period.Bmax`, B_dR⁺ = `New.Period.BdRPlus` (the ξ-adic
completion of B⁺), with θ : B_dR⁺ → ℂ_p (`New.Period.thetaBdR`) and the Frobenius φ on B
(`New.Period.frobEnd`).


 ### The Galois action on B_dR⁺ and the field B_dR 

### `actBdRPlus`

 `G_p` acts on `B_dR⁺`. 

### `BdR`

 The de Rham period field B_dR, defined as the fraction field of the ring B_dR⁺. 

### `actBdR`

 `G_p` acts on `B_dR`. 

### `instance : Algebra Bmax BdR`

 `B = B⁺[1/μ]` maps to `B_dR`, since `μ` is nonzero in the field `B_dR`. 

### `instance : Algebra (PadicAlgCl p) BdRPlus`

 The embedding of `Q̄_p` in `B_dR⁺`: `Q̄_p` is formally étale over `ℚ_p`, so its map to
`B⁺/ξ ≃ ℂ_p` lifts to the `ξ`-adic completion `B_dR⁺`. 

### `BdRPlus.associated_xi_tPeriod`

 In B_dR⁺ the period t (`tPeriod`) equals ξ times a unit.

This is Fontaine's result that the period t is a uniformiser of B_dR^+, in the form that t and ξ
agree up to a unit. 

### `smul_tPeriod`

 For every `g` in the absolute Galois group G_p of Q_p, `g` acts on `tPeriod` by multiplication
by χ(`g`) ∈ ℤ_p, where χ = `cyclotomicGp` is the p-adic cyclotomic character. Here `tPeriod` is the
image of `tPeriodAmax` in B_dR⁺, which plays the role of p times Fontaine's t. 

 ### θ, the embedding of Q̄_p, and the fundamental sequence 

### `thetaBdR_algebraMap_padicAlgCl`

 For x in Q̄_p, the map θ: B_dR⁺ → ℂ_p sends the image of x in B_dR⁺ to x itself, viewed in
ℂ_p. 

### `BdR.smul_algebraMap_padicAlgCl`

 The embedding of Q̄_p in B_dR is G_p-equivariant: g applied to the image of x is the image of
g(x).

This is the G_p-equivariance of the embedding of Q̄_p in B_dR^+ (Caruso; Brinon–Conrad), stated
after passing to the field B_dR. 

### `isUnit_coe_Bmax_of_dvd_mu`

 An element of `A_inf` that divides `μ` becomes a unit in `B = B⁺[1/μ]`. 

### `Bmax.exists_coe_eq_sub`

 For every `β` in `B_dR` there are `y` in `B` and `x` in `B_dR⁺` with `x = y - β` in `B_dR`:
every element of `B_dR` is congruent modulo `B_dR⁺` to an element of `B`. 

### `Bmax.exists_frobEnd_sub_eq_and_coe_eq`

 For every `a` in `B` there is `y` in `B` with `φ y - y = a` whose image in `B_dR` is the image
of some `x` in `B_dR⁺`: the map `φ - 1` sends `B ∩ B_dR⁺` onto `B`. 

### `Bmax.fundamental_sequence_surjective`

 Surjectivity in the fundamental exact sequence: for a in B and β in B_dR there is y in B
with φ(y) − y = a and y − β in B_dR⁺. 
