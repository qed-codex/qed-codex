---
{
  "module": "Zeta23/XiPrime/CertificateFn.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/CertificateFn.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/CertificateFn.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/CertificateFn.lean — the c = 2 and c = 3 count certificates over ABSTRACT REAL FUNCTIONS.

Zeta23.Assembly.count_certificate / count_certificate_c3 are stated for ONE parameter set P, with the
moments written as rtrace (P.hat T (Z.Gz P T)), frobSq (…) and the tail size as θ₀ T/(P.a T · P.L T).  Their
proofs never look inside those three real numbers (beyond frobSq ≥ 0).  For a HEIGHT FAMILY Pf : ℝ → Params
(the window at height T is (Pf T).phi T — the quartic window, Defs.Params.atV) we need the same algebra
with tr, fr, B, N, NII, lower arbitrary real functions of T; this file is that copy, proofs verbatim.
-/
```

### `count_certificate_fn`

 **c = 2 count certificate, function-abstract form.**  If eventually
4·tr − fr − 2N − 3NII − B(4 + 2√fr + B) ≤ lower, B ≥ 0, B → 0, NII = o(N), N → ∞, fr ≥ 0, and for every
δ > 0 eventually (1−δ)N ≤ tr and fr ≤ (κ+δ)N, then for every ε > 0 eventually (2 − κ − ε)N ≤ lower. 

### `count_certificate_c3_fn`

 **c = 3 count certificate, function-abstract form:** from
6·tr − fr − 3N − 5NII − B(6 + 2√fr + B) ≤ 2·lower and the moments, eventually (3/2 − κ/2 − ε)N ≤ lower. 
