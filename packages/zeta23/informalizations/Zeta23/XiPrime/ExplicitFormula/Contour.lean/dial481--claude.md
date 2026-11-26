---
{
  "module": "Zeta23/XiPrime/ExplicitFormula/Contour.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/Contour.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/Contour.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
(EF1) contour step, generic in the function f.

The weighted argument principle on the rectangle [1−c, c] × [−R, R] for an entire f whose zeros all
lie in the open vertical strip 1−c < Re s < c and which does not vanish on the two horizontal sides:
    (1/2πi) ∮ g · f′/f = Σ_{ρ : f ρ = 0, |Im ρ| < R} ord_ρ(f) · g(ρ).
No pole terms (contrast Zeta23.WeilEF.rectangle_identity for Λ, which has − H(0) − H(1)).
-/
```

### `differentiable_Hfn`

 `H = Hfn k` is entire (paperFT of a compactly supported C² function). 

### `mem_rectangle_iff`

 membership in the closed rectangle with corners (1−c) − iR and c + iR. 

### `rectangle_identity_of`

 **Generic rectangle identity.**  f, g entire; every zero of f has 1−c < Re < c (Zset = zero set);
f ≠ 0 on the horizontal lines Im s = ±R, 1−c ≤ Re s ≤ c.  Then the zeros of f with |Im| < R form a
finite set Z and (1/2πi)∮_{∂([1−c,c]×[−R,R])} g·f′/f = Σ_{ρ∈Z} ord_ρ(f)·g(ρ). 

### `rectangle_identity`

 **Rectangle identity for ξ′** under (F2):  at a height R ≥ 0 where ξ′ ≠ 0 on Im s = ±R,
1−c ≤ Re s ≤ c (c > 1):  (1/2πi)∮ H·ξ″/ξ′ = Σ_{ξ′(ρ)=0, |Im ρ|<R} m_ρ H(ρ)  — no pole terms. 
