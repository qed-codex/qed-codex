---
{
  "module": "Zeta23/MV/Final.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/MV/Final.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/MV/Final.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The Montgomery–Vaughan weighted Hilbert inequality

`eigen_bound` (`Zeta23/MV/Eigen.lean`) is exactly `EigenBound 13`; the spectral reduction of
`Duality.lean` turns it into `MVDiag 13` and, via polarization (`Zeta23/MV.lean`), into the
bilinear `∃ C > 0, MVHilbert C` of `Hypotheses.lean` (C = 26) — discharging `PaperInputs.MV`.


### `mvDiag_thirteen`

 **`MVDiag 13`** — the weighted Hilbert inequality, literature (diagonal) form. 

### `mv_hilbert`

 **H-MV:** `∃ C > 0, MVHilbert C` (the field `PaperInputs.MV`). 
