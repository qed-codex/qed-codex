---
{
  "module": "Zeta23/PrimeSideA/EndsE1.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/EndsE1.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/EndsE1.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23 — [lem:ends], bound for 𝓔₁ (§5.3).  Statement `calE1_bound` consumed by
Zeta23/PrimeSideA/Ends.lean.

ROUTE.  On I×I: |ν|,|ν'| ≤ B;  |K + K_∞| ≤ 2L² (abs_Kfun_le, abs_Kinf_le);
|K_∞ − K| ≤ (s ρ(τ) + ρ(τ')/s)/2 for every s > 0 (abs_Kinf_sub_Kfun_le), with the choice
s := g(τ')/g(τ), g(τ) := (1 + min(τ−T, 2T−τ))⁻² > 0.  Hence pointwise
  |K²−K_∞²||ν||ν'| ≤ L²B² ( ρ(τ)/g(τ)·g(τ') + g(τ)·ρ(τ')/g(τ') )
and integrating over I×I (product structure):  |𝓔₁| ≤ 2L²B² (∫_I ρ/g)(∫_I g),  ∫_I g ≤ 2.
Pointwise majorant (finite partial sums of the HasSum for ρ, ψ antitone, grid lemma):
  ρ(τ) ≤ W(τ−T) + W(2T−τ) + ψ(τ_d − τ)²,   W(Δ) := ψ(Δ)² + h⁻¹∫_{(Δ,∞)}ψ²,
and 1/g = (1+min(τ−T,2T−τ))² ≤ (1+(τ−T))², (1+(2T−τ))², (1+h+|τ_d−τ|)² respectively, so
  ∫_I ρ/g ≤ 2∫_0^T W(u)(1+u)² du + ∫_ℝ ψ(r)²(2+|r|)² dr ≪ L² + L·l   (split at 1; ψ ≤ L,
  ψ(r) ≤ (c/w)/r², ∫_{(Δ,∞)}ψ² ≤ min(8L, (c/w)²/(3Δ³)), log T ≤ 2l).
Budget: |𝓔₁| ≤ C(c_ϱ)·L²B²(L² + L l) ≤ C·L³B² l (L = λl ≤ l).
-/
```

 ### Definitions 

### `Wfun`

 `W(Δ) := ψ(Δ)² + h⁻¹ ∫_{(Δ,∞)} ψ²`. 

### `distB`

 distance to the boundary of `I = [T,2T]` (for τ ∈ I): `min(τ−T, 2T−τ)`. 

### `gwt`

 the weight `g(τ) := (1 + min(τ−T,2T−τ))⁻²` (only used for τ ∈ I, where it is in (0,1]). 

 ### Leaf integrals 

### `setIntegral_gwt_le`

 (Ig) `∫_I g ≤ 2`. 

### `antitone_setIntegral_psiA_sq_Ioi`

 J(u) := ∫_{(u,∞)} ψ² is antitone in u (ψ² ≥ 0). 

### `W1c`

 (W1c) ∫_0^1 J(u)(1+u)² du ≤ 32L, J(u) := ∫_{(u,∞)}ψ² ≤ 8L. 

### `W1d`

 (W1d) ∫_1^T J(u)(1+u)² du ≤ (4/3)(c/w)² log T: J(u) ≤ (c/w)²/(3u³) and (1+u)² ≤ 4u² on [1,T]. 

### `W3`

 (W3) the stray term: `∫_ℝ ψ(r)²(2+|r|)² dr ≤ 18L² + 18(c/w)²`, with integrability. 

 ### Pointwise facts on I 

### `abs_nuX_le_B_onI`

 on I the log⁺ term of [eq:Bdef] vanishes: `|ν(τ)| ≤ B`. 

### `majK1`

 the 𝓔₁ majorant kernel with its ν-weights (on `I×I`):
`L²·(ρ(τ)/g(τ)·g(τ') + g(τ)·ρ(τ')/g(τ'))·|ν(τ)||ν(τ')|`,  g = gwt. 

### `abs_E1integrand_le_majK1`

 pointwise: `|K²−K∞²|·|νν'| ≤ majK1` on `I×I` (weighted AM–GM; ν-free kernel). 

### `majK1_le`

 `majK1 ≤ L²B²·(ρ/g·g' + g·ρ'/g')` on `I×I` when `|ν| ≤ B` there. 

### `abs_E1integrand_le`

 pointwise bound for the 𝓔₁-integrand on `I×I`. 

 ### The majorant for ρ on I 

### `tau_d_gt`

 `τ_d = T + d h > 2T − h` (since `d = ⌊T/h⌋`). 

### `sum_le_sum_range_of_injOn`

 generic: a finite sum dominated termwise by a grid function is ≤ the grid sum over a range. 

### `h_le_one`

 `h ≤ 1` (as `L ≥ 8 > 2π`). 

### `rho_le_majorant`

 **Pointwise majorant**: for τ ∈ I,
`ρ(τ) ≤ W(τ−T) + W(2T−τ) + ψ(τ_d − τ)²`. 

 ### The weight integrals 

### `setIntegral_rho_div_gwt_le`

 `∫_I ρ/g ≤ 2[W1a+W1b+h⁻¹(W1c+W1d)] + W3`-type bound:  `∫_I ρ(τ)(1+min(τ−T,2T−τ))² dτ ≤ RHS`. 

 ### Assembly 

### `calE1_maj_bound`

 **Majorant bound behind 𝓔₁**: ∬_{I×I} majK1(ν) ≤ C·L³B²·l for T ≥ T₀. 

### `calE1_maj_bound_L`

 **Majorant bound behind 𝓔₁, L-intrinsic form** (no bandwidth cap):
∬_{I×I} majK1(ν) ≤ C·L³B²·(L + l) for T ≥ T₀ (l = log(T/2π) carries the genuine log T). 

### `abs_calE1_le_maj`

 `|𝓔₁(ν)| ≤ ∬_{I×I} majK1(ν)`. 

### `calE1_bound`

 **Bound for 𝓔₁** (cf. §5.3): `|𝓔₁| ≤ C · L³ B² l` for `T ≥ T₀` (corollary). 
