---
{
  "module": "proof/networks/SingleBitPieces/SecNetworks_LemGrouping.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/SingleBitPieces/SecNetworks_LemGrouping.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/SingleBitPieces/SecNetworks_LemGrouping.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The exponent of Lemma 1 in two forms: e·U + (e + 2)·gP/K = e(U + gP/K) + 2gP/K

The paper's Lemma 1 has the exponent e(U + gP/K) + 2gP/K, for every e ≥ 0. `exponent_eq` shows that
it equals e·U + (e + 2)·gP/K. 

### `exponent_eq`

 The exponent e·U + (e + 2)·gP/K equals the paper's exponent e(U + gP/K) + 2gP/K of Lemma 1. 
