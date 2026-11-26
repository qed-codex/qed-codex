---
{
  "module": "proof/rates/PaddedDescent/Col/Good.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Col/Good.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Col/Good.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The search for a colouring succeeds on few nodes

`PaddedDescent.F.goodG` compares the label bits between two classes with a bound β given as an
argument; it is a variant of the test `goodB`, whose bound is computed from the network and contains
the error term of a colouring lemma.
`goodG_iff` says what the test means, and `exists_goodG` that some colouring among the
K^g passes it, if no two nodes share more than M label bits, 4·D²·m·K ≤ g, (g+2)·K < 2^m and U +
3g²M/D ≤ K²·β. 

### `goodG_iff`

 What the test says: every class has fewer than 2g/K nodes, and two classes share at most β label
bits. 

### `exists_goodG`

 Some colouring among the K^g passes the test. 
