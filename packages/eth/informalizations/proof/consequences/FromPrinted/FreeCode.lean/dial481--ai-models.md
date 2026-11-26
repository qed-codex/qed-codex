---
{
  "module": "proof/consequences/FromPrinted/FreeCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/FreeCode.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FromPrinted/FreeCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Corollary 5 with an input code of the formulas that does not depend on k (read by the reader `readFree`), tied to the machine `Printed.SAT`, which decides with Algorithm 1

The proof in the paper: «Theorem 2 gives s_3 = 0 … s_3 = 0 implies s_k = 0 for every k ≥ 3; the
reduction (sparsify, then split every long clause into clauses of 3 literals with new variables) …».
What proof/consequences/FreeCode/ proves for every procedure D (`FreeCode.tied_of_decidesW`: D
behind the reader `readFree`, and a Turing machine that simulates it) is used as it stands.
* `stTiedThree` (= `FromPrinted.FreeCode.StTiedThree`): D = `core3 ℓ τ`, the machine of Theorem 2 in
  its decision form without its own reader, by `FromPrinted.SplitSat.stCore3`.
* `stTied` (= `FromPrinted.FreeCode.StTied`): D = the reduction on `core3`, by
  `SplitSat.stSparsifyK`, `FromPrinted.SplitSat.stCore3` and `SplitSat.stReduceCore`.
* `allZeroFrom`, `allZero`: Corollary 5, first with the two tied statements as hypotheses, then
  applied to their proofs: s_3 = 0 from `StTiedThree` (Theorem 2), s_k = 0 for k > 3 from `StTied`
  (the reduction).
* `allZeroRandomized`: from `SatFree.randomnessHelps` and `allZero`. 

### `stTiedThree`

 **«Theorem 2 gives s_3 = 0»**, for the code that does not depend on k, tied to the machine of
Theorem 2 in its decision form behind the reader: for every δ > 0 there are a polynomial-time reader
of the code, ℓ and τ such that `core3 ℓ τ` behind the reader itself has polynomial-time steps and
decides 3-SAT with the exponent δ, a Turing machine with finite alphabets simulates it with
polynomial overhead, and that Turing machine decides 3-SAT within ⌊c·2^{δn}⌋ steps. This is the
statement `FromPrinted.FreeCode.StTiedThree`. In the proof the named machine has the exponent δ/2. 

### `stTied`

 **Corollary 5, tied to the reduction**, for the code that does not depend on k: for every k ≥ 3
and δ > 0 there are a polynomial-time reader of the code, τ, ℓ₃ and τ₃ such that the reduction
(sparsify at width k with the threshold parameter τ, split every long clause, ask `core3 ℓ₃ τ₃`)
behind the reader itself has polynomial-time steps and decides k-SAT with the exponent δ, a Turing
machine with finite alphabets simulates it with polynomial overhead, and that Turing machine decides
k-SAT within ⌊c·2^{δn}⌋ steps. This is the statement `FromPrinted.FreeCode.StTied`. With ε = (δ/2)/3
the tree at width k has at most 2^{εn} leaves of at most B·n clauses; the machine of Theorem 2 in
its decision form is taken with the exponent δ₃ = ε/(1 + (k−3)·B). In the proof the named machine
has the exponent δ/2. 

### `allZeroFrom`

 **Corollary 5 from the two tied statements**, which are hypotheses here: «s_k = 0 for every k ≥ 3.
Hence s_∞ = 0, and both ETH and SETH are false», for the numbers s_k defined with the code that does
not depend on k. At k = 3 the Turing machine is that of `StTiedThree` («Theorem 2 gives s_3 = 0»),
at k > 3 that of `StTied` (the reduction); then the general `SatFree.s_eq_zero_of`. Nothing else is
known of the machines. 

### `allZero`

 **Corollary 5**: «s_k = 0 for every k ≥ 3. Hence s_∞ = 0, and both ETH and SETH are false», for
the numbers s_k defined with the code that does not depend on k. It is `allZeroFrom` applied to
`stTiedThree` (Theorem 2) and `stTied` (the reduction). 

### `allZeroRandomized`

 «and Corollary 5 holds under each of these conventions»: with randomized algorithms with error
at most p, for every p ≥ 0, s_k = 0 for every k ≥ 3. 
