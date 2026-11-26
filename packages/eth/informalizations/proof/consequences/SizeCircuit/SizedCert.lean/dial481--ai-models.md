---
{
  "module": "proof/consequences/SizeCircuit/SizedCert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/SizedCert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/SizedCert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 7: ψ ∧ Γ is written in polynomial time

Proof of `StSizedCert` of proof/consequences/SizeCircuit/Defs.lean: if the circuits are computed in
polynomial time, then so is (n in unary, s, ψ) ↦ (number of variables in unary, ψ ∧ Γ), and the
steps of `sizedBy gates E` are polynomial time if those of E are. The paper does not say this; it is
needed because the formula is written by a machine. 

### `gateClauses_polyT`

 The four clauses of a gate are polynomial time in (the number of its wire, the gate). 

### `wiresFormula_polyT`

 The clauses of all gates are polynomial time in (n in binary, the circuit). 

### `formulaOf_polyT`

 The formula of a circuit is polynomial time in (n in binary, the circuit). 

### `withGamma_polyT`

 (n in unary, s, ψ) ↦ (number of variables in unary, ψ ∧ Γ) is polynomial time if the circuits
are. 

### `stSizedCert`

 **`StSizedCert`.** The steps of `sizedBy gates E` are polynomial time if those of E are and the
circuits are computed in polynomial time. 
