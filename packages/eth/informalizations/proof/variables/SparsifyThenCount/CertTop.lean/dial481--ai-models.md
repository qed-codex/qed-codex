---
{
  "module": "proof/variables/SparsifyThenCount/CertTop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/SparsifyThenCount/CertTop.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/SparsifyThenCount/CertTop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The function `ADG Θ` is polynomial-time for every family of thresholds Θ that serves

`stCertDG : StepSparsify.StCertWalkSG → StepSparsify.StCertNoTaut → VariableBound.StCertCountD → StCertDG`.
The lemmas on the parameters and on the plan are taken from
proof/variables/VariableBound/Cert/Top.lean. Three
points are particular to this function. The walk has the thresholds Θ k s. Its certificate (a
hypothesis, `StepSparsify.StCertWalkSG`) asks for the precision s in unary instead of τ in binary; s
is the length of a list of units that is
computed in polynomial time. The root of the tree is the formula without the clauses that contain a
variable together with its negation, and deleting them is polynomial-time by the hypothesis
`StepSparsify.StCertNoTaut`. The exponent function
`VariableBound.eD` is the one of proof/variables/VariableBound; `eD_polyT` proves its certificate
with no hypothesis on a walk. 

### `planD_polyT`

 The plan, as a function of the input, is polynomial-time, if the solver, `pick` and `slU` are. 

### `eD_polyT`

 The exponent function of the input for the bound in n is polynomial-time, if the solver, `pick`
and `slU` are. 

### `stCertDG`

 For thresholds that serve, the function `ADG Θ` of (input, pad) is polynomial-time if the
solver, `pick` and `slU` are; given the certificates of the walk (`StepSparsify.StCertWalkSG`), of
the deletion of the clauses that contain a variable
together with its negation (`StepSparsify.StCertNoTaut`) and of the count of one sparse formula by
Steps 1 to 4 (`VariableBound.StCertCountD`). 
