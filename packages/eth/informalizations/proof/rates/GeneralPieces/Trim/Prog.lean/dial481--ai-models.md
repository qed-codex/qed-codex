---
{
  "module": "proof/rates/GeneralPieces/Trim/Prog.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Trim/Prog.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Trim/Prog.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Pieces as programs: the values of the pieces

Lemmas on the pieces with parameters (ρ, c) of Appendix A when they are given as programs (the
definitions `valF` and `Realizes` are in `DefGenPieces/Progs.lean`). In the paper an algorithm
computes the values of the pieces
(part (c) of the definition). Pieces as programs have no program for the values, so `valF` adds up
P's own factorization, top·bot, over all words of P's number of bits, on a pad that is long enough
for this loop.

`valF_eq_sum` says that `valF` is this sum; `valF_eq` says that, for programs that realize functions
A, it is the value of the piece, from either factorization. 

### `exists_bitsOf`

 Every word of n bits is the word of a function. 

### `valF_eq_sum`

 If the pad is long enough for the loop, `valF` is the sum of top·bot over all words of `cap`
bits. 

### `valF_eq`

 For part (c) of the definition of pieces (one algorithm computes every value of the A_i): when
the pad is long enough, `valF` is the value of the piece, from either
factorization. 
