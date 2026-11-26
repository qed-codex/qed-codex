---
{
  "module": "Zeta23/PrimeSideB/PP.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideB/PP.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideB/PP.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Prime side, part B/PP — paper §5 [prop:PP] (§5.4): the term 𝓜[P_X,P_X]

Consumed by `Zeta23/PrimeSideB.lean` ([thm:traces]) through the three results at the bottom of
this file:

* `prop_PP`        [prop:PP] first form (§5.4):
      𝓜[P_X,P_X] = (T/π) Σ_{n≤X} Λ(n)²/n · g(log n) + O(L²X);
* `sum_a2g_lower`, `sum_a2g_upper`  (§5.4, the "Finally" step, from [eq:gbounds]+[eq:cheb2]):
      (L−2w)³/6 − C·L² ≤ Σ_{n≤X} Λ(n)²/n · g(log n) ≤ L³/6 + C·L²,
  which give the paper's second form  𝓜[P_X,P_X] = (TL³/6π)(1+O(w/L)) + O(L²X).

Everything is stated in the abstract prime-side layer (Zeta23/PrimeSideA/Defs.lean +
`LocalHyps`/`EventuallyAt` of Zeta23/PrimeSideA.lean): `p : Setting` = (T, λ, w), `F : LocalFun` =
the taper data (φ̂, Φ, A_φ, g, a, b) subject to `LocalHyps cϱ p F` (the facts [eq:psidef],
[eq:abdef], [eq:gbounds], [eq:Phi2FT], …, each a proof obligation of Zeta23/Taper.lean, not an
axiom).  `P_X` is `Zeta23.PX` [eq:Pdef] of Zeta23/Defs.lean and 𝓜[·,·] is
`Zeta23.PrimeSide.Mform` (§5.4).  Analytic inputs: H-cheb = `Zeta23.ChebyshevMertens` [lem:cheb]
and H-MV = `Zeta23.MVHilbert` [lem:MV] from Zeta23/Hypotheses.lean (fields of `PaperInputs`).

## Proof route (paper §5.4, reorganised for Lean; labels as in the paper)
1. Bilinearity:  𝓜[P_X,P_X] = π⁻² Σ_{n,m≤X} a_n a_m 𝓜[cos(·y_n), cos(·y_m)],  a_n = Λ(n)/√n, y_n = log n.
2. Shear `(τ,τ') ↦ (x,τ') := (τ−τ',τ')` (measure-preserving on ℝ²) + Fubini  (§5.4 "Substituting
   τ = τ'+x … τ' ranges over I∩(I−x) = [T+x⁻, 2T−x⁺]"):
      𝓜[u,v] = ∫_{|x|≤T} Φ(x)² ∫_{max(T,T−x)}^{min(2T,2T−x)} u(τ'+x) v(τ') dτ' dx.
3. cos A cos B = ½cos(A−B) + ½cos(A+B): inner integral = ½J(xy_n, y_n−y_m) + ½J(xy_n, y_n+y_m),
   J(c,θ) := ∫_α^β cos(c+θτ')dτ' = (β−α)cos c (θ=0), = [sin(c+θβ)−sin(c+θα)]/θ (θ≠0), |J| ≤ 2/|θ|.
4. 𝒟 (n=m, "−"):  ½∫_{|x|≤T}Φ²(T−|x|)cos(xy_n) = πT g(y_n) + O(∫Φ²|x|)   by [eq:Phi2FT];
   𝒪₂ (all n,m, "+"):  ≤ (∫Φ²)(Σa_n)²/(2π² log 2) ≪ XL                        by [eq:cheb1];
   𝒪₁ (n≠m, "−"):  an explicit combination of 8 sums Σ_{n≠m} x_n conj(z_m)/(y_n−y_m) with
   |x_n| = a_n, |z_m| ≤ a_m ∫Φ², each ≤ C_MV·(∫Φ²)·Σ a_n²/δ_n with δ_n = 1/(2n) [eq:deltan] ≪ L²X by H-MV
   and [eq:cheb1] (Σ Λ(n)² ≪ X log X).
Constants: the paper's O(L²X) constant (and the λ=1 "18/L" sharpness) is not load-bearing;
we prove ∃ C.


 ## The main-term sum  Σ_{n≤X} a_n² g(y_n) = Σ_{n≤X} Λ(n)²/n · g(log n)   (§5.4) 

### `sumA2g`

 `Σ_{n ≤ X} Λ(n)²/n · g(log n)` — the sum in the first form of [prop:PP] (§5.4), indexed like
`Zeta23.PX` over `primeRange X = Finset.Ioc 0 ⌊X⌋₊` (Λ = 0 off prime powers).  Note `a_n² = Λ(n)²/n`
(§5.4). 

 ## Elementary facts about the index range and `X = e^L` 

### `Setting.log_X`

 `log X = L` (`X := e^L`). 

### `LocalHypsCore.L_add_one_le_X`

 `X = e^L ≥ 1 + L`; with `L ≥ 8` [eq:wrange] this gives `X ≥ 2` and `L ≤ X`. 

 ## The g-sandwich  (§5.4)

"Finally, by [eq:gbounds] and [eq:cheb2] (note a_n² = Λ(n)²/n),
  (L−2w)³/6 + O(L²) = Σ_{n≤Xe^{−2w}} a_n²(L−2w−y_n) ≤ Σ_{n≤X} a_n² g(y_n) ≤ Σ_{n≤X} a_n²(L−y_n) = L³/6+O(L²)". 

 ## Assembly of [prop:PP]  (§5.4) 

### `sum_sum_eq_diag_add_offdiag`

 diagonal / off-diagonal split of a double sum ("𝒟 collects the terms n=m …, 𝒪₁ the terms n≠m",
§5.4). 

### `Mform_PX_PX`

 **[eq:MPP]** (§5.4): bilinearity in the prime sum, then the per-pair decomposition:
  𝓜[P_X,P_X] = (1/2π²)·( Σ_n a_n² A⁻(y_n,y_n)  +  Σ_{n≠m} a_n a_m A⁻(y_n,y_m)  +  Σ_{n,m} a_n a_m A⁺(y_n,y_m) )
             =        𝒟-part              +          𝒪₁                   +          𝒪₂ . 

### `diag_estimate`

 **𝒟** (§5.4): with [eq:Phi2FT] ∫Φ²cos(xy) = 2πg(y),
  |(1/2π²)Σ_n a_n² A⁻(y_n,y_n) − (T/π) Σ_n a_n² g(y_n)| ≤ (1/2π²)·(Σ_n a_n²)·∫Φ²|x|. 

### `O2_estimate`

 **𝒪₂** (§5.4): "|∫(nm)^{iτ'}dτ'| ≤ 2/log(nm) ≤ 2/log 4 for all n,m, so
|𝒪₂| ≤ (1/2π²)(Σ a_n)²·2πbL·2/log4 ≪ XL" — pre-Chebyshev form:
  |Σ_{n,m} a_n a_m A⁺(y_n,y_m)| ≤ (∫Φ²/log 2)·(Σ_n a_n)².   (Terms with n=1 or m=1 vanish as Λ(1)=0;
otherwise y_n + y_m ≥ 2 log 2.) 

 ## Results consumed by PrimeSideB.lean 

### `prop_PP`

 **[prop:PP], first form** (§5.4, verbatim):
"𝓜[P_X,P_X] = (T/π) Σ_{n≤X} Λ(n)²/n · g(log n) + O(L²X)".
Here 𝓜[P_X,P_X] = `Mform F.Phi p.T (Zeta23.PX p.X) (Zeta23.PX p.X)` (§5.4, [eq:Pdef]).
Inputs: H-cheb [lem:cheb] and H-MV [lem:MV] (any constant), plus the taper facts `LocalHyps`.
Shape: ∃ C, for T ≥ T₀(λ, cϱ, the H-constants). 

### `sum_a2g_lower`

 **[prop:PP], the g-sandwich, lower half** (§5.4, verbatim):
"(L−2w)³/6 + O(L²) = Σ_{n≤Xe^{−2w}} a_n²(L−2w−y_n) ≤ Σ_{n≤X} a_n² g(y_n)",
"by [eq:gbounds] and [eq:cheb2] (note a_n² = Λ(n)²/n)".  One-sided, explicit-slack form. 

### `sum_a2g_upper`

 **[prop:PP], the g-sandwich, upper half** (§5.4, verbatim):
"Σ_{n≤X} a_n² g(y_n) ≤ Σ_{n≤X} a_n²(L−y_n) = L³/6 + O(L²)". 
