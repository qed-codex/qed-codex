---
{
  "module": "src/Lib/PadicHodge/TateSen.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/TateSen.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/TateSen.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tate's vanishing theorem, Hodge–Tate elimination and the filtration of B_dR

Let `χ` be the cyclotomic character `New.cyclotomicGp` of `New.Gp p = Gal(ℚ̄_p/ℚ_p)`, where the
class `[ThePrime p]` says that `p` is prime. The file also defines the filtration tⁿ B_dR⁺ of the de
Rham period field B_dR = `New.Period.BdR`.

## Main definitions and results

* `New.Period.tate_eq_zero_of_cyclotomicGp_twist`: the only `x` in `ℂ_p` with
  `χ(g) ^ u g x = χ(g) ^ v x` for all `g` near `1` is `0` when `u ≠ v`.
* `New.Period.le_of_hodgeTate_stable`: for a subspace of `ℂ_p ^ ι` stable under the Galois action
  twisted by `χ ^ u i` in the coordinate `i`, the vectors of minimal support can be taken algebraic,
  fixed and supported on one weight, by the theorems of Tate and Ax.
* `New.Period.hodgeFil`: the step tⁿ B_dR⁺, with t = `New.Period.tPeriod` a uniformiser of the
  discrete valuation ring B_dR⁺ = `New.Period.BdRPlus`, on which g acts by g t = χ(g) t
  (`New.Period.smul_tUnit_zpow`).
* `New.Period.forall_smul_eq_iff_mem_localFieldOf`: an open subgroup fixes in ℂ_p exactly its fixed
  field K in Q̄_p.
* `New.Period.BdR.exists_sub_mem_of_smul_sub_mem`: an element of B_dR that is invariant modulo a
  B_dR⁺-submodule S is congruent modulo S to an element of K; S = 0 gives the invariants of B_dR.

Notions from other files:
* `New.Period.OverGp`, `New.Period.localFieldOf Γ`: a homomorphism j = `toGp` from a group `Γ` to
  `New.Gp p` with open image, and the subfield of Q̄_p fixed by that image.

## Relation to the literature

Known result: The Ax–Sen–Tate theorem and Tate's vanishing of the invariants of C_p(i). Ax's theorem
is not proved in this file; it comes from an imported file, as `ax_mem_closure_fixedField` and
`exists_algebraic_of_fixed_near_one`, without the constant. Tate's theorem is stated for H⁰ only, on
any open subgroup, and is proved from the boundedness of the normalised trace to Q_p. A consequence
is that invariants of B_dR modulo a submodule come from the base field. Source: J. Ax, Zeros of
polynomials over local fields: the Galois action, J. Algebra 15 (1970); J. Tate, p-divisible groups
(1967), §3; proofs in Fontaine–Ouyang 3.3-3.5 and Brinon–Conrad §14.

See also `Lib.PadicHodge.Crystalline.Regularity` and `Lib.PadicHodge.PeriodRings.DeRhamPeriods`.


 ## Tate's vanishing theorem for cyclotomic twists of ℂ_p 

### `New.Period.exists_norm_normalizedTrace_le_of_pow_eq_one`

 There is a positive constant `C` bounding the normalised trace to `ℚ_p` of every root of unity
of `p`-power order in `Q̄_p`. The traces of the `p`-th roots of unity are bounded, as there are
finitely many; for any other root of order `p ^ (n + 1)` the trace vanishes. 

### `New.Period.exists_sum_smul_sub_one_pow_eq`

 An element of `Q̄_p` fixed by the stabilizer of a primitive root of unity `ζ` of order
`p ^ (n + 1)` is a `ℚ_p`-combination of the powers `(ζ - 1) ^ i` with `i` below
`(p ^ (n + 1)).totient`: the polynomial `Φ(X + 1)` is monic of that degree and kills `ζ - 1`. 

### `New.Period.exists_norm_normalizedTrace_le`

 Tate: there is a constant C, depending only on p, such that every z in Q̄_p fixed by the
kernel of the cyclotomic character, that is z in Q_p(μ_{p^∞}), has normalised trace to Q_p
of absolute value at most C·|z|. 

### `New.Period.eq_zero_of_smul_eq_cyclotomicGp_zpow_smul`

 Tate's theorem for the whole group: `ℂ_p` has no nonzero vector on which `Gal(ℚ̄_p/ℚ_p)` acts
through a nonzero power of the cyclotomic character. 

### `New.Period.tate_eq_zero_of_cyclotomicGp_twist`

 Tate's theorem: if `χ(g) ^ u • g • x = χ(g) ^ v • x` for all `g` near `1` in `Gal(ℚ̄_p/ℚ_p)`,
with `χ` the cyclotomic character and integers `u ≠ v`, then `x = 0` in `ℂ_p`. This is
`H⁰(U, ℂ_p(u - v)) = 0` for every open subgroup `U`, as the relation is asked only near `1`. 


## Elimination by vectors of minimal support

Elimination: a submodule `W` of a free module is contained in `W'` as soon as `W'` contains enough
vectors of `W` of minimal support.

* `New.Period.le_of_echelon`: the linear algebra, by induction on the support.


### `New.Period.le_of_echelon`

 Let `b` give coordinates on `V`. Suppose that for each nonzero `v ∈ W` to which all vectors of
`W` supported within `v` are proportional, some `u ∈ W ⊓ W'` supported within `v` has a
coordinate equal to `1`. Then `W ≤ W'`. 

### `New.Period.le_of_hodgeTate_stable`

 Let `ι` be finite and let `F` be a filter on `Gal(ℚ̄_p/ℚ_p)` with `nhds 1 ≤ F` (`hF`). Let the
subspace `W` of `ℂ_p ^ ι` be stable along `F` under `a ↦ (χ(g) ^ u i • g • a i)ᵢ` (`hW`). Suppose
that `W'` contains every vector `a` of `W` with coordinates in `ℚ̄_p` such that, for some `k`,
(a) `‖a i‖ ≤ 1`, (b) `a i = 0` whenever `u i ≠ u k`, (c) `a k = 1` and (d) each `a i` is fixed
along `F` (`h_pure`). Then `W ≤ W'`. 


## The filtration of B_dR and its Galois invariants

The relevant subgroup of `Gal(ℚ̄_p/ℚ_p)` is the image of `j = toGp : Γ → Gp p`, and K is
`New.Period.localFieldOf Γ`.


### `forall_smul_eq_iff_mem_localFieldOf`

 Ax–Sen–Tate: if `j : Γ → G_p` has open image, an element of `ℂ_p` is fixed by every `j(g)` if
and only if it lies in the subfield `K` of `ℚ̄_p` fixed by that image. 

### `prime_tPeriod`

 The period `tPeriod` is a prime element of B_dR⁺: it is associated to the prime `ξ = xi` of
B_dR⁺, which divides exactly the `y` with `thetaBdR y = 0`. 

### `tUnit`

 The period `tPeriod` as a unit of the field `B_dR`. 

### `hodgeFil`

 The step `tⁿ B_dR⁺` of the filtration of B_dR, a B_dR⁺-submodule, for any integer `n`. 

### `hodgeFil_anti`

 The filtration decreases: `tⁿ B_dR⁺ ≤ tᵐ B_dR⁺` for `m ≤ n`. 

### `mul_mem_hodgeFil`

 The filtration is multiplicative: `tᵐ B_dR⁺ · tⁿ B_dR⁺ ⊆ tᵐ⁺ⁿ B_dR⁺`. 

### `algebraMap_mem_hodgeFil_iff_xi_pow_dvd`

 An element `y` of B_dR⁺ lies in `tᴹ B_dR⁺` if and only if `ξ ^ M` divides `y`, where `ξ = xi` is
the prime of B_dR⁺ dividing exactly the kernel of `thetaBdR`. 

### `algebraMap_mem_hodgeFil_one_iff`

 An element `y` of B_dR⁺ lies in `t B_dR⁺` if and only if its residue `θ(y)` vanishes. 

### `coe_mem_hodgeFil_iff`

 An element of Q̄_p lies in every step `n ≤ 0` of the filtration, and in a step `n > 0` only if
it is zero. 

 ### Galois action and invariants 

### `smul_tUnit_zpow`

 An element `g` of `G_p` acts on `tᵏ` by `χ(g) ^ k`, for every integer `k`. 

### `BdR.exists_sub_mem_of_smul_sub_mem`

 Let `j = toGp : Γ → Gal(ℚ̄_p/ℚ_p)` have open image (`OverGp Γ p`, `p` prime) and let
`K = localFieldOf Γ` be the subfield of `ℚ̄_p` fixed by `j(Γ)`. If `x ∈ B_dR` and `j(g) • x - x`
lies in the B_dR⁺-submodule `S` of B_dR for every `g`, then `x - a ∈ S` for some `a ∈ K`. This is a
B_dR form of the Ax–Sen–Tate theorem; the case `S = 0` says that every element of B_dR fixed by
`j(Γ)` lies in `K`. 
