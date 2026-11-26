---
{
  "module": "proof/networks/Eight/SecCrossing_LemPieces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_LemPieces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_LemPieces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 2 from the eight-square identity, without hypotheses

The files of proof/networks/Eight/ imported here prove the parts of the section «Two crossing
equalities as a sum of ⌈λ/3⌉ + 1 cheaper functions»; where a part uses another one, it takes it as a
hypothesis. Here the hypotheses are filled in. The order is that
of the paper: the sign rule (`signs`, SecCrossing_Identity.lean) gives R + C = 2[x = v][y = u],
which gives part (a); the factorizations of R and C through 3 bits give part (b) (`stFact`, for the
functions `fTop`, `fBot` of the
paper's proof); part (c) is arithmetic. 

### `stFact`

 Lemma 2(b) for the functions of the paper's proof, θ = (Q, θ'), with the factorization through
2λ bits wherever the other one would need more. 

### `lemPieces`

 **Lemma 2**, parts (a), (b), (c), as in the paper but without the claims «computable in time
poly(λ)». 
