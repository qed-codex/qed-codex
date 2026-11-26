---
{
  "module": "proof/networks/SingleBitPieces/Level/Arith.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/SingleBitPieces/Level/Arith.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/SingleBitPieces/Level/Arith.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The arithmetic of the cost of a level: the sizes [This file works with a form of Lemma 2 whose pieces differ from those the paper prints, with ρ = (log 12)/4 in place of the paper's ρ = 11/12.]

Section 5 of the paper, proof of Proposition 3, «Cost». `level_size`: the sizes that occur in the
loop over the terms add up to a polynomial in sc + B + λ; the paper counts operations only and has
no such bound. 

### `level_size`

 Section 5, proof of Proposition 3, «Cost», the sizes: the sum of the sizes that occur in the
loop over the terms is polynomial in sc + B + λ. Not in the paper, which counts operations only. 
