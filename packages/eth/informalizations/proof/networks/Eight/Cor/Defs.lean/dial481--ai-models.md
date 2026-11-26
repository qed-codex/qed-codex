---
{
  "module": "proof/networks/Eight/Cor/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Cor/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Cor/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7: the input of a verifier and the specification of a procedure for #k-SAT (definitions only)

It defines `stripW`, which takes the witness off the input of a verifier; `Serves`, what a machine
must do to serve as the procedure for #k-SAT with a given exponent and constant; and `StEngine`,
Corollary 6 for machines cut into steps,
with the machine left open. This file has no theorem. It imports the statement files of the
corollaries and files of proof/consequences/WidthK/, proof/consequences/CountKSat/,
proof/consequences/GraphProblems/ and proof/consequences/CircuitLowerBound/. 

### `stripW`

 Takes the witness off the input of a verifier: from 1^{|w|} 0 w x it returns x. 

### `Serves`

 What a machine E must do to serve as the procedure for #k-SAT with the exponent δ and the
constant c: on (N in unary, ψ), for ψ with clauses of at most k literals, variables below N and no
clause written twice, it returns the number of satisfying
assignments on N variables in N + 1 bits, within c·2^{δN} steps and on states of size at most
c·(N+2)^c. 

### `StEngine`

 Corollary 6 for machines cut into steps, with the machine left open: for every k ≥ 1 and δ > 0
some machine with polynomial-time steps serves. 
