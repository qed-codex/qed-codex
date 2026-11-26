---
{
  "module": "proof/threesat/Given/Networks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Given/Networks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Given/Networks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The three statements of GivenStatement.lean

* `stOnGiven`: the count of operations is `Printed.stOnProcedures` for the procedures with the
  oracle built in, read as own steps plus queries (`QueryMachines.stClose`,
  `Printed.networkOn_close`); the polynomial-time steps are `Printed.networkOn_poly`;
* `stGridGiven`: `Printed.grid_isNetwork_of` and the certificates of the four procedures `gridProcs`
  (`gridProcs_poly`);
* `stFormulaGiven`: `Printed.formula_isNetwork` and `Printed.formulaProcs_keeps`;
* `onClosed`, `onSteps`: `stOnGiven` read for the step machine with the oracle built in, and for
  procedures that are step machines. 

### `ofProcs_poly`

 Step machines with polynomial-time steps and numbers in unary, as procedures that ask nothing. 

### `stOnGiven`

 **Lemma 1, applied to a network given in the sense of `IsGivenNetwork`.** 

### `gridProcs_poly`

 The four procedures of the row network and the column network of ι have polynomial-time steps,
and their numbers are given in unary. 

### `stGridGiven`

 **«Both networks satisfy Definition 2 with P = g³λ (so gP = N), with B₁ = gB + g²λ + 1 in the
role of B, and with τ = poly(B + λ)»**, Definition 2 being `IsGivenNetwork`. 

### `stFormulaGiven`

 **Section 6, «Definition 2 holds»**, of the network of Φ, Definition 2 being `IsGivenNetwork`. 

### `onClosed`

 `stOnGiven`, the count of operations, read for the step machine with the oracle built in. 

### `onSteps`

 `stOnGiven` for procedures that are step machines: polynomial-time steps of the step machine
`networkOnSteps g NM Np` and the number of its steps, in one conclusion. 
