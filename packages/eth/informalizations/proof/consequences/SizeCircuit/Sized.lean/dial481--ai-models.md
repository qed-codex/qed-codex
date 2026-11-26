---
{
  "module": "proof/consequences/SizeCircuit/Sized.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/Sized.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/Sized.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 7: «Corollary 6 then counts …»

Proof of `StSizedBy` of proof/consequences/SizeCircuit/Defs.lean: for every procedure E that serves
for #max(w,3)-SAT with a small enough exponent, the machine `sizedBy gates E` (ONE call of E on ψ ∧
Γ) returns the number of satisfying assignments of ψ with exactly s true variables within c'·2^{δn}
steps. The paper: «All these formulas have O(n) variables, so Corollary 6, applied with a small
enough value in place of δ, gives time O(2^{δn}).»

The number is right by `stGammaCount`; ψ ∧ Γ has width at most max(w,3) and N ≤ (a+1)·(n+1)
variables by `stGamma`; so δ_E·N ≤ δ·(n+1). Three small facts come from
proof/consequences/GraphProblems/Sized.lean (`cntN_dedup`, `cntN_le`, `ofWord_binary`: striking out
repeated clauses keeps the count, the count is at most 2^N, and a number written in N + 1 bits reads
back as itself). They do not use the other machine of that file (`GraphProblems.sized`, through
blocks). 

### `le_numVars`

 Γ has the variables x₀ … xₙ₋₁ among its variables. 

### `numVars_le`

 Γ has at most (a+1)·(n+1) variables. 

### `shaped_gamma`

 Γ is a 3-CNF on its variables, also for n = 0. 

### `stSizedBy`

 **`StSizedBy`.** Let gates test the size with at most a·(n+1) gates and let E serve as the
procedure for #max(w,3)-SAT with an exponent δ_E ≥ 0 such that δ_E·(a+1) ≤ δ. Then `sizedBy gates E`
returns, on (n in unary, s, ψ) for s ≤ n and ψ of width at most w on x₀ … xₙ₋₁, the number of
satisfying assignments of ψ with exactly s true variables, within c'·2^{δn} steps and on states of
size at most c'·(n + number of clauses + 2)^{c'}. 
