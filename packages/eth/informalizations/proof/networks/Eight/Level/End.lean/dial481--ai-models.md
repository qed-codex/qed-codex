---
{
  "module": "proof/networks/Eight/Level/End.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Level/End.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Level/End.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 2 from the eight-square identity, in the form that the networks of a grid need

The files of proof/networks/Eight/Level/ take the interface statements of
proof/networks/Eight/Level/Defs.lean as hypotheses. Here one of them, `Level.StPieces`, is derived
from Lemma 2 (`Eight.lemPieces` and `Eight.stFact` of
proof/networks/Eight/SecCrossing_LemPieces.lean), with ρ = 11/12 (`Eight.rho`) and t = ⌈λ/3⌉
(`Eight.tOf`). 

### `stPieces`

 Lemma 2 in the form that the networks of a grid need. 
