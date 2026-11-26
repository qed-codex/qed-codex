---
{
  "module": "proof/consequences/SplitSat/Procedure.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitSat/Procedure.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitSat/Procedure.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 5: «Theorem 2 gives s_3 = 0», for the machine of Theorem 2 in its decision form without its reader

`stCore3Eq`: the machine `ThreeSatPrinted.SATCp ℓ τ` of Theorem 2 is a reader of the input followed
by `core3 ℓ τ`; the two sides are the same by definition.
`stCore3`: what the tied form of Theorem 2 (`ThreeSatPrinted.algPseudocode_decides_viaC`) says of
`SATCp ℓ τ` on codes is said of `core3 ℓ τ` on pairs (N in unary, formula). A formula ψ with
variables below N is `Decode.toN φ` for an instance φ; a run of `SATCp ℓ τ` on the code of φ is a
run of `core3 ℓ τ` on what the reader returns (`GraphProblems.runs_of_mapIn`),
and that is (N in unary, ψ). The code has length below 25·(N+2)^4, so the sizes of the states are
polynomial in N. Nothing about the algorithm is proved anew. Only the certificate of polynomial-time
steps is built again (`core3_polyTimeSteps`), because `ThreeSatPrinted.SATCp_polyTimeSteps` is for
the machine with the reader in front, and `core3 ℓ τ` has none. 

### `stCore3Eq`

 The machine of Theorem 2 is the reader of the input followed by `core3`: the statement
`SplitSat.StCore3Eq`. 

### `core3_polyTimeSteps`

 The steps of `core3 ℓ τ` are polynomial time. 

### `core3_decides`

 If `SATCp ℓ τ` decides 3-SAT on codes within c·2^{δn} steps, then `core3 ℓ τ` decides 3-SAT on
pairs (N in unary, formula) with the exponent δ. 

### `stCore3`

 **«Theorem 2 gives s_3 = 0»**, for the machine of Theorem 2 in its decision form without its
reader: for every δ > 0 there are ℓ and τ such that `core3 ℓ τ` has polynomial-time steps and
decides 3-SAT with the exponent δ. This is the statement `SplitSat.StCore3`; ℓ and τ are those of
`ThreeSatPrinted.algPseudocode_decides_viaC`. 
