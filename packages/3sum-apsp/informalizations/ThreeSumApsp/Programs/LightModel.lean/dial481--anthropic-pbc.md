---
{
  "module": "ThreeSumApsp/Programs/LightModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/LightModel.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/LightModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# "Is solved in time T", read as a statement about programs of the light language

The light language (`Light.Stmt`, `Light.Program`) is a small language with assignments to numbered
locals, loads and stores, `if`, `while` and calls of numbered procedures; a compiler turns its
programs into programs of the word RAM.

The deductions between running-time claims are made for an arbitrary reading `M : DetTimeModel` of
the sentence "is solved by a deterministic algorithm in time T".  Here the sentence is read as: some
procedure of some program of the light language solves the task within that many steps, and its need
(`Light.Need`: the largest number that it forms, the cells that it uses, the depth of its calls) is
polynomially bounded.


### `lightModel`

 The reading of "is solved in time T" by programs of the light language. 
