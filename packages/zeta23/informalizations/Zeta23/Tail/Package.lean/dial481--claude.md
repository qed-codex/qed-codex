---
{
  "module": "Zeta23/Tail/Package.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Tail/Package.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Tail/Package.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Tail/Package.lean — [prop:tail] with all its analytic inputs discharged from the
repository's other files, in the exact shape Zeta23/Main.lean consumes ("hTailPkg").

Inputs discharged here: A₀ and the local count from PaperInputs.RvM.local_count
(Hypotheses.lean); [eq:hfbound] for φ = Zeta23.Params.norm_phiHat_sub_I_mul_le, a ≥ 1/2 =
Zeta23.Params.half_le_a, C₁ ≤ 2‖ϱ″‖₁ = Zeta23.Params.C1_le (Taper.lean);
conj φ̂(z̄) = φ̂(z) = Zeta23.GzGp.phiHat_conj (hypothesis-free). The side condition 8w ≤ L
[eq:wrange] holds eventually since L = λ log(T/2π) → ∞ (Zeta23.Tail.tendsto_L_atTop).
-/
```

### `C1_nonneg`

 C₁ = ‖φ″‖₁ ≥ 0. 

### `eventually_tailPackage`

 **[prop:tail] package for Main.lean**: for an abstract zero configuration Z satisfying the
paper's inputs and valid parameters P, there is θ₀ : ℝ → ℝ (namely
θ₀(T) = 4A₀C₁²X^{1/2}log(4T)/D₀² = theta0 A₀ (e^{L/4}·C₁) T) such that eventually in T
Assembly.TailInputs Z P T (θ₀ T) holds ("‖Ẽ‖ ≤ θ₀", "‖Ê‖₁ ≤ θ₀/(aL)"), and
θ₀(T) ≤ C · l(T) · T^{λ/2−1} eventually ("θ₀ ≤ 32A₀‖ϱ″‖₁² l T^{λ/2−1}"). 
