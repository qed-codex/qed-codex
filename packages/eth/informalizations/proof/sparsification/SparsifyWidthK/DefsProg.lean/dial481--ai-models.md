---
{
  "module": "proof/sparsification/SparsifyWidthK/DefsProg.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/DefsProg.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/DefsProg.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sparsification of a k-CNF as plain functions on List (List (ℕ × Bool)): definitions

The small functions `overP`, `addP`, `minusP`, `rootP` are those of
`StepMachines/Math/SparsifyProg.lean`. The thresholds θ and the width k are fixed
before the input is seen. That these functions carry out the rule of `SparsifyWidthK/Defs.lean` is
proved in `SparsifyWidthK/Refine.lean`; that they are polynomial-time, in
`SparsifyWidthK/Poly/Sparsify.lean`. 

### `maskP`

 The sublist of C picked by the mask m (positions beyond the length of m are dropped). 

### `masks`

 All lists of k truth values. The list does not depend on the input. 

### `heartsP`

 The sublists of length h of the clauses of length j: the candidate hearts. 

### `pairsK`

 The pairs (j, h) with 1 ≤ h < j ≤ k, in the order of the search: j upwards, for each j the size
h of the heart downwards.
The list does not depend on the input. 

### `tryP`

 The first heart of size h in clauses of size j that lies in at least θ (j - h) of them, with its
petals. 

### `pickK`

 The rule: smallest j, then largest heart. none at a leaf. 

### `stepK`

 The light child (the heart added) and the heavy child (the petals added); none at a leaf. 

### `toFin`

 The clauses as a finite set of finite sets. 

### `NF`

 Normal form: no literal twice in a clause, and no two clauses with the same set of literals. 
