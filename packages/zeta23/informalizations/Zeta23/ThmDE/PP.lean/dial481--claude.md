---
{
  "module": "Zeta23/ThmDE/PP.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmDE/PP.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmDE/PP.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmDE/PP.lean.  The §7.1 partial-summation step for a
Dirichlet character: [thm:E] proof (iii) "Σ_{(n,q)=1} Λ(n)²/n = (log²x)/2 + O_q(log x)"
([eq:cheb2a] for n coprime to q, Zeta23.ThmE.ChebyshevMertensCoprime.cheb2a) fed into the abstract
Abel-summation lemma Zeta23.ThmD.abel_sum_close:
  Σ_{n≤X,(n,q)=1} Λ(n)²/n · g(log n) = ∫_0^L g(y)·y dy + O_q(L²)   (g C¹, |g'| ≤ 2, g ≡ 0 on [L,∞)).
-/
```

### `sumA2gCoprime_close`

 the coprime partial-summation step (χ-version of Zeta23.ThmD.sumA2g_close). 
