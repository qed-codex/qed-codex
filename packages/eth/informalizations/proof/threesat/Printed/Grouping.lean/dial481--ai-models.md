---
{
  "module": "proof/threesat/Printed/Grouping.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/Grouping.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/Grouping.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 1 from Definition 4

The pieces come from proof/threesat/Printed/GroupingProcs.lean (`stOnProcedures`),
GroupingEntry.lean (`stEntryCost`), GroupingRun.lean (`stGroupingTiedOf`), GroupingPoly.lean
(`stGroupingPoly`). Here they are put together.
* `stGroupingTied_of`: Lemma 1 for the algorithm of its proof, from three statements proved in other
  folders: «a good grouping exists … fix the first good one» (`Eight.ViaGrouping.StSearch`), the run
  of the search (`Exits.StSearchStops`) and «so the value equals Z» (`Value.StValueEqualsZ`);
* `groupingLemma_of`: **Lemma 1** as printed, from the form for the named machine. 

### `stGroupingTied_of`

 Lemma 1 for the algorithm of its proof, from a proof of «a good grouping exists … fix the first
good one», the run of the search and «so the value equals Z». 

### `groupingLemma_of`

 **Lemma 1**, from the form for the named machine: the machine is `groupingMachine K (3K⁸) M`,
for a machine M that witnesses that (K, e) is achievable. 
