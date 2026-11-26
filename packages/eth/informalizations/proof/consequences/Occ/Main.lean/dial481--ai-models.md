---
{
  "module": "proof/consequences/Occ/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Occ/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Occ/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Variables that do not occur: «Z·2^{n'}» (proofs)

Every statement of proof/consequences/Occ/Defs.lean is proved here.
* `stSameAsFin`: for a formula φ with variables in `Fin N`, the variables that occur in
  `Decode.toN φ` are the values of the variables that occur in φ (`occEquiv`); carrying assignments
  along this bijection gives the equality of the two counts.
* `stCountOcc`: a formula on x₀ … xₙ₋₁ is `Decode.toN φ` for some φ (`GraphProblems.exists_toN`);
  its count on n variables is `SatK.numSat φ` (`CountKSat.stCntToN`); the sentence after Corollary
  11,
  `VariableBound.Rename.numSat_eq`, gives 2^(n−v)·Z in the vocabulary of `Fin N`, and `stSameAsFin`
  carries it over.
* The certificates: v is the length of the list of the variables with repetitions removed; n − v is
  at most n, which is given in unary, so 2^(n−v) is polynomial-time (`PolyT.two_pow`). 

### `mem_occurring`

 The variable v occurs in Φ if and only if some clause of Φ has a literal on v. 

### `lt_of_mem_occurring`

 In a formula on x₀ … xₙ₋₁ the variables that occur are below n. 

### `below_toN`

 A formula with variables in `Fin N`, read with numbers as variables, is a formula on x₀ …
x_(N−1). 

### `val_mem_occurring`

 The number i occurs in `Decode.toN φ` if and only if the variable xᵢ occurs in φ. 

### `occEquiv`

 The bijection between the variables that occur in `Decode.toN φ` (numbers) and the variables
that occur in φ (elements of `Fin N`): the number v goes to x_v. 

### `stNumOccLe`

 At most n variables occur in a formula on x₀ … xₙ₋₁. 

### `stSameAsFin`

 For a formula φ with variables in `Fin N`, the number of variables that occur in `Decode.toN φ`
is `MainTheoremForms.numOcc φ`, and the number of assignments of these variables that satisfy
`Decode.toN φ` is `MainTheoremForms.numSatOcc φ`. 

### `stCountOcc`

 «Z·2^{n'}»: a formula Φ on x₀ … xₙ₋₁ in which v variables occur has `Eight.numSat Φ`·2^(n−v)
satisfying assignments on x₀ … xₙ₋₁. 

### `stCountNil`

 «with no clause it has 2^n»: the formula without clauses has 2^n satisfying assignments on x₀ …
xₙ₋₁. 

### `stCountAllOccur`

 If every one of x₀ … xₙ₋₁ occurs in Φ and no other variable does, the number of satisfying
assignments on x₀ … xₙ₋₁ is `Eight.numSat Φ`. 

### `stNumOccCert`

 The number of variables that occur in Φ, written in unary, is computed from Φ in polynomial
time: list the variables of all literals, remove repetitions, take the length. 

### `numOcc_polyT`

 The number of variables of Φ that occur, as a number, is computed from ((n in unary, Φ), Z) in
polynomial time. 

### `free_unary`

 n − v in unary is computed from ((n in unary, Φ), Z) in polynomial time: it is at most n. 

### `twoPowFree_polyT`

 2^(n−v) is computed from ((n in unary, Φ), Z) in polynomial time. 

### `stTimesFreeCert`

 From ((n in unary, Φ), Z) the number Z·2^(n−v) is computed in polynomial time. 
