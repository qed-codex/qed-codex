---
{
  "module": "proof/rates/PaddedDescent/F/ArithStack.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithStack.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithStack.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The stack of the walk fits under the pad (the last part of `StAW`)

The depth-first walk through the sparsification tree for clauses of width k keeps a stack of
formulas; `stackLen k τ n m` bounds the length of the word of its state (stack and flag) when
the formula at the root has at most m clauses. Here: for τ = `tauOf (sOf n)`,
`sOf n` ≥ `s0K k` and m = `inLen k n` this is at most 2^(n/2^(sOf n) + 1), hence below the length of
the pad (`stackLen_le`). The degree of `stackLen` in n grows with k; it is
paid for because k ≤ sOf n is far below Y = `Ytop (sOf n)`: whatever is at most n^e with e ≤ Y is
below the pad (`le_pad_of_le_pow`). 

 ### Polynomials in n are below the pad 

### `nine_size_le`

 9·size n + 30 ≤ n/2^(sOf n) when sOf n ≥ 1. 

### `le_pad_of_le`

 Whatever is at most 2^30·(2^size n)^9, for instance 2^30·n^9, is below the pad. 

### `mul_size_le`

 e·size n ≤ n/2^(sOf n) for every e ≤ Y = Ytop (sOf n), when sOf n ≥ 1. 

### `le_pad_of_le_pow`

 Whatever is at most (2^size n)^e with e ≤ Y = Ytop (sOf n), for instance n^e, is below the pad. 

### `betaOf_lt_Ytop`

 4β + 10s + 1000 < Y. 

### `two_pow_betaOf_le`

 2^(4β + 10s + 1000) ≤ n for s = sOf n ≥ 1. 

### `clause_word_le`

 k·(3n + 5) + 10 ≤ a³ if n < a, k < a and 4 ≤ a. 

### `inLen_le_pow`

 `inLen k n` ≤ a^(k+4) if n < a and 2^(k+1) ≤ a. 

### `stackLen_le_two_pow`

 With a = 2^z, n < a, bsum τ k ≤ a, 2^(k+1) ≤ a and 16 ≤ a: `stackLen k τ n (inLen k n)` ≤
a^(k+12). 

### `stackLen_le`

 The last part of `StAW`: the stack of the walk for width k fits under the pad. 
