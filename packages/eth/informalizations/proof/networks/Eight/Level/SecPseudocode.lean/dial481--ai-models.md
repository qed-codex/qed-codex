---
{
  "module": "proof/networks/Eight/Level/SecPseudocode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Level/SecPseudocode.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Level/SecPseudocode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The choice of the level in the header of Algorithm 1, for the pieces of Lemma 2 from the eight-square identity

Algorithm 1 of Section 8 of the paper, for the pieces of Lemma 2 from the eight-square identity.
Procedure CLIQUE of Algorithm 1 is defined in proof/networks/Eight/Level/Defs.lean as
`Eight.Level.levelAlg`, the algorithm for one level that works with the functions A_0, …, A_t, t =
⌈λ/3⌉, of
`EightSquareStatement.lean` and ends with the division by 2^{t|ℛ|}: lines 16 and 19 of Algorithm 1
read «for each function ι : ℛ → {0, …, ⌈λ/3⌉}» and «return sum / 2^{⌈λ/3⌉|ℛ|}».
This file holds the choice of the level as in the header of Algorithm 1: the first ℓ with K_ℓ ≥
72/δ' and e_ℓ ≤ δ'/12, for the e_ℓ of Section 8 with ρ = 11/12 (`Eight.Level.levelE`):
`exists_first`, `firstLevel`, `firstLevel_spec`. 

 ## The choice of the level 

### `exists_first`

 Some level has K_ℓ ≥ 72/δ' and e_ℓ ≤ δ'/12. 

### `firstLevel`

 Header of Algorithm 1: «ℓ is the first level with K_ℓ ≥ 72/δ' and e_ℓ ≤ δ'/12». Same as in the
paper. 

### `firstLevel_spec`

 The first level is such a level. 
