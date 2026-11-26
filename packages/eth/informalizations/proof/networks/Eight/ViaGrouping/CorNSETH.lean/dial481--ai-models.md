---
{
  "module": "proof/networks/Eight/ViaGrouping/CorNSETH.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/CorNSETH.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/CorNSETH.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, the sentence after Corollary 5: NSETH is false, from a machine for k-SAT that is a parameter

The paper: NSETH «is false as well: a k-DNF is a tautology exactly if its negation, a k-CNF, is
unsatisfiable, and a deterministic algorithm is in particular a nondeterministic one». The
definitions are in proof/networks/Eight/Cor/NSETHDefs.lean; the first half of the
sentence is `Eight.tautology_iff` (proof/networks/Eight/Cor/NSETH.lean), which does not use any
algorithm and is not repeated. The second half is proved here for a machine M for k-SAT, cut into
steps, that is a parameter (definitions in proof/networks/Eight/ViaGrouping/CorDefs2.lean):
* `Decides M k δ c`: M decides k-SAT on n variables within c·2^{δn} steps, on states of polynomial
  size;
* `verifier M`: take the witness off the input and ignore it, run M on the rest, answer with the
  opposite bit;
* `verifier_recognizes`, `tautInNTimeTM_of`, `not_NSETH_TM_of`. The lines are those of
  proof/networks/Eight/Cor/NSETH.lean with M in the place of the machine named there.
The proofs in this file name no algorithm for cliques or for networks.

Different from the paper: the negation of a k-DNF ψ is the k-CNF with the same lists and all
literals negated. That formula is satisfiable exactly if the k-CNF with the same lists and the same
literals is (negate the assignment), so the
machine runs on the code of ψ as it stands. 

### `verifier_polyTimeSteps`

 The verifier has polynomial-time steps if M has. 

### `verifier_recognizes`

 **The verifier.** If M decides k-SAT with the exponent δ and the constant c, then `verifier M`,
on every witness w and the code of a k-DNF ψ on n variables, ends within c·2^{δn} steps with the bit
«ψ is a tautology». 

### `tautInNTimeTM_of`

 «A deterministic algorithm is in particular a nondeterministic one»: if a machine M with
polynomial-time steps decides k-SAT with the exponent δ/2, then the tautologies among the k-DNF
formulas on n variables are recognized in nondeterministic time O(2^{δn}).
The Turing machine simulates `verifier M`. If ψ is a tautology, the empty witness is accepted in
time; if some witness is accepted, the answer of the machine, which is the same on all witnesses, is
«tautology». 

### `not_NSETH_TM_of`

 **NSETH is false** (the sentence after Corollary 5), for Turing machines and nondeterministic
time in verifier form (`NSETH_TM` of proof/networks/Eight/Cor/NSETHDefs.lean), if for every k ≥ 1
and δ > 0 some machine with polynomial-time steps decides k-SAT with the exponent δ. 
