---
{
  "module": "proof/consequences/FromPrinted/Verifier.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/Verifier.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/Verifier.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sentence on NSETH after Corollary 5: the machines, on `Printed.SAT`, the deciding form of Algorithm 1

«a k-DNF is a tautology exactly if its negation, a k-CNF, is unsatisfiable, and a deterministic
algorithm is in particular a nondeterministic one»
* `stVerifier`: for k ≥ 3 the machine for k-SAT is `FromPrinted.SplitSat.SATsplit`
  (`FromPrinted.SplitSat.stSATsplit`), the reduction to 3-SAT run on the machine of Theorem 2 in its
  decision form; the verifier made from it has polynomial-time steps
  (`Eight.ViaGrouping.verifier_polyTimeSteps`) and returns, on every witness and the code of a k-DNF
  ψ, the bit that says whether ψ is a tautology (`Eight.ViaGrouping.verifier_recognizes`).
* `stSmallWidths`: for 1 ≤ k ≤ 3 the machine is the reader for width k followed by the machine of
  Theorem 2 in its decision form without its reader (`FromPrinted.SplitSat.stCore3`): a k-CNF with k
  ≤ 3 is a 3-CNF.
* `nsethFrom`, `nsethFalse`: «NSETH … is false as well», by `Eight.ViaGrouping.not_NSETH_TM_of`,
  first from the two statements as hypotheses, then on their proofs. 

### `stVerifier`

 **The verifier for tautologies, with the machine named**: for every k ≥ 3 and δ > 0 there are τ,
ℓ₃, τ₃, c such that `SATsplit k τ ℓ₃ τ₃` has polynomial-time steps and decides k-SAT with the
exponent δ and the constant c, and the verifier made from it has polynomial-time steps and, on every
witness w and the code of a k-DNF ψ on n variables, ends within c·2^{δn} steps, on states of size at
most c·(length of the code + 1)^c, with the bit that says whether ψ is a tautology. 

### `stSmallWidths`

 For 1 ≤ k ≤ 3 and δ > 0 there are ℓ, τ, c such that `SATsmall k ℓ τ` has polynomial-time steps
and decides k-SAT with the exponent δ and the constant c. 

### `nsethFrom`

 **«NSETH … is false as well»** (the sentence after Corollary 5), for Turing machines and
nondeterministic time in verifier form (`Eight.NSETH_TM`), from the two statements that name the
machines, as hypotheses: the machine for k-SAT is that of `StSmallWidths` for k ≤ 3 and that of
`StVerifier` for k > 3. 

### `nsethFalse`

 **«NSETH … is false as well»**: `nsethFrom` on the proofs `stVerifier` and `stSmallWidths`. 
