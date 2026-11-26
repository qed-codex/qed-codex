---
{
  "module": "src/Lib/PadicHodge/RadiusLemma.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/RadiusLemma.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/RadiusLemma.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The radius lemma: after Frobenius a frame is a constant basis times a unit over A

The radius lemma for a chart (`New.Lift.Chart`): a subring S of A_inf, the image of Λ⟦X⟧, where
Λ = W(𝔽_{p^𝔣}) are the constants; the image z of X is a Teichmüller lift, and E = z^e·(unit) + p is
an associate of ξ. Further A = `New.Period.Amax`, B⁺ = A[1/p] = `New.Period.BPlus`, φ is the
Frobenius, and t is a Galois element with `c.FixesThetaZ t`.

* `New.Lift.Chart.exists_E_pow_mul_eq_tau_pow_mul_iff`: A_inf[1/τ] ∩ S_B[1/E] = S.
* `New.Lift.Chart.tau_mul_z_dvd_smul_sub`: τz divides ty − y in B⁺ for every y in S_B.
* `New.Lift.Chart.radius_lemma`: if tz = [ε]z, Z has entries in S_B with Z'·Z = E^h and tZ = Z·G for
  some G over A_inf, and 3e ≤ p^l, then φ^l(Z) = φ^l(E)^b·C·V with C constant and V invertible over
  A (`New.Lift.Chart.IsRadiusFactorization`).

Notions from other files:
* `New.Period.tau`, `New.Period.mu`, `New.Period.xi`: the elements τ = [ε^{1/p}] − 1, μ = [ε] − 1
  and ξ of A_inf, with ξτ = μ; `New.Period.theta` is Fontaine's map θ : A_inf → O_C.
* `New.Lift.Chart.ainfToBPlus`: the structure ring homomorphism from A_inf to B⁺.
* `New.Lift.Chart.bicommutant`: the S-subalgebra S_B of the y in B⁺ whose multiplication commutes
  with every S-linear endomorphism of B⁺ that preserves the image of A. It contains p⁻¹ and is the
  p-adic closure of S[E/p] with p inverted (`New.Lift.Chart.adjoinEDivPClosure_eq_bicommutant`).
* `New.Lift.Chart.FixesThetaZ`: `c.FixesThetaZ t` says that t fixes the constants Λ and θ(z).

## Relation to the literature

Known result: Dwork's trick, giving an integral crystalline comparison with a uniform denominator.
Here `radius_lemma` gives φ^l(Z) = φ^l(E)^b·C·V, with C fixed by every g that fixes Λ and V
invertible over A_max. Whenever e·A ≤ p^l·δ, the y with Vy natural modulo E^A span at least
p^{4δ}S^d.
Source: M. Kisin, Crystalline representations and F-crystals, Progr. Math. 253 (2006), Lemma 1.2.6;
M. Kisin, Potentially semi-stable deformation rings, JAMS 21 (2008), Lemma 2.2; B. Bhatt,
P. Scholze, Prismatic F-crystals and crystalline Galois representations (2023), proof of Thm 5.6.

See also `Lib.PadicHodge.Kisin.PeriodMatrixFrame`.


### `exists_E_dvd_xi_sub_p_mul`

 `E` divides `xi - p * b` for some `b` in `Ainf` (for `b = 0`, as `E` and `xi` are
associates). 

### `sub_padicValNat_factorial_add_two_eq`

 The identity `n - v_p(n!) + 2 = (n + 1 - v_p((n + 1)!)) + v_p(n + 1) + 1` of `p`-adic
valuations, from `v_p((n + 1)!) = v_p(n + 1) + v_p(n!)` and `v_p((n + 1)!) ≤ n + 1`. 

### `tau_dvd_of_dvd_E_pow_mul`

 If `tau` divides `E ^ h * a` in `BPlus`, for `a` in `Ainf`, then `tau` divides `a` in
`Ainf`. 

### `tau_pow_mul_z_pow_dvd_of_dvd_E_pow_mul`

 Let `c` be a chart with z = `c.z` and E = `c.E` (the image in A_inf of the series
X^e·(unit) + p, ξ times a unit), and let τ = [ε^{1/p}] − 1. If τ^m·z^n divides E^h·a in `BPlus`,
for a in `Ainf`, then τ^m·z^n divides a in `Ainf`. 

### `tau_mul_z_pow_dvd_of_dvd_E_pow_mul`

 If `tau * z ^ n` divides `E ^ h * a` in `BPlus`, for `a` in `Ainf`, then it divides `a`
in `Ainf`. 

### `tau_pow_dvd_of_dvd_E_pow_mul`

 Let `tau` be the element τ = [ε^{1/p}] − 1 of `Ainf` = W(O^♭), the Witt vectors of the tilt of
O_{C_p}. Let `c` be a chart, with the image `c.S` of Λ⟦X⟧ in `Ainf`, and let `c.E` be its element
of `c.S` that is ξ times a unit, seen in `Ainf`. If the image of `tau ^ m` under the structure map
`ainfToBPlus : Ainf → BPlus` divides the image of `c.E ^ h * a`, for some `a` in `Ainf`, then
`tau ^ m` already divides `a` in `Ainf`. 

### `mem_S_of_E_pow_mul_mem_bicommutant`

 Let `c` be a chart with ring S = `c.S` (the image of Λ⟦X⟧ in A_inf), E = `c.E` and
S_B = `c.bicommutant` (the p-adic closure of S[E/p] in `BPlus`, with p inverted). If E^h·a lies in
S_B, for a in `Ainf`, then a lies in S. 

### `exists_E_pow_mul_eq_tau_pow_mul_iff`

 The equality A_inf[1/τ] ∩ S_B[1/E] = S, with denominators cleared. Let `c` be a chart with ring
S = `c.S` (the image of Λ⟦X⟧ in A_inf), E = `c.E` and S_B = `c.bicommutant` (the p-adic closure of
S[E/p] in `BPlus`, with p inverted), and let τ = [ε^{1/p}] − 1. For a in `Ainf`, the fraction a/τ^m
equals y/E^h for some h and some y in S_B if and only if a = τ^m·s for some s in S. 

### `frobEnd_pow_ainfToBPlus`

 `φ ^ l` on `BPlus` restricts on `S` to the Frobenius `c.φ ^ l` of the chart. 

### `frobEnd_pow_ainfToBPlus_z`

 `φ ^ l` raises `z`, a Teichmüller lift, to the power `p ^ l`. 

 ### The action of t and the radius lemma 

### `tau_mul_z_dvd_smul_sub`

 Let `c` be a chart with z = `c.z` and S_B = `c.bicommutant`, let τ = [ε^{1/p}] − 1, and let
t ∈ G_p fix Λ and θ(z) (`c.FixesThetaZ t`). Then τ·z divides t•y − y in `BPlus` for every y in
S_B. 

### `exists_z_pow_eq`

 `p` divides `xi`, hence `E` and `z ^ e`, in `Amax`; so `p ^ n` divides `z ^ N` there for
`e * n ≤ N`. 

### `exists_p_pow_mul_ev_eq_add_z_pow_mul`

 Truncation of a power series at order `D`, evaluated at `X = z ^ N / p ^ 2`: after clearing the
denominator `p ^ (2 * D)` the truncation lies in `S` and the tail is a multiple of `z ^ (N * D)`. 

### `extendedCoord_oneIndex_ev`

 Values of `ev` at `X = z ^ N / p ^ 2` are fixed by the projection onto `S_B`. 

### `natCongruentSet`

 The vectors `y` over `S` for which `M y` is congruent modulo `E ^ A` to a vector with entries
in `ℕ`. 

### `pow_smul_mem_span_of_unit`

 Let `ev` evaluate at `X = z ^ N / p ^ 2` with values in `Amax`, and let `V` be a unit over
`S⟦X⟧`. For `e * A ≤ N * δ`, the `y` with `ev V y` congruent to a vector in `ℕ ^ d` modulo `E ^ A`
span a submodule that contains `p ^ (4 * δ) • S ^ d`. 

### `exists_ainfToBPlus_eq_p_pow_mul_sub_z_mul`

 One step of the radius lemma. Let `c` be a chart with z = `c.z`, S = `c.S` and
S_B = `c.bicommutant`, and let t ∈ G_p fix Λ and θ(z) (`c.FixesThetaZ t`) with t•z = [ε]z. Let Y
over B⁺ and G over A_inf satisfy t•Y = YG with τ·z dividing every entry of G − 1
(τ = [ε^{1/p}] − 1), fix a row index i, q, n ∈ ℕ and a row W over S_B, and suppose q•Y_i − z^{n+1}·W
is the image of a row over A_inf. Then each entry p^{v+1}·W_j lies in S + z·S_B, where v is the
p-adic valuation of n + 1. 

### `exists_ev_eq_frobEnd_pow`

 Let `c` be a chart with z = `c.z`, S = `c.S` and S_B = `c.bicommutant`, and let t ∈ G_p fix Λ
and θ(z) (`c.FixesThetaZ t`) with t•z = [ε]z. Let `ev` : S⟦X⟧ → B⁺ be an S-algebra map with
z^{p^l} = p²·ev(X) and z ∣ ev(X). Let Y, W be matrices over B⁺ and G a matrix over A_inf with
t•Y = YG, with τ·z dividing every entry of G − 1 (τ = [ε^{1/p}] − 1), W over S_B and Y = 1 + z·W.
Then every entry p²·φ^l(W_ij), with φ = `frobEnd`, equals ev(f) for some f ∈ S⟦X⟧. 

### `exists_algHom_z_pow_eq_p_pow_two_mul`

 For `3 * e ≤ p ^ l` there is an `S`-algebra map `ev₀ : S⟦X⟧ → Amax` with
`z ^ (p ^ l) = p ^ 2 * ev₀ X` in `BPlus`: it evaluates at `X = p * T`, where
`z ^ (p ^ l) = p ^ 3 * T` with `T` in the `p`-adically complete ring `Amax`. 

### `exists_mul_eq_one_add_z_smul`

 Let `Z` be a matrix over `S_B` with `Z' * Z = E ^ h`. Then there are a matrix `B` over `BPlus`
whose entries are fixed by every `g` that fixes the constants Λ, and a matrix `W` over `S_B`, with
`B * Z = 1 + z • W`. 

### `IsRadiusFactorization`

 The conclusion of the radius lemma for a matrix `Z` over `BPlus`, exponents `l` and `b`, a
matrix `V` invertible over `Amax` and a matrix `C` over `BPlus`. 

### `IsRadiusFactorization.smul_C_eq`

 Every `g` in `G_p` that fixes the constants Λ fixes `C`. 

### `IsRadiusFactorization.map_frobEnd_eq`

 After `l` Frobenius steps, `Z` is `φ ^ l (E) ^ b` times `C * V`. 

### `IsRadiusFactorization.pow_smul_mem_span`

 For `e * A ≤ p ^ l * δ`, the `y` with `V y` natural modulo `E ^ A` span at least
  `p ^ (4 * δ) • S ^ d`. 

### `radius_lemma`

 Radius lemma. Let t fix the image of Λ = W(F_{p^f}) in A_inf and θ(z), with z the chart
coordinate (`c.FixesThetaZ`), and let tz = [ε]z. Let Z be a matrix over S_B (`c.bicommutant`) with
Z′Z = E^h and tZ = ZG for some G over A_inf, and let 3e ≤ p^l and b ∈ ℕ. Then there are V invertible
over `New.Period.Amax` and C over B⁺ with `IsRadiusFactorization`: C is fixed by every g that fixes
Λ, φ^l(Z) = φ^l(E)^b·C·V, and, whenever e·A ≤ p^l·δ, the y with Vy natural modulo E^A span at least
p^{4δ}S^d. 
