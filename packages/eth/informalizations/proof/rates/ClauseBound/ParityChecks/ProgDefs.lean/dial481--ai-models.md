---
{
  "module": "proof/rates/ClauseBound/ParityChecks/ProgDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/ProgDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/ProgDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One sparse formula counted through parity checks: the program, and the interface lemmas

ψ has m clauses of 1 to k literals on n variables, and every variable occurs in at most Δ clauses.
The parameters q = (m, nb, r, i₀, β) are those of `parOf n Δ m` (r = 0 if m ≤ nb). Every sum
over marks is one evaluation `evW`: the sum, over the admissible profiles of the network of marks of
up to three layers on n + r variables (lists of clauses: ψ, the incidences of the checks as clauses
`incL`, and a suffix of ψ), of a weight times the value of the network, which a clique solver
computes. 

### `rep`

 n in unary. 

### `parQ`

 The parameters; no checks if m ≤ nb. 

### `capM`

 The cap for the marks of the incidences, and for all layers. 

### `blkOL`

 The length of the blocks of the code of the labels, and the number of bits of a position in a
block. 

### `colMax`

 Bounds for the number of checks that contain a clause and for the number of clauses of a check,
in every state that is tried, if r ≤ 6n, m ≤ Δn and n < 2·nb·LD Δ. They do not depend
on the formula, so that one exponent of the pad serves all sparse formulas that come from one input. 

### `occOL`

 A bound for the number of clauses of the three layers in which a variable occurs. 

### `parM`

 (number of variables, cap, code parameters) in unary, for the network of marks. 

### `UbOL`

 Bounds for U and P of the networks, if r ≤ 6n and the cap is at most 11n. 

### `evW`

 One evaluation: `truncW (n + r) ws lo hi Ls` when the pad is long enough. 

### `orcA`

 The two functions that the choice of the checks asks. 

### `runToF`

 The choice of the checks, with every growing list cut off by the pad. 

### `countOL`

 The number of satisfying assignments of ψ among the 2ⁿ assignments. 

 ### Ev.lean 

### `StEvW`

 One evaluation is exact on three layers (or two) of clauses of 1 to k + 1 literals on n + r
variables in which no variable occurs too often. 

 ### Shape.lean: the layers of a state that is tried have the form that `StEvW` asks 

 ### Count.lean 

### `FitsOL`

 What the count for one formula needs of the length F of the pad. 

### `StCountOL`

 The count is right. `Hyp` is what the choice of the checks needs of the parameters. 

 ### CertOL.lean 
