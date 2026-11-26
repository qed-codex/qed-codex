---
{
  "module": "proof/variables/VariableBound/Net/CertRank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/CertRank.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/CertRank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 3 of Appendix D: the position of a string is found in polynomial time

In Step 3 of Appendix D, counting marks, multiplying powers of 2 and finding the position of a
string among those with as many ones take τ = n^O(1) operations. Proved here (`stCertRank`):
binomial coefficients of numbers given in
unary, the position `rank` of a string, and the number `cw` = ⌈log C(t, μ)⌉ of bits of a position,
in unary, are polynomial-time (`PolyT`, `Unary`).
The position is computed by a fold from the right whose state is the part of the string read so far
together with its position. 

### `stepR`

 One step of the fold: put the bit b in front of the string c.1, whose position is c.2. 

### `foldr_stepR`

 The fold yields the string and its position. 

### `stepR_polyT`

 One step of the fold is polynomial-time. 

### `len_rank_le`

 The word of the position of a string is at most as long as the word of the string. 

### `rank_polyT`

 The position of a string among the strings of its length with as many ones is polynomial-time. 

### `choose_min`

 C(t, μ) does not change if μ is cut off at t + 1. 

### `stCertRank`

 Step 3 of Appendix D: binomial coefficients C(t, μ) are polynomial-time for t and μ given in
unary; the position of a string among those with as many ones is polynomial-time; and ⌈log C(t, μ)⌉
is
given in unary for t given in unary and μ polynomial-time. 
