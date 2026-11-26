---
{
  "module": "proof/maintheorem/NamesInOrder/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/NamesInOrder/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/NamesInOrder/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The Main Theorem when the variables are x₀ … x_(n−1) and each occurs: the end theorems

The theorems of Chain.lean with the inequalities of Arith.lean, the chain for every solver
(`MainRoute.bothBoundsOnEverySolver`), the statement on the pairs and Θ
(proof/variables/PairsToBound) in the places of their hypotheses. The inequalities and
`boundInMWithoutThePolynomial` are in Arith.lean, `builtIsAssembledDirectly` in Chain.lean,
`generalFormFollows` and `generalFormFollowsAsPropositions` in General.lean. 

### `everyDirectAlternationMeetsTheBound`

 **The main statement**: Corollary 11 from the first sentence of Theorem A (c) and Theorem D (b),
for every machine. 

### `onEverySolver`

 The chain for every solver. 

### `forAllPieces`

 The chain for all pieces of Appendix B. 

### `mainTheoremHolds`

 **The Main Theorem**. 

### `corMinHolds`

 **Corollary 11**. 

### `boundInMHolds`

 **The first sentence of Theorem A (c)**, at α′ = 1/2. 
