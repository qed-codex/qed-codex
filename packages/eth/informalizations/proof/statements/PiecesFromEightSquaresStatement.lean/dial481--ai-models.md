---
{
  "module": "proof/statements/PiecesFromEightSquaresStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/PiecesFromEightSquaresStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/PiecesFromEightSquaresStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Appendix A: the pieces of Lemma 2 are pieces with parameters (11/12, c)

Definitions and statements only. The functions A_0, …, A_t, the numbers t, c^row_i, c^col_i are
those of `EightSquareStatement.lean` (namespace `Eight`); the programs for the two factorizations
(`Eight.eightF`) and for the
values (`Eight.aMul`) are those of `proof/networks/Eight/SecCrossing_PolyDefs.lean`. «Pieces with
parameters (ρ, c)» is `AppRunningTime.IsPieces` of `AppRunningTimeStatement.lean`, which also says
how «within T operations» is rendered. 

### `valEight`

 The program for the value of a piece of Lemma 2, as a function of (pad, (λ in unary, number i of
the piece), (x, y, u, v)). It uses neither the pad nor λ. 

### `LemPiecesPieces`

 The sentences after the definition of pieces: «By Lemma 2, the functions A_0, …, A_t of
Definition 5 are pieces with parameters (11/12, c), with 𝓘 = {0, …, t}, d = 2^t and the numbers
c^row_i, c^col_i defined there, for which
c^row_i + c^col_i ≤ 11λ/3 + 8. This holds for every integer c ≥ 8 such that 2^{cλ} exceeds the
polynomial running times in Lemma 2 for all λ ≥ 1.» Here it holds for every c ≥ 8: the programs are
polynomial-time and have
no loop that a pad cuts off, so the second condition on c does not occur. 
