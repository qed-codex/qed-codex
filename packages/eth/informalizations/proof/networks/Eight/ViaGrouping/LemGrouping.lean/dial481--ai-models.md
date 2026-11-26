---
{
  "module": "proof/networks/Eight/ViaGrouping/LemGrouping.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/LemGrouping.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/LemGrouping.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 1 along the printed proof: the bound on steps

The steps of the proof are proved in the files imported here: «A good grouping exists» and the
search (Search.lean), the tables W̃_γ, their bound, the cost of an entry and «the value equals Z»
(Table.lean), the paragraph «Cost»
(Main.lean), polynomial-time steps (Keeps.lean). This file puts them together into a bound on the
steps of the algorithm of the proof (`stLemGrouping`); that these steps take polynomial time is
`stKeeps`. Display.lean, which nothing here imports, says that what `tableM` returns is the display
of W̃_γ in the paper. 

### `stLemGrouping`

 **Lemma 1 for the algorithm of its proof**: if E evaluates (K, λ)-cliques with the exponent e,
then `netAlg K (3K⁸) E` evaluates networks on [3K⁸] with the exponent e(U + gP/K) + 2gP/K. A bound
on steps; that the steps take polynomial time is `stKeeps`. 
