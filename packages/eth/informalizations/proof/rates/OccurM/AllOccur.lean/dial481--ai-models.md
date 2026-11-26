---
{
  "module": "proof/rates/OccurM/AllOccur.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/OccurM/AllOccur.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/OccurM/AllOccur.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Back to the formulas in which every variable occurs

Let M count as in `ClausesOccur.CountsUnaryFor α`, on the code with N in unary. If all n variables
of φ occur then n is the number of variables that occur and the two ways of counting agree
(`VariableBound.Rename.allOccurStmt`), n ≤ k·m
(`ClauseBound.Alg.End.n_le`), and the code has at most 8·(k·m)² bits
(`ClauseBound.Alg.End.length_enc_succ_le`); so the polynomial in the length of the formula is
absorbed (`OccurM.back_le`). The machine is the same. 

### `allOccurOfUnary`

 What a machine that counts as in `ClausesOccur.CountsUnaryFor α`, on the code with N in unary,
gives for the formulas in which every variable occurs, for the same machine: the body of
`SatM.CountInRate` for m ≥ 2, with the constant 650·C + 1. 
