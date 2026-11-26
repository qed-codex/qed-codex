---
{
  "module": "proof/maintheorem/MainRoute/GeneralMain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MainRoute/GeneralMain.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MainRoute/GeneralMain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The chain for every solver: the end theorem

`routeOnEverySolver`: `routeOn_of` (General.lean) with the theorems of
proof/variables/RecursionToBound, proof/variables/PairsToBound and proof/maintheorem/MinOfBounds in
the places of its hypotheses. Neither the pieces of Appendix B nor the recursion of Appendix A
enters it. `bothBoundsOnEverySolver`: with the bound in m for every solver (`boundInMOnEverySolver`,
GeneralInM.lean), which takes from proof/rates/GeneralPieces the top level in m for a general
sequence of levels. 

### `routeOnEverySolver`

 **The chain for every solver.** From any polynomial-time algorithm for cliques with a sequence
of levels, a computed number in [e_ℓ, 2e_ℓ] and e_ℓ = O((log K_ℓ)^(−1/2)), and any function with the
bound in m, every machine assembled in the printed way has the bound of the Main Theorem, and such a
machine exists. 

### `bothBoundsOnEverySolver`

 **Both bounds from ONE algorithm for cliques.** For every polynomial-time algorithm for cliques
with a sequence of levels, a computed number in [e_ℓ, 2e_ℓ] and e_ℓ = O((log K_ℓ)^(−1/2)): every
machine that computes the function for the bound in m on it meets the bound in m, and every machine
assembled in the printed way from machines that compute the function of Steps 1 to 5 and the
function for the bound in m, both on it, and exhaustive counting has the bound of the Main Theorem. 
