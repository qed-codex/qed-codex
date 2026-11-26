---
{
  "module": "proof/variables/RecursionToBound/Cert/Top.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Cert/Top.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Cert/Top.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The function of Theorem D (a), with the sparsification of Step 5 of Appendix D, is polynomial-time

`countIsPolynomialTime : CountIsPolynomialTime`: for every polynomial-time solver S, every n₁ and
all polynomial-time `pick` and `num`, the function `count S n₁ pick num` of (input, padding string)
and its exponent `expo S n₁ pick num` (proof/variables/RecursionToBound/Defs.lean) are
polynomial-time, **on all inputs**, whether or not they are codes of formulas in the range of
Theorem D (a).

* `DeltaOf_unary`: «Δ the larger of 2 and the largest number of its clauses in which one variable
  occurs» (Step 5 of Appendix D) is the maximum of a list (`DeltaOf_eq`) and at most the number of
  clauses plus 2, so it is given in unary.
* `countOutput_polyT`: the count of one output. The output at a node is a list without repetitions
  made from the node; Steps 2 to 4 are polynomial-time jointly in k, n and Δ in unary, the padding
  string, the index and the formula (`VariableBound.StCertCountD`, proved as
  `VariableBound.certCountDc`).
* `countAll_polyT`: the walk that adds these counts (`walkSG_polyT`).
* `count_polyT`: without a plan, exhaustive counting (`CountKSatRate.Cert.bruteN_polyT_aux`); the
  result is written in n + 1 bits.

Here the pair r (the argument `r : ℕ × ℕ` of `countAll`, computed by `numU`) is given in binary,
each output has its own Δ, and the width is read from the formula. 

 ### The Δ of an output 

### `occN_polyT`

 The number of clauses in which a variable occurs is polynomial-time. 

### `foldr_max_map_le`

 The maximum of a list of values that are all at most b is at most b. 

### `DeltaOf_le`

 The Δ of a formula is at most its number of clauses plus 2. 

### `DeltaOf_polyT`

 The Δ of a formula is polynomial-time jointly in n and the formula, if n is given in unary. 

### `DeltaOf_unary`

 The Δ of a formula is given in unary. 

### `out_polyT`

 The output at a node is polynomial-time. 

 ### The count 

### `countOutput_polyT`

 The count of the output at a node is polynomial-time jointly in k, the padding string, the
index, n and the node, if k and n are given in unary; given the certificate of Steps 2 to 4. 

### `countAll_polyT`

 The sum of the counts of all outputs is polynomial-time jointly in k, r, the index, the decoded
formula and the padding string, if k and 2^k are given in unary. 

### `count_polyT`

 The function of (input, padding string) is polynomial-time, given the certificate of Steps 2 to 4. 

### `countIsPolynomialTime`

 The function and its exponent are polynomial-time in (input, padding string), on all inputs, for
every n₁, if the solver, `pick` and `num` are. 
