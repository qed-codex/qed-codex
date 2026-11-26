---
{
  "module": "Zeta23/XiPrime/ExplicitFormula/LitCorr.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/LitCorr.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/LitCorr.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ExplicitFormula/LitCorr.lean — (EF2) archimedean line + the "literature form with correction" layer of the
ξ′ / W explicit formulas.

§A (archimedean, 1 < c ≤ 3/2):  (1/2π)∫[H(c+it)+H(1−c−it)]·L(c+it)dt = H(0)+H(1) + (1/2π)∫h·[Re ψ(¼+ir/2) − log π]
   (Γℝ piece: WeilEF.gamma_line_shift/gammaR_bracket; rational piece: FullLine.rational_line_inst).
§B (generic line Re s = c): HwC c k t := H(c+it)+H(1−c−it), its decay/continuity/integrability against bounded g, and
   the ζ-case evaluation  Efn_line_identity : (1/2π)∫ HwC·E = literatureRHS k  (E = L + ζ′/ζ; = the
   EF_lit_zeta right-hand side [eq:EFstd] at any 1 < c ≤ 3/2).
§C (ξ′ at c = 5/4): the input Props FullLineIdentity / RationalLine, dEE, Hw := HwC (5/4), Jcorr, and
   xiPrime_EF_lit_corr :  Σ'_{ρ₁} m_{ρ₁} h_k(γ_{ρ₁}) = literatureRHS k + Jcorr k  [ξ″/ξ′ = E + E′/E, Expansion].
-/
```

 ## §A. The archimedean line 

### `Lfn_eq`

 L splits as Γℝ′/Γℝ + (1/s + 1/(s−1)) (definition). 

### `logDeriv_mul_sub_one`

 1/s + 1/(s−1) is the logarithmic derivative of s(s−1), off {0,1}. 

### `gamma_line`

 **Γℝ piece** (WeilEF.gamma_line_shift + gammaR_bracket):
(1/2π)∫[H(c+it)+H(1−c−it)]·Γℝ′/Γℝ(c+it) dt = (1/2π)∫ h_k(r)·gammaBracket(r) dr. 

### `rational_line`

 **rational piece**: (1/2π)∫[H(c+it)+H(1−c−it)]·(1/(c+it) + 1/(c+it−1)) dt = H(0) + H(1)
— the f = s(s−1) instance of the generic full-line identity (FullLine.rational_line_inst). 

### `integrable_weight_mul_logDeriv_Gammaℝ`

 integrability of the Γℝ piece with the two-sided weight. 

### `archimedean_line`

 **(EF2)**: the archimedean line identity. 

 ## §B. The generic line Re s = c: two-sided weight and the ζ-case evaluation 

### `HwC`

 the two-sided test weight on the line c: H(c+it) + H(1−c−it). 

 ## weight facts on the line 

 ## the ζ evaluation at general c:  (1/2π)∫[H+H̃]·E = literatureRHS k 

 ## §C. ξ′ at c = 5/4: input Props, the correction functional J, literature form with correction 

 ## Input propositions (discharged elsewhere) 

### `FullLineIdentity`

 (EF1) on the line c = 5/4, as a Prop (proved in `Main.full_line_identity`). 

### `RationalLine`

 the rational line identity at c = 5/4, as a Prop (Archimedean.rational_line). 

### `dEE`

 E′/E on the line: the function g(t) := (deriv E / E)(5/4 + it). 

### `Hw`

 the two-sided test weight on the line 5/4 (= HwC (5/4)). 

### `Jcorr`

 Jcorr k := (1/2π) ∫ [H(5/4+it) + H(1−5/4−it)]·(E′/E)(5/4+it) dt. 

### `integrable_Hw_mul_dEE`

 under (F2), Hw·(E′/E) is integrable. 

### `logDeriv_xiDeriv_line_split'`

 pointwise on Re s = 5/4:  ξ″/ξ′ = E + E′/E  (Expansion.logDeriv_xiDeriv_eq_Efn). 

### `xiPrime_EF_lit_corr`

 **ξ′ explicit formula, literature form with correction**:
Σ' m_{ρ₁} h_k(γ_{ρ₁}) = literatureRHS k + Jcorr k. 
