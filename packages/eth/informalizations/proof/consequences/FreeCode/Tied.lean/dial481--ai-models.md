---
{
  "module": "proof/consequences/FreeCode/Tied.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Tied.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Tied.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Corollary 5 with the code that does not depend on k, tied to its machines

The proof of Corollary 5 in the paper: «… Theorem 2 gives s_3 = 0 … s_3 = 0 implies s_k = 0 for
every k ≥ 3; the reduction (sparsify, then split every long clause into clauses of 3 literals with
new variables) …».
* `tied_of_decidesW`: any procedure D with polynomial-time steps that decides w-SAT on (N in unary,
  formula) with the exponent δ/2, put behind the reader `readFree`: the machine has polynomial-time
  steps and decides w-SAT on codes with the exponent δ; a Turing machine simulates it and decides
  w-SAT within ⌊c·2^{δn}⌋ steps.
* `stTiedThree` (= `FreeCode.StTiedThree`): D = `core3 ℓ τ`, the machine of Theorem 2 in its
  decision form without its own reader, by `SplitSat.stCore3`.
* `stTied` (= `FreeCode.StTied`): D = the reduction on `core3`, by `SplitSat.stSparsifyK`,
  `SplitSat.stCore3` and `SplitSat.stReduceCore`. 

### `tied_of_decidesW`

 A procedure D with polynomial-time steps that decides w-SAT on (N in unary, formula) with the
exponent δ/2, behind the reader `readFree`: there are a Turing machine M with finite alphabets and
c, q such that the machine behind the reader has polynomial-time steps and decides w-SAT on codes
with the exponent δ and the constant c, M simulates it with polynomial overhead, and M decides w-SAT
on codes within ⌊c·2^{δn}⌋ steps. 

### `stTiedThree`

 **«Theorem 2 gives s_3 = 0»**, for the code that does not depend on k, tied to the machine of
Theorem 2 in its decision form behind the reader: the statement `FreeCode.StTiedThree`. In the proof
the named machine has the exponent δ/2. 

### `stTied`

 **Corollary 5, tied to the reduction**, for the code that does not depend on k: the statement
`FreeCode.StTied`. With ε = (δ/2)/3 the tree at width k has at most 2^{εn} leaves of at most B·n
clauses; the machine of Theorem 2 in its decision form is taken with the exponent δ₃ = ε/(1 +
(k−3)·B). In the proof the named machine has the exponent δ/2. 
