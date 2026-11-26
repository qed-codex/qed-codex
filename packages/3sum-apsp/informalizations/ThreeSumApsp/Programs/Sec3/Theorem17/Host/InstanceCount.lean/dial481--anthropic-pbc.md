---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Host/InstanceCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/InstanceCount.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/InstanceCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The number of instances of the host of Theorem 17

Proof of Theorem 17: "There are at most 2√D h ≤ 2√D(ng/s + 1) ≤ 4ng instances", where `s = ⌊√D⌋` and
`h` is the number of pieces.  The host's table of chunks has as many entries as the paper's count of
the chunks (`length_chunkTab_eq_totalChunks`), and its number of pieces is the paper's
(`numPiecesNat_eq`), so the bound of `TriangleInstance.card_instanceIndices_le` applies.


### `HostData.m_le`

 Proof of Theorem 17: "There are at most 2√D h ≤ 2√D(ng/s + 1) ≤ 4ng instances".  Here `m` is the
number of instances of the host. 
