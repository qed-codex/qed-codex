---
{
  "module": "proof/networks/Value/End.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Value/End.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Value/End.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «… so the value equals Z»

Proof of Lemma 1, end of the paragraph «The algorithm». The value of the clique of the groups, as
the network of Definition 3 with two copies of the string on every edge, is
1. a sum over one string per edge of the product of the tables (`StCliqueValue`, the sentence after
   Definition 3);
2. a sum over all z ∈ ∏ S_a and over one string θ_{a,b} per pair {a, b} of nodes in different groups
   (`StJointSum`);
3. after the sum over each θ_{a,b}, the sum that defines Z (`StSumOut`).
`stValueEqualsZOf` puts the three together, `stValueEqualsZ` is the sentence. `stValueOf` and
`stValue` give the step in the form `Eight.ViaGrouping.StValue`, in which the proof of Lemma 1 in
proof/networks/Eight/ViaGrouping takes it. 

### `stValueEqualsZOf`

 «so the value equals Z», from the sentences before it. 

### `stValueEqualsZ`

 **«… so the value equals Z»**: the clique of the groups, as the network of Definition 3, has the
value of the network N. 

### `stValueOf`

 From «so the value equals Z» for the clique as a network to the form with one string per edge
and the tables `Paper.groupedTables`: back by the sentence after Definition 3, and the tables are
given by the display of W̃_γ. 

### `stValue`

 «… so the value equals Z», in the form in which the proof of Lemma 1 takes the step. (A
different declaration from the theorem of the same name in `Eight.ViaGrouping`; it is proved here
without using that theorem.) 
