---
{
  "module": "proof/consequences/SizeCircuit/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 7: the interface of proof/consequences/GraphProblems/ through Γ

Proofs of `StSizeGates` (CircuitDefs.lean) and of `StCircuitExists`, `StSizedFromEngine`,
`StSizedFromEngines` and `StSizedViaGamma` (Defs.lean). The paper: «All these formulas have O(n)
variables, so Corollary 6, applied with a small enough value in place of δ, gives time O(2^{δn}).»
Here the small enough value is δ/(a+1), where the circuit has at most a·(n+1) gates. 

### `stSizeGates`

 **`StSizeGates`.** The circuits `sizeGates n s` test the size with at most 6·(n+1) gates and are
computed in polynomial time. 

### `stCircuitExists`

 **`StCircuitExists`.** There is a family of circuits that tests the size with O(n) gates and is
computed in polynomial time: `sizeGates`. 

### `stSizedFromEngine`

 **`StSizedFromEngine`.** From Corollary 6 for machines cut into steps: for every family of
circuits that tests the size and is computed in polynomial time, every width w and every δ > 0,
there are a procedure E with polynomial-time steps, an exponent δ_E ≥ 0 with δ_E·(a+1) ≤ δ and a
constant c such that E serves as the procedure for #max(w,3)-SAT with δ_E and c, and
`sizedBy gates E` has polynomial-time steps and does what `GraphProblems.StSized` asks. (The proof
takes δ_E = δ/(a+1).) 

### `stSizedFromEngines`

 **`StSizedFromEngines`.** For every family En k ℓ τ of procedures of which Corollary 6 for
machines cut into steps holds, every family of circuits that tests the size and is computed in
polynomial time, every width w and every δ > 0: for some ℓ and τ the machine
`sizedBy gates (En (max w 3) ℓ τ)` has polynomial-time steps and does what `GraphProblems.StSized`
asks. 

### `stSizedViaGamma`

 **`StSizedViaGamma`.** With the circuits `sizeGates`: from Corollary 6 for machines cut into
steps, the interface `GraphProblems.StSized` of proof/consequences/GraphProblems/; the machine is
`sizedBy sizeGates E`. 
