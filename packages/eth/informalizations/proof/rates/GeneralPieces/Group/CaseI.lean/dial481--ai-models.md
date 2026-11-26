---
{
  "module": "proof/rates/GeneralPieces/Group/CaseI.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Group/CaseI.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Group/CaseI.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The lemma on groupings with explicit cost: case (i)

The proof of Lemma 8 first shows that some grouping has at most 2g/K nodes in every group and Y ≤ L
for all γ ≠ γ'. In case (i) this is shown in the proof of Lemma 1, by Chebyshev's inequality for
independent uniform χ(a): that is `Groundwork.Colouring.exists_colouring`, restated here with the
letters of Appendix A (`GeneralPieces.caseI`). It gives fewer than 2g/K nodes in every group. 

### `caseI`

 Case (i): g = 3K⁸ and ζ = 1/(2K). If the numbers c_{a,b} are symmetric and every node shares at
most P bits in all, some grouping has fewer than 2g/K nodes in every group and
Y ≤ (U + 2ζgP)/K² = (U + gP/K)/K² for any two groups. The proof is
`Groundwork.Colouring.exists_colouring`, which has a natural number P; a real P is rounded down. 
