---
{
  "module": "Zeta23/ThmE/MuMuChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/MuMuChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/MuMuChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/MuMuChi.lean — [prop:mumu] for Dirichlet characters (Theorem E, paper sec 7.2):
the diagonal mu_chi-evaluation.

Differences from the zeta-version: mu -> muq kappa q; window sup-bound |mu_chi| <= C_a * l
(muq_abs_le) instead of |mu| <= l, so the core lemmas carry an abstract bound A (>= 0); the
K-increment arrives in unified K(|r|+r^2)/t shape (muq_increment_bound); constants fold at the
end (C is existentially bound).
-/
```

### `abs_inner_sub_le_chi`

 Core scalar estimate (chi-version): for every x, the inner shear integral differs from
the window integral of muq^2 by at most (A^2 + A*K)|x| + A*K*x^2. 

### `mumu_core_chi`

 Core estimate of [prop:mumu]_chi at fixed (p, F). 

### `prop_mumu_chi`

 [prop:mumu]_chi: the diagonal mu_chi evaluation with O_q(l^2 log L) error; proof of the
statement recorded in Zeta23/ThmE/PrimeSideChi.lean. 
