---
{
  "module": "proof/networks/SingleBitPieces/SecProof_Cost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/SingleBitPieces/SecProof_Cost.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/SingleBitPieces/SecProof_Cost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 6 of the paper, paragraph «Cost», with the constants of the paper (This folder uses, in Lemma 2, pieces made from single bits, with ρ = (log 12)/4, which the paper does not print.)

The paper takes e = δ'/12 and K ≥ 72/δ'. With these constants, `network_exponent_le` is the display
of the paragraph «Cost», and `network_exponent_le'` its bound ¾δ'm + δ'g. 

### `network_exponent_le`

 **Section 6, «Cost».** «With e = δ'/12, K ≥ 72 and 1/K ≤ δ'/72, the exponent in Lemma 1 is eU +
e·gP/K + 2gP/K < ½δ'm + (1/144)δ'(m + g) + (1/6)δ'(m + g) = (97/144)δ'm + (25/144)δ'g.» Same as in
the paper, except that
the inequality is not strict, because U ≤ 6m here (the paper: U < 6m). K ≥ 72 follows from K ≥ 72/δ'
and δ' ≤ 1. 

### `network_exponent_le'`

 «… ≤ ¾δ'm + δ'g.» 
