---
{
  "module": "proof/consequences/CircuitLowerBound/Cert/Sched.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Cert/Sched.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Cert/Sched.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): the chains are computed in polynomial time

From m in unary, in polynomial time: the number `nu m` of the chain of m, its table `codeOf (nu m)`,
the next number of the chain, whether m stands before or at the last place of its chain, and
whether a table has room (`stCertSched`). The last place 2^2^2^a of chain a is never computed: it is
compared with s through two binary logarithms of s (`top_le_iff`). 

 ### Comparison with the last place of a chain 

### `leTop`

 «2^2^2^a ≤ s», by two logarithms. 

### `top_le_iff`

 The program decides «the last place of chain a is at most s». 

### `lt_top_iff`

 «s comes before the last place of chain a». 

### `eq_top_iff`

 «s is the last place of chain a»: it is at most s and not at most s − 1. 

 ### Certificates 

### `nu_unary`

 The number of the chain is given in unary. 

### `pos_polyT`

 The place of m in its chain. 

### `next_polyT`

 The next number of the chain. 

### `leTop_polyT`

 The comparison with the last place of chain a, for a in unary. 

### `ones_polyT`

 The number of ones at the start of a word. 

### `rest_polyT`

 The word after its first ones and the zero that ends them. 

### `fld_polyT`

 A number of W bits in a word. 

### `litOf_polyT`

 Five numbers of a word as a literal of a table. 

### `codeOfWord_polyT`

 The table written by a word. 

### `codeOf_polyT`

 The table with the number a. 

### `kb_polyT`

 The three components of a table. 

### `bt_le`

 A time has at most L bits. 

### `bt_unary`

 The number of bits of a time is given in unary if L is. 

### `fits_polyT`

 «There is room». 

### `stCertSched`

 The chains are computed in polynomial time from m in unary. 
