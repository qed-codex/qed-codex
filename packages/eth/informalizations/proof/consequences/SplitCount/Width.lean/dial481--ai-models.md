---
{
  "module": "proof/consequences/SplitCount/Width.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Width.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Width.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Corollary 6: the width reduction (the part beginning «Second» in its proof)

«each of these is turned into a 3-CNF with O(n) clauses and O(n) variables and the same number of
satisfying assignments, by the standard width reduction, which introduces a constant number of new
variables for each clause. The number is preserved if each new variable is forced, by three clauses
of at most 3 literals, to equal the disjunction of the two literals that it replaces in a long
clause»
The width reduction and its properties are those of proof/networks/Eight/Cor/Width.lean
(`Eight.Width.stWidth`), for formulas with variables in `Fin n`; the program `Eight.Width.widthP` on
formulas with numbers as variables gives the same formula (`Eight.Width.toN_widthReduce`) with the
same count (`Eight.Width.cntN_splitN`).
A formula on x₀ … xₙ₋₁ is `Decode.toN φ` for some φ (`GraphProblems.exists_toN`). 

### `stStepThree`

 **The width reduction of Corollary 6**, for the program: on Ψ on x₀ … xₙ₋₁ with m clauses of ≤ w
literals, `widthP` gives (n₃ in unary, Ψ₃): ≤ 3 literals per clause, variables below n₃, no clause
twice, n₃ ≤ n + (w−3)·m, ≤ m + 3(w−3)·m clauses, and as many satisfying assignments on n₃ variables
as Ψ on n. 
