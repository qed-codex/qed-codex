---
{
  "module": "proof/consequences/ThmCount/Remark.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/ThmCount/Remark.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/ThmCount/Remark.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The closing remark of Appendix C: «with it the time becomes 2^{O(n(log log n)^{2/3}/(log n)^{α/3})}», as a sentence

The sentence is that of the paper, with α = 1/2. `stRemarkTime` is `stRemarkTime_of`
(proof/consequences/ThmCount/Main.lean) applied to Theorem D(b)
(`RecursionWithPieces.Forms.thmVariablesB`). It is not the remark's own derivation of the time: the
sentence is weaker than Theorem D(b) at k = 3 and follows from it by comparing the rates. 

### `stRemarkTime`

 One deterministic algorithm computes the number of satisfying assignments of a 3-CNF on n ≥ 4
variables in time 2^{O(n·(log log n)^{2/3}/(log n)^{1/6})}: the statement `ThmCount.StRemarkTime`. 
