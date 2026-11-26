---
{
  "module": "proof/networks/SingleBitPieces/SecCrossing_PolyA.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/SingleBitPieces/SecCrossing_PolyA.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/SingleBitPieces/SecCrossing_PolyA.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A closure lemma for certificates of polynomial time, used for Lemma 2(a)
This file lies beside files for a variant of Lemma 2 whose pieces are made from single bits (ρ =
(log 12)/4), but its lemma serves the paper's own pieces of Lemma 2 as well.
«Computable in time poly(λ)» is rendered as a certificate `Groundwork.PolyT` (some Turing machine of
the model used here computes the function in time polynomial in the length of its input). The
statement here, `unary_min_right`, says that the smaller of a polynomial-time number and a number
given in unary is again given in unary.

It lies in the namespace `SingleBitPieces.SecCrossing_PolyA`. 

 ### The closure lemma 

### `unary_min_right`

 The smaller of any number and a number given in unary is given in unary. 
