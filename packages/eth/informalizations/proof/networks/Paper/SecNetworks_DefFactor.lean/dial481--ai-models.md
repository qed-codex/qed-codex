---
{
  "module": "proof/networks/Paper/SecNetworks_DefFactor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Paper/SecNetworks_DefFactor.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Paper/SecNetworks_DefFactor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 3 of the paper, Definition 1: factoring through c bits

This file imports Mathlib only. It renders Definition 1 of the paper as a predicate,
`Paper.FactorsThrough F c`.

**Not on the path to Theorem 2.** In the proof of Theorem 2 the functions Ψ of a network are *defined*
by their factorization
(`Groundwork.Network.Ψ`), so the predicate is never needed there.


### `FactorsThrough`

 **Definition 1 of the paper.** The function F : X × X' → ℤ *factors through c bits* if there are
f : X × {0,1}^c → ℤ and
f' : X' × {0,1}^c → ℤ with F(z, z') = ∑_θ f(z, θ) · f'(z', θ), the sum over all θ ∈ {0,1}^c.
Differences from the paper: a bit string of length c is a function `Fin c → Bool`; F takes its two
arguments one after the
other; X and X' need not be finite (the paper assumes that they are, and does not use it in the
definition). 
