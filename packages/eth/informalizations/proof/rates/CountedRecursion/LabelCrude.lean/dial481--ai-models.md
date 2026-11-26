---
{
  "module": "proof/rates/CountedRecursion/LabelCrude.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/LabelCrude.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/LabelCrude.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «Crude bounds give L ≤ N + 1»

Proof of Theorem A (b), the step from ℓ to ℓ + 1: crude bounds give L ≤ N + 1, B' ≤ N + g²B₁, g(P +
B₁) ≤ Ξ^{c+4} and K(L + B') ≤ Ξ^{c+5}. The statement `CrudeBounds` takes the first of the four as a
hypothesis. Here it is proved (`LabelCrude`) for the lemma's L = ⌈(U + 2ζgP)/K²⌉ and the total U of
either network of a pattern; `ProcedureCostFrom` takes it as a premise: the cost of an entry
(`EntryCostExplicit`) asks L ≤ 2gP for the L of a call, and L ≤ N + 1 = gP + 1 ≤ 2gP. For the bounds
on λ used along the recursion, the same inequality is part of `ChainLabel`, from which `ChainBase`
gets K(L + B') ≤ Ξ^{c+5}.
* `total_le`: U ≤ N, since there are at most g² ordered pairs of nodes and c_{a,a'} ≤ g²λ.
* `label_le_of`: L ≤ N + 1 whenever U ≤ N; `label_le_net`, `labelCrude : LabelCrude`: so for either
  network of a pattern. 

### `total_le`

 U ≤ N = g⁴λ, for either network of a pattern. 

### `label_le_of`

 «L ≤ N + 1», for every U ≤ N. 

### `label_le_net`

 **«Crude bounds give L ≤ N + 1»**, for the lemma's L and either network of a pattern. 

### `labelCrude`

 `label_le_net`, in the form of the statement `LabelCrude`. 
