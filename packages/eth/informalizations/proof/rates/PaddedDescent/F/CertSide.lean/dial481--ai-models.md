---
{
  "module": "proof/rates/PaddedDescent/F/CertSide.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/CertSide.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/CertSide.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The row network or the column network of the proof of Proposition 3 (Section 5), read off an
explicit table (`sideF`), is polynomial-time: the lengths of its states and
labels are given in unary, and its weights and factors are polynomial-time functions of the context
and the query (`stCertSide`, which
proves the interface statement `StCertSide`). The side g of the grid, the label length ℓ and the pad
are data, in unary. The flag tr (rows
or columns merged) is data too: each certificate is proved for a fixed tr, and the two cases are
joined at the end (`boolCases`). 

### `boolCases`

 A function with a truth value as a parameter is polynomial-time in that parameter too, if it is
for both of its values. 

### `boolCasesU`

 The same for lengths given in unary. 

 ### Positions in the words of the grid, with g as data 

 ### One rectangle under fuel 

 ### The weights and the factors 

 ### The network 

### `stCertSide`

 The row or column network of Proposition 3, read off an explicit table, keeps polynomial time:
lengths in unary, weights and factors polynomial-time. 
