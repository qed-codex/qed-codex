---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem17/ClassStarts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/ClassStarts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/ClassStarts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Pure facts about the starts of the classes and the table of chunks

Proof of Theorem 17.  The `n²` pairs `(a, b)` are listed class after class, where the class
of a residue `ϱ < p` holds the pairs whose weight is congruent to `ϱ` modulo the prime `p`, and each
class is cut into chunks of at most `cap` pairs.  The list of the starts of the classes has `p + 1`
entries, none above `n²`; the table of chunks has at most `n² + p` entries.


### `length_classStarts`

 The list of the starts of the classes has one entry for each residue, and one more for the
end. 

### `classStart_le_sq`

 A class starts at a place of the list of all n² pairs, or at its end. 

### `le_of_mem_classStarts`

 No entry of the list of the starts of the classes is above n². 

### `length_chunkTab_le_add`

 If `cap ≥ 1` and every residue is below `p`, the table of chunks has at most `n² + p` entries.
This is the number of cells that the host procedure of Theorem 17 reserves for each of its three
components. 
