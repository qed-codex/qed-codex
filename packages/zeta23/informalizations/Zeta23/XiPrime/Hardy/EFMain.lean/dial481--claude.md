---
{
  "module": "Zeta23/XiPrime/Hardy/EFMain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFMain.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFMain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/EFMain.lean — the W explicit formula WEF [XF′ Thm 9.2], assembled.
External inputs enter as Prop-valued hypotheses with fixed shapes (so this file stands independently;
Hardy/EFFinal.lean instantiates them):
  LineFactsW        — (EFExpansion X5–X8):  for 9/8 ≤ c ≤ 5/4 and W ≠ 0 on Re s = c:
                      E2LineFacts c ∧ FreezeFactsW c ∧ the F_𝒵 line bound;
  ContourFactsW     — (EFContour): WFullLineIdentity hZ hs c ∧ LminusLineIdentity c, given W ≠ 0 on
                      Re s = c and Re s = 1 − c below height t₀ and the line bound;
  CoeffFactsC       — LSeries_xiCoeffJ on lines Re s = c ≥ 9/8, + conj;
everything else is proved in the tree: the choice of c (EFBasic.exists_zeroFree_line), W(1−c) ≠ 0 at the real point
(reflection identity extended by continuity, below), GramBridge/GramBridgeW, HW.kfun_facts (weights at
|Im z| ≤ 3/4), w_EF_lit_corr (EFLitCorrW), JcorrW_estimate (EFJTermW), prime_term_complex, FamilyFacts.
-/
```

 ## 1. Input Props 

### `LineFactsW`

 EFExpansion, consumer shape. 

### `ContourFactsW`

 The EFContour data, in consumer shape. 

### `CoeffFactsC`

 The L-series identity on lines Re s = c ≥ 9/8, consumer shape (real or complex parameter). 

 ## 2. W at the real point 1 − c: the reflection identity by continuity 

### `hardyW_analyticAt_leftStrip`

 the left strip −1/2 < Re s < 0: W is analytic there (no poles: Γℝ(s) and Γℝ(1−s) regular, s ≠ 1). 

### `hardyW_eq_neg_chiFE_mul_goodStrip`

 **W(s) = −χ(s) W(1−s) at every point of the strip 1 < Re s < 3/2, real points included**
(Hardy.hardyW_eq_neg_chiFE_mul off ℝ, extended by continuity). 

### `hardyW_ne_zero_reflect`

 zero-freeness transfers from Re s = c to Re s = 1 − c (all points, below any height). 

 ## 3. Small geometric helpers 

 ## 4. The assembly 
