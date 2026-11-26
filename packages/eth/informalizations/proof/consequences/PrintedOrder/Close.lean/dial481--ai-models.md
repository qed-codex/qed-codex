---
{
  "module": "proof/consequences/PrintedOrder/Close.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/PrintedOrder/Close.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/PrintedOrder/Close.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Appendix C, Theorem C: the implication of proof/consequences/ThmCount/ applied

proof/consequences/ThmCount/ proves the implication from Theorem D(b) to Theorem C
(`ThmCount.stTheorem`) for every machine with the bound of Theorem D(b). Here it is applied to the
proof of Theorem D(b) (`RecursionWithPieces.Forms.thmVariablesB`). This is not the route of the
proof sketch of Appendix C. 

### `countRateFromBoundInN`

 **Theorem C**, in the wording of PaperSentencesStatement.lean: one algorithm computes the number
of satisfying assignments of a 3-CNF on n ≥ 2 variables in time 2^{O(n/(log n)^{1/20})}. It is
`ThmCount.stTheorem` applied to `RecursionWithPieces.Forms.thmVariablesB`. 
