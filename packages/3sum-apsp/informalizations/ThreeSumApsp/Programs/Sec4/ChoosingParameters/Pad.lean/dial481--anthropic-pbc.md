---
{
  "module": "ThreeSumApsp/Programs/Sec4/ChoosingParameters/Pad.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Pad.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Pad.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Padding X with zero columns

Proof of Corollary 26: "pad the inner dimension to 4^m < 4D with zero columns of X". Row by row: a
copy of the row and a fill with zeros. The invariant `PadX.Rows` says that the first i rows of the
padded matrix have been written; `PadX.Rows.succ` is what a round does to the memory, and
`padX_meets` the specification.


### `Height`

 The local variables of padX: the arguments N, D, D', aX, aX', the row, and a result that is not
used. 

### `padXBody`

 padX(N, D, D', aX, aX'): for each row i, copy its D entries from aX + i D to aX' + i D', and
fill the D' - D cells behind them with zeros. 

### `Rows`

 The memory before row i: the first i rows of the padded matrix stand at aX', and no cell outside
them has changed. 

### `Rows.succ`

 A round: row i of X has been copied, and zeros have been written behind it. 
