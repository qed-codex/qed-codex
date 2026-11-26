---
{
  "module": "proof/maintheorem/NamesInOrder/Chain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/NamesInOrder/Chain.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/NamesInOrder/Chain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Alternating two machines on the same input, and the chain of steps from a solver for cliques to the Main Theorem

The theorems `everyDirectAlternation_of`, `onEverySolver_of` and `forAllPieces_of` take the steps
that they need as hypotheses, named by the statements that they use; NamesInOrder/Main.lean supplies
them.
* `everyDirectAlternation_of`: both machines are started on the same word `SatM.enc k φ` and put out
  the same word, so a machine that runs them in alternation puts it out within q·(min(t₁, t₂) + L + 1)^q
  steps; `AlternationCostGoesIntoC` does the rest, and `VariableBound.Paper.corMinIsMainTheorem`
  passes from the bound of the Main Theorem to that of Corollary 11.
* `onEverySolver_of`: from `MainRoute.BothBoundsOnEverySolver`: its first clause gives the bound in
  m with a polynomial, its field `db` the bound of Theorem D (b) for every machine made as Step 6
  says, its field `exist` the machines.
* `forAllPieces_of`: the recursion of Appendix A on the pieces of Appendix B is an instance. 

### `everyDirectAlternation_of`

 Corollary 11 from the first sentence of Theorem A (c) and Theorem D (b), for every machine. 

### `builtIsAssembledDirectly`

 A machine that is built directly is assembled directly and has finite alphabets. 

### `onEverySolver_of`

 The chain for every solver. 

### `forAllPieces_of`

 The chain for all pieces of Appendix B: an instance of the chain for every solver. 

### `closed_of`

 The Main Theorem and Corollary 11, read off the chain with Theorem B. 

### `boundInMHolds_of`

 The first sentence of Theorem A (c), at α′ = 1/2, as a closed statement. 
