---
{
  "module": "Zeta23/PrimeSideA/MuMu.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/MuMu.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/MuMu.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/PrimeSideA/MuMu.lean

[prop:mumu] (paper §5.4): 𝓜[μ,μ] = 2πbL ∫_T^{2T} μ² + O(l² log L).

Paper proof, as implemented here:
  * shear τ = τ' + x (`sqIntegral_shear`):
      𝓜[μ,μ] = ∫_ℝ Φ(x)² (∫_{I∩(I−x)} μ(x+τ')μ(τ') dτ') dx;
  * Lipschitz step "μ(τ)=μ(τ')+O(|τ−τ'|/T)" (via `mu_increment_bound`'s (K|r|+10r²)/t):
      |∫_{Ix}(μ(x+τ')−μ(τ'))μ(τ')| ≤ l(K|x| + 10x²)   (window length ≤ T, τ' ≥ T);
  * completing ∫_{Ix} to ∫_I ("∫_{I−τ'}Φ² = 2πbL − tails"):
      |∫_{I∖Ix} μ²| ≤ l²·|x|   (vol(I∖Ix) = min(|x|,T));
  * ∫Φ²|x| ≤ 8 + 8log(cϱL/4w) ≪ log L  [eq:psiints]  and  ∫Φ²x² ≤ 8 + 2(cϱ/w)² = O(1).
-/
```

### `abs_inner_sub_le`

 Core scalar estimate: for every x, the inner shear integral differs from `∫_I μ²` by at most
`(1+K) l² |x| + 10 l x²`. 

### `mumu_core`

 **Core estimate of [prop:mumu]** at fixed (p, F), error in terms of the two Φ-integrals. 

 ## [prop:mumu] 

### `prop_mumu`

 **[prop:mumu]** (§5.4): `𝓜[μ,μ] = 2πbL ∫_T^{2T} μ² + O(l² log L)`.
(`hcheb`/`hlam` are unused here but kept so that the statement matches the fixed interface
shared with the other prime-side propositions.) 
