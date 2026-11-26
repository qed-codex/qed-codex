---
{
  "module": "Zeta23/XiPrime/Hardy/EFWeights.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFWeights.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFWeights.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/EFWeights.lean — the pair-weight bounds at an ARBITRARY imaginary shift |Im z| ≤ 3/4
(namespace Zeta23.XiPrime.HW).  This file builds on the per-window layer `TestWeight.WindowAt` of
ExplicitFormula/TestWeight.lean (norm_phiHat_le / abs_re_mul_norm_phiHat_le at general z, paperFT_kfun, kfun regularity).

The W contour runs on Re s = c with c ∈ (1, 5/4], and the low-zero / pole terms need
the weight at points with |Re ρ − 1/2| ≤ 3/4 off the line; so the per-factor estimates
(‖φ̂(w)‖ ≤ (1+C)e^{|Im w|L/2}L/(1+(Re w)²), |Re w|‖φ̂(w)‖ ≤ 2C·e^{|Im w|L/2}/(1+(Re w)²)) are evaluated at any z with
|Im z| ≤ 3/4, using e^{|Im z|L/2} ≤ e^{3L/8} (L ≥ 1); the two exponential factors multiply to X^{3/4}.
  paperFT_kfun_bounds : ‖ĥ_{kfun}(z)‖ ≤ C·X^{3/4}·L²·K_{τ_k}(Re z)K_{τ_l}(Re z),
                        (|Re z−τ_k| + |Re z−τ_l|)·‖ĥ_{kfun}(z)‖ ≤ C·X^{3/4}·L·K_{τ_k}(Re z)K_{τ_l}(Re z);
  paperFT_comp_neg    : ĥ_{u ↦ k(−u)}(z) = ĥ_k(−z)   (re-export of TestWeight.paperFT_comp_neg);
  cauchyK_le_of_far   : K_a(x) ≤ 4/T² when |x − a| ≥ T/2;
  kfun_regular', kfun_facts : (W0) for kfun and for u ↦ kfun(−u), one threshold / one constant with the bounds.
-/
```

 ## A. reflection of the paper Fourier transform 

### `paperFT_comp_neg`

 ĥ_{u ↦ k(−u)}(z) = ĥ_k(−z). 

 ## A'. the far Cauchy kernel (used by EFLowZeros and EFMain) 

### `cauchyK_le_of_far`

 if |x − a| ≥ T/2 > 0 then K_a(x) = (1 + (x−a)²)⁻¹ ≤ 4/T². 

 ## B. the factor and pair bounds at |Im| ≤ 3/4, from TestWeight.WindowAt 

### `factor_bounds_le`

 factor bounds at w = z − a with |Im z| ≤ 3/4. 

### `pair_bounds_le`

 pair bounds at |Im z| ≤ 3/4. 

 ## C. the consumer statements 

### `paperFT_kfun_bounds`

 **the pair-weight bounds at any |Im z| ≤ 3/4.** 

### `paperFT_kfun_neg`

 ĥ for the mirrored pair test function. 

 ## D. (W0) for kfun and its mirror, same threshold as the bounds 

### `kfun_regular'`

 **(W0)** regularity and support of kfun and of u ↦ kfun(−u). 

### `kfun_facts`

 All weight facts under one threshold and one constant, in the form consumed by `Hardy/EFMain`. 
