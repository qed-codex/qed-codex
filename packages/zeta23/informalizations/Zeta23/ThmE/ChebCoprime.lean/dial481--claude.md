---
{
  "module": "Zeta23/ThmE/ChebCoprime.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/ChebCoprime.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/ChebCoprime.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/ChebCoprime.lean — [eq:cheb2] restricted to
(n,q) = 1, derived from the unrestricted Zeta23.Cheb.chebyshevMertens by bounding the removed
prime-power terms: Σ_{p ∣ q} Σ_{k≥1} (log p)²/p^k ≤ Σ_{p∣q} (log p)² ≤ (log q)²
([thm:E] proof (iii): 'finitely many primes removed', O_q(·) errors).
-/
```

### `removed_le`

 The removed-terms bound: for a weight `w` with `0 ≤ w ≤ W` on the window,
`Σ_{n ≤ x, ¬(n,q)=1} Λ(n)²/n · w(n) ≤ W·(log q)²`. 

### `chebyshevMertensCoprime`

 **[eq:cheb2] with the (n,q)=1 restriction** ([thm:E] proof (iii)). 

### `chebyshevMertensCoprimeBounded`

 **Uniform coprime Chebyshev–Mertens**: one absolute `A` with
`ChebyshevMertensCoprimeBounded q (A·(1 + log q)²)` for every `q ≥ 1` (the uniform-in-`q`
`chebq_uniform` input; constant = ζ-constants + the (log q)² prime-power loss). 

### `chebyshevMertensCoprime'`

 the plain (per-q) version, re-derived from the uniform one. 
