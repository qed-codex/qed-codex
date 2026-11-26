---
{
  "module": "Zeta23/Statement/Seam.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Statement/Seam.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Statement/Seam.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Statement/Seam.lean — discharging the ζ-seam obligations of Zeta23.ZetaSeam from Mathlib. These are classical facts about riemannZeta, not inputs of the paper:
  * one_le_mult   : at a nontrivial zero the analytic order of ζ is finite and ≥ 1
                    (ζ analytic on ℂ ∖ {1}, which is connected, and ζ(2) ≠ 0 ⇒ identity theorem);
  * finite_window : finitely many nontrivial zeros with T₁ < Im ρ ≤ T₂
                    (zeros of ζ are locally finite on ℂ ∖ {1}; near 1 there are none because of the
                    pole; the closed box [0,1] × [T₁,T₂] is compact).
reflect_zero / mult_reflect (functional equation + conjugation) are proved elsewhere in the
repository.
-/
```

### `riemannZeta_analyticOnNhd_compl_one`

 ζ is analytic on ℂ ∖ {1}. 

### `isConnected_compl_one`

 ℂ ∖ {1} is connected. 

### `analyticOrderAt_riemannZeta_ne_top`

 ζ is not locally identically zero anywhere on ℂ ∖ {1}. 

### `ZetaSeam.one_le_mult_holds`

 Seam obligation H-fin. 

### `riemannZeta_zeros_locallyFinite`

 The zeros of ζ (away from 1) are locally finite on all of ℂ. 

### `ZetaSeam.finite_window_holds`

 Seam obligation: local finiteness of the nontrivial zeros in ordinate windows. 

### `ZetaSeam.of_reflect`

 With H-fin and finiteness discharged above, a ZetaSeam needs only the two reflection facts
(functional equation + conjugation symmetry). 
