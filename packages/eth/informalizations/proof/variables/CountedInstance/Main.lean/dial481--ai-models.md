---
{
  "module": "proof/variables/CountedInstance/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/CountedInstance/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/CountedInstance/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The recursion of Theorem A (b) on the pieces of Appendix B meets the hypothesis of Theorem D (a)

* `theRecursionMeetsTheHypothesisFrom`: Theorem B in counted operations, for the functions of its
  proof, gives a constant c and pieces D₀ with parameters (1/√2, c). «We may and do assume …» gives
  pieces D with parameters (1/√2, c + 2), the same d, 𝓘 and A_s, and all numbers of bits at most 2λ.
  Take x₀ = c + 18, so that x₀ ≥ 18 and 2^{x₀} ≥ c + 7 = (c + 2) + 5. Theorem A (b) in counted
  operations gives a constant C₀, which depends on c + 2 only, for the machine
  `cliqueMachine (c + 2) x₀ Alg`. The constant is replaced by the larger of C₀ and 10, and the
  clauses on numbers hold for it.
* `theRecursionMeetsTheHypothesis`: with the five premises proved. 

### `theRecursionMeetsTheHypothesisFrom`

 How: from Theorem B, «We may and do assume …» and Theorem A (b), all in counted operations, and
the clauses on numbers. 

### `theRecursionMeetsTheHypothesis`

 **«The pairs (K_ℓ, e_ℓ) of (40), for the pieces of Appendix B, satisfy this hypothesis»**, in
counted operations, for the named machine. 
