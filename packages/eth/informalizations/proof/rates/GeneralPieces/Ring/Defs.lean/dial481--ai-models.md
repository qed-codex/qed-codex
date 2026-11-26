---
{
  "module": "proof/rates/GeneralPieces/Ring/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The ring of Appendix B and the matrices of `ClauseBound.Boson.op`: the interface between them

The proof of the bound in m in `ClauseBound.Boson.Defs2` has no ring: an operator is its integer
matrix in the basis of the monomials, indexed by multisets of natural numbers without 0. `StBridge`
says that these
are the matrices of the operators a[r] that `AppHalfPiecesStatement.lean` defines on ℚ[t₁, t₂, …] by
display (47). Nothing is proved here. 

### `toN`

 A partition as a multiset of natural numbers. 

### `toL`

 The parts of a monomial as natural numbers. 

### `StBridge`

 The coefficient of t^π in a[r]·t^σ, a the monomial with the parts listed, is the entry (π, σ) of
the matrix `ClauseBound.Boson.op`. 
