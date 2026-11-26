---
{
  "module": "proof/sparsification/SparsifyWidthK/Poly/Sparsify.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/Poly/Sparsify.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsifyWidthK/Poly/Sparsify.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The functions of `SparsifyWidthK/DefsProg.lean`, which compute the two children of a node of the
sparsification tree of a k-CNF, are polynomial-time
(`PolyT`). The last theorem, `certStep`, proves `StCertStep`, one of the interface statements of
`SparsifyWidthK/Interfaces.lean`. The proofs use the closure
lemmas for list functions in `proof/machines/ToTuring/Lib` and the certificates of `overP`, `minusP`
and `addP` in `proof/machines/ToTuring/Poly/Sparsify.lean`, whose pattern
this file follows: every certificate is stated for arguments that depend on a context x, the form in
which the tactic `fun_prop` can use it.
The width k and the thresholds θ do not depend on the input, and nothing is assumed about them. 

### `polyT_maskP`

 Picking the sublist of a clause given by a mask is polynomial-time. 

### `polyT_heartsP`

 Listing the candidate hearts is polynomial-time. The list `masks k`, of length 2^k, does not
depend on the input. 

### `tryT`

 `tryP` with the threshold given as a number c.2 beside the pair c.1 = (j, h) of a clause size j
and a heart size h. 

### `polyT_tryT`

 The search for a heart of a given size that reaches a given threshold is polynomial-time. 

### `pickK_eq`

 `pickK` as a search along the list of the pairs (j, h) of a clause size j and a heart size h,
each with its threshold θ (j - h). This list does not depend on the input, so θ, an arbitrary
function, is never applied to a value computed from the input. 

### `polyT_pickK`

 The choice of the heart and its petals at a node is polynomial-time. 

### `polyT_stepK`

 The two children of a node of the sparsification tree are computed in polynomial time. 

### `certStep`

 The same for `stepK θ k` as a function of the node alone: the interface statement `StCertStep`. 
