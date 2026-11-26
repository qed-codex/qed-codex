---
{
  "module": "proof/networks/Eight/ViaGrouping/CorDefs2.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/CorDefs2.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/CorDefs2.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7: what Corollary 7, the circuit lower bound for E^NP and the sentence on NSETH ask of the procedures, and the verifier (definitions only)

The files proof/networks/Eight/ViaGrouping/CorGraph.lean, CorENP.lean and CorNSETH.lean prove
Corollary 7, the circuit lower bound for E^NP (Section 7) and «NSETH is false» for a procedure that
is a parameter. This file has the definitions that their
statements mention:
* `EngineCounts En`: what Corollary 6 for machines cut into steps says, of a family of machines En k
  ℓ τ for #k-SAT;
* `Decides M k δ c`: the same for k-SAT, of one machine;
* `verifier M`: the verifier for tautologies made from a machine M for k-SAT.
This file has no proofs. 

 ## Procedures for #k-SAT 

### `EngineCounts`

 Corollary 6 for machines cut into steps, said of a family of machines En k ℓ τ (k the width, ℓ a
level, τ a threshold parameter of the sparsification): for every k ≥ 1 and δ > 0 there are ℓ and τ
such that En k ℓ τ has polynomial-time steps and serves as
the procedure for #k-SAT with the exponent δ. 

 ## Machines for k-SAT 

### `Decides`

 The machine M, cut into steps, decides k-SAT with the exponent δ and the constant c: on the code
of a k-CNF φ on n variables it ends within c·2^{δn} steps, on states of size at most c·(length of
the code + 1)^c, with the bit «φ is satisfiable». 

 ## The verifier 

### `verifier`

 The verifier for the tautologies among the k-DNF formulas made from a machine M for k-SAT: take
the witness off and ignore it, run M on the rest, and answer with the opposite bit, as a word of one
bit. 
