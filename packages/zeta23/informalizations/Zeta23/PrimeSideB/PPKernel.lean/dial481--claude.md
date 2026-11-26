---
{
  "module": "Zeta23/PrimeSideB/PPKernel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideB/PPKernel.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideB/PPKernel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization of the paper
"More than two thirds of the zeros of the Riemann zeta function lie on the critical line".
-/
```


# Kernel lemmas for [prop:PP] (§5.4)

Pure measure-theory / trigonometric-integral / H-MV-application lemmas used by
`Zeta23/PrimeSideB/PP.lean`.

* `sqIntegral_shear`: the substitution `τ = τ' + x` on the square `I×I` (§5.4).
* `intervalIntegral_cos_linear*`: `∫_α^β cos(θt + c) dt` closed forms and the bound `2/|θ|` (§5.4).


 ## Elementary facts about the index range `primeRange X = Finset.Ioc 0 ⌊X⌋₊` 

### `acoef_sq`

 a_n² = Λ(n)²/n (§5.4). 

### `acoef_sq_mul_two_mul`

 2n·a_n² = 2Λ(n)² — the MV weight with δ_n = 1/(2n) [eq:deltan]. 

### `acoef_one`

 Λ(1) = 0, so a_1 = 0: terms with n = 1 never contribute. 

 ## The shear `(τ,τ') ↦ (x,τ') = (τ−τ',τ')` on `I × I`  (§5.4) 

### `shearHomeo`

 The shear `(x, τ') ↦ (x + τ', τ')` of `ℝ²` as a homeomorphism (its inverse is
`(τ, τ') ↦ (τ − τ', τ')`). 

### `Ix`

 The `τ'`-window at offset `x`:  `I ∩ (I − x) = [max(T−x, T), min(2T−x, 2T)]`
(§5.4: "= [T + x⁻, 2T − x⁺] for |x| < T", empty for `|x| > T`). 

### `sqIntegral_shear`

 **Shear + Fubini** (§5.4 "Substituting τ = τ'+x and noting that for fixed x the variable
τ' ranges over I∩(I−x)"): for continuous `Φ`, `G`,
  `∬_{I×I} Φ(τ−τ')² G(τ,τ') d(τ,τ') = ∫_ℝ Φ(x)² (∫_{I∩(I−x)} G(x+τ', τ') dτ') dx`.
The map `(x,τ') ↦ (x+τ',τ')` preserves Lebesgue measure on `ℝ²`. 

### `integrable_sq_mul_inner`

 The sheared integrand is integrable in `x` (Fubini), so the outer integral above is a genuine
Lebesgue integral. 

### `Ix_eq_empty`

 For `T ≥ 0` the window `I∩(I−x)` is empty unless `|x| ≤ T`; so the `x`-integral may be
restricted to `[−T, T]` (§5.4 "which is empty for |x| ≥ T"). 

### `Ix_le`

 On `|x| ≤ T` (and `T ≥ 0`) the window is the honest interval `[max(T−x,T), min(2T−x,2T)]`
with left end ≤ right end, of length `T − |x|`. 

 ## The inner `τ'`-integrals:  `∫_α^β cos(θt + c) dt`  (§5.4) 

### `cos_mul_cos_eq`

 `cos A cos B = (cos(A−B) + cos(A+B))/2` (§5.4, real form of
`P_X(τ)P_X(τ') = (1/2π²) Re Σ a_n a_m [n^{iτ}m^{−iτ'} + n^{iτ}m^{iτ'}]`). 

### `Jker`

 Closed form of `J(θ,c;α,β) := ∫_α^β cos(θt + c) dt`:  `(β−α)cos c` if `θ = 0` (§5.4 "the first
inner integral is T−|x|"), else `[sin(θβ+c) − sin(θα+c)]/θ` (§5.4). 

### `abs_Jker_le`

 `|J| ≤ 2/|θ|` for `θ ≠ 0` (§5.4 "≤ 2/log(nm)"). 

### `continuous_Jker_offset`

 `J` as a function of the offset `x` (through `c = xy`, `α = max(T−x,T)`, `β = min(2T−x,2T)`)
is continuous. 

### `inner_cos_cos`

 The inner integral of [eq:MPP] in closed form: for `|x| ≤ T`,
`∫_{I∩(I−x)} cos((x+τ')y) cos(τ'y') dτ' = ½ J(y−y', xy) + ½ J(y+y', xy)`. 

 ## Per-frequency-pair decomposition of `𝓜[cos(·y), cos(·y')]`  ([eq:MPP], §5.4) 

### `JmK`

 The "−" (difference-frequency) inner integral at offset x:  J(y−y', xy; I∩(I−x)). 

### `JpK`

 The "+" (sum-frequency) inner integral at offset x:  J(y+y', xy; I∩(I−x)). 

### `Aminus`

 A⁻(y,y') := ∫_{[−T,T]} Φ(x)² J(y−y', xy) dx and A⁺(y,y') := ∫_{[−T,T]} Φ(x)² J(y+y', xy) dx:
the two halves of 𝓜[cos(·y),cos(·y')] ([eq:MPP]: first / second inner integral). 

### `Mform_cos_cos`

 **[eq:MPP] per pair** (§5.4): for T ≥ 0,
𝓜[cos(·y), cos(·y')] = ½ A⁻(y,y') + ½ A⁺(y,y'). 

 ### The diagonal 𝒟 (§5.4) 

### `abs_Aminus_diag_sub_le`

 **𝒟, per frequency** (§5.4): "For n=m the first inner integral is T−|x|, so by
[eq:Phi2FT] … 𝒟 = (T/π)Σ a_n² g(y_n) + O(…)", "using ∫_{|x|>T}Φ² ≤ ∫Φ²|x|/T":
  |A⁻(y,y) − T ∫_ℝ Φ(x)² cos(xy) dx| ≤ ∫_ℝ Φ(x)²|x| dx. 

 ### The sum-frequency terms 𝒪₂ (§5.4) 

### `abs_Aplus_le`

 **𝒪₂, per pair** (§5.4: "|∫(nm)^{iτ'}dτ'| ≤ 2/log(nm)"): for y + y' > 0,
|A⁺(y,y')| ≤ (2/(y+y')) ∫_ℝ Φ². 

 ### The difference-frequency terms 𝒪₁, exact evaluation (§5.4) 

### `Cp`

 The four half-line trigonometric moments of Φ² (the paper's α_n^±, §5.4, split into
real and imaginary parts): C⁺(y) = ∫_0^T Φ²cos(xy), S⁺(y) = ∫_0^T Φ²sin(xy),
C⁻(y) = ∫_{−T}^0 Φ²cos(xy), S⁻(y) = ∫_{−T}^0 Φ²sin(xy). 

### `integral_sq_mul_sin_sub_sin`

 linearity step: ∫_a^b Φ²[sin(c₁+xy) − sin(c₂+xy')] in terms of the cos/sin moments. 

### `sub_mul_Aminus_eq`

 **𝒪₁, per pair, exact** (§5.4): for θ := y − y' ≠ 0 and T ≥ 0,
θ·A⁻(y,y') = [sin2θT·C⁻(y) + cos2θT·S⁻(y)] − [sinθT·C⁻(y') + cosθT·S⁻(y')]
           + [sin2θT·C⁺(y') + cos2θT·S⁺(y')] − [sinθT·C⁺(y) + cosθT·S⁺(y)].
(Paper: "n^{ix}(n/m)^{−ix⁺} equals m^{ix} for x>0 and n^{ix} for x<0 …"; we split [−T,T] at 0:
on x ≤ 0 the window is [T−x, 2T], on x ≥ 0 it is [T, 2T−x].) 

### `abs_halfMoment_le`

 Each half-line moment is bounded by ∫_ℝ Φ² (the paper's |α_n^±| ≤ πbL, §5.4; we use the
cruder ≤ ∫Φ² = 2πbL, constants being immaterial). 

 ## Applying H-MV on the prime-power frequencies  ([lem:MV], [eq:deltan]; §5.1, §5.4) 

### `inv_two_mul_le_abs_log_sub`

 **[eq:deltan]** (§5.1): "consecutive prime powers n<n' satisfy
log(n'/n) ≥ log((n+1)/n) ≥ 1/(2n), so δ_n⁻¹ ≤ 2n" — in the admissible-weight form H-MV wants:
1/(2n) ≤ |log n − log m| for all distinct n, m ≥ 1 (no primality needed). 

### `MV_primeRange`

 **H-MV on the prime-power frequencies** ([lem:MV] with [eq:deltan], §5.1: "We apply this with
{λ_r} = {log n : n ≤ X a prime power}" — we index by all n ∈ primeRange X, harmless since the weights
will carry a factor Λ(n)): for complex weights x, z, frequencies y_n = log n and admissible spacing
δ_n = 1/(2n),  ‖Σ_{n≠m} x_n conj(z_m)/(y_n−y_m)‖ ≤ C (Σ 2n‖x_n‖²)^{1/2} (Σ 2n‖z_n‖²)^{1/2}. 

### `MV_real`

 **Real form used for 𝒪₁** (§5.4: "a combination of four sums of the shape
Σ_{n≠m} x_n z̄_m/(y_n−y_m) … for instance the first is Σ_{n≠m}(a_n n^{2iT}) conj(a_m m^{2iT} ᾱ_m^+)/(y_n−y_m)"):
for real weights u, v and a real phase c, both
  Σ_{n≠m} u_n v_m cos(c(y_n−y_m))/(y_n−y_m)  and  Σ_{n≠m} u_n v_m sin(c(y_n−y_m))/(y_n−y_m)
(= Re, Im of the MV bilinear form with x_n = u_n e^{icy_n}, z_m = v_m e^{icy_m}) are bounded by
C (Σ 2n u_n²)^{1/2} (Σ 2n v_n²)^{1/2}. 

### `MV_size_le`

 The size of the MV bound for our weights (§5.4 "each of the four is at most
(3π/2)·πL·Σ_n a_n²/δ_n ≪ L²X"): with u = a and v = a·w (or vice versa), |w| ≤ W,
C (Σ 2n u_n²)^{1/2} (Σ 2n v_n²)^{1/2} ≤ 2 C W Σ_{n≤X} Λ(n)². 
