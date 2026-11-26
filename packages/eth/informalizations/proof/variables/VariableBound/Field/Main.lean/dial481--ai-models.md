---
{
  "module": "proof/variables/VariableBound/Field/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 13 (Family of checks), with its second sentence

The two halves put together: the list `famD m a` of the sets Γ_u, u ∈ Ω, is computed in polynomial
time (proof/variables/VariableBound/Field/Cert.lean), and it has the properties that the lemma
states
(proof/variables/VariableBound/Field/Family.lean, from the lemma over an arbitrary field with 2^s
elements, proof/variables/VariableBound/Family/Main.lean). 

### `famD_isFamily`

 Lemma 13 (Family of checks) for the listed family: for v = 2^a with 2 ≤ v ≤ m, the list
`famD m a` is not empty and has fewer than (32m)⁴ members, every member is an increasing list of
numbers below m,
and the members, indexed by their places in the list, have (a), (b), (c). 

### `lemFamily_listed`

 Lemma 13 (Family of checks) with its second sentence: the list `famD m a` is computed in
polynomial time, jointly in m and a, both given in unary; and for v = 2^a with 2 ≤ v ≤ m it is not
empty, has fewer than (32m)⁴
members, every member is an increasing list of numbers below m, and the members, indexed by their
places in the list, have (a), (b), (c). That the list is not empty is in the printed proof (|Ω| ≥
(15/16)·|𝔽|⁴), not in the
printed statement. 
