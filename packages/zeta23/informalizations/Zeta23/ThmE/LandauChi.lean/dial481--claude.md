---
{
  "module": "Zeta23/ThmE/LandauChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/LandauChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/LandauChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/LandauChi.lean — Landau partial fraction for L'/L(s,χ) (χ nontrivial):
transplant of Zeta23/WeilEF/Landau.lean's zeta_logDeriv_partial_fraction via the f-generic
Zeta23.WeilEF.logDeriv_partial_fraction_disk.  Simpler than the ζ-case: L(·,χ) is entire
(no pole exclusion) and the growth bound (LGrowth.LFunction_growth_right_uniform) is uniform
over the whole disk and fully explicit (8q(|Im|+3)); the center lower bound is
LGrowth.LFunction_lower_bound_two (1/3).
-/
```

### `L_logDeriv_partial_fraction`

 **Partial fraction for L'/L(s,χ) at height t** (|t| ≥ 6, χ ≠ 1): a finite set Z — the
L-zeros within distance (22/25)·(91/50) of 2+it — with Σ-multiplicity ≤ C·log(q(|t|+3)) and
L'/L(s) = Σ_{ρ ∈ Z} m_ρ/(s−ρ) + O(log(q(|t|+3))) on the ball of radius 3/2 around 2+it. 
