---
{
  "module": "proof/consequences/CountKSat/Poly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/Poly.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/Poly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The functions of the counting program, defined in `proof/consequences/CountKSat/Defs.lean`, are
polynomial-time (`PolyT`), and the counting machine `countMK` is
`IsPolyT` (its init, step and out are polynomial-time) if its decoder, its step function and the
machine that counts one sparse formula are. The last
theorem proves `StCertStepC`, one of the interface statements of
`proof/consequences/CountKSat/Interfaces.lean`. The proofs use the certificate of
`pickK` in `proof/sparsification/SparsifyWidthK/Poly/Sparsify.lean`, that of the summing walk in
`proof/consequences/CountKSat/Walk.lean`, the closure lemmas in `proof/machines/ToTuring/Lib` and
the certificates of the
combinators in `proof/machines/ToTuring/Poly`. `isPolyT_countMK` follows `IsPolyT.satM` of
`proof/machines/ToTuring/Poly/Sat.lean`. 

### `polyT_negU`

 Writing «no literal of H is true» as unit clauses is polynomial-time. 

### `polyT_stepC`

 The two children of a node of the counting tree are computed in polynomial time, for all
thresholds θ and every width k. 

### `rootC_polyT`

 The root of the counting tree is computed in polynomial time. The number n comes in unary, so
the n clauses xᵢ ∨ ¬xᵢ are no longer than the input. 

### `leafF_polyT`

 The formula that is counted at a leaf is computed in polynomial time. 

### `outW_polyT`

 Writing the result as a word of n + 1 bits is polynomial-time, again because n comes in unary. 

### `isPolyT_countMK`

 `countMK decU step M` is `IsPolyT` if `decU` and `step` are polynomial-time and M is `IsPolyT`. 

### `certStepC`

 One step of the counting tree is computed in polynomial time: the interface statement
`StCertStepC`. 
