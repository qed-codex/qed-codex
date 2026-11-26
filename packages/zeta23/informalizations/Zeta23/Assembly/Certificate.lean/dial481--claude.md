---
{
  "module": "Zeta23/Assembly/Certificate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Assembly/Certificate.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Assembly/Certificate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Assembly/Certificate.lean — the §6 certificate abstracted over the second moment: for any
zero configuration and window parameters, with the zero-side block/tail inputs as usual, if eventually
tr Ĝ ≥ (1−δ)N  and  ‖Ĝ‖_F² ≤ (κ+δ)N  (every δ > 0), then every count satisfying the fixed-T seam
inequality is eventually at least (2 − κ − ε)N(T,2T)  (every ε > 0).  At κ = 1/λ₁ + λ₁/3 this is the
paper's H(λ₁).  The arithmetic lives entirely in the two moment hypotheses; no prime side, no
zero-counting formula and no explicit formula is consumed here.
-/
```

### `N0star_lower_moment`

 κ-version of `N0star_lower_H`: moments ⟹ fixed-T lower bound. 

 ## Seam-agnostic count certificates (for the multiplicity-aware rank–trace variants:
the zero-side inequality arrives as the hypothesis h0, so the same algebra serves N₀* (seamA),
the c = 2 multiplicity-aware N₀ˢ seam, and — in halved form below — the c = 3 N_d seam). 

### `count_certificate`

 The moment certificate with the fixed-T seam inequality abstracted: any count `lower`
satisfying the seam shape eventually obeys the (2 − κ − ε) certificate. 

### `count_lower_moment_c3`

 the c = 3 fixed-T algebra: from `6·tr − frob − 3N − 3NII − B·(…) ≤ 2·lower` and the moment
bounds, `(3/2 − κ/2)·N − errors ≤ lower`. 
