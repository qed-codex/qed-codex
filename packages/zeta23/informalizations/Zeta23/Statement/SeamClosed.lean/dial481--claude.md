---
{
  "module": "Zeta23/Statement/SeamClosed.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Statement/SeamClosed.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Statement/SeamClosed.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Statement/SeamClosed.lean — the ζ-seam is closed.
All four fields of Zeta23.ZetaSeam are theorems of Mathlib:
  one_le_mult, finite_window  — Zeta23/Statement/Seam.lean ;
  reflect_zero, mult_reflect  — Zeta23/ZetaReflect.lean (Schwarz reflection
                                 riemannZeta_conj + functional equation at the analyticOrderAt level).
Hence the abstract ZeroConfig of ζ's nontrivial zeros and [eq:trivialchain] are hypothesis-free.
-/
```

### `zetaSeam`

 The ζ-seam, fully discharged: no hypotheses. 

### `zetaZeroConfig`

 The nontrivial zeros of ζ with multiplicities, as an abstract Zeta23.ZeroConfig — hypothesis-free.
carrier = {ρ | IsNontrivialZero ρ}, mult = zeroMult (both rfl). 

### `trivial_chain₀`

 [eq:trivialchain] for ζ, hypothesis-free: N₀ˢ ≤ N₀* ≤ N₀ ≤ N and N₀ˢ ≤ Nˢ ≤ N_d ≤ N. 

### `zerosIn_finite`

 Finiteness of every ordinate window of nontrivial zeros, hypothesis-free. 
