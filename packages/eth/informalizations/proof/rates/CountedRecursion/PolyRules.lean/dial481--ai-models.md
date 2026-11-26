---
{
  "module": "proof/rates/CountedRecursion/PolyRules.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PolyRules.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PolyRules.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Rules for polynomial-time steps

proof/machines/QueryMachines/Poly.lean has a certificate (`IsPolyQ`, a class that holds the coding
of the states) for every construction. Here each of them is restated for the statement
`PolyTimeSteps` (there is a certificate), so that the certificate of a machine can be written along
its definition, one rule for each construction, with the plain functions left to `fun_prop`. Also:
`askInt`, `askList`, `readAs`. 

### `lift_poly`

 A step machine with polynomial-time steps, seen as a machine that asks nothing. 

### `ofFun_poly`

 One step that applies a polynomial-time function. 

### `query_poly`

 A single query, computed in polynomial time from the input. 

### `mapAsk_poly`

 Queries rewritten by a polynomial-time function. 

### `mapIn_poly`

 A polynomial-time function applied to the input. 

### `mapOut_poly`

 A polynomial-time function applied to the result. 

### `bind_poly`

 One machine after the other. 

### `branch_poly`

 A choice between two machines by a polynomial-time function of the input. 

### `ite_poly`

 A choice by a polynomial-time test. 

### `const_poly`

 A constant. 

### `foldRange_poly`

 The loop over a range, if the range, the update and the start are polynomial-time. 

### `sumRange_poly`

 The sum over a range. 

### `prodRange_poly`

 The product over a range. 

### `subst_poly`

 Queries answered by a machine with query access. 

### `readAs_poly`

 Answers read by a polynomial-time function. 

### `asInt_polyT`

 An answer read as an integer. 

### `asList_polyT`

 An answer read as a list of integers. 

### `askInt_poly`

 One query, its answer read as an integer. 

### `askList_poly`

 One query, its answer read as a list of integers. 
