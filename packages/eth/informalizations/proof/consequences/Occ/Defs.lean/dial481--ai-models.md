---
{
  "module": "proof/consequences/Occ/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Occ/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Occ/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Variables that do not occur: «Z·2^{n'}» (definitions and statements only)

The paper uses one fact in three places. Section 6: «Φ has Z·2^{n'} satisfying assignments, where n'
of the n variables do not occur in Φ».
Appendix C: an output in which v of the n variables occur «has Z·2^{n−v} satisfying assignments».
After Corollary 11: the same with N − n.
Here Z is, as in Section 6, «the number of assignments of the variables occurring in Φ that satisfy
Φ» (`Eight.numSat Φ`), and the number of satisfying assignments on x₀ … xₙ₋₁ is
`CountKSat.cntN n Φ`, the form in which the counting programs of this development speak.
A formula is a list of clauses, a clause a list of literals (variable, value that makes the literal
true), with natural numbers as variables (`Groundwork.Prog.Fml`).

For formulas with variables in `Fin N` the identity is stated in MainTheoremFormsStatement.lean and
proved in proof/variables/VariableBound/Paper/Rename/Math.lean. This file adds the form for
programs, the bridge between the two forms (`StSameAsFin`),
and the certificate that the factor is computed in polynomial time when n is given in unary
(`StTimesFreeCert`).
This file has no theorem: every statement is a `def St… : Prop`; proof/consequences/Occ/Main.lean
proves them. 

### `Below`

 All variables of Φ are among x₀ … xₙ₋₁. 

### `numOcc`

 v: the number of variables that occur in Φ. 

### `StNumOccLe`

 At most n variables occur in a formula on x₀ … xₙ₋₁. 

### `StCountOcc`

 **«Z·2^{n'}».** A formula on x₀ … xₙ₋₁ in which v variables occur has Z·2^{n−v} satisfying
assignments, Z the number of assignments of the occurring variables that satisfy it. No condition on
the width or on the number of clauses:
with no clauses, Z = 1 and v = 0, and the number is 2^n. 

### `StCountNil`

 With no clauses the number is 2^n. 

### `StCountAllOccur`

 If every one of x₀ … xₙ₋₁ occurs, the two ways of counting agree. 

### `StSameAsFin`

 The two vocabularies of this development say the same: for a formula with variables in `Fin N`,
read with numbers as variables (`Decode.toN`), v and Z are `MainTheoremForms.numOcc` and
`MainTheoremForms.numSatOcc` of MainTheoremFormsStatement.lean. 

### `timesFree`

 The last step of a program that has computed Z for the formula Φ on n variables: from ((n in
unary, Φ), Z) the number Z·2^{n−v}. 

### `StTimesFreeCert`

 That step is polynomial-time. 

### `StNumOccCert`

 v in unary is computed in polynomial time. 
