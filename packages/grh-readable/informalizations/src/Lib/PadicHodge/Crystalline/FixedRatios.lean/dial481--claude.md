---
{
  "module": "src/Lib/PadicHodge/Crystalline/FixedRatios.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Crystalline/FixedRatios.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Crystalline/FixedRatios.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounded poles, φ-fixed elements of B_max, and ratios of periods fixed near 1

The period ring `B = B⁺[1/μ]` (`New.Period.Bmax`, `New.Period.BPlus`) lies inside `B_dR`, and `φ`
denotes its Frobenius. This file shows that bounded poles of the `φ^n y` control the denominators
of `y` in `μ`, and that a `φ`-fixed element of `B` lying in `B_dR⁺` is in `ℚ_[p]`. Using charts
(`New.Lift.Chart`), it shows that a ratio of two periods that is fixed by an open subgroup of `G_p`
lies in `W(𝔽_q)[1/p]` for some `q`.

## Main definitions and results

* `New.Period.pow_smul_mem_range_BPlus`: if the image of `φ^n(y)` in `B_dR` lies in
  `t^(−a)B_dR⁺` for every `n ≥ 0`, then `ν^a y` lies in the image of `B⁺` for every `ν` in `A_inf`
  divisible by `μ`.
* `New.Period.Bmax.exists_padic_eq_of_frobEnd_fixed`: kernel in the fundamental exact sequence: an
  element `y` of `B` with `φ(y) = y` whose image in `B_dR` lies in `B_dR⁺` belongs to `ℚ_[p]`.
* `New.Period.exists_pow_mul_eq_wittFq_mul_of_isChartOf`, `New.Period.Bmax.exists_witt_ratio`: a
  ratio of two periods that is fixed by an open subgroup of `G_p` lies in `W(𝔽_q)[1/p]` for some
  `q`, for a given chart and in general.

Notions from other files:
* `New.Period.BdRPlus`: the ξ-adic completion of B⁺, with fraction field `New.Period.BdR`.
* `New.Period.BPlus`, `New.Period.Bmax`: B⁺ = A_max[1/p] and B = B⁺[1/μ], μ = [ε] − 1.
* `New.Lift.Chart.bicommutant`: the S-algebra S_B of the y in B⁺ whose multiplication commutes with
  every S-linear endomorphism of B⁺ that keeps the image of A_max.

## Relation to the literature

Known; see `Lib.PadicHodge.Crystalline.Regularity` for sources.


 ## Bounded poles and φ-fixed elements of B in B_dR⁺ 

### `pow_smul_mem_range_BPlus`

 Let y ∈ B, a ∈ ℕ, and let ν ∈ A_inf be divisible by μ. If the image of φ^n(y) in B_dR lies
in t^(−a)B_dR^+ for every n ≥ 0, then ν^a y lies in the image of B^+.

Here φ^n(y) is the action of `(ofAdd n, 1)` in `FrobGal`, and `hodgeFil (-a)` is t^(−a)B_dR^+. 

### `Bmax.exists_padic_eq_of_frobEnd_fixed`

 Kernel in the fundamental exact sequence: an element y of B with φ(y) = y whose image in
B_dR lies in B_dR^+ belongs to Q_p. 


## Regularity of the period ring B

A chart (`New.Lift.Chart`) is a map `W(𝔽_q)⟦X⟧ → A_inf` with image `S = c.S`, sending `X` to
`z = c.z`. For `j : Γ → G_p`, `c.IsChartOf j` says that every `g` in `G_p` that fixes `θ(S)`
pointwise lies in `j Γ`. `c.extendToBPlus f` extends an `S`-linear map `f` of `A_inf` to `B⁺`,
linearly over `c.bicommutant`. `New.Period.localFieldOf Γ` is the subfield of `Q̄_p` fixed by `j Γ`,
and `New.Lift.WittFq f` is `W(𝔽_{p^f})`.


### `exists_pow_dvd_sub_of_separable`

 Newton's iteration: if `x` is a root of a separable polynomial over `K` and lies in the image
of `T` modulo `π`, then it lies in the image of `T` modulo every power of `π`. 

### `Lift.Chart.IsChartOf.dvd_extendToBPlus`

 Let `c` be a chart for `toGp` (`hc`): `c` is a Λ-algebra map Λ[[X]] → A_inf sending X to a
Teichmüller lift z, and every g in G_p fixing Λ pointwise and fixing θ(z) lies in the image of
`toGp`. Let `a l` be finitely many elements of the field fixed by `toGp Γ`, `y l ∈ B⁺`, and `f` a
`c.S`-linear endomorphism of `A_inf`, with chosen `c.S`-linear extension `c.extendToBPlus f` to
`B⁺`. Then `∑ l, a l * y l` divides `∑ l, a l * c.extendToBPlus f (y l)` in `B_dR⁺`. In particular
the second sum vanishes if the first does. 

### `isUnit_of_isIntegral_eq_mul`

 If a nonzero `x` algebraic over the field `K ⊆ R` equals `z * v` with `z` in `R` and `v`
integral over `R`, then `z` is a unit of `R`. 

### `Lift.Chart.IsChartOf.extendedCoord_eq_mul_of_eq_mul`

 Let `c` be a chart for `j = 𝒥.toGp`, let `a` lie in the field fixed by `j Γ`, and let
`B, C ∈ B⁺` satisfy `B = a C` in `B_dR`. Then the `i`-th extended coordinates of the chart satisfy
the same relation: `extendedCoord i B = a * extendedCoord i C` in `B_dR`. 

### `Period.exists_pow_mul_eq_wittFq_mul_of_mul_eq`

 Let `b, b' ∈ B` and `α ∈ B_dR` with `b = α b'` in `B_dR`, and let `w₀, w₁ ∈ W(𝔽_{p^f})` with
`w₁ ≠ 0` and `α w₁ = w₀`. Then `p ^ r b = w b'` for some `r` and some `w ∈ W(𝔽_{p^f})`. 

### `Lift.Chart.exists_wittFq_mul_eq_of_eq_mul`

 Let `γ 0, γ 1` lie in `c.bicommutant`, not both divisible by `z = c.z`, with `γ 0 = a γ 1` in
`B_dR` for some `a ∈ Q̄_p`. Here `c.bicommutant` is the ring S_B of elements of `B⁺` commuting with
every `c.S`-linear map of `B⁺` that keeps the image of A_max, and `z` is the image of `X` under the
chart. Then `a w₁ = w₀` in `B_dR` for some `w₀, w₁ ∈ W(𝔽_{p^f})`, `f = c.f`, with `w₁ ≠ 0`. 

### `Period.exists_pow_mul_eq_wittFq_mul_of_isChartOf`

 Let `j = 𝒥.toGp : Γ → G_p` have open image, and let `c` be a chart for j (`c.IsChartOf`: every g
that fixes θ(S) pointwise lies in j Γ), S the ring of the chart over W(F_{p^f}), f = `c.f`. If b,
b' ∈ B, b' ≠ 0 and g(b)b' = b·g(b') for all g in Γ, then p^m b = wb' for some m and some
w ∈ W(F_{p^f}).

Part of Fontaine's theorem on Galois invariants of the fraction field of the crystalline period
ring: only the nontrivial inclusion, with denominators cleared. 

### `Period.Bmax.exists_witt_ratio`

 If a, b ∈ B, b ≠ 0 and g(a)b = a·g(b) for all g near 1 in G_p, then p^n a = wb for some n, some
f and some w ∈ W(F_{p^f}).

A form of Fontaine's computation of the Galois invariants of the fraction field of the crystalline
period ring: a quotient a/b fixed by all g near 1 lies in W(F_{p^f})[1/p] for some unspecified
degree f. 
