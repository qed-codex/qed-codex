---
{
  "module": "proof/variables/RecursionWithPieces/Forms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionWithPieces/Forms.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionWithPieces/Forms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (b) and the joint bound of Theorem 1, Theorem D (b) and Corollary 11, through the function for Theorem 1 on the recursion of Appendix A with the pieces of Appendix B

This file holds two theorems. The step `together_of` to the paper's form, applied to
`SatM.targetUniform_all`, gives `togetherAllOccur`: one machine and one constant C satisfy the
bounds of Theorem 1, of Theorem D (b) and of Corollary 11
for formulas over x₀ … xₙ₋₁ that all occur. `thmVariablesB`, Theorem D (b), is read off from it.

Each of the two statements says that some machine exists and names none of the objects of
proof/variables/RecursionWithPieces. Their proofs go through `RecursionWithPieces.tiedAllCal`, of
which
`SatM.targetUniform_all` is a corollary; this is seen in the proofs, not in the statements. 

### `togetherAllOccur`

 Through `RecursionWithPieces.tiedAllCal`: ONE machine and ONE constant C satisfy the bound of
Theorem 1, the bound of Theorem D (b) and the bound of Corollary 11, for formulas over x₀ … xₙ₋₁.
Names none of the objects of proof/variables/RecursionWithPieces. 

### `thmVariablesB`

 Through `RecursionWithPieces.tiedAllCal`: Theorem D (b), the conclusion. Names none of the
objects of proof/variables/RecursionWithPieces. 
